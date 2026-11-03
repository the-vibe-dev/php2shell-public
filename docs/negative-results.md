# Negative results and incomplete chains

A negative result has a tested hypothesis and a bounded scope. It must not be converted into a claim that every installation is safe.

| Investigation | What the record supports | What it does not establish |
|---|---|---|
| Fixed PHP comparison for the isolated OOM cohort | The tested effect was absent under matching fixed-version controls | Freedom from all unrelated application vulnerabilities |
| Inert OOM controls | The observed effect depended on the tested triggering condition | A probability of exploitation against arbitrary hosts |
| OOM-only with ASLR | Isolated four-branch proofs used disabled ASLR and image calibration | Portable ASLR-enabled isolated exploitation |
| No-OOM stale-state study | Stale state and worker aborts with matched controls | Local standalone no-OOM 109619 RCE |
| Worker-pool routing | Some experiments missed when the necessary requests did not share a worker | That more workers fix the underlying lifetime violation |
| Default serializer controls | The tested mismatch effect was absent with consistent handler use | All possible application session behavior is safe |
| Upload-progress-disabled controls | The tested upload-progress-dependent route was removed | Every non-session producer/consumer variant is mitigated |
| WordPress ordinary REST route | Native session consumption was not observed in that route | Immunity of plugins, themes, custom code, or core PHP |
| Laravel ordinary session routes | Native PHP progress storage was not consumed by tested database/file middleware | All Laravel deployments or custom routes are unaffected |
| Drupal stock front controller | Full target execution was not established in the retained stock-route tests | Impossibility of other paths |
| Symfony fixture | A conditional API-level effect was recorded | Default framework exposure |
| FrankenPHP HTTP-only work | Strongest effect remained oracle-assisted | A complete unauthenticated HTTP-only execution chain |
| Mid-script object decoding | An assisted fixture produced an effect | A stock unauthenticated object writer and gadget chain |
| Third-party serializer hardening | An implementation-scope observation was recorded | A new proven remotely exploitable vulnerability |

## Controls versus failed attempts

The 61 selected negative controls are not 61 unsuccessful exploit attempts. They deliberately change a condition such as the runtime version, content interpretation, or configuration. Combining them with 26 target effects to calculate a success percentage would answer no well-defined research question.

## Preserve the original inference boundary

No-OOM local worker crashes do not disprove PHP's upstream RCE advisory. A configured application positive does not defeat an unrelated core patch. A source-supported possibility is not a runtime observation. A public model passing its unit tests is not evidence that the original PHP exploit was reproduced.

The source report also records bounded memory-layout and application-routing failures. Their operational parameters are omitted here; the fact that the attempted chain did not complete is retained without offering a tuning guide.

Sources: retained campaign report and application records identified in [references](references.md) and [results data](../data/results.json).
