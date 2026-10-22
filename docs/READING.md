# Read, discuss, and continue research

Use this workflow with the project's existing papers, notes, and research index. It needs no new service, account, specialist software, or mandatory state file. For a first tool check, use [FIRST_TASK.md](FIRST_TASK.md); for finding additional sources, use [LITERATURE.md](LITERATURE.md).

## Start from the current question

For an existing project, read its instructions and relevant note or index before asking the user to repeat known context. Establish the current question and intended output. Choose a useful reading depth:

| Request | Useful output | Read further when |
| --- | --- | --- |
| “What is this paper about?” | Problem, core idea, contribution, evidence, and boundaries | A claim or mechanism needs clarification |
| “How do these two blocks connect?” | Direct explanation tied to the selected figure or passage | Surrounding assumptions change the answer |
| “Why does this method behave this way?” | Causal steps, necessary concepts, then relevant equations | The question depends on a missing derivation or parameter |
| “Which method should I use?” | Comparator, conditions, evidence kind, supported conclusion, and gap | A decision depends on untested or unequal conditions |
| “Can I reproduce this result?” | Required model/data, parameters, procedure, expected measures, and missing inputs | The user proceeds to implementation or actual execution |

An overview does not require every equation or implementation parameter. A focused question does not require another paper summary. Follow the user's requested scope; when evidence is missing, state what is missing and what the available source still supports.

## Keep the source attached to the claim

Identify the exact source version and whether it is full text, an excerpt, or an abstract. Check the original page for a figure or formula that text extraction does not preserve. Metadata and search snippets help locate sources; they do not establish what an experiment proves.

For a conclusion that may guide later work, retain:

> Claim → source and location → relevant conditions → support and limits.

For example, “the reported test reduces error at the selected load” is narrower than “the method is more accurate.” Describe the authors' claim separately from what you have checked. Do not use a published paper's figure number to cite a different preprint without confirming the match.

When comparing methods, distinguish a complete-method benchmark, an ablation, a condition contrast, and feature coverage. Check the comparison's actual model or data, operating conditions, tuning, resources, and measures. Unequal tests may still be informative, but their results need an explicit boundary. Read the [acceptance cases](RESEARCH_ACCEPTANCE.md) for concrete examples.

## Improve the same note

First locate an existing note. Add one when a sustained reading task needs it, or when the user asks to save the result. Answer a local question inline if saving would add no lasting value. Keep the user's existing folder structure and preserve their writing.

A short first-pass note can contain the source/version, problem, mechanism, contribution, key evidence with locations, limitations, and useful open questions. Use only the parts needed for the task. Label an AI first pass as a draft; do not label it user-reviewed.

After discussion, correct the relevant passage in the same note. Remove or clearly qualify an outdated conclusion so it cannot be mistaken for the current answer. Preserve a useful question only if it may affect a later decision. Avoid accumulating transcripts, duplicate summaries, or unresolved questions that no longer matter.

Use the conversation's language and the deliverable's required language. If the user prefers bilingual notes, keep a concise translation beside the relevant passage and preserve its technical meaning; a preference for bilingual summaries does not imply a full-paper translation.

## Continue through the existing index

Reuse an existing research overview, project index, task list, or equivalent. When a session changes the research state, update the smallest useful entry:

| Item | What to retain |
| --- | --- |
| Current question | The problem currently being resolved |
| Established evidence | The supported result and links to the relevant source or note |
| Unresolved gap | The missing concept, source, condition, or result that matters next |
| Next output | A concrete next result, such as a revised comparison paragraph or a checked figure explanation |

These are useful contents, not mandatory fields or a new file format. If the project has no index, keep a brief continuation entry in an existing note. Create a separate index only if it benefits the project and fits the user's workflow. Do not save private project details in the shared workbench repository.

Keep these states distinct in the project's own wording:

- **AI first pass:** an initial source-grounded draft; the user has not confirmed reading it.
- **Enough for the present question:** the user explicitly chose to stop reading deeper. This does not prove every detail is understood or verified.
- **Implementation deferred:** the required detail or work is identified but has not been performed.
- **Actual validation:** record the operation, inputs, conditions, and observed result. A paper's own simulation or experiment is evidence from that paper, not validation of the user's project.

When the user says they understand enough, stop expanding the paper. Save only useful corrections and pending work, then move to the next agreed task. On return, recover the question, evidence, gap, and next output from the existing entry; ask only for information the project does not already contain.

## Small requests to use

> Read this paper at overview depth. Explain the problem, core idea, contribution, evidence, and limits. Use the existing note if there is one.

> Explain the selected figure's feedback path. Start with the signals and causal steps; add equations only where they help answer this question.

> Compare these results. Name the comparator, classify the evidence, check whether conditions are comparable, and state what remains unproven.

> Continue from our research index. Recover the current question, established evidence, unresolved gap, and next output, then work on that output.

The [research acceptance cases](RESEARCH_ACCEPTANCE.md) let maintainers inspect these behaviors using public repository material. They complement installer tests; they do not establish scientific validity for another project.
