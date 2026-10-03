# Foundation first, then personalization

Version 0.2.2 separates machine preparation from research decisions. The installer does not guess a discipline. The user's existing AI interprets a few answers and selects documented extensions. No extra model API is built into the installer.

## User journey

1. Download and extract the repository. Run `bash install.sh` on macOS/Linux or `.\install.ps1` in Windows PowerShell. A suitable Python 3.11+ is reused. Otherwise, the launcher uses a fixed, checksum-verified Astral uv installer to obtain Python locally.
2. The installer creates the workspace, project instructions, two original skills, and an isolated PDF-reading environment. It tests PDF extraction and writes the actual outcome.
3. Open that workspace in an AI agent. Ask it to read `START_HERE.md` and personalize the workbench.
4. The AI asks only for missing information, usually in three groups: your next research output; your methods and existing tools; your platform, access, language, and other constraints. It can ask a focused follow-up when correctness depends on it.
5. The AI writes a local profile and checks the proposed selection. Existing authorization is reused. It installs selected extensions and checks a real task. Unclear needs can be deferred without blocking the foundation.

For example, a researcher doing interviews may need reading and writing support without numerical libraries. Someone deriving equations can add symbolic mathematics. Someone analysing measurements can add units, uncertainty, data analysis, and figures. These are examples of decisions, not a fixed mapping from discipline names to software.

## Local commands

Run these from the extracted distribution with a suitable Python. Replace example paths with actual paths:

```bash
python workbench.py plan
python workbench.py setup --workspace "/path/to/project"
python workbench.py plan --workspace "/path/to/project" --profile "/path/to/profile.json"
python workbench.py apply --workspace "/path/to/project" --profile "/path/to/profile.json"
python workbench.py doctor --workspace "/path/to/project"
```

`plan` is read-only. `setup --offline` writes foundation files without downloading packages; incomplete checks remain pending. `apply` requires a verified foundation. It continues other selected profiles when one fails. Repeating `apply` retries incomplete work and checks existing installations. Selection of an empty list is valid. Applying a smaller selection does not uninstall earlier extensions.

After setup, the engine is copied into `.workbench/kit/0.2.2/`. The installed Python path appears in `START_HERE.md`. From the workspace on macOS/Linux, for example:

```bash
.workbench/envs/core/bin/python .workbench/kit/0.2.2/workbench.py doctor --workspace .
```

On Windows use `.workbench\envs\core\Scripts\python.exe` for that interpreter. The workspace must stay at its original path: Python virtual environments are not portable. Rebuild environments after moving a workspace. When Python was downloaded automatically, it lives under `.workbench/bootstrap/`; keep that directory. After a successful setup, the original download folder is no longer needed by the installed engine. An externally reused Python installation must still remain available.

## Profile and extensions

Use [profile.example.json](../profile.example.json). Only the `extensions` list controls the installer's selected actions. Its entries must match the catalog. Other answers supply context for the AI and are not executable instructions.

| ID | Files and runtime prepared | What remains task-specific |
| --- | --- | --- |
| `literature` | Academic search and reference verification skills | Database connections, coverage, optional workflow dependencies |
| `writing` | Shared, writing, and polishing skills | Author evidence, document tools, manuscript requirements |
| `symbolic` | SymPy skill and isolated SymPy environment | Mathematical assumptions and actual derivation |
| `units` | Units/uncertainty skill and isolated libraries | Measurement model and justified uncertainty inputs |
| `matlab` | MATLAB guidance skill | MATLAB or compatible runtime, required toolboxes, license |
| `data` | NumPy, pandas, SciPy, and Matplotlib environment | Method selection, data quality, interpretation |
| `figures` | NumPy and Matplotlib environment; nature-figure withheld pending nested-asset permissions | Data, figure design, journal requirements, any additional packages |

Use the recorded environment for its task. A skill may document additional integrations; installing the selected profile does not install every optional dependency mentioned upstream. The AI checks only the dependencies needed for the chosen task. Needs outside the catalog go through the source and license review in [SETUP.md](../SETUP.md).

## Records and verification

| Location | Purpose |
| --- | --- |
| `START_HERE.md` | Agent handoff and actual interpreter paths |
| `workbench-config.md` | Human-readable research context and task acceptance |
| `.workbench/state.json` | Machine installation history and file hashes |
| `.workbench/install-report.md` | Readable component status |
| `.workbench/profile.json` | Local answers and selected extensions |
| `.workbench/envs/` | Separate runtime for each configured profile |
| `.workbench/kit/0.2.2/NOTICE.md`, `THIRD_PARTY.md`, `SKILLS.md` | Retained source, attribution and license-scope documentation |
| `.workbench/envs/<profile>/.workbench-owner.json` | Matches the runtime ownership token in state; required before automatic repairs |
| `.workbench/locks/` | Resolved installed package versions |
| `.agents/skills/` | Project-scoped skill files |

**Files verified** means the installed files match the selected source. **Runtime verified** means the specified small functional check passed. **Task checks pending** means the AI still needs to confirm skill discovery and the user's actual workflow. None of these states proves a scientific conclusion.

Existing notes and configuration are preserved. Existing `AGENTS.md` content is backed up before appending the workbench block. A different same-name skill or modified installed engine is preserved and requires review. State files are written atomically, and a lock prevents simultaneous installation. A killed process can leave a stale lock; see [recovery](TROUBLESHOOTING.md).

Applying extensions rechecks the foundation skills and current PDF interpreter. A historical verified entry is insufficient. Normal Python bytecode caches beside source files are excluded from skill comparisons; changed sources and unexpected scripts still fail verification.

New runtimes receive matching ownership records in state and inside the environment before creation. An existing environment without these records may be checked and reused if it passes, but the installer will not change its packages or rebuild it. A diagnostic entry alone does not establish ownership. Failed legacy runtimes require a reviewed backup/replacement or a new dedicated workspace.

Version 0.2.2 reads older schema-1 state without claiming ownership of old environments. Unchanged installer-owned `START_HERE.md` is backed up and updated to the current engine. Edited entry points are preserved, with current instructions in `START_HERE-0.2.2.md`. Other conflicting human or skill files still require review. Profiles and state accept an optional UTF-8 BOM; malformed state is preserved with a controlled recovery error.

Skill revisions and file hashes are fixed in [registry.json](../registry.json). Direct runtime package versions are pinned; their resolved transitive versions are recorded after installation. This is not a fully hash-locked or offline package distribution. The runtime installer uses available binary wheels and stops if a compatible wheel is unavailable.

## Access and boundaries

The installer downloads public dependencies from GitHub, PyPI, and Astral's distribution. It does not upload research files, open paid accounts, or request credentials. Crossref search transmits the supplied search query. The agent's own hosting and data policies still apply.

The user completes account login, institutional authorization, and paid choices. Skills do not grant access to subscription papers. The AI application, commercial MATLAB, native office applications, large models, and a full local TeX distribution are not bundled. Check the agent's existing capabilities before adding software.

Codex uses project skills in `.agents/skills/`. Other agents can read their instructions explicitly, but their native discovery and permissions need verification. See the [official Codex skills guide](https://learn.chatgpt.com/docs/build-skills) and [uv installation documentation](https://docs.astral.sh/uv/getting-started/installation/).
