# Vaswani et al. (2017): Attention Is All You Need — abstract note

**Status: AI first-pass abstract draft; full-text reading and discussion pending.** Only the arXiv abstract page was read on 2026-10-03. The body, figures, and equations were not checked. This is the English adaptation of that note, not a new full-text review.

Source: [arXiv:1706.03762, abstract page](https://arxiv.org/abs/1706.03762). The page lists an initial submission in 2017 and version 7 revised in 2023. All paper-specific statements below come from its abstract.

## Main proposal

The authors introduce the Transformer, a sequence transduction model built around attention without recurrent or convolutional components. Translating a sentence from one language into another is one example of a sequence transduction task.

The abstract reports improved quality, parallelization, and training time in two machine translation tasks relative to the comparisons described there. These are author-reported results. This reading did not inspect comparison conditions or reproduce experiments. Historical leading results are not a claim about current rankings.

## Questions for full-text reading

1. How is attention calculated, and how are positions represented? Inspect methods and equations.
2. Which hardware, model sizes, and training conditions support the parallelization and time comparisons? Inspect experimental settings.
3. Does the method fit the user's research data? Define the target task and inspect relevant full-text evidence.

The abstract cannot answer these questions. Add source sections, key figures, and evidence to this same note during close reading. Do not mark this abstract draft as a completed detailed review.
