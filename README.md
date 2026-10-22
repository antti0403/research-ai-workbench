[English](README.md) | [简体中文](README.zh-CN.md)
<!-- workbench-release: 0.3.8 -->

# Research AI Workbench

A local setup toolkit that builds a clean, structured workspace for AI-assisted research. Includes a Python installer script and a standalone setup guide for coding agents.

[![Installer checks](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml/badge.svg)](https://github.com/antti0403/research-ai-workbench/actions/workflows/ci.yml)

---

## Why this exists

Setting up an AI agent for academic research usually runs into two problems:

1. **The blank slate problem**: You start in an empty directory. The model has no local tools, no structured place to put notes, and no guidelines on how to read PDFs without hallucinating.
2. **The bloated bundle problem**: A script tries to install 50 heavy packages on day one, cluttering your system with dependencies you might never use.

This workbench uses a progressive setup instead:

- **Minimal core first**: It creates an organized workspace directory (`~/ResearchWorkbench`), configures an isolated environment for reading papers and extracting text, and writes down clear communication and evidence rules.
- **Agent adds what is needed**: You open the workspace in your coding agent (Codex, Claude Code, Cursor, etc.). The agent asks what you are actually working on, then installs only the tools your specific task requires.

---

## Core components

- **Research workspace layout**: Structured folders for reading notes, data/code, and drafts; existing paper libraries are reused.
- **Isolated PDF reading runtime**: Dedicated environment for reading papers and extracting text without polluting your global Python setup.
- **Persistent research rules**: Clear directives on source support, formula preservation, and clear communication. Borrowed from ASD-STE100 and Karpathy's output ladder concepts.
- **Optional task extensions**: Plug in only what you need, such as arXiv/Semantic Scholar literature search, PaperQA for evidence retrieval, SymPy for math derivations, units validation, MATLAB guidance, or data visualization.

---

## Quick start

Clone the repository:

```bash
git clone https://github.com/antti0403/research-ai-workbench.git
cd research-ai-workbench
```

Run the installer for your platform:

**macOS / Linux:**
```bash
bash install.sh
```

**Windows (PowerShell):**
```powershell
.\install.ps1
```

The launchers reuse Python 3.11+ or obtain Python 3.12 locally when needed. The data and figures profiles require Python 3.12+ and check before creating an environment; other dependencies still require platform-compatible wheels.

The default workspace path is `~/ResearchWorkbench`. If you want to put it somewhere else, pass `--workspace "path/to/project"`.

Once the setup script finishes, open that workspace folder in your AI agent and send:

> Read START_HERE.md and personalize my research workbench. Ask only for missing task details, reuse my tools, install suitable extensions within my authorization, and verify one real task. Use my preferred language.

If you prefer to let an AI agent handle the whole setup without running shell scripts first, give it `SETUP.md`. That file is completely self-contained.

---

## First task

Start with the [three task requests](docs/FIRST_TASK.md): read an abstract, check one full-text claim, or ask across selected papers. Each specifies its expected output. The [worked example](examples/attention-scaling.md) includes original-source locators, a checked formula, and a reproducible numerical illustration.

For everyday reading, use the [reading workflow](docs/READING.md): start with the problem, core idea, contribution, evidence, and boundaries, then deepen only the current question. Resume through your existing research index and improve the same note. Try the [synthetic research acceptance cases](docs/RESEARCH_ACCEPTANCE.md) to inspect source use, mechanism explanations, and comparison limits.

For an existing project, send:

> Read START_HERE.md and my existing research index. Continue from the unresolved question in the current note, reuse working tools, and retain source conditions and my actual reading status.

For literature discovery, a connected **Undermind** plugin can find candidates, follow citation relationships, and analyze available PDFs. Keep selected original PDFs and citation records in Zotero or your reference manager, and verified understanding in Obsidian or your existing notes. See the optional [literature workflow](docs/LITERATURE.md); the installer does not install the service, sign in, or buy a subscription.

For academic drafting and revision, the **writing** profile adds **Anti Defensive Writing**, adapted from Adkid-Zephyr: organize prose around supported contributions, remove redundant defensive wording, and preserve material findings and qualifications. See the [writing workflow](docs/WRITING.md).

For requested text-watermark rewriting, **watermarks** uses the model already serving your conversation. No extra API, key, model, or server is needed. See [the workflow](docs/WATERMARKS.md). The standalone service remains optional for explicit API-driven automation; watermark removal requires separate verification.

## CLI checks and maintenance

The repository includes a Python utility (`workbench.py`) to inspect or check your setup:

```bash
# Preview what would be installed
python workbench.py plan

# Run a health check on an existing workspace
python workbench.py doctor --workspace "path/to/project"
```

The installer only fetches public open-source packages. It does not upload research files or call a model during installation. PaperQA queries require configured model/embedding services and may send selected passages to those providers and incur costs; see [PaperQA](docs/PAPERQA.md).

---

## Documentation

- [SETUP.md](SETUP.md): Standalone setup guide for agents.
- [SKILLS.md](SKILLS.md): Catalog of supported research skills and candidates.
- [docs/FIRST_TASK.md](docs/FIRST_TASK.md): Step-by-step walkthrough of your first research task.
- [docs/READING.md](docs/READING.md): Progressive reading, source-based comparisons, and research continuation.
- [docs/RESEARCH_ACCEPTANCE.md](docs/RESEARCH_ACCEPTANCE.md): Inspectable synthetic practice cases and acceptance limits.
- [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md): Tested operating systems, Python versions, and limits.
- [docs/AUTOMATION.md](docs/AUTOMATION.md): Reference for unattended profiles and CLI arguments.
- [docs/WATERMARKS.md](docs/WATERMARKS.md): Rewrite with the current conversation model; optional standalone API route.
- [docs/WRITING.md](docs/WRITING.md): Contribution-first drafting and revision with Anti Defensive Writing.
- [docs/LITERATURE.md](docs/LITERATURE.md): Undermind discovery, verified reference-manager PDFs, and source-linked notes.

---

## Credits and license

Original code and documentation are released under the [MIT License](LICENSE).

Acknowledgements:

- Skill sources and patterns from **袁一哲 / Yuan1z0825 (Nature Skills)** and **K-Dense Inc. (Scientific Agent Skills)**.
- **Guillaume Meyer and contributors** authored watermarks-remover; the optional standalone API profile downloads pinned client/service files unchanged with their MIT license.
- **Adkid-Zephyr** authored the MIT-licensed Anti-Defensive Writing source; the bundled skill is an explicitly modified adaptation.
- Workflow design inspired by **艺雨YiLight** and reviewed through **sunweihunu's transcript**.
- Communication principles borrow from **ASD-STE100** and **Andrej Karpathy**'s technical presentation notes.
- Third-party components retain their respective licenses. See [NOTICE.md](NOTICE.md) and [THIRD_PARTY.md](THIRD_PARTY.md) for full attribution.

Release **0.3.8**, setup guide **2.4**. See the [changelog](CHANGELOG.md).
