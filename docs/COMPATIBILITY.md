# Compatibility and verification

Updated: 2026-10-22 for repository 0.3.8. Tests use temporary workspaces and synthetic or public inputs, separate from private research. Results below retain the release actually tested.

## 0.3.8 progressive reading and research continuation

Local checks on macOS arm64 / Python 3.14.4 passed the 55-test suite (54 passed,
one Windows-only skip), repository syntax/link/version checks, both changed
skill-format checks, Bash syntax, the numerical example, and the actual offline
launcher/copied-engine preparation. Five real historical snapshots (both 0.3.0
variants, 0.3.1, 0.3.2, and 0.3.7) upgraded and repeated successfully in disposable
workspaces. Checks retained old kits and human rules/configuration/notes, verified
new foundation bytes and whole-tree backups, and refused edited old skills.

New regression cases exercise refusal of missing/extra/edited or unowned files,
invalid provenance, same-version changes and downgrades, directory-replacement
rollback, state-write retry, and partial upgrades. Current foundation checks do
not accept an old pristine skill merely because the global state version changed.
Dependency pins, profiles, and upstream source records are unchanged. Local online
package installation was not repeated; use the [PR's exact current-commit CI](https://github.com/antti0403/research-ai-workbench/pull/7/checks)
for Windows/macOS/Linux preservation and online-runtime evidence.

Controlled forward attempts used only the changed reading skill, original raw
synthetic fixture, and case requests; the answering agents were not given the
acceptance criteria. Inspection found:

- The mechanism answer preserved the feedback signs, combined process input,
  equilibrium, nonzero error, source locations, and scope. Source provenance was
  partial: it identified a toy, dimensionless source but did not explicitly call
  it a synthetic text diagram. It made no unsupported image/PDF inspection claim.
- The correction used draft 1.1, withdrew the old zero-error claim, retained the
  human comment, and edited the existing note/index without another tracker.
  The follow-up stopped deeper reading, deferred stability work, and recorded
  the next comparison task without claiming execution or complete understanding.
- The comparison answer distinguished all four evidence kinds, preserved the
  numerical differences, and rejected a ranking from unequal conditions.
- A fresh agent given only the saved note and index recovered the next task,
  deferred work, and performed algebraic check. It explicitly retained the gap
  that the underlying source excerpt had not been opened in that fresh session.

These are maintainer-controlled synthetic observations, not independent user
acceptance, native host-discovery testing, a before/after quality comparison, or
validation of a real scientific conclusion. Responses stayed outside the source
repository. The [case protocol](RESEARCH_ACCEPTANCE.md) supplies reproducible
requests and criteria for further checks.

## 0.3.7 current-conversation default

The `watermarks` profile prepares its bundled Skill without downloading a
service, creating API configuration, or requesting another model. The active
conversation performs ordinary revisions. `watermarks-api` explicitly opts in
to the retained standalone service; its existing API-wiring check remains in
online CI. Offline preparation/resume and exact-head CI are checked separately
from actual passage revision quality and vendor-watermark detection.

## 0.3.6 service launch and CI repair

The 0.3.5 Windows runtime job failed because `execve` split a path containing
spaces. The 0.3.4 macOS runtime job exceeded the 15-second startup allowance.
The launcher now runs the unchanged upstream service in its own process,
keeping argument boundaries and process termination consistent across platforms.
The fixture uses spaces and Unicode, checks that shutdown closes the listener,
and reports service diagnostics if the 60-second readiness deadline is exceeded.
Exact commit CI results determine platform verification.

## 0.3.5 service credential scope and macOS trust

The live service/API-wiring fixture passes with the provider key absent from
the local client's environment. Only the service process needs that key.
Local unit, repository, and release-preservation checks pass. On a macOS
Python.org build with no configured CA file, HTTPS certificate verification
failed before provider authentication. The macOS system CA bundle verifies the
provider's TLS connection; the service uses it only when no bundle is configured.
No TLS verification is disabled and no global trust setting is changed.

## 0.3.4 full watermarks-remover integration

Local macOS checks on 2026-10-15 passed 48 unit tests (47 passed, one
Windows-only skip), skill-format and repository syntax/link/version checks,
offline launcher/copied-engine preparation, and five previous-release upgrades.
The selected full upstream client/service sources were downloaded and checked
against per-file and license hashes. The installed full HTTP service executed
a Layer B paraphrase request against a controlled loopback API responder,
retained the original, wrote a candidate/report, refused existing outputs,
and rejected missing backend configuration. This checks real service/API
wiring with synthetic inputs, not an actual language model or watermark result.

The optional profile is included in copied-engine online runtime CI checks.
Use the exact PR commit's job results for platform evidence. The maintainer's
chosen real model API is not yet configured; real provider execution, factual
revision quality, native host discovery, and vendor-key watermark verification
remain separate pending checks. No paid model call or local model download
was made for this integration.

## 0.3.3 writing-profile integration

Local macOS checks on 2026-10-15 passed skill-format validation, repository
syntax/link/version checks, 45 unit tests (44 passed, one Windows-only skip),
offline launcher/copied-engine preparation, and the synthetic numerical example.
Four previous-release upgrade/resume checks, including 0.3.2, preserved old kits,
foundation skills, and human files. New tests exercise writing-profile selection,
offline copied-engine installation and repeat apply of the adapted skill and its
MIT license, pending upstream downloads, and preservation of edited writing
principles and research notes. Runtime dependencies and foundation skill bytes
are unchanged. These local checks do not establish native host discovery or
manuscript quality; inspect the exact PR commit's CI for other platform results.

## 0.3.2 optional literature workflow

This release adds original integration instructions for a connected Undermind service, generated entry-point routing, and kit/guide metadata. Foundation skill bytes, profile selection, and runtime dependency pins remain unchanged. No hosted service, model, subscription, or institutional access is installed by this release.

Local macOS arm64 checks on Python 3.14.4 passed the 43-test suite (42 passed, one Windows-only skip), source syntax/version/link checks, Bash syntax, the synthetic example, actual offline launcher/copied-engine preparation, and three previous-release upgrade/resume cases including canonical 0.3.1. These retained old kits, existing foundation skills, human instructions, configuration, and notes. Runtime pins are unchanged; local online dependency installation was not repeated.

Prior platform results retain their original release scope. Current-commit CI and real Undermind connection/search/full-text acceptance are separate evidence; adding instructions does not prove every user's account or full research workflow works.

## 0.3.1 release and first-task checks

Local Windows checks on Python 3.12.14 passed 43 tests (41 passed, two platform-related skips), repository metadata/syntax/link checks, actual offline launcher and copied-engine preparation, and offline upgrade/resume from both the released 0.3.0 and the later bilingual README commit. Canonical snapshots retained previous kits, existing skill bytes, human instructions, configuration, and notes. The new copied kit contains both READMEs and passes its own repository/link checker.

The data/figures profiles now declare Python 3.12+. Incompatible new environments are refused before creation or package installation; offline preparation remains pending. Existing environments are checked with their own interpreter and preserved for reviewed recovery if incompatible. CI's Python 3.11 release checks exercise the real refusal path; actual package runtime jobs still use Python 3.12. Platform wheel availability remains a separate requirement.

The full-text example checks one selected methods passage and equation in arXiv:1706.03762v7, with PDF extraction and an HTML equation check. Its standard-library synthetic calculation passed for three dimensions and an equal-score case. This is a selected-claim demonstration, not reproduction of model training or a PaperQA model query. CI now executes the numerical example, previous-kit upgrade checks, installed bilingual links, and the actual first-PDF shell commands. Consult the exact run results for platform success; configured jobs alone are not evidence.

The complete Windows online launcher/copied-engine check also passed: actual documented PowerShell PDF commands against a synthetic two-page PDF, core/figures/PaperQA installation, repeated apply, doctor, CLI invocation, and preservation. The blank-page tutorial fixture verifies page selection and the explicit no-text/OCR limitation; the separate core/PaperQA checks verify actual text extraction. No model services or private research were used.

## 0.3.0 optional PaperQA module

Local Windows checks on Python 3.12.14 passed 41 tests (39 passed, two platform-related skips), repository syntax/link/version checks, actual offline launcher/copied-engine preparation, and canonical-source 0.2.4→0.3.0 offline upgrade/resume. The upgrade retained both kits and preserved human instructions, notes, configuration, and existing foundation skills. New tests cover optional bundled-skill installation through the copied engine, offline pending status, repeat apply, and preservation of an edited PaperQA skill.

The pinned PaperQA package installed into an isolated Windows environment. Its local smoke check ingested an actual synthetic PDF, checked duplicate handling, retained page-linked evidence/citation/content hash, and round-tripped session JSON with outbound connections blocked and model adapters rejecting calls. The documented named settings also loaded through the actual `pqa --settings research view` CLI. No paper question was sent to a model.

The complete copied-engine online test exercised core/figures/PaperQA installation, repeated apply, doctor, CLI invocation, and human-file preservation in a deep Windows path with spaces and Unicode. Initial ordinary pip installation failed on deeply nested LiteLLM files with system long-path support disabled. The PaperQA interpreter now uses Windows extended paths for pip and runtime checks, without changing system policy; actual installation/resume and CLI checks passed with that handling. Test cleanup also handles extended paths. Other architectures, UNC/network shares, and PaperQA on Python versions other than 3.12 remain unverified locally.

The three-platform Python 3.12 runtime CI jobs now include PaperQA installation and these local evidence checks; use the [exact run results](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml) for cross-platform evidence. Configured coverage alone is not a passing result. Retrieval relevance, real model/provider connections, generated-answer quality, native host discovery, and scientific claim acceptance remain unverified.

## 0.2.4 project overview

Local Windows repository validation and actual offline launcher/copied-engine checks passed. A canonical-source 0.2.3→0.2.4 offline upgrade/resume preserved the earlier kit, human notes/configuration/instructions, and skill files. Only the README and release metadata changed; use CI for the proposed commit's unit and online runtime results.

## 0.2.3 documentation release

Local Windows checks on Python 3.12.14 passed repository syntax/link/version validation, 39 existing tests (37 passed, two platform-related skips), and actual offline launcher/copied-engine preparation. An isolated offline upgrade from canonical 0.2.2 sources to 0.2.3 retained both guide versions, preserved human notes, configuration, instructions and skill files, updated the owned entry point, and resumed successfully. Runtime dependencies remained honestly pending. This release changes documentation and kit metadata; runtime behavior and dependency pins are unchanged. See the CI results below for each exact commit's separate online checks.

## Earlier release evidence

The full runtime table below describes 0.2.0; later changes and their checks are recorded first.

The 0.2.2 Windows regression suite ran 39 tests on Python 3.12.14: 37 passed; two were skipped (privileged symbolic-link creation and a POSIX-only interpreter-link test). The suite exercised real Windows junctions, actual bytecode generation, canonical/relative skill paths, fresh foundation checks, runtime ownership and simulated repair failures, BOM/invalid JSON, Unicode output, and legacy/edited entry-point preservation. Mocked repair tests do not prove a real dependency installation.

On Windows with Python 3.12.14 and the existing PowerShell 7 shell, both actual launcher smoke checks passed: offline preparation/resume and online core/figures installation, PDF/PNG functional checks, copied-engine setup/doctor/apply, repeated apply, spaces/non-ASCII paths, and preservation of human instructions and notes. The computer's normal Windows PowerShell 5.1 policy blocked script execution; no policy was changed. CI includes a separate 5.1 launcher check under the runner's existing policy. These are isolated installer checks, not host discovery or research acceptance.

The new [CI workflow](https://github.com/antti0403/research-ai-workbench/blob/main/.github/workflows/ci.yml) defines Windows/macOS/Linux preservation and offline-launcher checks on Python 3.11, 3.12, and 3.14, plus separate actual core/figures installation and resume checks on Python 3.12. Consult the [run results](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml) for each exact commit; configured coverage is not itself a passing result. Missing-Python bootstrap, other extension integrations, host discovery, and independent research acceptance remain outside these CI checks.

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
