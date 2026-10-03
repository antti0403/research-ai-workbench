# Third-party sources, dependencies, and acknowledgements

Reviewed on 2026-10-03 for repository 0.3.1 and guide 1.7. This inventory describes how this project uses each source. A public repository is not necessarily open source, and a source credit is not a substitute for permission. Linked license texts and component-specific notices control reuse.

## What this repository contains

| Material | Relationship to this project |
| --- | --- |
| Installer, launchers, helpers, tests, `research-workbench`, `research-reading`, `research-paperqa`, guide and templates | Developed for this project with AI assistance. The project's MIT license covers these original contributions. External ideas and APIs are credited below. |
| Third-party skills | Not vendored here. The installer obtains selected files from upstream using catalog revisions and hashes. |
| Python, uv, Python packages and their native libraries/fonts | Not bundled here. Obtained or reused during setup; their distributions keep their own licenses. |
| Paper example | An attributed abstract paraphrase in `examples/attention-abstract.md`, not a reproduced paper, figure, or full-text review. |
| Video, transcript, social post, ASD-STE100 and product documentation | Linked sources of ideas or technical guidance. Their distributions are not included or relicensed. |

## Skills selected by the installer

### Nature Skills

- **Creator/maintainers:** 袁一哲 / [Yuan1z0825](https://github.com/Yuan1z0825) and contributors. The upstream README identifies its creator.
- **Revision:** [84880815fb37317b3766bff2c2abba395b8993c3](https://github.com/Yuan1z0825/nature-skills/tree/84880815fb37317b3766bff2c2abba395b8993c3).
- **License:** [pinned root Apache-2.0](https://github.com/Yuan1z0825/nature-skills/blob/84880815fb37317b3766bff2c2abba395b8993c3/LICENSE), subject to nested exceptions below. Its template appendix does not identify an additional copyright holder; this project does not invent one.
- **Use:** `literature` selects `skills/nature-academic-search` and `skills/nature-ref-verifier`; `writing` selects `skills/nature-shared`, `skills/nature-writing`, and `skills/nature-polishing`.
- **Integration:** Download the pinned archive, verify SHA-256, and extract the selected directories without changing their contents. Any root `LICENSE`/`NOTICE` is retained as `UPSTREAM_LICENSE`/`UPSTREAM_NOTICE`; in-directory notices are retained. The cache contains the full archive, including unselected material; it is not a distributable package owned by this project.
- **Redistribution:** Preserve the license and relevant copyright, attribution and NOTICE texts for covered files; mark modified files. Check nested material independently. Our MIT license does not apply to these skills.

### Scientific Agent Skills

- **Creator/maintainers:** [K-Dense Inc. / K-Dense-AI](https://github.com/K-Dense-AI) and contributors. Upstream notice: Copyright (c) 2025 K-Dense Inc.
- **Revision:** [154988403bb5a18e9d3c0ce4e6d5e2e4b184a298](https://github.com/K-Dense-AI/scientific-agent-skills/tree/154988403bb5a18e9d3c0ce4e6d5e2e4b184a298).
- **License:** [pinned MIT license](https://github.com/K-Dense-AI/scientific-agent-skills/blob/154988403bb5a18e9d3c0ce4e6d5e2e4b184a298/LICENSE.md).
- **Use:** `symbolic` selects `skills/sympy`; `units` selects `skills/uncertainty-and-units`; `matlab` selects `skills/matlab`.
- **Integration:** Download individual files and the license with the hashes in `registry.json`. Skill contents remain unchanged; `UPSTREAM_LICENSE.md` carries the upstream license. We select and connect these skills; we did not author them.
- **Redistribution:** Retain the copyright and MIT permission/disclaimer text with copies or substantial portions. A MATLAB skill does not include MATLAB or grant a MathWorks license.

## Nested sources and exceptions

| Source / attribution | Upstream location and use boundary |
| --- | --- |
| [figures4papers — ChenLiu-1996 and contributors](https://github.com/ChenLiu-1996/figures4papers) | Nature `skills/nature-figure/assets/figures4papers/`. The [pinned notice](https://github.com/Yuan1z0825/nature-skills/blob/84880815fb37317b3766bff2c2abba395b8993c3/skills/nature-figure/assets/figures4papers/THIRD_PARTY_NOTICES.md) reports no confirmed reuse license for its scripts/images. `nature-figure` is excluded from automatic selection in 0.2.1; `figures` retains NumPy and Matplotlib. Version 0.2.0 selected the full skill. Existing installations/caches are not removed. Do not republish these assets under our MIT or Nature's root license. |
| [Academic Phrasebank — John Morley, University of Manchester](https://www.phrasebank.manchester.ac.uk/) | Nature `skills/nature-polishing/references/phrasebank-playbook.md` and `section-moves.md` identify Phrasebank-derived guidance. Credit the original source as well as Nature Skills. The official site permits appropriate use/adaptation of generic phrases in writing and identifies the University as the intellectual-property owner. This is not a general license to redistribute its website or enhanced book. Neither is bundled here; bulk reuse needs its own terms review. |

The figures4papers notice refers to an older Nature root MIT license; the pinned root now contains Apache-2.0. Neither label grants missing rights to nested material. We preserve the notice rather than silently changing it.

Other upstream examples, papers, fonts, datasets and binary libraries can have separate terms. This review does not certify every upstream file or every platform's dependency tree. Inspect the actual materials and notices before redistributing downloaded directories or environments.

## Recommendations that are not automatic dependencies

| Project / author | Recorded source, license and role |
| --- | --- |
| Academic Research Skills / ARS Codex — Cheng-I Wu, Imbad0202 | [Codex revision 70b412fe69d3b5bf6b16adf64a96160bdd3c2d28](https://github.com/Imbad0202/academic-research-skills-codex/tree/70b412fe69d3b5bf6b16adf64a96160bdd3c2d28), [CC BY-NC 4.0](https://github.com/Imbad0202/academic-research-skills-codex/blob/70b412fe69d3b5bf6b16adf64a96160bdd3c2d28/LICENSE), [original project](https://github.com/Imbad0202/academic-research-skills). Candidate for research questions and arguments; not bundled or automatically installed. A paid setup service must not assume the noncommercial grant permits its use. Preserve attribution and identify adaptations if separately used. |
| Codex Autoresearch — Linxiao Li / leo-lilinxiao | [revision 0f54c571707487f59486ba7c50d405edfc746c19](https://github.com/leo-lilinxiao/codex-autoresearch/tree/0f54c571707487f59486ba7c50d405edfc746c19), [MIT license](https://github.com/leo-lilinxiao/codex-autoresearch/blob/0f54c571707487f59486ba7c50d405edfc746c19/LICENSE), [CITATION.cff](https://github.com/leo-lilinxiao/codex-autoresearch/blob/0f54c571707487f59486ba7c50d405edfc746c19/CITATION.cff). Candidate for constrained numerical experiments. Copyright notice names LLLLLe; citation metadata names Linxiao Li. Preserve supplied attribution. |
| Other Nature modules — Yuan1z0825 and contributors | Same pinned repository above; subpaths in [SKILLS.md](SKILLS.md). `nature-downloader`, `nature-reader`, `nature-paper-card`, `nature-paper2ppt` and withheld `nature-figure` are candidates. Review directory-level licenses/assets before installation. |

Earlier local installation records in SKILLS.md do not mean these candidates ship here or are installed for every user.

## Runtime dependencies

### Bootstrap and interpreter

| Component / attribution | Version, use, source and terms |
| --- | --- |
| uv — Astral Software Inc. and contributors | `0.12.22`, fallback when a suitable Python is missing. [Source](https://github.com/astral-sh/uv/tree/0.12.22), [MIT](https://github.com/astral-sh/uv/blob/0.12.22/LICENSE-MIT) or [Apache-2.0](https://github.com/astral-sh/uv/blob/0.12.22/LICENSE-APACHE). Our launchers invoke checksum-verified official installers; they do not contain uv's implementation. |
| CPython — Python Software Foundation and contributors | Existing Python 3.11+, or uv-managed Python 3.12; the environment determines the patch/build. [Python license/history](https://docs.python.org/3/license.html) includes incorporated software notices. [uv documentation](https://docs.astral.sh/uv/concepts/python-versions/) identifies [Astral python-build-standalone](https://github.com/astral-sh/python-build-standalone) distributions; builds and bundled libraries keep their own terms. |
| pip — PyPA / pip contributors | Version depends on bootstrap; not independently pinned. [Project](https://github.com/pypa/pip), [MIT license](https://github.com/pypa/pip/blob/main/LICENSE.txt), with separate licenses for vendored libraries. |

### Direct Python packages

Versions below are requested by `registry.json`. Credits identify upstream projects, not an exhaustive author list. Labels summarize the reviewed distribution metadata/license files. Full terms in each linked release remain authoritative. Packages are installed from PyPI, not vendored here.

| Package / attribution | Pinned release | Use | License summary |
| --- | --- | --- | --- |
| pypdf — Mathieu Fenniak and contributors | [6.19.0](https://pypi.org/project/pypdf/6.19.0/) | PDF reading | BSD-3-Clause |
| SymPy — SymPy Development Team | [1.14.0](https://pypi.org/project/sympy/1.14.0/) | Symbolic mathematics | BSD-3-Clause |
| Pint — Hernan E. Grecco and contributors | [0.26.1](https://pypi.org/project/pint/0.26.1/) | Physical units | BSD-3-Clause |
| uncertainties — Eric O. Lebigot and contributors | [3.2.3](https://pypi.org/project/uncertainties/3.2.3/) | Uncertainty propagation | BSD-3-Clause |
| NumPy — NumPy Developers | [2.5.3](https://pypi.org/project/numpy/2.5.3/) | Numerical arrays | Declared: BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0; retain all included notices |
| pandas — pandas Development Team and earlier credited contributors | [3.0.6](https://pypi.org/project/pandas/3.0.6/) | Tabular data | BSD-3-Clause; included components keep their notices |
| SciPy — SciPy Developers; Enthought credited in license | [1.18.1](https://pypi.org/project/scipy/1.18.1/) | Scientific computation | BSD-3-Clause project license; binaries include additional notices |
| Matplotlib — Matplotlib Development Team, John D. Hunter and contributors | [3.11.2](https://pypi.org/project/matplotlib/3.11.2/) | Plotting | Matplotlib license, based on the PSF license; bundled components have separate terms |

### Indirect packages observed during verification

These were resolved in the 2026-10-03 macOS arm64 verification environments. They are runtime dependencies, not separately requested skills. Versions may differ elsewhere. Actual installed versions are recorded under `.workbench/locks/`; `.dist-info` metadata and license files remain in each environment.

| Package / attribution | Observed release | Declared license / included notice |
| --- | --- | --- |
| contourpy — Ian Thomas and contributors | [1.4.0](https://pypi.org/project/contourpy/1.4.0/) | BSD-3-Clause |
| cycler — Thomas A. Caswell / Matplotlib project | [0.12.1](https://pypi.org/project/cycler/0.12.1/) | BSD; included LICENSE |
| fonttools — Just van Rossum and contributors | [4.66.1](https://pypi.org/project/fonttools/4.66.1/) | MIT; also LICENSE.external |
| kiwisolver — Nucleic Development Team | [1.5.1](https://pypi.org/project/kiwisolver/1.5.1/) | Modified BSD; included LICENSE |
| packaging — PyPA / packaging contributors | [26.3](https://pypi.org/project/packaging/26.3/) | Apache-2.0 OR BSD-2-Clause |
| Pillow — Jeffrey A. Clark and contributors | [12.3.0](https://pypi.org/project/pillow/12.3.0/) | MIT-CMU; linked libraries keep their terms |
| pyparsing — Paul McGuire and contributors | [3.3.3](https://pypi.org/project/pyparsing/3.3.3/) | MIT |
| python-dateutil — Gustavo Niemeyer and contributors | [2.9.0.post0](https://pypi.org/project/python-dateutil/2.9.0.post0/) | Dual Apache-2.0/BSD; included LICENSE |
| six — Benjamin Peterson and contributors | [1.17.0](https://pypi.org/project/six/1.17.0/) | MIT |
| mpmath — Fredrik Johansson and contributors | [1.3.0](https://pypi.org/project/mpmath/1.3.0/) | BSD; included LICENSE |
| flexcache — Hernan E. Grecco and contributors | [0.3](https://pypi.org/project/flexcache/0.3/) | BSD; included LICENSE |
| flexparser — Hernan E. Grecco and contributors | [0.4](https://pypi.org/project/flexparser/0.4/) | BSD-3-Clause |
| platformdirs — platformdirs / tox-dev contributors | [4.12.2](https://pypi.org/project/platformdirs/4.12.2/) | MIT |
| typing_extensions — Python typing contributors | [4.16.0](https://pypi.org/project/typing-extensions/4.16.0/) | PSF-2.0 |

pip 26.0.1 was also observed. Native libraries, fonts and pip-vendored modules are not fully enumerated by this package table; their notices ship inside the distributions. This is not a complete cross-platform software bill of materials or permission to strip notices when repackaging.

## Optional PaperQA integration

[PaperQA](https://github.com/Future-House/paper-qa) is by FutureHouse and contributors. Reviewed release: [v2026.08.12](https://github.com/Future-House/paper-qa/releases/tag/v2026.08.12), commit `57e89f7223b0960d5ee5ea048c69e3c47e088572`; installed package: [paper-qa 2026.8.12](https://pypi.org/project/paper-qa/2026.8.12/), Python >=3.11. It is downloaded only for the selected `paperqa` profile, without optional model/document extras; no upstream code is vendored or modified. The installed wheel retains `paper_qa-2026.8.12.dist-info/licenses/LICENSE`: Apache-2.0, copyright 2024 FutureHouse. [Pinned upstream license](https://github.com/Future-House/paper-qa/blob/57e89f7223b0960d5ee5ea048c69e3c47e088572/LICENSE). The reviewed PyPI wheel SHA-256 is `4cdf007207dea58edf1c1f3507ca33e1e7737fd8d7a17cb1736a8a089463918c`; pip pins the direct version, but this installer does not enforce that wheel hash or hash-lock all transitive dependencies.

Required dependencies include `paper-qa-pypdf`, `fhaviary`, `fhlmi`, LiteLLM and its provider clients, NumPy, Pydantic, tiktoken, tantivy, and HTTP/text/metadata utilities. Their individual distributions retain their licenses and notices in the isolated environment; resolved versions are recorded in `.workbench/locks/`. This is not a complete SBOM. Model weights, credentials, and remote services are not bundled or licensed by this project. Check dependency changes and provider/content terms before redistribution or querying private sources.

`skills/research-paperqa/SKILL.md`, `docs/PAPERQA.md` and the synthetic ingestion/evidence checks are this project's original MIT-licensed integration. API/CLI behavior is informed by the pinned PaperQA source. The generated PDF fixture is wholly synthetic, not a scientific result or copied paper. Local smoke checks establish parsing and evidence serialization only; real retrieval/model answer quality and host discovery are unverified.

## Development-only CI dependencies

GitHub Actions downloads the following actions for `.github/workflows/ci.yml`. They are not bundled in the research workspace or used by the installer. Both are maintained by GitHub / the `actions` project and contributors, and retain their own MIT licenses. Action source is used without local modifications.

| Component | Fixed revision | Scope and license |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout) | `3d3c42e5aac5ba805825da76410c181273ba90b1` (`v7.0.1`) | CI source checkout, credentials not persisted. [Pinned MIT license](https://github.com/actions/checkout/blob/3d3c42e5aac5ba805825da76410c181273ba90b1/LICENSE). |
| [actions/setup-python](https://github.com/actions/setup-python) | `5fda3b95a4ea91299a34e894583c3862153e4b97` (`v7.0.0`) | CI Python runtime selection. [Pinned MIT license](https://github.com/actions/setup-python/blob/5fda3b95a4ea91299a34e894583c3862153e4b97/LICENSE). Managed Python distributions retain their own terms. |

## Workflow and communication inspirations

| Creator / source | Contribution and review boundary |
| --- | --- |
| 艺雨YiLight, [《同济博一｜我的Codex论文辅助全流程》](https://www.bilibili.com/video/BV1cV3b67Ehs/) | Workflow inspiration: connect discovery, Zotero, an AI agent, research questions, reading, writing, analysis and follow-up. Original page metadata/description were checked; complete original subtitles were not obtained. No video or screenshot is republished here. |
| sunweihunu, [third-party transcript](https://github.com/sunweihunu/claude-research-skill-market/blob/main/transcript/BV1cV3b67Ehs_transcript.md) | Intermediary used to review the video's full sequence and candidate tools. Credit for transcript compilation is distinct from video authorship. It is a secondary source, not a verified verbatim original. We link it; we do not bundle its transcript or skill collection. |
| ASD / Simplified Technical English Maintenance Group, [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), [FAQ](https://www.asd-ste100.org/STE_faq.html) | Clear language, consistent terminology and explicit instructions informed our multilingual adaptation. The standard/dictionary is not bundled. No certification or strict compliance is claimed. |
| Andrej Karpathy, [post](https://x.com/karpathy/status/2105819303471976479), [mirror used for review](https://x.twstalker.com/karpathy/status/2105819303471976479) | Suggestions to consider diagrams, interactive pages and video when useful. The original X text was not directly readable during review. No exact quotation or claim that Karpathy designed this workbench is made. |
| OpenAI, [skills concepts](https://developers.openai.com/plugins/concepts/skills), [skill building](https://developers.openai.com/plugins/build/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Technical references for skill structure, discovery and persistent instructions. The documentation, software and models are not relicensed here; compatibility does not imply endorsement. |

The foundation-first installer, question grouping, catalog integration, verification and multilingual adaptation are this project's implementation. Do not present them as the video author's code or an official release by a credited organization.

## Research example, API, and existing applications

- **Paper:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. *Attention Is All You Need* (2017), [arXiv:1706.03762](https://arxiv.org/abs/1706.03762), [DOI](https://doi.org/10.48550/arXiv.1706.03762). `examples/attention-abstract.md` is our short paraphrase of its abstract. `examples/attention-scaling.md` checks a selected passage in v7 section 3.2.1 and footnote 4; its evidence table is original, and `examples/attention_scaling.py` is our standard-library synthetic numerical illustration. The v7 HTML and selected PDF page were checked on 2026-10-03; PDF formula extraction was fragmented, so the equation was checked against HTML. This is not reproduced training data, a model answer, or a full-paper review. Credit for the scientific work belongs to these authors. No PDF, figure, table or full abstract is reproduced. Paper rights remain separate from our MIT license.
- **Crossref:** `scripts/research_tools.py` calls the [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/). Crossref and its depositing members supply bibliographic data. Our request/parser code is our integration; returned research content is not our authorship. Preserve record-level provenance and check content-specific terms before redistribution. Metadata access does not grant full-text rights.
- **Existing applications:** [Zotero](https://www.zotero.org/) by the Corporation for Digital Scholarship and contributors, [Obsidian](https://obsidian.md/), [MATLAB](https://www.mathworks.com/products/matlab.html) by MathWorks, [GNU Octave](https://octave.org/), [R](https://www.r-project.org/), [Codex](https://developers.openai.com/codex/) by OpenAI, and [GitHub](https://github.com/) are named for interoperability or user choice. They are not bundled or automatically licensed to the user. Accounts, connectors and institutional access require their own review.

## Maintaining this inventory

For each new component, record the original creator, source, version, use location, bundled/downloaded/reference-only status, license, retained notices and local changes. Follow [CONTRIBUTING.md](CONTRIBUTING.md). Keep credit next to copied/adapted material where appropriate as well as here. New versions and platforms require checking their actual distributions.
