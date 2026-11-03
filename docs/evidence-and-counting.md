# Evidence, provenance, and counting

## Four separate assertions

1. **Recorded research result:** the retained report or receipt describes a laboratory observation.
2. **Artifact integrity:** bytes match a recorded digest when both are available.
3. **Public export consistency:** this edition faithfully represents selected records, counts, and limitations.
4. **Fresh reproduction:** someone actually reruns the original experiment and observes its result.

This publication task performs the third category, checks its own public code, and identifies the records used for the first category. It does not claim the fourth. Original artifact hashes are retained as identifiers; absent original bytes, the public tooling cannot independently verify those hashes or the underlying runtime behavior.

## Selected non-overlapping cohorts

| ID | Effects | Controls | Counting basis |
|---|---:|---:|---|
| C01 | 4 | 8 | Four vulnerable branch members, four corresponding fixed cases, four inert cases |
| C02 | 14 | 29 | Eleven configured installed-Moodle selector runs; earlier overlapping replays excluded |
| C03 | 8 | 24 | Eight Apache PHP version cases, each with three matched controls; FPM cases excluded |
| Total | 26 | 61 | Sum of these cohorts only |

Cohort boundaries are taken from the source `data/experiments.json`. The public checker recomputes the sum and validates unique IDs. It does not authenticate private raw runs, calculate an exploit-success rate, or certify that every campaign trial is included.

## Source record identifiers

| Cohort | Retained source | Recorded SHA-256 |
|---|---|---|
| C01 | OOM-only multiversion selector receipt | `0a4116d839edff7b4efcc9e3ee37416c568505ccb2cc1b2837e6510f5c318fd7` |
| C02 | Unified Moodle selector review | `d56e13c765e795e193558f5df25a4167600177ab8bd3fa0cc1256029843c67ed` |
| C03 | Apache session-file-inclusion receipt | `01bb8f7b13be2d14951d321c244105d26cfc284b0b8133948524504c2f271665` |

These digests describe original records, not this Markdown or the derived JSON. The public validator computes independent SHA-256 values for public files and prints them in its output.

## Why raw receipts are not copied wholesale

A JSON receipt can include executable requests, gadget data, memory addresses, a command invocation, or private file locations. Calling it evidence does not make the contents inert. This release exports a narrow schema containing results, conditions, control counts, limitations, and original artifact identifiers. The complete private receipts are not embedded as strings, base64, archives, links, or CI artifacts.

## Claim-to-source mapping

| Public claim | Source basis |
|---|---|
| Five mechanism families, not five CVEs | Retained complete technical report and publication facts |
| Four vulnerable/core-fixed pairs | Retained version cohort and PHP primary advisories |
| 26 effects / 61 controls | The three named cohort records above |
| No local standalone no-OOM RCE | Retained campaign limitations and negative-results report |
| Conditional Moodle results | C02 and the installed-application report |
| Seven study families with different results | Seven application/runtime report identifiers in results.json |
| Public examples are models, not exploit reproduction | Inspection of all newly authored public example code and its tests |

## How to review

Read the mechanism and its limit, then inspect the corresponding structured record and control description. Use the public checks to validate arithmetic and schema. For deeper peer review of original runtime evidence, request only the specific additional material needed through [research access](../RESEARCH_ACCESS.md).

No unexplained `verified: true` flag is used to imply a new live result. The data explicitly says `runtime_reproduced_for_public_edition: false`.
