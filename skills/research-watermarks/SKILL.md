---
name: research-watermarks
description: Rewrite selected research prose with the current conversation model to vary wording and sentence structure while preserving evidence. Use for requested text-watermark reduction or related prose rewriting; separate detector verification from the rewrite.
---

# Research text-watermark rewriting

Use the model already serving this conversation to rewrite the selected prose.
This is a writing task in the current agent: no separate API, key, model choice,
local server, or script execution is required. Existing API configuration does
not change this default. Do not ask the user to configure another model.

## Rewrite in the conversation

- Reuse the selected passage, target language, and revision scope. Keep the source
  intact. Return the candidate directly in chat, or save a separate candidate
  when the user requests a file.
- Rebuild sentences from their meaning rather than replacing words mechanically.
  Vary clause order, sentence boundaries, and phrasing where the argument allows;
  retain established technical terminology and the author's intended emphasis.
- Preserve facts, numbers, units, equations, citations, exact quotations,
  comparison conditions, unfavorable findings, uncertainty, and claim strength.
  Keep protected spans unchanged. Add no new evidence or references.
- Compare the candidate with the source before delivery and repair factual drift.
  Keep necessary academic qualifications. Use Anti Defensive Writing when it is
  already part of the selected writing workflow.
- Return the revised text with only material changes or unresolved issues noted.
  No setup report or operation JSON is needed for an ordinary chat revision.

Changed wording is not proof that a statistical watermark was removed. If no
appropriate detector was run, leave that result unverified. Do not invent a
removal rate, detector score, or guarantee of undetectability. Direct rewriting
is not execution of the upstream HTTP service or its numerical intensity setting.
Unicode cleanup alone is a separate operation and does not replace rewriting.

## Optional standalone automation

Only when the user explicitly requests a standalone service or API-driven batch
processing, read [the API service instructions](references/api-service.md).
Do not select that route merely because its scripts or old configuration exist.
