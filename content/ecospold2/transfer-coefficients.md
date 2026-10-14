# 转移系数

对应官方格式类型：`TTransferCoefficient`。本篇以文章解释该类型的 11 条字段；复合类型也会说明它们依附在哪个对象上。

## 转移系数：追踪特定投入对特定输出的贡献 <a href="#read-ttransfercoefficient" id="read-ttransfercoefficient"></a>

转移系数将一项特定投入与一项特定输出关联，记录该投入对该输出的贡献份额，用于根据投入量计算相应的输出贡献。在 XSD 中，`transferCoefficient` 定义在 `TCustomExchange` 内，因此中间交换和基本流交换都可以通过继承包含它，不能把它限制为只供中间产品使用。阅读时应同时保留容纳系数的交换和被引用交换的身份，才能知道所描述的是哪一条投入输出关系。

`exchangeId` 引用的是某个具体交换的 UUID，即交换实例的 `id`，不是产品主数据的 `intermediateExchangeId` 或基本流主数据的 `elementaryExchangeId`。同一主数据条目可能在同一个数据集中被多项交换引用，所以两种身份不能混用。系数自身的 `amount` 是转移系数数值；原说明要求将它与所引用交换的数量相乘，以得到该系数对应的数量贡献。这个 `amount` 不是另一笔投入量，也不是不加区分地分配整个过程环境影响的因子。不能仅凭一个系数的存在，就推出完整质量平衡、输出总量或通用过程计算算法。

`mathematicalRelation` 可以通过变量名或 `REF` 引用流、参数和属性来计算系数，结果写入这个系数的 `amount`；`isCalculatedAmount` 为 true 时表示该值是数学关系的计算结果。可选的 `uncertainty` 描述系数数值的不确定性，应与被引用交换数量的不确定性区分。取数时，可以读取已存系数与它的引用对象；若要进一步重新计算，必须另行处理引用、公式和不确定性，不能把它们合并成一个未经格式说明支持的计算规则。

证据链由 `sourceId`、`sourceContextId`、`sourceYear` 和 `sourceFirstAuthor` 组成。`sourceId` 指向有效来源，原选项说明将其关联到 `modellingAndValidation` 部分定义的来源；`sourceContextId` 指定来源的上下文，省略时使用数据集上下文；`sourceYear` 是出版或交流年份，网站记录最后访问；`sourceFirstAuthor` 是第一作者姓氏和名字缩写，现场测量、口头交流、个人书面交流和问卷调查，即 `sourceType` 为 4、5、6、7 时，则填写提供信息的人员。在子数据集中移除继承的来源引用，需要将 `sourceIdOverwrittenByChild` 设为 true，否则移除会被解释为保留父值。`comment` 用于每个系数的补充说明，读取时应与该系数而非其他交换的说明关联。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学输入份额及系数的来源

[下载本段 XML](xml-examples/transfer-coefficients-01.xml)。

```xml
<transferCoefficient xmlns="http://www.EcoInvent.org/EcoSpold02" exchangeId="00000000-0000-4000-8000-000000000104" amount="0.25" mathematicalRelation="0.5 * 0.5" isCalculatedAmount="true" sourceId="00000000-0000-4000-8000-000000000103" sourceContextId="00000000-0000-4000-8000-000000000100" sourceIdOverwrittenByChild="false" sourceYear="2025" sourceFirstAuthor="Example A.">
  <uncertainty><uniform minValue="0.2" maxValue="0.3"/></uncertainty>
  <comment xml:lang="zh">教学约定：exchangeId 指同一活动中被引用的投入交换实例；外层是接收这部分投入的输出交换。所有 UUID 和来源均虚构。</comment>
</transferCoefficient>
```

该完整片段位于交换的 transferCoefficient 子节点；两类交换通过 TCustomExchange 都可拥有它。教学约定被引用投入有 40 个已确认单位，则 0.25 的份额对应 10 个同口径单位的贡献，这只是解释引用语义，不是计算一个完整产品系统。exchangeId 指交换实例而非产品/基本流主数据。

### 示例 2：系数未给计算标记及显式来源删除

[下载本段 XML](xml-examples/transfer-coefficients-02.xml)。

```xml
<transferCoefficient xmlns="http://www.EcoInvent.org/EcoSpold02" exchangeId="00000000-0000-4000-8000-000000000104" amount="0.25" sourceIdOverwrittenByChild="true">
  <comment xml:lang="zh">教学属性语法：删除标记需要结合真实子数据集父引用解释；省略计算标记没有 XSD 默认值。</comment>
</transferCoefficient>
```

本例省略 isCalculatedAmount，与属性类型不同，这个转移系数字段没有 XSD default=false，读取器应保留缺失状态。sourceIdOverwrittenByChild=true 演示删除父来源标记；片段不是一份完整子数据集，也不证明所指投入已存在。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@exchangeId`（FieldID 2400）**：`transferCoefficient/@exchangeId="00000000-0000-4000-8000-000000000104"` 引用教学投入交换实例。应在同一活动的交换 id 中查找它，并确认方向与物质口径；不能按 intermediateExchangeId 或 elementaryExchangeId 查产品主数据代替。

**`@amount`（FieldID 2410）**：`@amount="0.25"` 是分给当前输出的投入份额，按原说明乘被引用交换的 amount。它不是外层输出量，也不是一个新投入；单位和守恒关系须结合被引用实例及具体用途确认。

**`@mathematicalRelation`（FieldID 2420）**：`@mathematicalRelation="0.5 * 0.5"` 保存系数 0.25 的数学关系。实际可引用变量或 REF，但这个示例用常量避免未定义参数；读取器只保存字符串。

**`@isCalculatedAmount`（FieldID 2425）**：主例 `@isCalculatedAmount="true"` 声明系数值由公式计算；第二例省略此标记时没有模式默认值。不能照搬 TProperty 的 default=false，也不能因为有公式就自行更改标记。

**`uncertainty`（FieldID 2430）**：`transferCoefficient/uncertainty/uniform` 的 0.2 和 0.3 表达系数量的不确定区间。它属于系数 amount，不应附到被引用交换的数量或年度产量上。

**`@sourceId`（FieldID 2440）**：主例 `@sourceId="00000000-0000-4000-8000-000000000103"` 指向教学来源主数据，说明系数依据。只有引用字符串不等于来源已在真实上下文中解析；示例不虚构真实文献。

**`@sourceContextId`（FieldID 2441）**：`@sourceContextId="00000000-0000-4000-8000-000000000100"` 限定来源的教学上下文。省略时采用数据集自身上下文，保留它与 sourceId 的配对，别使用投入交换的主数据上下文替代。

**`@sourceIdOverwrittenByChild`（FieldID 2442）**：主例 `@sourceIdOverwrittenByChild="false"` 不要求删除，第二例 true 且省略 sourceId 表示显式移除父来源的机制。子继承须先定位对应系数，不能把“没写来源”自动视作删除。

**`@sourceYear`（FieldID 2445）**：`@sourceYear="2025"` 是教学来源年份，网站来源可记录最后访问时点。它不表示系数适用期间，后者需结合活动时间与说明判断。

**`@sourceFirstAuthor`（FieldID 2446）**：`@sourceFirstAuthor="Example A."` 是教学作者冗余文本，或特定沟通来源的沟通者。读取时与来源 UUID 分开保存，不能以同名作者合并系数。

**`comment`（FieldID 2450）**：`transferCoefficient/comment` 说明被引用投入和外层接收输出的角色。它是普通字符串；应连同系数的父交换路径保存，才能知道 0.25 为谁分配了哪笔投入。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/transfer-coefficients-01.xml").getroot()
FIELDS = {
    "2400": "@exchangeId",
    "2410": "@amount",
    "2420": "@mathematicalRelation",
    "2425": "@isCalculatedAmount",
    "2430": "uncertainty",
    "2440": "@sourceId",
    "2441": "@sourceContextId",
    "2442": "@sourceIdOverwrittenByChild",
    "2445": "@sourceYear",
    "2446": "@sourceFirstAuthor",
    "2450": "comment",
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
LOCATIONS = ['es:flowData/es:intermediateExchange/es:transferCoefficient', 'es:flowData/es:elementaryExchange/es:transferCoefficient']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要追踪某投入对某输出的贡献时，读取交换下的 transferCoefficient，保留外层交换 id 及内部 exchangeId 等引用。这个读取例子保存系数与表达式，不执行贡献计算；先弄清它引用的是哪个交换实例，而非把主数据 UUID 当成实例 id。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange/transferCoefficient`；`flowData/elementaryExchange/transferCoefficient`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TTransferCoefficient")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-ttransfercoefficient)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
