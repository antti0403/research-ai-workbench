# Research AI Workbench

Set up a research workspace, then let your existing AI add the tools your next task needs.

The installer prepares project folders, two research skills, an isolated PDF-reading runtime, and records that let you resume setup. Start with reading and notes; add literature search, writing, symbolic mathematics, units, MATLAB guidance, data analysis, or plotting as needed. You do not need to choose unfamiliar skill names or buy another model API subscription for the installer.

## Start

1. Download this public repository with **Code → Download ZIP** and extract it.
2. Open a terminal in the extracted folder and run:

   **macOS / Linux**

   ```bash
   bash install.sh
   ```

   **Windows PowerShell**

   ```powershell
   .\install.ps1
   ```

   The workspace defaults to `ResearchWorkbench` in your home directory. Add `--workspace "path/to/my-project"` to choose another location. Keep the download until setup finishes. If execution is blocked, use [troubleshooting](docs/TROUBLESHOOTING.md).
3. Open the workspace in Codex or your existing local agent and send:

   > Read START_HERE.md and personalize my research workbench. Ask only for missing details about my next output, methods, existing tools, and constraints. Select and install suitable extensions, then verify one real task. Use my preferred language.

For agent-led setup, give your AI [SETUP.md](SETUP.md), the complete guide. It also works on its own; the standalone file does not contain the installer.

## After setup

Start with the [first-task walkthrough](docs/FIRST_TASK.md). It checks a saved, source-linked reading note before you expand the workbench. Installation checks and a successful research task are recorded separately.

| Need | Read |
| --- | --- |
| Commands, extensions, and installation records | [Automation reference](docs/AUTOMATION.md), [skill sources](SKILLS.md) |
| Failed or interrupted setup; tested environments | [Troubleshooting](docs/TROUBLESHOOTING.md), [compatibility](docs/COMPATIBILITY.md) |
| Personal research context and project rules | [Configuration template](templates/workbench-config.md), [rules template](templates/project-instructions.md) |
| Development, priorities, and releases | [Contributing](CONTRIBUTING.md), [maintenance](docs/MAINTENANCE.md), [changelog](CHANGELOG.md) |

Repository **0.2.3**, guide **1.5**. See compatibility for actual test scope.

## Access, language, and credits

The installer downloads public dependencies; it does not upload research files or request credentials. Optional search sends the query to its provider. Account login and paid choices remain with you. The AI application, MATLAB, commercial licenses, and institutional access are not included. Your agent's own data policies still apply.

Instructions are in English; conversation follows your language and deliverables follow their target requirements. Original code and material use the [MIT license](LICENSE). External components retain their own terms.

Optional skills come from **袁一哲 / Yuan1z0825 and Nature Skills contributors**, and **K-Dense Inc. and Scientific Agent Skills contributors**. Workflow inspiration comes from **艺雨YiLight**, reviewed through **sunweihunu's transcript**; communication guidance draws on **ASD-STE100** and **Andrej Karpathy** without claiming standards compliance. See the [third-party inventory](THIRD_PARTY.md) and [notices](NOTICE.md) for sources, runtime dependencies, and licenses.

ARS is excluded from automatic installation because of its noncommercial terms. `nature-figure` is withheld pending permission for nested assets; the `figures` plotting runtime remains available. Attribution does not grant permission or imply endorsement.
