# 数据录入者

对应官方格式类型：`TDataEntryBy`。本篇以文章解释该类型的 5 条字段；复合类型也会说明它们依附在哪个对象上。

## 录入者说明谁编制并提交了这份记录 <a href="#read-tdataentryby" id="read-tdataentryby"></a>

在 `administrativeInformation/dataEntryBy` 中，`TDataEntryBy` 记录编制数据集并将其录入数据库的人员。属性 `personId` 引用该人员，`personContextId` 指定人员主数据所属上下文，省略时使用数据集自身的上下文。属性 `personName` 和 `personEmail` 分别存储人员的名与姓以及完整电子邮件地址；它们用于显示和联系，身份连接仍依赖人员 ID 与上下文。

属性 `isActiveAuthor` 表示这位人员是否为数据集的活跃作者，完整数据 XSD 的默认值为 `false`。这里的活跃作者是后续维护中的联系角色：其他数据提供者今后修改数据集时，将征询此人的意见。它不能仅凭姓名是否出现在文件中推断，也不等同于版权人、审核人或原始数据采集者。取数时应保留这个标记，才能区分一般录入人员与需要在后续变更中联系的作者。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：录入人员与当前负责人

[下载本段 XML](xml-examples/data-entry-01.xml)。

```xml
<dataEntryBy xmlns="http://www.EcoInvent.org/EcoSpold02" personId="2163e122-88c4-55e7-af84-00947e9b7b0a" personContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" isActiveAuthor="true" personName="Teaching author" personEmail="demo@example.invalid">
  <!-- 教学构造的录入者，邮箱不用于联系真实人员。 -->
</dataEntryBy>
```

dataEntryBy 位于 administrativeInformation 中，本类型字段都是根属性，示例没有 personName 或 personEmail 子元素。人员标识沿用教学 demo，true 用于展示当前作者标记。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@personId`（FieldID 3400）**：`personId="2163e122-88c4-55e7-af84-00947e9b7b0a"` 标识准备并录入数据集的人员。直接读取属性后关联人员主数据（原表引用人员字段3610），不要与原始数据生成者或评审者自动视作同一角色。

**`@personContextId`（FieldID 3401）**：`personContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 是录入者人员引用的上下文。人员 UUID 加有效上下文才构成引用键；省略时回退到文件上下文，不能靠邮箱替代身份。

**`@isActiveAuthor`（FieldID 3403）**：`isActiveAuthor="true"` 表示此人是数据集的当前作者，其他提供者以后修改时会征询其意见。读取布尔值，不把它解释为人员账户在线、数据审核通过或自动授权发布；普通 XSD 省略时默认 false。

**`@personName`（FieldID 3405）**：`personName="Teaching author"` 是录入者的姓名属性。用属性读取取得文字，不找同名子元素；姓名便于阅读，同名不能保证人员身份相同。

**`@personEmail`（FieldID 3406）**：`personEmail="demo@example.invalid"` 保存完整电子邮件地址。它也是属性，示例地址为教学构造；提取时保留原文，不据其存在自动发送联系或判断信息已核实。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/data-entry-01.xml").getroot()
FIELDS = {
    "3400": "@personId",
    "3401": "@personContextId",
    "3403": "@isActiveAuthor",
    "3405": "@personName",
    "3406": "@personEmail",
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
LOCATIONS = ['es:administrativeInformation/es:dataEntryBy']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要追溯数据录入人员时，读取 dataEntryBy 的人员 UUID、有效上下文及主数据冗余信息。录入者与原始数据生成者是不同角色；只凭人名不宜关联或去重人员记录。生成工具则读取文件属性的 fileGenerator。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`administrativeInformation/dataEntryBy`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TDataEntryBy")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/administrativeInformation[1]/dataEntryBy[1]",
  "attributes": {
    "personId": "2163e122-88c4-55e7-af84-00947e9b7b0a",
    "personName": "Teaching author",
    "personEmail": "demo@example.invalid",
    "isActiveAuthor": "false"
  },
  "children_excerpt": []
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tdataentryby)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
