# Optional API service route

Use only for an explicit standalone-service or API-driven batch request. The
default Skill workflow uses the current conversation model without these steps.

The optional `watermarks-api` profile provides the pinned `remove-ai-marks`
client and full service runtime. Locate this skill's `scripts/watermarks.py`
and the project's current workbench kit. Full setup and verification details
are in that kit's `docs/WATERMARKS_API.md`; standalone distribution users can
also consult the API section of `SETUP.md`.

Reuse the user's chosen compatible API and sharing/cost authorization. Run
`init --workspace <project>` only to create missing configuration; preserve
existing values. Set `base_url`, `model`, and `allow_remote` in
`.workbench/watermarks/config.json`. Supply the provider key only through
`WATERMARKS_REWRITE_API_KEY`, never chat, configuration, logs, or Git.

Run `serve --workspace <project>` on loopback, then `status`. Run
`rewrite --workspace <project> --input <selected-prose.txt> --output <new.txt>`
for the reviewed `paraphrase@0.8` Layer B path. The helper preserves the source,
refuses existing outputs, and writes a candidate plus an operation report.
Missing API configuration is pending for this optional route only and must
never block a requested direct chat revision.

Record actual service/API execution separately from factual comparison and
vendor-watermark detection. Optional media and detector backends are separate
components, not prerequisites for direct rewriting.
