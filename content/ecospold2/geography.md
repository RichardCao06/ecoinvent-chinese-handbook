# 地理区域（TGeography）

源文分组：Geography。本章完整收录 **4 条字段定义**。

XML 位置：`activityDescription/geography`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

包含过程地理适用范围的信息。地理区域可以是活动所在的点位置、描述移动活动的一条线，或分布式活动或生产组合覆盖的区域；该区域包含多个位于具体地点的活动。对于市场（消费组合），地理区域描述市场边界，跨越这些边界的进口和出口受到限制。

### `@geographyId` · FieldID 400 <a href="#field-400" id="field-400"></a>

局部 XML 位置：`TGeography/@geographyId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用有效地点文件，该文件包含详细的地理区域信息。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

### `@geographyContextId` · FieldID 401 <a href="#field-401" id="field-401"></a>

局部 XML 位置：`TGeography/@geographyContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用该地理区域所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

### `shortname` · FieldID 410 <a href="#field-410" id="field-410"></a>

局部 XML 位置：`TGeography/shortname`；ecoSpold1 对照编号：`662`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString40` | 是 | 否 |

长度：40；多语言：是；主数据冗余字段：是。

geographyId 所引用地点的描述性简称，例如 EcoSpold 第 1 版的地区代码。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

### `comment` · FieldID 420 <a href="#field-420" id="field-420"></a>

局部 XML 位置：`TGeography/comment`；ecoSpold1 对照编号：`663`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TTextAndImage` | 否 | 否 |

长度：—；多语言：是；主数据冗余字段：否。

用于进一步解释地理区域的文本和图像字段。尤其在描述区域时，可以说明地理边界划定的性质，特别是在该区域不是行政区的情况下。这里也可提供市场边界的划定依据。文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。

文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。

复合类型详情：[ `TTextAndImage` ](text-and-image.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Contains information about the geographic validity of the process. The geography may be the point location of the activity, a line describing a mobile activity, or an area of a distributed activity or of a production mix, containing several located activities. For markets (consumption mixes), the geography describes the market boundaries, across which imports and exports are limited.

### `@geographyId` · FieldID 400 <a href="#en-field-400" id="en-field-400"></a>

Local XML path：`TGeography/@geographyId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to valid locations file with detailed geography information.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

### `@geographyContextId` · FieldID 401 <a href="#en-field-401" id="en-field-401"></a>

Local XML path：`TGeography/@geographyContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the geography.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

### `shortname` · FieldID 410 <a href="#en-field-410" id="en-field-410"></a>

Local XML path：`TGeography/shortname`；ecoSpold1 mapping：`662`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString40` | Yes | No |

Size：40；Multi language：Yes；Redundant master data：Yes。

Descriptive shortname of the location referenced by geographyId, e.g. the regional codes of EcoSpold version 1.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

### `comment` · FieldID 420 <a href="#en-field-420" id="en-field-420"></a>

Local XML path：`TGeography/comment`；ecoSpold1 mapping：`663`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TTextAndImage` | No | No |

Size：—；Multi language：Yes；Redundant master data：No。

Text and image field for further explanations of the geography. Especially for area descriptions, the nature of the geographical delimitation may be given, especially when this is not an administrative area. Justifications for market boundaries may also be provided here.Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

List of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

Complex type details：[ `TTextAndImage` ](text-and-image.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TGeography`。

{% endtab %}

{% endtabs %}
