"""Check real previous kits, offline upgrades, installed links, and preservation."""
import contextlib
import importlib.util
import io
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINES = ('b0c579325163833ec0571c319986b51785446329',
             '7df78332739f432b1b4d7eae79ef9a1f311ecadb',
             'dfc7cb9c0c724f9fee7cab5728943d44d4d65448',
             'bfcba49db8aa5c420b2fe0d54fcacc540a6a4a86',
             'b5460c78da16965f54aa37f16161674d8c4a5ef4')


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def snapshot(ref, destination):
    archive = subprocess.check_output(['git', 'archive', ref], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tree:
        for member in tree.getmembers():
            if not member.isfile():
                continue
            path = destination / member.name
            if not path.resolve().is_relative_to(destination.resolve()):
                raise RuntimeError('Snapshot path leaves the temporary source')
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(tree.extractfile(member).read())


def main():
    with tempfile.TemporaryDirectory(prefix='workbench-release-') as temporary:
        temporary = Path(temporary)
        candidate = temporary / 'candidate'
        candidate.mkdir()
        names = subprocess.check_output(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=ROOT).decode('utf-8').split('\0')
        for name in set(names) - {''}:
            path = candidate / name
            path.parent.mkdir(parents=True, exist_ok=True)
            data = (ROOT / name).read_bytes()
            # Match the canonical release's text endings, not an older checkout.
            if b'\0' not in data:
                data = data.replace(b'\r\n', b'\n')
            path.write_bytes(data)
        new = load(candidate / 'workbench.py', 'candidate_workbench')
        for index, ref in enumerate(BASELINES):
            baseline = temporary / ('baseline-' + str(index))
            baseline.mkdir()
            snapshot(ref, baseline)
            old = load(baseline / 'workbench.py', 'old_workbench_' + str(index))
            workspace = temporary / ('workspace spaces \u7814\u7a76-' + str(index))
            with contextlib.redirect_stdout(io.StringIO()):
                assert old.main(['setup', '--workspace', str(workspace), '--offline']) == 2
            old_kit = workspace / '.workbench/kit' / old.VERSION
            kit_before = {p.relative_to(old_kit): p.read_bytes() for p in old_kit.rglob('*') if p.is_file()}
            skill_before = {name: {p.relative_to(workspace / '.agents/skills' / name): p.read_bytes()
                                   for p in (workspace / '.agents/skills' / name).rglob('*') if p.is_file()}
                            for name in new.FOUNDATION_SKILLS}
            agents_before = (workspace / 'AGENTS.md').read_bytes()
            config = workspace / 'workbench-config.md'
            config.write_text('Human research context.\n', encoding='utf-8')
            note = workspace / 'wiki/notes.md'
            note.write_text('Human source-linked note.\n', encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()):
                assert new.main(['setup', '--workspace', str(workspace), '--offline']) == 2
                backups_before_resume = sorted((workspace / '.workbench/backups/skills').glob('*'))
                assert new.main(['setup', '--workspace', str(workspace), '--offline']) == 2
            assert sorted((workspace / '.workbench/backups/skills').glob('*')) == backups_before_resume
            assert all((old_kit / path).read_bytes() == data for path, data in kit_before.items())
            state = new.read_state(workspace)
            for name, previous in skill_before.items():
                target = workspace / '.agents/skills' / name
                expected = new.tree_hashes(candidate / 'skills' / name)
                assert new.tree_hashes(target) == expected == state['skills'][name]['files']
                assert state['skills'][name]['source']['version'] == new.VERSION
                if {path.as_posix(): new.digest(data) for path, data in previous.items()} != expected:
                    backups = list((workspace / '.workbench/backups/skills').glob(name + '-' + old.VERSION + '-*'))
                    assert len(backups) == 1
                    assert all((backups[0] / path).read_bytes() == data for path, data in previous.items())
            assert (workspace / 'AGENTS.md').read_bytes() == agents_before
            assert config.read_text(encoding='utf-8') == 'Human research context.\n'
            assert note.read_text(encoding='utf-8') == 'Human source-linked note.\n'
            kit = workspace / '.workbench/kit' / new.VERSION
            assert (kit / 'README.zh-CN.md').read_bytes() == (candidate / 'README.zh-CN.md').read_bytes()
            assert '.workbench/kit/' + new.VERSION + '/' in (workspace / 'START_HERE.md').read_text(encoding='utf-8')
            subprocess.run([sys.executable, str(kit / 'scripts/check_repository.py')], check=True, capture_output=True)
            assert (kit / 'scripts/research_tools.py').is_file()
            if sys.version_info[:2] < (3, 12):
                try:
                    with contextlib.redirect_stdout(io.StringIO()):
                        new.runtime(workspace, new.read_state(workspace), 'figures', new.REGISTRY['profiles']['figures']['requirements'])
                except new.SetupError as exc:
                    assert 'Python 3.12+' in str(exc)
                else:
                    raise AssertionError('Python 3.11 was not rejected before creating the figures environment')
                assert not (workspace / '.workbench/envs/figures').exists()
            edited_workspace = temporary / ('edited-workspace-' + str(index))
            with contextlib.redirect_stdout(io.StringIO()):
                assert old.main(['setup', '--workspace', str(edited_workspace), '--offline']) == 2
            edited_skill = edited_workspace / '.agents/skills/research-reading/SKILL.md'
            edited_skill.write_text('Human research-reading changes.\n', encoding='utf-8')
            previous_record = old.read_state(edited_workspace)['skills']['research-reading']
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    new.main(['setup', '--workspace', str(edited_workspace), '--offline'])
                except new.SetupError:
                    pass
                else:
                    raise AssertionError('Edited foundation skill was replaced or silently accepted')
            assert edited_skill.read_text(encoding='utf-8') == 'Human research-reading changes.\n'
            assert new.read_state(edited_workspace)['skills']['research-reading'] == previous_record
            assert not (edited_workspace / '.workbench/install.lock').exists()
            print('Passed: ' + ref[:7] + ' -> ' + new.VERSION + ' offline upgrade/resume, owned-skill backups, edited-skill refusal, retained kits/human files, installed bilingual links.')


if __name__ == '__main__':
    main()
