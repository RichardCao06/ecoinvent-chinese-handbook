# 影响指标结果

对应官方格式类型：`TImpactIndicatorResult`。本篇以文章解释该类型的 11 条字段；复合类型也会说明它们依附在哪个对象上。

## 影响评价结果不是一条环境排放 <a href="#read-timpactindicatorresult" id="read-timpactindicatorresult"></a>

`TImpactIndicatorResult` 保存已经计算出的影响指标结果。它的必需字段 `amount` 是指标值，不是某种污染物的排放量，也不是未表征的资源消耗量；即使字段名与交换数量相同，读数含义也由所在类型决定。提取 LCIA 结果时，需要同时保留方法、类别、指标和单位，不能只取出一列数值，也不能把这些结果与基本流交换相加。

一条结果包含三层必需的主数据标识。`impactMethodId` 引用影响评价方法；`impactCategoryId` 按 XSD 引用方法中的影响类别；`impactIndicatorId` 引用具体影响指标。它们分别回答采用什么方法、结果属于什么类别、使用什么指标。这些 ID 均为 UUID，不能因显示名称近似而互相替代。原表字段 1820 的说明写作“对影响类别所属方法的引用”，但其 XSD 引用对象为 `TImpactMethodCategory`，与 `impactMethodId` 的 `TImpactMethod` 不同；这项源文矛盾已在审阅中记录，此处明确区分实际的类别引用与方法引用，没有改写原表译文。

可选的 `impactMethodContextId`、`impactCategoryContextId` 和 `impactIndicatorContextId` 分别指定方法、类别和指标主数据所在上下文，任何一个省略时，都使用数据集自身的上下文。结果也包含便于阅读的必需多语言文本：`impactMethodName` 为方法名称，`impactCategoryName` 为类别名称，`name` 为指标名称，`unitName` 为指标值的单位名称。选择语言时应按 `xml:lang` 读取这些名称，不应把多语言版本当成多条独立结果。

因此，读 LCIA 结果的一条可靠路径，是先用方法、类别和指标的标识及上下文确定这条结果的身份，再把 `amount` 与 `unitName` 配对，最后核对活动、产品和系统模型等外部背景及参考数量基准。这个类型自身没有交换的 `inputGroup`、`outputGroup`，也没有为结果另列 `unitId`；不能照搬读取排放交换的字段路径。不同方法、不同指标、不同单位或不同参考基准的结果，应先确认可比性，不能只因中文名称相似就合并或比较。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学示例：13.9 kg CO2-eq 的模拟指标结果

[下载本段 XML](xml-examples/impact-indicators-01.xml)。

```xml
<impactIndicator xmlns="http://www.EcoInvent.org/EcoSpold02" impactIndicatorId="9ce9802d-268d-5ac0-af08-ffca6dc91aa2" impactMethodId="496741dc-72ec-5f95-bedb-078512fde969" impactCategoryId="07a7bfca-c863-5fd0-a2bf-24aa3af0d959" amount="13.9" impactIndicatorContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" impactMethodContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" impactCategoryContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
        <impactMethodName xml:lang="zh">教学方法（非官方）</impactMethodName>
        <impactMethodName xml:lang="en">Teaching method (synthetic, unofficial)</impactMethodName>
        <impactCategoryName xml:lang="zh">教学化石CO2类别</impactCategoryName>
        <impactCategoryName xml:lang="en">Teaching fossil CO2 category</impactCategoryName>
        <name xml:lang="zh">教学GWP（构造）</name>
        <name xml:lang="en">Teaching GWP (synthetic)</name>
        <unitName xml:lang="zh">kg CO2-eq</unitName>
        <unitName xml:lang="en">kg CO2-eq</unitName>
      </impactIndicator>
```

片段从教学结果文件取出并显式补全三层 master 上下文。方法、类别、指标均为构造标识，Teaching GWP (synthetic) 不代表官方影响方法。amount=13.9 是已提供的指标结果，不是排放交换，也没有 inputGroup/outputGroup 或 unitId。与完整教学文件中的 10 kg 参考输出配合时，只能给出 13.9/10=1.39 的算术比例；片段本身不含参考产品，不能自行推断分母。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@impactIndicatorId`（FieldID 1800）**：字段 `impactIndicatorId` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `impactIndicatorId="9ce9802d-268d-5ac0-af08-ffca6dc91aa2"` 属性中读到。该 UUID 指向具体教学影响指标 master；与方法和类别 UUID 一起保存以免同名指标混淆，不能当成 elementaryExchangeId。

**`@impactIndicatorContextId`（FieldID 1801）**：字段 `impactIndicatorContextId` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `impactIndicatorContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。它界定教学指标 master 的上下文，省略时回退 file context；指标 ID 与其 context 成对提取，不能只存展示名称。

**`@impactMethodId`（FieldID 1810）**：字段 `impactMethodId` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `impactMethodId="496741dc-72ec-5f95-bedb-078512fde969"` 属性中读到。这个 UUID 引用教学影响方法 master，是方法层而非指标层标识；与类别、指标分层保存，此例并不是官方影响方法。

**`@impactMethodContextId`（FieldID 1811）**：字段 `impactMethodContextId` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `impactMethodContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。此属性指定方法 master 的上下文，省略时回退文件 context；需要与 impactMethodId 配对，不能因教学例三种 context 相同就丢弃层级。

**`impactMethodName`（FieldID 1815）**：字段 `impactMethodName` 位于“教学示例：13.9 kg CO2-eq 的模拟指标结果”的直接子元素 `impactMethodName` 中，示例值为 `教学方法（非官方） / Teaching method (synthetic, unofficial)`。中英文 impactMethodName 明确为构造教学方法，是方法层展示名称；保留全部语言并以方法 UUID/context 核对，不根据名称自动套用真实 GWP 因子。

**`@impactCategoryId`（FieldID 1820）**：字段 `impactCategoryId` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `impactCategoryId="07a7bfca-c863-5fd0-a2bf-24aa3af0d959"` 属性中读到。该 UUID 引用影响类别 master；原文把说明写成“method of the impact category”的措辞不精确，此处按字段名和 schema 的类别引用读取，不将它替代 impactMethodId。

**`@impactCategoryContextId`（FieldID 1821）**：字段 `impactCategoryContextId` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `impactCategoryContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。它给出类别 master 上下文，省略时回退文件 context；单独保留，与方法和指标上下文各自对应。

**`impactCategoryName`（FieldID 1825）**：字段 `impactCategoryName` 位于“教学示例：13.9 kg CO2-eq 的模拟指标结果”的直接子元素 `impactCategoryName` 中，示例值为 `教学化石CO2类别 / Teaching fossil CO2 category`。impactCategoryName 展示“教学化石CO2类别”的中英文标签；名称供展示和分类，指标结果的身份仍要保留类别 UUID/context。

**`@amount`（FieldID 1830）**：字段 `amount` 可在“教学示例：13.9 kg CO2-eq 的模拟指标结果”根元素的 `amount="13.9"` 属性中读到。13.9 是已经给定的指标结果，展示单位为 kg CO2-eq，不是排放交换质量。只有结合完整例中唯一正参考输出 10 kg 才能读出算术比例 1.39；不能由此片段自行重做 LCIA。

**`name`（FieldID 1840）**：字段 `name` 位于“教学示例：13.9 kg CO2-eq 的模拟指标结果”的直接子元素 `name` 中，示例值为 `教学GWP（构造） / Teaching GWP (synthetic)`。name 中的 Teaching GWP (synthetic) 是具体指标标签，区别于 impactMethodName 和 impactCategoryName；读取全部语言，同时保留三层 master 引用。

**`unitName`（FieldID 1850）**：字段 `unitName` 位于“教学示例：13.9 kg CO2-eq 的模拟指标结果”的直接子元素 `unitName` 中，示例值为 `kg CO2-eq / kg CO2-eq`。kg CO2-eq 是指标结果的展示单位；TImpactIndicatorResult 没有 unitId/unitContextId 属性，不要补造这两项，真实结果的单位应结合指标 master 定义确认。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/impact-indicators-01.xml").getroot()
FIELDS = {
    "1800": "@impactIndicatorId",
    "1801": "@impactIndicatorContextId",
    "1810": "@impactMethodId",
    "1811": "@impactMethodContextId",
    "1815": "impactMethodName",
    "1820": "@impactCategoryId",
    "1821": "@impactCategoryContextId",
    "1825": "impactCategoryName",
    "1830": "@amount",
    "1840": "name",
    "1850": "unitName",
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

dataset = load_dataset("demo-lcia.spold", index=0)
LOCATIONS = ['es:flowData/es:impactIndicator']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

要拿已有碳足迹等结果，读取 impactIndicator，以方法、类别、指标三层 UUID 及有效上下文筛选，再保留 amount 与 unitName。该类型没有独立 unitId 字段，不能凭名称补出 UUID；文件没提供指标时应返回缺失，不能用 CO2 质量冒充影响结果。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/impactIndicator`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-lcia.spold", index=0)
records = read_section(dataset, "TImpactIndicatorResult")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-lcia.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/impactIndicator[1]",
  "attributes": {
    "impactIndicatorId": "9ce9802d-268d-5ac0-af08-ffca6dc91aa2",
    "impactMethodId": "496741dc-72ec-5f95-bedb-078512fde969",
    "impactCategoryId": "07a7bfca-c863-5fd0-a2bf-24aa3af0d959",
    "amount": "13.9"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}impactMethodName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学方法（非官方）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}impactMethodName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching method (synthetic, unofficial)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-timpactindicatorresult)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
