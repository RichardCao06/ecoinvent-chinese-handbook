#!/usr/bin/env python3
"""Validate a GitBook repo without a GitBook account or network access."""
from collections import Counter
from html.parser import HTMLParser
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
parser = argparse.ArgumentParser()
parser.add_argument('--snapshot', action='store_true', help='Also verify original export and attachment hashes')
args = parser.parse_args()
md = MarkdownIt('commonmark', {'html': True}).enable('table')
errors = []
references = []
anchors = {}

class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.refs.append(attrs[attr])

def walk(tokens):
    for token in tokens:
        yield token
        if token.children:
            yield from walk(token.children)

for file in sorted(ROOT.rglob('*.md')):
    text = file.read_text()
    tokens = md.parse(text)
    page_anchors = []
    for token in walk(tokens):
        for attr in ('href', 'src'):
            ref = token.attrGet(attr)
            if ref:
                references.append((file, ref))
        if token.type in {'html_block', 'html_inline'}:
            h = HTMLReferences()
            h.feed(token.content)
            page_anchors.extend(h.ids)
            references.extend((file, ref) for ref in h.refs)
    anchors[file.resolve()] = set(page_anchors)
    dup = [a for a, n in Counter(page_anchors).items() if n > 1]
    if dup:
        errors.append(f'{file.relative_to(ROOT)}: duplicate anchors {dup}')
    if file.parent == CONTENT / 'articles':
        if len(re.findall(r'^# ', text, re.M)) != 1:
            errors.append(f'{file.name}: expected one page title')
        if text.count('{% tabs %}') != 1 or text.count('{% endtabs %}') != 1 or text.count('{% endtab %}') != 2:
            errors.append(f'{file.name}: incomplete bilingual tabs')
        if '{% tab title="中文" %}' not in text or '{% tab title="English 原文" %}' not in text:
            errors.append(f'{file.name}: missing language tab')

for file, ref in references:
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc:
        continue
    target = (file.parent / unquote(parts.path)).resolve() if parts.path else file.resolve()
    if not target.is_relative_to(ROOT):
        errors.append(f'{file.relative_to(ROOT)}: reference leaves repository: {ref}')
    elif not target.exists():
        errors.append(f'{file.relative_to(ROOT)}: missing target {ref}')
    elif parts.fragment and target.suffix == '.md' and unquote(parts.fragment) not in anchors.get(target, set()):
        errors.append(f'{file.relative_to(ROOT)}: missing anchor {ref}')

toc_tokens = md.parse((CONTENT / 'SUMMARY.md').read_text())
toc = [t.attrGet('href') for t in walk(toc_tokens) if t.type == 'link_open']
if len(toc) != len(set(toc)):
    errors.append('SUMMARY.md contains duplicate pages')
content_pages = {p.relative_to(CONTENT).as_posix() for p in CONTENT.rglob('*.md') if p.name != 'SUMMARY.md'}
if set(toc) != content_pages:
    errors.append(f'SUMMARY coverage mismatch: missing {content_pages - set(toc)}, extra {set(toc) - content_pages}')

config = yaml.safe_load((CONTENT / '.gitbook.yaml').read_text())
if config != {'root': './', 'structure': {'readme': 'README.md', 'summary': 'SUMMARY.md'}}:
    errors.append('Unexpected content configuration')
site = yaml.safe_load((ROOT / 'gitbook-docs.yaml').read_text())
space = site['site']['structure'][0]['children'][0]
if (ROOT / space['content']['directory']).resolve() != CONTENT or space['content']['language'] != 'zh':
    errors.append('Incorrect site content mapping')

snapshot = json.loads((ROOT / 'audit/export.json').read_text())
assets = json.loads((ROOT / 'audit/assets.json').read_text())
if args.snapshot:
    for p in snapshot:
        path = CONTENT / p['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != p['markdown_sha256']:
            errors.append('Snapshot changed: ' + p['path'])
    for asset in assets:
        path = ROOT / asset['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != asset['sha256']:
            errors.append('Asset changed: ' + asset['path'])
issues = json.loads((ROOT / 'audit/issues.json').read_text())
if len(snapshot) != 99 or len(assets) != 213 or len(issues) != 170:
    errors.append('Unexpected source coverage')
report = {'pages': len(content_pages), 'articles': len(snapshot), 'topics': len(list((CONTENT / 'topics').glob('*.md'))),
          'source_blocks': sum(p['blocks'] for p in snapshot), 'assets': len(assets),
          'references': len(references), 'review_annotations': len(issues),
          'pending_expert_review': sum(n['status'] == 'needs_expert_review' for n in issues),
          'snapshot_hashes_checked': args.snapshot, 'errors': errors,
          'gitbook_import_preview_verified': False}
print(json.dumps(report, ensure_ascii=False, indent=2))
if args.snapshot:
    (ROOT / 'audit/validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
raise SystemExit(bool(errors))
