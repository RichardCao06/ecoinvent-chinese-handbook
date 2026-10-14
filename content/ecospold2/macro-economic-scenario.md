# 宏观经济情景（TMacroEconomicScenario）

源文分组：Macro-economic Scenario。本章完整收录 **4 条字段定义**。

XML 位置：`activityDescription/macroEconomicScenario`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

引用本数据集所用的宏观经济情景。

### `@macroEconomicScenarioId` · FieldID 700 <a href="#field-700" id="field-700"></a>

局部 XML 位置：`TMacroEconomicScenario/@macroEconomicScenarioId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

对有效情景列表中定义的某宏观经济情景的引用（见字段 3715）。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

### `@macroEconomicScenarioContextId` · FieldID 701 <a href="#field-701" id="field-701"></a>

局部 XML 位置：`TMacroEconomicScenario/@macroEconomicScenarioContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对宏观经济情景所属上下文的引用。若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

### `name` · FieldID 720 <a href="#field-720" id="field-720"></a>

局部 XML 位置：`TMacroEconomicScenario/name`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString80` | 80 | 是 | 否 | 是 | 是 |

本数据集所属宏观经济情景的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

### `comment` · FieldID 740 <a href="#field-740" id="field-740"></a>

局部 XML 位置：`TMacroEconomicScenario/comment`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | 否 | 否 | 是 | 否 |

描述宏观经济子数据集与父数据集默认情景的差异。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

References the macro-economic scenario used in this dataset.

### `@macroEconomicScenarioId` · FieldID 700 <a href="#en-field-700" id="en-field-700"></a>

Local XML path：`TMacroEconomicScenario/@macroEconomicScenarioId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

A reference to a macro-economic scenario defined in the list of valid scenarios (see field 3715).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

### `@macroEconomicScenarioContextId` · FieldID 701 <a href="#en-field-701" id="en-field-701"></a>

Local XML path：`TMacroEconomicScenario/@macroEconomicScenarioContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the macro-economic scenario. If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

### `name` · FieldID 720 <a href="#en-field-720" id="en-field-720"></a>

Local XML path：`TMacroEconomicScenario/name`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString80` | 80 | Yes | No | Yes | Yes |

Name of the macro-economic scenario that this dataset belongs to.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

### `comment` · FieldID 740 <a href="#en-field-740" id="en-field-740"></a>

Local XML path：`TMacroEconomicScenario/comment`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | No | No | Yes | No |

Description of how a macro-economic child dataset deviates from the default scenario of the parent dataset.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TMacroEconomicScenario`。

{% endtab %}

{% endtabs %}
