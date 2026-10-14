# 时间范围（TTimePeriod）

源文分组：Time period。本章完整收录 **4 条字段定义**。

XML 位置：`activityDescription/timePeriod`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

描述数据集有效时间段的开始日期和结束日期。

### `@startDate` · FieldID 600 <a href="#field-600" id="field-600"></a>

局部 XML 位置：`TTimePeriod/@startDate`；ecoSpold1 对照编号：`601`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `date` | — | 是 | 否 | 否 | 否 |

数据集有效时间段的开始日期，以完整日期（年-月-日）表示。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

### `@endDate` · FieldID 610 <a href="#field-610" id="field-610"></a>

局部 XML 位置：`TTimePeriod/@endDate`；ecoSpold1 对照编号：`602`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `date` | — | 是 | 否 | 否 | 否 |

数据集有效时间段的结束日期，以完整日期（年-月-日）表示。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

### `@isDataValidForEntirePeriod` · FieldID 620 <a href="#field-620" id="field-620"></a>

局部 XML 位置：`TTimePeriod/@isDataValidForEntirePeriod`；ecoSpold1 对照编号：`603`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 是 | 否 | 否 | 否 |

表示活动数据（在流数据下报告的基本流交换和中间交换）是否在所述整个时间段内有效。如果不是，可在“comment”中说明。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

### `comment` · FieldID 630 <a href="#field-630" id="field-630"></a>

局部 XML 位置：`TTimePeriod/comment`；ecoSpold1 对照编号：`611`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TTextAndImage` | — | 否 | 否 | 是 | 否 |

用于进一步说明所报告数据时间有效性的文本和图像字段。例如，可包括以下信息：
\- 所涉及单元过程的时间相关性有多强（例如，4 年前的数据是否仍适用于今天运行的活动）；
\- 数据为何不在整个时间段内有效，以及数据在哪些较短时间段内有效。
文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

复合类型详情：[ `TTextAndImage` ](text-and-image.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Describes start and end date of the time period for which the dataset is valid.

### `@startDate` · FieldID 600 <a href="#en-field-600" id="en-field-600"></a>

Local XML path：`TTimePeriod/@startDate`；ecoSpold1 mapping：`601`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `date` | — | Yes | No | No | No |

Start date of the time period for which the dataset is valid, presented as a complete date (year-month-day).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

### `@endDate` · FieldID 610 <a href="#en-field-610" id="en-field-610"></a>

Local XML path：`TTimePeriod/@endDate`；ecoSpold1 mapping：`602`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `date` | — | Yes | No | No | No |

End date of the time period for which the dataset is valid, presented as a complete date (year-month-day).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

### `@isDataValidForEntirePeriod` · FieldID 620 <a href="#en-field-620" id="en-field-620"></a>

Local XML path：`TTimePeriod/@isDataValidForEntirePeriod`；ecoSpold1 mapping：`603`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | Yes | No | No | No |

Indicates whether or not the activity data (elementary and intermediate exchanges reported under flow data) are valid for the entire time period stated. If not, explanations may be given under 'comment'.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

### `comment` · FieldID 630 <a href="#en-field-630" id="en-field-630"></a>

Local XML path：`TTimePeriod/comment`；ecoSpold1 mapping：`611`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TTextAndImage` | — | No | No | Yes | No |

Text and image field for additional explanations concerning the temporal validity of the data reported. It may e.g. include information about:- how strong the temporal correlation is for the unit process at issue (e.g., are four year old data still adequate for the activity operated today?),- why data is not valid for the entire period, and for which smaller periods data are then valid. Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

List of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

Complex type details：[ `TTextAndImage` ](text-and-image.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TTimePeriod`。

{% endtab %}

{% endtabs %}
