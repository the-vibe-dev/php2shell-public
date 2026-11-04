"""Validate the selected public export; never execute private research or contact targets."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

from review_results import validate_results

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = set("""
.gitignore
.github/ISSUE_TEMPLATE/research-access.md
.github/workflows/public-review.yml
README.md
RESEARCH_ACCESS.md
SECURITY.md
LICENSE.md
CITATION.cff
PUBLICATION_REVIEW.md
VALIDATION.md
audit/AUDIT_SUMMARY.md
audit/audit_summary.json
assets/php2shell-hero.svg
assets/mechanism-map.svg
docs/technical-report.md
docs/application-results.md
docs/negative-results.md
docs/evidence-and-counting.md
docs/remediation.md
docs/references.md
docs/defanging-methodology.md
data/README.md
data/results.json
data/related-results.json
data/version_matrix.csv
data/application_matrix.csv
pocs/README.md
pocs/offline_models.py
pocs/php_config_review.php
scripts/review_results.py
scripts/validate_publication.py
tests/test_public_edition.py
""".split())


def audit_model_source(source: str) -> None:
    """Reject capabilities unnecessary for the abstract offline Python models."""
    allowed_imports = {"__future__", "dataclasses", "json"}
    forbidden_calls = {
        "eval", "exec", "compile", "__import__", "open", "getattr", "setattr",
        "delattr", "breakpoint", "system", "popen", "Popen", "run", "call",
        "check_call", "check_output", "write_bytes", "write_text",
    }
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names = {item.name.split(".")[0] for item in node.names}
            if not names <= allowed_imports:
                raise ValueError("unapproved model import")
        if isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            if root not in allowed_imports:
                raise ValueError("unapproved model import")
        if isinstance(node, ast.Name) and node.id in {"__builtins__", "__loader__"}:
            raise ValueError("dynamic model runtime access")
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            raise ValueError("model introspection is not needed")
        if isinstance(node, ast.Call):
            name = (
                node.func.id if isinstance(node.func, ast.Name)
                else node.func.attr if isinstance(node.func, ast.Attribute)
                else ""
            )
            if name in forbidden_calls:
                raise ValueError("forbidden model capability")


def validate_audit(summary: dict) -> None:
    expected = {
        "schema_version", "audit_completed", "private_commit_reviewed",
        "private_poc_files_reviewed", "private_audit_ledger_sha256",
        "risk_buckets", "dispositions", "private_source_files_copied_to_public_tree",
        "method",
    }
    if set(summary) != expected:
        raise ValueError("unexpected audit-summary schema")
    if summary["schema_version"] != 1:
        raise ValueError("unsupported audit-summary schema")
    if summary["private_commit_reviewed"] != "ff7ef13d69748110a5329af5228aff2d5a7e4a98":
        raise ValueError("unexpected private source snapshot")
    if summary["private_poc_files_reviewed"] != 350:
        raise ValueError("private PoC audit count mismatch")
    if summary["private_source_files_copied_to_public_tree"] != 0:
        raise ValueError("private source copied into public tree")
    if not re.fullmatch(r"[0-9a-f]{64}", summary["private_audit_ledger_sha256"]):
        raise ValueError("invalid private audit ledger digest")
    buckets = summary["risk_buckets"]
    if set(buckets) != {"high", "medium", "low"} or sum(buckets.values()) != 350:
        raise ValueError("risk bucket totals mismatch")
    dispositions = summary["dispositions"]
    wanted = {
        "EXCLUDE_OPERATIONAL_OR_DUAL_USE_SOURCE",
        "EXCLUDE_RAW_CONFIGURATION_OR_RECEIPT",
        "EXCLUDE_PRIVATE_RESEARCH_NOTE",
    }
    if set(dispositions) != wanted or sum(dispositions.values()) != 350:
        raise ValueError("disposition totals mismatch")
    for mapping in (buckets, dispositions):
        if any(type(value) is not int or value < 0 for value in mapping.values()):
            raise ValueError("audit totals must be nonnegative integers")


def review_tree(root: Path = ROOT) -> dict:
    paths: dict[str, Path] = {}
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in {".git", "__pycache__", "verification-output"} for part in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"symlink not allowed: {rel}")
        if path.is_file():
            paths[rel.as_posix()] = path

    names = set(paths)
    if names != REQUIRED:
        raise ValueError(f"allowlist mismatch: extra={sorted(names-REQUIRED)}, missing={sorted(REQUIRED-names)}")

    contents: dict[str, str] = {}
    hashes: dict[str, str] = {}
    secret_patterns = [
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"\bAKIA[0-9A-Z]{16}\b",
        r"\bgh[pousr]_[A-Za-z0-9]{30,}\b",
        r"\bgithub_pat_[A-Za-z0-9_]{30,}\b",
    ]

    for name, path in paths.items():
        raw = path.read_bytes()
        if len(raw) > 100_000 or b"\x00" in raw:
            raise ValueError(f"binary/oversized public file: {name}")
        text = raw.decode("utf-8")
        if any(re.search(pattern, text) for pattern in secret_patterns):
            raise ValueError(f"credential-shaped content: {name}")
        contents[name] = text
        hashes[name] = hashlib.sha256(raw).hexdigest()

        if name.endswith(".json"):
            json.loads(text)

        if name.endswith(".md"):
            targets = re.findall(r"\]\(([^\s)]+)\)", text)
            targets += re.findall(r'(?:src|href)="([^"]+)"', text)
            for target in targets:
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    raise ValueError(f"broken/outside relative link: {name}: {target}")

        if name.endswith(".svg"):
            svg = ET.fromstring(text)
            for element in svg.iter():
                local = element.tag.rsplit("}", 1)[-1]
                if local in {"script", "foreignObject", "image"}:
                    raise ValueError(f"active/external SVG element: {name}")
                for key, value in element.attrib.items():
                    attr = key.rsplit("}", 1)[-1]
                    if attr.lower().startswith("on"):
                        raise ValueError(f"event handler in SVG: {name}")
                    if attr in {"href", "src"} and not value.startswith("#"):
                        raise ValueError(f"external SVG reference: {name}")

    audit_model_source(contents["pocs/offline_models.py"])

    php = contents["pocs/php_config_review.php"]
    if "PHP_SAPI !== 'cli'" not in php:
        raise ValueError("PHP diagnostic must reject web execution")
    if re.search(
        r"\b(?:eval|exec|system|shell_exec|passthru|proc_open|popen|unserialize|curl_exec|fsockopen|file_get_contents|file_put_contents|ini_set)\s*\(",
        php,
        re.I,
    ):
        raise ValueError("operational capability in PHP diagnostic")

    results = json.loads(contents["data/results.json"])
    totals = validate_results(results)

    versions = list(csv.DictReader(contents["data/version_matrix.csv"].splitlines()))
    wanted_versions = [(p["branch"], p["vulnerable"], p["core_fixed"]) for p in results["version_pairs"]]
    if [(p["branch"], p["vulnerable"], p["core_fixed"]) for p in versions] != wanted_versions:
        raise ValueError("version CSV/JSON mismatch")

    apps = list(csv.DictReader(contents["data/application_matrix.csv"].splitlines()))
    wanted_apps = [(p["name"], p["version"], p["interface"]) for p in results["applications"]]
    if [(p["name"], p["version"], p["interface"]) for p in apps] != wanted_apps:
        raise ValueError("application CSV/JSON mismatch")

    related = json.loads(contents["data/related-results.json"])
    if set(related) != {"evidence_status", "runtime_reproduced_for_public_edition", "note", "records"}:
        raise ValueError("related-results schema mismatch")
    if related["runtime_reproduced_for_public_edition"] is not False:
        raise ValueError("related results must not claim fresh runtime reproduction")
    if len(related["records"]) != 20 or len({r["id"] for r in related["records"]}) != 20:
        raise ValueError("related-results count mismatch")
    for record in related["records"]:
        if set(record) != {"id", "study", "outcome", "original_sha256"}:
            raise ValueError("related-results field mismatch")
        if not re.fullmatch(r"[0-9a-f]{64}", record["original_sha256"]):
            raise ValueError("related-results digest mismatch")

    audit = json.loads(contents["audit/audit_summary.json"])
    validate_audit(audit)

    return {
        "status": "PASS",
        "checked_files": len(paths),
        "selected_counts": totals,
        "private_poc_files_audited": audit["private_poc_files_reviewed"],
        "private_source_files_copied": audit["private_source_files_copied_to_public_tree"],
        "runtime_reproduced": False,
        "public_file_sha256": dict(sorted(hashes.items())),
    }


def main() -> int:
    try:
        result = review_tree()
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
