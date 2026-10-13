# ecoinvent 第 3.1 版

英文原题：ecoinvent Version 3.1  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.1)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.1 于 2014 年 7 月发布。此次发布主要聚焦新增数据，包括新产品和现有行业更新。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.1 于 2014 年 7 月 1 日发布</strong>。了解如何[升级到我们的最新版本](licensing.md)。

2023 年 10 月 17 日

该版本还恢复了第 2 版的分配模型及可再生能源累积能源需求（CED）相关流，并引入新的 LCIA 方法。

为确保清晰和透明，我们公开记录数据库最新更新与此前版本之间的变化。因此，我们提供多种文件，记录并阐明每个数据库版本所作的修改，包括详细变更报告、对应关系文件，以及包含每个版本全部活动的文件。此外，我们记录每个版本的全部已知问题，提醒数据库用户，并帮助他们理解和使用数据库。

### 新增与更新的数据 <a href="#zh-b0007" id="zh-b0007"></a>

#### 林业与木材 <a href="#zh-b0008" id="zh-b0008"></a>

林业与木材行业新增或更新了林业和林业机械、锯木、木制品、木材防腐剂及防腐服务，以及木材焚烧产热和发电的数据。

#### 金属 <a href="#zh-b0010" id="zh-b0010"></a>

金属行业新增铝生产数据，包括其供应链和电力使用。

#### 废物管理 <a href="#zh-b0012" id="zh-b0012"></a>

该行业新增废物焚烧过程数据。

#### 运输 <a href="#zh-b0014" id="zh-b0014"></a>

该行业新增道路货运数据，并更新现有数据的排放情况。还改进了许多产品的运输距离建模。

#### 供水 <a href="#zh-b0016" id="zh-b0016"></a>

该行业新增自来水生产数据，并提高了整个数据库中水消耗数据的一致性。

#### 农业 <a href="#zh-b0018" id="zh-b0018"></a>

农业部门新增乳制品和农业过程数据。

#### 机械 <a href="#zh-b0020" id="zh-b0020"></a>

该行业包含新增的机械使用和建筑材料数据。

### 相关文档与文件 <a href="#zh-b0022" id="zh-b0022"></a>

#### 变更报告 <a href="#zh-b0023" id="zh-b0023"></a>

本报告涵盖 ecoinvent 数据库第 3 版（2013 年）至第 3.1 版（2014 年）之间的所有变化，同时反映全数据库范围的变化和各行业特定变化。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[变更报告](../assets/638603ede67f-20140630_report_of_changes_ecoinvent_3.01_to_3.1.pdf)

#### ecoinvent v3.1 活动概览：未指定系统模型（Undefined） <a href="#zh-b0026" id="zh-b0026"></a>

一个列出 ecoinvent 第 3.1 版数据库中全部活动和产品的 Excel 文件，包含大部分元数据（地理区域、ISIC 分类、活动类型、技术水平、产品类型、单位等）。该文件还列出数据库中全部地理区域、基本流交换和中间交换。

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)  </strong>参阅[ecoinvent v3.1 活动概览：未指定系统模型（Undefined）](../assets/2dacd37093e1-activity_overview_for_users_3.1_undefined.xlsx)

#### ecoinvent 第 3.1 版活动概览：默认（Default） <a href="#zh-b0029" id="zh-b0029"></a>

一个列出 ecoinvent 第 3.1 版数据库中全部活动的 Excel 文件，包含专门针对“Allocation, ecoinvent default”系统模型的元数据。

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)</strong>参阅[ecoinvent v3.1 活动概览：默认（Default）](../assets/4e43ccdbcec9-activity_overview_for_users_3.1_default.xlsx)

#### ecoinvent 第 3.1 版活动概览：后果型（Consequential） <a href="#zh-b0032" id="zh-b0032"></a>

一个列出数据库中全部活动的 Excel 文件，包含专门针对长期后果型替代模型（Substitution, consequential, long-term）的元数据。

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)</strong>参阅[ecoinvent v3.1 活动概览：后果型（Consequential）](../assets/ab7e7ae78a9e-activity_overview_for_users_3.1_long-term-1.xlsx)

#### ecoinvent 第 3.1 版活动概览：截断（Cut-Off） <a href="#zh-b0035" id="zh-b0035"></a>

一个列出数据库中全部活动的 Excel 文件，包含专门针对按分类截断的分配模型（Allocation, cut-off by classification）的元数据。

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)</strong>参阅[ecoinvent v3.1 活动概览：截断（Cut-Off）](../assets/f0779c8332a5-activity_overview_for_users_3.1_cut-off.xlsx)

### 已知问题 <a href="#zh-b0038" id="zh-b0038"></a>

本部分列出 ecoinvent 数据库第 3.1 版中的全部已知数据错误。

#### 数据问题 <a href="#zh-b0040" id="zh-b0040"></a>

- 在“electricity production, nuclear, pressure water reactor, heavy water moderated”活动（所有地区）中，放射性物质向水的排放估算有误。因此，这些数据集的此类物质排放过高，导致电离辐射和各种毒性排放影响类别的影响被高估，尤其影响加拿大部分地区的电力组合。
- “copper mine operation”的 RoW 数据集中，“copper, 0.99%”基本流投入过高：对于两种联产品均约为正确值的 5 倍。作为临时修复建议，可将铜精矿对应投入设为 0.356 kg，将辉钼矿对应投入设为 0 kg。这适用于两种产品的分配模型数据集，以及后果型数据集。

- 铝工业特定区域电力组合的创建方式保持了所谓铝生产区域内各国的相对份额，但所得整个区域的电网组合与国际铝业协会网站发布的组合不一致。差异在以下地区尤其明显：区域 1（非洲）的煤电低了 12%、水电高了 12%；区域 4/5（亚洲，不含中国）的煤电高了 18%、水电低了 18%；区域 7（大洋洲）的煤电高了 12%、水电低了 12%；区域 2（北美），不含魁北克，煤电高了 14%、水电低了 15%。此外，魁北克电力组合基于第 3.0 版发布的过时数据；水电应减少 1%，核电应增加 1%。
- “treatment of aluminium scrap, post-consumer, by collecting, sorting, cleaning, pressing”活动中 PM &gt;10 um 的数量有误，比应有值大 10e5 倍。
- 下列活动遵循溶液中化学品的规则，移除了溶剂/水投入：

alkyd paint production, white, solvent-based, product in 60% solution state（溶剂型白色醇酸涂料生产，产品处于 60% 溶液状态）  

1. alkyd paint production, white, water-based, product in 60% solution state（水性白色醇酸涂料生产，产品处于 60% 溶液状态）
2. alkyd resin production, long oil, product in 70% white spirit solution state（长油度醇酸树脂生产，产品处于 70% 矿物油溶剂（white spirit）溶液状态）
3. printing ink production, offset, product in 47.5% solution state（胶版印刷油墨生产，产品处于 47.5% 溶液状态）
4. printing ink production, rotogravure, product in 55% toluene solution state（凹版印刷油墨生产，产品处于 55% 甲苯溶液状态）

- 遗憾的是，消耗所得产品（如下所列）的活动也缺少这一溶剂/水投入。

1. alkyd paint, white, without solvent, in 60% solution state（白色醇酸涂料，不计溶剂，处于 60% 溶液状态）  
   2. alkyd paint, white, without water, in 60% solution state（白色醇酸涂料，不计水，处于 60% 溶液状态）  
   3. alkyd resin, long oil, without solvent, in 70% white spirit solution state（长油度醇酸树脂，不计溶剂，处于 70% 矿物油溶剂（white spirit）溶液状态）  
   4. printing ink, offset, without solvent, in 47.5% solution state（胶版印刷油墨，不计溶剂，处于 47.5% 溶液状态）  
   5. printing ink, rotogravure, without solvent, in 55% toluene solution state（凹版印刷油墨，不计溶剂，处于 55% 甲苯溶液状态）

- “electricity, from municipal waste incineration to generic market for electricty, medium voltage”存在拼写错误：electricty 应为 electricity。
- 在 ecoinvent 第 3.0 版和第 3.1 版中，变压和输电损失按各个电压等级单独建模，未考虑电力市场中从高压向低压变压和输送过程中这些损失的累积性质。
- “treatment of wastewater from medium density fibreboard production, capacity 5E9l/year”的 GLO 和 RER 活动中，向“water, ground-, long-term”的硝酸盐排放有误。错误值（2.03E+5kg）已被正确值（2.03E-5kg）替换，并将在数据库下一次发布中纳入。

{% endtab %}

{% tab title="English 原文" %}

## ecoinvent v3.1 was released in July 2014. The main focus of this release was new data, with new products and updates to existing sectors. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.1 was released on July 1st, 2014</strong>. Discover how to [upgrade to our latest version](licensing.md).

Oct 17th, 2023

It also brought back the allocation model of version 2 as well as flows for the renewable CED and has introduced new LCIA methods.

As we wish to ensure clarity and transparency, we openly document the changes made between the latest update and the previous version of the database. Therefore, we offer various files that document and clarify the changes that have been made with each version of the database. These include detailed the report of changes, correspondence files, as well as files that include all activities of each version. Futrher, we document all known issues of each version to alert database users and to support their understanding and use of the database.

### New and Updated Data <a href="#en-b0007" id="en-b0007"></a>

#### Forestry & Wood <a href="#en-b0008" id="en-b0008"></a>

The forestry and wood sector was updated with new or updated data on forestry and forestry machinery, sawmilling, wood products, wood preservatives and wood preservation services, heat and electricity from wood incineration.

#### Metals <a href="#en-b0010" id="en-b0010"></a>

The metals sector was expanded with new data on aluminium production including its supply chain and electricity use.

#### Waste Management <a href="#en-b0012" id="en-b0012"></a>

The sector was updated with new data on waste incineration processes.

#### Transport <a href="#en-b0014" id="en-b0014"></a>

The sector was updated with new data on road freight transport and emission updates of the existing data. The sector also includes improved data transport distance modeling for many products.

#### Water Supply <a href="#en-b0016" id="en-b0016"></a>

The sector is updated with new data for tap water production, and improved consistency in water consumption data throughout the database.

#### Agriculture <a href="#en-b0018" id="en-b0018"></a>

The Agriculture sector is updated with new data on dairy products and agricultural processes.

#### Machinery <a href="#en-b0020" id="en-b0020"></a>

The sector includes new data on machinery use and building materials.

### Relevant Documents and Files <a href="#en-b0022" id="en-b0022"></a>

#### Report of Changes <a href="#en-b0023" id="en-b0023"></a>

This report covers all changes made in the ecoinvent database between version 3 (2013) and version 3.1 (2014). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/638603ede67f-20140630_report_of_changes_ecoinvent_3.01_to_3.1.pdf)

#### Activity Overview for ecoinvent v3.1, Undefined <a href="#en-b0026" id="en-b0026"></a>

An excel file listing all the activities and products present in the ecoinvent version 3.1 database including most of the metadata (geography, ISIC classification, activity type, technology level, product type, unit, etc.). This file also includes a list of all geographies, elementary and intermediate exchanges present in the database.

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)  </strong>See [Activity Overview for ecoinvent v3.1, Undefined](../assets/2dacd37093e1-activity_overview_for_users_3.1_undefined.xlsx)

#### Activity Overview for ecoinvent Version 3.1, Default <a href="#en-b0029" id="en-b0029"></a>

An excel file listing all the activities present in the ecoinvent version 3.1 database including metadata related specifically to the Allocation, ecoinvent default system model.

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)</strong>  See [Activity Overview for ecoinvent v3.1, Default](../assets/4e43ccdbcec9-activity_overview_for_users_3.1_default.xlsx)

#### Activity Overview for ecoinvent Version 3.1, Consequential <a href="#en-b0032" id="en-b0032"></a>

An excel file listing all the activities present in the database including metadata related specifically to the Substitution, consequential, long-term system model.

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)</strong>  See [Activity Overview for ecoinvent v3.1, Consequential](../assets/ab7e7ae78a9e-activity_overview_for_users_3.1_long-term-1.xlsx)

#### Activity Overview for ecoinvent Version 3.1, Cut-Off <a href="#en-b0035" id="en-b0035"></a>

An excel file which lists all the activities present in the database including metadata related specifically to the Allocation, cut-off by classification system model.

<strong>![doc-icon](../assets/024d8f149226-doc-icon.png)</strong>  See [Activity Overview for ecoinvent v3.1, Cut-Off](../assets/f0779c8332a5-activity_overview_for_users_3.1_cut-off.xlsx)

### Known Issues <a href="#en-b0038" id="en-b0038"></a>

This section lists all known data errors in version 3.1 of the ecoinvent database.

#### Data Issues <a href="#en-b0040" id="en-b0040"></a>

- In the activity electricity production, nuclear, pressure water reactor, heavy water moderated (all regions), emissions of radioactive substances to water have been estimated erroneously. These datasets therefore have too high emissions of these substances. The consequence is an overestimation of impacts in Ionizing Radiation and various toxic emission impact categories. Especially the electricity mixes of some Canadian regions are affected.
- The input of copper, 0.99% elementary flow is too high in the RoW dataset of copper mine operation: it is about 5x too high for both co-products, it could simply be 0.356 kg for copper concentrate and 0 kg for molybdenite as a recommendation for an intermediate fix. This goes for allocation models for both products, and for the consequential dataset.

- The regional electricity mixes specific to the aluminium industry were created in such a way that the relative shares of countries within so-called aluminium production areas were respected. However, the resulting area-wide grid mixes were not identical to those published on the International Aluminium Institute’s website. The differences are especially important for Area 1 (Africa), where coal is 12% too low and hydropower 12% too high, Area 4/5 (Asia w/o China) where coal is 18% too high and hydropower 18% too low, Area 7 (Oceania) where coal is 12% too high and hydropower 12% too low, and Area 2 (North America) w/o Quebec, where coal is 14% too high and hydropower 15% too low. Also, the electricity mix data for Quebec is based on outdated data published in version 3.0. The mix should have 1% less hydropower and 1% higher nuclear power.
- The activities “treatment of aluminium scrap, post-consumer, by collecting, sorting, cleaning, pressing” contains an error in the amount of PM &gt; 10 um, which is 10e5 bigger than it should.
- The following activities had the input of solvent/water removed, following the rule of chemicals in solution:

alkyd paint production, white, solvent-based, product in 60% solution state  

1. alkyd paint production, white, water-based, product in 60% solution state
2. alkyd resin production, long oil, product in 70% white spirit solution state
3. printing ink production, offset, product in 47.5% solution state
4. printing ink production, rotogravure, product in 55% toluene solution state

- Unfortunately, the demanding activities of the resulting products (listed below) also lack this input of solvent/water.

1. alkyd paint, white, without solvent, in 60% solution state  
   2. alkyd paint, white, without water, in 60% solution state  
   3. alkyd resin, long oil, without solvent, in 70% white spirit solution state   
   4. printing ink, offset, without solvent, in 47.5% solution state   
   5. printing ink, rotogravure, without solvent, in 55% toluene solution state

- Typo in “electricity, from municipal waste incineration to generic market for electricty, medium voltage” ; electricty instead of electricity
- In ecoinvent version 3.0 and version 3.1, the electricity losses from transformation and transmission are modeled on a voltage level-by-voltage level basis and do not consider the cumulative nature of these losses on their way from high to low voltage transformation and transmission on the electricity markets.
- In the “treatment of wastewater from medium density fibreboard production, capacity 5E9l/year”/GLO and RER activities the emission of Nitrate to water, ground-, long-term- is incorrect. The wrong value (2.03E+5kg) has been replaced by the correct value (2.03E-5kg) and will be included in the next release of the database.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **已处理／已说明 · b0006**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-023)
- **已处理／已说明 · b0023**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-024)
- **已处理／已说明 · b0025**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-025)
- **已处理／已说明 · b0005**：统一 CED 的中文名称。 已修正。 [查看完整记录](../review/issues.md#issue-026)
- **已处理／已说明 · b0042**：避免“高了 5 倍”被理解为正确值的 6 倍。 已明确比例关系。 [查看完整记录](../review/issues.md#issue-027)
- **已处理／已说明 · b0051**：保留五条完整可检索英文名称，同时补充逐条中文解释。 已补全中文解释。 [查看完整记录](../review/issues.md#issue-028)
