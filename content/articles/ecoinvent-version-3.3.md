# ecoinvent 第 3.3 版

英文原题：ecoinvent Version 3.3  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.3)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent 第 3.3 版于 2016 年发布，通过引入 WFLDB 的数百个新农业数据集扩展了数据库覆盖范围。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.3 于 2016 年 8 月 16 日发布</strong>。了解如何[升级至我们的最新版本](licensing.md)。

2023 年 10 月 24 日

此外，它还对数据库作出重要的整体改进，包括为所有产品增加价格、为各数据集提供 PDF 文档，以及引入 ILCD 方法、CPC 分类等。

为确保清晰透明，我们公开记录数据库最新更新与上一版本之间的变更。因此，每个数据库版本均提供多种文件，记录并解释所作变更，包括详细的变更报告、对应关系文件，以及列出各版本全部活动的文件。此外，我们记录各版本的所有已知问题，提醒数据库用户，并支持其理解和使用数据库。

### 新增及更新数据 <a href="#zh-b0007" id="zh-b0007"></a>

#### 种类丰富的新数据 <a href="#zh-b0008" id="zh-b0008"></a>

第 3.3 版纳入的首批 WFLDB 数据包含数百个新农业数据集，涉及的领域包括：

- 蔬菜（如芦笋、胡萝卜、洋葱、马铃薯）
- 水果（如柠檬、柑橘、橙、桃）
- 谷物及谷物产品（如燕麦、稻米、甜玉米、小麦）
- 茶
- 咖啡（如罗布斯塔和阿拉比卡）
- 糖及糖果原料（如可可和香草）

#### 技术与类别的区分 <a href="#zh-b0016" id="zh-b0016"></a>

对于许多产品，您可以选择不同国家、不同技术的生产。例如，草莓生产可选择露地、无加温温室，甚至加温温室。

此外，还区分鲜食品级和加工品级。

### 全数据库更新 <a href="#zh-b0019" id="zh-b0019"></a>

#### 所有产品的价格 <a href="#zh-b0020" id="zh-b0020"></a>

ecoinvent v3.3 为数据库所有产品（废物材料及其处置除外）提供价格数据。价格从文献、生产者直接收集，或依据进入活动的输入材料计算。这是提高数据库一致性和可靠性的重要一步，但部分价格数据仍有较大不确定性。不过，这些价格可用于经济分配、生命周期成本核算或处理社会 LCA 数据。

#### 改进市场和供应链 <a href="#zh-b0022" id="zh-b0022"></a>

部分部门通过更具体的本地数据改进了供应链。最主要的例子是欧洲和瑞士的废物处理活动，以及瑞士特定的供应链。

#### 每个数据集的 PDF 文档 <a href="#zh-b0024" id="zh-b0024"></a>

全面且易于获取的文档，对于在具体背景中更好地理解所用数据集至关重要。ecoinvent 第 3 版的一项重要进步是在数据集中直接纳入更多信息。虽然软件工具自行决定如何显示 ecoinvent 数据，我们现在为每个数据集提供 PDF 格式文档。该 PDF 包含单元过程信息及部分关键影响评价结果，使所有用户更容易获取 ecoinvent 数据集信息。

### 相关文档与文件 <a href="#zh-b0026" id="zh-b0026"></a>

#### 变更报告 <a href="#zh-b0027" id="zh-b0027"></a>

该报告涵盖 ecoinvent 数据库从第 3.2 版（2015）到第 3.3 版（2016）的全部变更，既反映全数据库变更，也反映各部门的特定变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/e7560598d4c4-change_report_v3_3_final.pdf)

#### 变更报告 <a href="#zh-b0030" id="zh-b0030"></a>

这份自动生成的 Excel 文件概述 ecoinvent 数据库第 3.2 版与第 3.3 版之间未指定系统模型的单元过程数据集变更。变更报告 XLS 文件可在 ecoinvent 数据库第 3 版在线平台 ecoQuery 的“文件”（Files）栏目中找到，供数据库许可证持有者使用。

#### 对应关系文件 <a href="#zh-b0032" id="zh-b0032"></a>

对应关系文件是一份电子表格，列出第 3.2 版和第 3.3 版的全部数据集，并匹配版本间的对应数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件](../assets/bddd19095e1e-ecoinvent_correspondence_file_eiv3.2_to_eiv3.3.xlsx)

#### ecoinvent 第 3.3 版活动概览：未指定系统模型 <a href="#zh-b0035" id="zh-b0035"></a>

一份 Excel 文件，列出 ecoinvent 第 3.3 版数据库的所有活动和产品，以及大部分元数据（地理区域、ISIC 分类、活动类型、技术水平、产品类型、单位等）。文件还包含数据库内所有地理区域、基本流交换和中间交换的清单。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.3 活动概览：未指定系统模型](../assets/2222ed0f26e2-activity_overview_for_users_3.3_undefined_1-1.xlsx)

#### ecoinvent 第 3.3 版活动概览：APOS <a href="#zh-b0038" id="zh-b0038"></a>

一份 Excel 文件，列出 ecoinvent 第 3.3 版数据库的所有活动，以及替代点分配模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.3 活动概览：APOS](../assets/75b961b9d93a-activity_overview_for_users_3.3_apos.xlsx)

#### ecoinvent 第 3.3 版活动概览：Consequential <a href="#zh-b0041" id="zh-b0041"></a>

一份 Excel 文件，列出数据库的所有活动，以及长期后果型替代系统模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.3 活动概览：Consequential](../assets/dd7bf50d86ae-activity_overview_for_users_3.3_consequential.xlsx)

#### ecoinvent 第 3.3 版活动概览：Cut-Off <a href="#zh-b0044" id="zh-b0044"></a>

一份 Excel 文件，列出数据库的所有活动，以及按分类截断的分配系统模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.3 活动概览：Cut-Off](../assets/1a12c0309c91-activity_overview_for_users_3.3_cut-off.xlsx)

#### ecoinvent 第 3.3 版的 LCIA 方法 <a href="#zh-b0047" id="zh-b0047"></a>

列出所有 LCIA 方法及其全部影响类别，以及 ecoinvent 提供的部分累积 LCI 结果清单。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.3 的 LCIA 方法](../assets/36b677e15ef1-list_of_methods_and_indicators_ecoinvent_v3.3.xlsx)

### 已知问题 <a href="#zh-b0050" id="zh-b0050"></a>

本栏目列出 ecoinvent 数据库第 3.3 版所有已知数据错误。ecoinvent 团队致力于在后续更新中消除这些错误；本已知问题栏目旨在提醒用户，并支持其理解和使用数据库。

#### 数据问题 <a href="#zh-b0052" id="zh-b0052"></a>

- “cotton production”活动（GLO、US 和 CN）的电力输入存在错误：数值表示 MJ 单位的数量，未转换为 kWh。目前正在修正，将于 ecoinvent 第 3.4 版发布时更新。
- 铝铸造似乎存在能源消耗相关错误。我们正在调查，将尽快提供全部细节并修正。
- GLO 的“sheep production, for meat”活动由 US 地理区域的同一活动复制创建。复制时重新计算了参考产品数量，但其他交换保持不变。US 与 GLO 绵羊活重的差异是正确的。此类数据可在 [faostat](https://www.fao.org/faostat/en/#data/QCL) 网站“livestock primary”的“yield”数据栏目中获取。然而，GLO 数据集的交换相对于参考产品而言不正确。用户应使用 US 数据集，并注意：若关注的地理区域不是 US，应审查这些交换在研究范围内的适用性。
- US 的“natural gas production”活动似乎存在一些错误。我们正在调查，将尽快提供全部细节并修正。
- CH 和 GLO 两个地理区域的“anaerobic digestion of manure”活动均存在质量不平衡。所产消化污泥数量过高，目前正在修正。过量消化污泥导致后果型系统模型中某些地理区域的电力出现负温室气体排放。该错误正在修正，将于 ecoinvent 第 3.4 版发布时更新。
- “electrolysis of lithium chloride, GLO, 2006”活动的电力输入计算不准确。该数据集将依据其引用来源的信息，在数据库第 3.4 版中修正。此类过程及技术每生产 kg 锂的电力输入范围为 28 至 32 kWh。28 与 32 kWh 的平均值为 30。由于该过程产出 0.15 kg 锂，电力输入按此缩放（每 kg 锂 30 kWh 乘以 0.15 kg 锂，得到 4.5 kWh）。

#### 说明显示问题 <a href="#zh-b0059" id="zh-b0059"></a>

- 活动名称为“electricity production, natural gas, combined cycle power plant”的数据集，其一般说明元素包含以“[‘text’, ‘”开头、以“‘]”结束的文本。删除这两个字符串即可解决问题。
- 部分电力或热电联产数据集还有另一种一般说明显示问题。例如说明显示为“”，应替换为数据提供方指定的字符串。如需受影响数据集清单及应采用的字符串内容，请[联系我们](https://ecoinvent.org/contact-us/)。

#### 后果型系统模型问题 <a href="#zh-b0062" id="zh-b0062"></a>

- “social”环境区室中存在三个基本流交换。由于 ecoinvent 尚未核算社会影响，在单元过程和清单层级均可忽略这些交换。
- 下表展示了某些数据集对指定供应活动并未提供的产品提出需求的情况。可忽略这两项交换。

### LCIA 方法实施问题 <a href="#zh-b0065" id="zh-b0065"></a>

#### Ecological Scarcity 2013 <a href="#zh-b0066" id="zh-b0066"></a>

- 该方法要求对采矿作业所开采材料的“耗散性使用”进行表征。这意味着该影响类别的表征因子应应用于考虑部分所采材料可能再利用或回收利用后的数量。ecoinvent 数据库不便直接计算该数量。目前 ecoinvent 在此类别计算的得分并不代表该方法的原本意图。这些得分在 LCA 中仍有用，但不应直接用于得出有关供应链这一特定方面的结论。在作出任何结论之前，应评价对得分贡献最大的材料的回收和再利用率。
- 该方法要求对水的“耗散性使用”进行表征。对蒸发进入大气的水应用表征因子，可较好体现这一要求，并代表 ecoinvent 大多数数据集中 100% 的耗散水。不过，水在发生化学反应时也会耗散，例如混凝土和混凝土的情况。如果所研究系统包含大量水泥或混凝土，ecoinvent 的实施方式可能低估水影响得分。
- 排入工业土壤的金属应按零表征，因为该方法不假定其转移至水体或通过其他机制被摄入。此外，地下水、长期地下水和海洋子区室没有二噁英水排放的法定限值，因此其表征因子也应为零。以下交换目前被错误表征。

{% endtab %}

{% tab title="English 原文" %}

## ecoinvent version 3.3 was released in 2016 and expanded the coverage of the database with several hundreds of new agricultural datasets from the WFLDB. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.3 was released on August 16th, 2016</strong>. Discover how to [upgrade to our latest version](licensing.md).

Oct 24th, 2023

Moreover, it included important overall improvements to the database, including the addition of prices for all products, pdf documentations per dataset, the ILCD method, the CPC classification among other things.

As we wish to ensure clarity and transparency, we openly document the changes made between the latest update and the previous version of the database. Therefore, we offer various files that document and clarify the changes that have been made with each version of the database. These include detailed the report of changes, correspondence files, as well as files that include all activities of each version. Futrher, we document all known issues of each version to alert database users and to support their understanding and use of the database.

### New and Updated Data <a href="#en-b0007" id="en-b0007"></a>

#### Large Variety of New Data <a href="#en-b0008" id="en-b0008"></a>

The first part of the WFLDB being included in version 3.3 covers several hundreds of new agricultural datasets, amongst other in the fields of:

- vegetables (such as asparagus, carrots, onions, potatoes)
- fruits (such as lemons, mandarins, oranges, peaches)
- cereal and grain products (such as oat, rice, sweetcorn, wheat)
- tea
- coffee (such as Robusta and Arabica)
- sugar and confectionery (such as cocoa and vanilla)

#### Distinction Between Technologies and Categories <a href="#en-b0016" id="en-b0016"></a>

For many products you can choose production in different countries and using different technologies. So you can, for example, choose between strawberry production in the open field, non-heated greenhouse or even in heated greenhouse.

Furthermore, a distinction is made between fresh grade and processing grade.

### Database Wide Updates <a href="#en-b0019" id="en-b0019"></a>

#### Prices for all Products <a href="#en-b0020" id="en-b0020"></a>

In ecoinvent v3.3, price data is available for all the products (except for waste materials and their disposal) in the database. These prices were collected from literature, directly from the producers or calculated based on the input materials entering the activity. While this is a significant step towards a more consistent and reliable database, some price data are quite uncertain still. Nevertheless, these prices can be used for economic allocation, life cycle costing or when working with social LCA data.

#### Improved Markets and Supply Chains <a href="#en-b0022" id="en-b0022"></a>

Some sectors have had their supply chains improved with more specific, local data. The largest examples are waste treatment activities in Europe and Switzerland, and supply chains specifically in Switzerland.

#### PDF Documentation of Every Dataset <a href="#en-b0024" id="en-b0024"></a>

Comprehensive and easy to access documentation is vital to better understand the dataset you are working with in context. One of the major steps in ecoinvent version 3 was to include more information directly in the dataset. While software tools decide themselves how to display ecoinvent data, we now offer the dataset documentation in a pdf file for every dataset. This pdf contains both unit process information as well as some key impact assessment results, which makes the information in ecoinvent datasets more accessible for all our users.

### Relevant Documents and Files <a href="#en-b0026" id="en-b0026"></a>

#### Report of Changes <a href="#en-b0027" id="en-b0027"></a>

This report covers all changes made in the ecoinvent database between version 3.2 (2015) and version 3.3 (2016). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/e7560598d4c4-change_report_v3_3_final.pdf)

#### Report of Changes <a href="#en-b0030" id="en-b0030"></a>

This automatically generated excel file provides an overview of changes made on the undefined unit process datasets between versions 3.2 and 3.3 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### Correspondence File <a href="#en-b0032" id="en-b0032"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.2 and 3.3 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File](../assets/bddd19095e1e-ecoinvent_correspondence_file_eiv3.2_to_eiv3.3.xlsx)

#### Activity Overview for ecoinvent Version 3.3, Undefined <a href="#en-b0035" id="en-b0035"></a>

An excel file listing all the activities and products present in the ecoinvent version 3.3 database including most of the metadata (geography, ISIC classification, activity type, technology level, product type, unit, etc.). This file also includes a list of all geographies, elementary and intermediate exchanges present in the database.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.3, Undefined](../assets/2222ed0f26e2-activity_overview_for_users_3.3_undefined_1-1.xlsx)

#### Activity Overview for ecoinvent Version 3.3, APOS <a href="#en-b0038" id="en-b0038"></a>

An excel file listing all the activities present in the ecoinvent version 3.3 database including metadata related specifically to the Allocation at the point of substitution.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.3, APOS](../assets/75b961b9d93a-activity_overview_for_users_3.3_apos.xlsx)

#### Activity Overview for ecoinvent Version 3.3, Consequential <a href="#en-b0041" id="en-b0041"></a>

An excel file listing all the activities present in the database including metadata related specifically to the Substitution, consequential, long-term system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.3, Consequential](../assets/dd7bf50d86ae-activity_overview_for_users_3.3_consequential.xlsx)

#### Activity Overview for ecoinvent Version 3.3, Cut-Off <a href="#en-b0044" id="en-b0044"></a>

An excel file which lists all the activities present in the database including metadata related specifically to the Allocation, cut-off by classification system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.3, Cut-Off](../assets/1a12c0309c91-activity_overview_for_users_3.3_cut-off.xlsx)

#### LCIA Methods in ecoinvent Version 3.3 <a href="#en-b0047" id="en-b0047"></a>

List of all LCIA methods including all the impact categories as well as list of selected LCI cumulative results provided by ecoinvent.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [LCIA Methods in ecoinvent v3.3](../assets/36b677e15ef1-list_of_methods_and_indicators_ecoinvent_v3.3.xlsx)

### Known Issues <a href="#en-b0050" id="en-b0050"></a>

This section lists all known data errors in version 3.3 of the ecoinvent database. While the ecoinvent team focuses on eliminating such errors for upcoming updates, this section of known issues exists to alert database users and to support their understanding and use of the database.

#### Data Issues <a href="#en-b0052" id="en-b0052"></a>

- The activity “cotton production” (GLO, US and CN) contains an error related to the electricity input. The value represents the amount in MJ, missing the conversion to kWh. The error is currently subjected to correction and will be updated for the release of ecoinvent version 3.4.
- The casting of aluminium seems to contain an error related to energy consumption. We are investigating this issue and will give all details, and fix it as soon as possible.
- The activity “sheep production, for meat” GLO was created as copy of the same activity for the geography US. When this was done the amount of reference product was recalculated but the other exchanges were left unchanged. The difference between the live weight of US versus GLO sheep is correct. It is possible to access this type of data on the [faostat](https://www.fao.org/faostat/en/#data/QCL) website, in the data section for “yield” of “livestock primary”. Nevertheless the exchanges for the GLO dataset are incorrect in relation to the reference product. Users should use the US dataset, keeping in mind that if their geography of interest is not US they should look into the validity of the exchanges for the scope of their study.
- The activity “natural gas production” US seems to contain some errors. We are investigating this issue and will give all details, and fix it as soon as possible.
- The activity “anaerobic digestion of manure” for both geographies CH and GLO are mass imbalanced. The amount of digester sludge produced is too high and it is now under correction. The excess amount of digester sludge is responsible for negative GHG emissions for electricity in certain geographies in the consequential system model. The error is currently subjected to correction and will be updated for the release of ecoinvent version 3.4.
- The activity “electrolysis of lithium chloride, GLO, 2006” contains an inaccurate calculation related to its electricity input. The datasets will be corrected for version 3.4 of the database based on the information reported in the source cited in the dataset. The electricity input for this type of process and technology ranges from 28 to 32 kWh per kg of lithium produced. 30 is the average of 28 and 32 kWh. Given the fact that the process yields 0.15 kg of lithium the electricity input was scaled accordingly (30 kWh per kg lithium times 0.15 kg of lithium yields 4.5 kWh).

#### Comment Display Issues <a href="#en-b0059" id="en-b0059"></a>

- In the datasets with activity name “electricity production, natural gas, combined cycle power plant”, the general comment elements contain the following string of text: “[‘text’, ‘”, ending with “‘]”. The issue can be solved by removing these two character strings.
- Some electricity or combined heat and electricity production datasets have another general comment display problem. Comments display for example “”, which should be replaced by a string of character specified by the data provider. For a list of affected datasets and the value these character string should take, please [contact us](https://ecoinvent.org/contact-us/).

#### Consequential System Model Issues <a href="#en-b0062" id="en-b0062"></a>

- Three elementary exchanges are found in the compartment “social”. These exchanges can be ignored, both at the unit process and the inventory level, as ecoinvent does not yet account for social impacts.
- The table below shows dataset making a demand of a product that is not supplied by the specified supplying activity. These two exchanges can be ignored.

### LCIA Method Implementation Issues <a href="#en-b0065" id="en-b0065"></a>

#### Ecological Scarcity 2013 <a href="#en-b0066" id="en-b0066"></a>

- The method calls for the characterization of the “dissipative use” of material extracted by mining operation. This means that the CFs in this impact category should be applied to amounts of taking into account that a fraction of the extracted material may be reused or recycled. The ecoinvent database does not allow to calculate easily this quantity. The scores currently calculated by ecoinvent in this category do not represent what the method intends. These scores are nevertheless useful in an LCA, but should not be used directly to support conclusion about this particular aspect of a supply chain. Rates of recycling and reuse of the material with the highest contribution to the score should be assessed before reaching any conclusion.
- The method calls for the characterization of the “dissipative use” of water. This is well captured by implementing the CF for evaporated water to air, and represents 100% of the dissipated water in the majority of the datasets in ecoinvent. However, water is also dissipated when it chemically reacts, for example in the case of concrete and concrete. If large quantity of cement or concrete are included in the system at hand, it is possible that the water impact score be underestimated by the implementation proposed by ecoinvent.
- Emissions of metal to the industrial soil should be zero, as they the method does not assume transfer to water and ingestion through other mechanism. Also, there is no legal limit of dioxins to water in the subcompartment groundwater, groundwater long term and ocean, so their CFs should have been zero. The exchanges below are currently wrongly characterised.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0068**：原文重复写 concrete and concrete，可能原应为 cement and concrete。译文未凭猜测替换材料名称。 专家核实原文应指水泥与混凝土还是仅混凝土。 [查看完整记录](../review/issues.md#issue-053)
