The part of **CVE-2026-109619** that interested me most was not the stale pointer by itself.

It was the lifetime mismatch.

A persistent PHP worker can serve many requests.

Request memory is short-lived.

Some worker-global state lives longer.

If a worker-global reference points into request-owned memory, correctness depends on that reference being cleared before the request heap disappears.

The chain I investigated looks conceptually like this:

**Request A**
→ publishes request-owned state
→ exits abnormally
→ request heap is freed
→ worker survives

**Request B**
→ lands on the same worker
→ reaches a consumer before normal reset
→ stale state is used

That means **worker placement becomes part of exploitability**.

A process pool makes the chain less deterministic.

It does not repair the lifetime bug.

I reproduced combined OOM/stale-state target effects in controlled Apache experiments, including cases that did not rely on deliberately holding nearly the entire worker pool.

But there is an important attribution limit:

My strongest local execution results used an **OOM producer**.

So I do **not** count those as independent proof that CVE-2026-109619 alone produced no-OOM RCE in my lab.

I separately reproduced no-OOM stale state and worker aborts on PHP 8.5.11.

**Standalone no-OOM CVE-2026-109619 RCE independently demonstrated in my campaign: zero.**

That negative result stayed in the report.

This was one of the recurring lessons from the project:

**A vulnerability class can be real while a particular exploit path remains unproven.**

More detail:

https://github.com/the-vibe-dev/php2shell-public

#SecurityResearch #UseAfterFree #PHP #ExploitDevelopment
