# 交换的通用字段（TCustomExchange）

源文分组：Exchanges。本章完整收录 **25 条字段定义**。

XML 位置：`flowData/{intermediateExchange|elementaryExchange}`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：是。

本部分包含两种交换类型共同使用的元素。中间交换或与环境的交换各自特有的元素，列于下方相应部分。

### `name` · FieldID 1000 <a href="#field-1000" id="field-1000"></a>

局部 XML 位置：`TCustomExchange/name`；ecoSpold1 对照编号：`3702`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString120` | 是 | 否 |

长度：120；多语言：是；主数据冗余字段：是。

交换的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@id` · FieldID 1005 <a href="#field-1005" id="field-1005"></a>

局部 XML 位置：`TCustomExchange/@id`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

该交换的唯一标识符。不能使用 intermediateExchangeId 或 elementaryExchangeId 来标识某个交换，因为数据集中的多个交换可以引用同一个主数据条目。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@amount` · FieldID 1020 <a href="#field-1020" id="field-1020"></a>

局部 XML 位置：`TCustomExchange/@amount`；ecoSpold1 对照编号：`3707`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

基本流交换或中间交换的数量。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@unitId` · FieldID 1030 <a href="#field-1030" id="field-1030"></a>

局部 XML 位置：`TCustomExchange/@unitId`；ecoSpold1 对照编号：`3706`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：是。

对该数量所用单位的引用。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@unitContextId` · FieldID 1031 <a href="#field-1031" id="field-1031"></a>

局部 XML 位置：`TCustomExchange/@unitContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：是。

对单位所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `unitName` · FieldID 1035 <a href="#field-1035" id="field-1035"></a>

局部 XML 位置：`TCustomExchange/unitName`；ecoSpold1 对照编号：`3706`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString40` | 是 | 否 |

长度：40；多语言：是；主数据冗余字段：是。

该数量所用单位的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@variableName` · FieldID 1040 <a href="#field-1040" id="field-1040"></a>

局部 XML 位置：`TCustomExchange/@variableName`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TVariableName` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：否。

变量名是交换的简称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（\_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific\_Value 与 Calorific\_value 等同）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@isCalculatedAmount` · FieldID 1050 <a href="#field-1050" id="field-1050"></a>

局部 XML 位置：`TCustomExchange/@isCalculatedAmount`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果为 true，则 amount 字段的值为 mathematicalRelation 或 transferCoefficient 的计算值。

**XSD 结构约束：** `use="optional"`；`default="false"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@mathematicalRelation` · FieldID 1060 <a href="#field-1060" id="field-1060"></a>

局部 XML 位置：`TCustomExchange/@mathematicalRelation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString32000` | 否 | 否 |

长度：32000；多语言：否；主数据冗余字段：否。

定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。

将公式在一组特定变量值下的计算结果写入 amount 字段。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@casNumber` · FieldID 1100 <a href="#field-1100" id="field-1100"></a>

局部 XML 位置：`TCustomExchange/@casNumber`；ecoSpold1 对照编号：`3701`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TCasNumber` | 否 | 否 |

长度：11；多语言：否；主数据冗余字段：是。

注明化学文摘社（CAS）编号。CAS 编号的格式为 000000-00-0，其中第一组数字不必完整，即允许少于六位数字。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `comment` · FieldID 1110 <a href="#field-1110" id="field-1110"></a>

局部 XML 位置：`TCustomExchange/comment`；ecoSpold1 对照编号：`3792`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString32000` | 否 | 否 |

长度：32000；多语言：是；主数据冗余字段：否。

可对每个单独的交换添加一般注释。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceId` · FieldID 1120 <a href="#field-1120" id="field-1120"></a>

局部 XML 位置：`TCustomExchange/@sourceId`；ecoSpold1 对照编号：`3715`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对有效来源的引用。

**取值选项（原表）：** 引用在建模与验证部分定义的来源。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceContextId` · FieldID 1121 <a href="#field-1121" id="field-1121"></a>

局部 XML 位置：`TCustomExchange/@sourceContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对来源所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceIdOverwrittenByChild` · FieldID 1122 <a href="#field-1122" id="field-1122"></a>

局部 XML 位置：`TCustomExchange/@sourceIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceYear` · FieldID 1125 <a href="#field-1125" id="field-1125"></a>

局部 XML 位置：`TCustomExchange/@sourceYear`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString30` | 否 | 否 |

长度：30；多语言：否；主数据冗余字段：是。

分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceFirstAuthor` · FieldID 1126 <a href="#field-1126" id="field-1126"></a>

局部 XML 位置：`TCustomExchange/@sourceFirstAuthor`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString40` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：是。

以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@pageNumbers` · FieldID 1130 <a href="#field-1130" id="field-1130"></a>

局部 XML 位置：`TCustomExchange/@pageNumbers`；ecoSpold1 对照编号：`3716`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString30` | 否 | 否 |

长度：30；多语言：否；主数据冗余字段：否。

如果数据来自文章或较长出版物中的特定页面，则填写相关页码。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@specificAllocationPropertyId` · FieldID 1150 <a href="#field-1150" id="field-1150"></a>

局部 XML 位置：`TCustomExchange/@specificAllocationPropertyId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用分配所使用的属性（Property）。这会覆盖由 masterAllocationPropertyId 定义、适用于整个数据集的默认设置。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@specificAllocationPropertyContextId` · FieldID 1151 <a href="#field-1151" id="field-1151"></a>

局部 XML 位置：`TCustomExchange/@specificAllocationPropertyContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对属性所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@specificAllocationPropertyIdOverwrittenByChild` · FieldID 1152 <a href="#field-1152" id="field-1152"></a>

局部 XML 位置：`TCustomExchange/@specificAllocationPropertyIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `transferCoefficient` · FieldID 1200 <a href="#field-1200" id="field-1200"></a>

局部 XML 位置：`TCustomExchange/transferCoefficient`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TTransferCoefficient` | 否 | 是 |

长度：—；多语言：否；主数据冗余字段：否。

转移系数将特定输入与特定输出关联，并记录该特定输入中流向该特定输出的份额。

格式定义见下方的复杂类型部分。

复合类型详情：[ `TTransferCoefficient` ](transfer-coefficients.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `uncertainty` · FieldID 1300 <a href="#field-1300" id="field-1300"></a>

局部 XML 位置：`TCustomExchange/uncertainty`；ecoSpold1 对照编号：`3708`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUncertainty` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

以分布函数及其参数和/或数据质量谱系数据的形式提供不确定性信息。

格式定义见下方的复杂类型部分。

复合类型详情：[ `TUncertainty` ](uncertainty.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `property` · FieldID 1400 <a href="#field-1400" id="field-1400"></a>

局部 XML 位置：`TCustomExchange/property`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TProperty` | 否 | 是 |

长度：—；多语言：否；主数据冗余字段：否。

交换的属性，例如干质量、含水率、价格、特定元素或物质的含量。

格式定义见下方的复杂类型部分。

复合类型详情：[ `TProperty` ](properties.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `tag` · FieldID 1450 <a href="#field-1450" id="field-1450"></a>

局部 XML 位置：`TCustomExchange/tag`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TTag` | 否 | 是 |

长度：40；多语言：否；主数据冗余字段：否。

tag 字段允许使用开放式关键词列表描述活动，可用于筛选、分组和搜索。validTags 文件引用提供预定义标签列表；但如果 validTags 主文件中找不到某个标签条目，语义验证过程应仅显示提示信息，而不应报错。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `synonym` · FieldID 1470 <a href="#field-1470" id="field-1470"></a>

局部 XML 位置：`TCustomExchange/synonym`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TSynonym` | 否 | 是 |

长度：80；多语言：是；主数据冗余字段：是。

名称的同义词列表。与普通多语言字符串不同，同义词可包含多个具有相同 xml:lang 属性值的元素。

允许 0..n 个条目，每个条目的最大长度为 80。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：Yes。

This section contains elements used in both exchange types. Elements unique to either Intermediate exchanges or Exchanges with environment are listed in the sections below.

### `name` · FieldID 1000 <a href="#en-field-1000" id="en-field-1000"></a>

Local XML path：`TCustomExchange/name`；ecoSpold1 mapping：`3702`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString120` | Yes | No |

Size：120；Multi language：Yes；Redundant master data：Yes。

Name of the exchange.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@id` · FieldID 1005 <a href="#en-field-1005" id="en-field-1005"></a>

Local XML path：`TCustomExchange/@id`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Unique identifier for this exchange. The intermediateExchangeId or the elementaryExchangeId can not be used to identify an exchange because one master data entry can be referenced by more than one exchange of a dataset.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@amount` · FieldID 1020 <a href="#en-field-1020" id="en-field-1020"></a>

Local XML path：`TCustomExchange/@amount`；ecoSpold1 mapping：`3707`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Amount of an elementary or intermediate exchange.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@unitId` · FieldID 1030 <a href="#en-field-1030" id="en-field-1030"></a>

Local XML path：`TCustomExchange/@unitId`；ecoSpold1 mapping：`3706`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：Yes。

Reference to the unit of the amount.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@unitContextId` · FieldID 1031 <a href="#en-field-1031" id="en-field-1031"></a>

Local XML path：`TCustomExchange/@unitContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：Yes。

Reference to the context of the unit.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `unitName` · FieldID 1035 <a href="#en-field-1035" id="en-field-1035"></a>

Local XML path：`TCustomExchange/unitName`；ecoSpold1 mapping：`3706`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString40` | Yes | No |

Size：40；Multi language：Yes；Redundant master data：Yes。

Unit name of the amount.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@variableName` · FieldID 1040 <a href="#en-field-1040" id="en-field-1040"></a>

Local XML path：`TCustomExchange/@variableName`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TVariableName` | No | No |

Size：40；Multi language：No；Redundant master data：No。

The variable name is a short name for the exchange, used when refering to the exchange amount in mathematical relations (formulas). Variables may contain characters, numbers and underscores (\_). Variable names must start with a character (a-z). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@isCalculatedAmount` · FieldID 1050 <a href="#en-field-1050" id="en-field-1050"></a>

Local XML path：`TCustomExchange/@isCalculatedAmount`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If true the value of the amount field is the calculated value of the mathematicalRelation or the transferCoefficient.

**XSD structural constraints：** `use="optional"`；`default="false"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@mathematicalRelation` · FieldID 1060 <a href="#en-field-1060" id="en-field-1060"></a>

Local XML path：`TCustomExchange/@mathematicalRelation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString32000` | No | No |

Size：32000；Multi language：No；Redundant master data：No。

Defines a mathematical formula with references to values of flows, parameters or properties by variable names or REF function.

The result of the formula with a specific set of variable values is written into the amount field.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@casNumber` · FieldID 1100 <a href="#en-field-1100" id="en-field-1100"></a>

Local XML path：`TCustomExchange/@casNumber`；ecoSpold1 mapping：`3701`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TCasNumber` | No | No |

Size：11；Multi language：No；Redundant master data：Yes。

Indicates the number according to the Chemical Abstract Service (CAS). The Format of the CAS-number: 000000-00-0, where the first string of digits needs not to be complete (i.e. less than six digits are admitted).

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `comment` · FieldID 1110 <a href="#en-field-1110" id="en-field-1110"></a>

Local XML path：`TCustomExchange/comment`；ecoSpold1 mapping：`3792`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString32000` | No | No |

Size：32000；Multi language：Yes；Redundant master data：No。

A general comment can be made about each individual exchange.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceId` · FieldID 1120 <a href="#en-field-1120" id="en-field-1120"></a>

Local XML path：`TCustomExchange/@sourceId`；ecoSpold1 mapping：`3715`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

A reference to a valid source.

**Options (original table)：** Reference to a source defined in the modelling and validation section.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceContextId` · FieldID 1121 <a href="#en-field-1121" id="en-field-1121"></a>

Local XML path：`TCustomExchange/@sourceContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the source.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceIdOverwrittenByChild` · FieldID 1122 <a href="#en-field-1122" id="en-field-1122"></a>

Local XML path：`TCustomExchange/@sourceIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceYear` · FieldID 1125 <a href="#en-field-1125" id="en-field-1125"></a>

Local XML path：`TCustomExchange/@sourceYear`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString30` | No | No |

Size：30；Multi language：No；Redundant master data：Yes。

Indicates the year of publication and communication, respectively. For web-sites: last visited.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@sourceFirstAuthor` · FieldID 1126 <a href="#en-field-1126" id="en-field-1126"></a>

Local XML path：`TCustomExchange/@sourceFirstAuthor`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString40` | No | No |

Size：40；Multi language：No；Redundant master data：Yes。

Indicates the first author by surname and abbreviated name (e.g., Einstein A.). In case of measurement on site, oral communication, personal written communication and questionnaries ('sourceType'=4, 5, 6, 7) the name of the communicating person is mentioned here.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@pageNumbers` · FieldID 1130 <a href="#en-field-1130" id="en-field-1130"></a>

Local XML path：`TCustomExchange/@pageNumbers`；ecoSpold1 mapping：`3716`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString30` | No | No |

Size：30；Multi language：No；Redundant master data：No。

The relevant page numbers if the data are sourced on specific pages in an article or larger publication.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@specificAllocationPropertyId` · FieldID 1150 <a href="#en-field-1150" id="en-field-1150"></a>

Local XML path：`TCustomExchange/@specificAllocationPropertyId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the Property used by the allocation. This overrides the dataset wide default defined by masterAllocationPropertyId.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@specificAllocationPropertyContextId` · FieldID 1151 <a href="#en-field-1151" id="en-field-1151"></a>

Local XML path：`TCustomExchange/@specificAllocationPropertyContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the property.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `@specificAllocationPropertyIdOverwrittenByChild` · FieldID 1152 <a href="#en-field-1152" id="en-field-1152"></a>

Local XML path：`TCustomExchange/@specificAllocationPropertyIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `transferCoefficient` · FieldID 1200 <a href="#en-field-1200" id="en-field-1200"></a>

Local XML path：`TCustomExchange/transferCoefficient`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TTransferCoefficient` | No | Yes |

Size：—；Multi language：No；Redundant master data：No。

Transfer coefficients relate specific inputs to specific outputs and record the share of this specific input that contributes to this specific output.

For the  format definition see the complex  type section below.

Complex type details：[ `TTransferCoefficient` ](transfer-coefficients.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `uncertainty` · FieldID 1300 <a href="#en-field-1300" id="en-field-1300"></a>

Local XML path：`TCustomExchange/uncertainty`；ecoSpold1 mapping：`3708`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUncertainty` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Uncertainty information in the form of distribution functions and their parameters and/or pedigree data.

For the format definition see the complex type section below.

Complex type details：[ `TUncertainty` ](uncertainty.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `property` · FieldID 1400 <a href="#en-field-1400" id="en-field-1400"></a>

Local XML path：`TCustomExchange/property`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TProperty` | No | Yes |

Size：—；Multi language：No；Redundant master data：No。

Properties of the exchange, e.g. dry mass, water content, price, content of specific elements or substances.

For the format definition see the complex type section below.

Complex type details：[ `TProperty` ](properties.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `tag` · FieldID 1450 <a href="#en-field-1450" id="en-field-1450"></a>

Local XML path：`TCustomExchange/tag`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TTag` | No | Yes |

Size：40；Multi language：No；Redundant master data：No。

The tag field allows an open list of keywords which describes the activity and can be used for filtering, grouping and searching. The validTags file reference provides a list of predefined tags, but the semantic validation procedure should only display an information (not an error) if a tag entry cannot be found in the validTags master file.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

### `synonym` · FieldID 1470 <a href="#en-field-1470" id="en-field-1470"></a>

Local XML path：`TCustomExchange/synonym`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TSynonym` | No | Yes |

Size：80；Multi language：Yes；Redundant master data：Yes。

List of synonyms for the name. Contrary to normal multi language strings, synonyms may contain more than one element with the same xml:lang attribute value.

0..n entries are allowed with a max. length of 80 each.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TCustomExchange`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **已处理／已说明 · `TCustomExchange.1200.description.0`**：原译文“输入对输出的贡献份额”可能被理解为输入占输出的比例。原文明确是该输入中分配到特定输出的份额，且 TTransferCoefficient.2410 要求将系数乘以被引用交换量。 已明确为“该特定输入中流向该特定输出的份额”，避免比例分母及流向歧义。
