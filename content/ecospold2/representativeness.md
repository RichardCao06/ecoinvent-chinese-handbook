# 代表性

对应官方格式类型：`TRepresentativeness`。本篇以文章解释该类型的 6 条字段；复合类型也会说明它们依附在哪个对象上。

## 代表性：理解数据代表的总体，以及样本如何形成 <a href="#read-trepresentativeness" id="read-trepresentativeness"></a>

`representativeness` 位于 `modellingAndValidation` 中，采用 `TRepresentativeness` 类型，记录数据集的代表性和数据如何采样或计算。它帮助读者判断数据能否服务于研究中的地区、技术和时间条件，而不是为每项交换提供一个新的数量。首先，`systemModelId` 引用所用系统模型，`systemModelContextId` 指定该模型的上下文，省略时采用数据集自身的上下文；`systemModelName` 是该引用的纯文本名称。这些信息说明活动数据集如何链接成产品系统。原文举出的 `undefined`、`attributional, average current suppliers, revenue allocation` 和 `consequential, small-scale, long-term decisions` 是该历史格式说明中的模型描述，不能未经核对就视为当前全部系统模型名称或完整清单。在正常 XSD 中，只要此可选结构出现，模型引用和模型名称便是其内部必填项。

`percent` 表示所采样数据占活动拟代表总体的百分比。该总体由地理区域、技术和时间范围共同确定，因此读取百分比之前，要先知道它针对的是哪个总体；它不是这个活动对产品系统的贡献率，也不是供应市场的份额。原表和 XSD 都将最大值规定为 100，但未填写这一可选属性，不代表覆盖比例为零或百分之百。

`samplingProcedure` 描述量化交换所用的采样和计算程序，应说明某些基本流交换或中间交换是否采用不同于一般程序的做法，以及组合不同采样程序可能产生的问题。这里有一个需要对照模式的源文疑点：英文说明随后混入了文本和图像字段的通用描述，但实际 XSD 把 `samplingProcedure` 定义为 `TString32000` 多语言文本，而不是 `TTextAndImage`。读取它应保留文本和语言，不应因为这段通用说明就尝试读取嵌套的 `text`、`imageUrl` 或 `variable`。

`extrapolations` 记录数据从其他时间、其他地理区域或其他技术外推而来的情况，以及外推如何实施。说明应交代单个交换是否采用不同的外推方法；如果把一个国家运行活动的数据用于另一个国家，可以在这里注明原始代表性，并记录外推引起的均值变化。读取这段内容后，才能把样本覆盖、原始来源和当前适用范围联系起来；不能仅因模型名称或地区代码符合要求，就跳过采样及外推说明。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学系统模型与样本代表性

[下载本段 XML](xml-examples/representativeness-01.xml)。

```xml
<representativeness xmlns="http://www.EcoInvent.org/EcoSpold02" systemModelId="00000000-0000-4000-8000-000000000105" systemModelContextId="00000000-0000-4000-8000-000000000100" percent="60">
  <systemModelName xml:lang="zh">教学链接约定（非官方模型）</systemModelName>
  <samplingProcedure xml:lang="zh">教学设定：在所声明地域、技术与时间范围内采集部分场所数据；电力用计量记录，物料用质量核算，组合时核对口径。</samplingProcedure>
  <extrapolations xml:lang="zh">教学设定：部分物料信息由另一期间外推；电力未采用该外推，均值调整须另记依据。</extrapolations>
</representativeness>
```

所有 UUID、覆盖率和采样叙述均为教学构造。percent=60 以百分值表示相对所代表总体的覆盖，不是把全部交换乘 0.6 的比例。samplingProcedure 和 extrapolations 在本版 XSD 都是普通字符串，尽管原文前者夹有富文本模板说明，不应套用 text/imageUrl 子结构。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@systemModelId`（FieldID 3000）**：`representativeness/@systemModelId="00000000-0000-4000-8000-000000000105"` 是教学链接约定的模型 UUID。它限定过程如何组成产品系统；查主数据时不能根据名称把它当作正式 ecoinvent 模型。

**`@systemModelContextId`（FieldID 3001）**：`@systemModelContextId="00000000-0000-4000-8000-000000000100"` 给出模型主数据的教学上下文。省略时使用数据集自身上下文；如果后者也未知，模型身份不能被确认匹配。

**`systemModelName`（FieldID 3005）**：`systemModelName` 的文本为“教学链接约定（非官方模型）”，它是模型引用的冗余显示名。读取语言与文本，但供应候选比较仍依赖模型 UUID 和有效上下文。

**`@percent`（FieldID 3010）**：`@percent="60"` 表示对所声明地域、技术、时间总体的教学采样覆盖率为 60%。它不是 0.60 的字段存储方式，也不是交换归一化系数；不应据此放大或缩小清单。 本版 XSD 明确限制最大值为 100，但未在该限制中另给最小值；类型校验与采样语义仍应分别判断。

**`samplingProcedure`（FieldID 3030）**：`samplingProcedure` 说明教学电力与物料的采样/核算方法及组合口径。按这个普通字符串的 `.text` 和语言读取；本版 XSD 为 TString32000，不能因原文富文本模板而添加 text 子节点。

**`extrapolations`（FieldID 3040）**：`extrapolations` 指出哪些教学物料由另一期间外推、哪些电力没有这样处理。应逐交换结合依据理解均值变化；它是普通字符串，不是自动执行外推的公式或新的交换量。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/representativeness-01.xml").getroot()
FIELDS = {
    "3000": "@systemModelId",
    "3001": "@systemModelContextId",
    "3005": "systemModelName",
    "3010": "@percent",
    "3030": "samplingProcedure",
    "3040": "extrapolations",
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
LOCATIONS = ['es:modellingAndValidation/es:representativeness']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要解释系统模型、样本总体或外推依据时，读取 representativeness 的全部字段，尤其保留 systemModelId 与上下文。比较数量之前先核对模型；百分比或外推描述是代表性元数据，不是清单中另一项数量。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`modellingAndValidation/representativeness`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TRepresentativeness")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/modellingAndValidation[1]/representativeness[1]",
  "attributes": {
    "systemModelId": "a381359e-f5e9-58f7-90b2-e0f2251938a1",
    "systemModelContextId": "f71ac544-3bc8-5c15-8ea4-072d907663f1"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}systemModelName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学约定系统（非官方模型）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}systemModelName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching convention (not an official model)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-trepresentativeness)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
