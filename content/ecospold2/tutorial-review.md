# 完整教程的编写与运行审阅

本教程将字段参考改写为连续的中文文章，覆盖主 HTML 的 **22 个分组、243 条字段**。三组叙述分别由另一位 AI 逐段审核，导读、实践代码和提取器也有独立审阅记录。明确的写作错误已修正；原文与模式的具体差异保留在正文及下方清单中。

三份 demo 是教学构造数据，已按原包 XSD 验证。提取器和查询例子通过实际运行及回归检查：读取电力、环境水、正负直接排放、供应候选和模拟 LCIA 指标；还检查了命名空间、多数据集、继承、缺失值、参考量异常、语言回退，以及跨模型和发布版本的候选。验证脚本位于仓库 `tools/test_ecospold_tutorial.py`。

数值练习中的方法与系数均是教学约定。测试不会为这些数值提供 ecoinvent 认证、清单完整性认证或真实 LCIA 方法认证；它确认文中程序与所给 demo 的行为一致。

本页保留 **29 条教程编写注记**，包括已修正问题、模式限定和需数据方进一步澄清的源文问题。它们与原字段参考的 27 条记录有范围重叠，不能相加为独立问题数量。原逐块翻译记录仍见[字段翻译与审校记录](translation-review.md)。

本轮按 XML 结构拆为五组 22 篇字段文章，替换独立表格翻译页。各章增加定位路径、使用说明与实际 demo 读取片段；`read_section.py` 只读取原始属性和节点树，不计算 LCI/LCIA，也不代替 XSD 或语义验证。新增的章节读取测试实际执行全部 22 段代码，并检查多语言、嵌套数量、负输出、缺失结构、多数据集与子数据集拒绝；与原 12 项提取器测试分别记录。

## 教程注记

### 1. 待专家复核 · TActivity 135

相关正文：[活动](activity.md#read-tactivity)

继承深度的父层数定义与地理／时间／情景类型说明之间关系未明确；正文保留原定义及0–3含义，不自行推断父链。

依据继承专门规范确认各层级的允许关系。

### 2. 待专家复核 · TActivity 120

相关正文：[活动](activity.md#read-tactivity)

格式说明的 TTextAndImage 复用段落写 imageUri，官方 XSD 实际元素名为 imageUrl。正文明确区分说明文字与模式标识，未静默改写源文。

解析采用实际XSD名称，建议官方统一说明命名；同问题涉及195、420、510、630等文本图像字段。

### 3. 待专家复核 · TClassification 300

相关正文：[分类](classification.md#read-tclassification)

classificationSystem 与 classificationValue 的说明称可选，但完整XSD默认minOccurs=1且HTML表格列为必填。正文并列说明差异。

实现时区分完整与子模式，并请数据方统一说明中的可选性。

### 4. 待专家复核 · TRequiredContextReference 7850

相关正文：[所需上下文引用](required-contexts.md#read-trequiredcontextreference)

requiredContextId 说明存在省略时回退，但当前完整XSD将其设为required。正文明确交代矛盾，不将回退说明变为可省略的验证规则。

请确认回退说明是否面向其他模式或早期版本；完整模式校验按XSD执行。

### 5. 已处理／已说明 · TDataGeneratorAndPublication 3560

相关正文：[数据生成者与发布](publication.md#read-tdatageneratorandpublication)

759、757及801是有效旧SpoldID引用，已依据XSD在正文解释对应当前fieldId 3550、3520及3110。

保持附译表中的原编号，通过明确的映射理解访问条件与来源引用。

### 6. 待专家复核 · TDataGeneratorAndPublication 3562

相关正文：[数据生成者与发布](publication.md#read-tdatageneratorandpublication)

原文及 TCompanyCode 的文字说明要求 7 个大写字母，但 XSD 仅规定 maxLength=7，没有固定长度和字母模式。

正文已区分文字约定与 XSD 约束；是否另有业务语义验证规则需由数据方确认。

### 7. 已处理／已说明 · TActivity 130

相关正文：[活动](activity.md#read-tactivity)

补明 EcoSpold02.xsd 中子数据集外层容器仍属于普通命名空间，避免将子类型的命名空间误套在容器元素上。

已在正文修正或补明。

### 8. 已处理／已说明 · TDataEntryBy 3403

相关正文：[数据录入者](data-entry.md#read-tdataentryby)

明确默认值来自完整数据模式；子模式未设该默认值，省略时先按继承处理。

已在正文修正或补明。

### 9. 已处理／已说明 · TDataGeneratorAndPublication 3525

相关正文：[数据生成者与发布](publication.md#read-tdatageneratorandpublication)

原文网站情况仅写 last visited，不能擅自缩窄为最后访问年份。

已在正文修正或补明。

### 10. 已处理／已说明 · TDataGeneratorAndPublication 3562

相关正文：[数据生成者与发布](publication.md#read-tdatageneratorandpublication)

区分文字约定与 TCompanyCode 实際 maxLength=7 约束，不让教程暗示 XSD 强制恰好 7 个字母。

已在正文修正或补明。

### 11. 已处理／已说明 · TFileAttributes 3820

相关正文：[文件属性](file-attributes.md#read-tfileattributes)

子模式未设 default=en；澄清完整记录的模式默认值与子差异记录的继承。

已在正文修正或补明。

### 12. 已处理／已说明 · TRequiredContextReference 7810

相关正文：[所需上下文引用](required-contexts.md#read-trequiredcontextreference)

补明官方子类型中的 use=optional 与 minOccurs=0，避免把完整数据模式的要求泛化到子差异记录。

已在正文修正或补明。

### 13. 待专家复核 · TActivity 110

相关正文：[活动](activity.md#read-tactivity)

官方 type=2 文字说明称没有中间交换，但本包完整 TFlowData 对 intermediateExchange 的默认 minOccurs=1；教学结果文件以中间交换保留参考输出并通过模式验证。

正文明确区分产品系统已汇总与 XML 参考输出；真实不同导出形式仍应按来源和实例确认，不能把说明中的绝对句用于文件阶段判定。

### 14. 待专家复核 · TParameter 1715

相关正文：[参数](parameters.md#read-tparameter)

该说明位于 TParameter 下，却将变量名描述为 exchange 的简称，可能沿用了交换字段说明；不能据此认定它仅能引用交换。

译文忠实保留“交换”措辞，请对照参数变量名字段及公式语言规范确认此处是否应为 parameter。

### 15. 待专家复核 · TImpactIndicatorResult 1820

相关正文：[影响指标结果](impact-indicators.md#read-timpactindicatorresult)

原文写“对影响类别所属方法的引用”，但 EcoSpold02FlowData.xsd 约第 1039–1048 行明确本字段为 impactCategoryId、类型 TUuid、referenceToComplexType=TImpactMethodCategory，区别于字段 1810 的 impactMethodId（TImpactMethod）。译文忠实保留原文方法措辞，源文说明与引用对象存在矛盾。

请确认应将官方说明修正为对影响类别的引用；实现时以 impactCategoryId 与 TImpactMethodCategory 的模式定义为依据。

### 16. 待专家复核 · TParameter 1715

相关正文：[参数](parameters.md#read-tparameter)

文档要求变量名以字母（a-z）开头，并描述字母、数字、下划线字符规则；EcoSpold02DataTypes.xsd 的 TVariableName 仅声明 maxLength=40 与 pattern=\w\S*（约第 858–862 行），该模式未直接表达与文字说明完全等价的规则。可能另有语义验证或公式解析约束。

保留原文变量规则；请核对公式解析及语义验证规范，不应将 XSD 验证通过等同于满足全部变量名规则。

### 17. 待专家复核 · TIntermediateExchange 1534

相关正文：[中间交换专用字段](intermediate-exchanges.md#read-tintermediateexchange)

此说明隶属于 @productionVolumeMathematicalRelation，但原文称公式结果写入 amount，可能为通用说明复制残留。官方 EcoSpold02FlowData.xsd 包含同样说明，同时将产量数值字段定义为 productionVolumeAmount；普通交换数值字段为 amount。仅凭XSD说明无法确认软件实际求值目标。译文保留原文 amount。

核对产量公式的实际求值实现，确认目标是否应为 productionVolumeAmount，并由技术编辑同步修正文档；不要据此把产量公式值写入普通交换 amount。

### 18. 待专家复核 · TIntermediateExchange 1520

相关正文：[中间交换专用字段](intermediate-exchanges.md#read-tintermediateexchange)

原表1520选项提示引用另一活动数据集字段105，该字段是activityNameId；官方XSD又将activityLinkId声明为TActivityIndexEntry引用，提示与结构引用对象需核对。叙述按已明确的供应活动链接含义解释，并保留原编号提示，不把不同标识混用。

按实际活动索引解析供应活动，向技术编辑核对该跨表字段编号；不使用交换实例或产品标识替代activityLinkId。

### 19. 待专家复核 · TUncertainty 2100

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原文将 σ 称为 variance（方差），而常见对数正态分布记号以 σ 为底层正态分布标准差、σ²为方差；同组字段则明确为 variance。译文忠实保留原符号及“方差”，不能据此自动将参数平方或开方。

以对应 XSD 字段定义及读取软件实际实现确认 Mu/Variance 参数的尺度；请技术编辑澄清原文 σ 的定义。

### 20. 待专家复核 · TUncertainty 2120

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原文要求从 mostLikelyValue 计算 meanValue，同时禁止在 ecoinvent 上下文使用 mostLikelyValue（#3797）。官方 EcoSpold02DataTypes.xsd 的 triangular 类型却将当前 @mostLikelyValue（fieldId=2122）设为 required；#3797 与当前编号不同，禁令适用对象及与模式必填要求的关系尚不清楚。三角分布均值也不能仅由众数单独确定。正文保留 shall/must not 及 #3797，不擅自撤销禁令。

请向数据方确认 #3797 是否仅指旧格式字段、当前 @mostLikelyValue 的提交规则及 meanValue 的具体含义；勿将众数直接当作三角分布均值。证据：Schemas/datasets/EcoSpold02DataTypes.xsd 的 triangular 定义。

### 21. 待专家复核 · TUncertainty 2140

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原文允许退化条件 a=b，但所列 Shape1 公式含分母 b-a，此条件下会出现除零；原文未说明退化分布如何处理。译文完整保留条件和公式。

核实实现是否对 a=b 单独生成常数样本，或是否应要求 a<b；确认前不要直接按常规形状公式计算该边界情况。

### 22. 待专家复核 · TUncertainty 2173

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原文仅将旧格式 standardDeviation95 描述为从均值两侧扩展、覆盖总体95%所需的值，未说明它是加性半宽度、乘性因子或其他量，不能一概理解成普通标准差。译文不额外指定计算形式。

读取 EcoSpold01 遗留数据时核对具体旧分布及字段约定，勿无条件将该值作为算术标准差。

### 23. 待专家复核 · TUncertainty 2110

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原文将正态分布参数称为 MeanValue 和 Deviation，但官方 XSD 中当前 normal 类型的属性为 meanValue、variance 和 varianceWithPedigreeUncertainty，没有 Deviation。原文的标准差概念说明不等同于当前字段的方差存储约定。

正文保留原文参数名称；实现时对照 fieldId=2111/2112/2113 的 XSD 定义，不将标准差直接写入 variance 字段。请数据方澄清旧参数名称与当前属性的关系。

### 24. 待专家复核 · TTextAndImage intro

相关正文：[文本与图像](text-and-image.md#read-ttextandimage)

源文开头将图像元素称为 imageUri，后文却称为 imageUrl；相同 imageUri 表述也出现于 TTechnology.510 和 TReview.3340 的复用说明。独立核查官方 Schemas/datasets/EcoSpold02DataTypes.xsd 的 TTextAndImage 定义，实际子元素为 text、imageUrl、variable，而没有 imageUri。译文忠实保留原文两种名称，文档说明与XSD元素定义存在冲突。

生成或解析XML时以该XSD中的 imageUrl 为准；原英文说明的 imageUri 应由技术编辑确认统一。译文原有名称不静默替换。

### 25. 待专家复核 · TUncertainty 2270

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

主 HTML 把 pedigreeMatrix 行类型写为 integer，但实际 EcoSpold02DataTypes.xsd 定义的是含五个整数评分属性的匿名复合类型。教程按 XSD 说明容器结构，原始译表应保留原表并提示差异。

请由技术编辑修正原表的类型标记，读取实现按 XSD 属性结构处理。

### 26. 待专家复核 · TUncertainty 2273

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原评分 4 为不足 15 年，评分 5 为超过 15 年，未明确恰好 15 年的分类。教程保留边界并明示缺口，没有自行推断为大于等于。

请依据数据质量指南或官方实现确认恰好 15 年时使用哪个评分。

### 27. 待专家复核 · TRepresentativeness 3030

相关正文：[代表性](representativeness.md#read-trepresentativeness)

samplingProcedure 的说明混入 TTextAndImage 模板，但 EcoSpold02MetaInformation.xsd 实际将该元素定义为 TString32000，不能包含 text/imageUrl/variable 子元素。教程保留其业务含义，并明确区分文字模板与实际字段类型。

请技术编辑移除错误的文本图像模板；实现以 TString32000 的 simpleContent 为准。

### 28. 待专家复核 · TProperty 2350

相关正文：[属性](properties.md#read-tproperty)

文字变量规则与 TVariableName 的 maxLength=40、pattern=\w\S* 并非直接等价；教程分别陈述文档规则与 XSD 约束，不从模式单独推断全部公式语言规则。

核对语义验证及公式解析规范以确认实际变量名规则。

### 29. 待专家复核 · TUncertainty 2150

相关正文：[不确定性](uncertainty.md#read-tuncertainty)

原文及官方 EcoSpold02DataTypes.xsd 注释均说“Absolute values of the values entered here will be used”，继而说将最小值参数加到所有样本。前句未明确绝对值处理是否只适用于 shape/scale，或也涵盖 minValue；模式仅声明三个浮点属性，不提供抽样实现。教程已移除将范围限定到形状、尺度参数的推断。

请数据方或抽样软件实现确认绝对值处理的参数范围及 minValue 的符号约定；确认前保留原句范围，不替源文规定负位置参数的处理。
