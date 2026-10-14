# 活动分类

对应官方格式类型：`TClassification`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 用分类定位行业，不把名称当作主数据标识 <a href="#read-tclassification" id="read-tclassification"></a>

活动描述中的 `classification` 可重复出现，每一项采用 `TClassification`，把一个分类体系与其中的类别配对。元素 `classificationSystem` 给出体系名称，如原文示例 `ISIC Rev. 4`；`classificationValue` 给出活动在该体系中所属的类别。它们便于展示和筛选，但机器解析的主数据引用是属性 `classificationId`，指向有效分类列表中的分类值。`classificationContextId` 指定这个分类所属上下文，省略时采用数据集自身的上下文。取数时应逐项保留体系、类别和引用标识，不能假定只有一个分类，也不能将不同体系中看起来相同的类别文本合并为同一条主数据。

这里有一处需明确交代的原文差异：字段说明把 `classificationSystem` 和 `classificationValue` 称为可选纯文本值，而本版完整数据 XSD 将两个元素设为至少出现一次，官方 HTML 表格也标为必填。阅读已有文本与校验文件结构是不同操作；校验当前完整数据时应按所用 XSD 执行，不能根据说明中的“可选”自行删除元素。子数据集另有差异模式，其规则还需结合继承处理。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：分类值引用与两层可读名称

[下载本段 XML](xml-examples/classification-01.xml)。

```xml
<classification xmlns="http://www.EcoInvent.org/EcoSpold02" classificationId="45b127bf-078e-5df0-a5c0-fd6ee9a6b53e" classificationContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
  <!-- 教学构造的分类，不是正式ISIC或其他分类主数据。 -->
  <classificationSystem xml:lang="zh">教学分类体系</classificationSystem>
  <classificationValue xml:lang="zh">教学产品制造</classificationValue>
</classification>
```

classification 可以放在活动描述或相应交换的分类位置。这里给出完整的分类体系名称和分类值名称，并明确它们与 UUID 引用的区别；虚构 UUID 不表示它已经出现在真实 validClassifications 表中。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`classificationSystem`（FieldID 300）**：`classificationSystem` 子元素的文本“教学分类体系”说明所用分类体系。按命名空间及语言读取它，不能把它当成分类值 UUID；原文称文字可选，但普通 XSD 要求存在这一子元素，本片段按 XSD 补齐，仍保留源文与模式的差异。

**`classificationValue`（FieldID 310）**：`classificationValue` 的“教学产品制造”是该活动在体系中所属类别的可读值。读取文本并与上面的体系名称关联；原文的可选描述同样与普通 XSD 必填要求有差异，不用省略示例来消除该疑点。

**`@classificationId`（FieldID 320）**：根属性 `classificationId="45b127bf-078e-5df0-a5c0-fd6ee9a6b53e"` 引用分类主数据中的具体分类值，而不是只引用体系名称。读取 UUID 并到对应上下文的合法分类表核实，不能从示例文字猜造真实编码。

**`@classificationContextId`（FieldID 321）**：`classificationContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 为分类引用指定上下文。与分类 UUID 配对保存；省略时用数据集自身上下文，本孤立片段不提供 `fileAttributes`，所以回退操作必须由完整文件的读取器执行。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/classification-01.xml").getroot()
FIELDS = {
    "300": "classificationSystem",
    "310": "classificationValue",
    "320": "@classificationId",
    "321": "@classificationContextId",
}
for field_id, relative_path in FIELDS.items():
    values = field_values(node, relative_path)
    print(field_id, relative_path, json.dumps(values, ensure_ascii=False))
```

换成完整 `.spold` 文件时，先使用本章定位路径选出目标节点，再把它作为 `node` 传入。例如属性 `@amount` 最终用 `.get("amount")` 读取；子元素 `unitName` 用带命名空间的 `.findall("es:unitName", ns)` 读取。嵌套路径先进入对应子元素，再取最后的属性；如 `lognormal/@variance`，不能在外层 `uncertainty` 上直接取 `variance`。复合类型的子元素不能只读外层 `.text`，其结构已保留在返回记录的 `xml` 中。

### 直接在完整 spold 中使用这些路径

沿用上一段的 `FIELDS` 字典与 `field_values`，下面改从完整文件选取本类型节点。先用配套 demo 运行，再把文件名改为自己的 `.spold`。XML 查找会返回全部同类节点；可选结构未提供时，匹配数为零，不会被填成数值零。多个路径代表同类型的不同使用位置，统计时按父路径区分。

```python
from read_section import load_dataset, NS

dataset = load_dataset("demo-product.spold", index=0)
LOCATIONS = ['es:activityDescription/es:classification', 'es:flowData/es:intermediateExchange/es:classification']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要按行业或某个分类体系筛选活动时，把同一 classification 节点内的 classificationSystem 和 classificationValue 成对保存。不同体系的同名类别不能直接合并；应连同相应标识和上下文核对。这个类型也用于中间交换的产品分类，位置为 flowData/intermediateExchange/classification；返回的父路径用于区分活动分类与产品分类，按行业筛选活动时只取 activityDescription 下的记录。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/classification`；`flowData/intermediateExchange/classification`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TClassification")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tclassification)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
