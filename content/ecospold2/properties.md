# 交换属性

对应官方格式类型：`TProperty`。本篇以文章解释该类型的 18 条字段；复合类型也会说明它们依附在哪个对象上。

## 交换属性：把产品特征与交换数量分开理解 <a href="#read-tproperty" id="read-tproperty"></a>

`TProperty` 附在交换的 `property` 元素中，描述干质量、含水率、价格、元素或物质含量等特征。中间交换和基本流交换都继承通用交换结构，因此都可具有这些属性。阅读一条属性时，首先用 `propertyId` 识别它引用的属性主数据，再读描述性文本 `name`；`propertyContextId` 指定该属性主数据所属的上下文，省略时采用数据集自身的上下文。UUID 引用和上下文确定的是属性身份，名称帮助人理解身份，不能仅靠同名文字认定两个属性一定相同。

属性的数值存于自身的 `amount`，其单位由 `unitId` 引用，`unitName` 提供单位名称，`unitContextId` 指明单位主数据上下文，省略时同样采用数据集上下文。这里的 `amount` 并不等于外层交换的 `amount`，也不保证与它具有相同单位；价格、含水率和干质量描述的量并不相同。取数时，应把属性定义、数值及单位一起读取，并核查其计量或归一化基准，不能直接把属性量加到投入输出清单中。`isDefiningValue` 为 true 时，属性值属于交换定义的一部分，与交换量之间具有不能针对不同数据集中个别实例改变的固定关系；它既不表示两个数值相等，也不是允许任意按比例改写所有属性的开关。

若属性不是手工指定的值，`mathematicalRelation` 可通过变量名或 `REF` 函数引用流、参数和属性的数值，计算结果写入本属性的 `amount`；`isCalculatedAmount` 为 true 表示这个数值来自该数学关系。`variableName` 则给本属性量一个可在数学关系中引用的名字。文档要求变量名以字母 a-z 开头，可以包含字母、数字和下划线，并且不区分大小写，例如 `calorific_Value` 与 `Calorific_value` 等同。所附 XSD 的 `TVariableName` 类型限定长度最多 40，并采用正则 `\w\S*`，它没有直接表达与文字规则完全等价的约束，因此不能仅凭 XSD 验证通过就认定变量名满足所有公式语言规则。读取已计算数值与重算公式是不同工作；字段定义本身不足以替代公式解析、引用解析和继承处理。

`uncertainty` 描述的是该属性值的不确定性，仍须按所选分布解释，而不是默认套用外层交换的不确定性。`sourceId` 引用记录该属性的有效来源或出版物，`sourceContextId` 指定来源上下文，省略时采用数据集上下文。对子数据集，如果要移除继承的来源引用，应将 `sourceIdOverwrittenByChild` 设为 true；仅让引用消失会按原文规则被解释为保留父值。`sourceYear` 记录出版或交流年份，网站来源记录最后访问；`sourceFirstAuthor` 通常填写第一作者的姓氏和名字缩写，例如 Einstein A.，而来源类型 `sourceType` 为 4、5、6、7 的现场测量、口头交流、个人书面交流或问卷调查，填写提供信息的人。最后，`comment` 可以补充该交换中这项具体属性的假设、说明和限制，使数值能够追溯到其证据。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学干质量属性及来源

[下载本段 XML](xml-examples/properties-01.xml)。

```xml
<property xmlns="http://www.EcoInvent.org/EcoSpold02" propertyId="00000000-0000-4000-8000-000000000101" propertyContextId="00000000-0000-4000-8000-000000000100" unitId="00000000-0000-4000-8000-000000000102" unitContextId="00000000-0000-4000-8000-000000000100" amount="0.8" isDefiningValue="true" mathematicalRelation="0.5 + 0.3" isCalculatedAmount="true" variableName="dry_mass" sourceId="00000000-0000-4000-8000-000000000103" sourceContextId="00000000-0000-4000-8000-000000000100" sourceIdOverwrittenByChild="false" sourceYear="2025" sourceFirstAuthor="Example A.">
  <name xml:lang="zh">干质量（教学属性）</name>
  <unitName xml:lang="zh">kg/kg</unitName>
  <uncertainty><normal meanValue="0.8" variance="0.0001" varianceWithPedigreeUncertainty="0.0004"/></uncertainty>
  <comment xml:lang="zh">教学构造：这里约定每 kg 交换产品含 0.8 kg 干物质；所有 UUID、文献名和单位身份都是虚构。</comment>
</property>
```

这是属于某个中间或基本流交换的完整 property 片段。它用自己的单位 kg/kg 存 0.8，与外层交换 amount 可以不同；本例定义了质量比例才可讨论与交换量相乘。公式 0.5 + 0.3 只演示已计算量的表达方式，读取器不求值。所有 UUID 与来源仅为教学，不表示真实主数据引用已解析。

### 示例 2：属性默认值与删除父来源的标记

[下载本段 XML](xml-examples/properties-02.xml)。

```xml
<property xmlns="http://www.EcoInvent.org/EcoSpold02" propertyId="00000000-0000-4000-8000-000000000101" amount="0.8" sourceIdOverwrittenByChild="true">
  <name xml:lang="zh">干质量（教学属性）</name>
  <comment xml:lang="zh">此片段演示省略可选标记及显式删除父来源的属性语法；真实子差异记录还需使用对应子模式并解析父属性。</comment>
</property>
```

这个完整类型片段省略 isDefiningValue 和 isCalculatedAmount：普通模式将二者默认作 false。sourceId 没有出现而删除标记为 true，用于说明子数据集显式移除父来源的机制；不能把本片段当作已完成继承展开的完整活动文件。省略来源本身与明确删除不同。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@propertyId`（FieldID 2300）**：主例 `property/@propertyId` 为 `00000000-0000-4000-8000-000000000101`，识别属性主数据；这是教学 UUID，不是所属交换实例的 id。按主数据引用保存，并保留外层交换路径。

**`@propertyContextId`（FieldID 2301）**：`property/@propertyContextId` 为教学上下文 `00000000-0000-4000-8000-000000000100`，限定属性 UUID 所属主数据空间。若省略，应使用已知的数据集上下文；缺上下文时不能仅靠 UUID 宣称解析成功。

**`name`（FieldID 2310）**：`property/name` 的中文文本为“干质量（教学属性）”。按子元素读取并保留语言，而不是用这个可变显示名称替代 propertyId。

**`@unitId`（FieldID 2320）**：`property/@unitId` 为 `00000000-0000-4000-8000-000000000102`，引用属性量自己的单位主数据。示例把它约定为 kg/kg，不能直接借用外层交换的单位 UUID。

**`@unitContextId`（FieldID 2321）**：`property/@unitContextId` 为 `00000000-0000-4000-8000-000000000100`，限定属性单位的主数据上下文。省略时回退到数据集上下文，不能与 propertyContextId 混为同一角色。

**`unitName`（FieldID 2325）**：`property/unitName` 为 `kg/kg`，是属性单位的展示文本。这个比例单位与外层交换可能用的 kg 不同；应结合单位身份与属性定义判断运算。

**`@amount`（FieldID 2330）**：`property/@amount="0.8"` 在本例约定为每 kg 产品的干质量比例。先独立保留属性量，不能把它作为额外 0.8 kg 交换求和，也不能对所有属性无条件乘交换量。

**`@isDefiningValue`（FieldID 2335）**：主例 `@isDefiningValue="true"` 表示属性值是交换定义的一部分，与交换 amount 的关系固定，不能在不同数据集的该交换实例中随意改变。本例干质量比例 0.8 因而是教学交换定义的一部分；第二例省略该标记时普通 XSD 默认 false，不能由属性名称推断它。

**`@mathematicalRelation`（FieldID 2340）**：`property/@mathematicalRelation="0.5 + 0.3"` 保存产生本例 0.8 的公式文本。它是属性量的数学关系，不是交换的公式；不通过 Python eval 执行。

**`@isCalculatedAmount`（FieldID 2345）**：主例 `@isCalculatedAmount="true"` 声明 amount 来自数学关系；第二例省略时普通 XSD 默认 false。该标记声明来源，读取器仍保留已有 amount，不据此覆盖数值。

**`@variableName`（FieldID 2350）**：`property/@variableName="dry_mass"` 为其他数学关系引用此属性提供变量名。它不是 TTextAndImage 的文本 variable，也不是属性的主数据 UUID。

**`uncertainty`（FieldID 2360）**：`property/uncertainty/normal` 存均值 0.8 及两种方差，描述当前属性 amount 的不确定性。保留属性父路径，不能将其移到外层交换的不确定性下。

**`@sourceId`（FieldID 2370）**：主例 `property/@sourceId` 为教学来源 `00000000-0000-4000-8000-000000000103`。它引用该属性值的有效来源，不是审查人员 ID 或外层交换实例 ID；需要对应主数据才能解析。

**`@sourceContextId`（FieldID 2371）**：`property/@sourceContextId` 为 `00000000-0000-4000-8000-000000000100`，限定属性来源 UUID 的上下文；省略时通常沿用数据集上下文。这个上下文与单位、属性上下文应分别保存。

**`@sourceIdOverwrittenByChild`（FieldID 2372）**：主例 `@sourceIdOverwrittenByChild="false"` 未要求删除父来源，第二例为 true 且没有 sourceId，用来演示显式移除。只有省略 sourceId 会保留父值，真实子记录仍须结合父属性与子模式。

**`@sourceYear`（FieldID 2375）**：`property/@sourceYear="2025"` 保存本例虚构来源的出版或沟通年份；网站情况可以表示最后访问时点。它不是数据有效年份，也不是 fileTimestamp。

**`@sourceFirstAuthor`（FieldID 2376）**：`property/@sourceFirstAuthor="Example A."` 是虚构第一作者的姓及名字缩写。特定沟通来源记录沟通者；这是冗余来源文本，不能替代 sourceId。

**`comment`（FieldID 2380）**：`property/comment` 明确每 kg 产品的干质量约定。它是普通多语言字符串，读取文本即可，不应按 text/imageUrl/variable 富文本结构寻找子节点。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/properties-01.xml").getroot()
FIELDS = {
    "2300": "@propertyId",
    "2301": "@propertyContextId",
    "2310": "name",
    "2320": "@unitId",
    "2321": "@unitContextId",
    "2325": "unitName",
    "2330": "@amount",
    "2335": "@isDefiningValue",
    "2340": "@mathematicalRelation",
    "2345": "@isCalculatedAmount",
    "2350": "@variableName",
    "2360": "uncertainty",
    "2370": "@sourceId",
    "2371": "@sourceContextId",
    "2372": "@sourceIdOverwrittenByChild",
    "2375": "@sourceYear",
    "2376": "@sourceFirstAuthor",
    "2380": "comment",
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
LOCATIONS = ['es:flowData/es:intermediateExchange/es:property', 'es:flowData/es:elementaryExchange/es:property']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要干质量、含水率、价格或组成等信息，读取每个交换下的 property，同时保留所属交换实例路径、propertyId、单位和 amount。只有明确属性定义与计量基准后，才能决定是否与交换量相乘；属性不是额外物质流。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange/property`；`flowData/elementaryExchange/property`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TProperty")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/intermediateExchange[1]/property[1]",
  "attributes": {
    "propertyId": "157cb588-bc77-5666-9107-3791e5783446",
    "amount": "1",
    "unitId": "00875264-8155-513e-8182-437026535fcb",
    "isDefiningValue": "true"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "干质量（教学比例）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Dry mass (teaching ratio)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tproperty)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
