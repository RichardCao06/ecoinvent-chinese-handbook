# 数据录入者（TDataEntryBy）

源文分组：Data entry by。本章完整收录 **5 条字段定义**。

XML 位置：`administrativeInformation/dataEntryBy`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

包含数据集作者的信息，即将数据录入数据库格式的人员，也是对数据负责的人员。

### `@personId` · FieldID 3400 <a href="#field-3400" id="field-3400"></a>

局部 XML 位置：`TDataEntryBy/@personId`；ecoSpold1 对照编号：`302`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

编制数据集并将其录入数据库的人员的 ID 编号。

**取值选项（原表）：** 条目必须与字段 3610 中的现有条目一致。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@personContextId` · FieldID 3401 <a href="#field-3401" id="field-3401"></a>

局部 XML 位置：`TDataEntryBy/@personContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对人员所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@isActiveAuthor` · FieldID 3403 <a href="#field-3403" id="field-3403"></a>

局部 XML 位置：`TDataEntryBy/@isActiveAuthor`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 否 | 否 | 否 | 否 |

此字段定义字段 3400 指定的人员是否为本数据集的活跃作者（active author）。其他数据提供者今后修改数据集时，将征询该活跃作者的意见。

**XSD 结构约束：** `use="optional"`；`default="false"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@personName` · FieldID 3405 <a href="#field-3405" id="field-3405"></a>

局部 XML 位置：`TDataEntryBy/@personName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | 是 | 否 | 否 | 是 |

人员的名字和姓氏。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@personEmail` · FieldID 3406 <a href="#field-3406" id="field-3406"></a>

局部 XML 位置：`TDataEntryBy/@personEmail`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString80` | 80 | 是 | 否 | 否 | 是 |

人员的完整电子邮件地址。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Contains information about the author of the dataset, i.e. the person that entered data into the database format and thereby is the person responsible for the data.

### `@personId` · FieldID 3400 <a href="#en-field-3400" id="en-field-3400"></a>

Local XML path：`TDataEntryBy/@personId`；ecoSpold1 mapping：`302`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

ID number for the person that prepared the dataset and enters the dataset into the database.

**Options (original table)：** Entry must be identical to an existing entry in field 3610

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@personContextId` · FieldID 3401 <a href="#en-field-3401" id="en-field-3401"></a>

Local XML path：`TDataEntryBy/@personContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the person.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@isActiveAuthor` · FieldID 3403 <a href="#en-field-3403" id="en-field-3403"></a>

Local XML path：`TDataEntryBy/@isActiveAuthor`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | No | No | No | No |

This field defines if the person specified by field 3400 is the active author for this dataset. The active author will be consulted in case of future changes to the dataset by different data providers.

**XSD structural constraints：** `use="optional"`；`default="false"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@personName` · FieldID 3405 <a href="#en-field-3405" id="en-field-3405"></a>

Local XML path：`TDataEntryBy/@personName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | Yes | No | No | Yes |

Name and surname of the person.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

### `@personEmail` · FieldID 3406 <a href="#en-field-3406" id="en-field-3406"></a>

Local XML path：`TDataEntryBy/@personEmail`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString80` | 80 | Yes | No | No | Yes |

Complete email address of the person.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataEntryBy`。

{% endtab %}

{% endtabs %}
