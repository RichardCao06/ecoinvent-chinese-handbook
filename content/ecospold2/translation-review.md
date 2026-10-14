# ecoSpold2 字段翻译与审校记录

完整翻译 **22 个分组、243 条字段、388 个源文块**。三位 AI 译者分组翻译，再由另一位 AI 独立交叉审校。字段元数据原样导出并与原 HTML 对照；每条同时关联同包 XSD 的 FieldID、字段名和所属类型。

格式包 v1.0.13 / XSD version 2.0.13。保留原件、SHA-256、逐块中文与英文、审阅记录；本记录不代表人工专家签核或 ecoinvent 官方认证。

本部分共有 **27 条审校注记**，其中 **12 条待专家复核**。与原支持文档的 170 条记录分开计数，避免混淆两次翻译范围。

## 注记清单

### 1. 已处理／已说明 · `TActivity.110.description.0`

相关章节：[活动](activity.md)

**原文：** Indicates the kind of data (1 = Unit process; 2 = System terminated) that is represented by this dataset. Data are always entered by the data providers as Unit process. The database-generated, attributional and consequential datasets are available both at the unit process level and as aggregated (terminated) system dataset (i.e. the life cycle inventory results) containing the aggregated elementary exchanges and impacts of the product system related to one specific product from the unit process. The terminated product systems include all upstream activity datasets, as linked by the intermediate exchanges, and therefore do not themselves have any intermediate exchanges, only environmental exchanges and accumulated impact assessment results.

**译文：** 表示本数据集所包含的数据种类（1 = 单元过程；2 = 已汇总的完整产品系统（System terminated））。数据提供方始终以单元过程形式录入数据。数据库生成的归因型和后果型数据集，既可按单元过程层级提供，也可作为汇总的完整系统数据集（即生命周期清单结果）提供；后者包含与该单元过程某一特定产品相关的产品系统中汇总的基本流交换和影响。完整产品系统包括通过中间交换链接的全部上游活动数据集，因此其自身不再包含任何中间交换，而仅包含环境交换和累积的影响评价结果。

**说明：** System terminated 在此指已沿中间交换纳入全部上游活动并汇总的产品系统，不是停运或生命周期终结的系统。

**处理建议：** 译为“已汇总的完整产品系统”，并在枚举中保留 System terminated 对照；全文保留仅有环境交换及累积影响结果的限定。

### 2. 已处理／已说明 · `TActivity.130.description.1`

相关章节：[活动](activity.md)

**原文：** Child activity is derived (inherited) from its parent activity and only the content changes in comparison to its parent are stored in the child process. Child activity datasets cannot be validated using the EcoSpold02 schema, since most of the required fields will not be filled. Please refer to the additional documentation regarding inheritance of datasets in the ecoinvent database for further details.

**译文：** 子活动由其父活动派生（继承）而来，子过程中仅存储相对于父活动发生变化的内容。子活动数据集不能使用 EcoSpold02 模式进行验证，因为其大多数必填字段不会填写。更多细节请参阅有关 ecoinvent 数据库数据集继承的补充文档。

**说明：** 原文限制是子活动数据集不能用 EcoSpold02 模式验证，不是数据集不能被任何方式验证；子过程仅存储相对父过程变化的内容。

**处理建议：** 译文明确保留模式名称、验证限制及仅存储差异的范围，不推断继承展开后的验证行为。

### 3. 待专家复核 · `TActivity.135.description.0`

相关章节：[活动](activity.md)

**原文：** The inheritance depth expresses the maximum number of parent datasets for the current dataset. The following values are used in the ecoinvent context: 0 = not a child, 1 = a geography child, 2 = a temporal child, 3 = a macro-economic scenario child.

**译文：** 继承深度表示当前数据集可具有的父数据集最大数量。ecoinvent 上下文采用以下值：0 = 不是子数据集；1 = 地理子数据集；2 = 时间子数据集；3 = 宏观经济情景子数据集。

**说明：** 原文先把 inheritance depth 定义为父数据集最大数量，随后又以地理、时间和宏观经济情景子数据集类型说明 1、2、3，层数与类型之间的对应关系需核对继承规范。

**处理建议：** 保持原文定义和全部枚举编号，请依据继承专门文档确认各层级的允许嵌套关系。

### 4. 待专家复核 · `TParameter.1715.description.0`

相关章节：[参数](parameters.md)

**原文：** The variable name is a short name for the exchange, used when refering to the exchange amount in mathematical relations (formulas). Variables may contain characters, numbers and underscores (\_). Variable names must start with a character (a-z). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**译文：** 变量名是交换的简短名称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（\_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific\_Value 与 Calorific\_value 相同）。

**说明：** 该说明位于 TParameter 下，却将变量名描述为 exchange 的简称，可能沿用了交换字段说明；不能据此认定它仅能引用交换。

**处理建议：** 译文忠实保留“交换”措辞，请对照参数变量名字段及公式语言规范确认此处是否应为 parameter。

### 5. 待专家复核 · `TImpactIndicatorResult.1820.description.0`

相关章节：[影响指标结果](impact-indicators.md)

**原文：** Reference to the method of the impact category.

**译文：** 对影响类别所属方法的引用。

**说明：** 原文写“对影响类别所属方法的引用”，但 EcoSpold02FlowData.xsd 约第 1039–1048 行明确本字段为 impactCategoryId、类型 TUuid、referenceToComplexType=TImpactMethodCategory，区别于字段 1810 的 impactMethodId（TImpactMethod）。译文忠实保留原文方法措辞，源文说明与引用对象存在矛盾。

**处理建议：** 请确认应将官方说明修正为对影响类别的引用；实现时以 impactCategoryId 与 TImpactMethodCategory 的模式定义为依据。

### 6. 已处理／已说明 · `TActivity.180.options`

相关章节：[活动](activity.md)

**原文：** 0 = Undefined (default); 1 = Net values; 2 = Gross values

**译文：** 0 = 未指定（Undefined，默认）；1 = 低位热值（Net values）；2 = 高位热值（Gross values）

**说明：** 原译枚举“净值/总值”容易被理解为一般净总数值；同字段说明明确 Net/Gross 指低位/高位热值。已改为具体热值名称，保留 0、1、2 及默认值对应关系，并补充原英文标签。

**处理建议：** 采用修正后的热值枚举中文说明。

### 7. 待专家复核 · `TActivity.120.description.0`

相关章节：[活动](activity.md)

**原文：** Text and image field for general information about the dataset. Only comments and references of more general nature that cannot be placed in any of the more specific comment fields, should be placed here. In general, the information in the dataset should be sufficient to judge the appropriateness of a dataset for a specific application.Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

**译文：** 用于提供数据集一般信息的文本和图像字段。这里只应填写性质较为一般、无法放入其他更具体说明字段的说明和引用。总体上，数据集中的信息应足以判断其是否适合某项特定应用。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

**说明：** 本块及 TActivity.120.description.1、TActivity.195.description.0/.1、TTimePeriod.630.description.0/.1 的复用说明使用 imageUri，但 EcoSpold02DataTypes.xsd 的 TTextAndImage 实际元素名为 imageUrl（约第 940 行）。译文忠实保留 imageUri，未静默改变原文 XML 名。

**处理建议：** 请依据 TTextAndImage 的实际 XSD 元素定义统一官方说明中的 imageUri/imageUrl 命名。

### 8. 待专家复核 · `TParameter.1715.description.0`

相关章节：[参数](parameters.md)

**原文：** The variable name is a short name for the exchange, used when refering to the exchange amount in mathematical relations (formulas). Variables may contain characters, numbers and underscores (\_). Variable names must start with a character (a-z). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**译文：** 变量名是交换的简短名称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（\_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific\_Value 与 Calorific\_value 相同）。

**说明：** 文档要求变量名以字母（a-z）开头，并描述字母、数字、下划线字符规则；EcoSpold02DataTypes.xsd 的 TVariableName 仅声明 maxLength=40 与 pattern=\w\S*（约第 858–862 行），该模式未直接表达与文字说明完全等价的规则。可能另有语义验证或公式解析约束。

**处理建议：** 保留原文变量规则；请核对公式解析及语义验证规范，不应将 XSD 验证通过等同于满足全部变量名规则。

### 9. 待专家复核 · `TUncertainty.2100.description.0`

相关章节：[不确定性与分布参数](uncertainty.md)

**原文：** The Lognormal-distribution with average value μ (Mu parameter) and variance σ (Variance parameter) is a Normal-distribution, shaping the natural logarithm of the characteristic values ln(x) instead of x-values.

**译文：** 具有平均值 μ（Mu 参数）和方差 σ（Variance 参数）的对数正态分布，是对特征值的自然对数 ln(x) 而非 x 值进行描述的正态分布。

**说明：** 原文将 σ 称为 variance（方差），而常见对数正态分布记号以 σ 为底层正态分布标准差、σ²为方差；同组字段则明确为 variance。译文忠实保留原符号及“方差”，不能据此自动将参数平方或开方。

**处理建议：** 以对应 XSD 字段定义及读取软件实际实现确认 Mu/Variance 参数的尺度；请技术编辑澄清原文 σ 的定义。

### 10. 待专家复核 · `TUncertainty.2120.description.1`

相关章节：[不确定性与分布参数](uncertainty.md)

**原文：** In case of triangular uncertainty distribution, the meanValue shall be calculated from the mostLikelyValue. The field mostLikelyValue (#3797) must not be used in the ecoinvent context.

**译文：** 采用三角不确定性分布时，应根据 mostLikelyValue 计算 meanValue。在 ecoinvent 上下文中，不得使用 mostLikelyValue 字段（#3797）。

**说明：** 原文要求从 mostLikelyValue 计算 meanValue，同时禁止在 ecoinvent 上下文使用 mostLikelyValue（#3797）。官方 EcoSpold02DataTypes.xsd 的 triangular 类型却将当前 @mostLikelyValue（fieldId=2122）设为 required；#3797 与当前编号不同，禁令适用对象及与模式必填要求的关系尚不清楚。三角分布均值也不能仅由众数单独确定。正文保留 shall/must not 及 #3797，不擅自撤销禁令。

**处理建议：** 请向数据方确认 #3797 是否仅指旧格式字段、当前 @mostLikelyValue 的提交规则及 meanValue 的具体含义；勿将众数直接当作三角分布均值。证据：Schemas/datasets/EcoSpold02DataTypes.xsd 的 triangular 定义。

### 11. 待专家复核 · `TUncertainty.2140.description.0`

相关章节：[不确定性与分布参数](uncertainty.md)

**原文：** Beta distribution using minValue (a), maxValue (b) and mostFrequentValue (m) parameters to calculate the two shape parameters of the underlying Gamma distributions. The parameters must follow this condition: ((a &lt;= m) and (m &lt;= b)) or (a = b). The shape values will be calculated by these formulas: Shape1 = 1 + 4 \* ((m-a) / (b-a)). Shape2 = 6 - Shape1.

**译文：** Beta 分布使用 minValue（a）、maxValue（b）和 mostFrequentValue（m）参数，计算底层 Gamma 分布的两个形状参数。参数必须满足条件：((a &lt;= m) and (m &lt;= b)) or (a = b)。形状参数按以下公式计算：Shape1 = 1 + 4 \* ((m-a) / (b-a))。Shape2 = 6 - Shape1。

**说明：** 原文允许退化条件 a=b，但所列 Shape1 公式含分母 b-a，此条件下会出现除零；原文未说明退化分布如何处理。译文完整保留条件和公式。

**处理建议：** 核实实现是否对 a=b 单独生成常数样本，或是否应要求 a<b；确认前不要直接按常规形状公式计算该边界情况。

### 12. 待专家复核 · `TUncertainty.2173.description.0`

相关章节：[不确定性与分布参数](uncertainty.md)

**原文：** The value, extended from both sides of the mean, that would be necessary to cover 95% of the population

**译文：** 从均值向两侧延伸、为覆盖总体 95% 所需的值。

**说明：** 原文仅将旧格式 standardDeviation95 描述为从均值两侧扩展、覆盖总体95%所需的值，未说明它是加性半宽度、乘性因子或其他量，不能一概理解成普通标准差。译文不额外指定计算形式。

**处理建议：** 读取 EcoSpold01 遗留数据时核对具体旧分布及字段约定，勿无条件将该值作为算术标准差。

### 13. 已处理／已说明 · `TDataGeneratorAndPublication.3560.options`

相关章节：[数据生成者与发布](publication.md)

**原文：** If 759=3

**译文：** 如果 759=3。

**说明：** 已对照官方 XSD 确认，这些编号是旧 SpoldID 引用：accessRestrictedTo 的 spoldID=759、fieldId=3550；publishedSourceId 的 spoldID=757、fieldId=3520；TValidSource/@id 的 spoldID=801、fieldId=3110。原文条件与编号映射一致。

**处理建议：** 保留原文 759=3、757 和 801；在按新版 fieldId 查找时使用上述对应关系。证据：Schemas/datasets/EcoSpold02MetaInformation.xsd 及 Schemas/MasterData/EcoSpold02Sources.xsd。

### 14. 已处理／已说明 · `TDataGeneratorAndPublication.3522.description.0`

相关章节：[数据生成者与发布](publication.md)

**原文：** If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**译文：** 如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。

**说明：** 已明确翻译子数据集删除引用与未提供引用的继承语义：必须将xxxOverwrittenByChild设为true，否则仍解释为保留父数据集值；不将删除引用误译为自动覆盖。

**处理建议：** 该规则同样适用于3563字段，译文已保持一致。

### 15. 已处理／已说明 · `TElementaryExchange.1660.description.0`

相关章节：[基本流交换专用字段](elementary-exchanges.md)

**原文：** Name of the compartment and subcompartment of the exchange. The xml document referenced by validCompartments contains definitions of valid compartment/subcompartment pairs for a given language.

**译文：** 交换的区室及子区室名称。validCompartments 所引用的 XML 文档包含给定语言下有效的区室／子区室配对的定义。

**说明：** 将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。

**处理建议：** 已修正术语，保留全部 XML 标识与引用编号。

### 16. 已处理／已说明 · `TCompartment.intro.0`

相关章节：[区室与子区室](compartments.md)

**原文：** Contains compartment pairs to specify an exchange.

**译文：** 包含用于指定交换的区室配对。

**说明：** 将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。

**处理建议：** 已修正术语，保留全部 XML 标识与引用编号。

### 17. 已处理／已说明 · `TCompartment.330.description.0`

相关章节：[区室与子区室](compartments.md)

**原文：** The name of the compartment.This is the plaintext value of the referenced compartment (field 5315).

**译文：** 区室名称。这是所引用区室（字段 5315）的纯文本值。

**说明：** 将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。

**处理建议：** 已修正术语，保留全部 XML 标识与引用编号。

### 18. 已处理／已说明 · `TCompartment.340.description.0`

相关章节：[区室与子区室](compartments.md)

**原文：** The name of the subcompartment.This is the plaintext value of the referenced subcompartment (field 5325).

**译文：** 子区室名称。这是所引用子区室（字段 5325）的纯文本值。

**说明：** 将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。

**处理建议：** 已修正术语，保留全部 XML 标识与引用编号。

### 19. 已处理／已说明 · `TCompartment.350.description.0`

相关章节：[区室与子区室](compartments.md)

**原文：** Reference to the compartment/subcompartment pair. Must be defined in list of valid compartments (see field 5330).

**译文：** 引用区室／子区室配对。该配对必须在有效区室列表中定义（见字段 5330）。

**说明：** 将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。

**处理建议：** 已修正术语，保留全部 XML 标识与引用编号。

### 20. 已处理／已说明 · `TCompartment.351.description.0`

相关章节：[区室与子区室](compartments.md)

**原文：** Reference to the context of the subcompartment

**译文：** 引用该子区室所属的上下文。

**说明：** 将 compartment/subcompartment 统一为站内数据结构用语“区室／子区室”；这些分类不仅表示空气、水、土壤等环境介质，还可包含自然资源区室。

**处理建议：** 已修正术语，保留全部 XML 标识与引用编号。

### 21. 待专家复核 · `TUncertainty.2110.description.0`

相关章节：[不确定性与分布参数](uncertainty.md)

**原文：** Normal (also known as "Gaussian") distribution. It is a family of distributions of the same general form, differing in their location and scale parameters: the mean ("MeanValue") and standard deviation ("Deviation"), respectively.

**译文：** 正态分布，也称“高斯”分布。它是一族具有相同一般形式的分布，其位置参数和尺度参数不同，分别为均值（MeanValue）和标准差（Deviation）。

**说明：** 原文将正态分布参数称为 MeanValue 和 Deviation，但官方 XSD 中当前 normal 类型的属性为 meanValue、variance 和 varianceWithPedigreeUncertainty，没有 Deviation。原文的标准差概念说明不等同于当前字段的方差存储约定。

**处理建议：** 正文保留原文参数名称；实现时对照 fieldId=2111/2112/2113 的 XSD 定义，不将标准差直接写入 variance 字段。请数据方澄清旧参数名称与当前属性的关系。

### 22. 待专家复核 · `TTextAndImage.intro.0`

相关章节：[文本、图像与文本变量](text-and-image.md)

**原文：** List of text, imageUri and variable elements. These can be combined in any order. Their desired order in the result must be given by the index attributes of the text and imageUrl elements.

**译文：** text、imageUri 和 variable 元素的列表。这些元素可按任意顺序组合。必须通过 text 和 imageUrl 元素的 index 属性指定它们在结果中的所需顺序。

**说明：** 源文开头将图像元素称为 imageUri，后文却称为 imageUrl；相同 imageUri 表述也出现于 TTechnology.510 和 TReview.3340 的复用说明。独立核查官方 Schemas/datasets/EcoSpold02DataTypes.xsd 的 TTextAndImage 定义，实际子元素为 text、imageUrl、variable，而没有 imageUri。译文忠实保留原文两种名称，文档说明与XSD元素定义存在冲突。

**处理建议：** 生成或解析XML时以该XSD中的 imageUrl 为准；原英文说明的 imageUri 应由技术编辑确认统一。译文原有名称不静默替换。

### 23. 待专家复核 · `TIntermediateExchange.1534.description.1`

相关章节：[中间交换专用字段](intermediate-exchanges.md)

**原文：** The result of the formula with a specific set of variable values is written into the amount field.

**译文：** 将公式在一组特定变量值下的计算结果写入 amount 字段。

**说明：** 此说明隶属于 @productionVolumeMathematicalRelation，但原文称公式结果写入 amount，可能为通用说明复制残留。官方 EcoSpold02FlowData.xsd 包含同样说明，同时将产量数值字段定义为 productionVolumeAmount；普通交换数值字段为 amount。仅凭XSD说明无法确认软件实际求值目标。译文保留原文 amount。

**处理建议：** 核对产量公式的实际求值实现，确认目标是否应为 productionVolumeAmount，并由技术编辑同步修正文档；不要据此把产量公式值写入普通交换 amount。

### 24. 已处理／已说明 · `TIntermediateExchange.1530.description.0`

相关章节：[中间交换专用字段](intermediate-exchanges.md)

**原文：** The product volume expressed per year in the same unit as the exchange.

**译文：** 按年表示的产品产量，单位与该交换相同。

**说明：** 将 production volume 的“生产量”统一为指南规定的“产量”，保留按年计量、单位与公式引用等全部原条件。

**处理建议：** 已修正为产量。

### 25. 已处理／已说明 · `TIntermediateExchange.1532.description.0`

相关章节：[中间交换专用字段](intermediate-exchanges.md)

**原文：** The variable name is a short name for the production volume of the exchange, used when refering to the production volume amount in mathematical relations (formulas). Variables may contain characters, numbers and underscores (\_). Variable names must start with a character (a-z). Variable names are not case sensitive (calorific\_Value equals Calorific\_value).

**译文：** 变量名是交换产量的简称，用于在数学关系（公式）中引用产量数值。变量可包含字母、数字和下划线（\_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific\_Value 与 Calorific\_value 等同）。

**说明：** 将 production volume 的“生产量”统一为指南规定的“产量”，保留按年计量、单位与公式引用等全部原条件。

**处理建议：** 已修正为产量。

### 26. 已处理／已说明 · `TIntermediateExchange.1535.description.0`

相关章节：[中间交换专用字段](intermediate-exchanges.md)

**原文：** A general comment can be made on the data source, assumptions and calculations for the production volume data.

**译文：** 可对产量数据的数据来源、假设和计算添加一般注释。

**说明：** 将 production volume 的“生产量”统一为指南规定的“产量”，保留按年计量、单位与公式引用等全部原条件。

**处理建议：** 已修正为产量。

### 27. 已处理／已说明 · `TCustomExchange.1200.description.0`

相关章节：[交换的通用字段](exchanges.md)

**原文：** Transfer coefficients relate specific inputs to specific outputs and record the share of this specific input that contributes to this specific output.

**译文：** 转移系数将特定输入与特定输出关联，并记录该特定输入中流向该特定输出的份额。

**说明：** 原译文“输入对输出的贡献份额”可能被理解为输入占输出的比例。原文明确是该输入中分配到特定输出的份额，且 TTransferCoefficient.2410 要求将系数乘以被引用交换量。

**处理建议：** 已明确为“该特定输入中流向该特定输出的份额”，避免比例分母及流向歧义。
