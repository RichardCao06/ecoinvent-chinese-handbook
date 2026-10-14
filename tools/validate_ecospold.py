"""Check field coverage, exact original metadata, review provenance and export integrity."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'
AUDIT = ROOT / 'audit/ecospold2'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def norm(text):
    return re.sub(r'\s+', ' ', text).strip()

class OriginalRows(HTMLParser):
    """Independent extraction of the ten-column rows using the standard library."""
    def __init__(self):
        super().__init__()
        self.stack = []
        self.fields = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.stack.append({'row': [], 'cell': None})
        elif self.stack:
            top = self.stack[-1]
            if tag == 'tr':
                top['row'] = []
            elif tag in ['td', 'th']:
                top['cell'] = []
            elif tag == 'br' and top['cell'] is not None:
                top['cell'].append(' ')

    def handle_data(self, text):
        if self.stack and self.stack[-1]['cell'] is not None:
            self.stack[-1]['cell'].append(text)

    def handle_endtag(self, tag):
        if not self.stack:
            return
        top = self.stack[-1]
        if tag in ['td', 'th'] and top['cell'] is not None:
            top['row'].append(norm(''.join(top['cell'])))
            top['cell'] = None
        elif tag == 'tr':
            row = top['row']
            if len(row) == 10 and row[1].isdigit():
                self.fields.append(row)
            top['row'] = []
        elif tag == 'table':
            self.stack.pop()

class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, text):
        self.text.append(text)

def visible(markdown):
    parser = VisibleText()
    parser.feed(MarkdownIt('commonmark', {'html': True}).enable('table').render(markdown))
    return norm(' '.join(parser.text))

def validate():
    errors = []
    if not (AUDIT / 'manifest.json').exists():
        return {'errors': ['Missing ecoSpold field manifest']}
    manifest = json.loads((AUDIT / 'manifest.json').read_text())
    source = json.loads((AUDIT / 'source.json').read_text())
    original = CONTENT / 'ecospold2/original/Format description/EcoSpold02.html'
    if sha(original) != source['source_sha256'] or sha(original) != manifest['source_sha256']:
        errors.append('Original HTML hash differs')
    parser = OriginalRows()
    parser.feed(original.read_text())
    expected = []
    xml_ns = {'xs': 'http://www.w3.org/2001/XMLSchema', 'es': 'http://www.EcoInvent.org/EcoSpold02'}
    schema_cache = {}
    for section in source['sections']:
        for field in section['fields']:
            expected.append([field[k] for k in ['name','field_id','spold1_id','options_en','type','size','multiple','required','multilingual','redundant_master_data']])
            fact = field['schema']
            path = CONTENT / 'ecospold2/original/Schemas/datasets' / fact['file']
            if path not in schema_cache:
                schema_cache[path] = ET.parse(path)
            matches = []
            for node in schema_cache[path].iter():
                if node.tag not in ['{http://www.w3.org/2001/XMLSchema}element', '{http://www.w3.org/2001/XMLSchema}attribute']:
                    continue
                fid = node.find('./xs:annotation/xs:appinfo/es:fieldId', xml_ns)
                if fid is not None and fid.text == field['field_id']:
                    matches.append(node)
            if len(matches) != 1:
                errors.append(f'Schema FieldID {field["field_id"]} match count {len(matches)}')
            else:
                node = matches[0]
                name = ('@' if node.tag.endswith('attribute') else '') + node.get('name', '')
                if name != field['name']:
                    errors.append(f'Schema name differs: {field["field_id"]}')
                for key in ['type','minOccurs','maxOccurs','use','default']:
                    if node.get(key) != fact[key]:
                        errors.append(f'Schema {key} differs: {field["field_id"]}')
    if parser.fields != [[norm(v) for v in row] for row in expected]:
        errors.append(f'Original metadata differs: extracted {len(parser.fields)} / expected {len(expected)}')
    translations = {}
    reviewed = set()
    for shard in 'abc':
        sp = AUDIT / f'source-{shard}.json'
        tp = AUDIT / f'translation-{shard}.json'
        sr = json.loads(sp.read_text())
        tr = json.loads(tp.read_text())
        review = json.loads((AUDIT / f'review-{shard}.json').read_text())
        if set(sr['blocks']) != set(tr['blocks']):
            errors.append(f'Translation coverage mismatch: {shard}')
        if review['source_sha256'] != sha(sp) or review['translation_sha256'] != sha(tp):
            errors.append(f'Review provenance differs: {shard}')
        if review['status'] not in ['passed','passed_with_notes'] or set(review['reviewed_blocks']) != set(sr['blocks']):
            errors.append(f'Review incomplete: {shard}')
        if review['reviewer'] == tr['translator']:
            errors.append(f'Reviewer is translator: {shard}')
        if reviewed & set(review['reviewed_blocks']):
            errors.append(f'Duplicate reviewed blocks: {shard}')
        reviewed.update(review['reviewed_blocks'])
        translations.update(tr['blocks'])
    if set(translations) != set(source['blocks']) or reviewed != set(source['blocks']):
        errors.append('Merged coverage differs')
    if manifest.get('presentation') == 'chaptered-narrative':
        appendix = visible((CONTENT / 'ecospold2/format-reference.md').read_text())
        for key,value in translations.items():
            if norm(value) not in appendix:
                errors.append('Chinese appendix source block missing: ' + key)
        for section in source['sections']:
            entries = [f for f in manifest['fields'] if f['section'] == section['id']]
            text = (CONTENT / entries[0]['page']).read_text()
            if text.count('id="read-'+section['id'].lower()+'"') != 1:
                errors.append('Missing narrative chapter anchor: ' + section['id'])
            for field in section['fields']:
                if not re.search(r'`@?' + re.escape(field['name'].lstrip('@')) + r'`',text):
                    errors.append('Field absent from chapter prose: ' + field['field_id'])
    else:
        for section in source['sections']:
            entries = [f for f in manifest['fields'] if f['section'] == section['id']]
            text = (CONTENT / entries[0]['page']).read_text()
            rendered = visible(text)
            for marker in ['{% tabs %}', '{% endtabs %}', '{% tab title="中文" %}', '{% tab title="English 原文" %}']:
                if text.count(marker) != 1:
                    errors.append(f'Incorrect bilingual tabs: {section["id"]} {marker}')
            for field in entries:
                if text.count(f'id="{field["anchor"]}"') != 1 or text.count(f'id="en-{field["anchor"]}"') != 1:
                    errors.append(f'Field anchors missing/duplicated: {field["field_id"]}')
            keys = [k for k in source['blocks'] if k.startswith(section['id'] + '.')]
            for key in keys:
                if norm(translations[key]) not in rendered or norm(source['blocks'][key]) not in rendered:
                    errors.append(f'Export text missing: {key}')
        overview_text = visible((CONTENT / 'ecospold2/README.md').read_text())
        for key in source['overview_blocks']:
            if norm(translations[key]) not in overview_text or norm(source['blocks'][key]) not in overview_text:
                errors.append(f'Overview text missing: {key}')
    for page in manifest['pages']:
        if sha(CONTENT / page['path']) != page['sha256']:
            errors.append('Field page modified without audit update: ' + page['path'])
    for file in manifest['original_files']:
        if sha(CONTENT / file['path']) != file['sha256']:
            errors.append('Original file changed: ' + file['path'])
    if len(parser.fields) != 243 or len(source['sections']) != 22 or len(source['blocks']) != 388:
        errors.append('Unexpected official field coverage')
    return {'sections': len(source['sections']), 'fields': len(parser.fields), 'source_blocks': len(source['blocks']),
            'pages': len(manifest['pages']), 'original_files': len(manifest['original_files']),
            'review_annotations': len(manifest['notes']),
            'pending_expert_review': sum(n['status'] == 'needs_expert_review' for n in manifest['notes']), 'errors': errors}

if __name__ == '__main__':
    result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))
