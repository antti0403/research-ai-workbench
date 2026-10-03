# PaperQA: questions over selected papers

The optional `paperqa` profile adds [PaperQA](https://github.com/Future-House/paper-qa), pinned to `paper-qa==2026.8.12`, and the original `research-paperqa` workflow skill. Use it to gather evidence across local papers and draft cited answers. Use the existing reading workflow for a single close reading when that is sufficient.

## Install the optional module

After the foundation passes, add `paperqa` to the existing `.workbench/profile.json` extension list, keeping other selections. A minimal selection is `{"extensions": ["paperqa"]}`. From the distribution, run:

```bash
python workbench.py plan --workspace "/path/to/project" --profile "/path/to/project/.workbench/profile.json"
python workbench.py apply --workspace "/path/to/project" --profile "/path/to/project/.workbench/profile.json"
python workbench.py doctor --workspace "/path/to/project"
```

For an installed kit, use the engine path in START_HERE.md. Installation downloads the package into an isolated environment; it makes no model calls. Its local check reads a synthetic PDF, checks page-linked evidence and duplicate handling, and round-trips evidence JSON with outbound connections blocked. It does not test retrieval relevance or a model-generated answer. Native host discovery and research acceptance remain pending.

On Windows, the installer uses extended interpreter paths for PaperQA's deeply nested dependency files. It does not change system long-path policy. Reuse the installed executable paths below; keep the workspace at its original location.

## Configure a small first query

Reuse a selected paper directory, or create one containing only papers you intend to query. Do not point PaperQA at the whole workspace. Choose supported model/embedding services or local endpoints, and confirm authorized data sharing and cost before indexing. Provider credentials stay in environment variables; do not put them in the configuration. Local PDFs can still send extracted content to remote models. The installer does not supply a model account or configure a local model.

From the project root, set the cache location:

```bash
# macOS / Linux
export PQA_HOME="$PWD/.workbench"
export LITELLM_LOCAL_MODEL_COST_MAP=True
mkdir -p "$PQA_HOME/.pqa/settings"
```

```powershell
# Windows PowerShell
$env:PQA_HOME = Join-Path (Get-Location).Path '.workbench'
$env:LITELLM_LOCAL_MODEL_COST_MAP = 'True'
New-Item -ItemType Directory -Force -Path (Join-Path $env:PQA_HOME '.pqa/settings') | Out-Null
```

Create `.workbench/.pqa/settings/research.json`. This is a schema example; replace every `REPLACE_` value before running a query. Use an absolute paper path, and write Windows paths with `/` or escaped backslashes in JSON. Preserve existing settings.

```json
{
  "llm": "REPLACE_ANSWER_MODEL",
  "summary_llm": "REPLACE_SUMMARY_MODEL",
  "embedding": "REPLACE_EMBEDDING_MODEL",
  "parsing": {"use_doc_details": false, "multimodal": false},
  "agent": {
    "agent_llm": "REPLACE_AGENT_MODEL",
    "max_timesteps": 5,
    "timeout": 180,
    "index": {
      "name": "selected-papers",
      "paper_directory": "REPLACE_ABSOLUTE_SELECTED_PAPER_DIRECTORY",
      "recurse_subdirectories": false
    }
  }
}
```

These settings disable metadata-provider enrichment and multimodal enrichment for the first run. Parsing may still call a model to infer a citation, and embedding, evidence summaries, and answers require configured services. Scanned PDFs may need separately authorized OCR. `max_timesteps` and `timeout` constrain the agent; they are not provider spending caps. See the [pinned upstream schema](https://github.com/Future-House/paper-qa/blob/57e89f7223b0960d5ee5ea048c69e3c47e088572/paperqa/settings.py) for provider/router configuration. Check the resolved dependencies in `.workbench/locks/` when diagnosing differences.

First inspect the settings. Once paper/model scope is authorized, index the same directory named in the JSON and ask one question:

```bash
.workbench/envs/paperqa/bin/pqa --settings research view
.workbench/envs/paperqa/bin/pqa --settings research index "/absolute/selected-papers"
.workbench/envs/paperqa/bin/pqa --settings research ask "Under what conditions do the selected studies report a benefit?"
```

```powershell
& .\.workbench\envs\paperqa\Scripts\pqa.exe --settings research view
& .\.workbench\envs\paperqa\Scripts\pqa.exe --settings research index 'C:/absolute/selected-papers'
& .\.workbench\envs\paperqa\Scripts\pqa.exe --settings research ask 'Under what conditions do the selected studies report a benefit?'
```

This version resolves named settings from `PQA_HOME/.pqa/settings/`; use `--settings research`, rather than assuming an arbitrary JSON path works. Keep indexes, model logs, and answer sessions in `.workbench/.pqa/`, which the workbench ignores in Git. Inspect logs before sharing: questions and source content can appear there.

## Small real-query acceptance

After model configuration and source-sharing/cost authorization, begin with the public paper in the [full-text worked example](../examples/attention-scaling.md). Ask what motivates its attention-score scaling, then ask whether that selected evidence guarantees improved accuracy in every application. Compare the answer's passages and locators with the example; the second question should retain the unsupported scope rather than invent evidence. Record models/settings, actual provider usage, session output, and each claim's support. These are proposed acceptance cases, not completed model-query results. Stop on extraction, authentication, or spending limits and retain the last successful step.

## Check and save the result

Ask your agent: “Use research-paperqa to answer this question using only my selected papers. Save the answer and evidence, verify each central claim against the cited original, and identify unsupported or contradictory findings.”

Save a note in your existing system, normally `wiki/`, and retain the original answer/session evidence locally. Include the question, selected paper list, extraction limitations, configured models, package version, and a claim-to-evidence table:

| Claim | Source and page/section | Evidence | Support status |
| --- | --- | --- | --- |
| One bounded claim from the answer | Verified locator in the original | Short passage or faithful paraphrase | Supported, partial, contradicted, or not checked |

Open the originals and check that a citation supports the claim under the stated conditions. Citation formatting alone is not validation. Distinguish PaperQA's summaries from raw passages and your interpretation; leave unknown locators unknown. Record local ingestion, model connection, actual query, host invocation, and claim verification separately in workbench-config.md.

No real model query was performed for this integration. CI/local smoke checks use synthetic evidence and no model credentials; they do not establish scientific answer quality. PaperQA and its dependencies retain their own licenses; see [THIRD_PARTY.md](../THIRD_PARTY.md).
