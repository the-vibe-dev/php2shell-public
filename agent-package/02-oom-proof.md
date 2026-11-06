One of the first things I wanted to know about **CVE-2026-109618** was simple:

Can I isolate the OOM condition from the rest of the PHP2Shell chains and reproduce a target-side effect across multiple PHP branches?

I tested four vulnerable/fixed pairs:

PHP 8.2.34 → 8.2.35
PHP 8.3.35 → 8.3.36
PHP 8.4.26 → 8.4.27
PHP 8.5.11 → 8.5.12

The isolated cohort produced:

**4 target effects**
**8 negative controls**

Each vulnerable branch had both:

• its corresponding fixed-version comparison;
• an inert control.

The important limitation is just as interesting as the positive result.

My isolated execution proof used **ASLR disabled and addresses calibrated to the exact laboratory image**.

So what did I prove?

I proved that the vulnerable state transition could produce a target-side execution effect in those specific builds.

What did I *not* prove?

A portable, production-ready, ASLR-on exploit.

That distinction is important in vulnerability research.

A working laboratory exploit is evidence of a primitive.

Portability is another engineering problem entirely.

The patch boundary was also useful to study. The core issue is not simply “PHP ran out of memory.” The problem is what happens when an exceptional exit interrupts request initialization and later cleanup code encounters state whose normal ownership assumptions no longer hold.

That is a much more interesting failure mode than a generic OOM crash.

Full writeup and vulnerable/fixed matrix:

https://github.com/the-vibe-dev/php2shell-public

#PHP #MemorySafety #CyberSecurity #VulnerabilityResearch
