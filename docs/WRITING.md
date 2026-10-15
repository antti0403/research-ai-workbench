# Evidence-based writing with Anti Defensive Writing

The optional `writing` profile includes `nature-writing`, `nature-polishing`,
their shared resources, and the bundled `anti-defensive-writing` adaptation.
Select this profile when the next task needs drafting or revision. Existing
document tools can still handle Word, LaTeX, or presentation output.

## Use the skills together

1. Establish the passage's purpose, target language, submission requirements,
   and available evidence. Reuse existing notes and results.
2. Use `nature-writing` to draft or restructure an argument, or `nature-polishing`
   for language revision. Use an existing equivalent host capability when suitable.
3. Apply `anti-defensive-writing` to lead with the strongest supported contribution,
   remove redundant defensive wording, and connect each finding to its evidence.
4. Compare the revision with the inputs. Preserve material unfavorable findings,
   quantitative comparisons, uncertainty, citations, and necessary conditions.
   Verify the target document format with the relevant document tool.

The framing skill has no runtime or service dependency. It is bundled in the
kit and copied into `.agents/skills/anti-defensive-writing` when `writing` is
selected, including during offline file preparation. Other writing skills still
need their pinned upstream downloads. Offline preparation can therefore leave
the overall profile pending. File preparation does not establish host discovery
or the quality of a real manuscript revision.

Use the installed engine identified by `START_HERE.md` to plan/apply a local
profile with `"extensions": ["writing"]`; preserve any other selected extensions.
For an existing writing installation, rerun apply with the new kit. Existing
different or edited skills are preserved for review. Setup does not silently
rewrite an edited project instruction file.

## Statistical text-watermark reduction

When the user requests watermark reduction, select the optional `watermarks`
profile and follow [the full service workflow](WATERMARKS.md). It installs the
upstream HTTP service/client and runs an actual Layer B rewrite through the
user’s configured model API. Unicode cleanup alone does not fulfill this task.
Keep the source and compare the candidate with evidence, formulas, citations,
and necessary qualifications. Model execution and vendor-key detection have
separate verification states.

## Example request

> Use Anti Defensive Writing to revise this abstract. State the main contribution
> directly, connect it to the supplied results, and remove repeated disclaimers.
> Preserve numerical values, comparison conditions, unfavorable findings that
> affect the conclusion, and necessary qualifications. Return the revised text
> in the draft's language and briefly explain material changes.

The invocation name is `$anti-defensive-writing`. Hosts without native discovery
can read `.agents/skills/anti-defensive-writing/SKILL.md` explicitly. Record a real
invocation and its output in the local workbench configuration.

## Adaptation and attribution

Source: [Adkid-Zephyr/anti-defensive-writing-Skill at the reviewed revision](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/tree/82d31402caa0db1790026824399044538483171b),
including its English and Chinese skills and root MIT license, reviewed on
2026-10-15. The workbench retains contribution-first structure and concise prose.
It replaces upstream instructions to avoid admitting losses or change the
comparison frame with explicit reporting of material findings and evaluation
changes. Necessary qualifications remain beside the claim they constrain.
See the [adapted skill](../skills/anti-defensive-writing/SKILL.md) and
[source inventory](../THIRD_PARTY.md) for provenance and retained license.
