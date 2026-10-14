# 交换的通用字段

对应官方格式类型：`TCustomExchange`。本篇以文章解释该类型的 25 条字段；复合类型也会说明它们依附在哪个对象上。

## 先读交换的共同结构 <a href="#read-tcustomexchange" id="read-tcustomexchange"></a>

一个活动的数据不只是一个总数，而是一组说明“交换了什么、交换多少、用什么单位表示”的记录。`TCustomExchange` 定义中间交换与基本流交换共有的字段；`TIntermediateExchange` 和 `TElementaryExchange` 在它的基础上增加各自的信息。因此，读到具体交换时，既要读取该交换类型的专用字段，也要读取这些共同字段。下文用代码标出实际 XML 名称：属性写在元素的开始标签中，名称、说明等内容则由子元素承载。

识别一条记录时，先区分名称与标识。必需的 `name` 是交换名称，必需的 `id` 是这条交换实例的 UUID。它不是产品的 `intermediateExchangeId`，也不是基本流主数据的 `elementaryExchangeId`：同一数据集可以有多条交换引用同一个主数据条目，因此按产品或基本流标识去重会丢失交换实例。随后读取必需的 `amount`，它以 `TFloatNumber` 表示这条交换的数量；必需的 `unitId` 引用该数量的单位，必需的 `unitName` 提供便于阅读的单位名称。可选的 `unitContextId` 指明单位主数据所属上下文，省略时使用数据集自身的上下文。取数时应把交换实例标识、数量、单位标识及其上下文一起保留，以免把不同单位或不同主数据空间的同名记录合并。

`name`、`unitName` 和可选的 `comment` 可以用多种语言表达；`comment` 为这条交换提供一般说明。读取文本时，应根据 `xml:lang` 选择需要的语言，而不是把多个语言版本串成一个名称。可重复的 `synonym` 是同义词，每条最多 80 个字符，可有 0..n 条；与普通多语言字符串不同，同义词允许同一个 `xml:lang` 对应多个条目。可重复的 `tag` 则是供筛选、分组和搜索使用的开放关键词。原说明写明，`validTags` 主文件中找不到某个标签时，语义验证应提示信息，而不应把它当成错误。`casNumber` 是可选的化学品 CAS 编号；这份格式说明给出的形式为 `000000-00-0`，并允许第一组数字不足六位。CAS 编号帮助识别化学物质，但并不能替代交换实例标识、单位或基本流区室信息。

一些交换数量还带有计算关系。可选的 `variableName` 为交换数量提供公式中的简称；文档要求以字母 a-z 开头，可含字母、数字和下划线，且不区分大小写，例如 `calorific_Value` 与 `Calorific_value` 等同。可选的 `mathematicalRelation` 通过变量名或 `REF` 函数引用流、参数和属性，在给定一组变量值后，其计算结果写入 `amount`。当 `isCalculatedAmount` 为 `true` 时，`amount` 是 `mathematicalRelation` 或 `transferCoefficient` 的计算值；共同交换类型的 XSD 将这一标记默认设为 `false`。解析文件可以读取已保存的数量与公式，但重新求值需要支持对应公式语言，不能把公式字符串本身当成数值。

可重复的 `transferCoefficient` 将特定输入与特定输出关联，表示该输入中流向该输出的份额；按其专用结构说明，系数应乘以被引用交换的数量。可选的 `uncertainty` 用分布函数、参数和／或数据质量谱系信息描述交换数量的不确定性。可重复的 `property` 描述交换的干质量、含水率、价格或特定元素和物质的含量。这三类字段都是具有内部结构的元素，读数时不能只提取其标签文字，也不能把属性值、不确定性参数或转移系数直接相加到交换数量中。

可选的 `sourceId` 指向有效来源，`sourceContextId` 指明来源所属上下文，省略时使用数据集上下文。`sourceYear` 记录出版或交流年份；网站来源记录最后访问年份。`sourceFirstAuthor` 用姓和名字缩写记录第一作者，例如 Einstein A.；在现场测量、口头交流、个人书面交流和问卷调查这几类来源中，即 `sourceType` 为 4、5、6、7 时，记录提供信息的人员。`pageNumbers` 给出文章或较大型出版物中实际取数的页码。这组字段与数量一同读取，才能追溯某条交换的依据；`sourceYear` 不等于活动数据的有效年份。

若交换有独立的分配设置，`specificAllocationPropertyId` 指定分配所用属性，并覆盖数据集层面由 `masterAllocationPropertyId` 定义的默认设置；`specificAllocationPropertyContextId` 指明该属性所属上下文，省略时使用数据集上下文。这些字段说明应使用哪项属性，不能单凭它们自行构造一套新的分配算法。继承时还要读取 `sourceIdOverwrittenByChild` 与 `specificAllocationPropertyIdOverwrittenByChild`：子数据集要移除对应的主数据引用，必须把相应标记设为 `true`；否则，引用不再出现仍可能被解释为“保留父数据集的值”，不能据此判断它已被清空。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学示例：只含共同类型字段的交换

[下载本段 XML](xml-examples/exchanges-01.xml)。

```xml
<exchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="00000000-0000-4000-8000-000000001005" amount="1.5" unitId="a4800e12-54b1-5444-a6d0-b48a59529439" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" variableName="fossil_co2" isCalculatedAmount="true" mathematicalRelation="0.15 * 10" casNumber="124-38-9" sourceId="00000000-0000-4000-8000-000000001120" sourceContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" sourceIdOverwrittenByChild="false" sourceYear="2025" sourceFirstAuthor="Demo A." pageNumbers="3-4" specificAllocationPropertyId="00000000-0000-4000-8000-000000001150" specificAllocationPropertyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" specificAllocationPropertyIdOverwrittenByChild="false">
  <name xml:lang="zh">二氧化碳，化石源（教学）</name>
  <name xml:lang="en">Carbon dioxide, fossil (synthetic)</name>
  <unitName xml:lang="zh">kg</unitName>
  <unitName xml:lang="en">kg</unitName>
  <comment xml:lang="zh">全部为教学构造；此处仅展示交换共用字段。</comment>
  <comment xml:lang="en">Synthetic teaching example of shared exchange fields only.</comment>
  <uncertainty>
    <lognormal meanValue="1.5" mu="0.4054651081081644" variance="0.01" varianceWithPedigreeUncertainty="0.04"/>
  </uncertainty>
  <synonym xml:lang="zh">教学化石二氧化碳</synonym>
  <synonym xml:lang="en">Synthetic fossil carbon dioxide</synonym>
  <synonym xml:lang="zh">教学 CO2</synonym>
  <property propertyId="00000000-0000-4000-8000-000000001400" propertyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" amount="1" unitId="00000000-0000-4000-8000-000000001401" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
    <name xml:lang="zh">教学比例属性</name>
    <name xml:lang="en">Synthetic ratio property</name>
    <unitName xml:lang="zh">kg/kg</unitName>
    <unitName xml:lang="en">kg/kg</unitName>
  </property>
  <transferCoefficient exchangeId="00000000-0000-4000-8000-000000001200" amount="0.6">
    <comment xml:lang="zh">教学输出中的某一输入贡献份额；被引用的输入行位于完整数据集。</comment>
  </transferCoefficient>
  <tag>synthetic-teaching</tag>
</exchange>
```

这是完整、可解析的 TCustomExchange 类型片段；&lt;exchange&gt; 是本教程用于类型级校验的示例根名，并非 flowData 的实际交换标签。它不含 inputGroup/outputGroup、产品或基本流 master ID，也不单独确定方向；完整文件要使用 intermediateExchange 或 elementaryExchange 的派生结构。所有 UUID、来源和属性均为教学构造。子元素依 XSD 顺序排列，属性顺序没有语义。这里 amount=1.5 kg 是交换数量，property/amount=1 kg/kg 是独立属性值，transferCoefficient/amount=0.6 是份额，三者不能混为一列。 此处的教学比例属性 1 kg/kg 仅展示属性结构，不表示 CO₂ 的真实碳质量分数或其他实测物性。

### 示例 2：教学示例：继承清除标志的共同字段片段

[下载本段 XML](xml-examples/exchanges-02.xml)。

```xml
<exchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="00000000-0000-4000-8000-000000001006" amount="1.5" unitId="a4800e12-54b1-5444-a6d0-b48a59529439" sourceIdOverwrittenByChild="true" specificAllocationPropertyIdOverwrittenByChild="true">
  <name xml:lang="zh">教学清除引用标记</name>
  <name xml:lang="en">Synthetic reference-removal markers</name>
  <unitName xml:lang="zh">kg</unitName>
  <unitName xml:lang="en">kg</unitName>
</exchange>
```

此片段展示 sourceId 与 specificAllocationPropertyId 缺省、对应 OverwrittenByChild=true 的显式清除写法；仅在实际子数据集继承处理中才发生清除父引用的效果。它不是已展开的 childActivityDataset，也不定义父值；普通缺省引用不等价于清除。UUID 和数值为教学构造。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`name`（FieldID 1000）**：字段 `name` 位于“教学示例：只含共同类型字段的交换”的直接子元素 `name` 中，示例值为 `二氧化碳，化石源（教学） / Carbon dioxide, fossil (synthetic)`。同一交换的中文和英文名称供展示与检索，应读取全部 `name` 子元素及其 `xml:lang`；这些标签不能代替 master UUID 作为合并依据。

**`@id`（FieldID 1005）**：字段 `id` 可在“教学示例：只含共同类型字段的交换”根元素的 `id="00000000-0000-4000-8000-000000001005"` 属性中读到。该 UUID 唯一标识数据集内的一条交换实例；同一产品或基本流 master 可被多条不同 `id` 的交换引用，因此保留每行，不按 master ID 去重。

**`@amount`（FieldID 1020）**：字段 `amount` 可在“教学示例：只含共同类型字段的交换”根元素的 `amount="1.5"` 属性中读到。这是交换数量，配合单位解释为 1.5 kg；读取属性原字符串并以有限 Decimal 校验，方向需由派生类型的分组判断，不能只看正负号。

**`@unitId`（FieldID 1030）**：字段 `unitId` 可在“教学示例：只含共同类型字段的交换”根元素的 `unitId="a4800e12-54b1-5444-a6d0-b48a59529439"` 属性中读到。该 UUID 指向数量单位的 master；应以 `unitId` 和有效 `unitContextId` 定位单位，不能把显示文本 kg 当作唯一身份。

**`@unitContextId`（FieldID 1031）**：字段 `unitContextId` 可在“教学示例：只含共同类型字段的交换”根元素的 `unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。此例显式给出单位上下文；读取该属性，与单位 UUID 一起保存；省略时按所在数据集的 `fileAttributes/@contextId` 回退，片段自身没有 fileAttributes，不能另猜上下文。

**`unitName`（FieldID 1035）**：字段 `unitName` 位于“教学示例：只含共同类型字段的交换”的直接子元素 `unitName` 中，示例值为 `kg / kg`。这里的 kg 是数量单位的冗余展示名称，两个语言版本都应保留；与 `unitId` 的 master 定义核对后才能进行可靠的单位换算。

**`@variableName`（FieldID 1040）**：字段 `variableName` 可在“教学示例：只含共同类型字段的交换”根元素的 `variableName="fossil_co2"` 属性中读到。`fossil_co2` 是公式引用交换数量时使用的变量名，不是流的 master 身份；读取为字符串，遵循以字母起始和不区分大小写的变量规则。

**`@isCalculatedAmount`（FieldID 1050）**：字段 `isCalculatedAmount` 可在“教学示例：只含共同类型字段的交换”根元素的 `isCalculatedAmount="true"` 属性中读到。`true` 表示记录的 amount 来自数学关系或传递系数的计算；读取标志与数值并列保存，标志本身既不提供公式结果，也不要求提取时重算。

**`@mathematicalRelation`（FieldID 1060）**：字段 `mathematicalRelation` 可在“教学示例：只含共同类型字段的交换”根元素的 `mathematicalRelation="0.15 * 10"` 属性中读到。字符串 `0.15 * 10` 展示如何记录产生 1.5 的数学关系；取数时保存原公式及 amount，涉及变量或 REF 时仍不执行 eval 或擅自解析成新的算法。

**`@casNumber`（FieldID 1100）**：字段 `casNumber` 可在“教学示例：只含共同类型字段的交换”根元素的 `casNumber="124-38-9"` 属性中读到。`124-38-9` 是此教学二氧化碳标签所用的 CAS 号，按字符串保留连字符；它辅助识别化学物质，但不能区分 ecoinvent 的来源、区室或 master 身份。

**`comment`（FieldID 1110）**：字段 `comment` 位于“教学示例：只含共同类型字段的交换”的直接子元素 `comment` 中，示例值为 `全部为教学构造；此处仅展示交换共用字段。 / Synthetic teaching example of shared exchange fields only.`。中英文 comment 明确限定为教学构造，并说明这里仅展示共同字段；应逐个读取评论文本及语言，用它解释数量的范围，不能把评论当作数量字段。

**`@sourceId`（FieldID 1120）**：字段 `sourceId` 可在“教学示例：只含共同类型字段的交换”根元素的 `sourceId="00000000-0000-4000-8000-000000001120"` 属性中读到。该 UUID 是教学来源 master 的引用；保存引用并结合 sourceContextId 查询有效来源，不因字段说明提到 modellingAndValidation 就把所有来源当作内嵌文字。

**`@sourceContextId`（FieldID 1121）**：字段 `sourceContextId` 可在“教学示例：只含共同类型字段的交换”根元素的 `sourceContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。此例的 sourceContextId 明确给出来源上下文；省略时采用文件上下文，取数时来源的 UUID 和 context 必须成对保留。

**`@sourceIdOverwrittenByChild`（FieldID 1122）**：字段 `sourceIdOverwrittenByChild` 可在“教学示例：只含共同类型字段的交换”根元素的 `sourceIdOverwrittenByChild="false"` 属性中读到。主例的 false 没有要求清除父来源引用；第二例 true 配合省略 sourceId 才展示子数据集显式清除父引用的标记。继承尚未展开时，缺失引用不能直接解释为无来源。

**`@sourceYear`（FieldID 1125）**：字段 `sourceYear` 可在“教学示例：只含共同类型字段的交换”根元素的 `sourceYear="2025"` 属性中读到。`2025` 是教学来源的出版或交流年份，网络来源则可表示最后访问年份；按字符串读取，不把它当作活动 timePeriod 或交换数量。

**`@sourceFirstAuthor`（FieldID 1126）**：字段 `sourceFirstAuthor` 可在“教学示例：只含共同类型字段的交换”根元素的 `sourceFirstAuthor="Demo A."` 属性中读到。`Demo A.` 表示教学来源第一作者的姓和名字缩写；现场测量或沟通型来源可对应交流者，需结合来源类型理解，不能据此推断活动生产者。

**`@pageNumbers`（FieldID 1130）**：字段 `pageNumbers` 可在“教学示例：只含共同类型字段的交换”根元素的 `pageNumbers="3-4"` 属性中读到。`3-4` 指教学来源中支持此记录的页码范围；保留字符串作为追溯信息，不按减法或两个数量处理。

**`@specificAllocationPropertyId`（FieldID 1150）**：字段 `specificAllocationPropertyId` 可在“教学示例：只含共同类型字段的交换”根元素的 `specificAllocationPropertyId="00000000-0000-4000-8000-000000001150"` 属性中读到。该 UUID 指向本交换的特定分配属性，并覆盖数据集的 masterAllocationPropertyId 默认值；只保存引用及上下文，不能仅据此字段自行实施分配。

**`@specificAllocationPropertyContextId`（FieldID 1151）**：字段 `specificAllocationPropertyContextId` 可在“教学示例：只含共同类型字段的交换”根元素的 `specificAllocationPropertyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。这是特定分配属性的 master 上下文，省略时回退文件 context；取数时和 specificAllocationPropertyId 一起用于定位属性。

**`@specificAllocationPropertyIdOverwrittenByChild`（FieldID 1152）**：字段 `specificAllocationPropertyIdOverwrittenByChild` 可在“教学示例：只含共同类型字段的交换”根元素的 `specificAllocationPropertyIdOverwrittenByChild="false"` 属性中读到。主例 false 保留通常的继承行为，第二例 true 加上省略 specificAllocationPropertyId 展示清除父分配属性引用的写法；必须先展开继承再判断最终有效引用。

**`transferCoefficient`（FieldID 1200）**：字段 `transferCoefficient` 对应“教学示例：只含共同类型字段的交换”的直接子元素 `transferCoefficient`，其中包含 `comment` 子元素。嵌套 transferCoefficient 的 amount=0.6 记录特定输入贡献到当前输出的份额，exchangeId 指向该输入交换实例；需读取整个子元素并在完整数据集中解析实例引用，0.6 不是当前交换的 kg 数量。

**`uncertainty`（FieldID 1300）**：字段 `uncertainty` 对应“教学示例：只含共同类型字段的交换”的直接子元素 `uncertainty`，其中包含 `lognormal` 子元素。嵌套 lognormal 明示 meanValue=1.5、mu=0.4054651081081644、variance=0.01 与含 pedigree 的方差 0.04；应保存 uncertainty 子树的分布类型和全部参数，不把两种方差或对数均值当作交换 amount。

**`property`（FieldID 1400）**：字段 `property` 对应“教学示例：只含共同类型字段的交换”的直接子元素 `property`，其中包含 `name` 子元素。property 的 name 为“教学比例属性 / Synthetic ratio property”，amount=1、unitName=kg/kg 仅是结构示意比例，不代表 CO₂ 的真实碳含量，propertyId 另指属性 master；逐个读取属性行，不把它和外层 amount=1.5 kg 混同，也不随交换参考数量归一化。

**`tag`（FieldID 1450）**：字段 `tag` 位于“教学示例：只含共同类型字段的交换”的直接子元素 `tag` 中，示例值为 `synthetic-teaching`。`synthetic-teaching` 是开放关键词，读取所有 tag 用于筛选和分组；不在预定义标签清单中按原规范应提示信息，而不能仅因此判整个记录非法。

**`synonym`（FieldID 1470）**：字段 `synonym` 位于“教学示例：只含共同类型字段的交换”的直接子元素 `synonym` 中，示例值为 `教学化石二氧化碳 / Synthetic fossil carbon dioxide / 教学 CO2`。这里有两个中文 synonym 和一个英文 synonym，展示同一种 xml:lang 可以重复；应保留全部同义词而非以语言作字典键覆盖前项。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/exchanges-01.xml").getroot()
FIELDS = {
    "1000": "name",
    "1005": "@id",
    "1020": "@amount",
    "1030": "@unitId",
    "1031": "@unitContextId",
    "1035": "unitName",
    "1040": "@variableName",
    "1050": "@isCalculatedAmount",
    "1060": "@mathematicalRelation",
    "1100": "@casNumber",
    "1110": "comment",
    "1120": "@sourceId",
    "1121": "@sourceContextId",
    "1122": "@sourceIdOverwrittenByChild",
    "1125": "@sourceYear",
    "1126": "@sourceFirstAuthor",
    "1130": "@pageNumbers",
    "1150": "@specificAllocationPropertyId",
    "1151": "@specificAllocationPropertyContextId",
    "1152": "@specificAllocationPropertyIdOverwrittenByChild",
    "1200": "transferCoefficient",
    "1300": "uncertainty",
    "1400": "property",
    "1450": "tag",
    "1470": "synonym",
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
LOCATIONS = ['es:flowData/es:intermediateExchange', 'es:flowData/es:elementaryExchange']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

先统一读取交换实例 id、amount、unitId、name、unitName 及计算标记，再结合具体中间交换或基本流节点读取方向与对象身份。这里读取的 property、uncertainty 等仍属于当前交换，不能把子结构里的 amount 混进交换量总和。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange`；`flowData/elementaryExchange`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TCustomExchange")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **6 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/intermediateExchange[1]",
  "attributes": {
    "id": "b8754d71-a0c7-5b08-a889-67d6f1146d58",
    "amount": "10",
    "unitId": "a4800e12-54b1-5444-a6d0-b48a59529439",
    "intermediateExchangeId": "c5a1fe25-46d4-5646-9d78-5c10b6bfdeae"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学产品"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching product"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tcustomexchange)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
