# Defanging methodology

## Why obfuscation was rejected

Obfuscation does not remove exploit capability. A loopback restriction, fixed marker, encoded payload, commented-out command, or disclaimer can often be reversed without understanding the underlying research. The public edition therefore uses **capability removal and independent replacement**, not concealment.

## Export model

The private repository and its history remain separate. The public repository was constructed as a new tree with no private parent commit and no later deletion of previously committed exploit code.

The export follows four rules:

1. **Retain conclusions and proof boundaries.** Root cause, versions, application prerequisites, positive outcomes, controls, and negative results remain available.
2. **Do not copy operational implementations.** Trigger builders, executable serialized objects, arbitrary command interfaces, target discovery, address calibration, worker targeting, retry orchestration, and raw request replay remain private.
3. **Replace with non-operational models.** Public examples model abstract state transitions or validate public summary data. They do not invoke vulnerable behavior.
4. **Keep provenance explicit.** Original-record names and SHA-256 digests identify retained private evidence; public checks do not claim to have rerun the original experiments.

## Capability categories reviewed

The private `pocs/` tree was scanned and manually sampled for:

- network and target selection;
- request, payload, and object construction;
- execution and target-side write primitives;
- memory-address, heap-shaping, and debugger logic;
- persistent-worker placement and retry automation;
- vulnerable service/application setup;
- raw configurations, receipts, and unpublished research notes.

All 350 private PoC/supporting-source files were excluded. Aggregate audit results are in [`../audit/AUDIT_SUMMARY.md`](../audit/AUDIT_SUMMARY.md).

## What the public examples can do

`pocs/offline_models.py` uses invented labels, integers, and booleans to explain:

- partial initialization and cleanup assumptions;
- request-lifetime mismatches;
- writer/reader format disagreement;
- the difference between stored data and an application reader;
- why a list of prerequisites is not proof of a stock application chain.

`pocs/php_config_review.php` reads settings from the invoking **CLI interpreter only**, refuses web execution, changes no settings, and returns no vulnerability or patch verdict.

The validation scripts check arithmetic, schemas, file selection, relative links, active SVG content, obvious credential patterns, and the absence of operational capabilities in the newly authored public examples.

## What this does not guarantee

Publishing a detailed technical explanation always carries residual misuse risk. Static checks cannot prove that every future contribution is harmless, and removing code cannot make public knowledge unknowable. The objective is narrower and testable: the repository does not distribute the private exploit implementations or provide an immediately reusable operational substitute.

Full scripts and additional evidence may be shared selectively for legitimate peer review under the process in [`../RESEARCH_ACCESS.md`](../RESEARCH_ACCESS.md).
