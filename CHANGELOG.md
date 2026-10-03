# Changelog

## 0.3.1 — 2026-10-03

- Preserve the revised bilingual README style; package its Chinese translation and check language-independent release markers. Publish a new immutable kit so both existing 0.3.0 variants can upgrade without replacing their old kit.
- Read the installed version in first-PDF commands and execute those documented shell commands in online installation checks. Validate links inside copied kits, and add actual previous-release upgrade/resume/preservation checks to CI.
- Declare Python 3.12+ for the current data/figures pins; reject an incompatible interpreter before creating a new profile or attempting package repair. Foundation remains Python 3.11+.
- Add three first-task requests and a full-text claim example with source locators, assumptions, unsupported-claim handling, and an executable synthetic calculation. Add proposed PaperQA model-query acceptance cases; real model queries remain unperformed.
- Clarify model-provider sharing/cost and verification scope in both READMEs; update standalone guide edition 1.7 and attribution.

## 0.3.0 — 2026-10-03

- Add the optional PaperQA profile, pinned to paper-qa 2026.8.12, and an original research-paperqa skill. Default foundation installation remains light and does not install PaperQA.
- Support installer-owned bundled skills in selected profiles, including offline file preparation and preservation of edited skills. Existing foundation skill bytes are unchanged.
- Check real synthetic PDF ingestion, duplicate handling, page-linked source contexts, and JSON serialization with outbound connections blocked and no model calls. Add optional copied-engine installation/resume and CLI checks to the three-platform Python 3.12 runtime CI jobs.
- Use extended Windows paths for PaperQA package installation and runtime checks to handle deeply nested LiteLLM files without changing system policy. Preserve existing runtime ownership and repair boundaries.
- Add a concise PaperQA workflow and standalone guide edition 1.6, with explicit selected-paper/model scope, project-local state, credentials, provider cost, and cited-claim verification. Update attribution and release metadata.
- Real model queries, retrieval relevance, host discovery, and scientific claim acceptance remain unverified.

## 0.2.4 — 2026-10-03

- Present README as a project overview with features, quick start, usage, documentation, contributing, and license sections.
- Identify the Python installer and standalone guide directly; add the CI status badge and clone instructions.
- Advance kit metadata for the revised bundled README. The standalone guide, installer behavior, original skills, and dependency/source pins are unchanged.

## 0.2.3 — 2026-10-03

- Shorten README around setup and the first task; group references by purpose.
- Simplify the standalone guide as edition 1.5, preserving the foundation and seven-step workflow, source checks, authorization, evidence, and recovery.
- Make AUTOMATION a command reference; separate current catalog, manual candidates, and historical checks in SKILLS.
- Reduce wide configuration tables and duplicate release instructions. Keep directory paths and public source records.
- Advance the kit version so revised bundled documents coexist with previous releases. Installer behavior, original skills, and dependency/source pins are unchanged.

## 0.2.2 — 2026-10-03

- Reject Windows junctions and reparse points in managed paths, and confirm resolved paths stay inside the workspace. Protect interpreter parent directories while allowing POSIX venv interpreter links.
- Record runtime ownership in state and a matching environment marker before creation. Repair only recognized environments; reuse working legacy runtimes without adopting or modifying their packages.
- Recheck foundation skills and the current PDF runtime before applying extensions. Record runtime creation and dependency failures for recovery.
- Ignore normal Python bytecode caches beside their source files during skill verification, while still rejecting source edits, unexpected scripts, and links.
- Normalize the skill root before comparisons so macOS temporary-directory aliases, Windows short paths, and relative paths use the same canonical location.
- Accept optional UTF-8 BOMs in profiles and state; validate state structure and nested records before using them. Capture Unicode subprocess output explicitly.
- Update unchanged installer-owned START_HERE.md when the engine version changes, backing up its previous contents. Preserve edited entry points and provide versioned instructions.
- Add CI for Windows, macOS, and Linux on Python 3.11, 3.12, and 3.14; add separate actual PDF/figures installation and resume checks on Python 3.12.
- Add repository validation, a first-task walkthrough, and maintenance priorities. Keep guide version 1.4 and existing dependency/skill pins.

## 0.2.1 — 2026-10-03

- Add a component-level third-party inventory with authors, pinned sources, license links, installation scope, runtime dependencies, and workflow inspirations.
- Credit the original YiLight video, the transcript used for review, ASD-STE100, Karpathy, upstream skills, and the paper used in the reading example.
- Exclude `nature-figure` from automatic selection because the pinned skill contains `figures4papers` assets whose reuse permission is unresolved. Keep the `figures` plotting runtime. Existing installations are not removed.
- Retain source and attribution documents in the installed engine kit, and require the same provenance checks for future contributions.
- Correct public-download guidance. The guide remains version 1.4; this patch does not add a research workflow.

## 0.2.0 — 2026-10-03

- Add macOS/Linux and Windows launchers, with existing-Python reuse and a local Astral uv fallback.
- Prepare a common project, two original skills, an isolated PDF runtime, persistent rules, and installation state before asking research questions.
- Add AI-led three-question intake and a validated local profile format; defer specialist choices when research needs are unknown.
- Add catalog-based installation for selected literature, writing, symbolic, units, MATLAB-guidance, data, and figure extensions.
- Pin upstream revisions and verify archive or file hashes. Preserve different existing skills, retain licenses, and isolate runtimes per profile.
- Add plan, apply, doctor, offline preparation, resumable checks, and meaningful preservation/failure tests.
- Exclude ARS from automatic installation because its reviewed revision uses CC BY-NC 4.0 terms.
- Update the English guide to 1.4. Native discovery and personal research acceptance remain separate from installer tests.

## 0.1.0 — 2026-10-03

- Package the setup workflow as a standalone repository, preserving single-file use through SETUP.md.
- Publish guide version 1.3 in English, adapted from the original Chinese guide version 1.2. Separate instruction language, conversation language, and deliverable language.
- Use portable English filenames for new project records while preserving users' existing localized names.
- Add a landing page, skill provenance and verification scope, compatibility notes, troubleshooting, and project templates.
- Include a real public-abstract reading example. Clearly distinguish it from full-text review or setup on another computer.
- Preserve clear communication, evidence checks, and task-based selection of diagrams and interactive explanations.
- Add an MIT license for original material and third-party notices.

Repository version and guide version are tracked separately. The English guide preserves the seven-step workflow and its authorization and evidence boundaries. Actual installer tests and unverified platforms are recorded separately in docs/COMPATIBILITY.md.
