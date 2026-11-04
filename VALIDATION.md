# Public-edition validation record

## Executed checks

On November 4, 2026, GitHub Actions run [41842023001](https://github.com/the-vibe-dev/php2shell-public/actions/runs/41842023001) completed successfully for audit commit `f060b4c5d07f245c18a3dfdb75d6fbce05e508c5`.

Environment: Ubuntu 24.04.5 runner, Python 3.12.3. The optional read-only diagnostic executed with PHP CLI 8.3.6; that interpreter version is only the diagnostic test environment, not an assertion about patch status.

| Check | Observed outcome |
|---|---|
| Public Python compilation | Passed |
| Unit tests, including rejection controls | **38 tests passed**; no failures or skips reported |
| Selected-cohort arithmetic | **26 target effects and 61 negative controls** matched the exported cohort records |
| Explicit public file inventory | **32 release files** passed the export checks |
| Private-source audit summary | **350 files audited; zero private source files copied** |
| Relative Markdown/HTML image links | Passed |
| SVG active/external-content checks | Passed |
| Public model import/call checks | Passed |
| Credential-shaped content checks | No matches in the exported files |
| JSON schema and CSV/JSON agreement | Passed |
| Offline model execution | Completed; every observation labeled as not a PHP reproduction |
| PHP diagnostic syntax | No syntax errors |
| PHP read-only diagnostic execution | Completed; output explicitly gives no vulnerability or patch verdict |

The workflow printed a SHA-256 inventory of all 32 checked files.

## Scope

These are tests of the public models, derived records, completed publication audit, and export boundary. No private exploit, original PHP memory-corruption experiment, remote target, or private evidence archive was executed or retrieved by the workflow.

The original evidence hashes identify retained records. This run does not authenticate unavailable private bytes or establish a new runtime reproduction. See [the publication review](PUBLICATION_REVIEW.md) and [audit summary](audit/AUDIT_SUMMARY.md) for the full scope and exclusions.

## Repository history

The public edition has an independent history. No private repository parent commit or import archive was used. The private source snapshot was not changed by this publication task.

This validation record is a documentation-only follow-up to the successful audit commit; GitHub Actions also validates the resulting current branch after this file update.
