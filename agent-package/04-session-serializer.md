Two days after the first PHP2Shell advisories, another issue appeared:

**CVE-2026-115560**

This one is fundamentally different.

It is not the same memory-corruption chain.

The interesting boundary is **serialization agreement**.

A simplified version of the condition I investigated was:

1. Upload progress writes session data.
2. The configured writer uses one session serialization format.
3. Application startup later changes the runtime session handler.
4. The same stored bytes are read under a different interpretation.
5. Application context provides the remaining object behavior needed for impact.

That last part matters.

The presence of attacker-controlled bytes in a session file does not automatically mean an application will deserialize them in a dangerous way.

The application has to actually provide the reader.

For the installed Moodle work I tested:

• Moodle 4.5.15
• Moodle 5.1.8
• Moodle 5.2.4
• Moodle 5.3

across selected PHP 8.2.35, 8.3.36, 8.4.27 and 8.5.12 environments using FPM and Apache/mod_php where appropriate.

The unified cohort recorded:

**11 configured runs**
**14 target effects**
**29 controls**

Controls included default-handler cases, upload-progress-disabled cases, and timing checks separating data creation from the later application read.

The conclusion is deliberately narrow:

**I demonstrated conditional application coverage of a known PHP issue.**

I did not demonstrate that default Moodle installs are vulnerable.

That difference between a core primitive and an application-complete exploit chain became one of the main themes of the entire project.

Full technical report:

https://github.com/the-vibe-dev/php2shell-public

#PHP #Moodle #ApplicationSecurity #VulnerabilityResearch
