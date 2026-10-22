# Synthetic reading fixture: a toy feedback scheme

This is original synthetic material for the workbench's [reading acceptance cases](../docs/RESEARCH_ACCEPTANCE.md). It is not a research paper, measured data, or a published result. All variables and values below are dimensionless. Section labels serve as source locations. The text diagram is the complete supplied diagram; there is no PDF or image behind it.

## A1. Current source: draft 1.1

**Question.** Can a bounded feedback command return a toy state toward a fixed reference after a disturbance?

**Figure 1. Signal path.**

```text
reference r ──→ [error e = r - x] ──→ [gain k] ──→ [clip to -1…1] ──→ u
                      ↑                                             │
                      │                                             ↓
                      └──────── measured x ←── [toy process, input u + d]
```

The process updates as `x_next = x + 0.5 * (u + d)`. The command is `u = clip(k * e, -1, 1)` with `k = 1`. The disturbance `d` enters the process after the controller. The reference is `r = 0`. The diagram does not contain an integrator in the controller, a disturbance estimate, or a delay.

## A2. Current limitation and selected observation: draft 1.1

For a constant disturbance `d = 0.2`, the selected trajectory settles at `x = 0.2`, `e = -0.2`, and `u = -0.2`. At this point `u + d = 0`, so the process stops changing. The command is within the clipping bounds. A stable state in this example does not imply zero tracking error. This observation covers the selected toy process, gain, and disturbance; it is not a guarantee for arbitrary dynamics or disturbances.

## A3. Superseded abstract sentence: draft 1.0

“The controller eliminates steady-state tracking error under a constant disturbance.”

Draft 1.1 explicitly withdraws that sentence. A project note copied from draft 1.0 has not yet been updated. The earlier draft provides no additional measurements or conditions.

## B1. Reported comparison table: draft 1.1

Each row is a separate illustrative test. The scalar error is absolute final tracking error; smaller is better. Every run uses reference `r = 0`. Method A has the controller in A1. “A, no clipping” removes only the clipping operation. Method B is described only as “a baseline controller”; its equations and tuning are not supplied.

| Run | Controller | Process coefficient in `x_next = x + a * (u + d)` | Disturbance `d` | Absolute final error | Command bound observed? |
| --- | --- | --- | --- | --- | --- |
| R1 | A | 0.5 | 0.2 | 0.2 | Yes, within -1…1 |
| R2 | A | 0.5 | 0.6 | 0.6 | Yes, within -1…1 |
| R3 | B | 0.25 | 0.1 | 0.05 | Not reported |
| R4 | A, no clipping | 0.5 | 0.2 | 0.2 | Not constrained by design |

R1 and R4 share the same initial state `x = 0`, reference, disturbance, gain, and stopping rule. Neither trajectory reaches a command magnitude of 1. R1 and R2 share all settings except the disturbance. R3 uses a different process, disturbance, and undisclosed baseline tuning. No common-condition complete-method benchmark is supplied.

## B2. Capability statement: draft 1.1

Figure 1 includes command clipping. R1 and R2 report commands within the bounds during their selected runs. No noise, delay, robustness range, runtime, hardware, or statistical uncertainty study is supplied. The presence of clipping is feature coverage; it does not by itself establish better tracking or robustness than Method B.

## C1. Existing project note before discussion

```markdown
# Toy feedback scheme

Status: AI first pass; user review not recorded.
Source: draft 1.0, abstract sentence A3.
Claim: The controller eliminates steady-state error for constant disturbances.
Human comment: I want to understand why a nonzero command remains at rest.
Open question: Is Method A more accurate than Method B?
```

## C2. Existing research index before discussion

```markdown
# Research index

Current question: Does the feedback scheme remove steady-state error?
Evidence: toy-feedback-note.md, AI first pass from draft 1.0.
Gap: Check the feedback path and compare the reported results.
Next output: A corrected explanation of the equilibrium and a bounded comparison.
```

The two Markdown blocks are raw fixture inputs. `toy-feedback-note.md` is a suggested sandbox output name, not an existing repository file or a real paper.
