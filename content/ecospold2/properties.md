# 交换属性（TProperty）

源文分组：TProperty。本章完整收录 **18 条字段定义**。

XML 位置：`…/property`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：否。

用于指定交换属性的格式。

### `@propertyId` · FieldID 2300 <a href="#field-2300" id="field-2300"></a>

局部 XML 位置：`TProperty/@propertyId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用该属性的主数据条目。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@propertyContextId` · FieldID 2301 <a href="#field-2301" id="field-2301"></a>

局部 XML 位置：`TProperty/@propertyContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对属性所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `name` · FieldID 2310 <a href="#field-2310" id="field-2310"></a>

局部 XML 位置：`TProperty/name`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString80` | 是 | 否 |

长度：80；多语言：是；主数据冗余字段：是。

属性的描述性名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@unitId` · FieldID 2320 <a href="#field-2320" id="field-2320"></a>

局部 XML 位置：`TProperty/@unitId`；ecoSpold1 对照编号：`3706`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：是。

对该数量所用单位的引用。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@unitContextId` · FieldID 2321 <a href="#field-2321" id="field-2321"></a>

局部 XML 位置：`TProperty/@unitContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：是。

对单位所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `unitName` · FieldID 2325 <a href="#field-2325" id="field-2325"></a>

局部 XML 位置：`TProperty/unitName`；ecoSpold1 对照编号：`3706`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString40` | 否 | 否 |

长度：40；多语言：是；主数据冗余字段：是。

属性量所用单位的名称。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@amount` · FieldID 2330 <a href="#field-2330" id="field-2330"></a>

局部 XML 位置：`TProperty/@amount`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

属性的值。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@isDefiningValue` · FieldID 2335 <a href="#field-2335" id="field-2335"></a>

局部 XML 位置：`TProperty/@isDefiningValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果此字段为 true，则该属性值是交换定义的一部分，因此与交换量之间具有固定关系；不能针对该交换在不同数据集中的个别实例改变这一关系。

**XSD 结构约束：** `use="optional"`；`default="false"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@mathematicalRelation` · FieldID 2340 <a href="#field-2340" id="field-2340"></a>

局部 XML 位置：`TProperty/@mathematicalRelation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString32000` | 否 | 否 |

长度：32000；多语言：否；主数据冗余字段：否。

定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。

将公式在一组特定变量值下的计算结果写入 amount 字段。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@isCalculatedAmount` · FieldID 2345 <a href="#field-2345" id="field-2345"></a>

局部 XML 位置：`TProperty/@isCalculatedAmount`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果为 true，则 amount 字段的值为 mathematicalRelation 的计算值。

**XSD 结构约束：** `use="optional"`；`default="false"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@variableName` · FieldID 2350 <a href="#field-2350" id="field-2350"></a>

局部 XML 位置：`TProperty/@variableName`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TVariableName` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：否。

定义变量名，以便在 mathematicalrelation（数学关系）中引用属性量。

变量名必须以字母（a-z）开头，可包含字母、数字和下划线（\_）。变量名不区分大小写（calorific\_Value 与 Calorific\_value 等同）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `uncertainty` · FieldID 2360 <a href="#field-2360" id="field-2360"></a>

局部 XML 位置：`TProperty/uncertainty`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUncertainty` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

属性值的不确定性。

复合类型详情：[ `TUncertainty` ](uncertainty.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceId` · FieldID 2370 <a href="#field-2370" id="field-2370"></a>

局部 XML 位置：`TProperty/@sourceId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对有效来源的引用，指明记录该属性的出版物。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceContextId` · FieldID 2371 <a href="#field-2371" id="field-2371"></a>

局部 XML 位置：`TProperty/@sourceContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对来源所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceIdOverwrittenByChild` · FieldID 2372 <a href="#field-2372" id="field-2372"></a>

局部 XML 位置：`TProperty/@sourceIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceYear` · FieldID 2375 <a href="#field-2375" id="field-2375"></a>

局部 XML 位置：`TProperty/@sourceYear`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString30` | 否 | 否 |

长度：30；多语言：否；主数据冗余字段：是。

分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceFirstAuthor` · FieldID 2376 <a href="#field-2376" id="field-2376"></a>

局部 XML 位置：`TProperty/@sourceFirstAuthor`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString40` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：是。

以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `comment` · FieldID 2380 <a href="#field-2380" id="field-2380"></a>

局部 XML 位置：`TProperty/comment`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString32000` | 否 | 否 |

长度：32000；多语言：是；主数据冗余字段：否。

可对某个特定交换的每项单独属性添加一般注释。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：No。

Format to specify properties of exchanges.

### `@propertyId` · FieldID 2300 <a href="#en-field-2300" id="en-field-2300"></a>

Local XML path：`TProperty/@propertyId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the master data entry for this property.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@propertyContextId` · FieldID 2301 <a href="#en-field-2301" id="en-field-2301"></a>

Local XML path：`TProperty/@propertyContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the property.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `name` · FieldID 2310 <a href="#en-field-2310" id="en-field-2310"></a>

Local XML path：`TProperty/name`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString80` | Yes | No |

Size：80；Multi language：Yes；Redundant master data：Yes。

Descriptive name of the property.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@unitId` · FieldID 2320 <a href="#en-field-2320" id="en-field-2320"></a>

Local XML path：`TProperty/@unitId`；ecoSpold1 mapping：`3706`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：Yes。

Reference to the unit of the amount.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@unitContextId` · FieldID 2321 <a href="#en-field-2321" id="en-field-2321"></a>

Local XML path：`TProperty/@unitContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：Yes。

Reference to the context of the unit.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `unitName` · FieldID 2325 <a href="#en-field-2325" id="en-field-2325"></a>

Local XML path：`TProperty/unitName`；ecoSpold1 mapping：`3706`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString40` | No | No |

Size：40；Multi language：Yes；Redundant master data：Yes。

Unit name of the property amount.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@amount` · FieldID 2330 <a href="#en-field-2330" id="en-field-2330"></a>

Local XML path：`TProperty/@amount`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The value of the property.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@isDefiningValue` · FieldID 2335 <a href="#en-field-2335" id="en-field-2335"></a>

Local XML path：`TProperty/@isDefiningValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If this field is true, the value of this property is a part of the definition of the exchange and therefore has a fixed relation to the amount of the exchange that cannot be changed for individual instances of the exchange in different datasets.

**XSD structural constraints：** `use="optional"`；`default="false"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@mathematicalRelation` · FieldID 2340 <a href="#en-field-2340" id="en-field-2340"></a>

Local XML path：`TProperty/@mathematicalRelation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString32000` | No | No |

Size：32000；Multi language：No；Redundant master data：No。

Defines a mathematical formula with references to values of flows, parameters or properties by variable names or REF function.

The result of the formula with a specific set of variable values is written into the amount field.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@isCalculatedAmount` · FieldID 2345 <a href="#en-field-2345" id="en-field-2345"></a>

Local XML path：`TProperty/@isCalculatedAmount`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If true the value of the amount field is the calculated value of the mathematicalRelation.

**XSD structural constraints：** `use="optional"`；`default="false"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@variableName` · FieldID 2350 <a href="#en-field-2350" id="en-field-2350"></a>

Local XML path：`TProperty/@variableName`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TVariableName` | No | No |

Size：40；Multi language：No；Redundant master data：No。

Defines a variable name for referencing the property amount in a mathematicalrelation.

Variable names must start with a character (a-z) and may contain characters, numbers and underscores (\_). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `uncertainty` · FieldID 2360 <a href="#en-field-2360" id="en-field-2360"></a>

Local XML path：`TProperty/uncertainty`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUncertainty` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Uncertainty of the property value.

Complex type details：[ `TUncertainty` ](uncertainty.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceId` · FieldID 2370 <a href="#en-field-2370" id="en-field-2370"></a>

Local XML path：`TProperty/@sourceId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

A reference to a valid source. It indicates the publication where the property is documented.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceContextId` · FieldID 2371 <a href="#en-field-2371" id="en-field-2371"></a>

Local XML path：`TProperty/@sourceContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the source.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceIdOverwrittenByChild` · FieldID 2372 <a href="#en-field-2372" id="en-field-2372"></a>

Local XML path：`TProperty/@sourceIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceYear` · FieldID 2375 <a href="#en-field-2375" id="en-field-2375"></a>

Local XML path：`TProperty/@sourceYear`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString30` | No | No |

Size：30；Multi language：No；Redundant master data：Yes。

Indicates the year of publication and communication, respectively. For web-sites: last visited.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `@sourceFirstAuthor` · FieldID 2376 <a href="#en-field-2376" id="en-field-2376"></a>

Local XML path：`TProperty/@sourceFirstAuthor`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString40` | No | No |

Size：40；Multi language：No；Redundant master data：Yes。

Indicates the first author by surname and abbreviated name (e.g., Einstein A.). In case of measurement on site, oral communication, personal written communication and questionnaries ('sourceType'=4, 5, 6, 7) the name of the communicating person is mentioned here.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

### `comment` · FieldID 2380 <a href="#en-field-2380" id="en-field-2380"></a>

Local XML path：`TProperty/comment`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString32000` | No | No |

Size：32000；Multi language：Yes；Redundant master data：No。

A general comment can be made about each individual property of a particular exchange.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TProperty`。

{% endtab %}

{% endtabs %}
