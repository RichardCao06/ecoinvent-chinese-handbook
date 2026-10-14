# 时间范围

对应官方格式类型：`TTimePeriod`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 时间段与整段有效性要分开判断 <a href="#read-ttimeperiod" id="read-ttimeperiod"></a>

`activityDescription/timePeriod` 采用 `TTimePeriod`。属性 `startDate` 和 `endDate` 是数据集有效时间段的完整日期，采用年-月-日；它们与文件创建、编辑和导出时间不同。属性 `isDataValidForEntirePeriod` 说明该活动的基本流交换和中间交换是否对所列整个时间段都有效，不能仅根据起止日期推定整段有效。

当 `isDataValidForEntirePeriod` 不为真时，可在元素 `comment` 中解释。这个 `TTextAndImage` 字段也可说明单元过程的时间相关性，例如较早数据是否仍适用于当前活动；还可说明为什么数据不覆盖整个期间、实际在哪些较短期间内有效。取数时应将起止日期、整段有效性标记和这段说明一并保存，否则会丢失日期区间内的重要限定。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：声明时间段及局部有效性

[下载本段 XML](xml-examples/time-period-01.xml)。

```xml
<timePeriod xmlns="http://www.EcoInvent.org/EcoSpold02" startDate="2025-01-01" endDate="2025-12-31" isDataValidForEntirePeriod="false">
  <!-- 教学构造的有效期，非真实数据年代。 -->
  <comment><text index="1" xml:lang="zh">教学数据仅适用于2025年1月至6月；下半年改造后需重新核实。</text></comment>
</timePeriod>
```

这个 timePeriod 片段声明全年范围，却明确标为不是整个时间段都有效，并在 comment 解释较小适用区间。false 不表示缺失或零交换量。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@startDate`（FieldID 600）**：`startDate="2025-01-01"` 是所声明有效时间段的开始日期。用属性读取取得完整年、月、日并按日期解析；它不是文件创建日期，本例日期只是教学构造。

**`@endDate`（FieldID 610）**：`endDate="2025-12-31"` 是所声明时间段的结束日期。与 startDate 一起保存和比较，不只保留年份；还须结合 false 标记及说明判断交换数据实际在哪个较短期间有效。

**`@isDataValidForEntirePeriod`（FieldID 620）**：`isDataValidForEntirePeriod="false"` 明确说明 flowData 的基本流和中间交换不适用于整个声明期间。读取布尔值时不要用非空字符串的真假代替语义，因为字符串“false”在 Python 中也非空；应据布尔词法规则解析，并进一步读取 comment。

**`comment`（FieldID 630）**：`comment/text` 指明只有2025年1月至6月适用，并说明下半年改造后须重新核实。按索引、语言读取说明，把这一限制与日期属性一起返回；不能因 endDate 写到12月就忽略实际有效性的限定。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/time-period-01.xml").getroot()
FIELDS = {
    "600": "@startDate",
    "610": "@endDate",
    "620": "@isDataValidForEntirePeriod",
    "630": "comment",
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
LOCATIONS = ['es:activityDescription/es:timePeriod']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

按年份选择数据时，读取 startDate、endDate 和 isDataValidForEntirePeriod。日期范围覆盖目标年份，并不自动说明该段内每一天的数据都同样适用；不要把文件编辑时间当作清单年份。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/timePeriod`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TTimePeriod")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/timePeriod[1]",
  "attributes": {
    "startDate": "2025-01-01",
    "endDate": "2025-12-31",
    "isDataValidForEntirePeriod": "true"
  },
  "children_excerpt": []
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-ttimeperiod)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
