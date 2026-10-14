# 文件属性（TFileAttributes）

源文分组：File attributes。本章完整收录 **13 条字段定义**。

XML 位置：`administrativeInformation/fileAttributes`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

包含关于整个文件的元信息。

### `@majorRelease` · FieldID 3800 <a href="#field-3800" id="field-3800"></a>

局部 XML 位置：`TFileAttributes/@majorRelease`；ecoSpold1 对照编号：`202`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

每次重大更新时，主发布版本号加一，例如每两年一次。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@minorRelease` · FieldID 3805 <a href="#field-3805" id="field-3805"></a>

局部 XML 位置：`TFileAttributes/@minorRelease`；ecoSpold1 对照编号：`202`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

在两次重大更新之间，每次发布时次发布版本号加一。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@majorRevision` · FieldID 3810 <a href="#field-3810" id="field-3810"></a>

局部 XML 位置：`TFileAttributes/@majorRevision`；ecoSpold1 对照编号：`207`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

修订号针对每个数据集单独设定，独立于整个数据库的发布版本，用于区分数据库主／次发布版本内的数据集不同版本。主修订号反映数据集已接受变更的数量，只能随时间增加，不得手动更改。在 ecoinvent 上下文中，每当活动变更加入数据库（即通过审查流程后），主修订号都会增加，同时将次修订号重置为 1。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@minorRevision` · FieldID 3815 <a href="#field-3815" id="field-3815"></a>

局部 XML 位置：`TFileAttributes/@minorRevision`；ecoSpold1 对照编号：`207`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

次修订号描述数据集在提交审查前编辑过程中的版本。在 ecoinvent 上下文中，每当数据提供者将对数据集的修改保存到本地，或作为草稿保存到 ecoinvent 服务器时，次修订号都会自动增加。每当主修订号增加（即数据集变更被审查者接受）时，次修订号重置为“1”。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@defaultLanguage` · FieldID 3820 <a href="#field-3820" id="field-3820"></a>

局部 XML 位置：`TFileAttributes/@defaultLanguage`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `string` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

该数据集所有多语言字段的默认语言。每个多语言字段至少应包含默认语言的值。如果未提供 defaultLanguage，则使用默认值（"en"）。

**XSD 结构约束：** `use="optional"`；`default="en"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@creationTimestamp` · FieldID 3830 <a href="#field-3830" id="field-3830"></a>

局部 XML 位置：`TFileAttributes/@creationTimestamp`；ecoSpold1 对照编号：`204a`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `dateTime` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

数据集创建时自动生成的日期。

**取值选项（原表）：** 数据集创建时间。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@lastEditTimestamp` · FieldID 3840 <a href="#field-3840" id="field-3840"></a>

局部 XML 位置：`TFileAttributes/@lastEditTimestamp`；ecoSpold1 对照编号：`204b`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `dateTime` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

数据集保存时自动生成的日期。

**取值选项（原表）：** 数据集最后编辑时间。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@internalSchemaVersion` · FieldID 3850 <a href="#field-3850" id="field-3850"></a>

局部 XML 位置：`TFileAttributes/@internalSchemaVersion`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString80` | 否 | 否 |

长度：80；多语言：否；主数据冗余字段：否。

数据集基于此内部模式版本生成。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@fileGenerator` · FieldID 3860 <a href="#field-3860" id="field-3860"></a>

局部 XML 位置：`TFileAttributes/@fileGenerator`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TBaseString255` | 否 | 否 |

长度：255；多语言：否；主数据冗余字段：否。

对创建此文件的程序的描述，最好包含版本。

**XSD 结构约束：** `use="optional"`（XSD 默认值）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@fileTimestamp` · FieldID 3870 <a href="#field-3870" id="field-3870"></a>

局部 XML 位置：`TFileAttributes/@fileTimestamp`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `dateTime` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

此文件创建的时间和日期。

**XSD 结构约束：** `use="optional"`（XSD 默认值）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@contextId` · FieldID 3880 <a href="#field-3880" id="field-3880"></a>

局部 XML 位置：`TFileAttributes/@contextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

表示此数据集所面向的上下文。该信息例如用于将数据集信息的可访问性限制在一个特定上下文内，并确定访问它所需的主数据文件。如果省略此属性，则假定该数据集为独立数据集，且无法解析主数据引用以取得所引用内容。

上下文取代 ecoSpold01 的质量网络（字段 id 304）。ecoinvent 质量网络的上下文 ID 可在 Context.xml 主数据文件中找到。

**XSD 结构约束：** `use="optional"`（XSD 默认值）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `contextName` · FieldID 3885 <a href="#field-3885" id="field-3885"></a>

局部 XML 位置：`TFileAttributes/contextName`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString80` | 否 | 否 |

长度：80；多语言：是；主数据冗余字段：是。

字段 3880 所引用上下文的名称。

上下文取代 ecoSpold01 的质量网络（字段 id 304）。ecoinvent 质量网络的上下文 ID 可在 Context.xml 主数据文件中找到。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `requiredContext` · FieldID 3890 <a href="#field-3890" id="field-3890"></a>

局部 XML 位置：`TFileAttributes/requiredContext`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TRequiredContextReference` | 否 | 是 |

长度：—；多语言：否；主数据冗余字段：否。

引用加载本文档所必需的上下文，以完整保留文档中的所有主数据引用。

复合类型详情：[ `TRequiredContextReference` ](required-contexts.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Contains metainformation regarding the file as a whole.

### `@majorRelease` · FieldID 3800 <a href="#en-field-3800" id="en-field-3800"></a>

Local XML path：`TFileAttributes/@majorRelease`；ecoSpold1 mapping：`202`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The major release number is increased by one with each major update (e.g. every second year).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@minorRelease` · FieldID 3805 <a href="#en-field-3805" id="en-field-3805"></a>

Local XML path：`TFileAttributes/@minorRelease`；ecoSpold1 mapping：`202`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The minor release number is increased by one for each release within the period of two major updates.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@majorRevision` · FieldID 3810 <a href="#en-field-3810" id="en-field-3810"></a>

Local XML path：`TFileAttributes/@majorRevision`；ecoSpold1 mapping：`207`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The revision number is specific to each dataset and is independent of the overall database release version and is used to discern different versions of the dataset within the database major/minor release versions. The major revision number reflects the amount of accepted changes to the dataset. It will only increase over time and must not be changed manually. In the ecoinvent context the major revision is increased each time changes to an activity are added to the database (i.e. after they passed the review process). This also resets the minor revision to 1.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@minorRevision` · FieldID 3815 <a href="#en-field-3815" id="en-field-3815"></a>

Local XML path：`TFileAttributes/@minorRevision`；ecoSpold1 mapping：`207`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The minor revision number describes versions of the dataset during the editing process before it is submitted for review. In th eecoinvent context it is increased automatically every time the data provider saves changes made to the dataset either locally or as a draft on the ecoinvent server. The minor revision number is reset to “1” each time the major revision number is increased (when changes to a dataset are accepted by a reviewer).

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@defaultLanguage` · FieldID 3820 <a href="#en-field-3820" id="en-field-3820"></a>

Local XML path：`TFileAttributes/@defaultLanguage`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `string` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Default language for all multi language fields of this dataset. Any multi language field should contain a value at least for the default language. If no defaultLanguage is given, the default value ("en") will be used.

**XSD structural constraints：** `use="optional"`；`default="en"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@creationTimestamp` · FieldID 3830 <a href="#en-field-3830" id="en-field-3830"></a>

Local XML path：`TFileAttributes/@creationTimestamp`；ecoSpold1 mapping：`204a`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `dateTime` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Automatically generated date when dataset is created.

**Options (original table)：** Time of creation of dataset

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@lastEditTimestamp` · FieldID 3840 <a href="#en-field-3840" id="en-field-3840"></a>

Local XML path：`TFileAttributes/@lastEditTimestamp`；ecoSpold1 mapping：`204b`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `dateTime` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Automatically generated date when dataset is saved.

**Options (original table)：** Time of last editing of dataset

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@internalSchemaVersion` · FieldID 3850 <a href="#en-field-3850" id="en-field-3850"></a>

Local XML path：`TFileAttributes/@internalSchemaVersion`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString80` | No | No |

Size：80；Multi language：No；Redundant master data：No。

Dataset is generated based on this internal schema version.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@fileGenerator` · FieldID 3860 <a href="#en-field-3860" id="en-field-3860"></a>

Local XML path：`TFileAttributes/@fileGenerator`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TBaseString255` | No | No |

Size：255；Multi language：No；Redundant master data：No。

Description of the program which created this file. Preferably including version.

**XSD structural constraints：** `use="optional"` (XSD default)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@fileTimestamp` · FieldID 3870 <a href="#en-field-3870" id="en-field-3870"></a>

Local XML path：`TFileAttributes/@fileTimestamp`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `dateTime` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Time and date this file was created.

**XSD structural constraints：** `use="optional"` (XSD default)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `@contextId` · FieldID 3880 <a href="#en-field-3880" id="en-field-3880"></a>

Local XML path：`TFileAttributes/@contextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Indicates the context for which this dataset is designed. The information is used, e.g. for restricting the accessibility of dataset information to one particular context and to determine which master data files are needed to access it. If this attribute is omitted the dataset is assumed to be a standalone dataset and masterdata references can not be dereferenced.

The context replaces the ecoSpold01 quality network (field id 304). The context id for the ecoinvent quality network can be found in the Context.xml master data file.

**XSD structural constraints：** `use="optional"` (XSD default)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `contextName` · FieldID 3885 <a href="#en-field-3885" id="en-field-3885"></a>

Local XML path：`TFileAttributes/contextName`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString80` | No | No |

Size：80；Multi language：Yes；Redundant master data：Yes。

The name of the context referenced by field 3880.

The context replaces the ecoSpold01 quality network (field id 304). The context id for the ecoinvent quality network can be found in the Context.xml master data file.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

### `requiredContext` · FieldID 3890 <a href="#en-field-3890" id="en-field-3890"></a>

Local XML path：`TFileAttributes/requiredContext`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TRequiredContextReference` | No | Yes |

Size：—；Multi language：No；Redundant master data：No。

Reference to a context required to load this document with all its master data references intact.

Complex type details：[ `TRequiredContextReference` ](required-contexts.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TFileAttributes`。

{% endtab %}

{% endtabs %}
