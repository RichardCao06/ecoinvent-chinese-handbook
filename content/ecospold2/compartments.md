# 区室与子区室（TCompartment）

源文分组：TCompartment。本章完整收录 **4 条字段定义**。

XML 位置：`…/elementaryExchange/compartment`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：否。

包含用于指定交换的区室配对。

### `compartment` · FieldID 330 <a href="#field-330" id="field-330"></a>

局部 XML 位置：`TCompartment/compartment`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TCompartmentName` | 40 | 是 | 否 | 是 | 是 |

区室名称。这是所引用区室（字段 5315）的纯文本值。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

### `subcompartment` · FieldID 340 <a href="#field-340" id="field-340"></a>

局部 XML 位置：`TCompartment/subcompartment`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TCompartmentName` | 40 | 是 | 否 | 是 | 是 |

子区室名称。这是所引用子区室（字段 5325）的纯文本值。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

### `@subcompartmentId` · FieldID 350 <a href="#field-350" id="field-350"></a>

局部 XML 位置：`TCompartment/@subcompartmentId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

引用区室／子区室配对。该配对必须在有效区室列表中定义（见字段 5330）。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

### `@subcompartmentContextId` · FieldID 351 <a href="#field-351" id="field-351"></a>

局部 XML 位置：`TCompartment/@subcompartmentContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

引用该子区室所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：No。

Contains compartment pairs to specify an exchange.

### `compartment` · FieldID 330 <a href="#en-field-330" id="en-field-330"></a>

Local XML path：`TCompartment/compartment`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TCompartmentName` | 40 | Yes | No | Yes | Yes |

The name of the compartment.This is the plaintext value of the referenced compartment (field 5315).

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

### `subcompartment` · FieldID 340 <a href="#en-field-340" id="en-field-340"></a>

Local XML path：`TCompartment/subcompartment`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TCompartmentName` | 40 | Yes | No | Yes | Yes |

The name of the subcompartment.This is the plaintext value of the referenced subcompartment (field 5325).

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

### `@subcompartmentId` · FieldID 350 <a href="#en-field-350" id="en-field-350"></a>

Local XML path：`TCompartment/@subcompartmentId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

Reference to the compartment/subcompartment pair. Must be defined in list of valid compartments (see field 5330).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

### `@subcompartmentContextId` · FieldID 351 <a href="#en-field-351" id="en-field-351"></a>

Local XML path：`TCompartment/@subcompartmentContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the subcompartment

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TCompartment`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **已处理／已说明 · `TCompartment.intro.0`**：将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。 已修正术语，保留全部 XML 标识与引用编号。

- **已处理／已说明 · `TCompartment.330.description.0`**：将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。 已修正术语，保留全部 XML 标识与引用编号。

- **已处理／已说明 · `TCompartment.340.description.0`**：将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。 已修正术语，保留全部 XML 标识与引用编号。

- **已处理／已说明 · `TCompartment.350.description.0`**：将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。 已修正术语，保留全部 XML 标识与引用编号。

- **已处理／已说明 · `TCompartment.351.description.0`**：将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。 已修正术语，保留全部 XML 标识与引用编号。
