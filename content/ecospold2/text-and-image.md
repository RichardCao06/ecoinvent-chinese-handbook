# 文本、图像与文本变量（TTextAndImage）

源文分组：TTextAndImage。本章完整收录 **3 条字段定义**。

XML 位置：`…/generalComment、…/comment 等 TTextAndImage 字段`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% hint style="warning" %}
本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：否。

text、imageUri 和 variable 元素的列表。这些元素可按任意顺序组合。必须通过 text 和 imageUrl 元素的 index 属性指定它们在结果中的所需顺序。

### `text` · FieldID 3900 <a href="#field-3900" id="field-3900"></a>

局部 XML 位置：`TTextAndImage/text`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TIndexedString32000` | 否 | 是 |

长度：32000；多语言：否；主数据冗余字段：否。

用于描述当前部分的自由文本。其 index 属性用于规定文本和图像元素的特定顺序。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TTextAndImage`。

### `imageUrl` · FieldID 3910 <a href="#field-3910" id="field-3910"></a>

局部 XML 位置：`TTextAndImage/imageUrl`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `anyURI` | 否 | 是 |

长度：—；多语言：否；主数据冗余字段：否。

可用于在文本之间插入图像。其 index 属性用于规定文本和图像元素的特定顺序。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TTextAndImage`。

### `variable` · FieldID 3920 <a href="#field-3920" id="field-3920"></a>

局部 XML 位置：`TTextAndImage/variable`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TNamedString32000` | 否 | 是 |

长度：32000；多语言：否；主数据冗余字段：否。

定义本部分 text 元素中使用的变量名及其值。派生数据集可以覆盖这些定义，以改变变量值。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TTextAndImage`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：No。

List of text, imageUri and variable elements. These can be combined in any order. Their desired order in the result must be given by the index attributes of the text and imageUrl elements.

### `text` · FieldID 3900 <a href="#en-field-3900" id="en-field-3900"></a>

Local XML path：`TTextAndImage/text`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TIndexedString32000` | No | Yes |

Size：32000；Multi language：No；Redundant master data：No。

Free text used to describe the current section. Its index attribute is used to enforce a specific order of text and image elements.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TTextAndImage`。

### `imageUrl` · FieldID 3910 <a href="#en-field-3910" id="en-field-3910"></a>

Local XML path：`TTextAndImage/imageUrl`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `anyURI` | No | Yes |

Size：—；Multi language：No；Redundant master data：No。

Can be used to mix images between texts. Its index attribute is used to enforce a specific order of text and image elements.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TTextAndImage`。

### `variable` · FieldID 3920 <a href="#en-field-3920" id="en-field-3920"></a>

Local XML path：`TTextAndImage/variable`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TNamedString32000` | No | Yes |

Size：32000；Multi language：No；Redundant master data：No。

Defines a varible name and its value used in a text element in this section. These can be overriden by derived datasets to change the value of variables.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TTextAndImage`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **待专家复核 · `TTextAndImage.intro.0`**：源文开头将图像元素称为 imageUri，后文却称为 imageUrl；相同 imageUri 表述也出现于 TTechnology.510 和 TReview.3340 的复用说明。独立核查官方 Schemas/datasets/EcoSpold02DataTypes.xsd 的 TTextAndImage 定义，实际子元素为 text、imageUrl、variable，而没有 imageUri。译文忠实保留原文两种名称，文档说明与XSD元素定义存在冲突。 生成或解析XML时以该XSD中的 imageUrl 为准；原英文说明的 imageUri 应由技术编辑确认统一。译文原有名称不静默替换。
