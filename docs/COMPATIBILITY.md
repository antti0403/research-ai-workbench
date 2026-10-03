# Compatibility and verification

Updated: 2026-10-03 for repository 0.2.4. Tests use temporary workspaces and synthetic or public inputs, separate from private research. Results below retain the release actually tested.

## 0.2.4 project overview

Local Windows repository validation and actual offline launcher/copied-engine checks passed. A canonical-source 0.2.3→0.2.4 offline upgrade/resume preserved the earlier kit, human notes/configuration/instructions, and skill files. Only the README and release metadata changed; use CI for the proposed commit's unit and online runtime results.

## 0.2.3 documentation release

Local Windows checks on Python 3.12.14 passed repository syntax/link/version validation, 39 existing tests (37 passed, two platform-related skips), and actual offline launcher/copied-engine preparation. An isolated offline upgrade from canonical 0.2.2 sources to 0.2.3 retained both guide versions, preserved human notes, configuration, instructions and skill files, updated the owned entry point, and resumed successfully. Runtime dependencies remained honestly pending. This release changes documentation and kit metadata; runtime behavior and dependency pins are unchanged. See the CI results below for each exact commit's separate online checks.

## Earlier release evidence

The full runtime table below describes 0.2.0; later changes and their checks are recorded first.

The 0.2.2 Windows regression suite ran 39 tests on Python 3.12.14: 37 passed; two were skipped (privileged symbolic-link creation and a POSIX-only interpreter-link test). The suite exercised real Windows junctions, actual bytecode generation, canonical/relative skill paths, fresh foundation checks, runtime ownership and simulated repair failures, BOM/invalid JSON, Unicode output, and legacy/edited entry-point preservation. Mocked repair tests do not prove a real dependency installation.

On Windows with Python 3.12.14 and the existing PowerShell 7 shell, both actual launcher smoke checks passed: offline preparation/resume and online core/figures installation, PDF/PNG functional checks, copied-engine setup/doctor/apply, repeated apply, spaces/non-ASCII paths, and preservation of human instructions and notes. The computer's normal Windows PowerShell 5.1 policy blocked script execution; no policy was changed. CI includes a separate 5.1 launcher check under the runner's existing policy. These are isolated installer checks, not host discovery or research acceptance.

The new [CI workflow](../.github/workflows/ci.yml) defines Windows/macOS/Linux preservation and offline-launcher checks on Python 3.11, 3.12, and 3.14, plus separate actual core/figures installation and resume checks on Python 3.12. Consult the [run results](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml) for each exact commit; configured coverage is not itself a passing result. Missing-Python bootstrap, other extension integrations, host discovery, and independent research acceptance remain outside these CI checks.

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
| Windows and Linux (0.2.0 historical scope) | Launchers or shared engine were provided; no runtime test in these operating systems was performed for 0.2.0. Current Windows 0.2.2 results are above; current CI results are linked separately. |
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
