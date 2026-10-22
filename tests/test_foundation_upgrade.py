"""Foundation upgrades retain user changes and verify the selected release."""
import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from test_workbench import w


class FoundationUpgradeTests(unittest.TestCase):
    old_files = {'SKILL.md': b'Previous foundation', 'references/removed.md': b'Old resource'}
    new_files = {'SKILL.md': b'Current foundation', 'references/added.md': b'New resource'}

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

    def source(self, version=None):
        return {'repository': 'antti0403/research-ai-workbench',
                'version': w.VERSION if version is None else version}

    def current_files(self, name):
        folder = w.ROOT / 'skills' / name
        return {relative: (folder / relative).read_bytes() for relative in w.tree_hashes(folder)}

    def install_old(self, name='research-reading', root=None, state=None, version='0.3.7'):
        root = self.root if root is None else root
        state = self.state if state is None else state
        w.install_directory(root, state, name, self.old_files, self.source(version))
        return root / '.agents/skills' / name

    def test_pristine_owned_upgrade_replaces_complete_tree_and_repeats_without_backup_duplication(self):
        target = self.install_old()
        old_hashes = w.tree_hashes(target)
        w.install_directory(self.root, self.state, 'research-reading', self.new_files,
                            self.source(), allow_owned_upgrade=True)
        expected = {name: w.digest(data) for name, data in self.new_files.items()}
        self.assertEqual(w.tree_hashes(target), expected)
        self.assertFalse((target / 'references/removed.md').exists())
        backups = list((self.root / '.workbench/backups/skills').iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual(w.tree_hashes(backups[0]), old_hashes)
        self.assertEqual(self.state['skills']['research-reading']['source'], self.source())
        self.assertEqual(self.state['skills']['research-reading']['host_discovery'], 'not verified')
        w.install_directory(self.root, self.state, 'research-reading', self.new_files,
                            self.source(), allow_owned_upgrade=True)
        self.assertEqual(list((self.root / '.workbench/backups/skills').iterdir()), backups)
        self.assertEqual(w.read_state(self.root)['skills']['research-reading']['files'], expected)

    def test_changed_or_unowned_skills_and_invalid_lineage_are_preserved(self):
        scenarios = ('edited', 'extra', 'missing', 'unowned', 'different repository',
                     'same version', 'downgrade', 'missing source', 'invalid version',
                     'upgrade disabled', 'optional skill')
        for index, scenario in enumerate(scenarios):
            with self.subTest(scenario=scenario):
                root = self.root / str(index)
                root.mkdir()
                state = w.read_state(root)
                w.save_state(root, state)
                name = 'research-paperqa' if scenario == 'optional skill' else 'research-reading'
                version = w.VERSION if scenario == 'same version' else '99.0.0' if scenario == 'downgrade' else '0.3.7'
                target = self.install_old(name, root, state, version)
                if scenario == 'edited':
                    (target / 'SKILL.md').write_bytes(b'Human changes')
                elif scenario == 'extra':
                    (target / 'human.md').write_bytes(b'Human notes')
                elif scenario == 'missing':
                    (target / 'references/removed.md').unlink()
                elif scenario == 'unowned':
                    del state['skills'][name]
                elif scenario == 'different repository':
                    state['skills'][name]['source']['repository'] = 'someone/another-workbench'
                elif scenario == 'missing source':
                    state['skills'][name].pop('source')
                elif scenario == 'invalid version':
                    state['skills'][name]['source']['version'] = None
                before = w.tree_hashes(target)
                record_before = copy.deepcopy(state['skills'])
                with self.assertRaises(w.SetupError):
                    w.install_directory(root, state, name, self.new_files, self.source(),
                                        allow_owned_upgrade=scenario != 'upgrade disabled')
                self.assertEqual(w.tree_hashes(target), before)
                self.assertEqual(state['skills'], record_before)
                self.assertFalse((root / '.workbench/backups/skills').exists())

    def test_rename_failure_restores_previous_tree_and_installation_record(self):
        target = self.install_old()
        old_hashes = w.tree_hashes(target)
        before = copy.deepcopy(self.state['skills'])
        rename = Path.rename

        def fail_staging(path, destination):
            if path.name == 'skill' and destination.resolve() == target.resolve():
                raise OSError('Synthetic directory replacement failure')
            return rename(path, destination)

        with patch.object(Path, 'rename', fail_staging):
            with self.assertRaises(OSError):
                w.install_directory(self.root, self.state, 'research-reading', self.new_files,
                                    self.source(), allow_owned_upgrade=True)
        self.assertEqual(w.tree_hashes(target), old_hashes)
        self.assertEqual(self.state['skills'], before)
        self.assertEqual(w.read_state(self.root)['skills'], before)
        w.install_directory(self.root, self.state, 'research-reading', self.new_files,
                            self.source(), allow_owned_upgrade=True)
        self.assertEqual(w.tree_hashes(target), self.state['skills']['research-reading']['files'])

    def test_state_write_failure_is_recoverable_without_replacing_the_backup(self):
        target = self.install_old()
        before = copy.deepcopy(self.state['skills'])
        atomic_write = w.atomic_write

        def fail_state(path, data):
            if path.name == 'state.json':
                raise OSError('Synthetic state write failure')
            return atomic_write(path, data)

        with patch.object(w, 'atomic_write', fail_state):
            with self.assertRaises(OSError):
                w.install_directory(self.root, self.state, 'research-reading', self.new_files,
                                    self.source(), allow_owned_upgrade=True)
        self.assertEqual(w.read_state(self.root)['skills'], before)
        backups = list((self.root / '.workbench/backups/skills').iterdir())
        state = w.read_state(self.root)
        w.install_directory(self.root, state, 'research-reading', self.new_files,
                            self.source(), allow_owned_upgrade=True)
        self.assertEqual(list((self.root / '.workbench/backups/skills').iterdir()), backups)
        self.assertEqual(w.tree_hashes(target), w.read_state(self.root)['skills']['research-reading']['files'])

    def test_current_engine_rejects_pristine_old_foundation_even_after_state_version_changes(self):
        for name in w.FOUNDATION_SKILLS:
            self.install_old(name)
        w.save_state(self.root, self.state)
        self.assertEqual(w.read_state(self.root)['version'], w.VERSION)
        before = copy.deepcopy(self.state['skills'])
        with patch.object(w, 'check_runtime', return_value='Synthetic runtime check'):
            self.assertFalse(w.verify_foundation(self.root, self.state))
            self.assertFalse(w.doctor(self.root, self.state))
        self.assertEqual(self.state['skills'], before)
        profile = self.root / 'selection.json'
        profile.write_text(json.dumps({'extensions': []}), encoding='utf-8')
        with patch.object(w, 'check_runtime', return_value='Synthetic runtime check'), patch.object(w, 'apply_profile') as apply:
            with self.assertRaises(w.SetupError):
                w.main(['apply', '--workspace', str(self.root), '--profile', str(profile)])
        apply.assert_not_called()

    def test_partial_setup_upgrade_keeps_each_skill_provenance_and_cannot_pass_foundation_checks(self):
        for name in w.FOUNDATION_SKILLS:
            self.install_old(name)
        second = w.FOUNDATION_SKILLS[1]
        edited = self.root / '.agents/skills' / second / 'SKILL.md'
        edited.write_bytes(b'Human reading workflow')
        previous = copy.deepcopy(self.state['skills'][second])
        with self.assertRaises(w.SetupError):
            w.main(['setup', '--workspace', str(self.root), '--offline'])
        state = w.read_state(self.root)
        first = w.FOUNDATION_SKILLS[0]
        self.assertEqual(state['skills'][first]['source'], self.source())
        self.assertEqual(state['skills'][first]['files'],
                         {name: w.digest(data) for name, data in self.current_files(first).items()})
        self.assertEqual(state['skills'][second], previous)
        self.assertEqual(edited.read_bytes(), b'Human reading workflow')
        with patch.object(w, 'check_runtime', return_value='Synthetic runtime check'):
            self.assertFalse(w.verify_foundation(self.root, state))
            self.assertFalse(w.doctor(self.root, state))


if __name__ == '__main__':
    unittest.main()
