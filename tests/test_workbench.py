import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec = importlib.util.spec_from_file_location('workbench', Path(__file__).resolve().parents[1] / 'workbench.py')
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)


class WorkbenchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'workspace with spaces'
        self.root.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def test_offline_bootstrap_is_resumable_and_preserves_human_content(self):
        (self.root / 'AGENTS.md').write_text('Human instructions: preserve experiments.\n')
        (self.root / 'workbench-config.md').write_text('Human research notes.\n')
        self.assertEqual(w.main(['setup', '--workspace', str(self.root), '--offline']), 2)
        before = (self.root / 'AGENTS.md').read_bytes()
        self.assertEqual(w.main(['setup', '--workspace', str(self.root), '--offline']), 2)
        self.assertEqual(before, (self.root / 'AGENTS.md').read_bytes())
        self.assertIn(b'Human instructions', before)
        self.assertEqual((self.root / 'workbench-config.md').read_text(), 'Human research notes.\n')
        state = w.read_state(self.root)
        self.assertEqual(state['checks']['runtime:core']['status'], 'pending')
        self.assertEqual(state['skills']['research-reading']['host_discovery'], 'not verified')
        self.assertTrue((self.root / 'START_HERE.md').is_file())
        self.assertIn('.workbench/', (self.root / '.gitignore').read_text())

    def test_modified_skill_is_preserved(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        skill = self.root / '.agents/skills/research-reading/SKILL.md'
        skill.write_text('Human modified skill')
        with self.assertRaises(w.SetupError):
            w.main(['setup', '--workspace', str(self.root), '--offline'])
        self.assertEqual(skill.read_text(), 'Human modified skill')

    def test_unknown_profile_cannot_become_command(self):
        p = self.root / 'profile.json'
        p.write_text(json.dumps({'extensions': ['symbolic; touch outside']}))
        with self.assertRaises(w.SetupError):
            w.load_profile(p)

    def test_unknown_research_can_defer_everything(self):
        self.assertEqual(w.plan({'extensions': []})['extensions'], [])
        self.assertEqual(len(w.plan({'extensions': ['units', 'units']})['extensions']), 1)

    def test_plan_has_no_workspace_side_effect(self):
        target = self.root / 'absent'
        self.assertEqual(w.main(['plan', '--workspace', str(target)]), 0)
        self.assertFalse(target.exists())

    def test_apply_requires_verified_foundation(self):
        p = self.root / 'profile.json'
        p.write_text('{"extensions":["symbolic"]}')
        with self.assertRaises(w.SetupError):
            w.main(['apply', '--workspace', str(self.root), '--profile', str(p)])

    def test_symlink_escape_is_refused(self):
        outside = Path(self.temp.name) / 'outside'
        outside.mkdir()
        try:
            (self.root / '.agents').symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('Symlink creation is unavailable on this environment')
        with self.assertRaises(w.SetupError):
            w.safe_path(self.root, '.agents/skills/example')
        self.assertEqual(list(outside.iterdir()), [])

    def test_archive_traversal_is_refused(self):
        archive = self.root / 'bad.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('root/skills/example/SKILL.md', 'test')
            z.writestr('root/../escaped', 'bad')
        with self.assertRaises(w.SetupError):
            w.archive_skill(archive, 'skills/example')

    def test_archive_keeps_whole_skill_and_license(self):
        archive = self.root / 'good.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('root/skills/example/SKILL.md', 'test')
            z.writestr('root/skills/example/references/a.md', 'evidence')
            z.writestr('root/LICENSE', 'upstream terms')
            z.writestr('root/unrelated.txt', 'do not install')
        files = w.archive_skill(archive, 'skills/example')
        self.assertEqual(set(files), {'SKILL.md', 'references/a.md', 'UPSTREAM_LICENSE'})

    def test_corrupt_state_is_preserved(self):
        control = self.root / '.workbench'
        control.mkdir()
        p = control / 'state.json'
        p.write_text('{broken')
        with self.assertRaises(w.SetupError):
            w.read_state(self.root)
        self.assertEqual(p.read_text(), '{broken')

    def test_concurrent_installation_is_refused(self):
        with w.installation_lock(self.root):
            with self.assertRaises(w.SetupError):
                with w.installation_lock(self.root):
                    pass
        self.assertFalse((self.root / '.workbench/install.lock').exists())

    def test_failed_extension_does_not_stop_other_extensions(self):
        state = w.read_state(self.root)
        def fake_skill(root, state, name, offline):
            if name == 'sympy':
                raise w.SetupError('simulated interrupted download')
        with patch.object(w, 'remote_skill', side_effect=fake_skill), patch.object(w, 'runtime'):
            result = w.apply_profile(self.root, state, {'extensions': ['symbolic', 'units']}, False)
        self.assertFalse(result)
        self.assertEqual(state['profiles']['symbolic']['status'], 'failed')
        self.assertEqual(state['profiles']['units']['status'], 'installed; task checks pending')

    def test_checksum_mismatch_does_not_install(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, count): return b'unexpected content'
        destination = self.root / 'download.bin'
        with patch.object(w.urllib.request, 'urlopen', return_value=Response()):
            with self.assertRaises(w.SetupError):
                w.download('https://example.com/fixed-file', destination, '0' * 64)
        self.assertFalse(destination.exists())
        self.assertFalse(destination.with_suffix('.bin.part').exists())

    def test_installed_engine_can_operate_its_workspace(self):
        with patch.object(w, 'ROOT', self.root / '.workbench/kit' / w.VERSION), patch.object(w, 'doctor', return_value=True):
            self.assertEqual(w.main(['doctor', '--workspace', str(self.root)]), 0)

    def test_doctor_reports_unfinished_profile_even_if_runtime_works(self):
        state = w.read_state(self.root)
        state['skills'] = {name: {'files': {}} for name in ('research-workbench', 'research-reading')}
        for name in state['skills']:
            (self.root / '.agents/skills' / name).mkdir(parents=True)
        state['profiles']['literature'] = {'status': 'failed'}
        with patch.object(w, 'run', return_value='runtime passed'):
            self.assertFalse(w.doctor(self.root, state))
        self.assertEqual(state['checks']['skill:nature-academic-search']['status'], 'missing')


if __name__ == '__main__':
    unittest.main()
