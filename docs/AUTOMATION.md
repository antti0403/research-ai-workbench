# Installer reference

The AI selects tools for the task; the engine installs explicit catalog profiles. It does not infer a discipline or call a model API. For the initial user flow see [README](../README.md); for agent-led decisions see [SETUP](../SETUP.md).

## Commands

From the extracted distribution, use Python 3.11+ and replace example paths:

```bash
python workbench.py plan
python workbench.py setup --workspace "/path/to/project"
python workbench.py plan --workspace "/path/to/project" --profile "/path/to/profile.json"
python workbench.py apply --workspace "/path/to/project" --profile "/path/to/profile.json"
python workbench.py doctor --workspace "/path/to/project"
```

| Command | Behavior |
| --- | --- |
| `plan` | Read-only catalog or profile inspection |
| `setup` | Foundation files, PDF runtime, checks, and agent handoff |
| `setup --offline` | Prepare files without downloads; runtime checks remain pending |
| `apply` | Recheck foundation, install selected extensions, continue unaffected profiles after failure |
| `doctor` | Check installation and report current failures |

Repeat setup/apply to resume. Empty extension lists are valid; a smaller list does not uninstall earlier profiles.

After setup, use the interpreter and engine paths recorded in `START_HERE.md`. For repository 0.2.3, from the workspace:

```bash
# macOS / Linux
.workbench/envs/core/bin/python .workbench/kit/0.2.3/workbench.py doctor --workspace .
```

```powershell
# Windows PowerShell
& .\.workbench\envs\core\Scripts\python.exe .\.workbench\kit\0.2.3\workbench.py doctor --workspace .
```

Keep the workspace at its original path; virtual environments need rebuilding after a move. Keep `.workbench/bootstrap/` if Python was downloaded there, or the reused external Python installation. The original source download is unnecessary once setup succeeds.

## Profiles

Start with [profile.example.json](../profile.example.json). Only `extensions` selects installer actions; entries must be catalog IDs. Other answers are context for the AI.

| ID | Prepared | Check for the actual task |
| --- | --- | --- |
| `literature` | Search and reference-checking skills | Coverage, connections, optional dependencies |
| `writing` | Writing, polishing, and shared skills | Evidence, document tools, target format |
| `symbolic` | SymPy skill and environment | Assumptions and derivation |
| `units` | Units/uncertainty skill and environment | Measurement model and inputs |
| `matlab` | MATLAB guidance skill | Runtime, toolboxes, license |
| `data` | NumPy, pandas, SciPy, Matplotlib environment | Data quality, method, interpretation |
| `figures` | NumPy and Matplotlib environment | Data and figure design; `nature-figure` withheld pending nested permissions |

Use each profile's recorded interpreter. Optional integrations mentioned by upstream skills are not all installed. Review needs outside the catalog with SETUP's source, license, and dependency checks.

## Records and verification

| Location | Purpose |
| --- | --- |
| `START_HERE.md` | Agent handoff and actual engine/interpreter paths |
| `workbench-config.md` | Research context, task results, remaining gaps |
| `.workbench/profile.json` | Private answers and selected extensions |
| `.workbench/state.json`, `.workbench/install-report.md` | Machine history/hashes and readable status |
| `.workbench/kit/0.2.3/` | Copied engine, guide, source/license records |
| `.workbench/envs/`, `.workbench/locks/` | Profile runtimes and resolved package versions |
| `.agents/skills/` | Project skill files |

**Files verified** means source files match the selected revision. **Runtime verified** means a small functional check passed. **Task checks pending** means host discovery and the user's workflow still need checking. No state proves a scientific conclusion.

## Preservation and recovery

Existing notes/configuration are preserved. `AGENTS.md` is backed up before the workbench block is appended. Conflicting skill or kit files require review. State writes are atomic; a lock blocks simultaneous installs. For a stale lock or malformed state, use [troubleshooting](TROUBLESHOOTING.md).

Before apply, the engine rechecks foundation files and the current PDF interpreter. Historical success alone is insufficient. Normal bytecode beside Python source is ignored; changed sources, unexpected scripts, and links still fail integrity checks.

Automatic runtime repairs require matching ownership tokens in state and `.workbench/envs/<profile>/.workbench-owner.json`. A working unowned legacy environment can be checked/reused; its packages are not changed and it is not adopted. Failed unowned runtimes need reviewed replacement or a new workspace.

Unchanged installer-owned `START_HERE.md` is backed up and updated for the current kit. Human edits are preserved; current instructions go to `START_HERE-0.2.3.md`. Older schema-1 state remains readable without granting runtime ownership. State/profile JSON accepts a UTF-8 BOM; malformed state is preserved for recovery.

Skill revisions/hashes and direct package versions are pinned in [registry.json](../registry.json); transitive versions are recorded after installation. This is not a fully hash-locked offline distribution. Missing compatible binary wheels stop installation.

## Access and host limits

Downloads use public GitHub, PyPI, and Astral sources. The installer does not upload research, open paid accounts, or request credentials. Crossref sends the supplied search query; the agent's own data policies apply.

The user handles login, institutional authorization, and paid choices. AI apps, commercial MATLAB, native office apps, large models, and a full local TeX distribution are not bundled. Reuse existing host capabilities first.

Codex project discovery uses `.agents/skills/`; verify invocation in the target host. Other agents may read instructions explicitly, but native discovery needs checking. See the [Codex skills guide](https://learn.chatgpt.com/docs/build-skills) and [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/).
