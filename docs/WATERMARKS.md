# Rewrite with the current conversation model

For a requested text-watermark reduction pass, use the model already serving
the conversation. Read the bundled `research-watermarks` skill and revise the
selected prose directly. No separate model API, key, server, or backend setup
is required. Existing API configuration does not override this default.

## Use it

Select the optional `watermarks` profile with the current engine's plan/apply,
keeping other selected extensions. It prepares the bundled skill offline too,
without downloading the upstream service or creating a model configuration.
Hosts without native skill discovery can read
`.agents/skills/research-watermarks/SKILL.md` explicitly.

Then ask, for example:

> Use research-watermarks with the current conversation model to rewrite this
> selected passage. Keep the original meaning, numbers, units, terminology,
> equations, citations, quotations, and necessary qualifications. Return the
> candidate here and check it against the source. Do not configure another API.

After drafting/polishing and Anti Defensive Writing, rebuild the selected
sentences from their meaning and compare the candidate with the source.
Preserve material unfavorable findings and claim strength. Keep the original;
create another file only when a file deliverable is requested. A normal chat
revision needs no operation JSON, service health check, or setup task.

Wording changes alone do not verify statistical-watermark removal. Record a
vendor-detection result only if an appropriate detector actually measured it.
Direct model rewriting is distinct from running the upstream `/clean` pipeline.

## Optional standalone automation

For an explicit standalone-service or API-driven batch request, select
`watermarks-api` and follow [the API service instructions](WATERMARKS_API.md).
That route retains the pinned MIT-licensed watermarks-remover client/runtime
and the existing helper. It requires its own model API because an independent
script cannot borrow the chat session. Old installations and API configuration
are preserved and are not used automatically.
