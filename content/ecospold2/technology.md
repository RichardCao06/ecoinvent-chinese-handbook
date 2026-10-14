# 技术（TTechnology）

源文分组：Technology。本章完整收录 **2 条字段定义**。

XML 位置：`activityDescription/technology`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

描述已收集数据所对应的技术。文本应包含识别活动数据所依据技术的属性和特征所需的信息。

### `@technologyLevel` · FieldID 500 <a href="#field-500" id="field-500"></a>

局部 XML 位置：`TTechnology/@technologyLevel`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 否 | 否 | 否 | 否 |

对所描述活动的技术进行大致分类的标签，可在建模时用于选择具有特定技术水平的过程。所用代码如下：0=未指定（Undefined）。用于没有技术水平的市场活动。1=新兴（New）。用于在某些方面被认为技术上优于现代技术，但在投资纯粹依据经济考虑时尚未成为最普遍安装选择的技术。2=现代（Modern）。用于在投资纯粹依据经济考虑时，当前新增产能所采用的技术（最有竞争力的技术）。3=当前（Current，默认）。用于介于现代和旧有之间的技术。4=旧有（Old）。用于在退役纯粹依据经济考虑时，当前正在退出使用的技术（竞争力最低的技术）。5=过时（Outdated）。用于已不再使用的技术。这些术语并不一定反映技术的年代。如果一项技术仍最有竞争力，即使已有百年历史，也可以属于现代技术；如果一项技术很快被其他更有竞争力的技术取代，即使出现时间相对较短，也可以属于旧有技术。技术水平是相对于“时间段”（Time Period）所给数据有效年份而言的。在时间序列中，同一技术的技术水平可随时间改变。即使在同一年，同一技术在不同地理位置也可被赋予不同技术水平。

**取值选项（原表）：** 0 = 未指定（undefined）, 1 = 新兴（New）, 2 = 现代（Modern）, 3 = 当前（Current，默认）, 4 = 旧有（Old）, 5 = 过时（Outdated）

**XSD 结构约束：** `use="optional"`；`default="3"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTechnology`。

### `comment` · FieldID 510 <a href="#field-510" id="field-510"></a>

局部 XML 位置：`TTechnology/comment`；ecoSpold1 对照编号：`692`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TTextAndImage` | — | 否 | 否 | 是 | 否 |

用于描述活动技术的文本和图像字段。文本应包含识别活动数据所依据技术的属性和特征所需的信息，描述该单元过程的技术属性。如果活动包含多个子活动，也应报告相应技术。描述应使用专业命名。文本和图像字段是 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。

text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。

复合类型详情：[ `TTextAndImage` ](text-and-image.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTechnology`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Contains a description of the technology for which data has been collected. The text should cover information necessary to identify the properties and particularities of the technology(ies) underlying the activity data.

### `@technologyLevel` · FieldID 500 <a href="#en-field-500" id="en-field-500"></a>

Local XML path：`TTechnology/@technologyLevel`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | No | No | No | No |

Label that grossly classifies the technology of the described activity and can be used in modelling to select processes with a specific technological level. The codes used are:0=Undefined. For market activities that do not have a technology level.1=New. For a technology assumed to be on some aspects technically superior to modern technology, but not yet the most commonly installed when investment is based on purely economic considerations.2=Modern. For a technology currently used when installing new capacity, when investment is based on purely economic considerations (most competitive technology). 3=Current (default). For a technology in between modern and old.4=Old. For a technology that is currently taken out of use, when decommissioning is based on purely economic considerations (least competitive technology).5=Outdated. For a technology no longer in use.The terms used does not necessarily reflect the age of the technologies. A modern technology can be a century old, if it is still the most competitive technology, and an old technology can be relatively young, if it is one that has quickly become superseded by other more competitive ones. The technology level is relative to the year for which the data are valid, as given under Time Period. In a time series, the same technology can move between different technology levels over time. The same technology can also be given different technology levels in different geographical locations, even in the same year.

**Options (original table)：** 0 = undefined, 1 = New, 2 = Modern, 3 = Current (default), 4 = Old, 5 = Outdated

**XSD structural constraints：** `use="optional"`；`default="3"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTechnology`。

### `comment` · FieldID 510 <a href="#en-field-510" id="en-field-510"></a>

Local XML path：`TTechnology/comment`；ecoSpold1 mapping：`692`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TTextAndImage` | — | No | No | Yes | No |

Text and image field to describe the technology of the activity. The text should cover information necessary to identify the properties and particularities of the technology(ies) underlying the activity data. Describes the technological properties of the unit process. If the activity comprises several subactivities, the corresponding technologies should be reported as well. Professional nomenclature should be used for the description.Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

List of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

Complex type details：[ `TTextAndImage` ](text-and-image.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTechnology`。

{% endtab %}

{% endtabs %}
