"""Publish reviewed XML examples and concrete paths for all 243 official fields."""
import hashlib
import json
import html
import re
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'content/ecospold2'
WORK=ROOT/'audit/ecospold2/tutorial'
NS_URI='http://www.EcoInvent.org/EcoSpold02'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def packets(require_reviews=True):
    sections={}
    for shard in 'abc':
        path=WORK/f'xml-examples-{shard}.json'
        packet=json.loads(path.read_text())
        if require_reviews:
            review=json.loads((WORK/f'xml-examples-review-{shard}.json').read_text())
            assert review['packet_sha256']==sha(path)
            assert review['reviewer']!=packet['author']
            assert review['status'] in ['passed','passed_with_notes']
            expected={(sid,str(f['field_id'])) for sid,s in packet['sections'].items() for f in s['walkthrough']}
            checked={(f['section'],str(f['field_id'])) for f in review['reviewed_fields']}
            assert checked==expected
        for sid,value in packet['sections'].items():
            assert sid not in sections
            sections[sid]=value
    return sections

def markdown_prose(text):
    # Preserve literal XML names in prose; leave existing inline code untouched.
    parts=re.split(r'(`[^`]*`)',text)
    return ''.join(part if index%2 else html.escape(part,quote=False) for index,part in enumerate(parts))

def path_for(field):
    return '/'.join(field['schema']['nested']+[field['name']])

def render_section(sid, slug, section, official, locations):
    directory=BASE/'xml-examples'
    directory.mkdir(exist_ok=True)
    out=['## 对照 XML 找到每个字段','',
         '以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。','']
    records=[]
    for index,example in enumerate(section['examples'],1):
        filename=f'{slug}-{index:02d}.xml'
        xml=example['xml'].strip()+'\n'
        (directory/filename).write_text(xml)
        out += [f'### 示例 {index}：{example["label_zh"]}','',
                f'[下载本段 XML](xml-examples/{filename})。','',
                '```xml',xml.rstrip(),'```','',markdown_prose(example['explanation_zh']),'']
        records.append({'filename':filename,'xml_sha256':sha(directory/filename)})
    out += ['### 顺着示例读取字段','',
            '下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。','']
    explanations={str(e['field_id']):e['explanation_zh'] for e in section['walkthrough']}
    fields={}
    for field in official['fields']:
        fid=field['field_id']
        path=path_for(field)
        fields[fid]=path
        out += [f'**`{path}`（FieldID {fid}）**：'+markdown_prose(explanations[fid]),'']
    out += ['### 按相同路径提取自己的字段','',
            '下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。','',
            '```python','import json','import xml.etree.ElementTree as ET','from read_xml_fields import field_values','',
            f'node = ET.parse("xml-examples/{slug}-01.xml").getroot()',
            'FIELDS = {']
    out += [f'    "{fid}": "{path}",' for fid,path in fields.items()]
    out += ['}','for field_id, relative_path in FIELDS.items():',
            '    values = field_values(node, relative_path)',
            '    print(field_id, relative_path, json.dumps(values, ensure_ascii=False))','```','',
            '换成完整 `.spold` 文件时，先使用本章定位路径选出目标节点，再把它作为 `node` 传入。例如属性 `@amount` 最终用 `.get("amount")` 读取；子元素 `unitName` 用带命名空间的 `.findall("es:unitName", ns)` 读取。嵌套路径先进入对应子元素，再取最后的属性；如 `lognormal/@variance`，不能在外层 `uncertainty` 上直接取 `variance`。复合类型的子元素不能只读外层 `.text`，其结构已保留在返回记录的 `xml` 中。','']
    xpath_locations=['/'.join('es:'+p if p not in ('.','') else p for p in path.split('/')) for path in locations]
    filename='demo-lcia.spold' if sid=='TImpactIndicatorResult' else 'demo-product.spold'
    out += ['### 直接在完整 spold 中使用这些路径','',
            '沿用上一段的 `FIELDS` 字典与 `field_values`，下面改从完整文件选取本类型节点。先用配套 demo 运行，再把文件名改为自己的 `.spold`。XML 查找会返回全部同类节点；可选结构未提供时，匹配数为零，不会被填成数值零。多个路径代表同类型的不同使用位置，统计时按父路径区分。','',
            '```python','from read_section import load_dataset, NS','',
            f'dataset = load_dataset("{filename}", index=0)',
            'LOCATIONS = '+repr(xpath_locations),
            'for location in LOCATIONS:',
            '    nodes = dataset.findall(location, NS)',
            '    print("父路径：", location, "匹配数：", len(nodes))',
            '    for node in nodes:',
            '        for field_id, relative_path in FIELDS.items():',
            '            print(field_id, relative_path,',
            '                  json.dumps(field_values(node, relative_path), ensure_ascii=False))',
            '```','']
    return '\n'.join(out), {'section':sid,'field_paths':fields,'examples':records}

def publish_readme():
    (BASE/'demo/XML-examples-README.txt').write_text('''ecoSpold2 逐章 XML 教学片段

本说明对应独立的 ecospold2-xml-examples.zip，包中包含 xml-examples/、两份字段读取脚本和三份完整教学 .spold。如当前目录没有 xml-examples/，请从 GitBook 各字段章节下载“XML 片段与读取代码 ZIP”。

xml-examples/*.xml 覆盖22种官方类型及243条字段，均为构造的教学数据，不是ecoinvent数据库记录。示例分开显示输入/输出、继承删除标记和8种互斥的不确定性分布。每份片段可用ElementTree独立解析，但它不是完整.spold文件，也没有提供有效的真实主数据引用或完整父链。

read_xml_fields.py 的 field_values(node, relative_path) 读取章节中的路径，例如 @amount、unitName、lognormal/@variance。属性返回原始字符串列表；元素返回包含attributes/text/xml的记录列表。缺失返回[]，不应用默认值、不转换单位、不执行公式、不作归一化或LCA计算。

在此目录运行GitBook每章的提取代码；保持xml-examples子目录。完整.spold应先按本章父级路径选择节点，再传给field_values。名称为es的前缀只是程序中定义的命名空间别名，必须绑定http://www.EcoInvent.org/EcoSpold02。

各片段按官方XSD对应类型进行了结构校验。这里是类型级校验，不覆盖完整文件的父级关系、身份约束、外部主数据或继承语义。查询整份数据集与数量归一化可另从 GitBook“提取与查询实践”下载 ecospold2-tutorial-demo.zip；该完整 demo 包才包含 extract_ecospold.py、query_demo.py 和相应 README.txt。本 XML 片段包不包含这三份文件，主要用于逐字段阅读和定位；不要把类型片段目录作为完整数据集目录交给导出器扫描。
''')
