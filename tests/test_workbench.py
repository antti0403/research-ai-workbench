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
        # Attribution remains available after the downloaded source folder is gone.
        kit = self.root / '.workbench/kit' / w.VERSION
        for name in ('LICENSE', 'NOTICE.md', 'THIRD_PARTY.md', 'SKILLS.md'):
            self.assertEqual((kit / name).read_bytes(), (w.ROOT / name).read_bytes())

    def test_modified_skill_is_preserved(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        skill = self.root / '.agents/skills/research-reading/SKILL.md'
        skill.write_text('Human modified skill')
        with self.assertRaises(w.SetupError):
            w.main(['setup', '--workspace', str(self.root), '--offline'])
        self.assertEqual(skill.read_text(), 'Human modified skill')

    def test_paperqa_is_optional_and_copied_engine_can_install_its_skill_offline(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        destination = self.root / '.agents/skills/research-paperqa/SKILL.md'
        self.assertFalse(destination.exists())
        engine = self.root / '.workbench/kit' / w.VERSION / 'workbench.py'
        spec = importlib.util.spec_from_file_location('copied_paperqa_engine', engine)
        copied = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(copied)
        state = copied.read_state(self.root)
        with patch.object(copied, 'download', side_effect=AssertionError('Bundled skill used network')):
            self.assertFalse(copied.apply_profile(self.root, state, {'extensions': ['paperqa']}, True))
            before = destination.read_bytes()
            self.assertFalse(copied.apply_profile(self.root, state, {'extensions': ['paperqa']}, True))
        self.assertEqual(before, destination.read_bytes())
        self.assertEqual(before, (w.ROOT / 'skills/research-paperqa/SKILL.md').read_bytes())
        self.assertEqual(state['checks']['runtime:paperqa']['status'], 'pending')
        self.assertEqual(state['skills']['research-paperqa']['host_discovery'], 'not verified')
        self.assertFalse((self.root / '.workbench/envs').exists())

    def test_paperqa_apply_preserves_edited_optional_skill_and_reports_failure(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        state = w.read_state(self.root)
        self.assertFalse(w.apply_profile(self.root, state, {'extensions': ['paperqa']}, True))
        destination = self.root / '.agents/skills/research-paperqa/SKILL.md'
        destination.write_text('Human paper workflow', encoding='utf-8')
        self.assertFalse(w.apply_profile(self.root, state, {'extensions': ['paperqa']}, True))
        self.assertEqual(destination.read_text(encoding='utf-8'), 'Human paper workflow')
        self.assertEqual(state['profiles']['paperqa']['status'], 'failed')

    def test_writing_copied_engine_installs_adaptation_and_license_offline(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        destination = self.root / '.agents/skills/anti-defensive-writing'
        self.assertFalse(destination.exists())
        engine = self.root / '.workbench/kit' / w.VERSION / 'workbench.py'
        spec = importlib.util.spec_from_file_location('copied_writing_engine', engine)
        copied = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(copied)
        state = copied.read_state(self.root)
        with patch.object(copied, 'download', side_effect=AssertionError('Offline apply used network')):
            self.assertFalse(copied.apply_profile(self.root, state, {'extensions': ['writing']}, True))
            before = copied.tree_hashes(destination)
            self.assertFalse(copied.apply_profile(self.root, state, {'extensions': ['writing']}, True))
        self.assertEqual(before, copied.tree_hashes(destination))
        self.assertEqual(before, w.tree_hashes(w.ROOT / 'skills/anti-defensive-writing'))
        self.assertTrue((destination / 'UPSTREAM_LICENSE').is_file())
        source = state['skills']['anti-defensive-writing']['source']
        self.assertEqual(source['repo'], 'Adkid-Zephyr/anti-defensive-writing-Skill')
        self.assertTrue(source['modified'])
        self.assertEqual(source['version'], w.VERSION)
        self.assertEqual(state['skills']['anti-defensive-writing']['host_discovery'], 'not verified')
        self.assertEqual(state['checks']['skill:nature-writing']['status'], 'pending')
        self.assertEqual(state['profiles']['writing']['status'], 'pending')
        self.assertFalse((self.root / '.workbench/envs').exists())

    def test_writing_apply_preserves_local_edits_and_unrelated_research(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        state = w.read_state(self.root)
        self.assertFalse(w.apply_profile(self.root, state, {'extensions': ['writing']}, True))
        skill = self.root / '.agents/skills/anti-defensive-writing/SKILL.md'
        skill.write_text('Human writing principles', encoding='utf-8')
        note = self.root / 'wiki/results.md'
        note.write_text('Human results and limitations', encoding='utf-8')
        agents_before = (self.root / 'AGENTS.md').read_bytes()
        self.assertFalse(w.apply_profile(self.root, state, {'extensions': ['writing']}, True))
        self.assertEqual(skill.read_text(encoding='utf-8'), 'Human writing principles')
        self.assertEqual(note.read_text(encoding='utf-8'), 'Human results and limitations')
        self.assertEqual((self.root / 'AGENTS.md').read_bytes(), agents_before)
        self.assertEqual(state['profiles']['writing']['status'], 'failed')

    def test_watermarks_offline_prepares_integration_without_claiming_service_download(self):
        w.main(['setup', '--workspace', str(self.root), '--offline'])
        state = w.read_state(self.root)
        with patch.object(w, 'download', side_effect=AssertionError('Offline apply used network')):
            self.assertFalse(w.apply_profile(self.root, state, {'extensions': ['watermarks']}, True))
        self.assertTrue((self.root / '.agents/skills/research-watermarks/scripts/watermarks.py').is_file())
        self.assertFalse((self.root / '.agents/skills/remove-ai-marks').exists())
        self.assertEqual(state['checks']['skill:remove-ai-marks']['status'], 'pending')
        self.assertEqual(state['profiles']['watermarks']['status'], 'pending')
        self.assertFalse((self.root / '.workbench/envs').exists())

    def test_pinned_source_mapping_installs_full_runtime_and_retained_license(self):
        data = {'SKILL.md': b'---\nname: test-client\ndescription: Test.\n---\n',
                'service/scripts/server.py': b'print("synthetic service")\n',
                'LICENSE': b'Synthetic test license notice\n'}
        source = {'repo': 'example/synthetic', 'commit': 'a' * 40,
                  'license_file': {'path': 'LICENSE', 'sha256': w.digest(data['LICENSE'])}}
        spec = {'source': 'synthetic', 'path': 'skills/test-client', 'files': [
            {'path': 'SKILL.md', 'sha256': w.digest(data['SKILL.md'])},
            {'path': 'runtime/service/scripts/server.py', 'source_path': 'service/scripts/server.py',
             'sha256': w.digest(data['service/scripts/server.py'])}]}

        class Response:
            def __init__(self, content): self.content = content
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, count): return self.content

        def fetch(request, **kwargs):
            relative = request.full_url.split('/' + source['commit'] + '/')[1]
            if relative == 'skills/test-client/SKILL.md': relative = 'SKILL.md'
            return Response(data[relative])

        state = w.read_state(self.root)
        with patch.dict(w.REGISTRY['sources'], {'synthetic': source}), patch.dict(w.REGISTRY['skills'], {'test-client': spec}), patch.object(w.urllib.request, 'urlopen', side_effect=fetch):
            w.remote_skill(self.root, state, 'test-client', False)
            destination = self.root / '.agents/skills/test-client'
            self.assertEqual((destination / 'runtime/service/scripts/server.py').read_bytes(), data['service/scripts/server.py'])
            self.assertEqual((destination / 'UPSTREAM_LICENSE.md').read_bytes(), data['LICENSE'])
            (destination / 'runtime/service/scripts/server.py').write_bytes(b'Human changes')
            with self.assertRaises(w.SetupError):
                w.remote_skill(self.root, state, 'test-client', False)
            self.assertEqual((destination / 'runtime/service/scripts/server.py').read_bytes(), b'Human changes')

    def test_source_mapping_refuses_parent_traversal_before_download(self):
        spec = {'source': 'watermarks-remover', 'path': 'skills/test-client',
                'files': [{'path': 'SKILL.md', 'source_path': '../escape', 'sha256': '0' * 64}]}
        with patch.dict(w.REGISTRY['skills'], {'test-client': spec}), patch.object(w, 'download') as download:
            with self.assertRaises(w.SetupError):
                w.remote_skill(self.root, w.read_state(self.root), 'test-client', False)
        download.assert_not_called()
        self.assertFalse((self.root / '.agents/skills/test-client').exists())

    def test_unknown_profile_cannot_become_command(self):
        p = self.root / 'profile.json'
        p.write_text(json.dumps({'extensions': ['symbolic; touch outside']}))
        with self.assertRaises(w.SetupError):
            w.load_profile(p)

    def test_python_311_rejects_figures_before_creating_or_installing_a_runtime(self):
        state = w.read_state(self.root)
        with patch.object(w.sys, 'version_info', (3, 11, 9)), patch.object(w, 'run') as run, patch.object(w.venv.EnvBuilder, 'create') as create:
            with self.assertRaisesRegex(w.SetupError, 'requires Python 3.12'):
                w.runtime(self.root, state, 'figures', w.REGISTRY['profiles']['figures']['requirements'])
        self.assertFalse((self.root / '.workbench/envs/figures').exists())
        run.assert_not_called()
        create.assert_not_called()
        self.assertEqual(state['checks']['runtime:figures']['status'], 'failed')

    def test_python_311_can_still_prepare_figures_offline_without_packages(self):
        state = w.read_state(self.root)
        with patch.object(w.sys, 'version_info', (3, 11, 9)), patch.object(w, 'run') as run:
            w.runtime(self.root, state, 'figures', w.REGISTRY['profiles']['figures']['requirements'], offline=True)
        self.assertEqual(state['checks']['runtime:figures']['status'], 'pending')
        self.assertFalse((self.root / '.workbench/envs/figures').exists())
        run.assert_not_called()

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
            z.writestr('root/skills/example/assets/THIRD_PARTY_NOTICES.md', 'nested terms')
            z.writestr('root/LICENSE', 'upstream terms')
            z.writestr('root/NOTICE', 'upstream attribution')
            z.writestr('root/unrelated.txt', 'do not install')
        files = w.archive_skill(archive, 'skills/example')
        self.assertEqual(set(files), {'SKILL.md', 'references/a.md', 'assets/THIRD_PARTY_NOTICES.md', 'UPSTREAM_LICENSE', 'UPSTREAM_NOTICE'})
        self.assertEqual(files['UPSTREAM_NOTICE'], b'upstream attribution')
        self.assertEqual(files['assets/THIRD_PARTY_NOTICES.md'], b'nested terms')

    def test_figure_profile_does_not_fetch_withheld_assets(self):
        state = w.read_state(self.root)
        with patch.object(w, 'remote_skill') as fetch, patch.object(w, 'runtime') as runtime:
            self.assertTrue(w.apply_profile(self.root, state, {'extensions': ['figures']}, False))
        fetch.assert_not_called()
        self.assertEqual(runtime.call_args.args[3], ['numpy==2.5.3', 'matplotlib==3.11.2'])
        self.assertNotIn('nature-figure', w.REGISTRY['skills'])

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
