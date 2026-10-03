# Maintenance priorities

The project provides a small foundation-first installer and a complete standalone guide. Judge changes by whether users can safely prepare, resume, and verify a real task. Preserve human research files, keep licensing boundaries explicit, and report actual verification scope.

## Current priorities

1. Preserve workspace boundaries, existing environments, source files, and human configuration.
2. Keep failure records actionable and installation resumable through the copied engine.
3. Exercise launchers and supported runtimes across operating systems and Python versions.
4. Improve the first successful task and handoff before expanding the optional catalog.
5. Consider transitive dependency locking and smaller code modules when release requirements justify them.

The 0.2.2 release addresses the first two priorities and adds CI and a [first-task walkthrough](FIRST_TASK.md). Missing-Python bootstrap, native host discovery, additional skill integrations, and independent user acceptance remain useful next evidence.

## Change and release workflow

- Start from the current main branch and keep each change on a descriptive branch. Review existing work before publishing.
- Add regression tests for behavior changes involving preservation, recovery, or current verification. Run fast checks before network-dependent installation checks.
- Use disposable synthetic workspaces. Keep private research, local profiles, credentials, caches, and diagnostic logs out of commits.
- Run `python -m unittest discover -s tests -v`, `python scripts/check_repository.py`, `bash -n install.sh`, and `python scripts/check_installation.py`. Use `--online` for an explicit actual core/figures test.
- Check the exact proposed commit's CI results and diff before merging. Repair failures and record any untested boundary honestly.
- Update engine/catalog release metadata, CHANGELOG.md, compatibility evidence, and affected instructions together. Record external components in THIRD_PARTY.md.
- Preserve edited files during upgrades. Only update an installer-owned entry point whose recorded hash still matches its contents, and retain a backup.

Existing direct dependency and skill pins remain intentional. Updating a pin requires availability, integrity, license, and functional checks; a newer version alone is insufficient.
