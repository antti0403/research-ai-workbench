"""Regression checks for workspace preservation, recovery, and user-edited JSON."""
import contextlib
import copy
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_workbench import w


class ReliabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'workspace spaces \u7814\u7a76'
        self.root.mkdir()
        self.state = w.read_state(self.root)
        w.save_state(self.root, self.state)
        self.quiet = contextlib.redirect_stdout(io.StringIO())
        self.quiet.__enter__()

    def tearDown(self):
        self.quiet.__exit__(None, None, None)
        self.temp.cleanup()

    def fake_python(self, profile='core'):
        python = w.environment_python(self.root, profile)
        python.parent.mkdir(parents=True, exist_ok=True)
        python.write_bytes(b'Synthetic interpreter; tests never execute it')
        return python

    def mark_owned(self, profile='core'):
        token = 'a' * 32
        self.state['runtimes'][profile] = {'token': token}
        marker = w.safe_path(self.root, '.workbench/envs/' + profile + '/.workbench-owner.json')
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(json.dumps({'schema': 1, 'profile': profile, 'token': token}), encoding='utf-8')
        return marker

    def core_skills(self):
        for name in ('research-workbench', 'research-reading'):
            w.install_directory(self.root, self.state, name, {'SKILL.md': b'Synthetic skill'}, {'source': 'test'})

    def test_unowned_existing_python_is_never_repaired(self):
        self.fake_python()
        with patch.object(w, 'run', side_effect=w.SetupError('missing package')) as run:
            with self.assertRaisesRegex(w.SetupError, 'no packages changed'):
                w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        self.assertEqual(run.call_count, 1)
        self.assertFalse(any('install' in call.args[0] for call in run.call_args_list))
        self.assertEqual(self.state['checks']['runtime:core']['status'], 'failed')
        self.assertFalse(self.state['runtimes'])

    def test_old_diagnostic_record_does_not_grant_runtime_ownership(self):
        (self.root / '.workbench/envs/core').mkdir(parents=True)
        self.state['checks']['runtime:core'] = {'status': 'failed'}
        with patch.object(w.venv, 'EnvBuilder') as builder:
            with self.assertRaisesRegex(w.SetupError, 'unrecognized'):
                w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        builder.assert_not_called()

    def test_legacy_working_runtime_is_verified_without_adoption(self):
        self.fake_python()
        with patch.object(w, 'run', return_value='pypdf==6.19.0') as run:
            w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        self.assertEqual(self.state['checks']['runtime:core']['status'], 'verified')
        self.assertFalse(self.state['runtimes'])
        self.assertFalse(any('install' in call.args[0] or 'ensurepip' in call.args[0] for call in run.call_args_list))

    def test_mismatched_marker_does_not_grant_ownership(self):
        self.fake_python()
        marker = self.mark_owned()
        marker.write_text('{}', encoding='utf-8')
        with patch.object(w, 'run', side_effect=w.SetupError('check failed')) as run:
            with self.assertRaisesRegex(w.SetupError, 'no packages changed'):
                w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        self.assertEqual(run.call_count, 1)
        self.assertEqual(marker.read_text(), '{}')

    def test_new_runtime_can_repair_and_resume_only_its_own_environment(self):
        calls = []
        def create(envdir):
            self.fake_python()
        def run(command, **kwargs):
            calls.append(command)
            if len(calls) == 1:
                raise w.SetupError('packages not installed yet')
            return 'pypdf==6.19.0'
        with patch.object(w.venv, 'EnvBuilder') as builder, patch.object(w, 'run', side_effect=run):
            builder.return_value.create.side_effect = create
            w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        self.assertTrue(w.owns_runtime(self.root, w.read_state(self.root), 'core'))
        self.assertTrue(any('install' in command for command in calls))
        token = self.state['runtimes']['core']['token']
        with patch.object(w.venv, 'EnvBuilder') as builder, patch.object(w, 'run', return_value='pypdf==6.19.0') as run:
            w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        builder.assert_not_called()
        self.assertFalse(any('install' in call.args[0] for call in run.call_args_list))
        self.fake_python().unlink()
        with patch.object(w.venv, 'EnvBuilder') as builder, patch.object(w, 'run', return_value='pypdf==6.19.0'):
            builder.return_value.create.side_effect = create
            w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        builder.return_value.create.assert_called_once()
        self.assertEqual(self.state['runtimes']['core']['token'], token)

    def test_creation_failure_is_recorded_and_owned_partial_runtime_can_retry(self):
        with patch.object(w.venv, 'EnvBuilder') as builder:
            builder.return_value.create.side_effect = OSError('synthetic creation error')
            with self.assertRaises(w.SetupError):
                w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        self.assertEqual(w.read_state(self.root)['checks']['runtime:core']['status'], 'failed')
        self.assertTrue(w.owns_runtime(self.root, self.state, 'core'))
        with patch.object(w.venv, 'EnvBuilder') as builder, patch.object(w, 'run', return_value='pypdf==6.19.0'):
            builder.return_value.create.side_effect = lambda envdir: self.fake_python()
            w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'])
        self.assertEqual(self.state['checks']['runtime:core']['status'], 'verified')

    def test_offline_runtime_does_not_create_environment_or_download(self):
        with patch.object(w.venv, 'EnvBuilder') as builder, patch.object(w, 'run') as run:
            w.runtime(self.root, self.state, 'core', w.REGISTRY['core_requirements'], offline=True)
        builder.assert_not_called()
        run.assert_not_called()
        self.assertFalse((self.root / '.workbench/envs').exists())
        self.assertEqual(self.state['checks']['runtime:core']['status'], 'pending')

    def test_apply_blocks_stale_verified_record_with_missing_interpreter(self):
        self.core_skills()
        self.state['checks']['runtime:core'] = {'status': 'verified'}
        w.save_state(self.root, self.state)
        profile = self.root / 'selection.json'
        profile.write_text('{"extensions":["figures"]}', encoding='utf-8')
        with patch.object(w, 'apply_profile') as apply:
            with self.assertRaisesRegex(w.SetupError, 'current checks'):
                w.main(['apply', '--workspace', str(self.root), '--profile', str(profile)])
        apply.assert_not_called()
        self.assertFalse((self.root / '.workbench/profile.json').exists())
        self.assertEqual(w.read_state(self.root)['checks']['runtime:core']['status'], 'failed')

    def test_apply_rechecks_current_runtime_even_with_verified_history(self):
        self.core_skills()
        self.fake_python()
        self.state['checks']['runtime:core'] = {'status': 'verified'}
        w.save_state(self.root, self.state)
        profile = self.root / 'selection.json'
        profile.write_text('{"extensions":[]}', encoding='utf-8')
        with patch.object(w, 'run', side_effect=w.SetupError('current check failed')), patch.object(w, 'apply_profile') as apply:
            with self.assertRaises(w.SetupError):
                w.main(['apply', '--workspace', str(self.root), '--profile', str(profile)])
        apply.assert_not_called()

    def test_apply_refuses_modified_foundation_skill_before_extensions(self):
        self.core_skills()
        self.fake_python()
        (self.root / '.agents/skills/research-reading/SKILL.md').write_text('Human change', encoding='utf-8')
        w.save_state(self.root, self.state)
        profile = self.root / 'selection.json'
        profile.write_text('{"extensions":[]}', encoding='utf-8')
        with patch.object(w, 'run', return_value='passed'), patch.object(w, 'apply_profile') as apply:
            with self.assertRaises(w.SetupError):
                w.main(['apply', '--workspace', str(self.root), '--profile', str(profile)])
        apply.assert_not_called()
        self.assertEqual((self.root / '.agents/skills/research-reading/SKILL.md').read_text(), 'Human change')

    def test_apply_fresh_checks_allow_retry_after_an_unrelated_profile_failure(self):
        self.core_skills()
        self.fake_python()
        self.state['profiles']['symbolic'] = {'status': 'failed'}
        w.save_state(self.root, self.state)
        profile = self.root / 'selection.json'
        profile.write_text('{"extensions":[]}', encoding='utf-8')
        with patch.object(w, 'run', return_value='passed'), patch.object(w, 'apply_profile', return_value=True) as apply:
            self.assertEqual(w.main(['apply', '--workspace', str(self.root), '--profile', str(profile)]), 0)
        apply.assert_called_once()

    def test_executed_skill_bytecode_does_not_break_doctor_or_resume(self):
        files = {'SKILL.md': b'Synthetic skill',
                 'scripts/helper.py': b'VALUE = 1\n',
                 'scripts/main.py': b'import helper\nprint(helper.VALUE)\n'}
        self.core_skills()
        w.install_directory(self.root, self.state, 'example', files, {'source': 'test'})
        directory = self.root / '.agents/skills/example'
        env = dict(os.environ)
        env.pop('PYTHONDONTWRITEBYTECODE', None)
        env.pop('PYTHONPYCACHEPREFIX', None)
        subprocess.run([sys.executable, str(directory / 'scripts/main.py')], check=True, capture_output=True, env=env)
        self.assertTrue(list(directory.rglob('*.pyc')))
        self.assertEqual(w.tree_hashes(directory), self.state['skills']['example']['files'])
        w.install_directory(self.root, self.state, 'example', files, {'source': 'test'})
        with patch.object(w, 'check_runtime', return_value='passed'):
            self.assertTrue(w.doctor(self.root, self.state))
        (directory / 'scripts/helper.py').write_text('VALUE = 2', encoding='utf-8')
        with self.assertRaises(w.SetupError):
            w.install_directory(self.root, self.state, 'example', files, {'source': 'test'})

    def test_extra_executable_is_not_hidden_as_bytecode(self):
        w.install_directory(self.root, self.state, 'example', {'SKILL.md': b'Example'}, {})
        extra = self.root / '.agents/skills/example/__pycache__/unexpected.py'
        extra.parent.mkdir()
        extra.write_text('print("unexpected")', encoding='utf-8')
        with self.assertRaises(w.SetupError):
            w.install_directory(self.root, self.state, 'example', {'SKILL.md': b'Example'}, {})
        self.assertTrue(extra.exists())

    def test_skill_hashes_use_one_canonical_root_for_relative_inputs(self):
        files = {'SKILL.md': b'Example', 'references/note.md': b'Evidence'}
        w.install_directory(self.root, self.state, 'example', files, {})
        original = Path.cwd()
        try:
            os.chdir(self.root)
            self.assertEqual(w.tree_hashes(Path('.agents/skills/example')), self.state['skills']['example']['files'])
        finally:
            os.chdir(original)

    def test_bom_profile_and_state_are_accepted(self):
        profile = self.root / 'bom.json'
        profile.write_text('{"extensions":[]}', encoding='utf-8-sig')
        self.assertEqual(w.load_profile(profile)['extensions'], [])
        path = self.root / '.workbench/state.json'
        path.write_text(json.dumps(self.state), encoding='utf-8-sig')
        self.assertEqual(w.read_state(self.root)['version'], w.VERSION)

    def test_malformed_state_shapes_raise_controlled_errors_and_preserve_bytes(self):
        bad = [[], None, 42, 'text', {}, {'schema': 1}]
        for section in ('checks', 'skills', 'profiles', 'runtimes', 'owned'):
            state = copy.deepcopy(self.state)
            state[section] = []
            bad.append(state)
        for section, value in [('checks', {'x': None}), ('checks', {'x': {'status': 2}}),
                               ('skills', {'example': {'files': []}}),
                               ('skills', {'example': {'files': {'../outside': 'a' * 64}}}),
                               ('skills', {'example': {'files': {'SKILL.md': None}}}),
                               ('profiles', {'symbolic': None}), ('profiles', {'unknown': {'status': 'failed'}}),
                               ('runtimes', {'core': {'token': 'wrong'}}),
                               ('owned', {'START_HERE.md': 'wrong'})]:
            state = copy.deepcopy(self.state)
            state[section] = value
            bad.append(state)
        path = self.root / '.workbench/state.json'
        for state in bad:
            with self.subTest(state=state):
                original = json.dumps(state).encode()
                path.write_bytes(original)
                with self.assertRaises(w.SetupError):
                    w.read_state(self.root)
                self.assertEqual(path.read_bytes(), original)

    def test_old_schema_one_state_adds_empty_ownership_without_claiming_environments(self):
        del self.state['runtimes']
        self.state['version'] = '0.2.1'
        path = self.root / '.workbench/state.json'
        path.write_text(json.dumps(self.state), encoding='utf-8')
        before = path.read_bytes()
        self.assertEqual(w.read_state(self.root)['runtimes'], {})
        self.assertEqual(path.read_bytes(), before)

    def test_owned_entry_point_updates_with_backup_but_human_edits_are_preserved(self):
        w.create_once(self.root, self.state, 'START_HERE.md', 'Old engine')
        self.assertEqual(w.update_owned_file(self.root, self.state, 'START_HERE.md', 'New engine'), 'updated owned file')
        self.assertTrue(list((self.root / '.workbench/backups').glob('START_HERE-*.md')))
        path = self.root / 'START_HERE.md'
        path.write_text('Human edit', encoding='utf-8')
        self.assertEqual(w.update_owned_file(self.root, self.state, 'START_HERE.md', 'Next engine'), 'preserved existing file')
        self.assertEqual(path.read_text(), 'Human edit')

    def test_setup_updates_a_legacy_owned_entry_point_and_keeps_its_backup(self):
        old = '.workbench/kit/0.2.1/workbench.py\n'
        w.create_once(self.root, self.state, 'START_HERE.md', old)
        self.assertEqual(w.main(['setup', '--workspace', str(self.root), '--offline']), 2)
        self.assertIn('.workbench/kit/' + w.VERSION, (self.root / 'START_HERE.md').read_text())
        backups = list((self.root / '.workbench/backups').glob('START_HERE-*.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), old)

    def test_setup_preserves_an_edited_entry_point_and_writes_current_instructions(self):
        (self.root / 'START_HERE.md').write_text('Human entry point', encoding='utf-8')
        self.assertEqual(w.main(['setup', '--workspace', str(self.root), '--offline']), 2)
        self.assertEqual((self.root / 'START_HERE.md').read_text(), 'Human entry point')
        alternative = self.root / ('START_HERE-' + w.VERSION + '.md')
        self.assertIn('.workbench/kit/' + w.VERSION, alternative.read_text())
        self.assertEqual(w.read_state(self.root)['checks']['entry-point']['status'], 'needs review')

    def test_subprocess_decoding_preserves_unicode_and_does_not_write_bytecode(self):
        command = [sys.executable, '-c', 'print("\\u7814\\u7a76")']
        self.assertEqual(w.run(command), '\u7814\u7a76')
        with patch.object(w.subprocess, 'run') as run:
            run.return_value.returncode = 0
            run.return_value.stdout = 'okay'
            w.run(['synthetic'])
        self.assertEqual(run.call_args.kwargs['env']['PYTHONDONTWRITEBYTECODE'], '1')

    @unittest.skipUnless(os.name == 'nt', 'Windows junctions only')
    def test_junctions_in_workspace_and_skill_are_preserved_and_refused(self):
        powershell = shutil.which('powershell')
        if not powershell:
            self.skipTest('Windows PowerShell unavailable')
        outside = Path(self.temp.name) / 'outside'
        outside.mkdir()
        marker = outside / 'human.txt'
        marker.write_text('Human content', encoding='utf-8')
        for relative in ('.agents', '.workbench/cache', '.workbench/envs/core/Scripts', 'skill/references'):
            with self.subTest(relative=relative):
                link = self.root / relative
                link.parent.mkdir(parents=True, exist_ok=True)
                env = dict(os.environ, WORKBENCH_TEST_LINK=str(link), WORKBENCH_TEST_TARGET=str(outside))
                command = "$ErrorActionPreference='Stop'; New-Item -ItemType Junction -Path $env:WORKBENCH_TEST_LINK -Target $env:WORKBENCH_TEST_TARGET | Out-Null"
                result = subprocess.run([powershell, '-NoProfile', '-Command', command], capture_output=True, env=env)
                self.assertEqual(result.returncode, 0, result.stderr)
                try:
                    with self.assertRaises(w.SetupError):
                        w.safe_path(self.root, relative + '/created.txt')
                    if relative == 'skill/references':
                        with self.assertRaises(w.SetupError):
                            w.tree_hashes(self.root / 'skill')
                    if relative.endswith('/Scripts'):
                        with self.assertRaises(w.SetupError):
                            w.environment_python(self.root, 'core')
                    self.assertEqual(marker.read_text(), 'Human content')
                    self.assertEqual(list(outside.iterdir()), [marker])
                finally:
                    link.rmdir()

    @unittest.skipIf(os.name == 'nt', 'POSIX virtualenv interpreter links')
    def test_real_virtualenv_interpreter_symlink_is_allowed(self):
        envdir = self.root / '.workbench/envs/core'
        w.venv.EnvBuilder(with_pip=False).create(envdir)
        python = w.environment_python(self.root, 'core')
        self.assertTrue(python.is_file())
        self.assertIn('3.', w.run([str(python), '--version']))


if __name__ == '__main__':
    unittest.main()
