# 区室与子区室

对应官方格式类型：`TCompartment`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 区室配对决定环境流的具体位置 <a href="#read-tcompartment" id="read-tcompartment"></a>

`TCompartment` 用来说明一条基本流属于哪一组区室与子区室。“区室”既可表达环境接收介质，也可用于自然资源分类，因此本文采用已交叉审阅确定的“区室／子区室”术语。内部的 `compartment` 和 `subcompartment` 是必需的多语言名称，提供所引用配对的纯文本表示；前者是区室名，后者是更细的子区室名。原表分别将它们追溯到字段 5315 和 5325，不应把这些跨表编号误读成该数据集里的交换编号。

必需的 `subcompartmentId` 是配对引用的 UUID，必须在有效区室清单中定义，原表指向字段 5330。可选的 `subcompartmentContextId` 指明子区室所属上下文，省略时使用数据集自身上下文。因而读数时应把配对标识及上下文与显示名称一起保存：显示名称有助于理解，主数据引用用于一致匹配。外层基本流的 `compartment` 元素与内层区室名称的 `compartment` 元素同名，但处于不同结构位置；提取时应按层级识别，避免把整个配对结构当成一段普通文字。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学示例：空气／未指定子区室

[下载本段 XML](xml-examples/compartments-01.xml)。

```xml
<compartment xmlns="http://www.EcoInvent.org/EcoSpold02" subcompartmentId="6bbb1a41-12de-5599-843e-cc02d4084a9a" subcompartmentContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
          <compartment xml:lang="zh">空气</compartment>
          <compartment xml:lang="en">air</compartment>
          <subcompartment xml:lang="zh">未指定</subcompartment>
          <subcompartment xml:lang="en">unspecified</subcompartment>
        </compartment>
```

这是教学基本流中的区室配对子元素，外层 compartment 包含同名内层 compartment，提取时必须区分两层。air/unspecified 是英文展示名称；subcompartmentId 引用区室/子区室配对 master，subcompartmentContextId 指其上下文，均为构造 UUID。片段没有流量和方向，不能靠 air 推断一条排放记录。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`compartment`（FieldID 330）**：字段 `compartment` 位于“教学示例：空气／未指定子区室”的直接子元素 `compartment` 中，示例值为 `空气 / air`。外层 compartment 下面的同名子元素展示空气/air；读取相对于外层根的直接子元素及 xml:lang，避免把外层容器误当名称文本，也不据“空气”自动推断输出方向。

**`subcompartment`（FieldID 340）**：字段 `subcompartment` 位于“教学示例：空气／未指定子区室”的直接子元素 `subcompartment` 中，示例值为 `未指定 / unspecified`。subcompartment 的未指定/unspecified 是对子区室的展示标签；逐语言保存，并与 subcompartmentId 指向的区室配对 master 核对，不能仅按“未指定”跨区室合并。

**`@subcompartmentId`（FieldID 350）**：字段 `subcompartmentId` 可在“教学示例：空气／未指定子区室”根元素的 `subcompartmentId="6bbb1a41-12de-5599-843e-cc02d4084a9a"` 属性中读到。该 UUID 引用 compartment/subcompartment 配对的 master，不是一个独立的交换实例或流 master；汇总基本流时应与其 context、流 ID/context、单位 ID/context 一起使用。

**`@subcompartmentContextId`（FieldID 351）**：字段 `subcompartmentContextId` 可在“教学示例：空气／未指定子区室”根元素的 `subcompartmentContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。这个属性明确区室配对 master 的上下文，省略时回退所在数据集的文件 context；读取片段时没有 fileAttributes 就保留未确认上下文，不凭显示名称猜归属。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/compartments-01.xml").getroot()
FIELDS = {
    "330": "compartment",
    "340": "subcompartment",
    "350": "@subcompartmentId",
    "351": "@subcompartmentContextId",
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
LOCATIONS = ['es:flowData/es:elementaryExchange/es:compartment']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

要统计某环境介质的排放，定位 elementaryExchange/compartment，配对读取 compartment 与 subcompartment。提取时保留外层基本流的 UUID、单位与方向；区室节点本身没有一笔可加入总量的交换 amount。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/elementaryExchange/compartment`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TCompartment")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **4 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/elementaryExchange[1]/compartment[1]",
  "attributes": {
    "subcompartmentId": "9bfcfd12-1b84-56cf-8bd8-1abc71a30268"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}compartment",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "自然资源"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}compartment",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "natural resource"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tcompartment)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
