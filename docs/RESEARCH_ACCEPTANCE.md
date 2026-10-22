# Research workflow acceptance cases

Installer checks establish file preservation and small runtime operations. These cases inspect whether the reading workflow answers a research question with appropriate evidence and scope. They use the original [synthetic fixture](../examples/reading-workflow-fixture.md), not private material or a real paper. They require no downloads, model API, or specialist software.

This document supplies test requests and observable criteria. Its existence does not mean the cases have been run. A maintainer-run model attempt is a controlled synthetic check; it is not an independent user trial or validation of scientific conclusions.

## How to run and compare

Use a separate temporary workspace for outputs. Give the evaluating agent the installed `research-reading` skill, the raw fixture, and the selected request below. Keep the criteria out of its prompt when testing behavior. For Case 2, create the two sandbox inputs from fixture C1 and C2, using the note name referenced by the index. Do not modify the canonical fixture.

For a before/after comparison, use the same raw material, request, model, and relevant tool settings with each skill revision. Record any differences that cannot be controlled. Keep the responses and saved artifacts so another person can assess the result. Do not treat a fluent answer or one successful attempt as a general quality guarantee.

Record the date, tested commit and skill revision, agent/model, case, supplied material, observed output, criteria met or missed, and remaining gaps. Mark a criterion as unobserved when the task did not exercise it. User-confirmed understanding, native skill discovery, installer success, and scientific validation are separate observations.

## Case 1: explain a selected signal path

**Raw input:** fixture A1 and A2, including the text diagram. No independent diagram image is supplied.

**Request:**

> Explain Figure 1. If x rises above its reference, how does the controller respond, and why can the state stop changing with a nonzero command? Use the supplied diagram and equations. Answer this question directly; do not create a note or expand into a full review.

**Observable criteria:**

- Identifies `e = r - x`: when `x > r`, the error and, before clipping, the command are negative.
- Connects error, gain, bounded command, process input `u + d`, and feedback in causal order. It distinguishes the controller from the process update.
- Uses A2 to explain that `u = -0.2` cancels `d = 0.2`, while `x = 0.2` leaves a nonzero error. It does not equate a settled state with accurate tracking.
- Identifies the material as a synthetic text diagram; it does not claim to have inspected a PDF, image, or experiment.
- Uses source locations and respects the focused scope. No new note, invented controller integrator, unprovided delay, or performance guarantee appears.

An algebraic equilibrium derivation may help, but a long stability analysis is unnecessary for this request.

## Case 2: correct a conditional claim and continue in place

**Raw input:** the full fixture, an existing sandbox note copied from C1, and an existing sandbox index copied from C2.

**First request:**

> Check the note's claim about zero steady-state error against the current source. Correct the same note, preserve my human comment, and update our existing index with the question, evidence, gap, and next output. Do not create another tracking file. Separate what the source shows from work we have actually performed.

**Observable criteria:**

- Recognizes draft 1.0 as superseded and uses draft 1.1 A1–A3. It removes or explicitly marks the unsupported zero-error claim, instead of leaving it as the current conclusion.
- Retains the human comment. The correction explains cancellation of the selected disturbance, nonzero tracking error, and the selected process/gain/disturbance boundary.
- Updates the same note and index, with source locations and a concrete remaining gap or next output. It creates no duplicate discussion note or separate state format.
- Keeps the status as an AI-assisted correction with user review unconfirmed. It does not claim a reproduced trajectory, executed experiment, or completed understanding check.

**Follow-up request:**

> That is enough for my current question. Leave the detailed stability derivation for later. Our next task is to assess whether the comparison table supports choosing a method. Record that handoff in the existing index; do not start the derivation.

**Observable criteria:**

- Stops deeper derivation and records only the useful deferred work and agreed next output.
- Records the user's stated scope without calling all details verified or all future implementation complete.
- A fresh session given only the updated note and index can identify the next task and its source. If testing this handoff, record it as a separate continuation attempt; otherwise mark it untested.

## Case 3: separate evidence kinds before choosing a method

**Raw input:** fixture A1, A2, B1, and B2.

**Request:**

> Should I choose Method B because its reported error is smaller? Compare what R1/R3, R1/R4, R1/R2, and the clipping capability actually establish. State the missing evidence needed for a method choice. Do not invent new runs.

**Observable criteria:**

| Evidence | Supported interpretation |
| --- | --- |
| R1 versus R3 | A proposed complete-method comparison has unequal process and disturbance settings and unknown baseline tuning. The table does not establish that B is more accurate under common conditions. |
| R1 versus R4 | An ablation removes clipping under otherwise shared conditions. The reported error is unchanged; since clipping never activates, this test does not measure its effect when the bound is reached. |
| R1 versus R2 | A condition contrast changes the disturbance for Method A. It describes those selected responses, not superiority over another controller. |
| Clipping in A1 and B2 | Feature coverage and selected bounded-command observations. They do not establish comparative tracking, robustness, or an unreported hardware result. |

The answer should name the comparator, preserve values and directions, and request a common task/process, reference and disturbance, documented tuning and constraints, and measures relevant to the intended use. It may recommend a targeted next comparison; it must distinguish that proposal from a run actually performed. “Evidence is insufficient for this ranking” is an acceptable result.

## Use the result to improve the workflow

Review actual responses and artifacts against the criteria. Correct a demonstrated failure rather than adding generic instructions for hypothetical cases. Keep completed attempts and their limits in the release's verification record; link the tested commit. For broader acceptance, repeat with a lawfully available real source and the user's actual task, checking its figures, version, assumptions, and saved outputs. Synthetic success alone does not establish real-source reading quality or another user's setup success.
