"""Independently check narrative coverage and the translated source-table appendix."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import zipfile
from markdown_it import MarkdownIt
from validate_ecospold import OriginalRows, norm, visible

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / 'content/ecospold2'
AUDIT = ROOT / 'audit/ecospold2'
WORK = AUDIT / 'tutorial'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class DescriptionRows(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = None
        self.values = []
        self.blocks = {}
        self.heads = []
        self.in_heading = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'tr':
            self.active = attrs.get('data-source-block')
            self.values = []
        if tag == 'th':
            self.in_heading = True

    def handle_data(self, data):
        if self.active:
            self.values.append(data)
        if self.in_heading:
            self.heads.append(data)

    def handle_endtag(self, tag):
        if tag == 'tr' and self.active:
            if self.active in self.blocks:
                raise ValueError('Duplicate source description row: ' + self.active)
            self.blocks[self.active] = norm(''.join(self.values))
            self.active = None
        elif tag == 'th':
            self.in_heading = False

def validate():
    errors = []
    if not (WORK / 'manifest.json').exists():
        return {'errors':['Missing tutorial manifest']}
    manifest = json.loads((WORK / 'manifest.json').read_text())
    source = json.loads((AUDIT / 'source.json').read_text())
    translations = {}
    for shard in 'abc':
        translations.update(json.loads((AUDIT / f'translation-{shard}.json').read_text())['blocks'])
    expected = {(s['id'],f['field_id']) for s in source['sections'] for f in s['fields']}
    coverage = [(c['section'],str(c['field_id'])) for c in manifest['coverage']]
    if len(coverage) != 243 or len(set(coverage)) != 243 or set(coverage) != expected:
        errors.append('Narrative does not cover exactly all 243 fields')
    for shard in 'abc':
        file = WORK / f'narrative-{shard}.json'
        narrative = json.loads(file.read_text())
        review = json.loads((WORK / f'narrative-review-{shard}.json').read_text())
        if review['narrative_sha256'] != sha(file) or review['status'] not in ['passed','passed_with_notes']:
            errors.append(f'Narrative review invalid: {shard}')
        if review['reviewer'] == narrative['author'] or review['reviewed_fields'] != narrative['coverage']:
            errors.append(f'Narrative review coverage invalid: {shard}')
    table_path = BASE / 'attachments/EcoSpold02.zh.html'
    raw = table_path.read_text()
    parser = OriginalRows()
    parser.feed(raw)
    wanted = []
    desc_keys = set()
    for section in source['sections']:
        for f in section['fields']:
            options = translations[f['options_block']] if f.get('options_block') else ''
            values = [f['name'],f['field_id'],f['spold1_id'],options,f['type'],f['size']]
            values.extend({'Yes':'是','No':'否'}.get(f[k],f[k]) for k in ['multiple','required','multilingual','redundant_master_data'])
            wanted.append([norm(v) for v in values])
            desc_keys.update(f['description_blocks'])
    if parser.fields != wanted:
        errors.append('Chinese original-table metadata differs')
    descriptions = DescriptionRows()
    descriptions.feed(raw)
    if set(descriptions.blocks) != desc_keys:
        errors.append('Chinese original-table description coverage differs')
    for key,value in descriptions.blocks.items():
        if value != norm(translations[key]):
            errors.append('Chinese original-table description differs: ' + key)
    expected_headers = ['名称','FieldID','SpoldID（第 1 版）','取值选项','类型','长度','可重复','必填','多语言','主数据冗余字段']
    if descriptions.heads != expected_headers * 22:
        errors.append('Original ten-column structure not preserved')
    article = (BASE / 'format-reference.md').read_text()
    if manifest.get('layout') != 'chaptered-narrative':
        errors.append('Tutorial is not split into narrative chapters')
    rendered = ''
    tokens = []
    for page in BASE.glob('*.md'):
        if page.name in ['format-reference.md','translation-review.md','tutorial-review.md']:
            continue
        text = page.read_text()
        page_tokens = MarkdownIt('commonmark',{'html':True}).enable('table').parse(text)
        tokens.extend(page_tokens)
        if any(t.type == 'table_open' or (t.type in ['html_block','html_inline'] and '<table' in t.content) for t in page_tokens):
            errors.append('A table appears outside the single appendix: '+page.name)
        rendered += ' '+visible(text)
    for shard in 'abc':
        narrative = json.loads((WORK / f'narrative-{shard}.json').read_text())
        for section,text in narrative['sections'].items():
            for para in text.split('\n\n')[1:]:
                if visible(para) not in rendered:
                    errors.append('Narrative paragraph lost: ' + section)
            chapter = ROOT / 'content' / manifest['chapter_pages'][section]
            value = chapter.read_text()
            for heading in ['## 怎样定位、使用与提取','## 对照 demo 理解读取结果']:
                if heading not in value:
                    errors.append('Chapter missing reading/extraction example: '+section)
    appendix_rows = OriginalRows()
    appendix_rows.feed(article)
    if appendix_rows.fields != wanted:
        errors.append('Single GitBook appendix differs from translated HTML metadata')
    layout_review = json.loads((WORK / 'chapter-layout-review.json').read_text())
    if layout_review['status'] not in ['passed','passed_with_notes']:
        errors.append('Chapter layout review not passed')
    current_review_path = WORK / 'xml-examples-guide-review.json'
    current_review = json.loads(current_review_path.read_text()) if current_review_path.exists() else None
    current_files = current_review['files'] if current_review else {}
    if manifest.get('chapter_xml_examples'):
        if current_review is None or current_review['status'] not in ['passed','passed_with_notes']:
            errors.append('Current XML example publication review missing')
    for filename, reviewed_sha in layout_review['files'].items():
        if sha(ROOT / filename) != reviewed_sha and filename not in current_files:
            errors.append('Reviewed chapter/helper changed without superseding review: '+filename)
    for filename, reviewed_sha in current_files.items():
        if sha(ROOT / filename) != reviewed_sha:
            errors.append('Current XML example review changed: '+filename)
    if manifest.get('chapter_xml_examples'):
        from render_ecospold_xml_examples import packets
        from ecospold_xml_examples import validate_packets
        try:
            reviewed_sections=packets()
            typed_counts=validate_packets()
            if len(reviewed_sections)!=22 or len(typed_counts)!=22:
                errors.append('XML examples do not cover all 22 types')
        except (AssertionError,ValueError) as exc:
            errors.append('XML example review/schema invalid: '+str(exc))
    for record in manifest['outputs'] + manifest['review_files']:
        path = ROOT / record['path']
        if not path.exists() or sha(path) != record['sha256']:
            errors.append('Tutorial audited output changed: ' + record['path'])
    code_review = json.loads((WORK / 'tutorial-code-review.json').read_text())
    if code_review['status'] not in ['passed','passed_with_notes']:
        errors.append('Demo/extractor independent review not passed')
    for path,expected_sha in code_review['files'].items():
        if sha(ROOT / path) != expected_sha:
            errors.append('Independently reviewed code or demo changed: ' + path)
    queries = json.loads((WORK / 'queries-review.json').read_text())
    query_text = (WORK / 'extraction-queries.txt').read_text()
    if queries['status'] not in ['passed','passed_with_notes'] or queries['markdown_sha256'] != hashlib.sha256(query_text.encode()).hexdigest() or queries['code_sha256'] != sha(BASE / 'demo/query_demo.py'):
        errors.append('Query example review differs')
    blocks = re.findall(r'```python\n(.*?)\n```',query_text,re.S)
    if len(blocks) != 1 or blocks[0].strip() != (BASE / 'demo/query_demo.py').read_text().strip():
        errors.append('Query code in article differs from runnable file')
    with zipfile.ZipFile(BASE / 'demo/ecospold2-tutorial-demo.zip') as z:
        for name in ['read_section.py','demo-product.spold','demo-electricity.spold','demo-lcia.spold','extract_ecospold.py','query_demo.py','README.txt']:
            if name not in z.namelist() or z.read(name) != (BASE / 'demo' / name).read_bytes():
                errors.append('Demo ZIP missing or stale: ' + name)
    if manifest.get('chapter_xml_examples'):
        with zipfile.ZipFile(BASE/'attachments/ecospold2-xml-examples.zip') as z:
            for record in manifest['chapter_xml_examples']:
                for example in record['examples']:
                    name='xml-examples/'+example['filename']
                    if name not in z.namelist() or z.read(name)!=(BASE/name).read_bytes():
                        errors.append('XML example ZIP missing or stale: '+name)
            if z.read('read_xml_fields.py')!=(BASE/'demo/read_xml_fields.py').read_bytes():
                errors.append('XML field reader ZIP stale')
    return {'narrative_fields':len(coverage),'translated_table_fields':len(parser.fields),
            'translated_description_rows':len(descriptions.blocks),'chapter_pages':len(manifest['chapter_pages']),'appendix_characters':len(article),
            'tables_only_in_appendix':not any(t.type=='table_open' for t in tokens),'errors':errors}

if __name__ == '__main__':
    report = validate()
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(bool(report['errors']))
