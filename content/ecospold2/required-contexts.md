# 所需上下文引用（TRequiredContextReference）

源文分组：Required Context Reference。本章完整收录 **7 条字段定义**。

XML 位置：`administrativeInformation/fileAttributes/requiredContext`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：否。

此类型用于指定：若要使用数据集引用的主数据读取该数据集，必须了解哪些上下文。

此类型可用于表明：读取该数据集需要来自不同上下文的主数据条目。读取数据集的软件必须识别这些上下文，并知道各上下文的实际主数据文件位于何处。

### `@majorRelease` · FieldID 7810 <a href="#field-7810" id="field-7810"></a>

局部 XML 位置：`TRequiredContextReference/@majorRelease`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

此版本号可用于确保某活动所需的主数据条目已经存在。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@minorRelease` · FieldID 7820 <a href="#field-7820" id="field-7820"></a>

局部 XML 位置：`TRequiredContextReference/@minorRelease`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

此版本号可用于确保某活动所需的主数据条目已经存在。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@majorRevision` · FieldID 7830 <a href="#field-7830" id="field-7830"></a>

局部 XML 位置：`TRequiredContextReference/@majorRevision`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

此版本号可用于确保某活动所需的主数据条目已经存在。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@minorRevision` · FieldID 7840 <a href="#field-7840" id="field-7840"></a>

局部 XML 位置：`TRequiredContextReference/@minorRevision`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

此版本号可用于确保某活动所需的主数据条目已经存在。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@requiredContextId` · FieldID 7850 <a href="#field-7850" id="field-7850"></a>

局部 XML 位置：`TRequiredContextReference/@requiredContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用该主数据文件所属的上下文。

如果省略此属性，应改用数据集自身的上下文。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `requiredContextName` · FieldID 7855 <a href="#field-7855" id="field-7855"></a>

局部 XML 位置：`TRequiredContextReference/requiredContextName`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString80` | 是 | 否 |

长度：80；多语言：是；主数据冗余字段：是。

字段 7850 所引用上下文的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@requiredContextFileLocation` · FieldID 7860 <a href="#field-7860" id="field-7860"></a>

局部 XML 位置：`TRequiredContextReference/@requiredContextFileLocation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `anyURI` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

指向包含此上下文主数据文件的目录的可选 URI 引用。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：No。

This type allows to specify which context(s) must be known if a dataset is to be read using the master data referenced by it.

It can be used signal that master data entries from different contexts are needed to read this dataset. The software reading the dataset must be aware of those contexts and must know where to find the actual master data files of each context.

### `@majorRelease` · FieldID 7810 <a href="#en-field-7810" id="en-field-7810"></a>

Local XML path：`TRequiredContextReference/@majorRelease`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

This version number can be used to make sure that the necessary master data entries are present for an activity.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@minorRelease` · FieldID 7820 <a href="#en-field-7820" id="en-field-7820"></a>

Local XML path：`TRequiredContextReference/@minorRelease`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

This version number can be used to make sure that the necessary master data entries are present for an activity.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@majorRevision` · FieldID 7830 <a href="#en-field-7830" id="en-field-7830"></a>

Local XML path：`TRequiredContextReference/@majorRevision`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | No | No |

Size：—；Multi language：No；Redundant master data：No。

This version number can be used to make sure that the necessary master data entries are present for an activity.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@minorRevision` · FieldID 7840 <a href="#en-field-7840" id="en-field-7840"></a>

Local XML path：`TRequiredContextReference/@minorRevision`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | No | No |

Size：—；Multi language：No；Redundant master data：No。

This version number can be used to make sure that the necessary master data entries are present for an activity.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@requiredContextId` · FieldID 7850 <a href="#en-field-7850" id="en-field-7850"></a>

Local XML path：`TRequiredContextReference/@requiredContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the master data file.

If this attribute is omitted the context of the dataset itself should be used instead.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `requiredContextName` · FieldID 7855 <a href="#en-field-7855" id="en-field-7855"></a>

Local XML path：`TRequiredContextReference/requiredContextName`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString80` | Yes | No |

Size：80；Multi language：Yes；Redundant master data：Yes。

The name of the context referenced by field 7850.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

### `@requiredContextFileLocation` · FieldID 7860 <a href="#en-field-7860" id="en-field-7860"></a>

Local XML path：`TRequiredContextReference/@requiredContextFileLocation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `anyURI` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Optional URI reference to the directory containing the master data files of this context.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TRequiredContextReference`。

{% endtab %}

{% endtabs %}
