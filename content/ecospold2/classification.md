# 活动分类（TClassification）

源文分组：Classification。本章完整收录 **4 条字段定义**。

XML 位置：`activityDescription/classification`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

包含用于指定活动分类的分类配对信息。

### `classificationSystem` · FieldID 300 <a href="#field-300" id="field-300"></a>

局部 XML 位置：`TClassification/classificationSystem`；ecoSpold1 对照编号：`501`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString255` | 是 | 否 |

长度：255；多语言：是；主数据冗余字段：是。

所用分类体系的名称，例如 ISIC Rev. 4。这是所引用分类体系（字段 320）的可选纯文本值。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

### `classificationValue` · FieldID 310 <a href="#field-310" id="field-310"></a>

局部 XML 位置：`TClassification/classificationValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString120` | 是 | 否 |

长度：120；多语言：是；主数据冗余字段：是。

活动在所指定分类体系中所属的类别。这是所引用分类值（字段 320）的可选纯文本值。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

### `@classificationId` · FieldID 320 <a href="#field-320" id="field-320"></a>

局部 XML 位置：`TClassification/@classificationId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对分类体系中某分类值的引用。该值必须在有效分类列表中定义（见字段 5160）。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

### `@classificationContextId` · FieldID 321 <a href="#field-321" id="field-321"></a>

局部 XML 位置：`TClassification/@classificationContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对分类所属上下文的引用。

若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Contains classification pairs to specify the activity.

### `classificationSystem` · FieldID 300 <a href="#en-field-300" id="en-field-300"></a>

Local XML path：`TClassification/classificationSystem`；ecoSpold1 mapping：`501`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString255` | Yes | No |

Size：255；Multi language：Yes；Redundant master data：Yes。

The name of the classification system used, e.g. ISIC Rev. 4. This is an optional plaintext value of the referenced classification system (field 320).

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

### `classificationValue` · FieldID 310 <a href="#en-field-310" id="en-field-310"></a>

Local XML path：`TClassification/classificationValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString120` | Yes | No |

Size：120；Multi language：Yes；Redundant master data：Yes。

The class that the activity belongs to within the specified classification system.  This is an optional plaintext value of the referenced classification value (field 320).

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

### `@classificationId` · FieldID 320 <a href="#en-field-320" id="en-field-320"></a>

Local XML path：`TClassification/@classificationId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the value of a classification system. Must be defined in list of valid classifications (see field 5160).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

### `@classificationContextId` · FieldID 321 <a href="#en-field-321" id="en-field-321"></a>

Local XML path：`TClassification/@classificationContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the classification.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TClassification`。

{% endtab %}

{% endtabs %}
