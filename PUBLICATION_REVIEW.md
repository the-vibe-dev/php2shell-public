# Public-edition review and export boundary

**Prepared November 3, 2026. Private source snapshot:** `ff7ef13d69748110a5329af5228aff2d5a7e4a98`.

## Decision

Publish a newly constructed, explicitly selected public tree. Do not fork, mirror, import, or publish the private repository's Git history. Do not copy a private archive into the public repository and remove it later: the earlier object would remain recoverable from Git history.

The full research scripts remain private and unchanged. The public edition retains technical conclusions, historical version pairs, application results, controls, attribution, and original-record identifiers. It replaces executable exploitation with clearly labeled offline models and a read-only configuration diagnostic.

## Completed private-source audit

The private `pocs/` tree contained **350 files**. Every file was enumerated, SHA-256 hashed, content-scanned for operational capability signals, risk-bucketed, and assigned a publication disposition. Representative files from every high-risk family were manually reviewed.

| Result | Count |
|---|---:|
| High operational/dual-use signal score | **193** |
| Medium | **80** |
| Low | **77** |
| Excluded as operational/dual-use source | **327** |
| Excluded raw configuration/receipt | **21** |
| Excluded private research note | **2** |
| Private PoC/supporting-source files copied into public tree | **0** |

The complete private ledger is retained with the research archive under SHA-256 `c3be3b6161fff210c048a8506998374cad8d073ecac9af001bdbae38669f8ab5`. The public audit summary is in [`audit/AUDIT_SUMMARY.md`](audit/AUDIT_SUMMARY.md).

This is a complete per-file **publication-disposition audit**, not a claim that every private experiment was rerun or that every private evidence byte was independently re-authenticated during publication.

## Findings from the review

| Exposure | Why superficial edits are insufficient | Public-edition treatment |
|---|---|---|
| A marker-labeled serializer PoC still constructs a triggering request and invokes execution-capable object behavior | A fixed marker or loopback restriction leaves the reusable mechanism present | Original script, request builder, payload, and execution primitive excluded |
| Original/curated harness catalog contains core, application, scheduling, and experimental implementations | A directory labeled curated is not a non-operational boundary | Entire original and curated harness trees excluded |
| Reports contain operational worker occupancy, retry, and diagnostic combinations | Removing code alone can leave an actionable recipe in prose | Findings and same-worker limit retained; parameterized orchestration omitted |
| Third-party serializer work has unresolved delivery/disclosure boundaries | A known-CVE label does not authorize unrelated unpublished detail | Bounded conclusion retained; unpublished trigger details excluded |
| Raw receipts can contain executable inputs, addresses, commands, or private locations | JSON and logs are not inherently safe | New narrow-schema derived summaries; no raw receipt copy |
| Old wording promised original downloadable PoCs | New public files do not reproduce the original RCE | README, examples, and access guidance explicitly describe the difference |

## Capability removed, not hidden

The public examples contain no target URL argument, network client, exploit payload builder, PHP object serialization, arbitrary command execution, address-discovery helper, heap-shaping routine, worker selection, vulnerable endpoint installer, or original request replay.

The educational lifetime model uses integer generations, not pointers. The format model compares invented labels, not PHP serialized bytes. The application models use booleans and never create object data. The local PHP diagnostic reads settings and refuses non-CLI execution. It does not launch the original tests.

No compressed, base64-encoded, commented-out, or otherwise concealed copy of the private scripts is included. Original script acquisition is not automated. Access inquiries are reviewed manually by the owner.

See [`docs/defanging-methodology.md`](docs/defanging-methodology.md) for the complete export method.

## Data and claims

Recorded results remain recorded results. Original digests identify private source records; public-file digests identify exported files. Public consistency tests are not fresh runtime evidence. Version comparisons are historical and scoped to the relevant CVEs. Default application exposure, universal reliability, new CVE credit, or mass exploitation is not claimed.

The public selected aggregate is **26 target effects and 61 controls** in three non-overlapping cohorts. Twenty additional bounded observations are not added to it. The seven study families include a runtime/SAPI study, not seven vulnerable applications.

## Automated checks

The repository has an explicit file allowlist, UTF-8/size checks, relative-link checks, SVG active-content checks, public-example import/call restrictions, secret-pattern checks, structured-data checks, CSV/JSON consistency checks, audit-summary checks, and unit tests for both accepted and rejected inputs.

CI has read-only repository permissions and executes only these public checks. It has no private repository credential, private artifact fetch, remote target, or exploit test. Read the actual GitHub Actions result before calling the checks passed; this document is not an execution receipt.

Static pattern checks are supporting controls, not proof that arbitrary future code is harmless. New files and changes require substantive review. No content filter can guarantee that published knowledge will never be misused.

## Manual access

[`RESEARCH_ACCESS.md`](RESEARCH_ACCESS.md) and the issue template implement a manual reputation-and-purpose review. Independent researchers may apply. No application form automatically shares scripts, grants repository membership, or authorizes redistribution.
