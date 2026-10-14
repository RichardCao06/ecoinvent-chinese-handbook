# 基本流交换专用字段（TElementaryExchange）

源文分组：Only valid for Elementary Exchanges。本章完整收录 **6 条字段定义**。

XML 位置：`flowData/elementaryExchange`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

包含仅适用于基本流交换的字段（除交换部分的字段之外）。与环境的交换是作为单元过程输入和输出记录的基本流，并包含其相关信息。

当交换发生于活动与环境之间时，此部分扩展交换部分。

**继承关系：** 本章仅列专用字段；完整交换结构还包含[交换的通用字段](exchanges.md)。

### `inputGroup` · FieldID 1600 <a href="#field-1600" id="field-1600"></a>

局部 XML 位置：`TElementaryExchange/inputGroup`；ecoSpold1 对照编号：`3503`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

表示输入流的类型。代码为：4=来自环境（From Environment）。

对于每个交换，只能存在 inputGroup 或 outputGroup 中的一个，以表明流的方向。

此字段相当于字段 1500，但有效值集合不同。

**取值选项（原表）：** 4 = 来自环境（From Environment）

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `outputGroup` · FieldID 1610 <a href="#field-1610" id="field-1610"></a>

局部 XML 位置：`TElementaryExchange/outputGroup`；ecoSpold1 对照编号：`3504`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

表示输出流的类型。代码为：4=流向环境（ToEnvironment）。

对于每个交换，只能存在 inputGroup 或 outputGroup 中的一个，以表明流的方向。

此字段相当于字段 1510，但有效值集合不同。

**取值选项（原表）：** 4 = 流向环境（ToEnvironment）

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `@elementaryExchangeId` · FieldID 1615 <a href="#field-1615" id="field-1615"></a>

局部 XML 位置：`TElementaryExchange/@elementaryExchangeId`；ecoSpold1 对照编号：`3793`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用此基本流交换的主数据条目。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `@elementaryExchangeContextId` · FieldID 1616 <a href="#field-1616" id="field-1616"></a>

局部 XML 位置：`TElementaryExchange/@elementaryExchangeContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用该基本流交换所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `compartment` · FieldID 1660 <a href="#field-1660" id="field-1660"></a>

局部 XML 位置：`TElementaryExchange/compartment`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TCompartment` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：是。

交换的区室及子区室名称。validCompartments 所引用的 XML 文档包含给定语言下有效的区室／子区室配对的定义。

复合类型详情：[ `TCompartment` ](compartments.md)。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `@formula` · FieldID 1670 <a href="#field-1670" id="field-1670"></a>

局部 XML 位置：`TElementaryExchange/@formula`；ecoSpold1 对照编号：`3711`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString40` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：是。

可以填写化学式，例如分子式。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Comprises fields (additional to the exchanges section) which are only valid for elementary exchanges. Exchanges with environment are elementary flows as inputs and outputs recorded in a unit process and its related information.

This section extends the exchanges section in case of exchanges with environment.

**Inheritance:** These are additional fields; the complete exchange also includes [common exchange fields](exchanges.md).

### `inputGroup` · FieldID 1600 <a href="#en-field-1600" id="en-field-1600"></a>

Local XML path：`TElementaryExchange/inputGroup`；ecoSpold1 mapping：`3503`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Indicates the kind of input flow. The codes are: 4=From Environment

For each exchange only an inputGroup or outputGroup shall exist. This indicates the direction of the flow.

This field is the equivalent of field 1500 with a different set of valid values.

**Options (original table)：** 4 = From Environment

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `outputGroup` · FieldID 1610 <a href="#en-field-1610" id="en-field-1610"></a>

Local XML path：`TElementaryExchange/outputGroup`；ecoSpold1 mapping：`3504`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Indicates the kind of output flow. The codes are: 4=ToEnvironment

For each exchange only an inputGroup or outputGroup shall exist. This indicates the direction of the flow.

This field is the equivalent of field 1510 with a different set of valid values.

**Options (original table)：** 4 = ToEnvironment

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `@elementaryExchangeId` · FieldID 1615 <a href="#en-field-1615" id="en-field-1615"></a>

Local XML path：`TElementaryExchange/@elementaryExchangeId`；ecoSpold1 mapping：`3793`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the master data entry for this elementary exchange

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `@elementaryExchangeContextId` · FieldID 1616 <a href="#en-field-1616" id="en-field-1616"></a>

Local XML path：`TElementaryExchange/@elementaryExchangeContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the elementary exchange.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `compartment` · FieldID 1660 <a href="#en-field-1660" id="en-field-1660"></a>

Local XML path：`TElementaryExchange/compartment`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TCompartment` | Yes | No |

Size：—；Multi language：No；Redundant master data：Yes。

Name of the compartment and subcompartment of the exchange. The xml document referenced by validCompartments contains definitions of valid compartment/subcompartment pairs for a given language.

Complex type details：[ `TCompartment` ](compartments.md)。

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

### `@formula` · FieldID 1670 <a href="#en-field-1670" id="en-field-1670"></a>

Local XML path：`TElementaryExchange/@formula`；ecoSpold1 mapping：`3711`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString40` | No | No |

Size：40；Multi language：No；Redundant master data：Yes。

Chemical formula (e.g. sum formula) may be entered.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TElementaryExchange`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **已处理／已说明 · `TElementaryExchange.1660.description.0`**：将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。 已修正术语，保留全部 XML 标识与引用编号。
