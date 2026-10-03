"""Exercise the actual launcher and copied engine in a disposable workspace."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'registry.json').read_text(encoding='utf-8'))['version']


def command(args, expected=0, extra_env=None):
    env = dict(os.environ)
    env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + env.get('PATH', '')
    env['PYTHONIOENCODING'] = 'utf-8'
    env.update(extra_env or {})
    result = subprocess.run(args, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=900)
    if result.returncode != expected:
        raise RuntimeError(f'Expected exit {expected}, got {result.returncode}:\n{result.stdout}\n{result.stderr}')
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--online', action='store_true', help='Download actual core and figures dependencies')
    parser.add_argument('--paperqa', action='store_true', help='Also install and check PaperQA locally; requires --online, makes no model calls')
    parser.add_argument('--powershell', choices=('powershell', 'pwsh'), help='Choose an existing Windows shell; its normal execution policy applies')
    args = parser.parse_args()
    if args.paperqa and not args.online:
        parser.error('--paperqa requires --online')
    # Extended paths also let the disposable Windows fixture clean up the
    # deeply nested package files when system long-path support is disabled.
    temporary_parent = ('\\\\?\\' + tempfile.gettempdir()) if os.name == 'nt' and args.paperqa else None
    with tempfile.TemporaryDirectory(prefix='workbench-check-', dir=temporary_parent) as temporary:
        # Pass an ordinary project path to the installer while the fixture's
        # cleanup retains the extended prefix.
        root = Path(temporary.removeprefix('\\\\?\\')) / 'research spaces \u7814\u7a76'
        root.mkdir()
        agents = b'Human instructions: preserve experiments.\n'
        notes = b'Human notes: keep these measurements.\n'
        (root / 'AGENTS.md').write_bytes(agents)
        (root / 'workbench-config.md').write_bytes(notes)
        shell = args.powershell or ('pwsh' if shutil.which('pwsh') else 'powershell')
        launcher = ([shell, '-NoProfile', '-File', str(ROOT / 'install.ps1')]
                    if os.name == 'nt' else ['bash', str(ROOT / 'install.sh')])
        command(launcher + ['--workspace', str(root)] + ([] if args.online else ['--offline']), expected=0 if args.online else 2)
        before = (root / 'AGENTS.md').read_bytes()
        assert before.startswith(agents), 'Human instructions changed'
        assert (root / 'workbench-config.md').read_bytes() == notes, 'Human notes changed'
        engine = root / '.workbench/kit' / VERSION / 'workbench.py'
        python = root / '.workbench/envs/core' / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        interpreter = str(python) if args.online else sys.executable
        command([interpreter, str(engine), 'setup', '--workspace', str(root)] + ([] if args.online else ['--offline']), expected=0 if args.online else 2)
        assert (root / 'AGENTS.md').read_bytes() == before, 'Resume duplicated or replaced instructions'
        assert (root / 'workbench-config.md').read_bytes() == notes, 'Resume changed notes'
        command([interpreter, str(engine), 'plan'])
        if args.online:
            command([interpreter, str(engine), 'doctor', '--workspace', str(root)])
            profile = root / '.workbench/selected.json'
            selected = ['figures', 'paperqa'] if args.paperqa else ['figures']
            profile.write_text(json.dumps({'extensions': selected}), encoding='utf-8-sig')
            command([interpreter, str(engine), 'apply', '--workspace', str(root), '--profile', str(profile)])
            command([interpreter, str(engine), 'apply', '--workspace', str(root), '--profile', str(profile)])
            command([interpreter, str(engine), 'doctor', '--workspace', str(root)])
            state = json.loads((root / '.workbench/state.json').read_text(encoding='utf-8'))
            assert state['checks']['runtime:core']['status'] == 'verified'
            assert state['checks']['runtime:figures']['status'] == 'verified'
            if args.paperqa:
                assert state['checks']['runtime:paperqa']['status'] == 'verified'
                assert 'research-paperqa' in state['skills']
                assert state['profiles']['paperqa']['status'] == 'installed; task checks pending'
                assert (root / 'AGENTS.md').read_bytes() == before
                assert (root / 'workbench-config.md').read_bytes() == notes
                pqa = root / '.workbench/envs/paperqa' / ('Scripts/pqa.exe' if os.name == 'nt' else 'bin/pqa')
                command([str(pqa), '--help'], extra_env={'PQA_HOME': str(root / '.workbench'), 'LITELLM_LOCAL_MODEL_COST_MAP': 'True'})
                print('Passed: PaperQA installation/resume, actual CLI, local PDF/evidence checks; model answering pending.')
            assert 'nature-figure' not in state['skills'], 'Withheld skill was installed'
            print('Passed: actual PDF and figures runtimes, copied-engine setup/doctor/apply, and resume.')
        else:
            state = json.loads((root / '.workbench/state.json').read_text(encoding='utf-8'))
            assert state['checks']['runtime:core']['status'] == 'pending'
            assert not (root / '.workbench/envs').exists(), 'Offline run created a runtime'
            print('Passed: actual offline launcher, copied-engine setup/plan, Unicode path, and preservation.')


if __name__ == '__main__':
    main()
