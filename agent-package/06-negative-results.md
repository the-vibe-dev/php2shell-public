Security research looks cleaner after publication than it does while you're actually doing it.

The successful chain gets the headline.

The failed runs usually disappear.

I kept mine.

Some of the most useful PHP2Shell conclusions came from paths that did **not** reach the claimed impact:

• no local standalone no-OOM CVE-2026-109619 RCE;
• no isolated ASLR-on OOM-only proof;
• no native upload-progress session read through the ordinary WordPress route I tested;
• no native read through the ordinary Laravel routes I tested;
• no stock Drupal front-controller execution;
• no complete HTTP-only FrankenPHP endgame;
• no demonstrated stock-application source for the guarded mid-script object path.

None of those means the product or vulnerability class is “safe.”

They mean:

**that exact path, build, configuration or assumption did not produce the claimed result.**

That is an important difference.

Negative controls are also why the positive results mean anything.

For the three non-overlapping publication cohorts, I retained:

**26 target effects**
**61 negative controls**

Those controls were not “failed attacks.”

They were deliberate changes to the conditions being tested:

fixed version versus vulnerable version;
default handler versus altered handler;
feature enabled versus disabled;
reader present versus reader absent;
target condition versus inert condition.

If changing the variable you think matters does not change the result, you probably haven't proven the variable mattered.

I published the negative-results section because I think that part of the research is as valuable as the successful PoCs.

https://github.com/the-vibe-dev/php2shell-public

#VulnerabilityResearch #CyberSecurity #Research #AppSec
