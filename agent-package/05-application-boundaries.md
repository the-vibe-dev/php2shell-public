One of the more useful parts of the PHP2Shell research was testing actual application boundaries.

I looked at relevant behavior across:

**Moodle
WordPress
Drupal
Symfony
Laravel
CakePHP
FrankenPHP**

The results were not remotely uniform.

And that was the point.

For example:

**WordPress**
The ordinary route I tested did not consume the native PHP upload-progress session.

**Laravel**
The ordinary database/file session routes I tested did not read that native PHP session either.

**Moodle**
Conditional serializer/session configurations produced target effects.

**Symfony and CakePHP**
Effects required explicit fixture or selected configuration conditions.

**Drupal**
I could observe useful native session behavior, but I did not establish stock front-controller RCE.

**FrankenPHP**
I reached startup and post-startup primitives, but not a complete HTTP-only end-to-end chain.

This is why I dislike vulnerability claims that jump from:

“attacker-controlled data exists”

to:

“the framework is exploitable.”

There are usually several boundaries in between.

Who wrote the data?

Where was it stored?

Who reads it?

Which serializer is active?

Does the application ever reach that reader?

Is there a usable object or side effect in the relevant context?

A writer without a reader is not an exploit chain.

A primitive without application reachability is not automatically a product vulnerability.

The complete application matrix is public here:

https://github.com/the-vibe-dev/php2shell-public

#AppSec #PHP #SecurityResearch #WebSecurity
