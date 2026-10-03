# Contributing

Report concrete setup failures, contribute verified environment results, or improve instructions. Start with the task and the step that failed, then provide relevant evidence.

For issues, include operating system and agent versions, selected skill revisions, expected and actual behavior, and attempted fixes. Share only relevant log excerpts. Remove credentials, account details, and private research material.

A new skill recommendation needs a source repository, actual subpath, purpose, dependencies, license link, account or cost requirements, and verification scope. Mark untested items as candidates. Popularity and marketing claims are not reasons to install an entire collection.

## Attribution and third-party material

Update [THIRD_PARTY.md](THIRD_PARTY.md) whenever you add, remove, update, copy, adapt, or recommend an external component. Record its upstream author or project, canonical URL, exact revision when available, the files or feature that use it, whether it is bundled or downloaded, its license, any modifications, and any unresolved permission limits. Credit workflow inspirations separately from executable dependencies. Credit an intermediary adaptation as well as its original source when both informed the work.

Inspect nested assets and notices; a repository-level license is not proof that every included paper, image, dataset, or reference has the same terms. Retain upstream copyright, license, NOTICE, and citation files when required. Mark changes to copied files. Do not use a source link or an acknowledgement as a substitute for permission. Keep components with unresolved reuse permissions out of automatic installation until reviewed.

The project's MIT license covers its original contributions. Do not relabel external material as MIT or imply that upstream authors endorse this project. For dependencies resolved at installation time, retain their distribution metadata and licenses; review the actual distribution before redistributing an installed environment. A license summary does not replace the full terms.

Keep canonical documentation and AI instructions in English. Preserve the user's choice of conversation language and the required language for deliverables. Do not claim that English by itself improves model accuracy. Simplify wording without weakening technical meaning, evidence requirements, or authorization boundaries.

Keep SETUP.md independently usable. Update affected README guidance and CHANGELOG, and check internal links. For environment validation, provide reproducible details using the [compatibility record](docs/COMPATIBILITY.md).

## Installer development

Use Python 3.11+ and a disposable workspace. Run `python -m unittest discover -s tests` and `bash -n install.sh`. Run actual setup and selected extensions before claiming they work; keep network and runtime tests separate from mocked failure tests. Never test against a user's real research files. Do not commit `.bootstrap`, `.workbench`, caches, downloaded third-party sources, or filled profiles.

Also run `python scripts/check_repository.py` and `python scripts/check_installation.py`. The latter exercises the real offline launcher and copied engine; `--online` installs and checks actual core/figures packages in a disposable workspace. CI runs preservation and offline checks on Windows/macOS/Linux with Python 3.11, 3.12, and 3.14, and actual runtime checks with Python 3.12. See [maintenance priorities](docs/MAINTENANCE.md).

Review pinned versions, hashes, license terms, and required shared resources when changing registry.json. Preserve private settings and human edits. Record operating system, Python, selected profiles, actual checks, and untested boundaries in the compatibility record. A source-code review is not a Windows execution test.
