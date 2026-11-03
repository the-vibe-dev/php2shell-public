# Public-edition validation record

## Executed checks

On November 3, 2026, GitHub Actions run [41680326443](https://github.com/the-vibe-dev/php2shell-public/actions/runs/41680326443) completed successfully for publication commit `08f624427ee4f6f19aad147828cfa11164f41a8b`.

Environment: Ubuntu 24.04 runner, Python 3.12.3. The optional read-only diagnostic executed with PHP CLI 8.3.6; that interpreter version is recorded only as the diagnostic test environment, not an assertion about patch status.

| Check | Observed outcome |
|---|---|
| Public Python compilation | Passed |
| Unit tests, including rejection controls | 33 tests, all passed; no failures or skips reported |
| Selected-cohort arithmetic | 26 target effects and 61 negative controls matched the exported cohort records |
| Explicit public file inventory | All 28 release files passed the export checks |
| Relative Markdown/HTML image links | Passed |
| SVG active/external-content checks | Passed |
| Public model import/call checks | Passed |
| Credential-shaped content checks | No matches in the exported files |
| JSON schema and CSV/JSON agreement | Passed |
| Offline model execution | Completed; every observation labeled as not a PHP reproduction |
| PHP diagnostic syntax | No syntax errors |
| PHP read-only diagnostic execution | Completed; output explicitly gives no vulnerability or patch verdict |

The workflow printed a SHA-256 inventory of the 28 checked files. This validation record is an additional documentation file; it is not included retroactively in that run's 28-file result. A later run triggered by adding this record checks the updated tree.

## Scope

These are tests of the new public examples, derived records, and publication boundary. No private exploit, original PHP memory-corruption experiment, remote target, or private evidence archive was executed or retrieved by this workflow.

The original evidence hashes identify retained records; this run does not authenticate unavailable private bytes or establish a new runtime reproduction. See [the publication review](PUBLICATION_REVIEW.md) for the full audit scope and exclusions.

## Repository history

The public edition starts with a new `.gitignore`-only root commit followed by the curated public tree. No private repository parent commit or import archive was used. The private source snapshot was not changed by this publication task.
