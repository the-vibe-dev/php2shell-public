# PHP2Shell LinkedIn Series — Agent Package

Seven ready-to-post LinkedIn posts featuring:

https://github.com/the-vibe-dev/php2shell-public

## Posting order

1. Launch / overview
2. CVE-2026-109618 OOM proof
3. CVE-2026-109619 worker lifetime / cross-request state
4. CVE-2026-115560 serializer mismatch
5. Application-boundary testing
6. Negative results and controls
7. Publication / defanging methodology

## Suggested cadence

Post one every 1–2 days. Do not publish the whole series at once.

## Agent guardrails

- Preserve CVE numbers, versions, counts, and proof limitations.
- Do not claim Charles discovered CVE-2026-109618, CVE-2026-109619, or CVE-2026-115560.
- Do not call 26 target effects / 61 controls a success rate.
- Do not generalize the named application tests into universal vulnerability claims.
- Preserve the distinction between combined OOM/stale-state execution and standalone no-OOM CVE-2026-109619.
- Preserve the ASLR limitation of the isolated OOM-only proof.
- Preserve CVE-2026-115560's application/configuration prerequisites.
- Do not pull exploit details from the private research repository into a public post.
- Promote only the public repository URL.
- Direct qualified researchers seeking full scripts to the repo's research-access process.
- Keep the voice technical, first-person, evidence-backed, and non-hypey.

## Suggested graphics

1. Overview: 3 CVEs / 5 mechanism families / 26 effects / 61 controls
2. OOM: vulnerable → fixed PHP version matrix
3. Worker lifetime: Request A → persistent worker → Request B
4. Serializer mismatch: writer format → stored bytes → reader format
5. Applications: route-boundary matrix
6. Negative results: positive evidence vs negative controls
7. Publication: 350 reviewed → 0 private source files copied
