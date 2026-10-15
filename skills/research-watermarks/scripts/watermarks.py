"""Configure and use the installed watermarks-remover Layer B HTTP service."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import ssl
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse


def config_path(workspace):
    return workspace / '.workbench/watermarks/config.json'


def initialize(workspace):
    path = config_path(workspace)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        config = {'backend': 'openai-compatible', 'base_url': None, 'model': None,
                  'allow_remote': False, 'strategy': 'paraphrase@0.8', 'port': 8765}
        with path.open('x', encoding='utf-8') as output:
            json.dump(config, output, indent=2)
            output.write('\n')
    print('Configuration: ' + str(path))


def settings(workspace):
    path = config_path(workspace)
    if not path.is_file():
        raise ValueError('Run init first: backend configuration is missing.')
    config = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(config, dict):
        raise ValueError('Configuration must be a JSON object.')
    if any('key' in name.lower() or 'token' in name.lower() for name in config):
        raise ValueError('Keep credentials in environment variables, not config.')
    if config.get('backend') != 'openai-compatible':
        raise ValueError('This workflow expects the selected OpenAI-compatible API backend.')
    port = config.get('port', 8765)
    if isinstance(port, bool) or not isinstance(port, int) or not 1024 <= port <= 65535:
        raise ValueError('Choose a local port from 1024 to 65535.')
    config['port'] = port
    url = config.get('base_url')
    if url:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError('Use a credential-free HTTP(S) model API base URL.')
        if parsed.hostname not in ('localhost', '127.0.0.1', '::1'):
            if parsed.scheme != 'https' or config.get('allow_remote') is not True:
                raise ValueError('A remote model API requires HTTPS and allow_remote=true.')
    if config.get('strategy', 'paraphrase@0.8') != 'paraphrase@0.8':
        raise ValueError('This wrapper uses the reviewed paraphrase@0.8 strategy.')
    return config


def missing(config, include_key=True):
    fields = [name for name in ('base_url', 'model') if not config.get(name)]
    if include_key and not os.environ.get('WATERMARKS_REWRITE_API_KEY'):
        fields.append('WATERMARKS_REWRITE_API_KEY environment variable')
    return fields


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def request(config, endpoint, body=None):
    headers = {'Content-Type': 'application/json'}
    token = os.environ.get('WATERMARKS_SERVER_API_KEY')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    data = None if body is None else json.dumps(body).encode('utf-8')
    req = urllib.request.Request(f"http://127.0.0.1:{config['port']}" + endpoint,
                                 data=data, headers=headers)
    with urllib.request.build_opener(NoRedirect()).open(req, timeout=180) as response:
        return json.load(response)


def serve(workspace, config):
    runtime = workspace / '.agents/skills/remove-ai-marks/runtime'
    server = runtime / 'service/scripts/server.py'
    if not server.is_file():
        raise ValueError('The full remove-ai-marks runtime is not installed.')
    gap = missing(config)
    if gap:
        print('Rewrite pending: ' + ', '.join(gap), file=sys.stderr)
    strategy = config_path(workspace).with_name('strategy.json')
    strategy.write_text(json.dumps({'default_strategy': 'paraphrase@0.8'}) + '\n', encoding='utf-8')
    env = dict(os.environ)
    # Do not accidentally reuse unrelated rewrite settings inherited from a shell.
    for name in tuple(env):
        if name.startswith('WATERMARKS_REWRITE_') and name != 'WATERMARKS_REWRITE_API_KEY':
            env.pop(name)
    env.update({'WATERMARKS_REWRITE_BACKEND': 'openai-compatible',
                'WATERMARKS_REWRITE_ALLOW_REMOTE': '1' if config.get('allow_remote') is True else '0',
                'WATERMARKS_REWRITE_REASONING_EFFORT': 'off',
                'WATERMARKS_SERVER_VERSION': 'workbench-c5297e9'})
    # Some macOS Python.org builds have no configured CA bundle. Use the
    # system trust bundle for this service only, retaining TLS verification.
    if (sys.platform == 'darwin' and not env.get('SSL_CERT_FILE')
            and not ssl.get_default_verify_paths().cafile
            and Path('/etc/ssl/cert.pem').is_file()):
        env['SSL_CERT_FILE'] = '/etc/ssl/cert.pem'
    for key, variable in (('base_url', 'WATERMARKS_REWRITE_BASE_URL'), ('model', 'WATERMARKS_REWRITE_MODEL')):
        if config.get(key):
            env[variable] = config[key]
    # Upstream appends /v1/chat/completions itself. Accept the common /v1
    # base URL form without accidentally sending to /v1/v1/chat/completions.
    if env.get('WATERMARKS_REWRITE_BASE_URL', '').rstrip('/').endswith('/v1'):
        env['WATERMARKS_REWRITE_BASE_URL'] = env['WATERMARKS_REWRITE_BASE_URL'].rstrip('/')[:-3]
    os.chdir(runtime)
    # Replace the launcher so Ctrl+C/termination also stops the actual service.
    os.execve(sys.executable, [sys.executable, '-u', str(server), '--host', '127.0.0.1',
                             '--port', str(config['port']), '--strategy-config', str(strategy)], env)


def rewrite(workspace, config, source, output):
    # Only the service needs the provider key; the local client talks to it.
    gap = missing(config, include_key=False)
    if gap:
        raise ValueError('Rewrite pending: ' + ', '.join(gap))
    source, output = source.resolve(), output.resolve()
    report_path = output.with_name(output.name + '.watermarks.json')
    if source.suffix.lower() != '.txt':
        raise ValueError('Export selected prose to a .txt input; keep protected spans separate.')
    if source == output or output.exists() or report_path.exists():
        raise ValueError('Choose a new candidate and report path; originals are preserved.')
    original = source.read_bytes()
    original.decode('utf-8')
    response = request(config, '/clean', {'name': 'selected-prose.txt',
                       'file': base64.b64encode(original).decode('ascii'),
                       'options': {'normalize_spaces': False, 'strategy': 'paraphrase@0.8'}})
    if not response.get('ok') or not response.get('report', {}).get('layer_b'):
        raise ValueError('The service did not report a completed Layer B rewrite.')
    candidate = base64.b64decode(response['cleaned'], validate=True)
    if not candidate.strip() or source.read_bytes() != original:
        raise ValueError('Empty result or input changed during processing; no output saved.')
    candidate.decode('utf-8')
    report = {'operation': 'Layer B statistical-watermark reduction rewrite',
              'source_sha256': hashlib.sha256(original).hexdigest(),
              'candidate_sha256': hashlib.sha256(candidate).hexdigest(),
              'changed': candidate != original,
              'backend_model': config['model'], 'service_report': response['report'],
              'vendor_watermark_detection': 'not performed',
              'factual_equivalence': 'requires review'}
    output.parent.mkdir(parents=True, exist_ok=True)
    # Reserve both paths before writing either result; never overwrite old outputs.
    with report_path.open('x', encoding='utf-8') as log:
        with output.open('xb') as result:
            result.write(candidate)
        json.dump(report, log, indent=2, ensure_ascii=False)
        log.write('\n')
    print('Candidate: ' + str(output))
    print('Operation report: ' + str(report_path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('init', 'serve', 'status', 'rewrite'))
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    workspace = args.workspace.expanduser().resolve()
    if args.command == 'init':
        initialize(workspace)
        return 0
    config = settings(workspace)
    if args.command == 'serve':
        return serve(workspace, config)
    if args.command == 'status':
        print(json.dumps({'service': request(config, '/health'),
                          'rewrite_configuration_pending': missing(config, include_key=False),
                          'capabilities': request(config, '/capabilities')}, indent=2))
        return 0
    if not args.input or not args.output:
        parser.error('rewrite requires --input and --output')
    rewrite(workspace, config, args.input, args.output)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except urllib.error.HTTPError as exc:
        # Avoid echoing provider response bodies, which can contain request details.
        print(f'Service request failed (HTTP {exc.code}); inspect local service status.', file=sys.stderr)
        raise SystemExit(1)
    except (ValueError, OSError, KeyError, urllib.error.URLError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
