<p align="center"><img src="assets/php2shell-hero.svg" alt="PHP2Shell independent research: three CVEs, five laboratory mechanism families, four version pairs" width="100%"></p>

# PHP2Shell — public research edition

**Independent research by Charles Vosburgh · [the-vibe-dev](https://github.com/the-vibe-dev)**

[Technical report](docs/technical-report.md) · [Application results](docs/application-results.md) · [Public examples](pocs/README.md) · [Evidence and counts](docs/evidence-and-counting.md) · [Publication audit](audit/AUDIT_SUMMARY.md) · [Request research access](RESEARCH_ACCESS.md)

This is the public edition of my PHP2Shell investigation: what the source analysis and retained laboratory records establish, what the controls ruled out, and where the proof remains conditional.

The original experiments investigated **CVE-2026-109618**, **CVE-2026-109619**, and **CVE-2026-115560**. The project records five target-execution mechanism families, not five new vulnerabilities. This work is independent reproduction and analysis; the PHP project and the original reporters retain credit for the underlying disclosures.

> **What is different about this edition?** The technical results remain substantive. Working exploitation chains, triggering request builders, executable object payloads, address-discovery logic, and worker-targeting automation are not distributed here. Public examples are offline mechanism models, evidence checks, and a read-only local configuration diagnostic. They do not reproduce RCE and are not a vulnerability scanner.

## Research at a glance

| Documented cohort | Target effects | Negative controls | Meaning |
|---|---:|---:|---|
| OOM-only PHP branch comparison | 4 | 8 | Four vulnerable builds, each with fixed-version and inert controls |
| Installed Moodle selector | 14 | 29 | Eleven configured runs; not eleven vulnerabilities |
| Apache session-file inclusion | 8 | 24 | A separate application inclusion prerequisite; eight tested PHP versions |
| **Selected non-overlapping total** | **26** | **61** | **Recorded research outcomes, not a success rate** |

These counts are transcribed from retained research records through **November 2, 2026**. Publication checks validate the public data's consistency; they do not rerun the original experiments or independently authenticate withheld evidence. The [evidence guide](docs/evidence-and-counting.md) identifies the source records and recorded digests.

## Five mechanisms, different proof boundaries

![Mechanism overview and proof boundaries](assets/mechanism-map.svg)

| Mechanism | Relationship | Strongest recorded result and limit |
|---|---|---|
| OOM-only corruption | CVE-2026-109618 | Target effects on four vulnerable PHP branches; isolated proof used disabled ASLR and image-specific calibration |
| OOM plus cross-request stale state | CVE-2026-109618 / 109619 | Combined-chain execution; not isolated proof of standalone no-OOM 109619 RCE |
| Session serializer mismatch | CVE-2026-115560 | Conditional installed-application effects; not default Moodle or framework exposure |
| Session-file inclusion | Independent application flaw required | Effects on core-vulnerable and core-fixed builds; a separate inclusion sink is essential |
| Mid-script decoding | Conditional fixture; assignment unresolved | Assisted laboratory effect; an unmodified application route was not established |

## Tested vulnerable / core-fixed pairs

| PHP branch | Vulnerable test build | Core-fixed comparison |
|---|---|---|
| 8.2 | 8.2.34 | 8.2.35 |
| 8.3 | 8.3.35 | 8.3.36 |
| 8.4 | 8.4.26 | 8.4.27 |
| 8.5 | 8.5.11 | 8.5.12 |

These are historical experiment pairs for 109618/109619, not a recommendation to install an old release or a declaration that every separate session issue is fixed. See [remediation](docs/remediation.md) and the primary advisories.

## Application testing is about the route, not the logo

Moodle, WordPress, Drupal, Symfony, Laravel, CakePHP, and FrankenPHP appear in the retained research. FrankenPHP is a server/runtime study, not an application framework. Results are not interchangeable:

- Moodle results depended on particular serialization and session behavior.
- Tested ordinary WordPress and Laravel routes did not read the native upload-progress session.
- Symfony and CakePHP positives depended on explicit fixtures or selected configuration.
- Stock Drupal execution and a complete HTTP-only FrankenPHP chain remained unproven.

[Read the complete application matrix →](docs/application-results.md)

## Public-source audit

The private source snapshot contained **350 PoC/supporting-source files**. Every one was enumerated, hashed, capability-scanned, risk-bucketed, and assigned a publication disposition. **Zero private source files were copied into this public tree.**

| Audit result | Count |
|---|---:|
| High operational/dual-use signal score | 193 |
| Medium | 80 |
| Low | 77 |
| Excluded operational/dual-use source | 327 |
| Excluded raw configurations/receipts | 21 |
| Excluded private research notes | 2 |

The detailed ledger remains with the private research archive; its SHA-256 is published in the [audit summary](audit/AUDIT_SUMMARY.md). The [defanging methodology](docs/defanging-methodology.md) explains why the public edition removes capability rather than hiding it with loopback checks, fixed commands, encoding, or disclaimers.

## Try the public review tools

Python examples use the standard library, do not connect to a target, and do not invoke PHP:

```text
python3 pocs/offline_models.py
python3 scripts/review_results.py
python3 -m unittest discover -s tests -v
python3 scripts/validate_publication.py
```

The optional local diagnostic reads a few settings from the **CLI interpreter only**:

```text
php pocs/php_config_review.php
```

Its output does not establish the configuration of a web-server pool, runtime application changes, vulnerability, or exploitability. It makes no configuration changes.

## What reviewers can inspect

| Material | Location |
|---|---|
| Mechanisms, results, limitations, and related research | [Technical report](docs/technical-report.md) |
| Seven application/runtime studies | [Application results](docs/application-results.md) |
| Negative results and what they do not prove | [Negative results](docs/negative-results.md) |
| Cohort records and original artifact identifiers | [Results JSON](data/results.json) |
| Machine-readable PHP/application matrices | [data](data/README.md) |
| Public/private separation and audit scope | [Publication review](PUBLICATION_REVIEW.md) |
| Private-source disposition audit | [Audit summary](audit/AUDIT_SUMMARY.md) |
| Additional material for established researchers | [Research access](RESEARCH_ACCESS.md) |

## Research access

The original scripts and full evidence remain separate. Established researchers may request specific material for legitimate peer review. Independent researchers are welcome; a verifiable research record matters more than an employer name. Charles reviews requests individually. There is no automatic download or access grant.

Use the repository's **Research access inquiry** issue template for a brief public introduction. Do not attach confidential information, credentials, or payloads. Further exchange is arranged privately.

## Attribution and limitations

The report distinguishes original vendor findings, recorded laboratory outcomes, source-based interpretation, and newly authored public examples. It does not claim new CVE credit, mass exploitation, universal reliability, or default vulnerability of every tested application. [References and provenance](docs/references.md).

Removing operational components reduces immediate misuse potential; it cannot guarantee that technical knowledge will never be misused. A localhost restriction, fixed command, or disclaimer is not treated as an effective defanging measure.
