# ecoSpold2 XML 字段参考

本部分将官方 `Format description/EcoSpold02.html` 拆分为 **22 个字段章节、243 条字段定义**，按 XML 结构组织。每条保留字段名、FieldID、ecoSpold1 对照编号、数据类型、长度、必填性、重复性、多语言和主数据冗余标记，以及完整的说明和取值选项。中文与英文可切换核对。

来源：[ecoinvent 官方 ecoSpold2 页面](https://support.ecoinvent.org/ecospold2) · [官方格式包](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/documentation_on_ecospold2_format.v1.0.13.zip) · [原件 ZIP](original/documentation_on_ecospold2_format.v1.0.13.zip)

格式包文件名版本为 **v1.0.13**，所附 XSD 的 `version` 为 **2.0.13**。这是该格式包的参考译本；应以实际数据文件对应的模式版本校验，不把历史格式说明视为所有新版本的完整规范。

## 如何查字段

1. 已知字段名：打开[字段索引](field-index.md)，搜索 `@amount`、`activityLinkId` 或 FieldID。
2. 正在阅读 XML：按父元素选择活动、交换、参数或管理信息章节；同名属性在不同结构下可能有不同含义。
3. 正在开发导入器：先看[阅读约定与 XSD 约束](reading-guide.md)，再结合每条的 XSD 出处检查。

## 按 XML 结构阅读

- [活动描述](activity-description.md)：活动、活动分类、地理区域、技术、时间范围、宏观经济情景。
- [交换数据与结果](flow-data.md)：交换的通用字段、中间交换专用字段、基本流交换专用字段、参数、影响指标结果。
- [复合类型](complex-types.md)：区室与子区室、不确定性与分布参数、交换属性、转移系数、文本、图像与文本变量。
- [建模与审查](modelling-validation.md)：代表性、审查。
- [管理信息](administrative-information.md)：数据录入者、数据生成者与发布、文件属性、所需上下文引用。

## 原文的阅读说明

{% tabs %}

{% tab title="中文" %}

本文档提供 EcoSpold02 模式的简化视图。开发者还应查阅模式文件，以确保正确实现该格式。

为区分 Xml 属性与元素，属性名称以“@”为前缀。

“SpoldID, version 1”列中编号后添加的标记，用于表示相对于 EcoSpold01 的变化。

“SpoldID, version 1”列用于帮助查找 EcoSpold01 字段。讨论该格式时，请使用新的“fieldId”列。

以下第 1 版 SpoldId 已在 EcoSpold02 格式中移除：

205	languageCode, 206	localLanguageCode, 208	impactAssessmentResult 400	datasetRelatesToProduct, 403	unit, 404	amount 490	localName, 493	infrastructureProcess, 494	infrastructureIncluded, 495	category, 496	subCategory, 497	localCategory, 498	localSubCategory, 499	formula 502	CASNumber 727	uncertaintyAdjustments, 761	countryCode 2401	referenceToCoProduct, 2403	allocationMethod, 2404	fraction, 2492	referenceToInputOutput 3506	category, 3507	subCategory, 3508	infrastructureProcess, 3509	localCategory, 3510	localSubCategory 3703	location, 3709	standardDeviation95, 3711	formula, 3794	localName, 3795	minValue, 3796	maxValue, 3797	mostLikelyValue 5807	companyCode, 5808	countryCode

{% endtab %}

{% tab title="English 原文" %}

This documentation provides a simplified view of the EcoSpold02 schemata. Developers should consult the schema files as well to make sure the format is implemented correctly.

To distinguish Xml attributes from elements attribute names are prefixed by "@".

Additions behind the numbers in the "SpoldID, version 1" column are used to indicate changes compared to EcoSpold01.

The "SpoldID, version 1" column is used to help find EcoSpold01 fields. Please use the new "fieldId" column for communications regarding the format.

The following version 1 SpoldIds have been removed in the EcoSpold02 format:

205	languageCode, 206	localLanguageCode, 208	impactAssessmentResult 400	datasetRelatesToProduct, 403	unit, 404	amount 490	localName, 493	infrastructureProcess, 494	infrastructureIncluded, 495	category, 496	subCategory, 497	localCategory, 498	localSubCategory, 499	formula 502	CASNumber 727	uncertaintyAdjustments, 761	countryCode 2401	referenceToCoProduct, 2403	allocationMethod, 2404	fraction, 2492	referenceToInputOutput 3506	category, 3507	subCategory, 3508	infrastructureProcess, 3509	localCategory, 3510	localSubCategory 3703	location, 3709	standardDeviation95, 3711	formula, 3794	localName, 3795	minValue, 3796	maxValue, 3797	mostLikelyValue 5807	companyCode, 5808	countryCode

{% endtab %}

{% endtabs %}

**范围说明：** 243 条是主数据集格式 HTML 中的全部字段条目，不是整个 XSD 包中全部节点的数量。主数据文件和基础类型的额外定义保留在原包中，入口见[阅读指南](reading-guide.md)。

译稿完成 AI 自审和独立 AI 交叉审阅；校验覆盖源文块、字段元数据、链接和原件哈希。具体原文疑点、已修正问题见[本部分审校记录](translation-review.md)，不代表人工专家签核或 ecoinvent 官方认证。
