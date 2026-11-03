# Public-edition review and export boundary

**Prepared November 3, 2026. Source snapshot:** `ff7ef13d69748110a5329af5228aff2d5a7e4a98`.

## Decision

Publish a newly constructed, explicitly selected public tree. Do not fork, mirror, import, or publish the private repository's Git history. Do not copy a private archive into the public repository and remove it in a later commit: the earlier copy would still exist in history.

The full research scripts remain separate and unchanged. The public edition retains technical conclusions, historical versions, application results, controls, attribution, and original-record identifiers. It replaces executable exploitation with clearly labeled offline models and a read-only configuration diagnostic.

## Findings from the source review

| Exposure | Why superficial edits are insufficient | Public-edition treatment |
|---|---|---|
| A marker-labeled serializer PoC still constructs a triggering request and invokes execution-capable object behavior | A fixed marker or loopback restriction leaves the reusable mechanism present | Original script, request builder, payload, and execution primitive excluded |
| Original/curated harness catalog contains core, application, scheduling, and experimental implementations | A directory labeled curated is not a non-operational boundary | Entire original and curated harness trees excluded |
| Report contains operational worker occupancy, retry, and diagnostic combinations | Removing code alone leaves an actionable recipe in prose | Preserve findings and same-worker limit, omit parameterized orchestration |
| Historical third-party serializer work has unresolved delivery/disclosure boundaries | A known CVE label does not authorize unrelated unpublished detail | Bounded conclusion retained; unpublished trigger details excluded |
| Raw receipts can contain executable inputs, addresses, commands, or private locations | JSON and logs are not inherently safe | New narrow-schema derived summaries, no raw receipt copy |
| Original audit only normalizes private paths and inventories source | Zero path-pattern hits do not establish defanging | Review capability, data fields, content selection, and history separately |
| Old wording promises original downloadable PoCs | New public files do not reproduce original RCE | README, examples, and access guidance explicitly describe the difference |

## Completeness and honesty about scope

The source inventory records 500 files, including 350 PoC/supporting-source files and 33 finding records. This is a **public-export audit**, not a claim that every line of all 350 private files was independently audited or every experiment rerun.

The report, application studies, cohort data, publication facts, catalog, inventory, selected findings, representative execution-capable code, and reused graphics were reviewed to establish what can be exported. Every executable file in the new public edition is newly authored and reviewed. No original exploit source or raw payload-bearing evidence file is copied, so the exclusion does not depend on successfully redacting each of the 350 files.

The private tree remains private and unchanged. Its snapshot ID is retained as provenance, not imported as a parent commit.

## Capability removed, not hidden

The public examples contain no target URL argument, network client, exploit payload builder, PHP object serialization, arbitrary command execution, address-discovery helper, heap-shaping routine, worker selection, vulnerable endpoint installer, or original request replay.

The educational lifetime model uses integer generations, not pointers. The format model compares invented labels, not PHP serialized bytes. The application models use booleans and never create object data. The local PHP diagnostic reads settings and refuses non-CLI execution. It does not launch the original tests.

No compressed, base64-encoded, commented-out, or otherwise concealed copy of the original scripts is included. Original script acquisition is not automated. Access inquiries are reviewed manually by the owner.

## Data and claims

Recorded results remain recorded results. Original digests identify private source records; public-file digests identify the exported files. Public consistency tests are not fresh runtime evidence. Version comparisons are historical and scoped to the relevant CVEs. Default application exposure, universal reliability, new CVE credit, or mass exploitation is not claimed.

The public selected aggregate is 26 target effects and 61 controls in three non-overlapping cohorts. Twenty further bounded observations are not added to it. The seven study families include a runtime/SAPI study, not seven vulnerable applications.

## Automated checks

The repository includes an explicit file allowlist, UTF-8/size checks, relative-link checks, SVG active-content checks, public-example import/call restrictions, secret-pattern checks, structured-data checks, CSV/JSON consistency checks, and unit tests for both model outcomes and rejected data.

CI has read-only repository permissions and executes only these public checks. It has no private repository credential, private artifact fetch, remote target, or exploit test. It prints a SHA-256 inventory of the public files. Read the actual GitHub Actions outcome before calling the checks passed; this document alone is not an execution receipt.

Static pattern checks are supporting controls, not a proof that arbitrary future code is harmless. New files and changes require substantive review. No content filter can guarantee that published knowledge will never be misused.

## Manual access

[RESEARCH_ACCESS.md](RESEARCH_ACCESS.md) and the issue template implement a manual reputation-and-purpose review. Independent researchers may apply. No application form automatically shares scripts, grants repository membership, or authorizes redistribution.
