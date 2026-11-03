"""Check published summary arithmetic; this does not verify private experiments."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate_results(data: dict) -> dict[str, int]:
    expected = {"schema_version", "as_of", "evidence_status", "runtime_reproduced_for_public_edition", "counting_rule", "counts", "cohorts", "mechanisms", "version_pairs", "applications"}
    if not isinstance(data, dict) or set(data) != expected:
        raise ValueError("unexpected public result schema")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("unsupported schema")
    if data["runtime_reproduced_for_public_edition"] is not False:
        raise ValueError("public checks are not original runtime reproductions")
    if data["evidence_status"] != "derived_summary_of_retained_research_records":
        raise ValueError("evidence status must identify the derived summary")
    if not data["counting_rule"] or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", data["as_of"]):
        raise ValueError("missing counting rule or date")
    cohorts = data["cohorts"]
    if len(cohorts) != 3 or len({c["id"] for c in cohorts}) != 3:
        raise ValueError("expected three unique selected cohorts")
    totals = {"target_effects": 0, "negative_controls": 0}
    for c in cohorts:
        if set(c) != {"id", "name", "target_effects", "negative_controls", "basis", "original_record", "original_sha256"}:
            raise ValueError("unexpected cohort field")
        if not re.fullmatch(r"[0-9a-f]{64}", c["original_sha256"]):
            raise ValueError("malformed source digest")
        if not c["basis"] or not c["original_record"]:
            raise ValueError("cohort needs counting basis and provenance")
        for field in totals:
            value = c[field]
            if type(value) is not int or value < 0:
                raise ValueError("counts must be nonnegative integers, not booleans")
            totals[field] += value
    if set(data["counts"]) != set(totals) or any(type(v) is not int for v in data["counts"].values()) or totals != data["counts"]:
        raise ValueError("published totals do not match selected cohorts")
    if len(data["mechanisms"]) != 5 or len({m["id"] for m in data["mechanisms"]}) != 5:
        raise ValueError("expected five unique mechanism families")
    for m in data["mechanisms"]:
        if set(m) != {"id", "name", "related_cves", "recorded_outcome", "limitation"} or not m["limitation"]:
            raise ValueError("mechanism schema or proof limit missing")
    pairs = data["version_pairs"]
    if len(pairs) != 4 or len({p["branch"] for p in pairs}) != 4:
        raise ValueError("expected four unique branch pairs")
    for p in pairs:
        if set(p) != {"branch", "vulnerable", "core_fixed"}:
            raise ValueError("unexpected version field")
    if len(data["applications"]) != 7 or len({a["name"] for a in data["applications"]}) != 7:
        raise ValueError("expected seven study families")
    for a in data["applications"]:
        if set(a) != {"name", "version", "interface", "outcome", "limitation", "original_sha256"} or not a["limitation"]:
            raise ValueError("application schema or limit missing")
        if not re.fullmatch(r"[0-9a-f]{64}", a["original_sha256"]):
            raise ValueError("malformed application source digest")
    return totals


def main() -> int:
    try:
        data = json.loads((ROOT / "data/results.json").read_text(encoding="utf-8"))
        totals = validate_results(data)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"public_summary_consistency": "PASS", "selected_counts": totals, "private_runtime_reproduced": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
