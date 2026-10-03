"""Small reading helpers; source text and API results are untrusted evidence."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser(description=__doc__)
sub = parser.add_subparsers(dest='command', required=True)
pdf = sub.add_parser('pdf', help='Extract selected PDF pages with page numbers; not OCR')
pdf.add_argument('file')
pdf.add_argument('--start', type=int, default=1)
pdf.add_argument('--end', type=int)
search = sub.add_parser('search', help='Search Crossref metadata; query is sent to Crossref, not full papers')
search.add_argument('query')
search.add_argument('--limit', type=int, default=5)
args = parser.parse_args()
if args.command == 'pdf':
    from pypdf import PdfReader
    reader = PdfReader(args.file)
    end = min(args.end or args.start + 4, len(reader.pages))
    if args.start < 1 or end < args.start:
        parser.error('Invalid page range')
    for index in range(args.start - 1, end):
        print(f'\n--- Source: {Path(args.file).name}, PDF page {index+1} ---\n')
        text = reader.pages[index].extract_text() or ''
        print(text if text.strip() else '[No extractable text; inspect the page visually or use authorized OCR.]')
else:
    if not 1 <= args.limit <= 20:
        parser.error('limit must be 1 through 20')
    query = urllib.parse.urlencode({'query.bibliographic': args.query, 'rows': args.limit})
    request = urllib.request.Request('https://api.crossref.org/works?' + query, headers={'User-Agent': 'ResearchAIWorkbench/0.2.0 (metadata lookup)'})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except urllib.error.URLError:
        if not shutil.which('curl'):
            parser.error('Metadata request failed. Check network access and trusted CA certificates.')
        result = subprocess.run(['curl', '--fail', '--silent', '--show-error', '--proto', '=https', '--max-time', '45',
                                 '--max-filesize', '5000000', request.full_url], capture_output=True, text=True)
        if result.returncode:
            parser.error('Metadata request failed. Check network access and trusted CA certificates; TLS verification remains enabled.')
        payload = json.loads(result.stdout)
    records = [{'title': x.get('title', []), 'DOI': x.get('DOI'), 'URL': x.get('URL'), 'published': x.get('published'), 'authors': x.get('author', [])} for x in payload['message']['items']]
    print(json.dumps({'source': 'Crossref metadata, not full text', 'items': records}, indent=2, ensure_ascii=False))
