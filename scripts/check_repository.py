"""Check source syntax, release metadata, local document links, and catalog references."""
import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
registry = json.loads((ROOT / 'registry.json').read_text(encoding='utf-8'))
module = ast.parse((ROOT / 'workbench.py').read_text(encoding='utf-8'))
version = next(node.value.value for node in module.body
               if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == 'VERSION' for target in node.targets))
if registry['version'] != version:
    errors.append('Engine and registry versions differ')
if f'Repository **{version}**' not in (ROOT / 'README.md').read_text(encoding='utf-8'):
    errors.append('README release metadata differs')
if not re.search(r'^## ' + re.escape(version) + r' ', (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8'), re.MULTILINE):
    errors.append('Current release has no changelog entry')
for path in ROOT.rglob('*.py'):
    if any(part in ('.git', '.workbench', '.venv', '__pycache__') for part in path.relative_to(ROOT).parts):
        continue
    ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
for path in ROOT.rglob('*.md'):
    if any(part in ('.git', '.workbench', '.venv', '__pycache__') for part in path.relative_to(ROOT).parts):
        continue
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        target = target.strip().strip('<>').split(' "')[0]
        if '://' in target or target.startswith(('mailto:', '#')) or '<' in target:
            continue
        relative = unquote(target.split('#')[0])
        if relative and not (path.parent / relative).exists():
            errors.append(f'{path.relative_to(ROOT)}: missing local link {target}')
for name, spec in registry['skills'].items():
    if spec['source'] not in registry['sources']:
        errors.append(f'{name}: unknown source')
for name, profile in registry['profiles'].items():
    if any(skill not in registry['skills'] for skill in profile['skills']):
        errors.append(f'{name}: unknown skill')
    if any(not re.fullmatch(r'[A-Za-z0-9_.-]+==[A-Za-z0-9_.+-]+', requirement) for requirement in profile['requirements']):
        errors.append(f'{name}: unpinned requirement')
if errors:
    raise SystemExit('\n'.join(errors))
print('Passed: Python syntax, release metadata, local document links, and catalog references.')
