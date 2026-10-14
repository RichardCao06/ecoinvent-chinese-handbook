# 转移系数（TTransferCoefficient）

源文分组：TTransferCoefficient。本章完整收录 **11 条字段定义**。

XML 位置：`…/transferCoefficient`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

用于根据投入量计算输出量的转移系数。

### `@exchangeId` · FieldID 2400 <a href="#field-2400" id="field-2400"></a>

局部 XML 位置：`TTransferCoefficient/@exchangeId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

引用某个交换的 UUID。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@amount` · FieldID 2410 <a href="#field-2410" id="field-2410"></a>

局部 XML 位置：`TTransferCoefficient/@amount`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TFloatNumber` | — | 是 | 否 | 否 | 否 |

应将转移系数的数值与所引用交换的数量相乘。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@mathematicalRelation` · FieldID 2420 <a href="#field-2420" id="field-2420"></a>

局部 XML 位置：`TTransferCoefficient/@mathematicalRelation`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString32000` | 32000 | 否 | 否 | 否 | 否 |

定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。

将公式在一组特定变量值下的计算结果写入 amount 字段。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@isCalculatedAmount` · FieldID 2425 <a href="#field-2425" id="field-2425"></a>

局部 XML 位置：`TTransferCoefficient/@isCalculatedAmount`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 否 | 否 | 否 | 否 |

如果为 true，则 amount 字段的值为 mathematicalRelation 的计算值。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `uncertainty` · FieldID 2430 <a href="#field-2430" id="field-2430"></a>

局部 XML 位置：`TTransferCoefficient/uncertainty`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUncertainty` | — | 否 | 否 | 否 | 否 |

转移系数数值的不确定性。

复合类型详情：[ `TUncertainty` ](uncertainty.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceId` · FieldID 2440 <a href="#field-2440" id="field-2440"></a>

局部 XML 位置：`TTransferCoefficient/@sourceId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对有效来源的引用。

**取值选项（原表）：** 引用在 modellingAndValidation 部分定义的来源。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceContextId` · FieldID 2441 <a href="#field-2441" id="field-2441"></a>

局部 XML 位置：`TTransferCoefficient/@sourceContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对来源所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceIdOverwrittenByChild` · FieldID 2442 <a href="#field-2442" id="field-2442"></a>

局部 XML 位置：`TTransferCoefficient/@sourceIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 否 | 否 | 否 | 否 |

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceYear` · FieldID 2445 <a href="#field-2445" id="field-2445"></a>

局部 XML 位置：`TTransferCoefficient/@sourceYear`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString30` | 30 | 否 | 否 | 否 | 是 |

分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceFirstAuthor` · FieldID 2446 <a href="#field-2446" id="field-2446"></a>

局部 XML 位置：`TTransferCoefficient/@sourceFirstAuthor`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | 否 | 否 | 否 | 是 |

以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `comment` · FieldID 2450 <a href="#field-2450" id="field-2450"></a>

局部 XML 位置：`TTransferCoefficient/comment`；ecoSpold1 对照编号：`3792`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | 否 | 否 | 是 | 否 |

可对每个单独的转移系数添加一般注释。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Transfer coefficients for calculating amounts of outputs from amounts of inputs.

### `@exchangeId` · FieldID 2400 <a href="#en-field-2400" id="en-field-2400"></a>

Local XML path：`TTransferCoefficient/@exchangeId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

Reference to the UUID of an exchange.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@amount` · FieldID 2410 <a href="#en-field-2410" id="en-field-2410"></a>

Local XML path：`TTransferCoefficient/@amount`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TFloatNumber` | — | Yes | No | No | No |

The amount of the transfer coefficient is to be multiplied with the amount of this referenced exchange.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@mathematicalRelation` · FieldID 2420 <a href="#en-field-2420" id="en-field-2420"></a>

Local XML path：`TTransferCoefficient/@mathematicalRelation`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString32000` | 32000 | No | No | No | No |

defines a mathematical formula with references to values of flows, parameters or properties by variable names or REF function

the result of the formula with a specific set of variable values is written into the amount field

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@isCalculatedAmount` · FieldID 2425 <a href="#en-field-2425" id="en-field-2425"></a>

Local XML path：`TTransferCoefficient/@isCalculatedAmount`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | No | No | No | No |

If true the value of the amount field is the calculated value of the mathematicalRelation.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `uncertainty` · FieldID 2430 <a href="#en-field-2430" id="en-field-2430"></a>

Local XML path：`TTransferCoefficient/uncertainty`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUncertainty` | — | No | No | No | No |

Uncertainty of the transfer coefficient amount.

Complex type details：[ `TUncertainty` ](uncertainty.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceId` · FieldID 2440 <a href="#en-field-2440" id="en-field-2440"></a>

Local XML path：`TTransferCoefficient/@sourceId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

A reference to a valid source.

**Options (original table)：** Reference to a source defined in the modellingAndValidation section.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceContextId` · FieldID 2441 <a href="#en-field-2441" id="en-field-2441"></a>

Local XML path：`TTransferCoefficient/@sourceContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the source.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceIdOverwrittenByChild` · FieldID 2442 <a href="#en-field-2442" id="en-field-2442"></a>

Local XML path：`TTransferCoefficient/@sourceIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | No | No | No | No |

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceYear` · FieldID 2445 <a href="#en-field-2445" id="en-field-2445"></a>

Local XML path：`TTransferCoefficient/@sourceYear`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString30` | 30 | No | No | No | Yes |

Indicates the year of publication and communication, respectively. For web-sites: last visited.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `@sourceFirstAuthor` · FieldID 2446 <a href="#en-field-2446" id="en-field-2446"></a>

Local XML path：`TTransferCoefficient/@sourceFirstAuthor`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | No | No | No | Yes |

Indicates the first author by surname and abbreviated name (e.g., Einstein A.). In case of measurement on site, oral communication, personal written communication and questionnaries ('sourceType'=4, 5, 6, 7) the name of the communicating person is mentioned here.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

### `comment` · FieldID 2450 <a href="#en-field-2450" id="en-field-2450"></a>

Local XML path：`TTransferCoefficient/comment`；ecoSpold1 mapping：`3792`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | No | No | Yes | No |

A general comment can be made about each individual transfer coefficient.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TTransferCoefficient`。

{% endtab %}

{% endtabs %}
