# Research AI Workbench

Give one guide to your AI. Let it configure research tools, skills, and working rules around your actual task.

**Start with [SETUP.md](SETUP.md).** It contains the complete workflow and can be shared as a single file. Open it on GitHub, select Raw, and save the file.

Use it for literature search, paper reading, notes, supported calculations, and writing. The AI first learns your research needs, then selects tools. Codex is the default; other agents can adapt the process to their actual capabilities.

## Start in three steps

1. Download [SETUP.md](SETUP.md) into your project or attach it to your AI conversation.
2. Send this request:

   > Set up my research AI workbench using the attached guide. First identify my research field, immediate task, and existing tools. Configure the tools and skills that task needs. Explain the steps clearly and verify the setup with a small task. Preserve my files and manual settings. Use my preferred language for conversation and the required language for deliverables.

3. Answer necessary questions and complete personal sign-in actions. The AI should deliver a configuration record, a real task output, and an honest list of unfinished steps.

A chat-only AI can plan and prepare instructions. Actual installation requires access to the target computer. Installing something in a cloud environment does not install it on your computer.

## What you get

- Tools and skills chosen for the task, with sources and actual installation states.
- A suitable organization for notes, calculations, and manuscripts.
- Persistent rules for evidence, terminology, derivations, and useful visual explanations.
- A private `workbench-config.md` recording completed, verified, and unfinished work.

This is a guide, not a software bundle. Results depend on agent capabilities, authorization, and environment. It does not provide software licenses, institutional access, model subscriptions, or external accounts.

## Current status

Repository version: **0.1.0**. Included guide: **1.3**. Some skill files and basic calculations were checked in a macOS maintenance environment. Complete setup on another user's computer has not been verified. Windows, Linux, and other agents remain unverified; see [compatibility and verification](docs/COMPATIBILITY.md).

| Need | Entry point |
| --- | --- |
| Start setup | [Complete guide](SETUP.md) |
| Inspect sources and verification limits | [Skill catalog](SKILLS.md) |
| See an output from a real public abstract | [Example](examples/README.md) |
| Resolve failures or resume interrupted work | [Troubleshooting](docs/TROUBLESHOOTING.md) |
| Create personal rules and configuration records | [Project rules](templates/project-instructions.md), [configuration template](templates/workbench-config.md) |
| Suggest improvements or report tests | [Contributing](CONTRIBUTING.md) |

## Language and explanations

Canonical instructions and templates are in English for sharing and maintenance. The AI should talk with each user in their preferred language and prepare papers in the required submission language. English is a format choice, not a guarantee of clearer instructions or higher model accuracy.

The workflow borrows ASD-STE100 principles: familiar words, explicit subjects, consistent terms, ordered steps, and preserved technical meaning. It does not claim strict compliance. Choose diagrams for structures, tables for comparisons, and interactive examples for parameter changes when useful. Web pages and videos are not mandatory outputs.

## License and sources

Original instructions and templates use the [MIT license](LICENSE). Third-party skills, papers, standards, and products retain their own terms; see [notices](NOTICE.md). This repository does not bundle skill source code or paper PDFs.
