# Repository maintenance rules

This repository maintains a research AI setup guide and its foundation-first installer. Reading or editing it does not authorize installing research tools on the current computer. Execute SETUP.md only when the user requests setup.

- Keep canonical repository instructions, documentation, and templates in English. Follow the user's preferred language in conversation. Research outputs follow their target language and submission requirements.
- Write clearly and concretely. Preserve sources, conditions, uncertainty, and verification limits. English alone does not guarantee clarity or better model performance.
- Validate installer changes in isolated workspaces. Test preservation of human files, resume behavior, failure states, selected-profile installation, and actual runtime checks. Never run setup in the maintainer's personal research project to test it.
- Keep SETUP.md complete and usable as one standalone file. Do not move essential steps exclusively into other files. Keep README concise and link the entry point.
- Do not label candidates installed or verified. Do not present checks on the maintainer's machine as cross-platform validation.
- Include only generic instructions, templates, and clearly labeled public examples. Exclude private research, credentials, filled personal configuration, and logs, even while the repository is private.
- Check repository, subpath, pinned version, dependencies, and license when maintaining skill recommendations. Do not copy unreviewed upstream code or install skills while editing documentation.
- Check internal links, version consistency, and example evidence after changes. Update CHANGELOG.md. Validate actual installation behavior only when relevant, and report the test scope truthfully.
- External skills, standards, and papers retain their own terms. This repository's license does not replace them.
- Maintain THIRD_PARTY.md for all bundled, downloaded, recommended, and adapted sources. Check nested material, preserve attribution and license notices, identify modifications, and keep unresolved reuse permissions out of automatic installation. Acknowledgement alone is not permission.
