# Remediation and historical version boundaries

The laboratory matrix is a historical test record, not a recommendation to deploy one of its older versions.

## Core memory-safety issues

PHP's October 21, 2026 advisories identify 8.2.35, 8.3.36, 8.4.27, and 8.5.12 as fixed releases for CVE-2026-109618 and CVE-2026-109619. Use a currently supported vendor release containing the relevant fixes or a vendor-confirmed backport, and ensure running workers use the updated build. These branch floors were rechecked in the primary advisories for this edition. [U1, U2](references.md).

Runtime configuration alone is not presented here as a complete substitute for those fixes. A failed public model or a favorable version string is not patch verification. Distribution backports, loaded extensions, pool configuration, and the actual worker build require operational verification in the affected environment.

## Separate serializer mismatch

PHP's October 23 notice advises administratively disabling session upload progress where the unusual runtime serializer-switch pattern may be present, until the applicable fix is deployed. Apply settings before request processing and restart affected workers. The retained November 2 research did not establish a fixed release for CVE-2026-115560; this document does not invent one. Consult the linked PHP notice and current vendor advisories for subsequent changes. [U3](references.md).

## Independent application flaws

A separate file-inclusion sink requires application remediation; applying an unrelated memory-safety patch does not remove that sink. Audit storage/reader assumptions and avoid interpreting untrusted data as executable content. A deliberately configured fixture is not evidence that default application settings need the same fix.

## Diagnostic limits

`pocs/php_config_review.php` reports only the invoking CLI interpreter's version and a few settings. It cannot see per-pool web configuration or later application overrides. It sends no requests, changes nothing, and issues no all-clear verdict.
