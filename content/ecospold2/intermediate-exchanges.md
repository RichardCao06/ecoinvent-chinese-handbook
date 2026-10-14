# 中间交换专用字段（TIntermediateExchange）

源文分组：Only valid for Intermediate Exchanges。本章完整收录 **18 条字段定义**。

XML 位置：`flowData/intermediateExchange`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% hint style="warning" %}
本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：是；分组必填：是。

包含仅适用于中间交换的字段，是交换部分之外的附加字段。中间交换是单元过程中记录的产品或废物投入和输出，以及相应的相关信息。

对于中间交换，本部分扩展交换部分。

**继承关系：** 本章仅列专用字段；完整交换结构还包含[交换的通用字段](exchanges.md)。

### `inputGroup` · FieldID 1500 <a href="#field-1500" id="field-1500"></a>

局部 XML 位置：`TIntermediateExchange/inputGroup`；ecoSpold1 对照编号：`3503`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

注明输入流的种类。代码如下：1=材料/燃料（Materials/Fuels），2=电力/热（Electricity/Heat），3=服务（Services），5=来自技术圈，未指定（From Technosphere (unspecified)）。

每个交换只能具有 inputGroup 或 outputGroup 中的一个，以表示流的方向。

**取值选项（原表）：** 1 = 材料/燃料（Materials/Fuels）；2 = 电力/热（Electricity/Heat）；3 = 服务（Services）；5 = 来自技术圈，未指定（From Technosphere (unspecified)）

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `outputGroup` · FieldID 1510 <a href="#field-1510" id="field-1510"></a>

局部 XML 位置：`TIntermediateExchange/outputGroup`；ecoSpold1 对照编号：`3504`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

注明输出流的种类。代码如下：0=参考产品（ReferenceProduct），2=副产品（By-product），3=待处理材料（MaterialForTreatment），5=存量增加（Stock Additions）。

每个交换只能具有 inputGroup 或 outputGroup 中的一个，以表示流的方向。

**取值选项（原表）：** 0 = 参考产品（ReferenceProduct）；2 = 副产品（By-product）；3 = 待处理材料（Material for Treatment）；5 = 存量增加（Stock Additions）

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@intermediateExchangeId` · FieldID 1515 <a href="#field-1515" id="field-1515"></a>

局部 XML 位置：`TIntermediateExchange/@intermediateExchangeId`；ecoSpold1 对照编号：`3793`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

引用该中间交换的主数据条目。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@intermediateExchangeContextId` · FieldID 1516 <a href="#field-1516" id="field-1516"></a>

局部 XML 位置：`TIntermediateExchange/@intermediateExchangeContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对中间交换所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@activityLinkId` · FieldID 1520 <a href="#field-1520" id="field-1520"></a>

局部 XML 位置：`TIntermediateExchange/@activityLinkId`；ecoSpold1 对照编号：`3715`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

显式引用供应该中间产品的活动。如果此字段为空，则由链接规则确定该活动；该规则使用本活动的地理和时间信息。

**取值选项（原表）：** 引用字段 105（位于另一个活动数据集中）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@activityLinkContextId` · FieldID 1521 <a href="#field-1521" id="field-1521"></a>

局部 XML 位置：`TIntermediateExchange/@activityLinkContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对活动链接所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@activityLinkIdOverwrittenByChild` · FieldID 1522 <a href="#field-1522" id="field-1522"></a>

局部 XML 位置：`TIntermediateExchange/@activityLinkIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeAmount` · FieldID 1530 <a href="#field-1530" id="field-1530"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeAmount`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

按年表示的产品产量，单位与该交换相同。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceIdOverwrittenByChild` · FieldID 1531 <a href="#field-1531" id="field-1531"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeSourceIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeVariableName` · FieldID 1532 <a href="#field-1532" id="field-1532"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeVariableName`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TVariableName` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：否。

变量名是交换产量的简称，用于在数学关系（公式）中引用产量数值。变量可包含字母、数字和下划线（\_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific\_Value 与 Calorific\_value 等同）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceId` · FieldID 1533 <a href="#field-1533" id="field-1533"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeSourceId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对有效来源的引用。

**取值选项（原表）：** 引用在建模与验证部分定义的来源。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeMathematicalRelation` · FieldID 1534 <a href="#field-1534" id="field-1534"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeMathematicalRelation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString32000` | 否 | 否 |

长度：32000；多语言：否；主数据冗余字段：否。

定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。

将公式在一组特定变量值下的计算结果写入 amount 字段。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `productionVolumeComment` · FieldID 1535 <a href="#field-1535" id="field-1535"></a>

局部 XML 位置：`TIntermediateExchange/productionVolumeComment`；ecoSpold1 对照编号：`724`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString32000` | 否 | 否 |

长度：32000；多语言：是；主数据冗余字段：否。

可对产量数据的数据来源、假设和计算添加一般注释。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceContextId` · FieldID 1536 <a href="#field-1536" id="field-1536"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeSourceContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对来源所属上下文的引用。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceYear` · FieldID 1537 <a href="#field-1537" id="field-1537"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeSourceYear`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString30` | 否 | 否 |

长度：30；多语言：否；主数据冗余字段：是。

分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceFirstAuthor` · FieldID 1538 <a href="#field-1538" id="field-1538"></a>

局部 XML 位置：`TIntermediateExchange/@productionVolumeSourceFirstAuthor`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString40` | 否 | 否 |

长度：40；多语言：否；主数据冗余字段：是。

以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `productionVolumeUncertainty` · FieldID 1539 <a href="#field-1539" id="field-1539"></a>

局部 XML 位置：`TIntermediateExchange/productionVolumeUncertainty`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUncertainty` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

以分布函数及其参数和/或数据质量谱系数据的形式提供不确定性信息。

格式定义见下方的复杂类型部分。

复合类型详情：[ `TUncertainty` ](uncertainty.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `classification` · FieldID 1540 <a href="#field-1540" id="field-1540"></a>

局部 XML 位置：`TIntermediateExchange/classification`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TClassification` | 否 | 是 |

长度：—；多语言：否；主数据冗余字段：是。

包含用于界定产品的分类配对。

复合类型详情：[ `TClassification` ](classification.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：Yes；Group required：Yes。

Comprises fields (additional to the exchanges section) which are only valid for intermediate exchanges. Intermediate exchanges are 
product or waste inputs and outputs recorded in a unit process and its related information.

This section extends the exchanges section in case of intermediate exchanges.

**Inheritance:** These are additional fields; the complete exchange also includes [common exchange fields](exchanges.md).

### `inputGroup` · FieldID 1500 <a href="#en-field-1500" id="en-field-1500"></a>

Local XML path：`TIntermediateExchange/inputGroup`；ecoSpold1 mapping：`3503`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Indicates the kind of input flow. 
The codes are: 1=Materials/Fuels, 2=Electricity/Heat, 3=Services, 5=From Technosphere (unspecified).

For each exchange only an inputGroup or outputGroup shall exist. This indicates the direction of the flow.

**Options (original table)：** 1 = Materials/Fuels; 2 = Electricity/Heat; 3 = Services; 5 = From Technosphere (unspecified)

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `outputGroup` · FieldID 1510 <a href="#en-field-1510" id="en-field-1510"></a>

Local XML path：`TIntermediateExchange/outputGroup`；ecoSpold1 mapping：`3504`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Indicates the kind of output flow. 
The codes are: 0=ReferenceProduct, 2=By-product, 3=MaterialForTreatment, 5=Stock Additions

For each exchange only an inputGroup or outputGroup shall exist. This indicates the direction of the flow.

**Options (original table)：** 0 = ReferenceProduct;  2 = By-product; 3 = Material for Treatment; 5=Stock Additions

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@intermediateExchangeId` · FieldID 1515 <a href="#en-field-1515" id="en-field-1515"></a>

Local XML path：`TIntermediateExchange/@intermediateExchangeId`；ecoSpold1 mapping：`3793`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the master data entry for this intermediate exchange

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@intermediateExchangeContextId` · FieldID 1516 <a href="#en-field-1516" id="en-field-1516"></a>

Local XML path：`TIntermediateExchange/@intermediateExchangeContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the intermediate exchange.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@activityLinkId` · FieldID 1520 <a href="#en-field-1520" id="en-field-1520"></a>

Local XML path：`TIntermediateExchange/@activityLinkId`；ecoSpold1 mapping：`3715`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Explicit reference to the activity which supplies the intermediate product. If this field is empty the activity will determined by a linking rule, which uses geographical and temporal information of this activity.

**Options (original table)：** Reference to 105 (in another activity dataset).

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@activityLinkContextId` · FieldID 1521 <a href="#en-field-1521" id="en-field-1521"></a>

Local XML path：`TIntermediateExchange/@activityLinkContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the activity link.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@activityLinkIdOverwrittenByChild` · FieldID 1522 <a href="#en-field-1522" id="en-field-1522"></a>

Local XML path：`TIntermediateExchange/@activityLinkIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeAmount` · FieldID 1530 <a href="#en-field-1530" id="en-field-1530"></a>

Local XML path：`TIntermediateExchange/@productionVolumeAmount`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | No | No |

Size：—；Multi language：No；Redundant master data：No。

The product volume expressed per year in the same unit as the exchange.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceIdOverwrittenByChild` · FieldID 1531 <a href="#en-field-1531" id="en-field-1531"></a>

Local XML path：`TIntermediateExchange/@productionVolumeSourceIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeVariableName` · FieldID 1532 <a href="#en-field-1532" id="en-field-1532"></a>

Local XML path：`TIntermediateExchange/@productionVolumeVariableName`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TVariableName` | No | No |

Size：40；Multi language：No；Redundant master data：No。

The variable name is a short name for the production volume of the exchange, used when refering to the production volume amount in mathematical relations (formulas). Variables may contain characters, numbers and underscores (\_). Variable names must start with a character (a-z). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceId` · FieldID 1533 <a href="#en-field-1533" id="en-field-1533"></a>

Local XML path：`TIntermediateExchange/@productionVolumeSourceId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

A reference to a valid source.

**Options (original table)：** Reference to a source defined in the modelling and validation section.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeMathematicalRelation` · FieldID 1534 <a href="#en-field-1534" id="en-field-1534"></a>

Local XML path：`TIntermediateExchange/@productionVolumeMathematicalRelation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString32000` | No | No |

Size：32000；Multi language：No；Redundant master data：No。

Defines a mathematical formula which references to values of flows, parameters or properties by variable names or REF function.

The result of the formula with a specific set of variable values is written into the amount field.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `productionVolumeComment` · FieldID 1535 <a href="#en-field-1535" id="en-field-1535"></a>

Local XML path：`TIntermediateExchange/productionVolumeComment`；ecoSpold1 mapping：`724`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString32000` | No | No |

Size：32000；Multi language：Yes；Redundant master data：No。

A general comment can be made on the data source, assumptions and calculations for the production volume data.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceContextId` · FieldID 1536 <a href="#en-field-1536" id="en-field-1536"></a>

Local XML path：`TIntermediateExchange/@productionVolumeSourceContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the source.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceYear` · FieldID 1537 <a href="#en-field-1537" id="en-field-1537"></a>

Local XML path：`TIntermediateExchange/@productionVolumeSourceYear`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString30` | No | No |

Size：30；Multi language：No；Redundant master data：Yes。

Indicates the year of publication and communication, respectively. For web-sites: last visited.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `@productionVolumeSourceFirstAuthor` · FieldID 1538 <a href="#en-field-1538" id="en-field-1538"></a>

Local XML path：`TIntermediateExchange/@productionVolumeSourceFirstAuthor`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString40` | No | No |

Size：40；Multi language：No；Redundant master data：Yes。

Indicates the first author by surname and abbreviated name (e.g., Einstein A.). In case of measurement on site, oral communication, personal written communication and questionnaries ('sourceType'=4, 5, 6, 7) the name of the communicating person is mentioned here.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `productionVolumeUncertainty` · FieldID 1539 <a href="#en-field-1539" id="en-field-1539"></a>

Local XML path：`TIntermediateExchange/productionVolumeUncertainty`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUncertainty` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Uncertainty information in the form of distribution functions and their parameters and/or pedigree data.

For the format definition see the complex type section below.

Complex type details：[ `TUncertainty` ](uncertainty.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

### `classification` · FieldID 1540 <a href="#en-field-1540" id="en-field-1540"></a>

Local XML path：`TIntermediateExchange/classification`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TClassification` | No | Yes |

Size：—；Multi language：No；Redundant master data：Yes。

Contains classification pairs to specify the product.

Complex type details：[ `TClassification` ](classification.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)，`TIntermediateExchange`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **待专家复核 · `TIntermediateExchange.1534.description.1`**：此说明隶属于 @productionVolumeMathematicalRelation，但原文称公式结果写入 amount，可能为通用说明复制残留。官方 EcoSpold02FlowData.xsd 包含同样说明，同时将产量数值字段定义为 productionVolumeAmount；普通交换数值字段为 amount。仅凭XSD说明无法确认软件实际求值目标。译文保留原文 amount。 核对产量公式的实际求值实现，确认目标是否应为 productionVolumeAmount，并由技术编辑同步修正文档；不要据此把产量公式值写入普通交换 amount。

- **已处理／已说明 · `TIntermediateExchange.1530.description.0`**：将 production volume 的“生产量”统一为指南规定的“产量”，保留按年计量、单位与公式引用等全部原条件。 已修正为产量。

- **已处理／已说明 · `TIntermediateExchange.1532.description.0`**：将 production volume 的“生产量”统一为指南规定的“产量”，保留按年计量、单位与公式引用等全部原条件。 已修正为产量。

- **已处理／已说明 · `TIntermediateExchange.1535.description.0`**：将 production volume 的“生产量”统一为指南规定的“产量”，保留按年计量、单位与公式引用等全部原条件。 已修正为产量。
