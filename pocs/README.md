# Public examples — deliberately non-operational

These are newly authored educational replacements, not the original exploit scripts with a target restriction. They contain no vulnerability-triggering request builder, serialized gadget, memory-corruption trigger, heap calibration, worker targeting, arbitrary command interface, or network client.

## Offline mechanism models

```text
python3 pocs/offline_models.py
```

| Function | What it illustrates | What it does not do |
|---|---|---|
| `partial_state` | Incomplete initialization versus cleanup assumptions | No allocations intended to exhaust memory and no PHP invocation |
| `request_lifetime` | A reference's owner generation versus the next request | No freed-memory access or process affinity |
| `format_agreement` | Writer/reader format agreement and rejection | No PHP decoder, object serialization, or gadget |
| `reader_boundary` | Stored data alone versus an independent application sink | No file inclusion or filesystem read |
| `application_requirements` | Missing prerequisites prevent a complete claim | No object creation, parsing, or execution |

All examples operate on small booleans, integers, and labels. Output explicitly says `EDUCATIONAL MODEL — NOT PHP REPRODUCTION`. Changing a label cannot turn them into an exploit; the operational components are absent.

## Read-only PHP configuration diagnostic

```text
php pocs/php_config_review.php
```

This file refuses web-SAPI execution and reports only a few local CLI settings. It does not load an application, change configuration, inspect files, send traffic, construct payloads, or conclude that a web service is safe. A web worker may use a different build or configuration, and application code can change relevant settings later.

## Evidence and public-tree checks

```text
python3 scripts/review_results.py
python3 -m unittest discover -s tests -v
python3 scripts/validate_publication.py
```

These commands check the exported records, examples, and release boundaries. They do not authenticate withheld raw evidence or rerun the original command-execution research. The public code's tests and the historical experiment controls are different datasets.

The full scripts are retained separately. Established researchers can follow [the manual access process](../RESEARCH_ACCESS.md).
