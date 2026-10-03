# Skill sources and verification scope

See [SETUP.md](SETUP.md) for selection criteria. This file records known revisions and checks for maintenance. **A recorded version is neither a requirement to install an old release forever nor evidence that a newer release has been tested.** Review changes at installation time and record the chosen revision.

Track source review, file installation, runtime dependencies, host discovery, and real task execution separately. Passing one stage does not establish the next.

## Skills with local installation records

These records come from a macOS maintenance environment on 2026-10-02. Setup was not repeated in another user's clean environment.

| Skill | Repository and path | Recorded commit | Checks performed | Still unverified |
| --- | --- | --- | --- | --- |
| academic-research-suite | [ARS Codex](https://github.com/Imbad0202/academic-research-skills-codex), `skills/academic-research-suite` | `70b412fe69d3b5bf6b16adf64a96160bdd3c2d28` | Complete directory matched upstream file hashes | Effectiveness for the target research task; other agents |
| matlab | [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills), `skills/matlab` | `154988403bb5a18e9d3c0ce4e6d5e2e4b184a298` | Complete directory matched upstream file hashes | MATLAB executable, license, toolboxes, and actual model execution |
| sympy | Same repository, `skills/sympy` | `154988403bb5a18e9d3c0ce4e6d5e2e4b184a298` | File integrity and basic symbolic differentiation | User-specific assumptions, derivations, and task |
| uncertainty-and-units | Same repository, `skills/uncertainty-and-units` | `154988403bb5a18e9d3c0ce4e6d5e2e4b184a298` | Integrity; power-unit calculation; rejection of incompatible units; simple uncertainty propagation | User data and uncertainty model |
| codex-autoresearch | [codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch), repository root | `0f54c571707487f59486ba7c50d405edfc746c19` | Complete directory matched upstream file hashes | Host invocation and a constrained experiment workflow; no automatic experiment started |

Recorded calculation environment: Python 3.14.4, SymPy 1.14.0, NumPy 2.4.4, SciPy 1.17.1, pint 0.26.1, uncertainties 3.2.3. These describe one environment, not universal requirements. Basic calculations are not acceptance of an entire skill workflow.

## Candidate modules

[Nature Skills](https://github.com/Yuan1z0825/nature-skills) directories and shared dependencies were reviewed on 2026-10-02 at reference commit `84880815fb37317b3766bff2c2abba395b8993c3`. A clean installation and full workflow test of all modules at that revision have not been completed for this repository.

| Purpose | Subdirectories under `skills/` | Dependencies and limits |
| --- | --- | --- |
| Search and full text | nature-academic-search, nature-downloader | Check database coverage, network access, and lawful full-text rights |
| Reading and detailed analysis | nature-reader, nature-paper-card | Check nature-shared for reader; state partial access explicitly |
| Writing and polishing | nature-writing, nature-polishing | Check nature-shared; preserve facts, terminology, and claim strength |
| Citation verification | nature-ref-verifier | Correct bibliography does not prove support for a claim |
| Figures and presentations | nature-figure, nature-paper2ppt | Check libraries and output formats; check nature-shared for paper2ppt |

Use the README, SKILL.md, and cross-directory references from the selected revision when repositories change. Other agents need their own supported directories and installation methods.

## Costs, access, and updates

Skill files do not include model services, MATLAB licenses, institutional access, or third-party APIs. The setup AI must identify required accounts and current costs for selected workflows. Mark unknown costs unconfirmed rather than promising everything is free.

Before updating, inspect and back up local changes. Update modules the current task needs, then recheck affected functions. Record date, old and new versions, and results. Record platform tests in [compatibility and verification](docs/COMPATIBILITY.md).
