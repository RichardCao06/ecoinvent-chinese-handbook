# 参数

对应官方格式类型：`TParameter`。本篇以文章解释该类型的 12 条字段；复合类型也会说明它们依附在哪个对象上。

## 参数为交换公式提供可追溯的数值 <a href="#read-tparameter" id="read-tparameter"></a>

`TParameter` 保存供公式使用的数据集参数。参数不是物质输入或排放记录，即使也具有 `amount`，也不能混入基本流或中间交换的清单总量。必需的 `name` 是可多语言填写的描述性名称，必需的 `parameterId` 引用有效参数主数据；可选的 `parameterContextId` 指明参数所属上下文，省略时使用数据集上下文。必需的 `amount` 保存参数当前数值，是阅读公式时可用的已保存值，而非参数名称或 UUID。

参数的单位信息均为可选：`unitId` 引用参数数值的单位，`unitContextId` 指明单位上下文，省略时使用数据集上下文，`unitName` 是可多语言填写的单位名称。未提供单位时，不应自动补成质量单位，也不能仅凭字段名认定参数无量纲；应结合参数主数据和用途理解。可选的多语言 `comment` 提供针对该参数的一般说明，可选的 `uncertainty` 描述参数数值的不确定性，读参数值时可将这些解释和质量信息一起保存。

`variableName` 是可选的公式变量名。官方原说明在这一参数字段下沿用了“交换简称”和“交换量”的措辞，这项疑点已记录；从 `TParameter` 的用途看，不能据此认定它只能引用交换。文档列出的规则仍是以字母 a-z 开头，可含字母、数字和下划线，并不区分大小写；`calorific_Value` 与 `Calorific_value` 为相同变量名。另一项已记录差异是，`TVariableName` 的 XSD 限制为最大长度 40，并使用 `\w\S*` 模式，并未直接表达与这些文字规则完全等价的限制。XSD 验证通过，不意味着已经满足公式解析器或语义验证的全部命名要求。

可选的 `mathematicalRelation` 通过变量名或 `REF` 函数引用流、参数和属性的值，在给定变量值后，将结果写入参数自身的 `amount`。可选的 `isCalculatedAmount` 为 `true` 时，说明该数值由该数学关系计算得到；这一参数标记的 XSD 没有声明默认值，不能套用共同交换类型的默认设置。阅读现有文件时应区分直接记录的当前数值与其计算依据，只有在正确理解公式语言和依赖关系后，才重新计算参数。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学示例：2.5 kWh/kg 电力强度参数

[下载本段 XML](xml-examples/parameters-01.xml)。

```xml
<parameter xmlns="http://www.EcoInvent.org/EcoSpold02" parameterId="0c72e7c0-a190-5ba6-85ae-0b15236cc19d" amount="2.5" unitId="0489b6ee-11b9-577d-b8e0-1e45b6b2fcc1" variableName="electricity_intensity" parameterContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" mathematicalRelation="25 / 10" isCalculatedAmount="true">
        <name xml:lang="zh">电力强度（教学）</name>
        <name xml:lang="en">Electricity intensity (synthetic)</name>
        <unitName xml:lang="zh">kWh/kg</unitName>
        <unitName xml:lang="en">kWh/kg</unitName>
      <uncertainty><normal meanValue="2.5" variance="0.01" varianceWithPedigreeUncertainty="0.04"/></uncertainty><comment xml:lang="zh">教学电力强度；公式仅保存文本，不执行。</comment><comment xml:lang="en">Synthetic electricity intensity; formula text is never evaluated.</comment></parameter>
```

该独立参数片段以 parameterId 引用教学参数 master；它没有交换实例 id 和方向。amount=2.5、单位 kWh/kg 表示教学电力强度，mathematicalRelation="25 / 10" 与已记录值一致，但提取器只读取值和公式字符串，不使用 eval。参数不因参考产品为 10 kg 再被归一化。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`name`（FieldID 1700）**：字段 `name` 位于“教学示例：2.5 kWh/kg 电力强度参数”的直接子元素 `name` 中，示例值为 `电力强度（教学） / Electricity intensity (synthetic)`。中英文 name 说明这是教学电力强度参数；读取全部名称和 xml:lang 便于展示，参数 master 身份仍由 parameterId 和其 context 确定。

**`@parameterId`（FieldID 1705）**：字段 `parameterId` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `parameterId="0c72e7c0-a190-5ba6-85ae-0b15236cc19d"` 属性中读到。该 UUID 引用参数 master，不是交换实例 id；保存参数引用以便在 master data 中核对定义，不能当作供应活动或产品 UUID。

**`@parameterContextId`（FieldID 1706）**：字段 `parameterContextId` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `parameterContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。参数上下文已显式给出，省略时回退文件 context；取数时将它与 parameterId 配对，片段无文件上下文时不自行猜默认值。

**`@amount`（FieldID 1710）**：字段 `amount` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `amount="2.5"` 属性中读到。2.5 是参数当前值，单位为 kWh/kg；该值已经是电力强度，不因完整数据集参考产品为 10 kg 再除以 10，也不自动生成交换行。

**`@unitId`（FieldID 1712）**：字段 `unitId` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `unitId="0489b6ee-11b9-577d-b8e0-1e45b6b2fcc1"` 属性中读到。此 UUID 引用电力强度所用单位的 master；参数的单位属性在 XSD 中可选，缺省时不能填造单位 UUID，应保存未知并结合参数定义核对。

**`@unitContextId`（FieldID 1713）**：字段 `unitContextId` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。显式单位上下文与 unitId 共同定位参数单位，省略时回退文件 context；该上下文和 parameterContextId 即使相同也分别保留。

**`unitName`（FieldID 1714）**：字段 `unitName` 位于“教学示例：2.5 kWh/kg 电力强度参数”的直接子元素 `unitName` 中，示例值为 `kWh/kg / kWh/kg`。展示单位 kWh/kg 表明参数是每千克产品的电力强度；读取各语言 unitName 并结合单位 master 核对，不能按字符串将它当成 kWh 交换数量。

**`@variableName`（FieldID 1715）**：字段 `variableName` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `variableName="electricity_intensity"` 属性中读到。`electricity_intensity` 是数学关系引用参数值的变量名，不是 parameterId；保存原变量名，遵循以字母起始、数字和下划线可用且不区分大小写的规则。

**`@mathematicalRelation`（FieldID 1720）**：字段 `mathematicalRelation` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `mathematicalRelation="25 / 10"` 属性中读到。`25 / 10` 展示参数值 2.5 的教学关系；提取时只保存该字符串和 amount，不执行 eval，也不根据公式修改实际读取的数值。

**`@isCalculatedAmount`（FieldID 1725）**：字段 `isCalculatedAmount` 可在“教学示例：2.5 kWh/kg 电力强度参数”根元素的 `isCalculatedAmount="true"` 属性中读到。true 表示 amount 是已计算得到的参数值；此标志不等于要求读取软件重算，还需和数学关系、缺失值及已展开继承的状态一起理解。

**`uncertainty`（FieldID 1730）**：字段 `uncertainty` 对应“教学示例：2.5 kWh/kg 电力强度参数”的直接子元素 `uncertainty`，其中包含 `normal` 子元素。uncertainty/normal 中 meanValue=2.5、variance=0.01、varianceWithPedigreeUncertainty=0.04 描述参数值的不确定性；保存完整分布属性，与电力交换 25 kWh 的不确定性区分。

**`comment`（FieldID 1740）**：字段 `comment` 位于“教学示例：2.5 kWh/kg 电力强度参数”的直接子元素 `comment` 中，示例值为 `教学电力强度；公式仅保存文本，不执行。 / Synthetic electricity intensity; formula text is never evaluated.`。comment 的中英文文本明确参数和公式仅用于教学，提取应保留全部说明及语言，用来解释范围，而不是把文本当作计算指令。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/parameters-01.xml").getroot()
FIELDS = {
    "1700": "name",
    "1705": "@parameterId",
    "1706": "@parameterContextId",
    "1710": "@amount",
    "1712": "@unitId",
    "1713": "@unitContextId",
    "1714": "unitName",
    "1715": "@variableName",
    "1720": "@mathematicalRelation",
    "1725": "@isCalculatedAmount",
    "1730": "uncertainty",
    "1740": "comment",
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
LOCATIONS = ['es:flowData/es:parameter']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

要查看公式输入值，读取 parameter 的 amount、variableName、单位及数学关系。参数可供多个交换使用，并非一笔新增投入；公式作为文本保留，不执行 eval，也不要把参数量归一化为参考产品的额外交换。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/parameter`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TParameter")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/parameter[1]",
  "attributes": {
    "parameterId": "0c72e7c0-a190-5ba6-85ae-0b15236cc19d",
    "amount": "2.5",
    "unitId": "0489b6ee-11b9-577d-b8e0-1e45b6b2fcc1",
    "variableName": "electricity_intensity"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "电力强度（教学）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Electricity intensity (synthetic)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tparameter)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
