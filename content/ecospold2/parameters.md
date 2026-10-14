# 参数（TParameter）

源文分组：Parameters。本章完整收录 **12 条字段定义**。

XML 位置：`flowData/parameter`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% hint style="warning" %}
本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

供公式使用的数据集参数。

### `name` · FieldID 1700 <a href="#field-1700" id="field-1700"></a>

局部 XML 位置：`TParameter/name`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString80` | 80 | 是 | 否 | 是 | 是 |

参数的描述性名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@parameterId` · FieldID 1705 <a href="#field-1705" id="field-1705"></a>

局部 XML 位置：`TParameter/@parameterId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

对有效主数据参数的引用。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@parameterContextId` · FieldID 1706 <a href="#field-1706" id="field-1706"></a>

局部 XML 位置：`TParameter/@parameterContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对参数所属上下文的引用。

若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@amount` · FieldID 1710 <a href="#field-1710" id="field-1710"></a>

局部 XML 位置：`TParameter/@amount`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TFloatNumber` | — | 是 | 否 | 否 | 否 |

参数的当前值。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@unitId` · FieldID 1712 <a href="#field-1712" id="field-1712"></a>

局部 XML 位置：`TParameter/@unitId`；ecoSpold1 对照编号：`3706`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 是 |

对参数数量单位的引用。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@unitContextId` · FieldID 1713 <a href="#field-1713" id="field-1713"></a>

局部 XML 位置：`TParameter/@unitContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 是 |

对单位所属上下文的引用。若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `unitName` · FieldID 1714 <a href="#field-1714" id="field-1714"></a>

局部 XML 位置：`TParameter/unitName`；ecoSpold1 对照编号：`3706`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString40` | 40 | 否 | 否 | 是 | 是 |

参数数量的单位名称。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@variableName` · FieldID 1715 <a href="#field-1715" id="field-1715"></a>

局部 XML 位置：`TParameter/@variableName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TVariableName` | 40 | 否 | 否 | 否 | 否 |

变量名是交换的简短名称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（\_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific\_Value 与 Calorific\_value 相同）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@mathematicalRelation` · FieldID 1720 <a href="#field-1720" id="field-1720"></a>

局部 XML 位置：`TParameter/@mathematicalRelation`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString32000` | 32000 | 否 | 否 | 否 | 否 |

定义数学公式，通过变量名或 REF 函数引用流、参数或属性的值。

将采用一组特定变量值计算得到的公式结果写入 amount 字段。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@isCalculatedAmount` · FieldID 1725 <a href="#field-1725" id="field-1725"></a>

局部 XML 位置：`TParameter/@isCalculatedAmount`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 否 | 否 | 否 | 否 |

若为 true，则 amount 字段的值为 mathematicalRelation 的计算值。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `uncertainty` · FieldID 1730 <a href="#field-1730" id="field-1730"></a>

局部 XML 位置：`TParameter/uncertainty`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUncertainty` | — | 否 | 否 | 否 | 否 |

参数数量的不确定性。

复合类型详情：[ `TUncertainty` ](uncertainty.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `comment` · FieldID 1740 <a href="#field-1740" id="field-1740"></a>

局部 XML 位置：`TParameter/comment`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | 否 | 否 | 是 | 否 |

可对每个单独参数填写一般说明。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Dataset parameters for use in formulas.

### `name` · FieldID 1700 <a href="#en-field-1700" id="en-field-1700"></a>

Local XML path：`TParameter/name`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString80` | 80 | Yes | No | Yes | Yes |

Descriptive name of the parameter.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@parameterId` · FieldID 1705 <a href="#en-field-1705" id="en-field-1705"></a>

Local XML path：`TParameter/@parameterId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

A reference to a valid master data parameter.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@parameterContextId` · FieldID 1706 <a href="#en-field-1706" id="en-field-1706"></a>

Local XML path：`TParameter/@parameterContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the parameter.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@amount` · FieldID 1710 <a href="#en-field-1710" id="en-field-1710"></a>

Local XML path：`TParameter/@amount`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TFloatNumber` | — | Yes | No | No | No |

The current value of the parameter.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@unitId` · FieldID 1712 <a href="#en-field-1712" id="en-field-1712"></a>

Local XML path：`TParameter/@unitId`；ecoSpold1 mapping：`3706`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | Yes |

Reference to the unit of the parameter amount.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@unitContextId` · FieldID 1713 <a href="#en-field-1713" id="en-field-1713"></a>

Local XML path：`TParameter/@unitContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | Yes |

Reference to the context of the unit. If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `unitName` · FieldID 1714 <a href="#en-field-1714" id="en-field-1714"></a>

Local XML path：`TParameter/unitName`；ecoSpold1 mapping：`3706`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString40` | 40 | No | No | Yes | Yes |

Unit name of the parameter amount.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@variableName` · FieldID 1715 <a href="#en-field-1715" id="en-field-1715"></a>

Local XML path：`TParameter/@variableName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TVariableName` | 40 | No | No | No | No |

The variable name is a short name for the exchange, used when refering to the exchange amount in mathematical relations (formulas). Variables may contain characters, numbers and underscores (\_). Variable names must start with a character (a-z). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@mathematicalRelation` · FieldID 1720 <a href="#en-field-1720" id="en-field-1720"></a>

Local XML path：`TParameter/@mathematicalRelation`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString32000` | 32000 | No | No | No | No |

Defines a mathematical formula with references to values of flows, parameters or properties by variable names or REF function.

The result of the formula with a specific set of variable values is written into the amount field.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `@isCalculatedAmount` · FieldID 1725 <a href="#en-field-1725" id="en-field-1725"></a>

Local XML path：`TParameter/@isCalculatedAmount`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | No | No | No | No |

If true the value of the amount field is the calculated value of the mathematicalRelation.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `uncertainty` · FieldID 1730 <a href="#en-field-1730" id="en-field-1730"></a>

Local XML path：`TParameter/uncertainty`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUncertainty` | — | No | No | No | No |

Uncertainty of the parameter amount.

Complex type details：[ `TUncertainty` ](uncertainty.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

### `comment` · FieldID 1740 <a href="#en-field-1740" id="en-field-1740"></a>

Local XML path：`TParameter/comment`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | No | No | Yes | No |

A general comment can be made about each individual parameter.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TParameter`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **待专家复核 · `TParameter.1715.description.0`**：该说明位于 TParameter 下，却将变量名描述为 exchange 的简称，可能沿用了交换字段说明；不能据此认定它仅能引用交换。 译文忠实保留“交换”措辞，请对照参数变量名字段及公式语言规范确认此处是否应为 parameter。

- **待专家复核 · `TParameter.1715.description.0`**：文档要求变量名以字母（a-z）开头，并描述字母、数字、下划线字符规则；EcoSpold02DataTypes.xsd 的 TVariableName 仅声明 maxLength=40 与 pattern=\w\S*（约第 858–862 行），该模式未直接表达与文字说明完全等价的规则。可能另有语义验证或公式解析约束。 保留原文变量规则；请核对公式解析及语义验证规范，不应将 XSD 验证通过等同于满足全部变量名规则。
