# Public data

- [results.json](results.json): selected cohort counts, five mechanism summaries, historical version pairs, and seven study summaries.
- [version_matrix.csv](version_matrix.csv): four historical vulnerable/core-fixed test pairs for 109618/109619.
- [application_matrix.csv](application_matrix.csv): seven application/runtime study summaries.
- [related-results.json](related-results.json): twenty additional bounded observations, preserved without operational probe parameters.

All runtime outcomes are derived from retained research records. `runtime_reproduced_for_public_edition` is false. Original SHA-256 values identify private source records; these are not claimed to be digests of the public summaries.

No request bytes, serialized objects, heap layouts, executable payloads, memory addresses, target URLs, laboratory credentials, or hidden archives are embedded. Status labels preserve an observation's limit and are not a generic exploitability score.

See [counting and evidence](../docs/evidence-and-counting.md). Run `python3 scripts/review_results.py` from the repository root for the arithmetic check.
