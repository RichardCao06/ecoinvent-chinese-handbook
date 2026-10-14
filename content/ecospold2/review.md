# 审查（TReview）

源文分组：Review。本章完整收录 **11 条字段定义**。

XML 位置：`modellingAndValidation/review`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

包含开展鉴定性评审（critical review）的人员信息，以及评审的主要结果、结论和提出的建议。

允许多名评审者。

### `@reviewerId` · FieldID 3300 <a href="#field-3300" id="field-3300"></a>

局部 XML 位置：`TReview/@reviewerId`；ecoSpold1 对照编号：`5616`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

注明开展评审的人员。

**取值选项（原表）：** 引用字段 3610。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewerContextId` · FieldID 3301 <a href="#field-3301" id="field-3301"></a>

局部 XML 位置：`TReview/@reviewerContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

对评审者所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewerName` · FieldID 3305 <a href="#field-3305" id="field-3305"></a>

局部 XML 位置：`TReview/@reviewerName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | 是 | 否 | 否 | 是 |

人员的名字和姓氏。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewerEmail` · FieldID 3306 <a href="#field-3306" id="field-3306"></a>

局部 XML 位置：`TReview/@reviewerEmail`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString80` | 80 | 是 | 否 | 否 | 是 |

人员的完整电子邮件地址。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewDate` · FieldID 3310 <a href="#field-3310" id="field-3310"></a>

局部 XML 位置：`TReview/@reviewDate`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `date` | — | 是 | 否 | 否 | 否 |

验证或评审日期。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMajorRelease` · FieldID 3320 <a href="#field-3320" id="field-3320"></a>

局部 XML 位置：`TReview/@reviewedMajorRelease`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 是 | 否 | 否 | 否 |

经验证或评审的数据集版本。引用字段 3800。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMinorRelease` · FieldID 3325 <a href="#field-3325" id="field-3325"></a>

局部 XML 位置：`TReview/@reviewedMinorRelease`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 是 | 否 | 否 | 否 |

经验证或评审的数据集版本。引用字段 3805。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMajorRevision` · FieldID 3330 <a href="#field-3330" id="field-3330"></a>

局部 XML 位置：`TReview/@reviewedMajorRevision`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 是 | 否 | 否 | 否 |

经验证或评审的数据集版本。引用字段 3810。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMinorRevision` · FieldID 3335 <a href="#field-3335" id="field-3335"></a>

局部 XML 位置：`TReview/@reviewedMinorRevision`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 是 | 否 | 否 | 否 |

经验证或评审的数据集版本。引用字段 3815。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `details` · FieldID 3340 <a href="#field-3340" id="field-3340"></a>

局部 XML 位置：`TReview/details`；ecoSpold1 对照编号：`5615`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TTextAndImage` | — | 否 | 否 | 是 | 否 |

用于记录数据集评审者注释的文本和图像字段。文本和图像字段是 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。

text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。

复合类型详情：[ `TTextAndImage` ](text-and-image.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `otherDetails` · FieldID 3350 <a href="#field-3350" id="field-3350"></a>

局部 XML 位置：`TReview/otherDetails`；ecoSpold1 对照编号：`5619`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | 否 | 否 | 是 | 否 |

包含评审过程的进一步信息，例如数据集首次发布后补充的小幅修正。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Contains information about who carried out the critical review and about the main results and conclusions of the review and the recommendations made.

Multiple reviewers allowed

### `@reviewerId` · FieldID 3300 <a href="#en-field-3300" id="en-field-3300"></a>

Local XML path：`TReview/@reviewerId`；ecoSpold1 mapping：`5616`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

Indicates the person who carried out the review.

**Options (original table)：** Reference to 3610.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewerContextId` · FieldID 3301 <a href="#en-field-3301" id="en-field-3301"></a>

Local XML path：`TReview/@reviewerContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the reviewer.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewerName` · FieldID 3305 <a href="#en-field-3305" id="en-field-3305"></a>

Local XML path：`TReview/@reviewerName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | Yes | No | No | Yes |

Name and surname of the person.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewerEmail` · FieldID 3306 <a href="#en-field-3306" id="en-field-3306"></a>

Local XML path：`TReview/@reviewerEmail`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString80` | 80 | Yes | No | No | Yes |

Complete email address of the person.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewDate` · FieldID 3310 <a href="#en-field-3310" id="en-field-3310"></a>

Local XML path：`TReview/@reviewDate`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `date` | — | Yes | No | No | No |

Date of validation or review.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMajorRelease` · FieldID 3320 <a href="#en-field-3320" id="en-field-3320"></a>

Local XML path：`TReview/@reviewedMajorRelease`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | Yes | No | No | No |

The dataset version validated or reviewed. Refers to 3800.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMinorRelease` · FieldID 3325 <a href="#en-field-3325" id="en-field-3325"></a>

Local XML path：`TReview/@reviewedMinorRelease`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | Yes | No | No | No |

The dataset version validated or reviewed. Refers to 3805.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMajorRevision` · FieldID 3330 <a href="#en-field-3330" id="en-field-3330"></a>

Local XML path：`TReview/@reviewedMajorRevision`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | Yes | No | No | No |

The dataset version validated or reviewed. Refers to 3810.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `@reviewedMinorRevision` · FieldID 3335 <a href="#en-field-3335" id="en-field-3335"></a>

Local XML path：`TReview/@reviewedMinorRevision`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | Yes | No | No | No |

The dataset version validated or reviewed. Refers to 3815.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `details` · FieldID 3340 <a href="#en-field-3340" id="en-field-3340"></a>

Local XML path：`TReview/details`；ecoSpold1 mapping：`5615`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TTextAndImage` | — | No | No | Yes | No |

Text and image field for the comment of the reviewer of the dataset. Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

List of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

Complex type details：[ `TTextAndImage` ](text-and-image.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

### `otherDetails` · FieldID 3350 <a href="#en-field-3350" id="en-field-3350"></a>

Local XML path：`TReview/otherDetails`；ecoSpold1 mapping：`5619`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | No | No | Yes | No |

Contains further information from the review process, e.g. on smaller corrections added after the first publication of the dataset.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TReview`。

{% endtab %}

{% endtabs %}
