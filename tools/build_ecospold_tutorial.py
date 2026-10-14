"""Compose the reviewed narrative tutorial and its faithful Chinese HTML appendix."""
import hashlib
import html
import json
from pathlib import Path
import re
import zipfile
import copy
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'content/ecospold2'
AUDIT = ROOT / 'audit/ecospold2'
WORK = AUDIT / 'tutorial'
GROUPS = [
    ('活动描述：确定清单适用于什么活动', ['TActivity','TClassification','TGeography','TTechnology','TTimePeriod','TMacroEconomicScenario']),
    ('交换数据：从清单中读取数量和结果', ['TCustomExchange','TIntermediateExchange','TElementaryExchange','TParameter','TImpactIndicatorResult']),
    ('复合类型：解释区室、属性、不确定性和文本', ['TCompartment','TUncertainty','TProperty','TTransferCoefficient','TTextAndImage']),
    ('建模与审查：判断结果的依据', ['TRepresentativeness','TReview']),
    ('管理信息：保留来源和版本证据', ['TDataEntryBy','TDataGeneratorAndPublication','TFileAttributes','TRequiredContextReference'])]
TITLES = {'TActivity':'活动','TClassification':'分类','TGeography':'地理区域','TTechnology':'技术',
          'TTimePeriod':'时间范围','TMacroEconomicScenario':'宏观经济情景','TCustomExchange':'交换的通用字段',
          'TIntermediateExchange':'中间交换专用字段','TElementaryExchange':'基本流交换专用字段','TParameter':'参数',
          'TImpactIndicatorResult':'影响指标结果','TCompartment':'区室与子区室','TUncertainty':'不确定性',
          'TProperty':'属性','TTransferCoefficient':'转移系数','TTextAndImage':'文本与图像',
          'TRepresentativeness':'代表性','TReview':'审查','TDataEntryBy':'数据录入者',
          'TDataGeneratorAndPublication':'数据生成者与发布','TFileAttributes':'文件属性','TRequiredContextReference':'所需上下文引用'}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def escape(value):
    return html.escape(str(value), quote=True)

def flag(value):
    return {'Yes':'是','No':'否'}.get(value,value)

def tables(source, translations):
    """Preserve the source's ten-column metadata row and colspan=9 explanation rows."""
    fragments = []
    heads = ['名称','FieldID','SpoldID（第 1 版）','取值选项','类型','长度','可重复','必填','多语言','主数据冗余字段']
    for section in source['sections']:
        sid = section['id']
        fragments.append(f'<h3><a href="#appendix-{sid}" id="appendix-{sid}"></a>{TITLES[sid]}（{sid}）</h3>')
        occurrence = section['occurrence']
        fragments.append(f'<p>原表分组可重复：{flag(occurrence[1])}；原表分组必填：{flag(occurrence[3])}。</p>')
        fragments.extend(f'<p>{escape(translations[k])}</p>' for k in section['intro_blocks'])
        parts = ['<table class="format-table">', '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in heads) + '</tr></thead>', '<tbody>']
        for f in section['fields']:
            options = translations[f['options_block']] if f.get('options_block') else ''
            vals = [f['name'],f['field_id'],f['spold1_id'],options,f['type'],f['size'],flag(f['multiple']),flag(f['required']),flag(f['multilingual']),flag(f['redundant_master_data'])]
            parts += [f'<tr data-field-id="{escape(f["field_id"])}">' + ''.join(f'<td>{escape(v)}</td>' for v in vals) + '</tr>']
            for key in f['description_blocks']:
                parts += [f'<tr data-source-block="{escape(key)}"><td></td><td colspan="9">{escape(translations[key])}</td></tr>']
        parts += ['</tbody></table>']
        fragments += parts
    return '\n'.join(fragments)

def xml_examples():
    uri = 'http://www.EcoInvent.org/EcoSpold02'
    ns = {'es':uri}
    ET.register_namespace('',uri)
    product = ET.parse(OUT / 'demo/demo-product.spold').getroot()
    lcia = ET.parse(OUT / 'demo/demo-lcia.spold').getroot()
    flow = product.find('es:activityDataset/es:flowData',ns)
    selected = [
        ('参考产品：10 kg',next(n for n in flow.findall('es:intermediateExchange',ns) if n.findtext('es:outputGroup',namespaces=ns) == '0')),
        ('电力输入：25 kWh',next(n for n in flow.findall('es:intermediateExchange',ns) if n.find('es:inputGroup',ns) is not None)),
        ('化石源二氧化碳修正：仍是 outputGroup 输出',next(n for n in flow.findall('es:elementaryExchange',ns) if n.get('amount') == '-0.1')),
        ('模拟 LCIA 指标：13.9 kg CO2-eq',lcia.find('es:activityDataset/es:flowData/es:impactIndicator',ns))]
    def identity(n):
        return (n.tag,dict(n.attrib),(n.text or '').strip(),[identity(c) for c in n])
    def fold(match):
        indent, tag, attrs, ending = match.groups()
        if len(match.group()) <= 100:
            return match.group()
        attr_list = re.findall(r'[\w:.-]+="[^"]*"',attrs)
        return indent + tag + '\n' + '\n'.join(indent+'    '+a for a in attr_list) + '\n' + indent + ending
    result = ['### 对照 demo 阅读四个实际 XML 节点', '',
              '下面的节点直接摘自配套教学文件，仅将较长的属性行折行。每个片段是该节点的完整结构；文件根元素、兄弟节点和管理信息请看完整 demo。', '']
    manifest = []
    for title, node in selected:
        assert node is not None
        saved = copy.deepcopy(node)
        saved.tail = None
        xml = ET.tostring(saved,encoding='unicode').strip()
        xml = re.sub(r'(?m)^([ \t]*)(<[\w:.-]+)([^\n>]*?)(/?>)',fold,xml)
        assert identity(ET.fromstring(xml)) == identity(saved), title
        result += [f'**{title}**', '', '```xml', xml, '```', '']
        manifest.append({'title':title,'tag':node.tag,'attributes':dict(node.attrib),'snippet_sha256':hashlib.sha256(xml.encode()).hexdigest()})
    return '\n'.join(result),manifest

def build_content():
    source = json.loads((AUDIT / 'source.json').read_text())
    translations = {}
    for shard in 'abc':
        translations.update(json.loads((AUDIT / f'translation-{shard}.json').read_text())['blocks'])
    guide = json.loads((WORK / 'guide.json').read_text())
    guide_review = json.loads((WORK / 'tutorial-guide-review.json').read_text())
    for filename, value in [('opening.md',guide['opening']),('practice.md',guide['practice'])]:
        assert guide_review['files'][filename] == hashlib.sha256(value.encode()).hexdigest(), filename
    assert guide_review['status'] in ['passed','passed_with_notes']
    query_review = json.loads((WORK / 'queries-review.json').read_text())
    assert query_review['status'] in ['passed','passed_with_notes']
    query_text = (WORK / 'extraction-queries.txt').read_text()
    assert query_review['markdown_sha256'] == hashlib.sha256(query_text.encode()).hexdigest()
    assert query_review['code_sha256'] == digest(OUT / 'demo/query_demo.py')
    code_review = json.loads((WORK / 'tutorial-code-review.json').read_text())
    assert code_review['status'] in ['passed','passed_with_notes']
    chapters = {}
    coverage = []
    notes = []
    for shard in 'abc':
        path = WORK / f'narrative-{shard}.json'
        narrative = json.loads(path.read_text())
        review = json.loads((WORK / f'narrative-review-{shard}.json').read_text())
        assert review['narrative_sha256'] == digest(path), shard
        assert review['reviewer'] != narrative['author'], shard
        assert review['status'] in ['passed','passed_with_notes'], shard
        assert review['reviewed_fields'] == narrative['coverage'], shard
        assert not set(chapters) & set(narrative['sections'])
        chapters.update(narrative['sections'])
        coverage.extend(narrative['coverage'])
        notes.extend(narrative.get('notes',[]))
    expected = {(s['id'],f['field_id']) for s in source['sections'] for f in s['fields']}
    actual = [(c['section'],str(c['field_id'])) for c in coverage]
    assert len(actual) == len(set(actual)) == 243 and set(actual) == expected
    for s in source['sections']:
        text = chapters[s['id']]
        for f in s['fields']:
            assert re.search(r'`@?' + re.escape(f['name'].lstrip('@')) + r'`',text), (s['id'],f['name'])
    snippets, snippet_manifest = xml_examples()
    opening = guide['opening'].replace('### 先读参考产品，再读电力输入',snippets+'\n### 先读参考产品，再读电力输入')
    opening = opening.replace('## 三、先用 demo 走通一次读取过程','## 三、先用 demo 走通一次读取过程\n\n[下载 demo、提取脚本及使用说明 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后即可按第五节运行。')
    article = [opening.strip(), '']
    for number, (title, types) in enumerate(GROUPS,1):
        article += [f'### 4.{number} {title}', '']
        for sid in types:
            text = re.sub(r'(?m)^### ', '#### ',chapters[sid].strip())
            # Give the chapter a stable, namespace-aware destination for review links.
            lines = text.splitlines()
            if lines[0].startswith('#### '):
                lines[0] += f' <a href="#read-{sid}" id="read-{sid}"></a>'
            article += ['\n'.join(lines), '']
    practice = guide['practice'].replace('### 按你的问题筛选数据',query_text+'\n\n### 按你的问题筛选数据')
    practice = practice.replace('本文配套的教程审阅记录','[本文配套的教程审阅记录](tutorial-review.md)')
    article += [practice.strip(), '']
    appendix = tables(source,translations)
    for lang, mapping in [('中文',translations),('English 原文',source['blocks'])]:
        article += ['{% tabs %}' if lang=='中文' else '',f'{{% tab title="{lang}" %}}', '']
        for key in source['overview_blocks']:
            value = escape(mapping[key]).replace('\r\n','\n')
            article += [value, '']
        article += ['{% endtab %}', '']
    article += ['{% endtabs %}', '', appendix, '']
    text = '\n'.join(article).replace('\r\n','\n').replace('\r','\n').rstrip()+'\n'
    (OUT / 'README.md').write_text(text)
    (OUT / 'attachments').mkdir(exist_ok=True)
    overview_zh = '\n'.join(f'<p>{escape(translations[k])}</p>' for k in source['overview_blocks'])
    table_html = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ecoSpold2 原始格式表中文翻译</title>
<style>body{{font:16px/1.7 system-ui,sans-serif;color:#16352d;margin:0}}main{{padding:32px;max-width:1800px;margin:auto}}h1,h2,h3{{line-height:1.3}}a{{color:#087760}}.table-scroll{{overflow:auto;margin:24px 0;border:1px solid #cdded6;border-radius:8px}}table{{border-collapse:collapse;width:100%;min-width:1100px}}th,td{{text-align:left;vertical-align:top;padding:10px;border:1px solid #d9e4de;overflow-wrap:anywhere}}th{{background:#e0f2e9;position:sticky;top:0}}tr[data-field-id]{{background:#f2f7f4;font-weight:600}}td[colspan]{{font-weight:400}}nav{{display:flex;flex-wrap:wrap;gap:14px}}.notice{{padding:16px;background:#f6f5e9;border-left:4px solid #a39c46}}@media print{{main{{padding:0}}table{{min-width:0;font-size:9pt}}.table-scroll{{overflow:visible}}}}</style>
</head><body><main><h1>ecoSpold2 原始格式表中文翻译</h1>
<p>来源：官方 EcoSpold02.html，格式包 v1.0.13 / XSD version 2.0.13。完整翻译 22 个分组、243 条字段；保留十列结构和说明行。</p>
<p class="notice">先读完整教程了解读法与取数口径，再用本表核对字段。原表的必填、重复、取值标记忠实保留；原文疑点见审校记录，模式实现应查 XSD。</p>
<nav><a href="https://hiqlcd.gitbook.io/hiqlcd-docs/ecospold2-xml-zi-duan-can-kao/ecospold2">完整中文教程</a><a href="https://hiqlcd.gitbook.io/hiqlcd-docs/ecospold2-xml-zi-duan-can-kao/ecospold2/translation-review">字段审校记录</a><a href="../original/Format%20description/EcoSpold02.html">英文原件</a></nav>
{overview_zh}
{appendix.replace('<table class="format-table">','<div class="table-scroll"><table class="format-table">').replace('</table>','</table></div>')}
<p>这是非官方中文参考译表，原始格式的权利归相应权利人所有。英文原件与所附模式保留在原始下载包中。</p>
</main></body></html>'''
    (OUT / 'attachments/EcoSpold02.zh.html').write_text(table_html.replace('\r\n','\n'))
    audit_page = ['# 完整教程的编写与运行审阅', '',
        '本教程将字段参考改写为连续的中文文章，覆盖主 HTML 的 **22 个分组、243 条字段**。三组叙述分别由另一位 AI 逐段审核，导读、实践代码和提取器也有独立审阅记录。明确的写作错误已修正；原文与模式的具体差异保留在正文及下方清单中。', '',
        '三份 demo 是教学构造数据，已按原包 XSD 验证。提取器和查询例子通过实际运行及回归检查：读取电力、环境水、正负直接排放、供应候选和模拟 LCIA 指标；还检查了命名空间、多数据集、继承、缺失值、参考量异常、语言回退，以及跨模型和发布版本的候选。验证脚本位于仓库 `tools/test_ecospold_tutorial.py`。', '',
        '数值练习中的方法与系数均是教学约定。测试不会为这些数值提供 ecoinvent 认证、清单完整性认证或真实 LCIA 方法认证；它确认文中程序与所给 demo 的行为一致。', '',
        f'本页保留 **{len(notes)} 条教程编写注记**，包括已修正问题、模式限定和需数据方进一步澄清的源文问题。它们与原字段参考的 27 条记录有范围重叠，不能相加为独立问题数量。原逐块翻译记录仍见[字段翻译与审校记录](translation-review.md)。', '',
        '## 教程注记', '']
    for index,note in enumerate(notes,1):
        sid = note.get('section') or note.get('block','').split('.')[0]
        fid = note.get('field_id') or (note.get('block','').split('.')[1] if '.' in note.get('block','') else '')
        status = '待专家复核' if note.get('status') == 'needs_expert_review' else '已处理／已说明'
        audit_page += [f'### {index}. {status} · {sid} {fid}', '',
            f'相关正文：[{TITLES.get(sid,sid)}](README.md#read-{sid})', '',
            note.get('reason_zh',note.get('reason','')), '',note.get('recommendation_zh',''), '']
    write_review = '\n'.join(audit_page).rstrip()+'\n'
    (OUT / 'tutorial-review.md').write_text(write_review)
    demo_dir = OUT / 'demo'
    with zipfile.ZipFile(demo_dir / 'ecospold2-tutorial-demo.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(demo_dir.iterdir()):
            if path.suffix in ['.spold','.py','.txt','.json']:
                item = zipfile.ZipInfo(path.name,date_time=(2026,10,14,0,0,0))
                item.compress_type = zipfile.ZIP_DEFLATED
                item.external_attr = 0o644 << 16
                z.writestr(item,path.read_bytes())
    summary_path = ROOT / 'content/SUMMARY.md'
    summary = summary_path.read_text().replace('[字段参考概览](ecospold2/README.md)','[完整教程：读懂 XML 并提取数据](ecospold2/README.md)')
    needle = '  - [字段翻译与审校记录](ecospold2/translation-review.md)'
    if 'ecospold2/tutorial-review.md' not in summary:
        summary = summary.replace(needle,'  - [完整教程的编写与运行审阅](ecospold2/tutorial-review.md)\n'+needle)
    summary_path.write_text(summary)
    output_paths = [OUT / 'README.md',OUT / 'tutorial-review.md',OUT / 'attachments/EcoSpold02.zh.html'] + [p for p in demo_dir.iterdir() if p.is_file()]
    manifest = {'scope':'A continuous Chinese tutorial, complete 243-field narrative, runnable synthetic demo and faithful original-table translation',
                'coverage':coverage,'notes':notes,'source_blocks':len(source['blocks']),
                'source_html_sha256':source['source_sha256'],'xml_snippets':snippet_manifest,
                'outputs':[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in sorted(output_paths)],
                'review_files':[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in sorted(WORK.glob('*review*.json'))]}
    (WORK / 'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'narrative_fields':len(coverage),'characters':len(text),'article_bytes':len(text.encode()),'translated_tables':22},ensure_ascii=False))
    return manifest

if __name__ == '__main__':
    build_content()
