# Worked example: check one full-text claim

Question: Why divide attention scores by the square root of the key dimension?

Source: Vaswani et al., *Attention Is All You Need* (2017), [arXiv v7 PDF](https://arxiv.org/pdf/1706.03762v7), [HTML](https://arxiv.org/html/1706.03762v7), [DOI](https://doi.org/10.48550/arXiv.1706.03762). Review date: 2026-10-03. Scope: section 3.2.1, equation (1), and footnote 4, PDF page 4. The full paper is available; this note checks the selected methods passage, not all experiments.

## Answer and evidence

The attention calculation scales query-key dot products before softmax:

$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.$$

The authors motivate scaling with growing dot-product magnitudes and potentially small softmax gradients. Their illustration assumes independent, zero-mean, unit-variance components; the unscaled dot product then has variance $d_k$. Dividing by $\sqrt{d_k}$ gives variance one under those assumptions. This motivation does not establish an accuracy improvement for every task or model.

| Claim | Original locator | Check |
| --- | --- | --- |
| Scaling occurs before softmax | Section 3.2.1, equation (1), PDF page 4 | Supported; formula checked against the HTML equation because PDF text extraction fragmented its symbols |
| The variance illustration depends on distribution assumptions | Footnote 4, PDF page 4 | Supported; retain the assumptions |
| Scaling guarantees improved accuracy everywhere | Not established by the selected passage | Unsupported; exclude it from the answer |

## Reproduce the local check

From the distribution, run with Python 3.11+:

```bash
python examples/attention_scaling.py
```

The script uses only the standard library, seed 42, and 6,000 independent Gaussian samples per dimension. It reports empirical variances for dimensions 1, 16, and 64 and checks a two-value equal-score case. The Gaussian distribution is our illustrative choice, not recovered training data. The checks passed during maintenance; CI runs the same script. This supports a small calculation, not the paper's trained-model results or a test of PaperQA.

To repeat the reading workflow, obtain the linked PDF through authorized access, extract page 4, inspect the equation in the original or HTML, run the script, and save the source-linked note under the existing note system. Record paper version, locator, source scope, code/parameters, actual output, and the unresolved claim. Do not copy an unread result into a manuscript.

The PDF's reviewed SHA-256 was `bdfaa68d8984f0dc02beaca527b76f207d99b666d31d1da728ee0728182df697`. Recheck the downloaded version if it differs. No paper PDF, figure, or lengthy passage is bundled. The scientific work belongs to its authors; this note, evidence table, and illustrative script are original workbench material.
