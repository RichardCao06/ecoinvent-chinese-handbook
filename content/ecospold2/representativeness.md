# 代表性（TRepresentativeness）

源文分组：Representativeness。本章完整收录 **6 条字段定义**。

XML 位置：`modellingAndValidation/representativeness`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：否。

包含数据集信息的代表性，以及数据如何采样和／或计算的信息。

### `@systemModelId` · FieldID 3000 <a href="#field-3000" id="field-3000"></a>

局部 XML 位置：`TRepresentativeness/@systemModelId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

系统模型描述如何将活动数据集链接成产品系统。ecoinvent 网络中的部分选项为：'undefined'（未指定系统模型）、'attributional, average current suppliers, revenue allocation'（归因型、当前供应商平均组合、按收入分配）、'consequential, small-scale, long-term decisions'（后果型、小规模、长期决策）。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `@systemModelContextId` · FieldID 3001 <a href="#field-3001" id="field-3001"></a>

局部 XML 位置：`TRepresentativeness/@systemModelContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

引用该系统模型所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `systemModelName` · FieldID 3005 <a href="#field-3005" id="field-3005"></a>

局部 XML 位置：`TRepresentativeness/systemModelName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | 是 | 否 | 是 | 是 |

所引用系统模型（字段 3000）的纯文本值。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `@percent` · FieldID 3010 <a href="#field-3010" id="field-3010"></a>

局部 XML 位置：`TRepresentativeness/@percent`；ecoSpold1 对照编号：`722`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TPercent` | — | 否 | 否 | 否 | 否 |

所采样数据占该活动拟代表总体的百分比；该总体由 Geography、Technology 和 Time Period 下的字段确定。

**取值选项（原表）：** 最大值为 100。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `samplingProcedure` · FieldID 3030 <a href="#field-3030" id="field-3030"></a>

局部 XML 位置：`TRepresentativeness/samplingProcedure`；ecoSpold1 对照编号：`725`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | 否 | 否 | 是 | 否 |

描述用于量化交换的采样和计算程序的文本。应说明特定基本流交换和中间交换的采样程序是否不同于一般程序，并指出组合不同采样程序可能产生的问题。文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `extrapolations` · FieldID 3040 <a href="#field-3040" id="field-3040"></a>

局部 XML 位置：`TRepresentativeness/extrapolations`；ecoSpold1 对照编号：`726`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | 否 | 否 | 是 | 否 |

描述从另一时间期间、另一地理区域或另一技术外推数据的情况，以及这些外推的具体实施方式。

应说明是否在单个交换层面进行了不同的外推。

如果将代表某一国家运行活动的数据用于另一国家的活动，可在这里注明其原始代表性。

也可在这里说明外推导致的均值变化。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：No。

Contains information about the representativeness of the information in the dataset and about how data have been sampled and/or calculated.

### `@systemModelId` · FieldID 3000 <a href="#en-field-3000" id="en-field-3000"></a>

Local XML path：`TRepresentativeness/@systemModelId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

The system model describes how activity datasets are linked to form product systems. Some options in the ecoinvent network are 'undefined', 'attributional, average current suppliers, revenue allocation', 'consequential, small-scale, long-term decisions'.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `@systemModelContextId` · FieldID 3001 <a href="#en-field-3001" id="en-field-3001"></a>

Local XML path：`TRepresentativeness/@systemModelContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the system model.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `systemModelName` · FieldID 3005 <a href="#en-field-3005" id="en-field-3005"></a>

Local XML path：`TRepresentativeness/systemModelName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString120` | 120 | Yes | No | Yes | Yes |

This is the plaintext value of the referenced system model (field 3000).

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `@percent` · FieldID 3010 <a href="#en-field-3010" id="en-field-3010"></a>

Local XML path：`TRepresentativeness/@percent`；ecoSpold1 mapping：`722`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TPercent` | — | No | No | No | No |

Percent of data sampled out of the total that the activity is intended to represent (as given by the fields under Geography, Technology and Time Period).

**Options (original table)：** Maximum 100

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `samplingProcedure` · FieldID 3030 <a href="#en-field-3030" id="en-field-3030"></a>

Local XML path：`TRepresentativeness/samplingProcedure`；ecoSpold1 mapping：`725`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | No | No | Yes | No |

Text describing the sampling and calculation procedures applied for quantifying the exchanges. Reports whether the sampling procedure for particular elementary and intermediate exchanges differ from the general procedure. Mentions possible problems in combining different sampling procedures.Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

### `extrapolations` · FieldID 3040 <a href="#en-field-3040" id="en-field-3040"></a>

Local XML path：`TRepresentativeness/extrapolations`；ecoSpold1 mapping：`726`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TString32000` | 32000 | No | No | Yes | No |

Describes extrapolations of data from another time period, another geographical area or another technology and the way these extrapolations have been carried out.

It should be reported whether different extrapolations have been done on the level of individual exchanges.

If data representative for a activity operated in one country is used for another country's activity, its original representativity can be indicated here.

Changes in mean values due to extrapolations may also be reported here.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TRepresentativeness`。

{% endtab %}

{% endtabs %}
