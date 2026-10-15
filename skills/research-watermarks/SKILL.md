---
name: research-watermarks
description: Run watermarks-remover's full text-watermark reduction service on selected research prose using a configured model API. Use when the user asks to remove or weaken statistical text watermarks, configure the rewrite backend, or resume the watermarks workflow.
---

# Research text-watermark reduction

Use the installed `remove-ai-marks` skill and its full HTTP service for Layer B
model rewriting. This workflow is for the user's selected manuscript prose.
Unicode cleanup alone does not satisfy a statistical-watermark reduction request.

Locate `scripts/watermarks.py` beside this entry point. Read the project's
`START_HERE.md`, effective instructions, and local watermarks configuration.
Keep original drafts, equations, citations, exact quotations, numerical values,
comparison conditions, and required disclosures. Process selected prose into a
new candidate and review factual equivalence after rewriting. Do not run a
manuscript-wide metadata strip, rewrite code, or modify source-paper attachments
merely because this text workflow was selected.

## Configure and start

Run `python scripts/watermarks.py init --workspace <project>` using this skill's
actual script path. It creates `.workbench/watermarks/config.json` if absent.
Reuse existing configuration. Configure the user's API base URL, model name,
and `allow_remote` choice. Keep the API key only in the local environment as
`WATERMARKS_REWRITE_API_KEY`. Do not copy keys into chat, config, logs, or Git.
No new subscription, local model, or paid request follows from file installation.
Use the user's chosen endpoint and authorization for actual requests.

The strategy is `paraphrase@0.8`: a real rewrite pass intended to weaken
token-sampling patterns. It does not depend on optional masked-language models.
Start `watermarks.py serve --workspace <project>` in a local terminal. It serves
on loopback and uses the installed upstream runtime. Check `status` and the
upstream `/capabilities` endpoint. Read `remove-ai-marks/SKILL.md` for HTTP usage.
If the backend configuration or API key is missing, complete installation and
report the exact pending fields; do not call the rewrite function operational.

## Rewrite and verify the result

Use `watermarks.py rewrite --workspace <project> --input <selected-prose.txt>
--output <new-candidate.txt>`. The wrapper sends plain text through `/clean`
with Layer B required, preserves the source, rejects an existing output, and
writes a local operation report. Use a real authorized public fixture first
when configuring the API, then process the user's selected material within its
sharing and cost authorization. Compare content, units, citations, and protected
spans. Use the writing and Anti Defensive Writing workflows for the argument.

Record actual API/model execution separately from vendor-watermark detection.
An HTTP success or changed wording does not establish removal of a secret-key
watermark. Use an appropriate authorized detector when available; otherwise
label vendor verification unperformed. Do not substitute a stylometry score
for that test, invent a removal percentage, or claim undetectability. A rewrite
backend can introduce its own signal; keep this uncertainty explicit.

The full installed runtime includes optional media and detector entry points;
the selected profile configures the text rewrite path only. Inspect capabilities
and separately review dependencies before using other backends.
