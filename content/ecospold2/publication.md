# 数据生成者与发布（TDataGeneratorAndPublication）

源文分组：Data generator and publication。本章完整收录 **17 条字段定义**。

XML 位置：`administrativeInformation/dataGeneratorAndPublication`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

包含谁收集、汇编或发布原始数据的信息。此人与 'DataEntryBy' 中的人可能相同，也可能不同。此外，还包含数据集所依据出版物的类型及数据集可访问性的信息。

### `@personId` · FieldID 3500 <a href="#field-3500" id="field-3500"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@personId`；ecoSpold1 对照编号：`751`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 是 | 否 | 否 | 否 |

生成数据集的个人的 ID 编号。该编号必须对应于相应数据集中所列某个人的 ID 编号。

**取值选项（原表）：** 数据生成者的 ID 编号，即收集、汇编或发布原始数据的个人或组织的编号。数据生成者与作者（见 'DataEntryBy'）可能相同，也可能不同。此字段旨在确认并引用数据来源，以及承担主要数据收集工作的个人或组织。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@personContextId` · FieldID 3501 <a href="#field-3501" id="field-3501"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@personContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

引用该人员所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@personName` · FieldID 3505 <a href="#field-3505" id="field-3505"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@personName`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | 是 | 否 | 否 | 是 |

人员的名和姓。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@personEmail` · FieldID 3506 <a href="#field-3506" id="field-3506"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@personEmail`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString80` | 80 | 是 | 否 | 否 | 是 |

人员的完整电子邮件地址。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@dataPublishedIn` · FieldID 3510 <a href="#field-3510" id="field-3510"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@dataPublishedIn`；ecoSpold1 对照编号：`756`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 否 | 否 | 否 | 否 |

表示数据集是否已发布：未发布、部分发布或完整发布。

代码为：0=数据本身未发布（默认）；1=部分单元过程或子系统的数据已发布；2=数据已完整发布于 'referenceToPublishedSource' 中。

**取值选项（原表）：** 0 = 数据本身未在其他地方发布（默认）；1 = 部分单元过程或子系统的数据已发布；2 = 数据已完整发布于某来源中（引用字段 757）。

**XSD 结构约束：** `use="optional"`；`default="0"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceId` · FieldID 3520 <a href="#field-3520" id="field-3520"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@publishedSourceId`；ecoSpold1 对照编号：`757`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

记录该数据集的报告的 ID 编号。

**取值选项（原表）：** 引用 801。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceContextId` · FieldID 3521 <a href="#field-3521" id="field-3521"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@publishedSourceContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

引用该已发布来源所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceIdOverwrittenByChild` · FieldID 3522 <a href="#field-3522" id="field-3522"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@publishedSourceIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 否 | 否 | 否 | 否 |

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceYear` · FieldID 3525 <a href="#field-3525" id="field-3525"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@publishedSourceYear`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString30` | 30 | 否 | 否 | 否 | 是 |

分别表示出版年份或沟通年份。对于网站，表示最后访问年份。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceFirstAuthor` · FieldID 3526 <a href="#field-3526" id="field-3526"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@publishedSourceFirstAuthor`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | 否 | 否 | 否 | 是 |

以姓和名字缩写标明第一作者，例如 Einstein A.。对于现场测量、口头沟通、个人书面沟通和问卷（'sourceType'=4, 5, 6, 7），这里填写沟通人员的姓名。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@pageNumbers` · FieldID 3530 <a href="#field-3530" id="field-3530"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@pageNumbers`；ecoSpold1 对照编号：`762`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TBaseString30` | 30 | 否 | 否 | 否 | 否 |

若数据取自文章或较大型出版物的特定页面，则填写相关页码。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@isCopyrightProtected` · FieldID 3540 <a href="#field-3540" id="field-3540"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@isCopyrightProtected`；ecoSpold1 对照编号：`758`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 是 | 否 | 否 | 否 |

表示是否存在著作权。应相应填写 '1'（是）或 '0'（否）。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@accessRestrictedTo` · FieldID 3550 <a href="#field-3550" id="field-3550"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@accessRestrictedTo`；ecoSpold1 对照编号：`759`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | 否 | 否 | 否 | 否 |

表示数据集可能存在的访问限制。

所用代码为：0=公开；1=被许可人；2=仅结果；3=受限制。

accessRestrictedTo=0：无访问限制。

accessRestrictedTo=1：只有许可证持有者（由上下文定义）可以访问。

accessRestrictedTo=2：许可证持有者（由上下文定义）可以访问 LCI 结果，但不能访问单元过程原始数据。数据库管理员具有完整访问权限。

accessRestrictedTo=3：只有 'companyCode' 指定的组织和数据库管理员可以访问。

**取值选项（原表）：** 0=公开；1=被许可人；2=仅结果；3=受限制。

**XSD 结构约束：** `use="optional"`；`default="0"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyId` · FieldID 3560 <a href="#field-3560" id="field-3560"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@companyId`；ecoSpold1 对照编号：`760`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

引用允许使用此数据集的组织／机构；数据集使用限于该组织／机构。

**取值选项（原表）：** 如果 759=3。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyContextId` · FieldID 3561 <a href="#field-3561" id="field-3561"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@companyContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | 否 | 否 | 否 | 否 |

引用该公司所属的上下文。

如果省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyCode` · FieldID 3562 <a href="#field-3562" id="field-3562"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@companyCode`；ecoSpold1 对照编号：`760`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `TCompanyCode` | 7 | 否 | 否 | 否 | 是 |

所引用公司（字段 3560）的可选 7 字母代码的纯文本值。

**取值选项（原表）：** 如果 759=3。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyIdOverwrittenByChild` · FieldID 3563 <a href="#field-3563" id="field-3563"></a>

局部 XML 位置：`TDataGeneratorAndPublication/@companyIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 长度 | 必填 | 可重复 | 多语言 | 主数据冗余字段 |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | 否 | 否 | 否 | 否 |

如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Contains information about who collected, compiled or published the orginal data. This may or may not be the same person as under 'DataEntryBy'. Furthermore contains information about kind of publication underlying the dataset and the accessibility of the dataset.

### `@personId` · FieldID 3500 <a href="#en-field-3500" id="en-field-3500"></a>

Local XML path：`TDataGeneratorAndPublication/@personId`；ecoSpold1 mapping：`751`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | Yes | No | No | No |

ID number for the person that generated the dataset. It must correspond to an ID number of a person listed in the respective dataset.

**Options (original table)：** ID number for the data generator, i.e. the person or organisation that collected, compiled or published the original data. This may or may not be the same person as the author (see 'DataEntryBy'). The purpose of this field is to acknowledge and reference the origin of the data and the person or organisation that performed the majority of the work in data collection.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@personContextId` · FieldID 3501 <a href="#en-field-3501" id="en-field-3501"></a>

Local XML path：`TDataGeneratorAndPublication/@personContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the person.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@personName` · FieldID 3505 <a href="#en-field-3505" id="en-field-3505"></a>

Local XML path：`TDataGeneratorAndPublication/@personName`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | Yes | No | No | Yes |

Name and surname of the person.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@personEmail` · FieldID 3506 <a href="#en-field-3506" id="en-field-3506"></a>

Local XML path：`TDataGeneratorAndPublication/@personEmail`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString80` | 80 | Yes | No | No | Yes |

Complete email address of the person.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@dataPublishedIn` · FieldID 3510 <a href="#en-field-3510" id="en-field-3510"></a>

Local XML path：`TDataGeneratorAndPublication/@dataPublishedIn`；ecoSpold1 mapping：`756`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | No | No | No | No |

Indicates whether the dataset has been published (not, partly, entirely).

The codes are: 0=Data as such not published (default). 1=The data of some unit processes or subsystems are published. 2=Data has been published entirely in 'referenceToPublishedSource'.

**Options (original table)：** 0 = Data as such not published elsewhere (default), 1 = The data of some unit processes or subsystems are published, 2 = Data has been published entirely in (refers to field 757)

**XSD structural constraints：** `use="optional"`；`default="0"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceId` · FieldID 3520 <a href="#en-field-3520" id="en-field-3520"></a>

Local XML path：`TDataGeneratorAndPublication/@publishedSourceId`；ecoSpold1 mapping：`757`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

ID number for the report in which the dataset is documented.

**Options (original table)：** Reference to 801

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceContextId` · FieldID 3521 <a href="#en-field-3521" id="en-field-3521"></a>

Local XML path：`TDataGeneratorAndPublication/@publishedSourceContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the published source.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceIdOverwrittenByChild` · FieldID 3522 <a href="#en-field-3522" id="en-field-3522"></a>

Local XML path：`TDataGeneratorAndPublication/@publishedSourceIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | No | No | No | No |

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceYear` · FieldID 3525 <a href="#en-field-3525" id="en-field-3525"></a>

Local XML path：`TDataGeneratorAndPublication/@publishedSourceYear`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString30` | 30 | No | No | No | Yes |

Indicates the year of publication and communication, respectively. For web-sites: last visited.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@publishedSourceFirstAuthor` · FieldID 3526 <a href="#en-field-3526" id="en-field-3526"></a>

Local XML path：`TDataGeneratorAndPublication/@publishedSourceFirstAuthor`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString40` | 40 | No | No | No | Yes |

Indicates the first author by surname and abbreviated name (e.g., Einstein A.). In case of measurement on site, oral communication, personal written communication and questionnaries ('sourceType'=4, 5, 6, 7) the name of the communicating person is mentioned here.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@pageNumbers` · FieldID 3530 <a href="#en-field-3530" id="en-field-3530"></a>

Local XML path：`TDataGeneratorAndPublication/@pageNumbers`；ecoSpold1 mapping：`762`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TBaseString30` | 30 | No | No | No | No |

The relevant page numbers if the data are sourced on specific pages in an article or larger publication.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@isCopyrightProtected` · FieldID 3540 <a href="#en-field-3540" id="en-field-3540"></a>

Local XML path：`TDataGeneratorAndPublication/@isCopyrightProtected`；ecoSpold1 mapping：`758`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | Yes | No | No | No |

Indicates whether or not a copyright exists. '1' (Yes) or '0' (No) should be entered correspondingly.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@accessRestrictedTo` · FieldID 3550 <a href="#en-field-3550" id="en-field-3550"></a>

Local XML path：`TDataGeneratorAndPublication/@accessRestrictedTo`；ecoSpold1 mapping：`759`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `integer` | — | No | No | No | No |

Indicates possible access restrictions for the dataset.

The codes used are: 0=Public, 1=Licensees, 2=Results only, 3=Restricted

accessRestrictedTo=0: No access restrictions.

accessRestrictedTo=1: only license holders (as defined by context) have access.

accessRestrictedTo=2: license holders (as defined by context) have access to LCI results but not to unit process raw data. Database administrator have full access.

accessRestrictedTo=3: only the organisation specified by 'companyCode' and the database administrator have access.

**Options (original table)：** 0=Public, 1=Licensees, 2=Results only, 3=Restricted

**XSD structural constraints：** `use="optional"`；`default="0"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyId` · FieldID 3560 <a href="#en-field-3560" id="en-field-3560"></a>

Local XML path：`TDataGeneratorAndPublication/@companyId`；ecoSpold1 mapping：`760`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to an organisation/institute that the use of this dataset is restricted to.

**Options (original table)：** If 759=3

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyContextId` · FieldID 3561 <a href="#en-field-3561" id="en-field-3561"></a>

Local XML path：`TDataGeneratorAndPublication/@companyContextId`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TUuid` | 36 | No | No | No | No |

Reference to the context of the company.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyCode` · FieldID 3562 <a href="#en-field-3562" id="en-field-3562"></a>

Local XML path：`TDataGeneratorAndPublication/@companyCode`；ecoSpold1 mapping：`760`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `TCompanyCode` | 7 | No | No | No | Yes |

Optional 7 letter code plaintext of the referenced company (field 3560)

**Options (original table)：** If 759=3

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

### `@companyIdOverwrittenByChild` · FieldID 3563 <a href="#en-field-3563" id="en-field-3563"></a>

Local XML path：`TDataGeneratorAndPublication/@companyIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Size | Required | Multiple occurrence | Multi language | Redundant master data |
| --- | --- | --- | --- | --- | --- |
| `boolean` | — | No | No | No | No |

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TDataGeneratorAndPublication`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **已处理／已说明 · `TDataGeneratorAndPublication.3560.options`**：已对照官方 XSD 确认，这些编号是旧 SpoldID 引用：accessRestrictedTo 的 spoldID=759、fieldId=3550；publishedSourceId 的 spoldID=757、fieldId=3520；TValidSource/@id 的 spoldID=801、fieldId=3110。原文条件与编号映射一致。 保留原文 759=3、757 和 801；在按新版 fieldId 查找时使用上述对应关系。证据：Schemas/datasets/EcoSpold02MetaInformation.xsd 及 Schemas/MasterData/EcoSpold02Sources.xsd。

- **已处理／已说明 · `TDataGeneratorAndPublication.3522.description.0`**：已明确翻译子数据集删除引用与未提供引用的继承语义：必须将xxxOverwrittenByChild设为true，否则仍解释为保留父数据集值；不将删除引用误译为自动覆盖。 该规则同样适用于3563字段，译文已保持一致。
