# Research AI Workbench

[![Installer checks](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml/badge.svg)](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml)

A local setup toolkit for AI-assisted research, with a Python installer and a standalone setup guide.

It prepares a workspace for reading, notes, and research outputs. Your existing AI agent then selects extensions for your next task.

## Features

- **Research foundation:** project folders, persistent instructions, two original research skills, and an isolated PDF-reading runtime.
- **Optional extensions:** literature search, [PaperQA evidence questions](docs/PAPERQA.md), writing, symbolic mathematics, units, MATLAB guidance, data analysis, and plotting.
- **Resumable setup:** recorded checks, isolated environments, and preservation of existing files and settings.
- **Agent-led configuration:** reuse your tools and add capabilities for a concrete task. The installer requires no additional model API subscription.

## Quick start

Download and extract the repository using **Code → Download ZIP**, or clone it:

```bash
git clone https://github.com/antti0403/research-ai-workbench.git
cd research-ai-workbench
```

From the repository folder, run the command for your system:

**macOS / Linux**

```bash
bash install.sh
```

**Windows PowerShell**

```powershell
.\install.ps1
```

The default workspace is `~/ResearchWorkbench`. Add `--workspace "path/to/project"` to choose another location. The launchers reuse Python 3.11+ or obtain it locally. Keep the source folder until setup finishes; see [troubleshooting](docs/TROUBLESHOOTING.md) if execution is blocked.

Open the workspace in Codex or your existing local agent and send:

> Read START_HERE.md and personalize my research workbench. Ask only for missing task details, reuse my tools, install suitable extensions within my authorization, and verify one real task. Use my preferred language.

For setup handled entirely by an agent, give it [SETUP.md](SETUP.md). That guide also works as a standalone file.

## Usage

Inspect a proposed setup or check an existing workspace from the repository with Python 3.11+:

```bash
python workbench.py plan
python workbench.py doctor --workspace "path/to/project"
```

Start with the [first-task walkthrough](docs/FIRST_TASK.md), then select extensions for actual gaps. See the [installer reference](docs/AUTOMATION.md) for profiles, apply/resume commands, and installed interpreter paths.

The installer downloads public dependencies and does not upload research files or request credentials. Search queries go to their provider; PaperQA may send selected paper passages to configured model/embedding services; your agent's data policies still apply. AI applications and any required MATLAB runtimes, accounts, commercial licenses, or institutional access are provided separately.

## Documentation

- [Setup guide](SETUP.md) — complete agent workflow.
- [Skill catalog and candidates](SKILLS.md) — sources and verification scope.
- [Compatibility](docs/COMPATIBILITY.md) — tested environments and limits.
- [Templates](templates/workbench-config.md) — personal configuration and [project rules](templates/project-instructions.md).

Repository **0.3.0**, guide **1.6**. Changes are recorded in the [changelog](CHANGELOG.md).

## Contributing

Bug reports, documentation improvements, and reproducible environment checks are welcome. Read [Contributing](CONTRIBUTING.md) for development checks and source-review requirements, and [maintenance priorities](docs/MAINTENANCE.md) for planned work. Keep private research and credentials out of reports.

## License and acknowledgements

Original code, skills, and documentation use the [MIT license](LICENSE). External components retain their own terms; see [notices](NOTICE.md) and the [third-party inventory](THIRD_PARTY.md).

Optional skills are by **袁一哲 / Yuan1z0825 and Nature Skills contributors**, and **K-Dense Inc. and Scientific Agent Skills contributors**. Workflow inspiration comes from **艺雨YiLight**, reviewed through **sunweihunu's transcript**. Communication guidance draws on **ASD-STE100** and **Andrej Karpathy**, without claiming standards compliance. Instructions are in English; conversation and deliverables follow the user's language requirements.

ARS is excluded from automatic installation because of its noncommercial terms. `nature-figure` is withheld pending nested-asset permissions; the `figures` runtime remains available. Attribution does not grant permission or imply endorsement.
