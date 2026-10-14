"""Compose the reviewed narrative tutorial and its faithful Chinese HTML appendix."""
import hashlib
import html
import json
from pathlib import Path
import re
import zipfile
import copy
import xml.etree.ElementTree as ET
import sys
from ecospold_layout import GROUPS as LAYOUT, CHAPTERS

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
        fragments.append(f'<h3><a href="#appendix-{sid.lower()}" id="appendix-{sid.lower()}"></a>{TITLES[sid]}（{sid}）</h3>')
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
    # Publish one reading route and replace old bilingual cards with narrative chapters.
    def chunk(text, heading, next_heading=None):
        start = text.index(heading)
        end = text.index(next_heading,start) if next_heading else len(text)
        return text[start:end].strip()
    guide_title = '首先确定文件里的量属于哪个层级'
    opening_parts = re.split(r'(?m)^## ',opening)
    introduction = opening_parts[0].replace('# 读懂一份 ecoSpold2 文件：从 XML 结构到所需数据','# 完整教程：读懂 XML 并提取数据')
    introduction = introduction.replace('正文采用连续讲解；需要核对类型、长度和必填标记时，可读文末的原始 HTML 格式表中文译表，或使用字段索引。', '各章按 XML 结构组织，以文章说明字段含义、使用场景和提取方法；最后的完整中文 HTML 译表用于逐项查询。')
    introduction = re.sub(r'，或使用\[字段索引\]\(field-index.md\)', '',introduction)
    introduction = re.sub(r'，或使用字段索引', '',introduction)
    introduction = introduction.replace('这篇文章','这套教程').replace('正文采用连续讲解；需要核对类型、长度和必填标记时，可读文末的原始 HTML 格式表中文译表。','各章采用文章讲解；需要核对类型、长度和必填标记时，可读最后的[完整中文格式译表](format-reference.md)。')
    def write_page(name,value):
        (OUT / name).write_text(value.replace('\r\n','\n').replace('\r','\n').rstrip()+'\n')
    write_page('data-levels.md','# 判断 UPR、LCI 与 LCIA\n\n'+opening_parts[1].split('\n',1)[1])
    write_page('xml-structure.md','# XML 结构、命名空间与继承\n\n'+opening_parts[2].split('\n',1)[1])
    demo_text = opening_parts[3].split('\n',1)[1].replace('按第五节运行','按[提取与查询实践](extraction-practice.md)运行')
    write_page('demo-walkthrough.md','# 用 demo 走通读取过程\n\n'+demo_text)
    introduction += '\n\n'+opening_parts[4].split('\n',1)[1].strip()+'\n'
    introduction += '\n\n## 按问题进入教程\n\n先读[判断 UPR、LCI 与 LCIA](data-levels.md)，确定数量的层级，再读[XML 结构、命名空间与继承](xml-structure.md)和[demo 读取演示](demo-walkthrough.md)。五组字段文章沿文件结构展开；[提取与查询实践](extraction-practice.md)提供完整代码和筛选方法。最后的[官方格式说明中文版本](format-reference.md)集中保留原始表格译文。\n\n'
    extraction = json.loads((WORK / 'chapter-extraction.json').read_text())
    sys.path.insert(0,str(OUT / 'demo'))
    from read_section import PATHS, load_dataset, read_section
    chapter_paths = []
    for group_slug,group_title,items in LAYOUT:
        group_body = [f'# {group_title}', '', '本组把相关 XML 结构分为下面的文章章节。每篇先解释字段及其相互关系，再说明使用和提取，最后对照教学 demo。', '']
        for sid,slug,title in items:
            group_body += [f'[{title}]({slug}.md)：'+chapters[sid].split('\n',1)[0].lstrip('# '), '']
            narrative = re.sub(r'(?m)^### ', '## ',chapters[sid].strip())
            narrative_lines = narrative.splitlines()
            narrative_lines[0] += f' <a href="#read-{sid.lower()}" id="read-{sid.lower()}"></a>'
            body = [f'# {title}', '', '对应官方格式类型：`'+sid+'`。本篇以文章解释该类型的 '+str(len(next(s for s in source['sections'] if s['id']==sid)['fields']))+' 条字段；复合类型也会说明它们依附在哪个对象上。', '', '\n'.join(narrative_lines), '', '## 怎样定位、使用与提取', '', extraction[sid]['use_zh'], '',
                    '定位路径相对于完整的 `/ecoSpold/activityDataset`：'+ '；'.join('`'+p+'`' for p in PATHS[sid])+'。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。', '',
                    '下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。', '',
                    '原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。', '',
                    '```python', 'import json', 'from read_section import load_dataset, read_section', '',
                    'dataset = load_dataset("'+('demo-lcia.spold' if sid=='TImpactIndicatorResult' else 'demo-product.spold')+'", index=0)',
                    'records = read_section(dataset, "'+sid+'")', 'print("匹配节点数：", len(records))', 'print(json.dumps(records[:2], ensure_ascii=False, indent=2))', '```', '', '## 对照 demo 理解读取结果', '']
            filename = 'demo-lcia.spold' if sid=='TImpactIndicatorResult' else 'demo-product.spold'
            examples = read_section(load_dataset(OUT / 'demo' / filename),sid)
            if examples:
                first = examples[0]
                excerpt = {'path':first['path'],'attributes':first['attributes'], 'children_excerpt':[{'tag':n['tag'],'attributes':n['attributes'],'text':n['text']} for n in first['children'][:2]]}
                body += [f'在 `{filename}` 中实际匹配 **{len(examples)} 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。', '', '```json', json.dumps(excerpt,ensure_ascii=False,indent=2), '```', '']
                if sid=='TTextAndImage':
                    body += ['这里的外层说明节点可能没有属性，具体文字在 `children` 中的 `text` 节点；继续查看其子节点，而不要因为外层 `text` 是空白就认为说明不存在。', '']
                if sid=='TUncertainty':
                    body += ['外层不确定性节点通常没有分布参数属性，参数位于 `children` 中选中的分布节点。谱系矩阵是另一个子节点，应保留它与该分布的关系。', '']
            else:
                body += [f'`{filename}` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。', '']
            body += ['## 继续阅读', '', '[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-'+sid.lower()+')用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。', '']
            write_page(slug+'.md','\n'.join(body))
            chapter_paths.append(OUT / (slug+'.md'))
        write_page(group_slug+'.md','\n'.join(group_body))
        introduction += f'### {group_title}\n\n'+' · '.join(f'[{title}]({slug}.md)' for _,slug,title in items)+'\n\n'
    write_page('README.md',introduction)
    practice = guide['practice'].replace('### 按你的问题筛选数据',query_text+'\n\n### 按你的问题筛选数据')
    practice = practice.replace('本文配套的教程审阅记录','[本文配套的教程审阅记录](tutorial-review.md)')
    practice = practice.replace('本文解释这些字段','[不确定性章节](uncertainty.md)解释这些字段')
    extraction_practice = chunk(practice,'## 五、','## 六、').replace('## 五、用 Python 提取成可分析的数据','# 提取与查询实践')
    extraction_practice += '\n\n[先看 demo 的具体 XML 节点](demo-walkthrough.md) · [保留数据解释与追溯信息](provenance.md)\n'
    write_page('extraction-practice.md',extraction_practice)
    write_page('provenance.md',chunk(practice,'## 六、','## 附录：').replace('## 六、从“拿到一个数”走到“拿到可解释的数据”','# 保留数据解释与追溯信息'))
    appendix = tables(source,translations)
    appendix_text = [chunk(practice,'## 附录：').replace('## 附录：原始 HTML 格式表的中文翻译','# 附录：官方 EcoSpold02.html 中文版本'), '']
    appendix_text[0] = appendix_text[0].replace('前面的正文','各章正文')
    for key in source['overview_blocks']:
        appendix_text += [escape(translations[key]).replace('\r\n','\n'),'']
    appendix_text += [appendix,'']
    write_page('format-reference.md','\n'.join(appendix_text))
    for retired in ['field-index.md','reading-guide.md']:
        (OUT / retired).unlink(missing_ok=True)
    text = '\n'.join(p.read_text() for p in chapter_paths)
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
        '本轮按 XML 结构拆为五组 22 篇字段文章，替换独立表格翻译页。各章增加定位路径、使用说明与实际 demo 读取片段；`read_section.py` 只读取原始属性和节点树，不计算 LCI/LCIA，也不代替 XSD 或语义验证。新增的章节读取测试实际执行全部 22 段代码，并检查多语言、嵌套数量、负输出、缺失结构、多数据集与子数据集拒绝；与原 12 项提取器测试分别记录。', '',
        '## 教程注记', '']
    for index,note in enumerate(notes,1):
        sid = note.get('section') or note.get('block','').split('.')[0]
        fid = note.get('field_id') or (note.get('block','').split('.')[1] if '.' in note.get('block','') else '')
        status = '待专家复核' if note.get('status') == 'needs_expert_review' else '已处理／已说明'
        audit_page += [f'### {index}. {status} · {sid} {fid}', '',
            f'相关正文：[{TITLES.get(sid,sid)}]({CHAPTERS[sid][0]}.md#read-{sid.lower()})', '',
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
    nav = ['## ecoSpold2 XML 字段参考','','- [完整教程：读懂 XML 并提取数据](ecospold2/README.md)',
           '  - [判断 UPR、LCI 与 LCIA](ecospold2/data-levels.md)',
           '  - [XML 结构、命名空间与继承](ecospold2/xml-structure.md)',
           '  - [用 demo 走通读取过程](ecospold2/demo-walkthrough.md)']
    for group_slug,group_title,items in LAYOUT:
        nav += [f'  - [{group_title}](ecospold2/{group_slug}.md)']
        nav += [f'    - [{title}](ecospold2/{slug}.md)' for _,slug,title in items]
    nav += ['  - [提取与查询实践](ecospold2/extraction-practice.md)',
            '  - [保留数据解释与追溯信息](ecospold2/provenance.md)',
            '  - [完整教程的编写与运行审阅](ecospold2/tutorial-review.md)',
            '  - [字段翻译与审校记录](ecospold2/translation-review.md)',
            '  - [附录：官方 EcoSpold02.html 中文版本](ecospold2/format-reference.md)','']
    summary = re.sub(r'## ecoSpold2 XML 字段参考\n.*?(?=## 参考与审核)', '\n'.join(nav)+'\n',summary_path.read_text(),flags=re.S)
    summary_path.write_text(summary)
    # Replace legacy field-card anchors in historical review links with chapter targets.
    review_path = OUT / 'translation-review.md'
    review_path.write_text(re.sub(r'(\([^()]+\.md)#field-\d+(\))',r'\1\2',review_path.read_text()))
    output_paths = list(OUT.glob('*.md')) + [OUT / 'attachments/EcoSpold02.zh.html'] + [p for p in demo_dir.iterdir() if p.is_file()]
    manifest = {'scope':'A chaptered Chinese reading tutorial, 22 narrative field chapters, runnable synthetic demos and a single final translated-table appendix',
                'coverage':coverage,'notes':notes,'source_blocks':len(source['blocks']),
                'source_html_sha256':source['source_sha256'],'xml_snippets':snippet_manifest,
                'layout':'chaptered-narrative','chapter_pages':{sid:'ecospold2/'+slug+'.md' for sid,(slug,title) in CHAPTERS.items()},
                'appendix_page':'ecospold2/format-reference.md',
                'outputs':[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in sorted(output_paths)],
                'review_files':[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in sorted(WORK.glob('*review*.json'))]}
    (WORK / 'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'narrative_fields':len(coverage),'characters':len(text),'article_bytes':len(text.encode()),'translated_tables':22},ensure_ascii=False))
    return manifest

if __name__ == '__main__':
    build_content()
