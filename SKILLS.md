# Skills: catalog, candidates, and past checks

Use [SETUP.md](SETUP.md) to select for a task and [Automation](docs/AUTOMATION.md) for profile IDs. This page separates what the installer offers from manual candidates and historical results.

## Current catalog

Repository 0.3.1 installs two original MIT-licensed foundation skills: `research-workbench` for setup and `research-reading` for source-linked notes. Optional bundles are defined in [registry.json](registry.json).

| Source | Automatic scope | Limits |
| --- | --- | --- |
| Nature Skills | Literature search/reference checks; writing, polishing, and required shared files | Pinned Apache-2.0 root license; nested material may differ |
| Scientific Agent Skills | MATLAB guidance, SymPy, units/uncertainty | Pinned MIT source and individual file hashes; MATLAB itself is not installed |
| PaperQA | Optional local-paper question answering runtime and original research-paperqa skill | Model/embedding services, data-sharing scope, cost, and cited-claim support need task checks; see [workflow](docs/PAPERQA.md) |
| Python packages | Core PDF reading and selected computation/plotting environments | Direct versions pinned; resolved versions recorded per runtime |

Source revisions, hashes, authors, and license evidence live in the registry and [third-party inventory](THIRD_PARTY.md). Automatic installation uses those pins; review and verification are required to update them.

**Excluded:** ARS uses CC BY-NC 4.0 at the reviewed revision and needs intended-use review before manual installation. `nature-figure` is withheld pending permission for its nested `figures4papers` assets; `figures` installs only the plotting runtime. Earlier local installations are not removed.

Files matching a source, dependencies loading, host discovery, and a real task passing are separate checks. Skills do not supply accounts, MATLAB licenses, institutional access, model services, or every upstream optional integration.

## Manual candidates

The guide lists exact candidate paths. Nature modules were reviewed at `84880815fb37317b3766bff2c2abba395b8993c3` on 2026-10-02; a complete clean installation and workflow test of every module was not performed.

| Need | Nature directories under `skills/` | Check |
| --- | --- | --- |
| Search / full text | `nature-academic-search`, `nature-downloader` | Coverage and lawful access |
| Reading / paper analysis | `nature-reader`, `nature-paper-card` | Shared dependencies and actual source scope |
| Writing / polishing | `nature-writing`, `nature-polishing` | `nature-shared`, evidence, terminology, claim strength |
| Reference metadata | `nature-ref-verifier` | Metadata does not prove claim support |
| Figures / presentations | `nature-figure`, `nature-paper2ppt` | Figure assets withheld; review presentation dependencies separately |

Read the chosen revision's instructions and cross-directory references. A historical revision is not proof that a newer one works. Manual selections need their own source, license, dependency, cost, and host checks.

## Historical local checks

These results describe one macOS maintenance environment on 2026-10-02, not another user's clean setup. All listed skill directories matched upstream hashes.

| Skill | Additional check | Still unverified |
| --- | --- | --- |
| `academic-research-suite` | Files only | Target-task effectiveness and other agents |
| `matlab` | Files only | Executable, license, toolboxes, model execution |
| `sympy` | Basic differentiation | User assumptions, derivation, and task |
| `uncertainty-and-units` | Power units, incompatible-unit rejection, simple propagation | User data and uncertainty model |
| `codex-autoresearch` | Files only; no experiment started | Host invocation and constrained experiment |

Recorded sources and paths:

- [ARS Codex](https://github.com/Imbad0202/academic-research-skills-codex), `skills/academic-research-suite`: `70b412fe69d3b5bf6b16adf64a96160bdd3c2d28`.
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills), `skills/matlab`, `skills/sympy`, `skills/uncertainty-and-units`: `154988403bb5a18e9d3c0ce4e6d5e2e4b184a298`.
- [Codex Autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch), repository root: `0f54c571707487f59486ba7c50d405edfc746c19`.

Calculation environment: Python 3.14.4, SymPy 1.14.0, NumPy 2.4.4, SciPy 1.17.1, Pint 0.26.1, uncertainties 3.2.3. These are historical facts, not universal requirements.

For updates, inspect/back up local changes, check only the needed modules, and record old/new revisions, date, and results. Mark unknown costs unconfirmed. Add platform evidence to [compatibility](docs/COMPATIBILITY.md).
