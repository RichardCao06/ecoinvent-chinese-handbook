# 阅读约定与 XSD 约束

## 字段名、路径与 FieldID

`@amount` 表示 XML 属性 `amount="…"`；没有 `@` 的名称表示子元素。章节中 `TActivity`、`TUncertainty` 等是 XSD 类型名，不是 XML 标签。FieldID 是格式规范的字段编号，不是活动、交换或主数据条目的 UUID。

每条的“局部 XML 位置”从所属模式类型开始。嵌套属性会保留父元素，例如 `TUncertainty/lognormal/@meanValue` 与 `TUncertainty/normal/@meanValue` 含义不同。正文开头另给出在数据集中的位置；`…` 表示可在多个位置复用的结构。

## 数据集的顶层结构

以下为所附 XSD 的结构导读，省略了属性和内部子元素，不是一份可直接通过模式校验的数据集：

```text
ecoSpold
├── activityDataset
│   ├── activityDescription
│   ├── flowData
│   ├── modellingAndValidation
│   └── administrativeInformation
└── childActivityDataset（另一种可选数据集分支）
```

根模式允许多个数据集；`activityDataset` 与 `childActivityDataset` 在 `xsd:choice` 中选择。两个容器元素都属于 `http://www.EcoInvent.org/EcoSpold02` 命名空间。`activityDataset` 使用该命名空间的 `TActivityDataset` 类型；`childActivityDataset` 使用 `http://www.EcoInvent.org/EcoSpold02Child` 命名空间的 `TActivityDataset` 类型，其内部子元素属于子数据集命名空间。容器元素的命名空间与其类型或内部元素的命名空间须分别判断。出处：[EcoSpold02.xsd](original/Schemas/datasets/EcoSpold02.xsd)、[EcoSpold02Activity.xsd](original/Schemas/datasets/EcoSpold02Activity.xsd)、[EcoSpold02ChildActivity.xsd](original/Schemas/datasets/EcoSpold02ChildActivity.xsd)。

## 如何理解原表的标记

| 标记 | 阅读方式 |
| --- | --- |
| 类型 Type | 保留官方类型名，例如 `TUuid`、`TFloatNumber`；具体定义见 XSD。 |
| 长度 Size | 忠实保留原表。`—` 表示原表未列出，不表示字段无约束。 |
| 必填 Req | 表示所属结构中的要求；还需判断父元素是否出现、选择了哪个分支以及是否为子数据集。 |
| 可重复 Multiple Occurrence | 保留原表的逻辑重复标记；序列化出现次数另列 XSD `minOccurs` / `maxOccurs`。 |
| 多语言 Multi Language | 表示支持多语言文本；部分文本通过多个带 `xml:lang` 的同名元素表示，不能只根据“可重复：否”拒绝这些元素。 |
| 主数据冗余 Redundant Master Data | 指原表标识的主数据冗余字段；名称、单位等可能随 UUID 引用一起存入数据集，不应自行删除。 |
| Options | 保留枚举值与说明的对应关系。正文说明还可能包含额外条件，不能只读枚举表。 |
| SpoldID, version 1 | 用于与 ecoSpold1 对照；`new`、`rename`、`type` 等变更标记保留原样，不是 XML 值。 |

## XSD 约束优先结合上下文解释

每条的“XSD 结构约束”来自同一原包中的元素或属性声明。XML 属性未写 `use` 时默认 `optional`；元素未写 `minOccurs` / `maxOccurs` 时默认均为 `1`。这些值只描述局部声明，不替代完整模式校验。

尤其需要注意 `xsd:choice`：一个 `uncertainty` 选择恰好一种分布，不要求同时包含所有分布。选择 `lognormal` 后，才判断其属性的必填要求。`TTextAndImage` 的选择组则允许多次出现，不能用同一规则理解所有选择组。父级次数、序列、继承、唯一性约束以及类型限制也需在 XSD 中核对。

多个“原表可重复：否”的多语言字段，在 XSD 中的 `maxOccurs` 是 `unbounded`；前者按原表保留，后者按序列化结构展示。若实现软件，应检查 `xml:lang` 的唯一性约束，而不是把不同语言的文本当作无条件重复数据。

## 基础类型、文本属性与完整模式

243 条字段来自 `EcoSpold02.html`。基础类型内部的属性或结构（例如文本的 `xml:lang`、排序用 `index`、文本变量名称）未必在主 HTML 中逐项列为 FieldID，因此还应查 [EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd) 与 [XmlNamespace.xsd](original/Schemas/XmlNamespace.xsd)。本部分没有把主 HTML 的条目数称为整个模式的全部节点数量。

活动描述、建模和管理信息：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)。交换、参数与影响指标：[EcoSpold02FlowData.xsd](original/Schemas/datasets/EcoSpold02FlowData.xsd)。继承型子数据集须查原包中的 `EcoSpold02Child*.xsd`，不能直接套用正常数据集的全部必填要求。

## 主数据文件的字段说明

本次中文逐字段译稿覆盖用户指定的 `EcoSpold02.html`。原包中的以下主数据 HTML 保留英文原件，可用于查 UUID 引用的目标字段：

- [EcoSpold02ActivityNames](original/Format%20description/EcoSpold02ActivityNames.html)
- [EcoSpold02Classifications](original/Format%20description/EcoSpold02Classifications.html)
- [EcoSpold02Companies](original/Format%20description/EcoSpold02Companies.html)
- [EcoSpold02Compartments](original/Format%20description/EcoSpold02Compartments.html)
- [EcoSpold02Context](original/Format%20description/EcoSpold02Context.html)
- [EcoSpold02ElementaryExchanges](original/Format%20description/EcoSpold02ElementaryExchanges.html)
- [EcoSpold02Geographies](original/Format%20description/EcoSpold02Geographies.html)
- [EcoSpold02IntermediateExchanges](original/Format%20description/EcoSpold02IntermediateExchanges.html)
- [EcoSpold02Languages](original/Format%20description/EcoSpold02Languages.html)
- [EcoSpold02MacroEconomicScenarios](original/Format%20description/EcoSpold02MacroEconomicScenarios.html)
- [EcoSpold02Parameters](original/Format%20description/EcoSpold02Parameters.html)
- [EcoSpold02Persons](original/Format%20description/EcoSpold02Persons.html)
- [EcoSpold02Properties](original/Format%20description/EcoSpold02Properties.html)
- [EcoSpold02Sources](original/Format%20description/EcoSpold02Sources.html)
- [EcoSpold02SystemModels](original/Format%20description/EcoSpold02SystemModels.html)
- [EcoSpold02Tags](original/Format%20description/EcoSpold02Tags.html)
- [EcoSpold02Units](original/Format%20description/EcoSpold02Units.html)

[下载完整官方原包](original/documentation_on_ecospold2_format.v1.0.13.zip) · [字段索引](field-index.md) · [审校记录](translation-review.md)
