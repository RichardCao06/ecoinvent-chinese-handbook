# 影响指标结果（TImpactIndicatorResult）

源文分组：Impact Indicator Results。本章完整收录 **11 条字段定义**。

XML 位置：`flowData/impactIndicator`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% hint style="warning" %}
本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

计算得到的影响指标。

### `@impactIndicatorId` · FieldID 1800 <a href="#field-1800" id="field-1800"></a>

局部 XML 位置：`TImpactIndicatorResult/@impactIndicatorId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

对影响指标的引用。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactIndicatorContextId` · FieldID 1801 <a href="#field-1801" id="field-1801"></a>

局部 XML 位置：`TImpactIndicatorResult/@impactIndicatorContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对影响指标所属上下文的引用。若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactMethodId` · FieldID 1810 <a href="#field-1810" id="field-1810"></a>

局部 XML 位置：`TImpactIndicatorResult/@impactMethodId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

对影响指标所属方法的引用。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactMethodContextId` · FieldID 1811 <a href="#field-1811" id="field-1811"></a>

局部 XML 位置：`TImpactIndicatorResult/@impactMethodContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对影响评价方法所属上下文的引用。若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `impactMethodName` · FieldID 1815 <a href="#field-1815" id="field-1815"></a>

局部 XML 位置：`TImpactIndicatorResult/impactMethodName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | 是 | 否 | 是 | 是 |

影响评价方法的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactCategoryId` · FieldID 1820 <a href="#field-1820" id="field-1820"></a>

局部 XML 位置：`TImpactIndicatorResult/@impactCategoryId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

对影响类别所属方法的引用。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactCategoryContextId` · FieldID 1821 <a href="#field-1821" id="field-1821"></a>

局部 XML 位置：`TImpactIndicatorResult/@impactCategoryContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对影响类别所属上下文的引用。若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `impactCategoryName` · FieldID 1825 <a href="#field-1825" id="field-1825"></a>

局部 XML 位置：`TImpactIndicatorResult/impactCategoryName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | 是 | 否 | 是 | 是 |

影响类别的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@amount` · FieldID 1830 <a href="#field-1830" id="field-1830"></a>

局部 XML 位置：`TImpactIndicatorResult/@amount`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TFloatNumber` | — | 是 | 否 | 否 | 否 |

影响指标的值。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `name` · FieldID 1840 <a href="#field-1840" id="field-1840"></a>

局部 XML 位置：`TImpactIndicatorResult/name`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | 是 | 否 | 是 | 是 |

影响指标的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `unitName` · FieldID 1850 <a href="#field-1850" id="field-1850"></a>

局部 XML 位置：`TImpactIndicatorResult/unitName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString40` | 40 | 是 | 否 | 是 | 是 |

影响指标数量的单位名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Calculated impact indicators

### `@impactIndicatorId` · FieldID 1800 <a href="#en-field-1800" id="en-field-1800"></a>

Local XML path：`TImpactIndicatorResult/@impactIndicatorId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

Reference to the impact indicator.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactIndicatorContextId` · FieldID 1801 <a href="#en-field-1801" id="en-field-1801"></a>

Local XML path：`TImpactIndicatorResult/@impactIndicatorContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the impact indicator. If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactMethodId` · FieldID 1810 <a href="#en-field-1810" id="en-field-1810"></a>

Local XML path：`TImpactIndicatorResult/@impactMethodId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

Reference to the method of the impact indicator.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactMethodContextId` · FieldID 1811 <a href="#en-field-1811" id="en-field-1811"></a>

Local XML path：`TImpactIndicatorResult/@impactMethodContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the impact method. If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `impactMethodName` · FieldID 1815 <a href="#en-field-1815" id="en-field-1815"></a>

Local XML path：`TImpactIndicatorResult/impactMethodName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | Yes | No | Yes | Yes |

Name of the impact method.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactCategoryId` · FieldID 1820 <a href="#en-field-1820" id="en-field-1820"></a>

Local XML path：`TImpactIndicatorResult/@impactCategoryId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

Reference to the method of the impact category.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@impactCategoryContextId` · FieldID 1821 <a href="#en-field-1821" id="en-field-1821"></a>

Local XML path：`TImpactIndicatorResult/@impactCategoryContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the impact category. If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `impactCategoryName` · FieldID 1825 <a href="#en-field-1825" id="en-field-1825"></a>

Local XML path：`TImpactIndicatorResult/impactCategoryName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | Yes | No | Yes | Yes |

Name of the impact category.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `@amount` · FieldID 1830 <a href="#en-field-1830" id="en-field-1830"></a>

Local XML path：`TImpactIndicatorResult/@amount`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TFloatNumber` | — | Yes | No | No | No |

The value of the impact indicator.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `name` · FieldID 1840 <a href="#en-field-1840" id="en-field-1840"></a>

Local XML path：`TImpactIndicatorResult/name`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | Yes | No | Yes | Yes |

Name of the impact indicator.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

### `unitName` · FieldID 1850 <a href="#en-field-1850" id="en-field-1850"></a>

Local XML path：`TImpactIndicatorResult/unitName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString40` | 40 | Yes | No | Yes | Yes |

Unit name of the impact indicator amount.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TImpactIndicatorResult`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **待专家复核 · `TImpactIndicatorResult.1820.description.0`**：原文写“对影响类别所属方法的引用”，但 EcoSpold02FlowData.xsd 约第 1039–1048 行明确本字段为 impactCategoryId、类型 TUuid、referenceToComplexType=TImpactMethodCategory，区别于字段 1810 的 impactMethodId（TImpactMethod）。译文忠实保留原文方法措辞，源文说明与引用对象存在矛盾。 请确认应将官方说明修正为对影响类别的引用；实现时以 impactCategoryId 与 TImpactMethodCategory 的模式定义为依据。
