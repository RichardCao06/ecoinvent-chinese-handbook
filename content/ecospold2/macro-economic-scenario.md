# 宏观经济情景

对应官方格式类型：`TMacroEconomicScenario`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 情景是主数据引用，也可能是子数据集的变化依据 <a href="#read-tmacroeconomicscenario" id="read-tmacroeconomicscenario"></a>

`activityDescription/macroEconomicScenario` 采用 `TMacroEconomicScenario`。属性 `macroEconomicScenarioId` 指向有效情景列表中的宏观经济情景；`macroEconomicScenarioContextId` 指定该情景主数据所属上下文，省略时使用数据集自身的上下文。元素 `name` 是情景名称，供人阅读；不能用它替换情景 UUID 做唯一连接。

元素 `comment` 说明宏观经济子数据集与父数据集默认情景的差异。它是 `TString32000` 文本，而不是混合图片的 `TTextAndImage`。读取情景时，可先保留名称和引用，再结合活动的父数据集关系阅读这段差异说明；仅从名称无法知道哪些输入、输出或其他条件相对于父情景发生了变化。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：宏观情景引用及与父情景的区别

[下载本段 XML](xml-examples/macro-economic-scenario-01.xml)。

```xml
<macroEconomicScenario xmlns="http://www.EcoInvent.org/EcoSpold02" macroEconomicScenarioId="0984f81b-aa81-5830-b34b-99b00a49a684" macroEconomicScenarioContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
  <!-- 教学构造的情景，非官方预测。 -->
  <name xml:lang="zh">教学需求变化情景</name>
  <comment xml:lang="zh">教学宏观情景子活动：相对父活动默认情景调整需求假设，其他条件须在完整文件中核查。</comment>
</macroEconomicScenario>
```

本例展示 activityDescription 中的宏观情景。comment 在这个类型中是直接多语言文本，不能套用其他 comment 所用的 text/index 嵌套结构。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@macroEconomicScenarioId`（FieldID 700）**：`macroEconomicScenarioId="0984f81b-aa81-5830-b34b-99b00a49a684"` 引用情景主数据。提取 UUID 并核对合法情景表，不从“需求变化”这类名称自行推导模型参数；本例只是教学引用。

**`@macroEconomicScenarioContextId`（FieldID 701）**：`macroEconomicScenarioContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 指定情景主数据上下文。与情景 UUID 一同识别对象；该属性省略时才采用文件自身上下文，不能把它当作地区上下文。

**`name`（FieldID 720）**：`name` 子元素写“教学需求变化情景”，说明数据集所属情景的可读名称。读取元素文本及 xml:lang，身份匹配仍依据 UUID 和上下文；名称本身不说明全部经济假设。

**`comment`（FieldID 740）**：`comment` 的直接文本说明教学子活动相对父默认情景调整需求假设。直接读这个子元素的文本和语言，不寻找不存在的 `comment/text`；完整应用还需加载父活动及变化字段，不能由一句说明推算任何真实数值。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/macro-economic-scenario-01.xml").getroot()
FIELDS = {
    "700": "@macroEconomicScenarioId",
    "701": "@macroEconomicScenarioContextId",
    "720": "name",
    "740": "comment",
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
LOCATIONS = ['es:activityDescription/es:macroEconomicScenario']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

提取情景名称或对比情景数据时，保留情景主数据引用及有效上下文，并阅读 comment。情景字段不是一项投入，不能直接用情景名称推导数量变化；有继承时仍须先展开。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/macroEconomicScenario`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TMacroEconomicScenario")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/macroEconomicScenario[1]",
  "attributes": {
    "macroEconomicScenarioId": "0984f81b-aa81-5830-b34b-99b00a49a684"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学情景"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching scenario"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tmacroeconomicscenario)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
