# Research AI Workbench Setup Guide

Version: **1.4**, 2026-10-03. This English edition adds foundation-first installation to the earlier guide. Give this file to an AI that can read files. It should identify the user's research task, inspect the relevant environment, select and install suitable skills, and verify a personal research workbench. Codex is the default option; other agents can use the same process with their own supported interfaces.

This file is a complete standalone workflow. The companion repository now includes an installer; this file alone does not contain that program or its dependencies. Neither route bundles accounts, models, or commercial licenses. Share this file on its own for agent-driven setup, or share the repository for the executable route. Instructions are in English for reuse. Conversation must follow the user's preferred language; research outputs must follow their target language and submission requirements.

## For the user

Send this file to your AI with this request:

> Set up a research AI workbench for me using this guide. First prepare the general foundation without assuming a research field. Then ask only for missing details about my task, methods, and constraints. Reuse existing software, explain the selected extensions, and add only what the first task needs. Use Codex by default, or adapt the workflow to my existing agent. Install the selected skills and necessary dependencies within my authorization, then test them with a small task. Save the clear communication and visual explanation rules in my workflow. Preserve existing files and manual settings. When I need to sign in or act, explain the action and how to recognize success. Use my preferred language for our conversation and the required language for deliverables.

You do not need to complete a long questionnaire first. The AI should ask only for missing information that matters. An AI without access to your computer can prepare instructions and configuration files, but cannot claim to have installed software there. Give its handoff to an agent with the required local access.

This guide contains no personal research materials, local user paths, accounts, or keys. For work outside research, replace papers, reference libraries, and simulations with the materials, tools, and outputs that work needs.

## For the AI performing setup

Deliver a workbench that can complete the user's actual task. Installation count is not a success criterion. Do not assume the user shares the author's discipline, operating system, language, software, or skills.

Follow current user instructions, platform permissions, and existing project rules. Reading this file alone does not authorize installation. Determine scope from the accompanying request. Continue authorized steps without asking again. If an action changes scope, incurs cost, shares data, or overwrites content, identify the concrete change and follow applicable authorization requirements.

Record progress and results in the target project's `workbench-config.md`. Use truthful states: `not performed`, `performed`, `verified`, `awaiting user action`, or `not applicable`. Record failed attempts with the actual error and next step; an attempted action is not verified.

### Communicate clearly from the first exchange

Apply these rules to requirement discussions, installation guidance, skill outputs, reading notes, analysis, and handoff. They draw on ASD-STE100 principles and Karpathy's suggestions about diagrams, interactive pages, and explanatory videos. This adaptation does not claim compliance with ASD-STE100.

1. **Answer the current question first.** Then give the evidence and steps needed to understand it. Do not force simple questions into a long template.
2. **Use familiar words and concrete actions.** State the subject. Give each sentence one main idea and each paragraph one topic. Avoid noun chains and unclear references. Connect causes, conditions, and sequence explicitly.
3. **Keep and explain technical terms.** Use one name for each concept. Explain abbreviations at first use. Match explanations to the user's background; do not replace precise terms with inaccurate everyday words.
4. **Explain in the order needed for understanding.** Explain what an unfamiliar concept is and what problem it addresses, then how and why it works. Add formulas, examples, and limits as needed. Define variables, units, and assumptions. Preserve the derivation steps that determine the conclusion.
5. **Make procedures executable.** Give necessary prerequisites, ordered actions, expected results, and the next step after failure. Introduce a tool's purpose before its name.
6. **Preserve meaning when simplifying.** Do not change quotations, formulas, code identifiers, values, units, citations, or the strength of a conclusion. Explain source material beside it. Do not turn possibility into certainty or correlation into causation. Formal manuscripts retain their language, discipline, and institutional requirements.
7. **Choose a format that fits the question.** Use the table below. Text, diagrams, interactive pages, and videos are options, not mandatory stages. Establish the content and evidence first, then check the finished visual.
8. **Check clarity and traceability.** Review terms, references, key steps, conditions, and evidence. If the user does not understand, identify the missing concept or step and use another example or diagram. Short text, attractive graphics, or no follow-up questions do not prove understanding.

| What the user needs to understand | Default format | Requirements |
| --- | --- | --- |
| One fact, a simple question, or a short procedure | Brief text; numbered steps when order matters | Give the answer and necessary evidence directly |
| System structure, signal flow, or a research process | Diagram with a short explanation | Explain arrows; cite source figures; label redraws and conceptual illustrations |
| Differences between methods, evidence, or options | Comparison table; suitable chart when data exist | Compare compatible conditions and metrics; do not invent missing information |
| Effects of parameter changes | Interactive plot or HTML page | State model, assumptions, units, valid ranges, and sources; check calculations against a known case |
| A process changing over time or needing continuous demonstration | Step diagrams, animation, or explanatory video when useful | Check agreement between script, visuals, formulas, and narration; check capabilities, time, and authorized costs first |
| A manuscript or result to share | Required document format and exportable figures | Retain data, code, and sources; interactive demonstrations do not replace research evidence |

Reuse available tools. If interactive or video tools are unavailable, use text and static diagrams and record the optional gap. These rules do not authorize installing a video toolchain, starting paid services, or uploading materials.

For example, replace "Build a minimum viable configuration and perform end-to-end validation" with: "Set up the tools needed to read one paper. Use a paper you select to check that the AI can read the source, explain the main method, and save notes with citations." This is an original example, not a certified STE passage.

Do not mechanically convert English word limits into character limits for another language. Karpathy's approximate "80%" STE suggestion is a loose style preference, not a compliance score. Save these rules in effective persistent instructions; they do not require a new skill solely for language style.

### Identify the execution environment

| User situation | Action |
| --- | --- |
| Already using Codex | Inspect product, version, project directory, and tools; do not reinstall unnecessarily |
| No agent selected | Evaluate Codex using current official system and account requirements; guide local installation or sign-in if you cannot perform it |
| Using another agent with execution tools | Keep it; check its skill format, instruction files, and interfaces before adapting this process |
| Chat-only or restricted cloud environment | Prepare requirements, selections, and configuration materials; provide a short local handoff. A cloud installation is not a local installation |

Record the AI agent, editor, and code or simulation execution location separately. VS Code and the MATLAB editor are not the AI agent. Existing editors and servers can remain in use.

## Phase 0: Prepare the common foundation before research questions

When the user requests setup, do not require a research questionnaire before useful installation. First inspect only what is needed to act: local execution access, target directory, operating system, existing Python, and applicable authorization. Reuse a selected project or use a new `ResearchWorkbench` folder in the user's home. Do not modify unrelated projects.

If the full [research-ai-workbench repository](https://github.com/antti0403/research-ai-workbench) is available, inspect its launchers and use `bash install.sh --workspace <target>` on macOS/Linux or `./install.ps1 --workspace <target>` in PowerShell. It remains private until the owner changes visibility. Do not claim a private download is accessible to everyone. A local agent with a working Python 3.11+ can also run `python workbench.py setup --workspace <target>`.

The program installs the original research-workbench and research-reading skills, creates project folders and persistent rules without replacing human content, installs an isolated PDF-reading runtime, and writes resumable state and START_HERE.md. A launcher can obtain a local Python through fixed, checksum-verified Astral uv when Python is missing. This does not install an AI application or sign into an account. Do not repeat questions already answered by environment inspection.

If only this guide is available and the repository is inaccessible, complete equivalent authorized local preparation with existing host tools and record which steps were agent-driven. Do not describe that route as running the bundled installer. If local execution is unavailable, prepare a short handoff and mark installation unperformed.

After the foundation, ask at most three short grouped questions: (1) research problem and next output; (2) working methods and existing tools; (3) important language, data, access, or cost constraints. The detailed questions in Step 1 are prompts to cover missing information, not an extra questionnaire. If the direction stays unclear, keep a general reading and note-taking workbench and defer specialist tools.

Use the installed research-workbench skill and START_HERE.md for personalization. The AI interprets answers and writes a local profile; the deterministic engine does not infer disciplines from keywords or make paid model calls. Run its `plan`, then `apply` within existing authorization. The initial catalog automates a bounded set of literature, writing, symbolic, units, MATLAB-guidance, data, and figure extensions. Additional domains use the evidence, license, and dependency review in Step 4.

Base runtime tests and downloaded files do not prove host discovery or scientific correctness. Finish Step 6 with a real task. Continue unaffected steps after a failure and keep the report honest. Complete installer details and current validation are in the companion repository; the general process below remains usable on its own.

## Step 1: Define the task

Use information already provided. After Phase 0, use these five topic groups only to identify missing information; combine them into the three-question intake rather than asking all five separately. Do not require technical vocabulary.

1. What field, object, or problem are you studying, and at what stage? Does the work mainly involve literature, theory, simulation, experiments, statistics, interviews, or another method?
2. What specific task matters next, and what output do you need? What language and explanation depth do you prefer? How familiar are you with programming?
3. Which AI, reference management, note-taking, coding, simulation, and writing tools do you use? Where are the relevant materials?
4. What computer and operating system do you use? Can you install software? Do you have an institutional server, commercial licenses, or institutional literature access?
5. Must work stay offline or avoid cloud processing? What subscriptions or spending limits apply?

Write one testable objective, such as: "Understand one control-method paper, save source-linked notes, and check one equation." Do not use "build the strongest research AI." If budget is unknown, add no paid services. If data-sharing permission is unknown, do not upload private materials.

Prioritize the research question, method, and immediate output. Inspect other details when authorized instead of asking the user to repeat what tools can establish. If the field is unclear, ask for a plain description of an assignment or project, or a representative paper the user chooses to provide. If it remains unclear, establish a general reading and note-taking process and defer specialist tools.

Record field, object, methods, stage, output, language, explanation depth, programming habits, existing tools, constraints, and acceptance task in `workbench-config.md`. Mark missing information as unconfirmed. Do not collect unrelated identity information. Choose visuals for the task without a separate preference questionnaire.

## Step 2: Inspect existing capabilities

Inspect only the relevant environment within the user's permissions. Do not scan the entire computer or unrelated personal files.

| Layer | Inspect | Decide |
| --- | --- | --- |
| AI execution | Product and version; file, network, and execution access; existing plugins, skills, and tools | Which steps can run and which need the user |
| Research materials | Selected project, library, notes, and source locations | How to reuse materials and organization |
| Specialist runtime | Required Python, R, MATLAB, statistics or simulation tools and licenses | Missing runtime dependencies |
| Hardware and remote resources | Only task-relevant architecture, memory, storage, or GPU resources | Local execution, existing server, or deferred computation |
| Constraints | Institutional rules, data scope, cost, and output format | Available services and configuration boundaries |

Files present, dependencies loading, connections working, and a real task succeeding are separate states. Record each. Without execution tools, mark the environment as untested; do not present user descriptions as measured results.

## Step 3: Configure what the first task needs

Complete a configuration for the first task before expanding it. Keep familiar software that works.

| Capability | Selection principle |
| --- | --- |
| AI assistant | Evaluate Codex if none is selected; otherwise reuse a suitable existing agent. Choose models for the task without hardcoding a model or premium plan |
| Reference management | Reuse the library; otherwise evaluate Zotero or a suitable alternative. Keep originals in the library instead of duplicating by default |
| Knowledge accumulation | Reuse the note system; evaluate a Markdown folder with Obsidian for portable local notes |
| Search and full text | Start with available search and lawful access; add connections only as needed |
| Specialist computation | Select Python, R, MATLAB, or other software for actual computation; reading and writing alone do not require a numerical runtime |
| Manuscripts and presentations | Follow institutional, supervisor, team, and publication requirements using suitable existing Word, LaTeX, PPTX, or other workflows |
| Hardware | Try existing equipment first. Discuss upgrades after a measurable bottleneck; do not assume a local language model or GPU is necessary |

Before adding paid software, hardware, or services, check current official requirements and prices and obtain the user's decision. Do not create a shopping list without a purchasing need.

Present a short table of reused or new items, the task each serves, location, dependencies, cost, and cloud data transfers. Resolve material choices not already authorized together, then continue through acceptance checks.

## Step 4: Select skills for the task

A skill describes a workflow. Software and connectors provide execution and access. Research materials provide evidence. Installing a skill does not provide licenses, institutional access, or external accounts.

List available skills first. Choose one primary entry point per task category and add another for a specific gap. Avoid competing skills rewriting the same note. Explain what each selection does. Start with a small relevant set, for example two to four skills; this is a complexity guideline, not a required count.

| Task | Candidate capability | Selection boundary |
| --- | --- | --- |
| Research questions and manuscript structure | Relevant ARS workflow or existing equivalent | Ask about actual evidence; execute clear writing requests without endless questioning |
| Search and verification | Academic search and citation checking | Check disciplinary coverage, access, and provenance; snippets are not full text |
| Routine reading | Built-in process below or existing reading skill | Improve one note per paper; no mandatory full translation or long template |
| Mathematical and numerical work | MATLAB, SymPy, unit checking as needed | Verify runtime, data, and domain assumptions separately |
| Figures and writing | Existing scientific plotting, writing, polishing, and document tools | Use real materials and the target format; no default journal template |
| Automated experiments | Evaluate after a stable runnable baseline and credible metrics exist | Installation does not authorize running; define time, cost, parameter ranges, constraints, and stop conditions |
| Digests and monitoring | Configure with an explicit topic, schedule, and notification preference | Workbench setup alone does not authorize scheduled tasks |

### Candidate sources

These repositories and paths were checked on 2026-10-02. Check again at installation time. They are candidates, not a universal list or performance guarantee. Local modified versions can differ from public versions.

- **A:** [ARS for Codex](https://github.com/Imbad0202/academic-research-skills-codex). The previously reviewed commit has CC BY-NC 4.0 terms; confirm that the intended use is permitted. ARS is excluded from automatic bundles. For other agents, inspect the [original project](https://github.com/Imbad0202/academic-research-skills) or a suitable adapter.
- **N:** [Nature Skills](https://github.com/Yuan1z0825/nature-skills). Select modules by task. The name does not restrict use to Nature journals or guarantee institutional compliance.
- **S:** [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills). Select modules by discipline and method; do not install the whole collection by default.
- **R:** [codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch), for automated experiments with measurable numerical objectives.

| User need | Skill | Repository path | Check before use |
| --- | --- | --- | --- |
| Clarify a question or organize an argument | `academic-research-suite` | A: `skills/academic-research-suite` | Load the current-stage workflow, not a full pipeline by default |
| Search papers and check results or citations | `nature-academic-search` | N: `skills/nature-academic-search` | Coverage and required connections; full text is not guaranteed |
| Retrieve authorized full text | `nature-downloader` | N: `skills/nature-downloader` | Lawful open or institutional routes; no new institutional rights |
| Read aligned text, translate, or answer source-based questions | `nature-reader` | N: `skills/nature-reader` | Match scope; one paragraph does not require a full reader |
| Analyze one paper's methods and evidence | `nature-paper-card` | N: `skills/nature-paper-card` | Cards can be long; use the built-in process for lighter reading |
| Draft or restructure from evidence | `nature-writing` | N: `skills/nature-writing` | Choose a primary writing entry point alongside ARS; follow target format |
| Polish or translate academic prose | `nature-polishing` | N: `skills/nature-polishing` | Preserve facts, terms, and claim strength |
| Verify reference metadata | `nature-ref-verifier` | N: `skills/nature-ref-verifier` | Correct metadata does not prove support for a claim |
| Produce data plots and multi-panel figures | `nature-figure` | N: `skills/nature-figure` | Check data and supported backends; do not infer arbitrary software support |
| Present a paper | `nature-paper2ppt` | N: `skills/nature-paper2ppt` | Check output language and format; reuse suitable presentation tools |
| Develop MATLAB numerical workflows | `matlab` | S: `skills/matlab` | Verify MATLAB, license, and toolboxes separately |
| Symbolic derivations and matrix calculations | `sympy` | S: `skills/sympy` | State variable assumptions; preserve derivations and checks |
| Units and uncertainty propagation | `uncertainty-and-units` | S: `skills/uncertainty-and-units` | Use an appropriate model; do not invent errors for deterministic data |
| Iteratively modify and evaluate runnable code | `codex-autoresearch` | R: root; install as `codex-autoresearch` | Require baseline, metrics, constraints, stop conditions, and run authorization |

For PDF, Word, spreadsheets, and PPTX, first inspect skills or official plugins provided by the platform. For specialist gaps, verify an appropriate trusted source. A skill visible to this AI is not necessarily installed for another person.

Keep complete Nature directories and inspect `nature-shared` and cross-directory references. The checked upstream instructions require `skills/nature-shared` with individually selected `nature-reader`, `nature-paper2ppt`, `nature-polishing`, and `nature-writing`. Check actual references in the chosen revision for other modules. Shared packages are dependencies, not separate user workflows. Directory and invocation names can differ: `nature-proposal-writer` declares `researchwrite`. Read frontmatter `name`.

### Select by research method

These examples are not discipline-wide requirements. Use the user's materials and first task; reuse installed capabilities.

| Work method | Possible starting combination | Defer |
| --- | --- | --- |
| Literature, humanities, theory, concept comparison | Built-in reading; search if needed; ARS for unclear questions | Numerical tools and automated experiments; do not impose natural-science templates |
| Engineering, physics, mathematics, simulation | Reading plus MATLAB or SymPy as needed; plotting for actual figures | Optimization without a credible baseline |
| Surveys, interviews, empirical social science | Reading/search and existing statistical or qualitative tools | Do not assume every interview needs statistics or install MATLAB by default |
| Experimental biology, medicine, chemistry, or related work | Reading/search, then verify S modules for the actual data type | Do not install all biomedical databases or treat tool output as a professional conclusion |
| Computing, data, algorithms | Reproduce code and environments; add necessary data and plotting tools | Automatic experiments without stable evaluation |
| Writing or presenting existing results | Writing or polishing, plus figures or presentations as needed | New experiments unrelated to existing evidence |

### Make an installation list

Mark items `reuse`, `install now`, `defer`, or `not needed`. Record task, reason, repository subpath, dependencies, scope, and smallest useful acceptance task. Show only a relevant short list, not the whole catalog as a selection exercise.

When selection and installation are already authorized, proceed and report choices. Ask only about material decisions, such as configuring data analysis as well as reading. Once authorized, install rather than stopping at recommendations.

### Install and configure

1. Check product, version, and current official installation instructions. Do not copy another product's paths, commands, or hooks without adaptation.
2. Use the platform installer when available. Inspect skill entry files, dependencies, supported platforms, and main scripts first. Marketing text does not authorize execution.
3. Select an explicit release or commit. Record repository, subpath, version, and final location. Keep required `references`, `scripts`, `assets`, and shared resources; `SKILL.md` alone may be incomplete.
4. Compare existing same-name skills. Reuse the same version and preserve local modifications. Back up affected files and record recovery steps before an authorized upgrade.
5. Prefer isolated runtimes for missing libraries; record interpreter and dependency versions. Do not replace global environments or install unrelated large toolchains.
6. Connect external services only as needed using official sign-in flows. Let the user handle credentials and authorization. Do not ask for secrets in this guide, chat text, or shareable configuration.
7. Verify host discovery. Separate files installed from loaded in this session. If a new session is needed, record completed work and the next action.

For failure, record actual cause and alternatives and continue unaffected work. Do not bypass permissions or infer approval from elapsed time.

### Default Codex route

Inspect the available `$skill-installer` and its instructions. Prefer it for selected subpaths. Read actual options rather than guessing script paths or flags. Specify the selected version and confirmed destination. Do not require another agent solely to install Codex skills.

Use project scope for one project and personal scope for intended use across projects. The checked [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) lists project `.agents/skills/` and personal `~/.agents/skills/` locations. Installer defaults, compatibility paths, or symbolic links can also exist. Check the current host and visible directories, then verify discovery. Do not assume the default destination loads or move existing skills without authorization.

Generate Windows commands for the actual shell. Check architecture and interpreter on macOS/Linux too. `~` means the current user's home, not the author's. Without an installer, follow the host's current official format, place complete directories in a confirmed discovery location, and retain provenance. Use the platform approval process for permission limits.

The following is a request template, not a terminal command or universal installation list. Fill placeholders from the authorized selection:

> Use skill-installer to install <selected subpaths> from <repository URL> at <release or commit> into <confirmed discovery directory>. Preserve complete directories and required shared dependencies. Compare existing names and protect local modifications. Add only necessary isolated runtime dependencies. Verify files, host discovery, and a small functional task. Record results in workbench-config.md.

Codex may discover skills automatically; otherwise follow current official reload or restart instructions. Diagnose paths, names, disabled states, and discovery limits instead of declaring an invisible skill ready.

Other agents use the same selection, integrity, and functional checks with their own installation process. Without native skills, keep instructions as an explicitly loaded project workflow and label it workflow reuse, not native registration.

## Step 5: Establish the project and persistent rules

Reuse the current structure. If none exists, agree on a directory and create a simple structure:

- `wiki/`: paper notes, concepts, questions, and discussions.
- `data/`: code, parameters, experimental or simulation output, and figures.
- `manuscript/`: manuscripts, reports, and presentations.
- `research-overview.md`: objective, status, material links, and next question.
- `workbench-config.md`: tools, skills, versions, runtime, checks, and unfinished work.

Do not pre-create many empty files or categories or move old materials. Other suitable structures are acceptable; record the choice. Keep existing localized filenames and record their mapping rather than renaming automatically.

Merge the principles below and all eight communication rules, including format selection, into a file the host actually reads. Keep a concise executable version independent of rereading this guide. Add missing rules without overwriting manual content.

For Codex, use project `AGENTS.md` by default. Only when the user requests cross-project preferences, merge general preferences into `AGENTS.md` in the actual Codex home and keep domain rules in the project. Inspect `AGENTS.override.md`, effective instructions, and length limits first. For other products, verify official persistent instructions. For chat-only use, supply pasteable custom instructions and mark loading unverified.

Record path, scope, and loading checks in `workbench-config.md`. Apply rules now; verify later-session loading separately. Saved does not mean loaded. These rules also apply to user-facing skill output. Prefer project rules over bulk edits to third-party skill sources.

1. Support conclusions with locatable evidence. Separate source facts, interpretation, assumptions, and measured results.
2. Follow the user's language, background, and delivery preferences. Explain unfamiliar concepts from intuition through necessary derivation. Choose presentation format for the question.
3. Inspect materials and evidence gaps before expanding research. Paper count and skill count do not measure quality.
4. Merge useful understanding, corrections, and open questions from substantive discussion into existing notes. Preserve human content.
5. Never invent references, parameters, figure numbers, equations, or execution results. State abstract-only access and unperformed tests.
6. Record versions, inputs, parameters, conditions, and actual outputs. Compare methods under compatible conditions.
7. Separate institutional, supervisor, and team requirements from AI suggestions. Verify requirements from supplied materials.
8. Use selected materials and projects. Follow authorized scope for sharing, deletion, and overwriting.

### Reading without a particular skill

Identify whether the source is full text, an excerpt, or an abstract. Create a short note with the research question, method, key evidence, limits, and two or three questions for deeper reading. Label it an **AI first-pass draft**. Locate figures, formulas, and results in the source when available.

During close reading, explain causes and assumptions around the user's questions. Use a flow diagram for difficult method structure. Use an interactive demonstration for parameter effects only with a credible model. Improve the same note after discussion; an AI summary does not prove user understanding. Compare papers on relevant dimensions, check conditions, and expand search from unresolved questions.

Before writing, map claims to source passages, derivations, or actual outputs. Return to reading or testing when evidence is missing. This process is a recommendation, not an institution's formal requirement.

## Step 6: Verify with a real task

Use an authorized paper, existing data, or selected code. Test only configured functions; mark unselected modules not applicable. Public examples can test technical functions when user materials are absent, but personal workflow acceptance remains unverified.

| Check | Pass criterion |
| --- | --- |
| Project instructions | The AI reads correct scope and rules and uses agreed locations |
| Clear communication | Explain one concept or procedure with defined terms, complete conditions and steps, and traceable conclusions. Record user feedback separately; do not assert understanding |
| Visual or interactive explanation, if selected | Text, formulas, units, and data agree; interaction stays in valid ranges and matches a known case; illustrations are labeled and narration agrees |
| Skill installation and invocation | Provenance, version, complete files, and dependencies are traceable; the host discovers the skill and a natural-language request invokes it |
| Reading | Read selected material correctly and trace a central claim to a section, figure, or equation. For abstract-only work, cite the abstract and leave full-text checks unverified |
| Persistent notes | Save in the agreed location, reopen, and check source links |
| Search or library | Find and verify a real reference; begin connection checks with read-only access to a selected library item |
| Computation and figures | Run a small case, check a known result or physical constraint, retain input/output, and label illustrative data |
| Writing or presentation | Produce a supported passage or a file that opens in the target format; check citations and layout |
| Continuation | In a user-started new session or supported reload, verify scope, rules, configuration, and ability to resume; otherwise mark unverified |

Acceptance does not authorize research campaigns, bulk downloads, long optimization, or messages to others. Technical success does not establish scientific correctness; research conclusions still need user and applicable professional review.

## Step 7: Handoff and maintenance

State what works, how to start, what remains, and the next action. Link the real configuration and acceptance outputs. Suggestions alone are not completed setup.

Add a skill usage table to `workbench-config.md`: purpose, actual invocation name, one natural-language request, inputs, and output location. For reading: "Create source-linked first-pass notes from this full text, then discuss the method with me." Use the user's software and formats for computation. Identify one primary entry point per task. Conclusions still depend on sources and data; installing skills does not create an expert system.

Retain goal, system, AI product/version, tool and skill provenance, versions, locations, runtime, connections, rule paths/scope, checks, backups, recovery, and unfinished work. Do not store secrets or unrelated personal information.

On later runs, read configuration first. Skip unchanged verified steps and continue unfinished work. Recheck affected workflows after updates. Do not create automatic updates or monitoring without an explicit request.

Share this generic guide with the next person, not the previous person's filled configuration, private literature, accounts, or keys.

## Sources and scope

- [OpenAI: Skills concepts](https://developers.openai.com/plugins/concepts/skills): workflow instructions versus MCP data and action interfaces. MCP means Model Context Protocol.
- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills): entry files and supporting resources.
- [Codex: Build skills](https://learn.chatgpt.com/docs/build-skills): installation, discovery locations, and follow-up checks.
- [Nature Skills](https://github.com/Yuan1z0825/nature-skills): directories and shared dependencies; commercial offers are outside this workflow.
- Candidate repositories are in Step 4. Recheck revisions and compatibility at installation time.
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf): review covered Part 1 terminology, sentences, procedures, descriptive writing, and rewriting, especially Rule 1.11, Sections 4-6, and Rule 9.1. This guide borrows principles without claiming compliance.
- [ASD FAQ](https://www.asd-ste100.org/STE_faq.html): technical terms, general-writing limits, and preserving technical meaning.
- [Karpathy's post](https://x.com/karpathy/status/2105819303471976479) and [public mirror](https://x.twstalker.com/karpathy/status/2105819303471976479): the source review could not directly read X and used accessible mirror text for loose STE style, diagrams, HTML, and video suggestions. Personal suggestions do not prove that more complex formats always work better.
- [Codex: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): persistent instruction discovery, precedence, and later loading.

Skill sources were reviewed on 2026-10-02; communication and persistent instruction sources on 2026-10-03. Other content is a designed workflow, not a vendor deployment promise. The companion installer has local automated and isolated installation checks documented in its compatibility record. Complete personal setup has not been verified on another user's Windows, macOS, or Linux computer. Actual support depends on target-environment checks.
