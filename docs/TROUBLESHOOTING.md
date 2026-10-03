# Troubleshooting and recovery

Read `.workbench/install-report.md` and `workbench-config.md` in the target project first. Address the failed component. Preserve successful work and human edits.

| Symptom | Meaning and next action |
| --- | --- |
| Cannot download the repository | This repository is public. Check the URL, connection, or proxy, then retry Code → Download ZIP. No collaborator invitation is needed. |
| Launcher cannot find Python | Online launchers can obtain a local Python through Astral uv. On macOS/Linux this requires Bash, curl, and a SHA-256 utility. Offline use requires Python 3.11+ already installed. |
| PowerShell blocks the script | Follow the computer's normal software policy. Ask the administrator for an approved method, or have an authorized agent use an already installed Python to run `workbench.py setup`. The launcher does not bypass policy. |
| Offline setup exits with code 2 | Files were prepared but dependencies are pending. Rerun the same setup online. |
| Certificate or network error | Check connectivity, proxy configuration, and trusted CA certificates. Python HTTPS failures can use curl's OS trust when available. Never disable certificate checks. |
| Checksum mismatch | No mismatched download is installed. Retry once; if it persists, verify the upstream release and catalog with the maintainer. Do not remove the hash check. |
| No compatible package wheel | The operating system, architecture, or Python version may not be supported by a pinned package. Use a compatible environment or review a version update. The installer does not silently build arbitrary native source packages. |
| A profile failed | Inspect its report. Rerun `apply` with the same local profile after resolving the cause. Other completed profiles remain available. |
| Installation lock exists | A run is active or was forcibly interrupted. Confirm the recorded process is no longer installing, then remove only the stale `.workbench/install.lock` with the user's applicable authorization and retry. |
| Same-name skill differs | The installer preserves it. Review and back up local changes before explicitly choosing an upgrade; do not delete the entire skill folder automatically. |
| Installed engine differs | A same-version engine was changed locally. Preserve it and use a reviewed new release or a separate workspace. No silent overwrite occurs. |
| State file is unreadable | Preserve `.workbench/state.json` for recovery. Restore a known-good copy or inspect existing outputs before rebuilding the record; do not assume nothing was installed. |
| Unrecognized runtime is preserved | There is no matching ownership record. A working runtime can be checked and reused; repairs require reviewing and backing it up before replacement, or choosing a new workspace. Do not manufacture a marker or treat an old check as ownership. |
| apply reports failed current foundation checks | Inspect the new core/skill results, rerun setup for the affected foundation, and then retry apply. Old verified records do not bypass missing files or a broken interpreter. |
| START_HERE.md still refers to an old engine | If the file was edited, setup preserves it and writes versioned instructions. Read the entry-point row in the report and reconcile the new file with your notes. |
| Managed destination is a junction or link | It is preserved and refused to prevent writes to another location. Select a dedicated directory or reconcile the existing link before setup. |
| Skill files exist but are not visible | Check the actual host's discovery path and disabled state. Reload or start a new session if needed, then invoke the skill. File integrity alone does not prove discovery. |
| Runtime exists but a task cannot import a package | Use the profile's interpreter from `.workbench/envs/`. Install additional task-specific dependencies only when needed and record them. |
| Workspace was moved or base Python removed | Virtual environments depend on their original path and base interpreter. Preserve research files, then rebuild the affected environment under a reviewed plan. |
| AI only gives advice | Local setup requires file and execution tools. Give the installation materials to an authorized local agent and keep installation marked pending. |
| Library unavailable after browser login | A browser, connector, and local tool may use different accounts. Check the actual connection's account and scope. |
| Only an abstract is available | Mark the source scope. Do not invent full-text methods, equations, or figures. |
| Explanations remain difficult | Check whether rules loaded and identify the missing concept. Explain it with a concrete example or diagram. |

## Check and resume

From the original distribution, use a suitable Python:

```bash
python workbench.py setup --workspace "/path/to/project"
python workbench.py apply --workspace "/path/to/project" --profile "/path/to/profile.json"
python workbench.py doctor --workspace "/path/to/project"
```

Run only the command needed for the current failure. If the distribution was removed, use the copied engine and installed interpreter listed in `START_HERE.md`. `doctor` rechecks files and supported runtimes without downloads. It does not repair missing components or prove the user's task passed. Exit 0 means the command's supported checks passed; exit 2 means checks remain incomplete or failed; exit 1 means setup stopped with an error.

## Update or remove

Record the old version, location, and local modifications. Back up affected files privately. Recheck affected skills and tasks after an update. This release preserves conflicting files and does not offer an automatic cross-version upgrade or universal uninstall command.

Identify what the workbench added and what is pre-existing or shared. Follow the user's authorization for deletion. Preserve research sources, notes, results, and shared applications. Restore the recorded configuration if a reviewed update fails.
