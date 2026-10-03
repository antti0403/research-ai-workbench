---
name: research-paperqa
description: Use the optional PaperQA environment to answer questions across selected local papers and produce source-linked evidence notes. Use for multi-paper evidence questions; verify cited passages before using an answer in research writing.
---

# Questions over selected papers

Read the project's START_HERE.md and workbench-config.md. The `paperqa` profile installs `paper-qa==2026.8.12` in `.workbench/envs/paperqa` and this original MIT-licensed skill. It does not configure a model or validate a research answer. If absent, add `paperqa` to the existing extension selection and apply it through the recorded engine within the user's setup authorization. Preserve other selections.

## Prepare the query

- Define one question and select a small paper set. Reuse the library's originals; use a dedicated directory containing only the selected materials. Do not index the whole project or library by default. Record exclusions, missing full text, and extraction problems.
- Confirm the chosen LLM, summary model, agent model, embedding service or local endpoints, source-sharing scope, and budget from existing authorization. PaperQA can transmit passages, queries, and metadata to configured providers. Credentials belong in provider environment variables, never a note or settings JSON. Installation authorization alone does not authorize querying private papers or paid services.
- Set `PQA_HOME` to the absolute project `.workbench` directory before starting PaperQA. This release stores settings, indexes, answers, and logs under `PQA_HOME/.pqa`. Keep that private. Set `LITELLM_LOCAL_MODEL_COST_MAP=True` to use the installed cost map.
- Write `.workbench/.pqa/settings/research.json`, preserving any existing configuration. Set `llm`, `summary_llm`, `embedding`, and `agent.agent_llm` explicitly. Set `agent.index.paper_directory` to the selected directory, `name` to a stable corpus name, and `recurse_subdirectories` to false. Set `parsing.use_doc_details` and `parsing.multimodal` to false for an initial text-only run; automatic citation inference may still call the LLM. Inspect the pinned upstream Settings schema for provider-specific options. Do not guess model names or silently fall back to defaults.

The executable is `.workbench/envs/paperqa/bin/pqa` on macOS/Linux or `.workbench/envs/paperqa/Scripts/pqa.exe` on Windows. Use the actual path and shell; from the project, invoke that executable with:

```text
--settings research view
--settings research index <selected-paper-directory>
--settings research ask <one-quoted-question>
```

`view` checks the settings; `index` and `ask` may incur model calls. Verify the selected directory and provider settings before those calls. Bound agent steps and timeout, monitor actual provider usage, and stop on authentication, budget, or extraction failure rather than retrying blindly. A timeout is not a spending cap. The copied kit's `docs/PAPERQA.md` contains a full example.

## Deliver a checked note

Save the question, selected sources, PaperQA/model/settings versions, answer, and generated references. Preserve the session/evidence JSON from the local answer index when available; never include credentials. Open the cited originals and compare each central claim with its passage and page/section. Report ambiguous citations, contradictory findings, missing conditions, and unanswered parts.

Produce one note under the existing note system, normally `wiki/`, with a compact claim-to-evidence table: claim, source, locator, supporting passage or paraphrase, and support status. Distinguish a raw passage from a model summary and your interpretation. Never invent a missing page, citation, or result. Avoid extensive quotation.

Record separately in workbench-config.md: dependency/local-ingestion checks; host invocation; model connection; actual query; citation/claim acceptance. A successful generated answer does not prove claim support. On insufficient evidence, retain the gap and propose the next source to inspect.
