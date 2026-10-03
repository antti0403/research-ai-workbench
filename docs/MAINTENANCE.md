# Maintenance priorities

Improve the path from setup to one verified research task before expanding the catalog. Preserve human files and report actual test scope.

## Next evidence to collect

1. Missing-Python bootstrap tests in clean Windows and Linux environments.
2. Native skill discovery and independent user acceptance, beyond installer checks.
3. Task-specific literature, writing, and computation integrations.
4. Transitive dependency locking and smaller code modules when release needs justify them.

The 0.2.2 reliability release added ownership checks, safer paths, resume fixes, and cross-platform CI. Version 0.3.1 adds bilingual kit checks, actual release upgrade checks, profile Python requirements, and a full-text claim example. See [compatibility](COMPATIBILITY.md) for recorded results and [first task](FIRST_TASK.md) for acceptance.

## Releases

Use a descriptive branch from current main. Follow [Contributing](../CONTRIBUTING.md) for checks and third-party review; keep tests in disposable workspaces and personal data out of commits. Review the exact proposed commit's diff and CI before merging.

Update engine/catalog metadata, affected instructions, and [CHANGELOG](../CHANGELOG.md) together. Bundled documentation changes need a new kit version: same-version conflicts are deliberately preserved. Keep compatibility entries tied to the release actually tested.

A new pin requires availability, integrity, license, and functional checks. A newer version alone is not sufficient. Preserve edited files and back up unchanged owned entry points when upgrading.
