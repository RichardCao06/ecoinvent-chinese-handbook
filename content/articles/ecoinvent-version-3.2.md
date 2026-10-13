# ecoinvent 第 3.2 版

英文原题：ecoinvent Version 3.2  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.2)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.2 于 2015 年 11 月发布，进一步更新电力部门，提供冷藏运输数据，并为多个部门增加新的国际数据。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.2 于 2015 年 11 月 30 日发布</strong>。了解如何[升级至我们的最新版本](licensing.md)。

2023 年 10 月 24 日

它还为地区、国家和产品引入市场组。

为确保清晰透明，我们公开记录数据库最新更新与上一版本之间的变更。因此，每个数据库版本均提供多种文件，记录并解释所作变更，包括详细的变更报告、对应关系文件，以及列出各版本全部活动的文件。此外，我们记录各版本的所有已知问题，提醒数据库用户，并支持其理解和使用数据库。

### 新增及更新数据 <a href="#zh-b0007" id="zh-b0007"></a>

### 电力 <a href="#zh-b0008" id="zh-b0008"></a>

#### 电力部门全面更新 <a href="#zh-b0009" id="zh-b0009"></a>

ecoinvent 第 3.0 版发布时增加了全球各国的电力生产数据。得益于保罗谢勒研究所（PSI）的大量工作，第 3.2 版使用最新电网组合和可获得的最新电力生产数据，再次更新电力部门。此次更新涉及 2,200 多个数据集，覆盖 56 个国家，占全球电力生产的 89%。所有技术的年度产量均已更新，意味着 ecoinvent 3.2 采用最新电力组合数据。此外，还纳入新的技术，例如硬煤、褐煤、燃油和天然气电厂的热电联产（CHP），以及新的地热发电技术。此次更新不仅覆盖现有电力区域，还通过增加冰岛和爱沙尼亚等国家提供更详细信息。此外，新增的电力市场组将 UCTE、ENTSO-E、亚洲或美国等较大区域的电力组合合并到一个数据集中，使使用更方便。下文进一步说明这一新功能。

#### 中国 32 个地区的电力数据 <a href="#zh-b0011" id="zh-b0011"></a>

中国是世界人口最多的国家，快速增长的经济使其成为世界最大的能源消费者和生产者。第 3.2 版包含中国 32 个地区的电力生产数据，以及中国不同电网和全国整体的组合。这些数据详细说明中国各地区电力生产环境影响的差异。

#### 运输 <a href="#zh-b0013" id="zh-b0013"></a>

如今，商品和食品的全球贸易日益增加，即使是易腐商品也不例外。第 3.2 版通过纳入冷藏运输数据回应这一需求。冷藏运输覆盖所有不同运输方式：船舶、火车、飞机和卡车。

#### 市场组 <a href="#zh-b0015" id="zh-b0015"></a>

第 3.2 版新增市场组，这是一种便于阅读和修改数据集的新数据集类型。市场组针对部分地区、国家和产品提供。例如，若希望了解 UCTE、ENTSO-E 区域或整个大洲的电力组合，可在市场组数据集中查找。这样，经常一起使用的电力组合等被分组，便于使用。

#### 新增国际数据 <a href="#zh-b0017" id="zh-b0017"></a>

除上述新增内容外，第 3.2 版还增加水泥、木材及废物处理领域的新数据。尤其值得关注的是欧洲铝生产数据集，它们在欧洲铝业协会（EAA）支持下得到更新。

### 相关文档与文件 <a href="#zh-b0019" id="zh-b0019"></a>

#### 变更报告 <a href="#zh-b0020" id="zh-b0020"></a>

该报告涵盖 ecoinvent 数据库从第 3.1 版（2014）到第 3.2 版（2015）的全部变更，既反映全数据库变更，也反映各部门的特定变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/a47d793d0077-report_of_changes_v3_2-1.pdf)

#### 变更报告 <a href="#zh-b0023" id="zh-b0023"></a>

这份自动生成的 Excel 文件概述 ecoinvent 数据库第 3.1 版与第 3.2 版之间未指定系统模型的单元过程数据集变更。变更报告 XLS 文件可在 ecoinvent 数据库第 3 版在线平台 ecoQuery 的“文件”（Files）栏目中找到，供数据库许可证持有者使用。

#### 对应关系文件 <a href="#zh-b0025" id="zh-b0025"></a>

对应关系文件是一份电子表格，列出第 3.1 版和第 3.2 版的全部数据集，并匹配版本间的对应数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件](../assets/573bb7ab7642-ecoinvent_correspondence_file_eiv3_1_to_eiv3_2_updated20151214_2-3.xlsx)

#### ecoinvent 第 3.2 版活动概览：未指定系统模型 <a href="#zh-b0028" id="zh-b0028"></a>

一份 Excel 文件，列出 ecoinvent 第 3.2 版数据库的所有活动和产品，以及大部分元数据（地理区域、ISIC 分类、活动类型、技术水平、产品类型、单位等）。文件还包含数据库内所有地理区域、基本流交换和中间交换的清单。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.2 活动概览：未指定系统模型](../assets/0a4b53555649-activity_overview_for_users_3.2_undefined_20160901-4.xlsx)

#### ecoinvent 第 3.2 版活动概览：APOS <a href="#zh-b0031" id="zh-b0031"></a>

一份 Excel 文件，列出 ecoinvent 第 3.2 版数据库的所有活动，以及替代点分配模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.2 活动概览：APOS](../assets/c05b16833b90-activity_overview_for_users_3.2_apos-2.xlsx)

#### ecoinvent 第 3.2 版活动概览：Consequential <a href="#zh-b0034" id="zh-b0034"></a>

一份 Excel 文件，列出数据库的所有活动，以及长期后果型替代系统模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.2 活动概览：Consequential](../assets/432123773d3d-activity_overview_for_users_3.2_consequential-2.xlsx)

#### ecoinvent 第 3.2 版活动概览：Cut-Off <a href="#zh-b0037" id="zh-b0037"></a>

一份 Excel 文件，列出数据库的所有活动，以及按分类截断的分配系统模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.2 活动概览：Cut-Off](../assets/49316d902abd-activity_overview_for_users_3.2_cut-off-1.xlsx)

#### ecoinvent 第 3.2 版的 LCIA 方法 <a href="#zh-b0040" id="zh-b0040"></a>

列出所有 LCIA 方法及其全部影响类别，以及 ecoinvent 提供的部分累积 LCI 结果清单。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.2 的 LCIA 方法](../assets/0324a3eb9240-list_of_methods_and_indicators_ecoinvent_v3.2-2.xlsx)

### 已知问题 <a href="#zh-b0043" id="zh-b0043"></a>

本栏目列出 ecoinvent 数据库第 3.2 版所有已知数据错误。

#### 数据问题 <a href="#zh-b0045" id="zh-b0045"></a>

- 在后果型系统模型中，以下 4 个受约束市场没有收到边际供应商输入：market for residual hardwood, wet；market for residual softwood, wet；market for residual wood, dry；market for venting of nitrogen, liquid；market for ground granulated blast furnace slag。

- 在后果型系统模型中，RoW 的“market for hydrogen, liquid”不存在，原本链接至该市场的消费活动收到的“hydrogen, liquid”数量为 0。
- 遵循溶液中化学品的规则，下列活动移除了溶剂／水输入：alkyd paint production, white, solvent-based, product in 60% solution state；alkyd paint production, white, water-based, product in 60% solution state；alkyd resin production, long oil, product in 70% white spirit solution state；printing ink production, offset, product in 47.5% solution state；printing ink production, rotogravure, product in 55% toluene solution state。
- 遗憾的是，需求下列所得产品的活动也缺少相应溶剂／水输入：alkyd paint, white, without solvent, in 60% solution state；alkyd paint, white, without water, in 60% solution state；alkyd resin, long oil, without solvent, in 70% white spirit solution state；printing ink, offset, without solvent, in 47.5% solution state；printing ink, rotogravure, without solvent, in 55% toluene solution state。
- v3.2 的“market for copper”存在失真。其供应来自 DE 和 GLO 的“copper production, from imported concentrates”活动，前者从 v2.2 转换而来，后者自动生成。这些活动原本不应生产“copper”，正在工作中的未指定系统模型数据库中修正并重命名（可通过 ecoEditor 访问）。下一次计算数据库版本发布（v3.3，计划于 2016 年）将包含修正后的活动和市场。希望在 v3.2 使用“market for copper”的用户可按以下方式修正：编辑市场，删除来自“copper production, from imported concentrates”（DE 和 GLO）的“copper”交换；提高其他生产者的相对贡献，使其覆盖 100% 市场份额。

对于存在市场组的产品，所有 RoW 活动均从 GLO 市场组获得供应。在某些情况下，尤其本地消费者较多时，这可能导致较大错误。该问题将在 ecoinvent 3.3 中修正。

{% endtab %}

{% tab title="English 原文" %}

## ecoinvent v3.2 was released in November 2015. This release provided a further update of the electricity sector, data on refrigerated transport and new international data for several sectors. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.2 was released on November 30th, 2015</strong>. Discover how to [upgrade to our latest version](licensing.md).

Oct 24th, 2023

It also introduced market groups for regions, countries and products.

As we wish to ensure clarity and transparency, we openly document the changes made between the latest update and the previous version of the database. Therefore, we offer various files that document and clarify the changes that have been made with each version of the database. These include detailed the report of changes, correspondence files, as well as files that include all activities of each version. Further, we document all known issues of each version to alert database users and to support their understanding and use of the database.

### New and Updated Data <a href="#en-b0007" id="en-b0007"></a>

### Electricity <a href="#en-b0008" id="en-b0008"></a>

#### Complete Update of the Electricity Sector <a href="#en-b0009" id="en-b0009"></a>

With the release of ecoinvent version 3.0, electricity production data for countries from all over the world were added. Thanks to extensive work from the Paul Scherrer Institute (PSI), version 3.2 features another update of the electricity sector using the newest grid mixes and the latest available data on electricity production. The update includes over 2,200 datasets, covering 89% of the world’s electricity production in 56 countries. The annual production volumes for all technologies were updated, which means ecoinvent 3.2 now uses the latest electricity mix data. Moreover, new technologies such as combined heat & power (CHP) production for hard coal, lignite, oil and natural gas plants as well as new geothermal generation are now also included. The update did not only cover the existing electricity regions but further detail was provided by adding countries, such as Iceland and Estonia. Additionally, the addition of market groups for electricity provides more ease of use by combining the electricity mixes for bigger regions in one dataset, such as UCTE, ENTSO-E, Asia, or the USA. More details on this new feature is provided below.

#### Electricity Data for 32 Chinese Regions <a href="#en-b0011" id="en-b0011"></a>

China is the world’s most populous country with a fast-growing economy that has led it to be the largest energy consumer and producer in the world. Version 3.2 includes electricity production data for 32 Chinese regions, as well as mixes for different grids within China and for China as a whole. This data offers detailed information on the differences in environmental impacts of the electricity production of all Chinese regions.

#### Transport <a href="#en-b0013" id="en-b0013"></a>

Nowadays goods and foodstuffs are increasingly traded on a global scale, even if they are easily perishable. Version 3.2 addresses this demand by including data on refrigerated transport. The refrigerated transport is available for all different modes of transport: ship, train, aircraft and truck.

#### Market Groups <a href="#en-b0015" id="en-b0015"></a>

Version 3.2 features market groups, a new type of dataset that facilitates readability and modifying datasets. Market groups exist for a selection of regions, countries and products. If you are, for example, interested in knowing the electricity mixes for the regions of UCTE, ENTSO-E or whole continents, you can find that information in the market group dataset. In this way e.g. electricity mixes that are commonly used together are grouped for ease of use and convenience.

#### New International Data <a href="#en-b0017" id="en-b0017"></a>

Besides the above-mentioned additions, version 3.2 also features new data in the areas of the cement, wood and waste treatment. Especially noteworthy are the European aluminium production datasets which were updated with the support of the European Aluminium Association (EAA).

### Relevant Documents and Files <a href="#en-b0019" id="en-b0019"></a>

#### Report of Changes <a href="#en-b0020" id="en-b0020"></a>

This report covers all changes made in the ecoinvent database between version 3.1 (2014) and version 3.2 (2015). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/a47d793d0077-report_of_changes_v3_2-1.pdf)

#### Report of changes <a href="#en-b0023" id="en-b0023"></a>

This automatically generated excel file provides an overview of changes made on the undefined unit process datasets between versions 3.1 and 3.2 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### Correspondence File <a href="#en-b0025" id="en-b0025"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.1 and 3.2 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File](../assets/573bb7ab7642-ecoinvent_correspondence_file_eiv3_1_to_eiv3_2_updated20151214_2-3.xlsx)

#### Activity Overview for ecoinvent Version 3.2, Undefined <a href="#en-b0028" id="en-b0028"></a>

An excel file listing all the activities and products present in the ecoinvent version 3.2 database including most of the metadata (geography, ISIC classification, activity type, technology level, product type, unit, etc.). This file also includes a list of all geographies, elementary and intermediate exchanges present in the database.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.2, Undefined](../assets/0a4b53555649-activity_overview_for_users_3.2_undefined_20160901-4.xlsx)

#### Activity Overview for ecoinvent Version 3.2, APOS <a href="#en-b0031" id="en-b0031"></a>

An excel file listing all the activities present in the ecoinvent version 3.2 database including metadata related specifically to the Allocation at the point of substitution.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.2, APOS](../assets/c05b16833b90-activity_overview_for_users_3.2_apos-2.xlsx)

#### Activity Overview for ecoinvent Version 3.2, Consequential <a href="#en-b0034" id="en-b0034"></a>

An excel file listing all the activities preesent in the database including metadata related specifically to the Substitution, consequential, long-term system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.2, Consequential](../assets/432123773d3d-activity_overview_for_users_3.2_consequential-2.xlsx)

#### Activity Overview for ecoinvent Version 3.2, Cut-Off <a href="#en-b0037" id="en-b0037"></a>

An excel file which lists all the activities present in the database including metadata related specifically to the Allocation, cut-off by classification system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.2, Cut-Off](../assets/49316d902abd-activity_overview_for_users_3.2_cut-off-1.xlsx)

#### LCIA Methods in ecoinvent Version 3.2 <a href="#en-b0040" id="en-b0040"></a>

List of all LCIA methods including all the impact categories as well as list of selected LCI cumulative results provided by ecoinvent.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [LCIA Methods in ecoinvent v3.2](../assets/0324a3eb9240-list_of_methods_and_indicators_ecoinvent_v3.2-2.xlsx)

### Known Issues <a href="#en-b0043" id="en-b0043"></a>

This section lists all known data errors in version 3.2 of the ecoinvent database.

#### Data issues <a href="#en-b0045" id="en-b0045"></a>

- In the consequential system model, the following 4 constrained markets receive no input from their marginal supplier: market for residual hardwood, wet; market for residual softwood, wet; market for residual wood, dry; market for venting of nitrogen, liquid; market for ground granulated blast furnace slag

- In the consequential system model, the “market for hydrogen, liquid” RoW is not present, and consumer activities originally linking to this market receive a 0 amount of “hydrogen, liquid”.
- The following activities had the input of solvent/water removed, following the rule of chemicals in solution: alkyd paint production, white, solvent-based, product in 60% solution state; alkyd paint production, white, water-based, product in 60% solution state; alkyd resin production, long oil, product in 70% white spirit solution state; printing ink production, offset, product in 47.5% solution state; printing ink production, rotogravure, product in 55% toluene solution state.
- Unfortunately, the demanding activities of the resulting products (listed below) also lack this input of solvent/water: alkyd paint, white, without solvent, in 60% solution state; alkyd paint, white, without water, in 60% solution state; alkyd resin, long oil, without solvent, in 70% white spirit solution state; printing ink, offset, without solvent, in 47.5% solution state; printing ink, rotogravure, without solvent, in 55% toluene solution state.
- The “market for copper” is distorted in v3.2. It is supplied by the activities “copper production, from imported concentrates” DE and GLO, which were converted from v2.2, and generated automatically respectively. Those activities were not intended to produce “copper” and are already being corrected and renamed in the working version of the Undefined database (accessible through the ecoEditor). The next release of the calculated database (v3.3, scheduled for 2016) will contain the corrected activities and the corrected market. The users which want to use the “market for copper” in v3.2 can correct it the following way: edit the market and remove “copper” exchanges coming from “copper production, from imported concentrates” (DE and GLO); increase the relative contribution of the other producers to cover 100% market share.

For the products where market groups exist, all RoW activities are getting their supply from GLO market groups. This can lead to big errors in some cases, specially when there are many local consumers. This is corrected for the ecoinvent 3.3.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0046**：原文声称 4 个市场，实际列出 5 个市场名称。 保留原文数量和全部名称，请专家核实应为 5 个还是清单中有误。 [查看完整记录](../review/issues.md#issue-051)
- **已处理／已说明 · b0010**：统一指南规定的产量术语。 已将生产量改为产量。 [查看完整记录](../review/issues.md#issue-052)
