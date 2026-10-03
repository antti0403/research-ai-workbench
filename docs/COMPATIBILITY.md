# Compatibility and verification

Updated: 2026-10-03 for repository 0.2.1. Tests used temporary workspaces and synthetic or public inputs, separate from private research. Full runtime results below were obtained for 0.2.0; they are historical evidence, not a new full installation of 0.2.1.

The 0.2.1 attribution patch passed 16 automated tests and the Bash syntax check. The tests verify that source/license documents remain in the installed kit, root and nested notices survive skill extraction, and the figures profile keeps its plotting runtime without requesting the withheld skill. Internal documentation links and direct dependency/source coverage were checked. Runtime package pins and launchers are unchanged. No additional Windows/Linux or personal research acceptance test was performed.

| Environment or capability | Actual result and limits |
| --- | --- |
| macOS arm64, existing Python 3.14.4 | Foundation installation passed. PDF generation/extraction check passed. |
| macOS arm64, automatic runtime path | Forced the missing-Python branch, downloaded uv 0.12.22 and managed CPython 3.12.15 into the workspace, then installed and verified the foundation. This is a branch test on the maintainer's computer, not a clean-machine trial. |
| Workspace path containing spaces | Automatic runtime download and setup passed. |
| Resume through installed engine | Reran setup using the copied engine and its core interpreter from the workspace; passed without needing the original source directory. |
| Core PDF helper | Synthetic PDF text round trip passed; OCR and complex scientific page layout remain outside this check. |
| Metadata search | One live Crossref request returned parseable bibliographic results. Search ranking, paper identity, and claim support require source checks. |
| Symbolic mathematics | Skill integrity and pinned environment installation passed; derivative and equation checks passed. |
| Units and uncertainty | Skill integrity and environment installation passed; power units, incompatible-unit rejection, and uncertainty checks passed. |
| Literature, writing, and MATLAB skills | Complete selected files and retained licenses matched recorded sources. Host discovery, workflow-specific dependencies, writing quality, and MATLAB runtime/license were not verified. |
| Data analysis | Pinned environment installed; small numerical and exported-figure checks passed. This does not validate a real statistical analysis. |
| Figure profile (0.2.0 historical result) | Skill files and pinned plotting environment installed; numerical and PNG export checks passed. In 0.2.1 the skill is withheld because of nested-asset permissions; runtime pins remain unchanged. A functional test does not establish redistribution rights. |
| Failure and preservation tests | 15 automated tests passed: human-content preservation, repeated offline setup, modified skills, read-only planning, profile validation, prerequisite enforcement, path/archive checks, complete skill resources and licenses, corrupt state, concurrent installation, download integrity, partial profile failure, installed-engine operation, and honest doctor failure reporting. |
| Original skill format | Both bundled skills passed the local skill format validator. Native invocation in a new host session remains unverified. |
| Shell launcher | Bash syntax check and actual macOS execution passed. |
| Windows and Linux | Launchers or shared engine provided; no runtime test in these operating systems was performed. PowerShell execution remains unverified. |
| Other AI agents | Explicit instruction-reading fallback documented; native skill discovery and permissions must be checked for each host. |
| Complete setup for another user | No independent user acceptance trial recorded. |

## What the checks mean

A passing runtime test proves a small supported operation in the tested environment. It does not prove that every upstream skill integration is available or that research conclusions are correct. A file hash proves file integrity against the selected source, not source quality.

The installer pins direct package versions and records resolved dependencies. Availability on other architectures or Python versions can differ. It does not silently replace a working global runtime or compile missing native packages from source.

## Contribute a useful test

Download the full distribution in the target environment. Run setup and choose one small real task. Record the operating system, agent version, existing software, added revisions, actual commands and outputs, failed checks, and recovery. Confirm discovery, open saved outputs, and test resuming. Do not publish personal paths, account details, private research, or keys.

```text
Date:
Operating system, architecture, Python, and agent version:
Existing environment and items added:
Task and public example link:
Selected profiles, skill revisions, and dependencies:
Steps performed and passed:
Failures and actual errors:
Retry or recovery results:
Host discovery and task acceptance:
Unverified parts:
```
