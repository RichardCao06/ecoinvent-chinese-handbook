# 附录：官方 EcoSpold02.html 中文版本

下面保留原表的十列结构、字段次序、FieldID、旧 SpoldID、取值选项和逐行说明，只把自然语言翻译为中文。这里的必填与重复标记来自原表，不擅自用编者理解改写；实现解析器时，还须结合正文所述父元素、分支和 XSD 约束。

可以[下载独立的中文 HTML 译表](attachments/EcoSpold02.zh.html)，或查看[官方英文 HTML 原件](original/Format%20description/EcoSpold02.html)。原件及完整模式保存在[官方格式包](original/documentation_on_ecospold2_format.v1.0.13.zip)中。附录便于逐项核对，各章正文负责解释读法、使用场景和取数步骤。

本文档提供 EcoSpold02 模式的简化视图。开发者还应查阅模式文件，以确保正确实现该格式。

为区分 Xml 属性与元素，属性名称以“@”为前缀。

“SpoldID, version 1”列中编号后添加的标记，用于表示相对于 EcoSpold01 的变化。

“SpoldID, version 1”列用于帮助查找 EcoSpold01 字段。讨论该格式时，请使用新的“fieldId”列。

以下第 1 版 SpoldId 已在 EcoSpold02 格式中移除：

205	languageCode, 206	localLanguageCode, 208	impactAssessmentResult 400	datasetRelatesToProduct, 403	unit, 404	amount 490	localName, 493	infrastructureProcess, 494	infrastructureIncluded, 495	category, 496	subCategory, 497	localCategory, 498	localSubCategory, 499	formula 502	CASNumber 727	uncertaintyAdjustments, 761	countryCode 2401	referenceToCoProduct, 2403	allocationMethod, 2404	fraction, 2492	referenceToInputOutput 3506	category, 3507	subCategory, 3508	infrastructureProcess, 3509	localCategory, 3510	localSubCategory 3703	location, 3709	standardDeviation95, 3711	formula, 3794	localName, 3795	minValue, 3796	maxValue, 3797	mostLikelyValue 5807	companyCode, 5808	countryCode

<h3><a href="#appendix-tactivity" id="appendix-tactivity"></a>活动（TActivity）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含活动数据集的标识信息，包括名称和分类。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="100"><td>activityName</td><td>100</td><td>401-rename</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TActivity.100.description.0"><td></td><td colspan="9">本数据集所表示活动的名称。</td></tr>
<tr data-field-id="102"><td>@id</td><td>102</td><td>200-type</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.102.description.0"><td></td><td colspan="9">该活动的唯一标识符。UUID 数据类型是包含十六进制字符的 36 个字符长字符串，可确保标识符在全球范围内唯一。新条目的 UUID 必须由外部软件提供。网上有多种 UUID 生成器，大多数编程语言中也有相应实现。</td></tr>
<tr data-field-id="105"><td>@activityNameId</td><td>105</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.105.description.0"><td></td><td colspan="9">对该活动的活动名称主数据条目的引用。</td></tr>
<tr data-field-id="106"><td>@activityNameContextId</td><td>106</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.106.description.0"><td></td><td colspan="9">对活动名称所属上下文的引用。</td></tr>
<tr data-source-block="TActivity.106.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="110"><td>@type</td><td>110</td><td>201-type</td><td>1 = 单元过程；2 = 已汇总的完整产品系统（System terminated）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.110.description.0"><td></td><td colspan="9">表示本数据集所包含的数据种类（1 = 单元过程；2 = 已汇总的完整产品系统（System terminated））。数据提供方始终以单元过程形式录入数据。数据库生成的归因型和后果型数据集，既可按单元过程层级提供，也可作为汇总的完整系统数据集（即生命周期清单结果）提供；后者包含与该单元过程某一特定产品相关的产品系统中汇总的基本流交换和影响。完整产品系统包括通过中间交换链接的全部上游活动数据集，因此其自身不再包含任何中间交换，而仅包含环境交换和累积的影响评价结果。</td></tr>
<tr data-field-id="115"><td>@specialActivityType</td><td>115</td><td>new</td><td>0 = 普通转化活动（默认）；1 = 市场活动；10 = 市场组；2 = 投入产出活动（IO activity）；3 = 残余活动；4 = 生产组合；5 = 进口活动；6 = 供应组合；7 = 出口活动；8 = 再出口活动；9 = 修正活动</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.115.description.0"><td></td><td colspan="9">特殊活动类型如下：
0 = “普通”转化活动。转化活动是将输入转化为不同输出的人类活动，例如硬煤矿将地下硬煤转化为可销售产品硬煤。此处采用最广义的转化活动概念，包括开采、生产、运输、消费和废物处理活动，即任何中间输出不同于中间输入的人类活动。引入“转化活动”这一概念，仅用于在后续活动建模和链接中，将这些“普通”活动与市场活动、生产及供应组合、进出口活动和修正数据集区分开。
1 = 市场活动。市场活动不转化输入，而仅将某转化活动的中间输出传递给以该中间输出作为输入的消费转化活动，例如将供应商处的硬煤传递至消费者处的硬煤。市场活动通常混合不同转化活动的类似中间输出，因此提供这些中间输出的消费组合。
10 = 市场组。市场组与市场之间的关系，类似于市场与转化活动之间的关系。在未指定系统模型中，市场组仅包含参考产品。链接算法将位于市场组地理范围内、且具有相同参考产品的供应市场添加为输入。
2 = 投入产出活动（IO activity）。IO 活动表示来自国家供给使用表的活动数据集，通常对应某一特定行业的供给和使用。
3 = 残余活动。在同一年及同一地理区域内，从某活动类别的供给使用数据（IO 活动）中减去该类别所有可用单元过程后，所得的活动即为残余活动。
4 = 生产组合。生产组合表示某地理区域内特定产品供应者按生产量加权的平均情况。
5 = 进口活动。进口活动表示某特定产品进入某特定地理区域的进口，仅用于国家层面的平衡核算，不参与任何自动生成的消费组合。进入行政约束市场的进口，以及来自部分孤立市场的进口，按普通转化活动建模，以便纳入相关市场活动（消费组合）。
6 = 供应组合。供应组合是在生产组合中加入某特定产品进入某特定地理区域的进口。
7 = 出口活动。出口活动表示国家生产组合的出口量，以该国范围为其地理位置，不参与任何自动生成的消费组合。为正确计算出口的价值，将市场活动所包含的相同活动和数据直接加入出口活动，包括运输活动、生产损失、批发商和零售商活动，以及产品税和补贴。
8 = 再出口活动。再出口活动表示某地理区域的再出口量，不参与任何自动生成的消费组合。
9 = 修正活动。修正活动是向产品系统添加两次的活动，一次带正流、一次带负流，以便将一个或多个交换从系统的一部分转移至另一部分，例如修正上游活动的下游效应，或修正分配造成的质量平衡偏差。更多说明见 ecoinvent《数据质量指南》中的“产品质量差异导致的下游变化”（Downstream changes caused by differences in product quality）和“分配修正”（Allocation corrections）章节。</td></tr>
<tr data-field-id="120"><td>generalComment</td><td>120</td><td>492</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.120.description.0"><td></td><td colspan="9">用于提供数据集一般信息的文本和图像字段。这里只应填写性质较为一般、无法放入其他更具体说明字段的说明和引用。总体上，数据集中的信息应足以判断其是否适合某项特定应用。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TActivity.120.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-field-id="130"><td>@parentActivityId</td><td>130</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.130.description.0"><td></td><td colspan="9">parentActivityId 是指向父活动数据集的 UUID。此字段填入 UUID 时，父活动数据集的全部字段内容均由子活动数据集承接；子活动数据集即通过 UUID 调用父数据集的活动。</td></tr>
<tr data-source-block="TActivity.130.description.1"><td></td><td colspan="9">子活动由其父活动派生（继承）而来，子过程中仅存储相对于父活动发生变化的内容。子活动数据集不能使用 EcoSpold02 模式进行验证，因为其大多数必填字段不会填写。更多细节请参阅有关 ecoinvent 数据库数据集继承的补充文档。</td></tr>
<tr data-source-block="TActivity.130.description.2"><td></td><td colspan="9">子活动数据集（&quot;http://www.EcoInvent.org/EcoSpold02Child&quot;）中的字段有 5 种填写方式：</td></tr>
<tr data-source-block="TActivity.130.description.3"><td></td><td colspan="9">1）将字段留空：此时采用父活动数据集中的值。</td></tr>
<tr data-source-block="TActivity.130.description.4"><td></td><td colspan="9">2）填入内容：此时采用填入的值，忽略父活动数据集中的值。</td></tr>
<tr data-source-block="TActivity.130.description.5"><td></td><td colspan="9">3）在字符串字段中填入包含 {{PARENTTEXT}} 的文本：此时，父活动数据集中的字段内容会插入子数据集所填文本的该位置。</td></tr>
<tr data-source-block="TActivity.130.description.6"><td></td><td colspan="9">4）在类型为 TTextAndImage 的字段中，同时支持 {{PARENTTEXT}} 和 {{text_variables}}；后者允许在父数据集中定义文本变量，并在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TActivity.130.description.7"><td></td><td colspan="9">5）对于具有对应数学关系字段的数量（amount）字段，在 mathematicalRelation 字段中填入包含保留变量 PARENTVALUE 的内容，例如公式 PARENTVALUE*0.5 会使原数量（amount）字段的值减半。</td></tr>
<tr data-field-id="131"><td>@parentActivityContextId</td><td>131</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.131.description.0"><td></td><td colspan="9">对父活动所属上下文的引用。</td></tr>
<tr data-source-block="TActivity.131.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="135"><td>@inheritanceDepth</td><td>135</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.135.description.0"><td></td><td colspan="9">继承深度表示当前数据集可具有的父数据集最大数量。ecoinvent 上下文采用以下值：0 = 不是子数据集；1 = 地理子数据集；2 = 时间子数据集；3 = 宏观经济情景子数据集。</td></tr>
<tr data-field-id="145"><td>includedActivitiesStart</td><td>145</td><td>402-type</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.145.description.0"><td></td><td colspan="9">描述活动的起点。对于“system terminated”（已汇总的完整产品系统），起点始终是“从摇篮开始，即包含全部上游活动”（From cradle, i.e. including all upstream activities）。对于单元过程，可根据输入的性质描述起点，例如“从接收［如原材料 X］开始……”或“以［如劳动力和能源］输入为起点的服务”。</td></tr>
<tr data-field-id="150"><td>includedActivitiesEnd</td><td>150</td><td>402-type</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.150.description.0"><td></td><td colspan="9">描述活动名称中未能不言自明的所包含活动，以及有意排除的活动或输入。例如，“application of pesticides”（农药施用）活动作为一项服务时排除农药本身，以便适用于多种有效成分。说明应以最后一个活动和／或交付点结束，例如“直至并包括将产品装载到货车上”。</td></tr>
<tr data-field-id="170"><td>synonym</td><td>170</td><td>491-type</td><td></td><td>TSynonym</td><td>80</td><td>是</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.170.description.0"><td></td><td colspan="9">名称的同义词列表。与一般多语言字符串不同，同义词可包含多个 xml:lang 属性值相同的元素。</td></tr>
<tr data-source-block="TActivity.170.description.1"><td></td><td colspan="9">允许 0..n 个条目，每个条目的最大长度为 80。</td></tr>
<tr data-field-id="175"><td>tag</td><td>175</td><td>new</td><td></td><td>TTag</td><td>40</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.175.description.0"><td></td><td colspan="9">tag 字段允许使用开放的关键词列表描述活动，可用于筛选、分组和搜索。validTags 文件引用提供预定义标签的列表；但若在 validTags 主文件中找不到某标签条目，语义验证程序应仅显示提示信息，而非错误。</td></tr>
<tr data-field-id="180"><td>@energyValues</td><td>180</td><td>203</td><td>0 = 未指定（Undefined，默认）；1 = 低位热值（Net values）；2 = 高位热值（Gross values）</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.180.description.0"><td></td><td colspan="9">表示数据集中采用能源数值的方式。代码为：0 = 未指定（默认）；1 = 净（低位）热值；2 = 总（高位）热值。</td></tr>
<tr data-source-block="TActivity.180.description.1"><td></td><td colspan="9">此数据字段默认设为 0。</td></tr>
<tr data-field-id="190"><td>@masterAllocationPropertyId</td><td>190</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.190.description.0"><td></td><td colspan="9">通过 UUID 引用本数据集所有交换的默认分配属性。可为每项交换覆盖该分配属性（见字段 1150：specificAllocationPropertyId）。</td></tr>
<tr data-source-block="TActivity.190.description.1"><td></td><td colspan="9">某特定输出的分配因子，等于该输出所声明的 TProperty 值乘以输出数量，再除以所有输出的相应 TProperty 值与输出数量乘积之和。</td></tr>
<tr data-field-id="191"><td>@masterAllocationPropertyContextId</td><td>191</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.191.description.0"><td></td><td colspan="9">对主分配属性所属上下文的引用。</td></tr>
<tr data-source-block="TActivity.191.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="192"><td>@masterAllocationPropertyIdOverwrittenByChild</td><td>192</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.192.description.0"><td></td><td colspan="9">若必须在子数据集中移除对某主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设为 true。否则，移除引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="195"><td>allocationComment</td><td>195</td><td>2407</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.195.description.0"><td></td><td colspan="9">用于进一步说明分配程序及所选分配属性的文本和图像字段。比较不同分配参数（如物理参数和经济参数）时，若分配因子恰好相同，也可在此报告。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TActivity.195.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-field-id="200"><td>@datasetIcon</td><td>200</td><td>new</td><td></td><td>anyURI</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.200.description.0"><td></td><td colspan="9">数据集图标的 URL。图标用于快速识别特定数据集，也可用于产品品牌和公司徽标。图标并非数据集的直接组成部分，而是存储于本地或 ecoinvent 网络服务器，可通过 Http 协议获取。</td></tr>
</tbody></table>
<h3><a href="#appendix-tclassification" id="appendix-tclassification"></a>分类（TClassification）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>包含用于指定活动分类的分类配对信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="300"><td>classificationSystem</td><td>300</td><td>501</td><td></td><td>TString255</td><td>255</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TClassification.300.description.0"><td></td><td colspan="9">所用分类体系的名称，例如 ISIC Rev. 4。这是所引用分类体系（字段 320）的可选纯文本值。</td></tr>
<tr data-field-id="310"><td>classificationValue</td><td>310</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TClassification.310.description.0"><td></td><td colspan="9">活动在所指定分类体系中所属的类别。这是所引用分类值（字段 320）的可选纯文本值。</td></tr>
<tr data-field-id="320"><td>@classificationId</td><td>320</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TClassification.320.description.0"><td></td><td colspan="9">对分类体系中某分类值的引用。该值必须在有效分类列表中定义（见字段 5160）。</td></tr>
<tr data-field-id="321"><td>@classificationContextId</td><td>321</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TClassification.321.description.0"><td></td><td colspan="9">对分类所属上下文的引用。</td></tr>
<tr data-source-block="TClassification.321.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
</tbody></table>
<h3><a href="#appendix-tgeography" id="appendix-tgeography"></a>地理区域（TGeography）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含过程地理适用范围的信息。地理区域可以是活动所在的点位置、描述移动活动的一条线，或分布式活动或生产组合覆盖的区域；该区域包含多个位于具体地点的活动。对于市场（消费组合），地理区域描述市场边界，跨越这些边界的进口和出口受到限制。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="400"><td>@geographyId</td><td>400</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TGeography.400.description.0"><td></td><td colspan="9">引用有效地点文件，该文件包含详细的地理区域信息。</td></tr>
<tr data-field-id="401"><td>@geographyContextId</td><td>401</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TGeography.401.description.0"><td></td><td colspan="9">引用该地理区域所属的上下文。</td></tr>
<tr data-source-block="TGeography.401.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="410"><td>shortname</td><td>410</td><td>662</td><td></td><td>TString40</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TGeography.410.description.0"><td></td><td colspan="9">geographyId 所引用地点的描述性简称，例如 EcoSpold 第 1 版的地区代码。</td></tr>
<tr data-field-id="420"><td>comment</td><td>420</td><td>663</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TGeography.420.description.0"><td></td><td colspan="9">用于进一步解释地理区域的文本和图像字段。尤其在描述区域时，可以说明地理边界划定的性质，特别是在该区域不是行政区的情况下。这里也可提供市场边界的划定依据。文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。</td></tr>
<tr data-source-block="TGeography.420.description.1"><td></td><td colspan="9">文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。</td></tr>
</tbody></table>
<h3><a href="#appendix-ttechnology" id="appendix-ttechnology"></a>技术（TTechnology）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>描述已收集数据所对应的技术。文本应包含识别活动数据所依据技术的属性和特征所需的信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="500"><td>@technologyLevel</td><td>500</td><td>new</td><td>0 = 未指定（undefined）, 1 = 新兴（New）, 2 = 现代（Modern）, 3 = 当前（Current，默认）, 4 = 旧有（Old）, 5 = 过时（Outdated）</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTechnology.500.description.0"><td></td><td colspan="9">对所描述活动的技术进行大致分类的标签，可在建模时用于选择具有特定技术水平的过程。所用代码如下：0=未指定（Undefined）。用于没有技术水平的市场活动。1=新兴（New）。用于在某些方面被认为技术上优于现代技术，但在投资纯粹依据经济考虑时尚未成为最普遍安装选择的技术。2=现代（Modern）。用于在投资纯粹依据经济考虑时，当前新增产能所采用的技术（最有竞争力的技术）。3=当前（Current，默认）。用于介于现代和旧有之间的技术。4=旧有（Old）。用于在退役纯粹依据经济考虑时，当前正在退出使用的技术（竞争力最低的技术）。5=过时（Outdated）。用于已不再使用的技术。这些术语并不一定反映技术的年代。如果一项技术仍最有竞争力，即使已有百年历史，也可以属于现代技术；如果一项技术很快被其他更有竞争力的技术取代，即使出现时间相对较短，也可以属于旧有技术。技术水平是相对于“时间段”（Time Period）所给数据有效年份而言的。在时间序列中，同一技术的技术水平可随时间改变。即使在同一年，同一技术在不同地理位置也可被赋予不同技术水平。</td></tr>
<tr data-field-id="510"><td>comment</td><td>510</td><td>692</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TTechnology.510.description.0"><td></td><td colspan="9">用于描述活动技术的文本和图像字段。文本应包含识别活动数据所依据技术的属性和特征所需的信息，描述该单元过程的技术属性。如果活动包含多个子活动，也应报告相应技术。描述应使用专业命名。文本和图像字段是 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
<tr data-source-block="TTechnology.510.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
</tbody></table>
<h3><a href="#appendix-ttimeperiod" id="appendix-ttimeperiod"></a>时间范围（TTimePeriod）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>描述数据集有效时间段的开始日期和结束日期。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="600"><td>@startDate</td><td>600</td><td>601</td><td></td><td>date</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.600.description.0"><td></td><td colspan="9">数据集有效时间段的开始日期，以完整日期（年-月-日）表示。</td></tr>
<tr data-field-id="610"><td>@endDate</td><td>610</td><td>602</td><td></td><td>date</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.610.description.0"><td></td><td colspan="9">数据集有效时间段的结束日期，以完整日期（年-月-日）表示。</td></tr>
<tr data-field-id="620"><td>@isDataValidForEntirePeriod</td><td>620</td><td>603</td><td></td><td>boolean</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.620.description.0"><td></td><td colspan="9">表示活动数据（在流数据下报告的基本流交换和中间交换）是否在所述整个时间段内有效。如果不是，可在“comment”中说明。</td></tr>
<tr data-field-id="630"><td>comment</td><td>630</td><td>611</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.630.description.0"><td></td><td colspan="9">用于进一步说明所报告数据时间有效性的文本和图像字段。例如，可包括以下信息：
- 所涉及单元过程的时间相关性有多强（例如，4 年前的数据是否仍适用于今天运行的活动）；
- 数据为何不在整个时间段内有效，以及数据在哪些较短时间段内有效。
文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TTimePeriod.630.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
</tbody></table>
<h3><a href="#appendix-tmacroeconomicscenario" id="appendix-tmacroeconomicscenario"></a>宏观经济情景（TMacroEconomicScenario）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>引用本数据集所用的宏观经济情景。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="700"><td>@macroEconomicScenarioId</td><td>700</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TMacroEconomicScenario.700.description.0"><td></td><td colspan="9">对有效情景列表中定义的某宏观经济情景的引用（见字段 3715）。</td></tr>
<tr data-field-id="701"><td>@macroEconomicScenarioContextId</td><td>701</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TMacroEconomicScenario.701.description.0"><td></td><td colspan="9">对宏观经济情景所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="720"><td>name</td><td>720</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TMacroEconomicScenario.720.description.0"><td></td><td colspan="9">本数据集所属宏观经济情景的名称。</td></tr>
<tr data-field-id="740"><td>comment</td><td>740</td><td>new</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TMacroEconomicScenario.740.description.0"><td></td><td colspan="9">描述宏观经济子数据集与父数据集默认情景的差异。</td></tr>
</tbody></table>
<h3><a href="#appendix-tcustomexchange" id="appendix-tcustomexchange"></a>交换的通用字段（TCustomExchange）</h3>
<p>原表分组可重复：是；原表分组必填：是。</p>
<p>本部分包含两种交换类型共同使用的元素。中间交换或与环境的交换各自特有的元素，列于下方相应部分。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1000"><td>name</td><td>1000</td><td>3702</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1000.description.0"><td></td><td colspan="9">交换的名称。</td></tr>
<tr data-field-id="1005"><td>@id</td><td>1005</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1005.description.0"><td></td><td colspan="9">该交换的唯一标识符。不能使用 intermediateExchangeId 或 elementaryExchangeId 来标识某个交换，因为数据集中的多个交换可以引用同一个主数据条目。</td></tr>
<tr data-field-id="1020"><td>@amount</td><td>1020</td><td>3707</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1020.description.0"><td></td><td colspan="9">基本流交换或中间交换的数量。</td></tr>
<tr data-field-id="1030"><td>@unitId</td><td>1030</td><td>3706</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1030.description.0"><td></td><td colspan="9">对该数量所用单位的引用。</td></tr>
<tr data-field-id="1031"><td>@unitContextId</td><td>1031</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1031.description.0"><td></td><td colspan="9">对单位所属上下文的引用。</td></tr>
<tr data-source-block="TCustomExchange.1031.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1035"><td>unitName</td><td>1035</td><td>3706</td><td></td><td>TString40</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1035.description.0"><td></td><td colspan="9">该数量所用单位的名称。</td></tr>
<tr data-field-id="1040"><td>@variableName</td><td>1040</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1040.description.0"><td></td><td colspan="9">变量名是交换的简称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific_Value 与 Calorific_value 等同）。</td></tr>
<tr data-field-id="1050"><td>@isCalculatedAmount</td><td>1050</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1050.description.0"><td></td><td colspan="9">如果为 true，则 amount 字段的值为 mathematicalRelation 或 transferCoefficient 的计算值。</td></tr>
<tr data-field-id="1060"><td>@mathematicalRelation</td><td>1060</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1060.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TCustomExchange.1060.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="1100"><td>@casNumber</td><td>1100</td><td>3701</td><td></td><td>TCasNumber</td><td>11</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1100.description.0"><td></td><td colspan="9">注明化学文摘社（CAS）编号。CAS 编号的格式为 000000-00-0，其中第一组数字不必完整，即允许少于六位数字。</td></tr>
<tr data-field-id="1110"><td>comment</td><td>1110</td><td>3792</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1110.description.0"><td></td><td colspan="9">可对每个单独的交换添加一般注释。</td></tr>
<tr data-field-id="1120"><td>@sourceId</td><td>1120</td><td>3715</td><td>引用在建模与验证部分定义的来源。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1120.description.0"><td></td><td colspan="9">对有效来源的引用。</td></tr>
<tr data-field-id="1121"><td>@sourceContextId</td><td>1121</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1121.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TCustomExchange.1121.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1122"><td>@sourceIdOverwrittenByChild</td><td>1122</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1122.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1125"><td>@sourceYear</td><td>1125</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1125.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="1126"><td>@sourceFirstAuthor</td><td>1126</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1126.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="1130"><td>@pageNumbers</td><td>1130</td><td>3716</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1130.description.0"><td></td><td colspan="9">如果数据来自文章或较长出版物中的特定页面，则填写相关页码。</td></tr>
<tr data-field-id="1150"><td>@specificAllocationPropertyId</td><td>1150</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1150.description.0"><td></td><td colspan="9">引用分配所使用的属性（Property）。这会覆盖由 masterAllocationPropertyId 定义、适用于整个数据集的默认设置。</td></tr>
<tr data-field-id="1151"><td>@specificAllocationPropertyContextId</td><td>1151</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1151.description.0"><td></td><td colspan="9">对属性所属上下文的引用。</td></tr>
<tr data-source-block="TCustomExchange.1151.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1152"><td>@specificAllocationPropertyIdOverwrittenByChild</td><td>1152</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1152.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1200"><td>transferCoefficient</td><td>1200</td><td>new</td><td></td><td>TTransferCoefficient</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1200.description.0"><td></td><td colspan="9">转移系数将特定输入与特定输出关联，并记录该特定输入中流向该特定输出的份额。</td></tr>
<tr data-source-block="TCustomExchange.1200.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1300"><td>uncertainty</td><td>1300</td><td>3708</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1300.description.0"><td></td><td colspan="9">以分布函数及其参数和/或数据质量谱系数据的形式提供不确定性信息。</td></tr>
<tr data-source-block="TCustomExchange.1300.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1400"><td>property</td><td>1400</td><td>new</td><td></td><td>TProperty</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1400.description.0"><td></td><td colspan="9">交换的属性，例如干质量、含水率、价格、特定元素或物质的含量。</td></tr>
<tr data-source-block="TCustomExchange.1400.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1450"><td>tag</td><td>1450</td><td>new</td><td></td><td>TTag</td><td>40</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1450.description.0"><td></td><td colspan="9">tag 字段允许使用开放式关键词列表描述活动，可用于筛选、分组和搜索。validTags 文件引用提供预定义标签列表；但如果 validTags 主文件中找不到某个标签条目，语义验证过程应仅显示提示信息，而不应报错。</td></tr>
<tr data-field-id="1470"><td>synonym</td><td>1470</td><td>new</td><td></td><td>TSynonym</td><td>80</td><td>是</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1470.description.0"><td></td><td colspan="9">名称的同义词列表。与普通多语言字符串不同，同义词可包含多个具有相同 xml:lang 属性值的元素。</td></tr>
<tr data-source-block="TCustomExchange.1470.description.1"><td></td><td colspan="9">允许 0..n 个条目，每个条目的最大长度为 80。</td></tr>
</tbody></table>
<h3><a href="#appendix-tintermediateexchange" id="appendix-tintermediateexchange"></a>中间交换专用字段（TIntermediateExchange）</h3>
<p>原表分组可重复：是；原表分组必填：是。</p>
<p>包含仅适用于中间交换的字段，是交换部分之外的附加字段。中间交换是单元过程中记录的产品或废物投入和输出，以及相应的相关信息。</p>
<p>对于中间交换，本部分扩展交换部分。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1500"><td>inputGroup</td><td>1500</td><td>3503</td><td>1 = 材料/燃料（Materials/Fuels）；2 = 电力/热（Electricity/Heat）；3 = 服务（Services）；5 = 来自技术圈，未指定（From Technosphere (unspecified)）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1500.description.0"><td></td><td colspan="9">注明输入流的种类。代码如下：1=材料/燃料（Materials/Fuels），2=电力/热（Electricity/Heat），3=服务（Services），5=来自技术圈，未指定（From Technosphere (unspecified)）。</td></tr>
<tr data-source-block="TIntermediateExchange.1500.description.1"><td></td><td colspan="9">每个交换只能具有 inputGroup 或 outputGroup 中的一个，以表示流的方向。</td></tr>
<tr data-field-id="1510"><td>outputGroup</td><td>1510</td><td>3504</td><td>0 = 参考产品（ReferenceProduct）；2 = 副产品（By-product）；3 = 待处理材料（Material for Treatment）；5 = 存量增加（Stock Additions）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1510.description.0"><td></td><td colspan="9">注明输出流的种类。代码如下：0=参考产品（ReferenceProduct），2=副产品（By-product），3=待处理材料（MaterialForTreatment），5=存量增加（Stock Additions）。</td></tr>
<tr data-source-block="TIntermediateExchange.1510.description.1"><td></td><td colspan="9">每个交换只能具有 inputGroup 或 outputGroup 中的一个，以表示流的方向。</td></tr>
<tr data-field-id="1515"><td>@intermediateExchangeId</td><td>1515</td><td>3793</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1515.description.0"><td></td><td colspan="9">引用该中间交换的主数据条目。</td></tr>
<tr data-field-id="1516"><td>@intermediateExchangeContextId</td><td>1516</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1516.description.0"><td></td><td colspan="9">对中间交换所属上下文的引用。</td></tr>
<tr data-source-block="TIntermediateExchange.1516.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1520"><td>@activityLinkId</td><td>1520</td><td>3715</td><td>引用字段 105（位于另一个活动数据集中）。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1520.description.0"><td></td><td colspan="9">显式引用供应该中间产品的活动。如果此字段为空，则由链接规则确定该活动；该规则使用本活动的地理和时间信息。</td></tr>
<tr data-field-id="1521"><td>@activityLinkContextId</td><td>1521</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1521.description.0"><td></td><td colspan="9">对活动链接所属上下文的引用。</td></tr>
<tr data-source-block="TIntermediateExchange.1521.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1522"><td>@activityLinkIdOverwrittenByChild</td><td>1522</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1522.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1530"><td>@productionVolumeAmount</td><td>1530</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1530.description.0"><td></td><td colspan="9">按年表示的产品产量，单位与该交换相同。</td></tr>
<tr data-field-id="1531"><td>@productionVolumeSourceIdOverwrittenByChild</td><td>1531</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1531.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1532"><td>@productionVolumeVariableName</td><td>1532</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1532.description.0"><td></td><td colspan="9">变量名是交换产量的简称，用于在数学关系（公式）中引用产量数值。变量可包含字母、数字和下划线（_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific_Value 与 Calorific_value 等同）。</td></tr>
<tr data-field-id="1533"><td>@productionVolumeSourceId</td><td>1533</td><td>new</td><td>引用在建模与验证部分定义的来源。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1533.description.0"><td></td><td colspan="9">对有效来源的引用。</td></tr>
<tr data-field-id="1534"><td>@productionVolumeMathematicalRelation</td><td>1534</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1534.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TIntermediateExchange.1534.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="1535"><td>productionVolumeComment</td><td>1535</td><td>724</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1535.description.0"><td></td><td colspan="9">可对产量数据的数据来源、假设和计算添加一般注释。</td></tr>
<tr data-field-id="1536"><td>@productionVolumeSourceContextId</td><td>1536</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1536.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TIntermediateExchange.1536.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1537"><td>@productionVolumeSourceYear</td><td>1537</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TIntermediateExchange.1537.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="1538"><td>@productionVolumeSourceFirstAuthor</td><td>1538</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TIntermediateExchange.1538.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="1539"><td>productionVolumeUncertainty</td><td>1539</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1539.description.0"><td></td><td colspan="9">以分布函数及其参数和/或数据质量谱系数据的形式提供不确定性信息。</td></tr>
<tr data-source-block="TIntermediateExchange.1539.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1540"><td>classification</td><td>1540</td><td>new</td><td></td><td>TClassification</td><td></td><td>是</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TIntermediateExchange.1540.description.0"><td></td><td colspan="9">包含用于界定产品的分类配对。</td></tr>
</tbody></table>
<h3><a href="#appendix-telementaryexchange" id="appendix-telementaryexchange"></a>基本流交换专用字段（TElementaryExchange）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>包含仅适用于基本流交换的字段（除交换部分的字段之外）。与环境的交换是作为单元过程输入和输出记录的基本流，并包含其相关信息。</p>
<p>当交换发生于活动与环境之间时，此部分扩展交换部分。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1600"><td>inputGroup</td><td>1600</td><td>3503</td><td>4 = 来自环境（From Environment）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1600.description.0"><td></td><td colspan="9">表示输入流的类型。代码为：4=来自环境（From Environment）。</td></tr>
<tr data-source-block="TElementaryExchange.1600.description.1"><td></td><td colspan="9">对于每个交换，只能存在 inputGroup 或 outputGroup 中的一个，以表明流的方向。</td></tr>
<tr data-source-block="TElementaryExchange.1600.description.2"><td></td><td colspan="9">此字段相当于字段 1500，但有效值集合不同。</td></tr>
<tr data-field-id="1610"><td>outputGroup</td><td>1610</td><td>3504</td><td>4 = 流向环境（ToEnvironment）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1610.description.0"><td></td><td colspan="9">表示输出流的类型。代码为：4=流向环境（ToEnvironment）。</td></tr>
<tr data-source-block="TElementaryExchange.1610.description.1"><td></td><td colspan="9">对于每个交换，只能存在 inputGroup 或 outputGroup 中的一个，以表明流的方向。</td></tr>
<tr data-source-block="TElementaryExchange.1610.description.2"><td></td><td colspan="9">此字段相当于字段 1510，但有效值集合不同。</td></tr>
<tr data-field-id="1615"><td>@elementaryExchangeId</td><td>1615</td><td>3793</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1615.description.0"><td></td><td colspan="9">引用此基本流交换的主数据条目。</td></tr>
<tr data-field-id="1616"><td>@elementaryExchangeContextId</td><td>1616</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1616.description.0"><td></td><td colspan="9">引用该基本流交换所属的上下文。</td></tr>
<tr data-source-block="TElementaryExchange.1616.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1660"><td>compartment</td><td>1660</td><td>new</td><td></td><td>TCompartment</td><td></td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TElementaryExchange.1660.description.0"><td></td><td colspan="9">交换的区室及子区室名称。validCompartments 所引用的 XML 文档包含给定语言下有效的区室／子区室配对的定义。</td></tr>
<tr data-field-id="1670"><td>@formula</td><td>1670</td><td>3711</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TElementaryExchange.1670.description.0"><td></td><td colspan="9">可以填写化学式，例如分子式。</td></tr>
</tbody></table>
<h3><a href="#appendix-tparameter" id="appendix-tparameter"></a>参数（TParameter）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>供公式使用的数据集参数。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1700"><td>name</td><td>1700</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TParameter.1700.description.0"><td></td><td colspan="9">参数的描述性名称。</td></tr>
<tr data-field-id="1705"><td>@parameterId</td><td>1705</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1705.description.0"><td></td><td colspan="9">对有效主数据参数的引用。</td></tr>
<tr data-field-id="1706"><td>@parameterContextId</td><td>1706</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1706.description.0"><td></td><td colspan="9">对参数所属上下文的引用。</td></tr>
<tr data-source-block="TParameter.1706.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1710"><td>@amount</td><td>1710</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1710.description.0"><td></td><td colspan="9">参数的当前值。</td></tr>
<tr data-field-id="1712"><td>@unitId</td><td>1712</td><td>3706</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TParameter.1712.description.0"><td></td><td colspan="9">对参数数量单位的引用。</td></tr>
<tr data-field-id="1713"><td>@unitContextId</td><td>1713</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TParameter.1713.description.0"><td></td><td colspan="9">对单位所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1714"><td>unitName</td><td>1714</td><td>3706</td><td></td><td>TString40</td><td>40</td><td>否</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TParameter.1714.description.0"><td></td><td colspan="9">参数数量的单位名称。</td></tr>
<tr data-field-id="1715"><td>@variableName</td><td>1715</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1715.description.0"><td></td><td colspan="9">变量名是交换的简短名称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific_Value 与 Calorific_value 相同）。</td></tr>
<tr data-field-id="1720"><td>@mathematicalRelation</td><td>1720</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1720.description.0"><td></td><td colspan="9">定义数学公式，通过变量名或 REF 函数引用流、参数或属性的值。</td></tr>
<tr data-source-block="TParameter.1720.description.1"><td></td><td colspan="9">将采用一组特定变量值计算得到的公式结果写入 amount 字段。</td></tr>
<tr data-field-id="1725"><td>@isCalculatedAmount</td><td>1725</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1725.description.0"><td></td><td colspan="9">若为 true，则 amount 字段的值为 mathematicalRelation 的计算值。</td></tr>
<tr data-field-id="1730"><td>uncertainty</td><td>1730</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1730.description.0"><td></td><td colspan="9">参数数量的不确定性。</td></tr>
<tr data-field-id="1740"><td>comment</td><td>1740</td><td>new</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TParameter.1740.description.0"><td></td><td colspan="9">可对每个单独参数填写一般说明。</td></tr>
</tbody></table>
<h3><a href="#appendix-timpactindicatorresult" id="appendix-timpactindicatorresult"></a>影响指标结果（TImpactIndicatorResult）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>计算得到的影响指标。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1800"><td>@impactIndicatorId</td><td>1800</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1800.description.0"><td></td><td colspan="9">对影响指标的引用。</td></tr>
<tr data-field-id="1801"><td>@impactIndicatorContextId</td><td>1801</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1801.description.0"><td></td><td colspan="9">对影响指标所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1810"><td>@impactMethodId</td><td>1810</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1810.description.0"><td></td><td colspan="9">对影响指标所属方法的引用。</td></tr>
<tr data-field-id="1811"><td>@impactMethodContextId</td><td>1811</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1811.description.0"><td></td><td colspan="9">对影响评价方法所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1815"><td>impactMethodName</td><td>1815</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1815.description.0"><td></td><td colspan="9">影响评价方法的名称。</td></tr>
<tr data-field-id="1820"><td>@impactCategoryId</td><td>1820</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1820.description.0"><td></td><td colspan="9">对影响类别所属方法的引用。</td></tr>
<tr data-field-id="1821"><td>@impactCategoryContextId</td><td>1821</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1821.description.0"><td></td><td colspan="9">对影响类别所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1825"><td>impactCategoryName</td><td>1825</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1825.description.0"><td></td><td colspan="9">影响类别的名称。</td></tr>
<tr data-field-id="1830"><td>@amount</td><td>1830</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1830.description.0"><td></td><td colspan="9">影响指标的值。</td></tr>
<tr data-field-id="1840"><td>name</td><td>1840</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1840.description.0"><td></td><td colspan="9">影响指标的名称。</td></tr>
<tr data-field-id="1850"><td>unitName</td><td>1850</td><td>new</td><td></td><td>TString40</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1850.description.0"><td></td><td colspan="9">影响指标数量的单位名称。</td></tr>
</tbody></table>
<h3><a href="#appendix-tcompartment" id="appendix-tcompartment"></a>区室与子区室（TCompartment）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>包含用于指定交换的区室配对。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="330"><td>compartment</td><td>330</td><td>new</td><td></td><td>TCompartmentName</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCompartment.330.description.0"><td></td><td colspan="9">区室名称。这是所引用区室（字段 5315）的纯文本值。</td></tr>
<tr data-field-id="340"><td>subcompartment</td><td>340</td><td>new</td><td></td><td>TCompartmentName</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCompartment.340.description.0"><td></td><td colspan="9">子区室名称。这是所引用子区室（字段 5325）的纯文本值。</td></tr>
<tr data-field-id="350"><td>@subcompartmentId</td><td>350</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCompartment.350.description.0"><td></td><td colspan="9">引用区室／子区室配对。该配对必须在有效区室列表中定义（见字段 5330）。</td></tr>
<tr data-field-id="351"><td>@subcompartmentContextId</td><td>351</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCompartment.351.description.0"><td></td><td colspan="9">引用该子区室所属的上下文。</td></tr>
<tr data-source-block="TCompartment.351.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
</tbody></table>
<h3><a href="#appendix-tuncertainty" id="appendix-tuncertainty"></a>不确定性（TUncertainty）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>必须从以下不确定性方法（对数正态、正态、……、未定义分布）中恰好选择一种。TUncertainty 复杂类型用于多个位置，因此，一个数据集可在不同位置包含多个 uncertainty 元素。但每个具有不确定性信息的元素只能包含一个 uncertainty 元素。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="2010"><td>comment</td><td>2010</td><td>3792</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2010.description.0"><td></td><td colspan="9">可对每项不确定性信息填写一般说明。</td></tr>
<tr data-field-id="2100"><td>lognormal</td><td>2100</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2100.description.0"><td></td><td colspan="9">具有平均值 μ（Mu 参数）和方差 σ（Variance 参数）的对数正态分布，是对特征值的自然对数 ln(x) 而非 x 值进行描述的正态分布。</td></tr>
<tr data-field-id="2101"><td>@meanValue</td><td>2101</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2101.description.0"><td></td><td colspan="9">几何平均值。</td></tr>
<tr data-field-id="2102"><td>@mu</td><td>2102</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2102.description.0"><td></td><td colspan="9">底层正态分布的算术平均值。</td></tr>
<tr data-field-id="2103"><td>@variance</td><td>2103</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2103.description.0"><td></td><td colspan="9">底层正态分布的无偏方差。</td></tr>
<tr data-field-id="2104"><td>@varianceWithPedigreeUncertainty</td><td>2104</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2104.description.0"><td></td><td colspan="9">底层正态分布的无偏方差，包括基础不确定性和谱系不确定性。</td></tr>
<tr data-field-id="2110"><td>normal</td><td>2110</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2110.description.0"><td></td><td colspan="9">正态分布，也称“高斯”分布。它是一族具有相同一般形式的分布，其位置参数和尺度参数不同，分别为均值（MeanValue）和标准差（Deviation）。</td></tr>
<tr data-field-id="2111"><td>@meanValue</td><td>2111</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2111.description.0"><td></td><td colspan="9">算术平均值。</td></tr>
<tr data-field-id="2112"><td>@variance</td><td>2112</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2112.description.0"><td></td><td colspan="9">无偏方差。</td></tr>
<tr data-field-id="2113"><td>@varianceWithPedigreeUncertainty</td><td>2113</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2113.description.0"><td></td><td colspan="9">无偏方差，包括基础不确定性和谱系不确定性。</td></tr>
<tr data-field-id="2120"><td>triangular</td><td>2120</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2120.description.0"><td></td><td colspan="9">参数为 minValue、mostLikelyValue 和 maxValue。</td></tr>
<tr data-source-block="TUncertainty.2120.description.1"><td></td><td colspan="9">采用三角不确定性分布时，应根据 mostLikelyValue 计算 meanValue。在 ecoinvent 上下文中，不得使用 mostLikelyValue 字段（#3797）。</td></tr>
<tr data-field-id="2121"><td>@minValue</td><td>2121</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2121.description.0"><td></td><td colspan="9">最小值。</td></tr>
<tr data-field-id="2122"><td>@mostLikelyValue</td><td>2122</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2122.description.0"><td></td><td colspan="9">众数。</td></tr>
<tr data-field-id="2123"><td>@maxValue</td><td>2123</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2123.description.0"><td></td><td colspan="9">最大值。</td></tr>
<tr data-field-id="2130"><td>uniform</td><td>2130</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2130.description.0"><td></td><td colspan="9">minValue 与 maxValue 参数之间的均匀分布。如果 maxValue 参数小于 minValue 参数，则交换两者的值。</td></tr>
<tr data-field-id="2131"><td>@minValue</td><td>2131</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2131.description.0"><td></td><td colspan="9">最小值。</td></tr>
<tr data-field-id="2132"><td>@maxValue</td><td>2132</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2132.description.0"><td></td><td colspan="9">最大值。</td></tr>
<tr data-field-id="2140"><td>beta</td><td>2140</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2140.description.0"><td></td><td colspan="9">Beta 分布使用 minValue（a）、maxValue（b）和 mostFrequentValue（m）参数，计算底层 Gamma 分布的两个形状参数。参数必须满足条件：((a &lt;= m) and (m &lt;= b)) or (a = b)。形状参数按以下公式计算：Shape1 = 1 + 4 * ((m-a) / (b-a))。Shape2 = 6 - Shape1。</td></tr>
<tr data-field-id="2141"><td>@minValue</td><td>2141</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2141.description.0"><td></td><td colspan="9">最小值（a）。</td></tr>
<tr data-field-id="2142"><td>@mostFrequentValue</td><td>2142</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2142.description.0"><td></td><td colspan="9">最常出现的值（m）。</td></tr>
<tr data-field-id="2143"><td>@maxValue</td><td>2143</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2143.description.0"><td></td><td colspan="9">最大值（b）。</td></tr>
<tr data-field-id="2150"><td>gamma</td><td>2150</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2150.description.0"><td></td><td colspan="9">Gamma 分布使用尺度参数和形状参数。这里输入的值将取绝对值使用。minimum 参数的值将加到所有抽样值上。</td></tr>
<tr data-field-id="2151"><td>@shape</td><td>2151</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2151.description.0"><td></td><td colspan="9">形状参数。</td></tr>
<tr data-field-id="2152"><td>@scale</td><td>2152</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2152.description.0"><td></td><td colspan="9">尺度参数。</td></tr>
<tr data-field-id="2153"><td>@minValue</td><td>2153</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2153.description.0"><td></td><td colspan="9">最小值（位置参数）。</td></tr>
<tr data-field-id="2160"><td>binomial</td><td>2160</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2160.description.0"><td></td><td colspan="9">二项分布使用 n 和 p 参数。</td></tr>
<tr data-field-id="2161"><td>@n</td><td>2161</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2161.description.0"><td></td><td colspan="9">独立试验次数。</td></tr>
<tr data-field-id="2162"><td>@p</td><td>2162</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2162.description.0"><td></td><td colspan="9">每次试验的成功概率。</td></tr>
<tr data-field-id="2170"><td>undefined</td><td>2170</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2170.description.0"><td></td><td colspan="9">此“分布”可用于保存 EcoSpold01 格式的旧数据；该格式复用 minValue、maxValue 和 standardDeviation95 字段，存储未定义分布的数据。</td></tr>
<tr data-field-id="2171"><td>@minValue</td><td>2171</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2171.description.0"><td></td><td colspan="9">最小值。</td></tr>
<tr data-field-id="2172"><td>@maxValue</td><td>2172</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2172.description.0"><td></td><td colspan="9">最大值。</td></tr>
<tr data-field-id="2173"><td>@standardDeviation95</td><td>2173</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2173.description.0"><td></td><td colspan="9">从均值向两侧延伸、为覆盖总体 95% 所需的值。</td></tr>
<tr data-field-id="2270"><td>pedigreeMatrix</td><td>2270</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2270.description.0"><td></td><td colspan="9">数据质量指标提供数据质量的定性评价。该评价可转换为定量的附加不确定性，并加到基础不确定性上。pedigreeMatrix 元素将 5 个数据质量指标分组，其自身不包含数据。</td></tr>
<tr data-field-id="2271"><td>@reliability</td><td>2271</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2271.description.0"><td></td><td colspan="9">1=基于测量且经过验证的数据。</td></tr>
<tr data-source-block="TUncertainty.2271.description.1"><td></td><td colspan="9">2=部分基于假设且经过验证的数据，或基于测量但未经过验证的数据。</td></tr>
<tr data-source-block="TUncertainty.2271.description.2"><td></td><td colspan="9">3=部分基于有专业依据的估算、但未经过验证的数据。</td></tr>
<tr data-source-block="TUncertainty.2271.description.3"><td></td><td colspan="9">4=有专业依据的估算，例如由行业专家作出的估算。</td></tr>
<tr data-source-block="TUncertainty.2271.description.4"><td></td><td colspan="9">5=无专业依据的估算（默认）。</td></tr>
<tr data-field-id="2272"><td>@completeness</td><td>2272</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2272.description.0"><td></td><td colspan="9">1=来自所考察市场相关全部场所的代表性数据，时间跨度足以平滑正常波动。</td></tr>
<tr data-source-block="TUncertainty.2272.description.1"><td></td><td colspan="9">2=来自所考察市场相关场所中 &gt;50% 的代表性数据，时间跨度足以平滑正常波动。</td></tr>
<tr data-source-block="TUncertainty.2272.description.2"><td></td><td colspan="9">3=仅来自所考察市场相关部分场所（&lt;&lt;50%）的代表性数据，或来自 &gt;50% 的场所但时间跨度较短的数据。</td></tr>
<tr data-source-block="TUncertainty.2272.description.3"><td></td><td colspan="9">4=仅来自所考察市场相关一个场所的代表性数据，或来自部分场所但时间跨度较短的数据。</td></tr>
<tr data-source-block="TUncertainty.2272.description.4"><td></td><td colspan="9">5=代表性未知，或来自少数场所且时间跨度较短的数据。</td></tr>
<tr data-field-id="2273"><td>@temporalCorrelation</td><td>2273</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2273.description.0"><td></td><td colspan="9">1=与数据集的时间期间（字段 600-610）相差不足 3 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.1"><td></td><td colspan="9">2=与数据集的时间期间（字段 600-610）相差不足 6 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.2"><td></td><td colspan="9">3=与数据集的时间期间（字段 600-610）相差不足 10 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.3"><td></td><td colspan="9">4=与数据集的时间期间（字段 600-610）相差不足 15 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.4"><td></td><td colspan="9">5=数据年代未知，或与数据集的时间期间（字段 600-610）相差超过 15 年。</td></tr>
<tr data-field-id="2274"><td>@geographicalCorrelation</td><td>2274</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2274.description.0"><td></td><td colspan="9">1=来自研究区域的数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.1"><td></td><td colspan="9">2=来自包含研究区域的更大区域的平均数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.2"><td></td><td colspan="9">3=来自生产条件相似区域的数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.3"><td></td><td colspan="9">4=来自生产条件略有相似之处的区域的数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.4"><td></td><td colspan="9">5=来自未知区域或明显不同区域的数据，例如以北美代替中东、以 OECD 欧洲代替俄罗斯。</td></tr>
<tr data-field-id="2275"><td>@furtherTechnologyCorrelation</td><td>2275</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2275.description.0"><td></td><td colspan="9">1=来自所研究企业、过程和材料的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.1"><td></td><td colspan="9">2=来自所研究过程和材料（即相同技术），但企业不同的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.2"><td></td><td colspan="9">3=来自所研究过程和材料，但技术不同的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.3"><td></td><td colspan="9">4=有关相关过程或材料的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.4"><td></td><td colspan="9">5=有关实验室规模相关过程的数据，或来自不同技术的数据。</td></tr>
</tbody></table>
<h3><a href="#appendix-tproperty" id="appendix-tproperty"></a>属性（TProperty）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>用于指定交换属性的格式。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="2300"><td>@propertyId</td><td>2300</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2300.description.0"><td></td><td colspan="9">引用该属性的主数据条目。</td></tr>
<tr data-field-id="2301"><td>@propertyContextId</td><td>2301</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2301.description.0"><td></td><td colspan="9">对属性所属上下文的引用。</td></tr>
<tr data-source-block="TProperty.2301.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2310"><td>name</td><td>2310</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TProperty.2310.description.0"><td></td><td colspan="9">属性的描述性名称。</td></tr>
<tr data-field-id="2320"><td>@unitId</td><td>2320</td><td>3706</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2320.description.0"><td></td><td colspan="9">对该数量所用单位的引用。</td></tr>
<tr data-field-id="2321"><td>@unitContextId</td><td>2321</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2321.description.0"><td></td><td colspan="9">对单位所属上下文的引用。</td></tr>
<tr data-source-block="TProperty.2321.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2325"><td>unitName</td><td>2325</td><td>3706</td><td></td><td>TString40</td><td>40</td><td>否</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TProperty.2325.description.0"><td></td><td colspan="9">属性量所用单位的名称。</td></tr>
<tr data-field-id="2330"><td>@amount</td><td>2330</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2330.description.0"><td></td><td colspan="9">属性的值。</td></tr>
<tr data-field-id="2335"><td>@isDefiningValue</td><td>2335</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2335.description.0"><td></td><td colspan="9">如果此字段为 true，则该属性值是交换定义的一部分，因此与交换量之间具有固定关系；不能针对该交换在不同数据集中的个别实例改变这一关系。</td></tr>
<tr data-field-id="2340"><td>@mathematicalRelation</td><td>2340</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2340.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TProperty.2340.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="2345"><td>@isCalculatedAmount</td><td>2345</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2345.description.0"><td></td><td colspan="9">如果为 true，则 amount 字段的值为 mathematicalRelation 的计算值。</td></tr>
<tr data-field-id="2350"><td>@variableName</td><td>2350</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2350.description.0"><td></td><td colspan="9">定义变量名，以便在 mathematicalrelation（数学关系）中引用属性量。</td></tr>
<tr data-source-block="TProperty.2350.description.1"><td></td><td colspan="9">变量名必须以字母（a-z）开头，可包含字母、数字和下划线（_）。变量名不区分大小写（calorific_Value 与 Calorific_value 等同）。</td></tr>
<tr data-field-id="2360"><td>uncertainty</td><td>2360</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2360.description.0"><td></td><td colspan="9">属性值的不确定性。</td></tr>
<tr data-field-id="2370"><td>@sourceId</td><td>2370</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2370.description.0"><td></td><td colspan="9">对有效来源的引用，指明记录该属性的出版物。</td></tr>
<tr data-field-id="2371"><td>@sourceContextId</td><td>2371</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2371.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TProperty.2371.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2372"><td>@sourceIdOverwrittenByChild</td><td>2372</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2372.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="2375"><td>@sourceYear</td><td>2375</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2375.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="2376"><td>@sourceFirstAuthor</td><td>2376</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2376.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="2380"><td>comment</td><td>2380</td><td>new</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TProperty.2380.description.0"><td></td><td colspan="9">可对某个特定交换的每项单独属性添加一般注释。</td></tr>
</tbody></table>
<h3><a href="#appendix-ttransfercoefficient" id="appendix-ttransfercoefficient"></a>转移系数（TTransferCoefficient）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>用于根据投入量计算输出量的转移系数。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="2400"><td>@exchangeId</td><td>2400</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2400.description.0"><td></td><td colspan="9">引用某个交换的 UUID。</td></tr>
<tr data-field-id="2410"><td>@amount</td><td>2410</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2410.description.0"><td></td><td colspan="9">应将转移系数的数值与所引用交换的数量相乘。</td></tr>
<tr data-field-id="2420"><td>@mathematicalRelation</td><td>2420</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2420.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TTransferCoefficient.2420.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="2425"><td>@isCalculatedAmount</td><td>2425</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2425.description.0"><td></td><td colspan="9">如果为 true，则 amount 字段的值为 mathematicalRelation 的计算值。</td></tr>
<tr data-field-id="2430"><td>uncertainty</td><td>2430</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2430.description.0"><td></td><td colspan="9">转移系数数值的不确定性。</td></tr>
<tr data-field-id="2440"><td>@sourceId</td><td>2440</td><td>new</td><td>引用在 modellingAndValidation 部分定义的来源。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2440.description.0"><td></td><td colspan="9">对有效来源的引用。</td></tr>
<tr data-field-id="2441"><td>@sourceContextId</td><td>2441</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2441.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TTransferCoefficient.2441.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2442"><td>@sourceIdOverwrittenByChild</td><td>2442</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2442.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="2445"><td>@sourceYear</td><td>2445</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TTransferCoefficient.2445.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="2446"><td>@sourceFirstAuthor</td><td>2446</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TTransferCoefficient.2446.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="2450"><td>comment</td><td>2450</td><td>3792</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2450.description.0"><td></td><td colspan="9">可对每个单独的转移系数添加一般注释。</td></tr>
</tbody></table>
<h3><a href="#appendix-ttextandimage" id="appendix-ttextandimage"></a>文本与图像（TTextAndImage）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>text、imageUri 和 variable 元素的列表。这些元素可按任意顺序组合。必须通过 text 和 imageUrl 元素的 index 属性指定它们在结果中的所需顺序。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3900"><td>text</td><td>3900</td><td>new</td><td></td><td>TIndexedString32000</td><td>32000</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTextAndImage.3900.description.0"><td></td><td colspan="9">用于描述当前部分的自由文本。其 index 属性用于规定文本和图像元素的特定顺序。</td></tr>
<tr data-field-id="3910"><td>imageUrl</td><td>3910</td><td>new</td><td></td><td>anyURI</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTextAndImage.3910.description.0"><td></td><td colspan="9">可用于在文本之间插入图像。其 index 属性用于规定文本和图像元素的特定顺序。</td></tr>
<tr data-field-id="3920"><td>variable</td><td>3920</td><td>new</td><td></td><td>TNamedString32000</td><td>32000</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTextAndImage.3920.description.0"><td></td><td colspan="9">定义本部分 text 元素中使用的变量名及其值。派生数据集可以覆盖这些定义，以改变变量值。</td></tr>
</tbody></table>
<h3><a href="#appendix-trepresentativeness" id="appendix-trepresentativeness"></a>代表性（TRepresentativeness）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>包含数据集信息的代表性，以及数据如何采样和／或计算的信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3000"><td>@systemModelId</td><td>3000</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3000.description.0"><td></td><td colspan="9">系统模型描述如何将活动数据集链接成产品系统。ecoinvent 网络中的部分选项为：&#x27;undefined&#x27;（未指定系统模型）、&#x27;attributional, average current suppliers, revenue allocation&#x27;（归因型、当前供应商平均组合、按收入分配）、&#x27;consequential, small-scale, long-term decisions&#x27;（后果型、小规模、长期决策）。</td></tr>
<tr data-field-id="3001"><td>@systemModelContextId</td><td>3001</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3001.description.0"><td></td><td colspan="9">引用该系统模型所属的上下文。</td></tr>
<tr data-source-block="TRepresentativeness.3001.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3005"><td>systemModelName</td><td>3005</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TRepresentativeness.3005.description.0"><td></td><td colspan="9">所引用系统模型（字段 3000）的纯文本值。</td></tr>
<tr data-field-id="3010"><td>@percent</td><td>3010</td><td>722</td><td>最大值为 100。</td><td>TPercent</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3010.description.0"><td></td><td colspan="9">所采样数据占该活动拟代表总体的百分比；该总体由 Geography、Technology 和 Time Period 下的字段确定。</td></tr>
<tr data-field-id="3030"><td>samplingProcedure</td><td>3030</td><td>725</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3030.description.0"><td></td><td colspan="9">描述用于量化交换的采样和计算程序的文本。应说明特定基本流交换和中间交换的采样程序是否不同于一般程序，并指出组合不同采样程序可能产生的问题。文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。</td></tr>
<tr data-field-id="3040"><td>extrapolations</td><td>3040</td><td>726</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.0"><td></td><td colspan="9">描述从另一时间期间、另一地理区域或另一技术外推数据的情况，以及这些外推的具体实施方式。</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.1"><td></td><td colspan="9">应说明是否在单个交换层面进行了不同的外推。</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.2"><td></td><td colspan="9">如果将代表某一国家运行活动的数据用于另一国家的活动，可在这里注明其原始代表性。</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.3"><td></td><td colspan="9">也可在这里说明外推导致的均值变化。</td></tr>
</tbody></table>
<h3><a href="#appendix-treview" id="appendix-treview"></a>审查（TReview）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>包含开展鉴定性评审（critical review）的人员信息，以及评审的主要结果、结论和提出的建议。</p>
<p>允许多名评审者。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3300"><td>@reviewerId</td><td>3300</td><td>5616</td><td>引用字段 3610。</td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3300.description.0"><td></td><td colspan="9">注明开展评审的人员。</td></tr>
<tr data-field-id="3301"><td>@reviewerContextId</td><td>3301</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3301.description.0"><td></td><td colspan="9">对评审者所属上下文的引用。</td></tr>
<tr data-source-block="TReview.3301.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3305"><td>@reviewerName</td><td>3305</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TReview.3305.description.0"><td></td><td colspan="9">人员的名字和姓氏。</td></tr>
<tr data-field-id="3306"><td>@reviewerEmail</td><td>3306</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TReview.3306.description.0"><td></td><td colspan="9">人员的完整电子邮件地址。</td></tr>
<tr data-field-id="3310"><td>@reviewDate</td><td>3310</td><td>new</td><td></td><td>date</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3310.description.0"><td></td><td colspan="9">验证或评审日期。</td></tr>
<tr data-field-id="3320"><td>@reviewedMajorRelease</td><td>3320</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3320.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3800。</td></tr>
<tr data-field-id="3325"><td>@reviewedMinorRelease</td><td>3325</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3325.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3805。</td></tr>
<tr data-field-id="3330"><td>@reviewedMajorRevision</td><td>3330</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3330.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3810。</td></tr>
<tr data-field-id="3335"><td>@reviewedMinorRevision</td><td>3335</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3335.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3815。</td></tr>
<tr data-field-id="3340"><td>details</td><td>3340</td><td>5615</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TReview.3340.description.0"><td></td><td colspan="9">用于记录数据集评审者注释的文本和图像字段。文本和图像字段是 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
<tr data-source-block="TReview.3340.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
<tr data-field-id="3350"><td>otherDetails</td><td>3350</td><td>5619</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TReview.3350.description.0"><td></td><td colspan="9">包含评审过程的进一步信息，例如数据集首次发布后补充的小幅修正。</td></tr>
</tbody></table>
<h3><a href="#appendix-tdataentryby" id="appendix-tdataentryby"></a>数据录入者（TDataEntryBy）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含数据集作者的信息，即将数据录入数据库格式的人员，也是对数据负责的人员。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3400"><td>@personId</td><td>3400</td><td>302</td><td>条目必须与字段 3610 中的现有条目一致。</td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataEntryBy.3400.description.0"><td></td><td colspan="9">编制数据集并将其录入数据库的人员的 ID 编号。</td></tr>
<tr data-field-id="3401"><td>@personContextId</td><td>3401</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataEntryBy.3401.description.0"><td></td><td colspan="9">对人员所属上下文的引用。</td></tr>
<tr data-source-block="TDataEntryBy.3401.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3403"><td>@isActiveAuthor</td><td>3403</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataEntryBy.3403.description.0"><td></td><td colspan="9">此字段定义字段 3400 指定的人员是否为本数据集的活跃作者（active author）。其他数据提供者今后修改数据集时，将征询该活跃作者的意见。</td></tr>
<tr data-field-id="3405"><td>@personName</td><td>3405</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataEntryBy.3405.description.0"><td></td><td colspan="9">人员的名字和姓氏。</td></tr>
<tr data-field-id="3406"><td>@personEmail</td><td>3406</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataEntryBy.3406.description.0"><td></td><td colspan="9">人员的完整电子邮件地址。</td></tr>
</tbody></table>
<h3><a href="#appendix-tdatageneratorandpublication" id="appendix-tdatageneratorandpublication"></a>数据生成者与发布（TDataGeneratorAndPublication）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含谁收集、汇编或发布原始数据的信息。此人与 &#x27;DataEntryBy&#x27; 中的人可能相同，也可能不同。此外，还包含数据集所依据出版物的类型及数据集可访问性的信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3500"><td>@personId</td><td>3500</td><td>751</td><td>数据生成者的 ID 编号，即收集、汇编或发布原始数据的个人或组织的编号。数据生成者与作者（见 &#x27;DataEntryBy&#x27;）可能相同，也可能不同。此字段旨在确认并引用数据来源，以及承担主要数据收集工作的个人或组织。</td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3500.description.0"><td></td><td colspan="9">生成数据集的个人的 ID 编号。该编号必须对应于相应数据集中所列某个人的 ID 编号。</td></tr>
<tr data-field-id="3501"><td>@personContextId</td><td>3501</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3501.description.0"><td></td><td colspan="9">引用该人员所属的上下文。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3501.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3505"><td>@personName</td><td>3505</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3505.description.0"><td></td><td colspan="9">人员的名和姓。</td></tr>
<tr data-field-id="3506"><td>@personEmail</td><td>3506</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3506.description.0"><td></td><td colspan="9">人员的完整电子邮件地址。</td></tr>
<tr data-field-id="3510"><td>@dataPublishedIn</td><td>3510</td><td>756</td><td>0 = 数据本身未在其他地方发布（默认）；1 = 部分单元过程或子系统的数据已发布；2 = 数据已完整发布于某来源中（引用字段 757）。</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3510.description.0"><td></td><td colspan="9">表示数据集是否已发布：未发布、部分发布或完整发布。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3510.description.1"><td></td><td colspan="9">代码为：0=数据本身未发布（默认）；1=部分单元过程或子系统的数据已发布；2=数据已完整发布于 &#x27;referenceToPublishedSource&#x27; 中。</td></tr>
<tr data-field-id="3520"><td>@publishedSourceId</td><td>3520</td><td>757</td><td>引用 801。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3520.description.0"><td></td><td colspan="9">记录该数据集的报告的 ID 编号。</td></tr>
<tr data-field-id="3521"><td>@publishedSourceContextId</td><td>3521</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3521.description.0"><td></td><td colspan="9">引用该已发布来源所属的上下文。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3521.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3522"><td>@publishedSourceIdOverwrittenByChild</td><td>3522</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3522.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="3525"><td>@publishedSourceYear</td><td>3525</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3525.description.0"><td></td><td colspan="9">分别表示出版年份或沟通年份。对于网站，表示最后访问年份。</td></tr>
<tr data-field-id="3526"><td>@publishedSourceFirstAuthor</td><td>3526</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3526.description.0"><td></td><td colspan="9">以姓和名字缩写标明第一作者，例如 Einstein A.。对于现场测量、口头沟通、个人书面沟通和问卷（&#x27;sourceType&#x27;=4, 5, 6, 7），这里填写沟通人员的姓名。</td></tr>
<tr data-field-id="3530"><td>@pageNumbers</td><td>3530</td><td>762</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3530.description.0"><td></td><td colspan="9">若数据取自文章或较大型出版物的特定页面，则填写相关页码。</td></tr>
<tr data-field-id="3540"><td>@isCopyrightProtected</td><td>3540</td><td>758</td><td></td><td>boolean</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3540.description.0"><td></td><td colspan="9">表示是否存在著作权。应相应填写 &#x27;1&#x27;（是）或 &#x27;0&#x27;（否）。</td></tr>
<tr data-field-id="3550"><td>@accessRestrictedTo</td><td>3550</td><td>759</td><td>0=公开；1=被许可人；2=仅结果；3=受限制。</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.0"><td></td><td colspan="9">表示数据集可能存在的访问限制。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.1"><td></td><td colspan="9">所用代码为：0=公开；1=被许可人；2=仅结果；3=受限制。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.2"><td></td><td colspan="9">accessRestrictedTo=0：无访问限制。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.3"><td></td><td colspan="9">accessRestrictedTo=1：只有许可证持有者（由上下文定义）可以访问。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.4"><td></td><td colspan="9">accessRestrictedTo=2：许可证持有者（由上下文定义）可以访问 LCI 结果，但不能访问单元过程原始数据。数据库管理员具有完整访问权限。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.5"><td></td><td colspan="9">accessRestrictedTo=3：只有 &#x27;companyCode&#x27; 指定的组织和数据库管理员可以访问。</td></tr>
<tr data-field-id="3560"><td>@companyId</td><td>3560</td><td>760</td><td>如果 759=3。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3560.description.0"><td></td><td colspan="9">引用允许使用此数据集的组织／机构；数据集使用限于该组织／机构。</td></tr>
<tr data-field-id="3561"><td>@companyContextId</td><td>3561</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3561.description.0"><td></td><td colspan="9">引用该公司所属的上下文。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3561.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3562"><td>@companyCode</td><td>3562</td><td>760</td><td>如果 759=3。</td><td>TCompanyCode</td><td>7</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3562.description.0"><td></td><td colspan="9">所引用公司（字段 3560）的可选 7 字母代码的纯文本值。</td></tr>
<tr data-field-id="3563"><td>@companyIdOverwrittenByChild</td><td>3563</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3563.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
</tbody></table>
<h3><a href="#appendix-tfileattributes" id="appendix-tfileattributes"></a>文件属性（TFileAttributes）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含关于整个文件的元信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3800"><td>@majorRelease</td><td>3800</td><td>202</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3800.description.0"><td></td><td colspan="9">每次重大更新时，主发布版本号加一，例如每两年一次。</td></tr>
<tr data-field-id="3805"><td>@minorRelease</td><td>3805</td><td>202</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3805.description.0"><td></td><td colspan="9">在两次重大更新之间，每次发布时次发布版本号加一。</td></tr>
<tr data-field-id="3810"><td>@majorRevision</td><td>3810</td><td>207</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3810.description.0"><td></td><td colspan="9">修订号针对每个数据集单独设定，独立于整个数据库的发布版本，用于区分数据库主／次发布版本内的数据集不同版本。主修订号反映数据集已接受变更的数量，只能随时间增加，不得手动更改。在 ecoinvent 上下文中，每当活动变更加入数据库（即通过审查流程后），主修订号都会增加，同时将次修订号重置为 1。</td></tr>
<tr data-field-id="3815"><td>@minorRevision</td><td>3815</td><td>207</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3815.description.0"><td></td><td colspan="9">次修订号描述数据集在提交审查前编辑过程中的版本。在 ecoinvent 上下文中，每当数据提供者将对数据集的修改保存到本地，或作为草稿保存到 ecoinvent 服务器时，次修订号都会自动增加。每当主修订号增加（即数据集变更被审查者接受）时，次修订号重置为“1”。</td></tr>
<tr data-field-id="3820"><td>@defaultLanguage</td><td>3820</td><td>new</td><td></td><td>string</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3820.description.0"><td></td><td colspan="9">该数据集所有多语言字段的默认语言。每个多语言字段至少应包含默认语言的值。如果未提供 defaultLanguage，则使用默认值（&quot;en&quot;）。</td></tr>
<tr data-field-id="3830"><td>@creationTimestamp</td><td>3830</td><td>204a</td><td>数据集创建时间。</td><td>dateTime</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3830.description.0"><td></td><td colspan="9">数据集创建时自动生成的日期。</td></tr>
<tr data-field-id="3840"><td>@lastEditTimestamp</td><td>3840</td><td>204b</td><td>数据集最后编辑时间。</td><td>dateTime</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3840.description.0"><td></td><td colspan="9">数据集保存时自动生成的日期。</td></tr>
<tr data-field-id="3850"><td>@internalSchemaVersion</td><td>3850</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3850.description.0"><td></td><td colspan="9">数据集基于此内部模式版本生成。</td></tr>
<tr data-field-id="3860"><td>@fileGenerator</td><td>3860</td><td>new</td><td></td><td>TBaseString255</td><td>255</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3860.description.0"><td></td><td colspan="9">对创建此文件的程序的描述，最好包含版本。</td></tr>
<tr data-field-id="3870"><td>@fileTimestamp</td><td>3870</td><td>new</td><td></td><td>dateTime</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3870.description.0"><td></td><td colspan="9">此文件创建的时间和日期。</td></tr>
<tr data-field-id="3880"><td>@contextId</td><td>3880</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3880.description.0"><td></td><td colspan="9">表示此数据集所面向的上下文。该信息例如用于将数据集信息的可访问性限制在一个特定上下文内，并确定访问它所需的主数据文件。如果省略此属性，则假定该数据集为独立数据集，且无法解析主数据引用以取得所引用内容。</td></tr>
<tr data-source-block="TFileAttributes.3880.description.1"><td></td><td colspan="9">上下文取代 ecoSpold01 的质量网络（字段 id 304）。ecoinvent 质量网络的上下文 ID 可在 Context.xml 主数据文件中找到。</td></tr>
<tr data-field-id="3885"><td>contextName</td><td>3885</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TFileAttributes.3885.description.0"><td></td><td colspan="9">字段 3880 所引用上下文的名称。</td></tr>
<tr data-source-block="TFileAttributes.3885.description.1"><td></td><td colspan="9">上下文取代 ecoSpold01 的质量网络（字段 id 304）。ecoinvent 质量网络的上下文 ID 可在 Context.xml 主数据文件中找到。</td></tr>
<tr data-field-id="3890"><td>requiredContext</td><td>3890</td><td>new</td><td></td><td>TRequiredContextReference</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3890.description.0"><td></td><td colspan="9">引用加载本文档所必需的上下文，以完整保留文档中的所有主数据引用。</td></tr>
</tbody></table>
<h3><a href="#appendix-trequiredcontextreference" id="appendix-trequiredcontextreference"></a>所需上下文引用（TRequiredContextReference）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>此类型用于指定：若要使用数据集引用的主数据读取该数据集，必须了解哪些上下文。</p>
<p>此类型可用于表明：读取该数据集需要来自不同上下文的主数据条目。读取数据集的软件必须识别这些上下文，并知道各上下文的实际主数据文件位于何处。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="7810"><td>@majorRelease</td><td>7810</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7810.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7820"><td>@minorRelease</td><td>7820</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7820.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7830"><td>@majorRevision</td><td>7830</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7830.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7840"><td>@minorRevision</td><td>7840</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7840.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7850"><td>@requiredContextId</td><td>7850</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7850.description.0"><td></td><td colspan="9">引用该主数据文件所属的上下文。</td></tr>
<tr data-source-block="TRequiredContextReference.7850.description.1"><td></td><td colspan="9">如果省略此属性，应改用数据集自身的上下文。</td></tr>
<tr data-field-id="7855"><td>requiredContextName</td><td>7855</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TRequiredContextReference.7855.description.0"><td></td><td colspan="9">字段 7850 所引用上下文的名称。</td></tr>
<tr data-field-id="7860"><td>@requiredContextFileLocation</td><td>7860</td><td>new</td><td></td><td>anyURI</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7860.description.0"><td></td><td colspan="9">指向包含此上下文主数据文件的目录的可选 URI 引用。</td></tr>
</tbody></table>
