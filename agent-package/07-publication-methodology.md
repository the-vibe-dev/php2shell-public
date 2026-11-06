I wanted the PHP2Shell work to be reviewable.

I did **not** want the public repo to become a convenient download-and-run exploitation package.

So I treated publication as a separate engineering problem.

The private research tree contained:

**350 PoC/supporting-source files**

I audited all 350 before building the public repository.

Publication triage:

**193 high operational/dual-use signal**
**80 medium**
**77 low**

Final disposition:

**327 operational/dual-use files excluded**
**21 raw configurations/receipts excluded**
**2 private research notes excluded**
**0 private source files copied into the public repository**

The public repo was then built independently.

It does not inherit the private Git history.

It does not contain a deleted exploit hiding in an earlier commit.

The public examples are newly authored offline mechanism models, evidence-validation tools, and a read-only CLI configuration diagnostic.

They do not:

• build triggering HTTP requests;
• generate executable object payloads;
• discover target addresses;
• shape the heap;
• select workers;
• replay the original chains;
• accept arbitrary commands.

The technical findings are still there.

So are the version matrices, application results, negative experiments, evidence methodology, remediation notes and proof boundaries.

Researchers with an established track record who need to inspect a specific full script or underlying evidence can request access through the repository.

Independent researchers are welcome too. I care more about a verifiable body of work and a legitimate review purpose than an employer name.

Public research repository:

https://github.com/the-vibe-dev/php2shell-public

I’d be especially interested in feedback from people who work on PHP internals, persistent-worker runtimes, session handling, or exploit reliability.

#SecurityResearch #ResponsibleDisclosure #PHP #CyberSecurity
