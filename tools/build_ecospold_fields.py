"""Publish reviewed, complete EcoSpold02.html translations as GitBook chapters."""
import hashlib
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT if (ROOT / 'content/.gitbook.yaml').exists() else ROOT / 'ecoinvent-gitbook'
CONTENT = REPO / 'content'
OUT = CONTENT / 'ecospold2'
AUDIT = REPO / 'audit/ecospold2'
WORK = AUDIT if ROOT == REPO else ROOT / 'translation-work/ecospold-fields'
SOURCE_DIR = OUT / 'original' if ROOT == REPO else ROOT / 'translation-work/reference/ecospold2-v1.0.13'
SOURCE = json.loads((WORK / 'source.json').read_text())
BLOCKS = SOURCE['blocks']
CONFIG = [
 ('activity-description', '活动描述', [
  ('TActivity', 'activity', '活动', 'activityDescription/activity'),
  ('TClassification', 'classification', '活动分类', 'activityDescription/classification'),
  ('TGeography', 'geography', '地理区域', 'activityDescription/geography'),
  ('TTechnology', 'technology', '技术', 'activityDescription/technology'),
  ('TTimePeriod', 'time-period', '时间范围', 'activityDescription/timePeriod'),
  ('TMacroEconomicScenario', 'macro-economic-scenario', '宏观经济情景', 'activityDescription/macroEconomicScenario')]),
 ('flow-data', '交换数据与结果', [
  ('TCustomExchange', 'exchanges', '交换的通用字段', 'flowData/{intermediateExchange|elementaryExchange}'),
  ('TIntermediateExchange', 'intermediate-exchanges', '中间交换专用字段', 'flowData/intermediateExchange'),
  ('TElementaryExchange', 'elementary-exchanges', '基本流交换专用字段', 'flowData/elementaryExchange'),
  ('TParameter', 'parameters', '参数', 'flowData/parameter'),
  ('TImpactIndicatorResult', 'impact-indicators', '影响指标结果', 'flowData/impactIndicator')]),
 ('complex-types', '复合类型', [
  ('TCompartment', 'compartments', '区室与子区室', '…/elementaryExchange/compartment'),
  ('TUncertainty', 'uncertainty', '不确定性与分布参数', '…/uncertainty'),
  ('TProperty', 'properties', '交换属性', '…/property'),
  ('TTransferCoefficient', 'transfer-coefficients', '转移系数', '…/transferCoefficient'),
  ('TTextAndImage', 'text-and-image', '文本、图像与文本变量', '…/generalComment、…/comment 等 TTextAndImage 字段')]),
 ('modelling-validation', '建模与审查', [
  ('TRepresentativeness', 'representativeness', '代表性', 'modellingAndValidation/representativeness'),
  ('TReview', 'review', '审查', 'modellingAndValidation/review')]),
 ('administrative-information', '管理信息', [
  ('TDataEntryBy', 'data-entry', '数据录入者', 'administrativeInformation/dataEntryBy'),
  ('TDataGeneratorAndPublication', 'publication', '数据生成者与发布', 'administrativeInformation/dataGeneratorAndPublication'),
  ('TFileAttributes', 'file-attributes', '文件属性', 'administrativeInformation/fileAttributes'),
  ('TRequiredContextReference', 'required-contexts', '所需上下文引用', 'administrativeInformation/fileAttributes/requiredContext')])]
LOOKUP = {item[0]: item for _, _, items in CONFIG for item in items}
assert set(LOOKUP) == {s['id'] for s in SOURCE['sections']}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(name, text):
    (OUT / name).write_text(text.replace('\r\n', '\n').replace('\r', '\n').rstrip() + '\n')

def cell(value):
    return str(value).replace('|', '\\|').replace('\n', '<br>')

def yn(value, zh):
    return {'Yes': '是', 'No': '否'}.get(value, value) if zh else value

def code(value):
    return f'`{value}`' if value else '—'

def prose(value):
    # These inputs are plain text, not Markdown. Preserve literal formula syntax
    # and source numbering rather than allowing Markdown to reinterpret them.
    value = html.escape(value, quote=False)
    value = re.sub(r'([\\`*_\[\]])', r'\\\1', value)
    value = re.sub(r'(?m)^(\d+)([.)])(?=\s)', r'\1\\\2', value)
    return re.sub(r'(?m)^([#+-])(?=\s)', r'\\\1', value)

TRANSLATIONS = {}
NOTES = []
REVIEWS = []
for shard in 'abc':
    source = json.loads((WORK / f'source-{shard}.json').read_text())
    translation = json.loads((WORK / f'translation-{shard}.json').read_text())
    review = json.loads((WORK / f'review-{shard}.json').read_text())
    assert set(source['blocks']) == set(translation['blocks']), shard
    assert review['status'] in ['passed', 'passed_with_notes'], shard
    assert review['translation_sha256'] == sha(WORK / f'translation-{shard}.json'), shard
    assert set(review['reviewed_blocks']) == set(source['blocks']), shard
    assert not (set(TRANSLATIONS) & set(translation['blocks']))
    TRANSLATIONS.update(translation['blocks'])
    NOTES.extend(translation.get('notes', []))
    REVIEWS.append(review)
assert set(TRANSLATIONS) == set(BLOCKS)
assert all(isinstance(v, str) and v.strip() for v in TRANSLATIONS.values())
OUT.mkdir(exist_ok=True)
AUDIT.mkdir(parents=True, exist_ok=True)
if SOURCE_DIR.resolve() != (OUT / 'original').resolve():
    shutil.copytree(SOURCE_DIR, OUT / 'original', dirs_exist_ok=True)
    shutil.copy2(SOURCE_DIR.parent / 'documentation_on_ecospold2_format.v1.0.13.zip', OUT / 'original/documentation_on_ecospold2_format.v1.0.13.zip')
for shard in 'abc':
    for prefix in ['source', 'translation', 'review']:
        if WORK.resolve() != AUDIT.resolve():
            shutil.copy2(WORK / f'{prefix}-{shard}.json', AUDIT / f'{prefix}-{shard}.json')
if WORK.resolve() != AUDIT.resolve():
    shutil.copy2(WORK / 'source.json', AUDIT / 'source.json')

def schema_note(field, zh):
    s = field['schema']
    if field['name'].startswith('@'):
        spec = f'`use="{s["use"] or "optional"}"`'
        if s['use'] is None:
            spec += '（XSD 默认值）' if zh else ' (XSD default)'
    else:
        spec = f'`minOccurs="{s["minOccurs"] or "1"}"`，`maxOccurs="{s["maxOccurs"] or "1"}"`'
        if not s['minOccurs'] or not s['maxOccurs']:
            spec += '（未显式声明的值按 XSD 默认值列出）' if zh else ' (undeclared values use XSD defaults)'
    if s['default'] is not None:
        spec += f'；`default="{s["default"]}"`'
    if s['choice']:
        spec += '。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断' if zh else '. This field is within an xsd:choice branch; interpret occurrence in its parent structure'
    return spec

records = []
for section in SOURCE['sections']:
    sid = section['id']
    _, slug, title, location = LOOKUP[sid]
    page = [f'# {title}（{sid}）', '',
            f'源文分组：{section["title_en"]}。本章完整收录 **{len(section["fields"])} 条字段定义**。', '',
            f'XML 位置：`{location}`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。', '',
            '[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)', '',
            '> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。', '']
    relevant_notes = [n for n in NOTES if n['block'].startswith(sid + '.')]
    if any(n['status'] == 'needs_expert_review' for n in relevant_notes):
        page += ['{% hint style="warning" %}', '本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。', '{% endhint %}', '']
    page += ['{% tabs %}', '']
    for lang, text_map in [('中文', TRANSLATIONS), ('English 原文', BLOCKS)]:
        zh = lang == '中文'
        page += [f'{{% tab title="{lang}" %}}', '', f'## {"结构说明" if zh else "Structure"}', '']
        occurrence = section['occurrence']
        page += [f'{"分组可重复" if zh else "Group multiple occurrences"}：{yn(occurrence[1], zh)}；{"分组必填" if zh else "Group required"}：{yn(occurrence[3], zh)}。', '']
        for key in section['intro_blocks']:
            page += [prose(text_map[key]), '']
        if sid == 'TUncertainty':
            page += [('**XSD 阅读提示：** 每个 `uncertainty` 元素在 `lognormal`、`normal`、`triangular`、`uniform`、`beta`、`gamma`、`binomial`、`undefined` 中恰选一种分布。以下属性所属的分布由“局部 XML 位置”区分；`pedigreeMatrix` 是独立的可选元素。'
                      if zh else '**XSD reading note:** Each uncertainty element selects exactly one of lognormal, normal, triangular, uniform, beta, gamma, binomial, or undefined. Local XML paths distinguish distribution-specific attributes; pedigreeMatrix is a separate optional element.'), '']
        if sid in ['TIntermediateExchange', 'TElementaryExchange']:
            page += [('**继承关系：** 本章仅列专用字段；完整交换结构还包含[交换的通用字段](exchanges.md)。' if zh else '**Inheritance:** These are additional fields; the complete exchange also includes [common exchange fields](exchanges.md).'), '']
        for f in section['fields']:
            fid = f['field_id']
            anchor = f'field-{fid}' if zh else f'en-field-{fid}'
            s = f['schema']
            local = '/'.join([sid] + s['nested'] + [f['name']])
            page += [f'### `{f["name"]}` · FieldID {fid} <a href="#{anchor}" id="{anchor}"></a>', '',
                     f'{"局部 XML 位置" if zh else "Local XML path"}：`{local}`；{"ecoSpold1 对照编号" if zh else "ecoSpold1 mapping"}：{code(f["spold1_id"])}。', '',
                     '| ' + ('类型 | 必填 | 可重复' if zh else 'Type | Required | Multiple occurrence') + ' |',
                     '| --- | --- | --- |',
                     '| ' + ' | '.join(cell(v) for v in [code(f['type']), yn(f['required'], zh), yn(f['multiple'], zh)]) + ' |', '',
                     f'{"长度" if zh else "Size"}：{f["size"] or "—"}；{"多语言" if zh else "Multi language"}：{yn(f["multilingual"], zh)}；{"主数据冗余字段" if zh else "Redundant master data"}：{yn(f["redundant_master_data"], zh)}。', '']
            for key in f['description_blocks']:
                page += [prose(text_map[key]), '']
            if f.get('options_block'):
                page += [f'**{"取值选项（原表）" if zh else "Options (original table)"}：** {prose(text_map[f["options_block"]])}', '']
            if f['type'] in LOOKUP:
                target = LOOKUP[f['type']]
                page += [f'{"复合类型详情" if zh else "Complex type details"}：[ `{f["type"]}` ]({target[1]}.md)。', '']
            page += [f'**{"XSD 结构约束" if zh else "XSD structural constraints"}：** {schema_note(f, zh)}。', '',
                     f'{"模式出处" if zh else "Schema source"}：[{s["file"]}](original/Schemas/datasets/{s["file"]})，`{s["owner"]}`。', '']
            if zh:
                records.append({'section': sid, 'name': f['name'], 'field_id': fid, 'local_path': local,
                                'page': f'ecospold2/{slug}.md', 'anchor': anchor, 'metadata': {k: f[k] for k in ['type','size','required','multiple','multilingual','redundant_master_data','spold1_id']},
                                'source_blocks': f['description_blocks'] + ([f['options_block']] if f.get('options_block') else [])})
        page += ['{% endtab %}', '']
    page += ['{% endtabs %}', '']
    if relevant_notes:
        page += ['## 翻译与审校注记', '']
        for n in relevant_notes:
            tag = '待专家复核' if n['status'] == 'needs_expert_review' else '已处理／已说明'
            page += [f'- **{tag} · `{n["block"]}`**：{n["reason_zh"]} {n.get("recommendation_zh", "")}', '']
    write(f'{slug}.md', '\n'.join(page))

overview = ['# ecoSpold2 XML 字段参考', '',
 '本部分将官方 `Format description/EcoSpold02.html` 拆分为 **22 个字段章节、243 条字段定义**，按 XML 结构组织。每条保留字段名、FieldID、ecoSpold1 对照编号、数据类型、长度、必填性、重复性、多语言和主数据冗余标记，以及完整的说明和取值选项。中文与英文可切换核对。', '',
 f'来源：[ecoinvent 官方 ecoSpold2 页面](https://support.ecoinvent.org/ecospold2) · [官方格式包]({SOURCE["source_url"]}) · [原件 ZIP](original/documentation_on_ecospold2_format.v1.0.13.zip)', '',
 '格式包文件名版本为 **v1.0.13**，所附 XSD 的 `version` 为 **2.0.13**。这是该格式包的参考译本；应以实际数据文件对应的模式版本校验，不把历史格式说明视为所有新版本的完整规范。', '',
 '## 如何查字段', '',
 '1. 已知字段名：打开[字段索引](field-index.md)，搜索 `@amount`、`activityLinkId` 或 FieldID。',
 '2. 正在阅读 XML：按父元素选择活动、交换、参数或管理信息章节；同名属性在不同结构下可能有不同含义。',
 '3. 正在开发导入器：先看[阅读约定与 XSD 约束](reading-guide.md)，再结合每条的 XSD 出处检查。', '',
 '## 按 XML 结构阅读', '']
for group_slug, group_title, items in CONFIG:
    overview += [f'- [{group_title}]({group_slug}.md)：' + '、'.join(x[2] for x in items) + '。']
overview += ['', '## 原文的阅读说明', '', '{% tabs %}', '']
for lang, text_map in [('中文', TRANSLATIONS), ('English 原文', BLOCKS)]:
    overview += [f'{{% tab title="{lang}" %}}', '']
    for k in SOURCE['overview_blocks']:
        overview += [prose(text_map[k]), '']
    overview += ['{% endtab %}', '']
overview += ['{% endtabs %}', '',
 '**范围说明：** 243 条是主数据集格式 HTML 中的全部字段条目，不是整个 XSD 包中全部节点的数量。主数据文件和基础类型的额外定义保留在原包中，入口见[阅读指南](reading-guide.md)。', '',
 '译稿完成 AI 自审和独立 AI 交叉审阅；校验覆盖源文块、字段元数据、链接和原件哈希。具体原文疑点、已修正问题见[本部分审校记录](translation-review.md)，不代表人工专家签核或 ecoinvent 官方认证。']
write('README.md', '\n'.join(overview))

for group_slug, group_title, items in CONFIG:
    text = [f'# {group_title}', '', '本组按官方 XML 结构组织。字段章节同时保留中文说明与英文原文。', '',
            '| 字段章节 | 模式类型 | 字段条目数 |', '| --- | --- | --- |']
    for sid, slug, title, _ in items:
        count = next(len(s['fields']) for s in SOURCE['sections'] if s['id'] == sid)
        text += [f'| [{title}]({slug}.md) | `{sid}` | {count} |']
    if group_slug == 'flow-data':
        text += ['', '中间交换与基本流交换继承 `TCustomExchange`。查看其中一种交换时，请同时阅读通用字段和该交换的专用字段。']
    text += ['', '[全部字段索引](field-index.md) · [阅读约定与 XSD 约束](reading-guide.md)']
    write(group_slug + '.md', '\n'.join(text))

index = ['# 全部字段索引', '', '共 **243 条字段定义**。按字段名排序；同名属性通过局部路径和 FieldID 区分。`@` 表示 XML 属性，不是实际名称的一部分；路径首段 `T…` 为所属模式类型，不是 XML 标签。', '',
         '| 字段 | 所属局部路径 | FieldID | 章节 |', '| --- | --- | --- | --- |']
for r in sorted(records, key=lambda r: (r['name'].lstrip('@').lower(), r['section'], int(r['field_id']))):
    slug = LOOKUP[r['section']][1]
    index += [f'| [`{r["name"]}`]({slug}.md#{r["anchor"]}) | `{cell(r["local_path"])}` | {r["field_id"]} | {LOOKUP[r["section"]][2]} |']
write('field-index.md', '\n'.join(index))

guide = '''# 阅读约定与 XSD 约束

## 字段名、路径与 FieldID

`@amount` 表示 XML 属性 `amount="…"`；没有 `@` 的名称表示子元素。章节中 `TActivity`、`TUncertainty` 等是 XSD 类型名，不是 XML 标签。FieldID 是格式规范的字段编号，不是活动、交换或主数据条目的 UUID。

每条的“局部 XML 位置”从所属模式类型开始。嵌套属性会保留父元素，例如 `TUncertainty/lognormal/@meanValue` 与 `TUncertainty/normal/@meanValue` 含义不同。正文开头另给出在数据集中的位置；`…` 表示可在多个位置复用的结构。

## 数据集的顶层结构

以下为所附 XSD 的结构导读，省略了属性和内部子元素，不是一份可直接通过模式校验的数据集：

```text
ecoSpold
├── activityDataset
│   ├── activityDescription
│   ├── flowData
│   ├── modellingAndValidation
│   └── administrativeInformation
└── childActivityDataset（另一种可选数据集分支）
```

根模式允许多个数据集；`activityDataset` 与 `childActivityDataset` 在 `xsd:choice` 中选择。两个容器元素都属于 `http://www.EcoInvent.org/EcoSpold02` 命名空间。`activityDataset` 使用该命名空间的 `TActivityDataset` 类型；`childActivityDataset` 使用 `http://www.EcoInvent.org/EcoSpold02Child` 命名空间的 `TActivityDataset` 类型，其内部子元素属于子数据集命名空间。容器元素的命名空间与其类型或内部元素的命名空间须分别判断。出处：[EcoSpold02.xsd](original/Schemas/datasets/EcoSpold02.xsd)、[EcoSpold02Activity.xsd](original/Schemas/datasets/EcoSpold02Activity.xsd)、[EcoSpold02ChildActivity.xsd](original/Schemas/datasets/EcoSpold02ChildActivity.xsd)。

## 如何理解原表的标记

| 标记 | 阅读方式 |
| --- | --- |
| 类型 Type | 保留官方类型名，例如 `TUuid`、`TFloatNumber`；具体定义见 XSD。 |
| 长度 Size | 忠实保留原表。`—` 表示原表未列出，不表示字段无约束。 |
| 必填 Req | 表示所属结构中的要求；还需判断父元素是否出现、选择了哪个分支以及是否为子数据集。 |
| 可重复 Multiple Occurrence | 保留原表的逻辑重复标记；序列化出现次数另列 XSD `minOccurs` / `maxOccurs`。 |
| 多语言 Multi Language | 表示支持多语言文本；部分文本通过多个带 `xml:lang` 的同名元素表示，不能只根据“可重复：否”拒绝这些元素。 |
| 主数据冗余 Redundant Master Data | 指原表标识的主数据冗余字段；名称、单位等可能随 UUID 引用一起存入数据集，不应自行删除。 |
| Options | 保留枚举值与说明的对应关系。正文说明还可能包含额外条件，不能只读枚举表。 |
| SpoldID, version 1 | 用于与 ecoSpold1 对照；`new`、`rename`、`type` 等变更标记保留原样，不是 XML 值。 |

## XSD 约束优先结合上下文解释

每条的“XSD 结构约束”来自同一原包中的元素或属性声明。XML 属性未写 `use` 时默认 `optional`；元素未写 `minOccurs` / `maxOccurs` 时默认均为 `1`。这些值只描述局部声明，不替代完整模式校验。

尤其需要注意 `xsd:choice`：一个 `uncertainty` 选择恰好一种分布，不要求同时包含所有分布。选择 `lognormal` 后，才判断其属性的必填要求。`TTextAndImage` 的选择组则允许多次出现，不能用同一规则理解所有选择组。父级次数、序列、继承、唯一性约束以及类型限制也需在 XSD 中核对。

多个“原表可重复：否”的多语言字段，在 XSD 中的 `maxOccurs` 是 `unbounded`；前者按原表保留，后者按序列化结构展示。若实现软件，应检查 `xml:lang` 的唯一性约束，而不是把不同语言的文本当作无条件重复数据。

## 基础类型、文本属性与完整模式

243 条字段来自 `EcoSpold02.html`。基础类型内部的属性或结构（例如文本的 `xml:lang`、排序用 `index`、文本变量名称）未必在主 HTML 中逐项列为 FieldID，因此还应查 [EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd) 与 [XmlNamespace.xsd](original/Schemas/XmlNamespace.xsd)。本部分没有把主 HTML 的条目数称为整个模式的全部节点数量。

活动描述、建模和管理信息：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)。交换、参数与影响指标：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)。继承型子数据集须查原包中的 `EcoSpold02Child*.xsd`，不能直接套用正常数据集的全部必填要求。

## 主数据文件的字段说明

本次中文逐字段译稿覆盖用户指定的 `EcoSpold02.html`。原包中的以下主数据 HTML 保留英文原件，可用于查 UUID 引用的目标字段：
'''
for path in sorted((SOURCE_DIR / 'Format description').glob('*.html')):
    if path.name != 'EcoSpold02.html':
        guide += f'\n- [{path.stem}](original/Format%20description/{path.name})'
guide += '\n\n[下载完整官方原包](original/documentation_on_ecospold2_format.v1.0.13.zip) · [字段索引](field-index.md) · [审校记录](translation-review.md)\n'
write('reading-guide.md', guide)

review_text = ['# ecoSpold2 字段翻译与审校记录', '',
 f'完整翻译 **22 个分组、243 条字段、{len(BLOCKS)} 个源文块**。三位 AI 译者分组翻译，再由另一位 AI 独立交叉审校。字段元数据原样导出并与原 HTML 对照；每条同时关联同包 XSD 的 FieldID、字段名和所属类型。', '',
 '格式包 v1.0.13 / XSD version 2.0.13。保留原件、SHA-256、逐块中文与英文、审阅记录；本记录不代表人工专家签核或 ecoinvent 官方认证。', '',
 f'本部分共有 **{len(NOTES)} 条审校注记**，其中 **{sum(n["status"] == "needs_expert_review" for n in NOTES)} 条待专家复核**。与原支持文档的 170 条记录分开计数，避免混淆两次翻译范围。', '',
 '## 注记清单', '']
for i, n in enumerate(NOTES, 1):
    parts = n['block'].split('.')
    target = LOOKUP.get(parts[0])
    if target:
        fragment = f'#field-{parts[1]}' if parts[1].isdigit() else ''
        link = f'[{target[2]}]({target[1]}.md{fragment})'
    else:
        link = '[原文阅读说明](README.md)'
    tag = '待专家复核' if n['status'] == 'needs_expert_review' else '已处理／已说明'
    review_text += [f'### {i}. {tag} · `{n["block"]}`', '', f'相关章节：{link}', '',
                   f'**原文：** {prose(BLOCKS[n["block"]])}', '', f'**译文：** {prose(TRANSLATIONS[n["block"]])}', '',
                   f'**说明：** {n["reason_zh"]}', '', f'**处理建议：** {n.get("recommendation_zh", "见说明。")}', '']
write('translation-review.md', '\n'.join(review_text))

nav = ['## ecoSpold2 XML 字段参考', '', '- [字段参考概览](ecospold2/README.md)',
       '  - [阅读约定与 XSD 约束](ecospold2/reading-guide.md)', '  - [全部字段索引](ecospold2/field-index.md)']
for group_slug, group_title, items in CONFIG:
    nav += [f'  - [{group_title}](ecospold2/{group_slug}.md)']
    nav += [f'    - [{title}](ecospold2/{slug}.md)' for _, slug, title, _ in items]
nav += ['  - [字段翻译与审校记录](ecospold2/translation-review.md)', '']
summary = (CONTENT / 'SUMMARY.md').read_text()
summary = re.sub(r'## ecoSpold2 XML 字段参考\n.*?(?=## 参考与审核)', '', summary, flags=re.S)
summary = summary.replace('## 参考与审核', '\n'.join(nav) + '\n## 参考与审核')
(CONTENT / 'SUMMARY.md').write_text(summary)

manifest = {'source_sha256': SOURCE['source_sha256'], 'package_sha256': sha(OUT / 'original/documentation_on_ecospold2_format.v1.0.13.zip'),
            'source_file': SOURCE['source_file'], 'source_url': SOURCE['source_url'],
            'sections': len(SOURCE['sections']), 'fields': records, 'source_blocks': len(BLOCKS),
            'notes': NOTES, 'reviews': REVIEWS,
            'pages': [{'path': p.relative_to(CONTENT).as_posix(), 'sha256': sha(p)} for p in sorted(OUT.glob('*.md'))],
            'original_files': [{'path': p.relative_to(CONTENT).as_posix(), 'sha256': sha(p)} for p in sorted((OUT / 'original').rglob('*')) if p.is_file()]}
(AUDIT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'pages': len(manifest['pages']), 'fields': len(records), 'source_blocks': len(BLOCKS), 'notes': len(NOTES)}, ensure_ascii=False, indent=2))
