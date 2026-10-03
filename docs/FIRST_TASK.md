# Complete your first research task

Start in the installed workspace. Read `.workbench/install-report.md`; repair failed foundation steps before using its Python tools. Installed files and small runtime checks do not yet prove that your research workflow works.

## Choose one output

Use START_HERE.md as the project entry point, then give the agent one request:

| Task | Copyable request | Expected output |
| --- | --- | --- |
| Start reading | Read one selected abstract, explain its question and approach, and mark full-text gaps. Save a source-linked note. | One note under `wiki/` or your existing system |
| Check a claim | Check one selected full-text claim against its passage or equation. Retain assumptions, run a small calculation when useful, and label unsupported conclusions. | A claim-to-evidence table and actual check output; see [worked example](../examples/attention-scaling.md) |
| Compare papers | Use research-paperqa on my selected papers within my existing model/data/cost authorization. Save evidence, check central citations, and record unanswered questions. | A comparison note and local session/evidence; [configuration and acceptance](PAPERQA.md) |

Record file installation, host invocation, real task execution, and claim support separately in workbench-config.md. A model answer is an input to verification.

## Read one public abstract

Open the workspace in your existing agent and send:

> Read START_HERE.md and the installation report. Use my preferred language. Read the public arXiv abstract at https://arxiv.org/abs/1706.03762, check its title and authors, and save wiki/attention-first-pass.md. Explain the research problem and main approach, link the source, mark the scope as abstract only, and list what requires reading the full paper. Reuse existing tools. Do not add specialist extensions for this task unless an actual gap requires them.

Expected output: a Markdown note at `wiki/attention-first-pass.md`, containing a source link, the source scope, a short explanation, and unanswered questions. Compare its structure with the [existing example](../examples/attention-abstract.md).

Reopen the saved note. Check that it does not claim to have read methods, equations, figures, or results that were absent from the abstract. Ask your agent to explain one unfamiliar concept and revise the same note. Record the output location, tools used, and remaining gaps in `workbench-config.md`.

This is a suggested acceptance task. It is not a new independent user trial or a full-text review.

## Read selected pages from your own PDF

The foundation's helper can extract text with page numbers. It does not perform OCR. From the workspace, replace `paper.pdf` with the actual local file:

**macOS / Linux**

```bash
KIT=$(.workbench/envs/core/bin/python -c 'import json; print(".workbench/kit/" + json.load(open(".workbench/state.json", encoding="utf-8-sig"))["version"])')
.workbench/envs/core/bin/python "$KIT/scripts/research_tools.py" pdf paper.pdf --start 1 --end 2
```

**Windows PowerShell**

```powershell
$kitVersion = (Get-Content -LiteralPath .\.workbench\state.json -Raw | ConvertFrom-Json).version
$kit = Join-Path .\.workbench\kit $kitVersion
& .\.workbench\envs\core\Scripts\python.exe (Join-Path $kit 'scripts/research_tools.py') pdf .\paper.pdf --start 1 --end 2
```

Give the numbered excerpt to your agent, ask it to save a source-linked note, then compare the note with the original pages. Inspect equations, tables, and diagrams visually. If a page has no extractable text, retain that limitation and use an authorized OCR route when needed.

After this task works, use `START_HERE.md` to personalize the workbench around your actual next output.
