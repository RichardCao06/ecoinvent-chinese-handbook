# ecoinvent 第 3.0 版

英文原题：ecoinvent Version 3.0  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.0)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.0 于 2013 年 5 月发布，是 ecoinvent 数据库第三次主要版本发布。数据库第 3 版提供了多项令人期待的新功能，以及新增和更新的数据集。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.0 于 2013 年 5 月 6 日发布</strong>。了解如何[升级到我们的最新版本](licensing.md)。

2023 年 10 月 16 日

ecoinvent 于 2013 年 9 月 4 日发布了错误修复版 3.01。ecoinvent v3.01 纠正了第 3.0 版中的部分错误，并取代该版本。这些修改优化了数据库的使用和准确性。

为确保清晰和透明，我们公开记录数据库最新更新与此前版本之间的变化。因此，我们提供多种文件，记录并阐明每个数据库版本所作的修改，包括详细变更报告、对应关系文件，以及包含每个版本全部活动的文件。此外，我们记录每个版本的全部已知问题，提醒数据库用户，并帮助他们理解和使用数据库。

### ecoinvent 第 3.0 版相关文件 <a href="#zh-b0007" id="zh-b0007"></a>

#### 变更报告 <a href="#zh-b0008" id="zh-b0008"></a>

为确保清晰和透明，公开记录数据库最新更新与此前版本之间的变化十分重要。本报告涵盖 ecoinvent 数据库第 2.2 版至第 3.0 版（2013 年）之间的所有变化，同时反映全数据库范围的变化和各行业特定变化。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[变更报告](../assets/1fd0ecc76fd9-report_of_changes_ecoinvent_2.2_to_3.0_20130904.pdf)

#### 基本流交换对应关系文件 <a href="#zh-b0011" id="zh-b0011"></a>

基本流交换对应关系文件是一个电子表格，详细列出第 2.2 版中所有基本流交换、区室和子区室，以及它们在第 3.0 版中对应的术语和功能。该文件还列出第 3 版新增交换，使您能够直接比较 ecoinvent 2.2 和 v3.0。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[基本流交换对应关系文件](../assets/0924b23cc5e2-correspondence_file_elementary-exchanges_v2.2-v3.0_20130904.xls)

#### 中间交换对应关系文件 <a href="#zh-b0014" id="zh-b0014"></a>

此文件比较第 2.2 版的“过程”名称与第 3.0 版的“活动”和“产品”名称，从而完整呈现 ecoinvent 2.2 与 v3.0 之间的全部变化。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[中间交换对应关系文件](../assets/7f294018741b-correspondence_file_intermediate-exchangesv2.2_to_v3.0_20130904.xlsx)

#### ecoinvent 第 3.01 版活动概览 <a href="#zh-b0017" id="zh-b0017"></a>

一个列出数据库中全部活动的 Excel 文件。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[ecoinvent v3.01 活动概览](../assets/58caafe4b015-activity_overview_for_users_3.01_20130904-1.xlsx)

### 已知问题 <a href="#zh-b0020" id="zh-b0020"></a>

本部分列出 ecoinvent 数据库第 3.1 版中的全部已知数据错误。ecoinvent 团队着力在后续更新中消除这些错误，本部分列出已知问题旨在提醒用户，并帮助他们理解和使用数据库。

#### 数据问题 <a href="#zh-b0022" id="zh-b0022"></a>

- 重新引入并修正此前版本中被系统性截断或忽略的全部副产品的工作尚未完成。若干运输车辆数据集缺少完整的副产品集合。这会影响分配结果，因此这些车辆的影响被高估。同样，若干产品的副产品是纯金属，而不是废金属，影响了这些产品相关的环境影响。
- 少数交换因各种原因未正确链接，在已链接版本中作为投入消失。它们包括：“waste packaging glass, unsorted”（APOS 系统模型）；“heat, future”（Substitution, consequential, long-term 系统模型）；“heat, central or small-scale, other than natural gas”（Substitution, consequential, long-term 系统模型）；“natural gas, low pressure”（APOS 及 Substitution, consequential, long-term 系统模型）；“roundwood, azobe from sustainable forest management, CM, debarked”（APOS 及 Substitution, consequential, long-term 系统模型）。这可能使具有这些投入的数据集结果略有失真。

- 金属行业中缺少部分数据集（例如“steel production, electric, unalloyed”及碲的受约束市场），部分市场的组成也不准确（例如金和银市场）。这些问题可能使部分金属产生异常结果。
- 活动“processing of anode slime, primary copper production”以碲化铜为参考产品、银为副产品，这是因为阳极泥是碲的主要来源。不过，由于该副产品的存在，碲仅承担很少的环境负荷，在后果型系统模型中甚至出现整体负值。此数据集应改为处理活动，以银和亚碲酸钠作为副产品，并建立亚碲酸钠受约束市场。这一已知错误影响所有大量使用碲的数据集。
- “water/ground-, long-term”交换的表征因子被错误纳入不包含长期排放（w/o LT）的影响评价方法。
- 命名规范。ecoinvent 数据库中所有名称和文本字段均默认使用英式英语。不正确的命名（例如 sulfur dioxide/sulphur dioxide）将在 ecoinvent v3.1 数据库中修正。

#### ecoinvent 3.01 <a href="#zh-b0029" id="zh-b0029"></a>

ecoinvent 于 2013 年 9 月 4 日发布错误修复版 3.01。该版本纠正第 3.0 版中的部分错误，并取代该版本。这些修改将优化数据库的使用和准确性。

#### 价格修正 <a href="#zh-b0031" id="zh-b0031"></a>

部分产品价格数据质量较差，影响了分配系统模型的结果。现已用更准确的数值修正这些价格。

本次更新影响以下产品的价格：  
aluminium, wrought alloy; battery, Li-ion, rechargeable, prismatic; charger, electric passenger car; charger, for electric scooter; controller, for electric scooter; converter, for electric passenger car; cryolite; door, inner, glass-wood; door, inner, wood; door, outer, wood-aluminium; door, outer, wood-glass; electric bicycle; electric motor, electric passenger car; electric motor, for electric scooter; electric scooter, without battery; glass cullet, sorted; glider, for electric scooter; hydrogen fluoride; inverter, for electric passenger car; lorry production, 40 ton; lorry, 16 metric ton; lorry, 28 metric ton; passenger car, electric, without battery; phosphoric acid, industrial grade, without water, in 85% solution state; potassium hydroxide; power distribution unit, for electric passenger car; powertrain, for electric passenger car; powertrain, for electric scooter; single-Si wafer, for electronics; solar collector glass tube, with silver mirror; tetrafluoroethylene; tissue paper; titanium dioxide; transport, passenger car, electric; transport, passenger, electric bicycle; transport, passenger, electric bicycle, label-certified electricity; transport, passenger, with electric scooter; waste packaging glass, unsorted; window frame, aluminium, U=1.6 W/m2K; window frame, wood, U=1.5 W/m2K; window frame, wood-metal, U=1.6 W/m2K; zinc oxide; zinc sulfide。

#### 数据修正 <a href="#zh-b0034" id="zh-b0034"></a>

用户或我们自身在部分数据集中发现了错误，既包括来自 v2.2 的错误，也包括为 v3.0 所作修改带来的错误。

#### 已处理以下错误： <a href="#zh-b0036" id="zh-b0036"></a>

- “glass cullet, sorted”供应链已重新构建，现在该产品具有受约束市场，而不再被归为待处理材料。更新后的变更报告第 17 章介绍了这对从第 2.2 版转换的数据集的影响。这一变化也影响第 3.0 版的一些新增数据集：在第 3.01 版中，它们不再是处理活动，而是普通转化活动，例如“glass cullet supply, for Saint-Gobain ISOVER SA”和“glass wool mat production, Saint-Gobain ISOVER SA”。
- “dimethylamine production”中发现的数据错误已修正。
- “basalt quarry operation”中的颗粒物排放已修正。
- “transport, passenger car, electric”和“transport, passenger, electric scooter”中的制动磨损排放已修改，以与其他运输数据集保持一致。
- 活动“manganese sulfate production”已修改，现在包含“manganese concentrate”投入。

#### 新增或修正的市场 <a href="#zh-b0042" id="zh-b0042"></a>

已为不同产品新增部分区域市场，以更好地反映现有供应链并提高结果质量。

#### 第 3.01 版更新新增的本地市场包括： <a href="#zh-b0044" id="zh-b0044"></a>

- “market for heat, central or small-scale, natural gas”，位于 CH 和 Europe without Switzerland
- “market for heat, central or small-scale, other than natural gas”，位于 CH 和 Europe without Switzerland
- “market for heat, district or industrial, natural gas”，位于 CH 和 Europe without Switzerland
- “market for heat, district or industrial, other than natural gas”，位于 CH 和 Europe without Switzerland
- “market for linerboard”，位于 RER
- “market for fluting medium”，位于 RER

部分其他市场也以不同方式修正。  
“market for waste emulsion paint, separated”“market for waste bitumen sheet”“market for waste vapour barrier, flame-retarded”和“market for waste vapour barrier, flame-retarded”的默认运输距离已调整，并加入“Default transport assumptions”（默认运输假设）文档中的例外清单。

#### 生产量修正 <a href="#zh-b0052" id="zh-b0052"></a>

若干产品的生产量已调整，其中一些修改在变更报告中说明。热产品的生产量也已调整，以更好地匹配新建本地市场。

#### 不确定性修复 <a href="#zh-b0054" id="zh-b0054"></a>

由于数据库文件导出中的软件问题，部分数据集的不确定性因子有误。现在，所有数据集中不确定性字段的平均值和方差均正确显示。

#### 真实价值（True Value） <a href="#zh-b0056" id="zh-b0056"></a>

现在，真实价值关系已正确计算，消除了分配系统模型中的少量计算错误。

#### LCIA 矩阵格式改进 <a href="#zh-b0058" id="zh-b0058"></a>

LCIA 矩阵已采用更方便用户的格式。产品名称更清晰，整体排列也变得更实用：活动和产品现在按行排列，方法按列排列。

{% endtab %}

{% tab title="English 原文" %}

## ecoinvent v3.0 was released in May 2013. ecoinvent v3.0 is the third major release of the ecoinvent database. The third version of the database offers several exciting new features as well as new and updated datasets. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.0 was released on May 6th, 2013</strong>. Discover how to [upgrade to our latest version](licensing.md).

Oct 16th, 2023

ecoinvent released a bug-fix version 3.01 on 4th September 2013. ecoinvent v3.01 corrects some errors present in the 3.0 version and substitutes that version. The changes made optimise the use and accuracy of the ecoinvent database.

As we wish to ensure clarity and transparency, we openly document the changes made between the latest update and the previous version of the database. Therefore, we offer various files that document and clarify the changes that have been made with each version of the database. These include detailed the report of changes, correspondence files, as well as files that include all activities of each version. Futrher, we document all known issues of each version to alert database users and to support their understanding and use of the database.

### Relevant files for ecoinvent Version 3.0 <a href="#en-b0007" id="en-b0007"></a>

#### Report of Changes <a href="#en-b0008" id="en-b0008"></a>

To ensure clarity and transparency, it is important to openly document the changes made between the latest update and the previous version of the database. This report covers all changes made in the ecoinvent database between version 2.2 and version 3.0 (2013). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/1fd0ecc76fd9-report_of_changes_ecoinvent_2.2_to_3.0_20130904.pdf)

#### Correspondence File for Elementary Exchanges <a href="#en-b0011" id="en-b0011"></a>

The correspondence file for elementary exchanges is a spreadsheet that provides with a detailed overview of all elementary exchanges, compartments and sub-compartments in version 2.2 and to which term and function they correspond to in version 3.0. It also lists the new version 3 exchanges allowing you to draw a direct comparison between ecoinvent 2.2 and v3.0.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File for Elementary Exchanges](../assets/0924b23cc5e2-correspondence_file_elementary-exchanges_v2.2-v3.0_20130904.xls)

#### Correspondence File for Intermediate Exchanges <a href="#en-b0014" id="en-b0014"></a>

This file draws up a comparison between the “process” names in version 2.2 and the “activity” and “product” names you can find in version 3.0 thereby giving a complete picture of all changes which have taken place between ecoinvent 2.2 and v3.0.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File for Intermediate Exchanges](../assets/7f294018741b-correspondence_file_intermediate-exchangesv2.2_to_v3.0_20130904.xlsx)

#### Activity Overview for ecoinvent Version 3.01 <a href="#en-b0017" id="en-b0017"></a>

An excel file which lists all the activities present in the database

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.01](../assets/58caafe4b015-activity_overview_for_users_3.01_20130904-1.xlsx)

### Known Issues <a href="#en-b0020" id="en-b0020"></a>

This section lists all known data errors in version 3.1 of the ecoinvent database. While the ecoinvent team focuses on eliminating such errors for upcoming updates, this section of known issues exists to alert database users and to support their understanding and use of the database.

#### Data issues <a href="#en-b0022" id="en-b0022"></a>

- The reintroduction and correction of all by-products that have been systematically cut-off or ignored during previous versions of the database is not complete. Several transport vehicle datasets are missing a full set of by-products. This affects the allocation result and the impacts of these vehicles are therefore overestimated. Similarly, several products have a by-product of pure metal, instead of scrap which affects the impacts associated to those products.
- There are a few exchanges that are not correctly linked (for several reasons), and disappear as inputs in the linked version. They are: “waste packaging glass, unsorted” (in APOS SM); “heat, future” (in Substitution, consequential, long-term SM); “heat, central or small-scale, other than natural gas” (in Substitution, consequential, long-term SM); “natural gas, low pressure” (APOS SM; Substitution, consequential, long-term SM); “roundwood, azobe from sustainable forest management, CM, debarked” (APOS; Substitution, consequential, long-term SM). This can slightly distort the results of the datasets that have one of those inputs.

- In the metal sector some datasets are missing (i.e. “steel production, electric, unalloyed”; constrained market for tellurium), and some markets have inaccurate compositions (i.e. market for gold and silver). These problems might deliver strange results for some metals.
- The activity “processing of anode slime, primary copper production” has copper telluride as its reference product and silver as by-product, which follows from the fact that anode slime is the principal source of tellurium. However, due to the by-product, tellurium receives very little burden, and in the consequential system model even overall negative values. This dataset should be changed into a treatment activity with silver and sodium tellurite as by-products, and with a constrained market for sodium tellurite. This known error affects all datasets that use tellurium in significant amounts.
- Characterization factors of water/ground-, long-term exchanges have erroneously been included in the w/o LT impact methods
- Naming convention. British English is used as the default language for all names and text fields in the ecoinvent database. Incorrect naming (such as sulfur dioxide/ sulphur dioxide) will be corrected for the ecoinvent v3.1. database

#### ecoinvent 3.01 <a href="#en-b0029" id="en-b0029"></a>

ecoinvent released a bug-fix version 3.01 on 4th September 2013. This version corrects some errors present in the 3.0 version and substitutes that version. The changes made will optimise the use and accuracy of the ecoinvent database.

#### Corrected Prices <a href="#en-b0031" id="en-b0031"></a>

Some products had poor price data which affected the results in the allocation system model. The prices have now been corrected with a more accurate value.

This update affects the price for the following products:   
aluminium, wrought alloy; battery, Li-ion, rechargeable, prismatic; charger, electric passenger car; charger, for electric scooter; controller, for electric scooter; converter, for electric passenger car; cryolite; door, inner, glass-wood; door, inner, wood; door, outer, wood-aluminium; door, outer, wood-glass; electric bicycle; electric motor, electric passenger car; electric motor, for electric scooter; electric scooter, without battery; glass cullet, sorted; glider, for electric scooter; hydrogen fluoride; inverter, for electric passenger car; lorry production, 40 ton; lorry, 16 metric ton; lorry, 28 metric ton; passenger car, electric, without battery; phosphoric acid, industrial grade, without water, in 85% solution state; potassium hydroxide; power distribution unit, for electric passenger car; powertrain, for electric passenger car; powertrain, for electric scooter; single-Si wafer, for electronics; solar collector glass tube, with silver mirror; tetrafluoroethylene; tissue paper; titanium dioxide; transport, passenger car, electric; transport, passenger, electric bicycle; transport, passenger, electric bicycle, label-certified electricity; transport, passenger, with electric scooter; waste packaging glass, unsorted; window frame, aluminium, U=1.6 W/m2K; window frame, wood, U=1.5 W/m2K; window frame, wood-metal, U=1.6 W/m2K; zinc oxide; zinc sulfide.

#### Corrected Data <a href="#en-b0034" id="en-b0034"></a>

Errors were found in some datasets (originating from v2.2 as well as from changes made for v3.0) by our users or by ourselves.

#### The Following Errors Have Been Addressed: <a href="#en-b0036" id="en-b0036"></a>

- The “glass cullet, sorted” supply chain has been restructured, and now “glass cullet, sorted” has a constrained market, instead of being classified as material for treatment. How this affected the datasets converted from version 2.2 is described in Chapter 17 of the updated Change Report. This change affected as well some datasets new in version 3.0, that are not treatment activities anymore in version 3.01, but ordinary transforming activities, like: “glass cullet supply, for Saint-Gobain ISOVER SA” and “glass wool mat production, Saint-Gobain ISOVER SA”.
- Data errors found in “dimethylamine production” have been corrected.
- Particulate emissions in “basalt quarry operation” have been corrected.
- The brake wear emissions in “transport, passenger car, electric” and “transport, passenger, electric scooter” have been edited to be consistent with other transport datasets.
- The activity “manganese sulfate production” has been modified; it now receives an input of “manganese concentrate”.

#### Markets Added or Corrected <a href="#en-b0042" id="en-b0042"></a>

Some regional markets have been added for different products. This allows to better reflect the existing supply chains and to improve the quality of the results.

#### The Added Local Markets During Version 3.01 Update are: <a href="#en-b0044" id="en-b0044"></a>

- “market for heat, central or small-scale, natural gas”, in CH, and Europe without Switzerland
- “market for heat, central or small-scale, other than natural gas”, in CH, and Europe without Switzerland
- “market for heat, district or industrial, natural gas”, in CH, and Europe without Switzerland
- “market for heat, district or industrial, other than natural gas”, in CH, and Europe without Switzerland
- “market for linerboard”, in RER
- “market for fluting medium”, in RER

Some other markets have been corrected in different ways.  
The markets for “market for waste emulsion paint, separated”; “market for waste bitumen sheet”; “market for waste vapour barrier, flame-retarded”; and “market for waste vapour barrier, flame-retarded” got their default transport distances adjusted, and were added to the exception list in the “Default transport assumptions” document.

#### Corrected Production Volumes <a href="#en-b0052" id="en-b0052"></a>

The production volumes of several products have been adjusted; some of those changes are addressed in the Change Report. Heat products have had their production volumes adjusted to better fit to the new local markets created.

#### Uncertainties Repaired <a href="#en-b0054" id="en-b0054"></a>

Due to a software issue in the export of the files from our database, the uncertainty factors were wrong in some datasets. The mean value and variance in the uncertainty fields is now presented correctly in all datasets.

#### True Value <a href="#en-b0056" id="en-b0056"></a>

The true value relations are now calculated correctly, removing a few calculation errors from the allocation system model.

#### Format of LCIA Matrices Improved <a href="#en-b0058" id="en-b0058"></a>

The LCIA matrices have been formatted in a more user-friendly way. The names of the products are clearer, and the general arrangement has changed to become more useful: activities and products are now listed in rows and the methods can be found in columns.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0021**：本页面为第 3.0 版，但已知问题引言写第 3.1 版；可能为版本号笔误。 请核实已知问题所对应版本；暂保留原文。 [查看完整记录](../review/issues.md#issue-016)
- **待专家复核 · b0051**：原文四项市场中最后两项名称相同，可能重复或漏写另一市场。 请核对变化报告确认列表；暂保留原文重复项。 [查看完整记录](../review/issues.md#issue-017)
- **已处理／已说明 · b0006**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-018)
- **已处理／已说明 · b0008**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-019)
- **已处理／已说明 · b0010**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-020)
- **已处理／已说明 · b0037**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-021)
- **已处理／已说明 · b0053**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-022)
