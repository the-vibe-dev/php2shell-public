# Public-release source audit

**Private source snapshot reviewed:** `ff7ef13d69748110a5329af5228aff2d5a7e4a98`  
**Audit completed:** November 3, 2026

## Scope

The private repository contained **350 files under `pocs/`**. Every file was enumerated, SHA-256 hashed, scanned for operational capability signals, assigned a risk bucket, and given a publication disposition. **No private PoC/supporting-source file was copied into this public repository.**

The complete per-file audit ledger is retained with the private research archive. Its SHA-256 is:

```text
c3be3b6161fff210c048a8506998374cad8d073ecac9af001bdbae38669f8ab5
```

The ledger is not published because its full path inventory would disclose additional private experiment structure without improving review of the public edition. This document publishes the method, aggregate results, and exclusion policy.

## Capability triage

| Bucket | Files |
|---|---:|
| High operational/dual-use signal score | **193** |
| Medium | **80** |
| Low | **77** |
| **Total** | **350** |

These are publication-triage labels, not CVSS ratings or vulnerability severities. A low-scoring note or configuration file was still excluded when it depended on operational material or exposed private experiment structure.

## Final disposition

| Disposition | Files |
|---|---:|
| `EXCLUDE_OPERATIONAL_OR_DUAL_USE_SOURCE` | **327** |
| `EXCLUDE_RAW_CONFIGURATION_OR_RECEIPT` | **21** |
| `EXCLUDE_PRIVATE_RESEARCH_NOTE` | **2** |
| Private files copied into public tree | **0** |

## What was scanned

The capability scan looked for, among other things:

- network clients and target parameterization;
- multipart/request and payload construction;
- arbitrary command or target-side execution primitives;
- address discovery, heap/layout calibration, and debugger automation;
- same-worker selection, saturation, retry, and scheduling logic;
- vulnerable endpoint/container setup;
- raw receipts, configurations, and unpublished research notes.

Representative files from every high-risk family were then manually reviewed, including OOM/address-calibration work, cross-request worker-placement automation, serializer-mismatch request construction and gadget invocation, session-file inclusion replays, framework probes, FPM/FrankenPHP work, and third-party serializer research.

## Public replacement

The public `pocs/` directory was authored separately. It contains only:

- abstract offline state/lifetime/format models;
- a CLI-only, read-only PHP configuration diagnostic;
- public-data consistency checks and unit tests.

The public examples do not connect to targets, execute PHP experiments, construct triggering requests, serialize objects, calculate addresses, select workers, launch subprocesses, write marker files, or accept arbitrary commands.

## Boundary of this audit

This audit establishes the selection and capability boundary for the public repository. It does **not** rerun the private exploits or independently re-authenticate every retained private evidence byte. Public numerical claims remain derived summaries of the retained research records, with original record identifiers and digests documented separately.
