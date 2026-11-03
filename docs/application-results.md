# Application and runtime results

These are results reported in retained owned-laboratory records through November 2, 2026. Application versions are transcribed from those records; this publication task did not install each application again or freshly verify its release identity. They are not prevalence measurements.

| Study | Recorded version | Interface | Recorded outcome | Important limit |
|---|---|---|---|---|
| WordPress | 7.1.2 | Apache | Ordinary REST native-session readback negative; separate PHP-core experiments positive under their own conditions | Plugins, themes, custom routes, and other PHP-core paths are not ruled out |
| Moodle | 4.5.15; 5.1.8; 5.2.4; 5.3 | FPM and Apache | Conditional handler-switch effects; default/progress-disabled controls negative | Selected combinations, not every release/runtime permutation or default exposure |
| Drupal | 11.4.11 | Apache | Native progress record observed; stock front-controller RCE unproven; auxiliary conditional route positive | Auxiliary route is not the stock application route |
| Symfony | 8.1.10 | FPM/Nginx | Conditional handler-switch effect using a custom session-reading route and real session API | Unmodified stock object-writing/reading chain unproven |
| Laravel | 12.70.2 | FPM | Tested ordinary database/file session routes did not consume the native PHP session | A separate native control could read it; no universal immunity claim |
| CakePHP | App template 5.4.0; core 5.4.2 | FPM/Nginx | Conditional handler-switch effect under selected session configuration | Default preset was negative; no default-config vulnerability claim |
| FrankenPHP | 1.13.1; PHP 8.4 pair | FrankenPHP | Startup restart behavior; strongest later effect required an external research oracle | No complete HTTP-only chain; server/runtime study, not a framework finding |

## WordPress: distinguish native-session reachability from core susceptibility

The ordinary tested REST route did not expose a native PHP session identifier or consume the upload-progress record. A separate native control read the record. That difference identifies a missing application reader in the tested path; it does not negate the separate conditional PHP-core experiments carried through a WordPress laboratory image.

## Moodle: configured installed-site evidence

The selected cohort records 11 runs, 14 target effects, and 29 controls. It covers the listed releases and selected core-fixed PHP branches. The retained report uses the installed application's session route, with temporal checks that distinguish the pre-reader and post-reader state. Default-handler and progress-disabled controls did not produce the effect.

The public result deliberately omits operational synchronization, serialized object data, and gadget selection. Those omissions do not change the conclusion: a documented non-default configuration met the conditions of a separate session issue. They do limit what a reader can reproduce from this public repository alone.

## Drupal: data creation did not prove the end-to-end chain

The report distinguishes native storage creation, tested stock front-controller misses, and auxiliary conditional routes. Observing a low-level failure or intermediate state is not equivalent to proving application-route execution. Detailed shaping and diagnostic recipes remain private; the unresolved stock-route claim remains explicit.

## Symfony: an API inside a fixture is not a default deployment

The recorded positive experiment used Symfony's real session API from a custom route and selected serializer behavior. A no-switch control retained data without the target effect. This is informative about an interpretation boundary, but it does not establish a reachable stock-application object producer and reader.

## Laravel: session drivers are not interchangeable

The tested database and file session drivers did not read the native PHP upload-progress session through the ordinary application middleware. A deliberate native control did. A filesystem artifact alone therefore did not establish consumption by Laravel's session stack.

## CakePHP: the preset matters

The retained source/report distinguishes the default preset from an explicitly configured session profile. Positive records depended on the selected profile and aligned session behavior; default and other controls were negative. Two fresh positive project records and five fresh controls are described in the source, but they are not added to the selected 26/61 aggregate because that aggregate has a separate cohort definition.

## FrankenPHP: assisted evidence remains assisted

Startup behavior differed across the tested PHP pair, and later experiments investigated additional runtime state. The strongest reported effect used an external oracle. This is preserved as an assisted result, not silently promoted to an HTTP-only remote chain. The unproven address-discovery/end-to-end path remains unproven here.

## Evidence identifiers

The original report digests for each study are in [results.json](../data/results.json). They identify retained records, not publicly included complete logs. The corresponding [CSV](../data/application_matrix.csv) provides a compact index. [Evidence guide](evidence-and-counting.md).
