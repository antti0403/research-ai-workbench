# Statistical text-watermark reduction

The optional **`watermarks`** profile installs the full watermarks-remover
**`remove-ai-marks`** HTTP client and service sources, plus the workbench's
**`research-watermarks`** integration. This workflow runs **Layer B model
rewriting** to weaken statistical patterns in word choices. Unicode cleanup
alone does not perform that operation.

The source is [Guillaume Meyer and contributors' MIT-licensed project](https://github.com/guillaumemeyer/watermarks-remover/tree/c5297e9e69fec0779c29127c7892427e673fafd9).
The installer checks individual client, service, and license hashes. Upstream
files remain unchanged; service sources are arranged inside the installed
client's `runtime/`. Optional media tools, local model weights, and watermark
detector backends require separate setup. This profile uses the user's existing
compatible model API; it does not install Docker or Ollama.

## Install and configure

Use the current engine identified in `START_HERE.md` to plan/apply profile ID
`watermarks`, keeping other selected extensions. Existing different skills are
preserved. Offline preparation installs the original integration skill but
leaves external client/runtime downloads pending. After installation, run:

```bash
python .agents/skills/research-watermarks/scripts/watermarks.py init --workspace .
```

Edit `.workbench/watermarks/config.json` with the user's API base URL and model:

```json
{
  "backend": "openai-compatible",
  "base_url": "https://your-model-provider.example/v1",
  "model": "your-chosen-model",
  "allow_remote": true,
  "strategy": "paraphrase@0.8",
  "port": 8765
}
```

The endpoint must support Chat Completions. Use the provider's actual URL and
model; the example is not a functioning service. `allow_remote` records the
choice to send selected prose to that endpoint. Observe the user's sharing and
cost authorization. Keep the API key only in the local environment variable
`WATERMARKS_REWRITE_API_KEY`, never in chat, this config, or Git. The initializer
leaves URL/model unset and preserves an existing config.

`paraphrase@0.8` is an explicit Layer B strategy that avoids the upstream default's
optional local masked-language-model dependency. A rewrite backend may introduce
its own watermark. Actual removal must be assessed separately from API success.

## Start and use

Run this command in a local terminal with the provider key available in its environment. Only the service needs that provider key; local status/rewrite clients do not need a second copy:

```bash
python .agents/skills/research-watermarks/scripts/watermarks.py serve --workspace .
```

Keep the terminal running. Stop with Ctrl+C. Restart after changing config.
The service binds to `127.0.0.1`; optional `WATERMARKS_SERVER_API_KEY` can protect
local HTTP requests and must also be available to the client. No login service
or write hook is enabled by the installer.

In another terminal, check health and rewrite a selected prose text file:

```bash
python .agents/skills/research-watermarks/scripts/watermarks.py status --workspace .
python .agents/skills/research-watermarks/scripts/watermarks.py rewrite --workspace . --input manuscript/selected-prose.txt --output manuscript/selected-prose.rewritten.txt
```

The client submits the text to the upstream `/clean` endpoint, requires a
completed `report.layer_b`, and writes a new candidate plus a `.watermarks.json`
operation report. It preserves the input and refuses existing outputs. Missing
configuration or a failed rewrite is an error, not successful watermark removal.
The full upstream client remains available as `$remove-ai-marks`; use
`$research-watermarks` for research-specific configuration and routing.

## Fit it into research writing

1. Draft or polish from verified evidence; use Anti Defensive Writing to clarify
   the argument and contribution when selected.
2. Select the prose for the requested watermark-reduction pass. Retain the source
   and keep equations, citations, exact quotations, code, and numerical values
   protected. Do not send a whole PDF/DOCX/LaTeX document to a prose rewrite.
3. Run the configured Layer B pass on an authorized public fixture first, then
   on the user's selected text. Review meaning, factual claims, units, language,
   and necessary qualifications before accepting the candidate.
4. Record the actual backend/model execution. Use an appropriate authorized
   vendor detector when available; otherwise leave vendor verification unperformed.
   Preserve required disclosures and the author's actual contribution.

## Separate verification states

| Check | Evidence |
| --- | --- |
| Installation | Pinned client/runtime files and retained upstream license |
| Service | Live health, capabilities, and explicit missing-backend failures |
| API wiring | Controlled test responder received a real service rewrite request; not a model experiment |
| Real model rewrite | An authorized configured provider actually returned the candidate |
| Factual equivalence | The candidate was compared with its source and evidence |
| Vendor-watermark reduction | An appropriate detector measured the original and candidate; otherwise unverified |

Run `python scripts/check_watermarks.py --workspace <project>` from the installed
kit for a disposable service/API-wiring test. It uses no provider credentials or
paid model calls and makes no claim about real watermark removal. Local style
scores are not substitutes for a vendor-key detector or authorship evidence.
