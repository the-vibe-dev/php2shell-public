# References, attribution, and provenance

## Primary public references

- **U1:** PHP, [RCE via OOM corruption — GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w), CVE-2026-109618.
- **U2:** PHP, [RCE via stale global state — GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp), CVE-2026-109619.
- **U3:** PHP, [October 23, 2026 session upload-progress notice](https://www.php.net/archive/2026.php#2026-10-23-1), CVE-2026-115560.
- **U4:** PHP, [session upload-progress documentation](https://www.php.net/manual/en/session.upload-progress.php).
- **U5:** php-src, [issue #24481](https://github.com/php/php-src/issues/24481), separately tracked related research; not an additional PHP2Shell CVE in this report.

U1–U3 were retrieved during public-edition preparation on November 3, 2026. The other entries are source-referenced context, not claims of a fresh patch verification. The official advisory pages and their credited reporters are authoritative for original disclosure credit.

## Research-source snapshot

The author's retained source snapshot is commit `ff7ef13d69748110a5329af5228aff2d5a7e4a98`, with tree `afaaab9439573acb98850ddef263540812c8269d`. The snapshot identifier is provenance, not a public download URL. Its history and exploit files are not ancestors of this public repository.

Reviewed publication sources included:

| Source document | Git blob identifier |
|---|---|
| Application research | `6b656ae9e86756471defdce0c6886897f1304d4d` |
| Experiment/cohort data | `a209f4afb1913949ff8c78be0d81148b1944f1ce` |
| Publication facts | `f093ea7978de5ea02b96603767aad5659d5f8dc6` |
| PoC catalog | `622cc5629cb606cdeb8fa30d7aaf7a7b81d55f22` |
| Source publication audit | `22614f1ed65f402a58d9419b9a7535c71e650831` |
| Reused hero graphic | `ba87fb5a3b705a430dc280bb9992e385f95f7ca8` |
| Reused mechanism graphic | `d45661a824f062fb839570cb5dae7e259af74cf3` |

The complete technical report, findings excerpts, and representative execution-capable script were also reviewed to set the export boundary. Original report/receipt SHA-256 identifiers are preserved in the selected data. Git object IDs and SHA-256 artifact hashes are different identifiers and should not be conflated.

## Attribution

Charles Vosburgh's contribution described here is independent reproduction, analysis, application/configuration testing, control design, and interpretation of retained laboratory results. No original CVE discovery or new CVE assignment is claimed. This edition does not redistribute third-party exploit implementations or relabel their authorship.

The source inventory reports 33 finding records and 350 PoC/supporting-source files. Those inventory numbers do not imply 33 vulnerabilities or 350 independently reviewed safe public scripts. The public edition selects five mechanism families and related bounded results rather than copying the full inventory.

## Dates and uncertainty

Research results are through November 2, 2026. Public-edition preparation is November 3, 2026. Application versions are recorded lab metadata. Subsequent release or disclosure changes should be added as dated updates rather than silently rewriting the historical experiment.
