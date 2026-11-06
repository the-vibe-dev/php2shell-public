I spent October 23 through November 2 reproducing and stress-testing the PHP issues that became known as **PHP2Shell**.

The result is now public:

https://github.com/the-vibe-dev/php2shell-public

The work centered on three disclosed vulnerabilities:

• **CVE-2026-109618** — exceptional OOM handling can leave request state partially initialized.

• **CVE-2026-109619** — request-owned state can survive across requests in a persistent worker and be consumed after its original heap is gone.

• **CVE-2026-115560** — a separate upload-progress/session serialization mismatch that depends heavily on application behavior.

I did not discover these CVEs. My goal was different:

**Reproduce them independently, compare vulnerable and fixed builds, test real application boundaries, and find out where the exploit story stops being universal.**

Across three non-overlapping experiment cohorts, the retained research records contain:

**26 target effects**
**61 negative controls**

That includes:

• four vulnerable/fixed PHP branch comparisons;
• eleven configured Moodle runs;
• eight PHP versions tested against a separate session-file inclusion path.

I ultimately demonstrated **five target-execution mechanism families** in the lab.

That does not mean five new CVEs.

It does not mean five default-vulnerable applications.

And it definitely does not mean “PHP2Shell works everywhere.”

A large part of the research was figuring out why it *doesn't*.

The repo includes the technical report, application matrix, negative results, evidence/counting methodology, remediation notes, and non-operational public review tools.

Over the next several posts I’m going to break down the parts I found most interesting.

#CyberSecurity #VulnerabilityResearch #PHP #SecurityResearch
