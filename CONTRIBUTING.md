# Contributing

Report concrete setup failures, contribute verified environment results, or improve instructions. Start with the task and the step that failed, then provide relevant evidence.

For issues, include operating system and agent versions, selected skill revisions, expected and actual behavior, and attempted fixes. Share only relevant log excerpts. Remove credentials, account details, and private research material.

A new skill recommendation needs a source repository, actual subpath, purpose, dependencies, license link, account or cost requirements, and verification scope. Mark untested items as candidates. Popularity and marketing claims are not reasons to install an entire collection.

Keep canonical documentation and AI instructions in English. Preserve the user's choice of conversation language and the required language for deliverables. Do not claim that English by itself improves model accuracy. Simplify wording without weakening technical meaning, evidence requirements, or authorization boundaries.

Keep SETUP.md independently usable. Update affected README guidance and CHANGELOG, and check internal links. For environment validation, provide reproducible details using the [compatibility record](docs/COMPATIBILITY.md).

## Installer development

Use Python 3.11+ and a disposable workspace. Run `python -m unittest discover -s tests` and `bash -n install.sh`. Run actual setup and selected extensions before claiming they work; keep network and runtime tests separate from mocked failure tests. Never test against a user's real research files. Do not commit `.bootstrap`, `.workbench`, caches, downloaded third-party sources, or filled profiles.

Review pinned versions, hashes, license terms, and required shared resources when changing registry.json. Preserve private settings and human edits. Record operating system, Python, selected profiles, actual checks, and untested boundaries in the compatibility record. A source-code review is not a Windows execution test.
