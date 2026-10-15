"""Test the installed full Layer B service with a controlled local API responder."""
import argparse
import base64
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request


def command(helper, *args, env, expected=0):
    result = subprocess.run([sys.executable, str(helper), *map(str, args)],
                            env=env, capture_output=True, text=True,
                            encoding='utf-8', timeout=30)
    if result.returncode != expected:
        raise RuntimeError(f'Expected exit {expected}, got {result.returncode}: '
                           + result.stdout + result.stderr)
    return result


def free_port():
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


def wait_service(url, process):
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError('Service exited: ' + process.stderr.read().decode('utf-8'))
        try:
            with urllib.request.urlopen(url + '/health', timeout=1) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError):
            time.sleep(0.1)
    raise RuntimeError('Local service did not become ready.')


def stop(process):
    process.terminate()
    try:
        process.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()


def check(workspace):
    skills = Path(workspace).resolve() / '.agents/skills'
    for name in ('remove-ai-marks', 'research-watermarks'):
        if not (skills / name / 'SKILL.md').is_file():
            raise RuntimeError('Install the watermarks profile before this check.')
    if not (skills / 'remove-ai-marks/UPSTREAM_LICENSE.md').is_file():
        raise RuntimeError('The retained upstream license is missing.')
    calls = []
    candidate = 'For this synthetic case, the voltage is 230 V at 50 Hz.'

    class ModelHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
            calls.append((self.path, body))
            data = json.dumps({'choices': [{'message': {'content': candidate}}]}).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *_args):
            pass

    model = ThreadingHTTPServer(('127.0.0.1', 0), ModelHandler)
    thread = threading.Thread(target=model.serve_forever, daemon=True)
    thread.start()
    try:
        with tempfile.TemporaryDirectory(prefix='watermarks-wiring-') as temporary:
            root = Path(temporary)
            for name in ('remove-ai-marks', 'research-watermarks'):
                shutil.copytree(skills / name, root / '.agents/skills' / name,
                                ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            helper = root / '.agents/skills/research-watermarks/scripts/watermarks.py'
            env = {key: value for key, value in os.environ.items()
                   if not key.startswith('WATERMARKS_')}
            env['PYTHONDONTWRITEBYTECODE'] = '1'
            command(helper, 'init', '--workspace', root, env=env)
            config_path = root / '.workbench/watermarks/config.json'
            config = json.loads(config_path.read_text())
            source = root / 'source.txt'
            output = root / 'candidate.txt'
            original = 'Synthetic fixture at 50 Hz uses 230 V.\u200b'
            source.write_text(original, encoding='utf-8')
            command(helper, 'rewrite', '--workspace', root, '--input', source,
                    '--output', output, env=env, expected=1)
            if output.exists() or calls:
                raise RuntimeError('Unconfigured client performed a rewrite.')
            config.update({'base_url': f'http://127.0.0.1:{model.server_port}/v1',
                           'model': 'synthetic-test-responder', 'port': free_port()})
            config_path.write_text(json.dumps(config))
            env['WATERMARKS_REWRITE_API_KEY'] = 'synthetic-test-key'
            process = subprocess.Popen([sys.executable, str(helper), 'serve', '--workspace', str(root)],
                                       env=env, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            try:
                url = f"http://127.0.0.1:{config['port']}"
                wait_service(url, process)
                command(helper, 'status', '--workspace', root, env=env)
                command(helper, 'rewrite', '--workspace', root, '--input', source,
                        '--output', output, env=env)
                report = json.loads(output.with_name(output.name + '.watermarks.json').read_text())
                if output.read_text() != candidate or source.read_text() != original:
                    raise RuntimeError('Candidate or source preservation failed.')
                if len(calls) != 1 or calls[0][0] != '/v1/chat/completions':
                    raise RuntimeError('The service did not call the configured compatible API.')
                if calls[0][1]['model'] != config['model'] or '230 V' not in json.dumps(calls[0][1]):
                    raise RuntimeError('The model request lost its selected input/model.')
                if report['service_report']['layer_b']['strategy'] != ['paraphrase@0.8']:
                    raise RuntimeError('The required Layer B strategy did not execute.')
                if report['vendor_watermark_detection'] != 'not performed':
                    raise RuntimeError('The test incorrectly claims vendor watermark verification.')
                command(helper, 'rewrite', '--workspace', root, '--input', source,
                        '--output', output, env=env, expected=1)
                if len(calls) != 1 or output.read_text() != candidate:
                    raise RuntimeError('Existing output was overwritten or another model call was made.')
            finally:
                stop(process)
            # A live service without a configured backend must reject /clean.
            config.update({'base_url': None, 'model': None})
            config_path.write_text(json.dumps(config))
            env.pop('WATERMARKS_REWRITE_API_KEY')
            process = subprocess.Popen([sys.executable, str(helper), 'serve', '--workspace', str(root)],
                                       env=env, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            try:
                wait_service(url, process)
                body = json.dumps({'name': 'sample.txt', 'file': base64.b64encode(b'Fixture').decode()}).encode()
                request = urllib.request.Request(url + '/clean', data=body,
                                                 headers={'Content-Type': 'application/json'})
                try:
                    urllib.request.urlopen(request, timeout=5)
                except urllib.error.HTTPError as exc:
                    if exc.code != 400:
                        raise
                else:
                    raise RuntimeError('Unconfigured live service reported a successful clean.')
            finally:
                stop(process)
    finally:
        model.shutdown()
        model.server_close()
        thread.join(timeout=5)
    print('Passed: full installed HTTP service, Layer B request through a controlled '
          'local API responder, explicit missing-backend failures, source preservation, '
          'and existing-output refusal. No real model call, paid API, or '
          'vendor-watermark removal test was performed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    check(parser.parse_args().workspace)
