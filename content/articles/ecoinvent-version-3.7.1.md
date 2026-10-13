# ecoinvent 3.7.1 版

英文原题：ecoinvent Version 3.7.1  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.7.1)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.7.1 于 2020 年 12 月发布。它包含与数据库 3.7 版相同的数据集，但对 3.7 版的特定数据集作出两项重要修正。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.7.1 于 2020 年 12 月 17 日发布</strong>。了解如何[升级到最新版本](licensing.md)。

2024年3月18日

此对 ecoinvent 数据库 3.7 版的更新包含相同的新增和更新数据集，并对数据库作出两项重要修正。3.7 版发布时新增了 900 多个数据集，更新了 1,000 多个数据集，包括 100 多种新产品。该更新扩展了金属、肥料、林业与木材、包装材料、废物／回收及沼气供应链等多个部门的覆盖范围，也更新了电力市场组合。ecoinvent 3.7 的铁烧结矿生产数据集存在错误。

<strong>ecoinvent v3.7.1</strong>于 2020 年 12 月发布，以便  

- <strong>修正铁烧结矿生产数据集</strong>：在 ecoinvent v3.7 中，该数据集估算的二噁英和颗粒物（PM）排放存在数量级错误。这一错误使采用多数方法的人类健康和生态毒性指标计算的数据库结果失真。
- <strong>更新锌矿开采数据集</strong>：国际锌业协会在 ecoinvent v3.7 发布后提供了此数据集的建模改进，显著改善数据库结果。这项改进影响采用矿产资源指标计算的数据库结果。

ecoinvent v3.7.1 的发布会影响 v3.7 中采用矿产资源、人类健康和生态毒性指标计算的结果，具体取决于所用方法。<strong>基于所有其他影响类别的研究和项目，包括气候变化、水资源耗竭、累积能源需求、土地利用和土地利用变化、化石资源耗竭、酸化、富营养化、电离辐射、可再生资源、平流层臭氧耗竭、光化学氧化剂形成、放射性物质和臭氧层耗竭，</strong>完全不受此次补充发布影响。

可获取详细的[受影响类别报告](../assets/42659ab6e598-technical-report_v3-7-1_20201217-1.pdf)。

### 新增和更新的数据 <a href="#zh-b0010" id="zh-b0010"></a>

#### 金属 <a href="#zh-b0011" id="zh-b0011"></a>

金属部门新增和更新铜、镍、铁、钢，以及钴、稀土、钨、铍等稀缺金属的数据。数据贡献者包括 EMPA（由瑞士联邦环境署 BAFU 资助）、Cobalt Institute 和格拉茨工业大学。北美铝数据集也采用加拿大铝业协会贡献的数据进行了修订。

#### 肥料 <a href="#zh-b0013" id="zh-b0013"></a>

肥料数据纳入农业、畜牧业和化学品部门。ecoinvent v3.7.1 包含 Yara International ASA 和 Fertilizers Europe 提供的矿物肥料生产新增与更新数据，由 Quantis（WFLDB）合作提交。此外，肥料部门的市场和市场组合进行了总体重组和更新，现区分用于养分供应的有机肥料和矿物肥料。

#### 能源 <a href="#zh-b0015" id="zh-b0015"></a>

ecoinvent 3.7.1 版还引入了与 Carbotech 合作获得的瑞士沼气生产和供应链新数据。此外，归因型电力市场组合已更新，反映多数国家在 2017 年的状况；美国和加拿大的参考年为 2018 年。数据创建和审查与苏黎世联邦理工学院及保罗谢勒研究所（PSI）合作完成。

#### 木材 <a href="#zh-b0017" id="zh-b0017"></a>

ecoinvent v3.7.1 发布后，林业与木材部门中大多数林业活动和木材加工相关数据集得到更新。还新增了交叉层压木材、结构木材、三层和五层板以及空心刨花板等木基产品。此更新与 Werner Umwelt & Entwicklung 共同完成，并得益于与瑞士联邦环境署（BAFU）的合作。

#### 纸与纸浆 <a href="#zh-b0019" id="zh-b0019"></a>

3.7.1 版更新了包装材料相关数据，具体包含行业协会 Pro-Carton、ECMA 欧洲纸盒制造商协会、Eurosac 和 CEPI Eurokraft 提供的纸盒用纸板、牛皮纸和纸袋更新数据。瑞典研究院（RISE）促成了协会与 ecoinvent 之间的数据移交。

#### 废物处理与回收 <a href="#zh-b0021" id="zh-b0021"></a>

3.7.1 版通过新增包装材料回收活动数据，加强了废物处理与回收部门，包括欧洲和瑞士饮料罐及纸板回收的一系列新地区数据。此更新使用苏黎世联邦理工学院和 Carbotech 发表的案例研究文献数据。

#### 建筑材料 <a href="#zh-b0023" id="zh-b0023"></a>

ecoinvent v3.7.1 包含 ISOVER Saint Gobain 玻璃棉毡数据集的更新版本，由 Werner Umwelt & Entwicklung 提交。数据库现在为该品牌玻璃棉毡建模了两种可选胶黏剂。

### 相关文档和文件 <a href="#zh-b0025" id="zh-b0025"></a>

#### 变更报告（pdf） <a href="#zh-b0026" id="zh-b0026"></a>

本报告涵盖 ecoinvent 数据库 3.6 版（2019）与 3.7.1 版（2020）之间的全部变更，包括数据库整体变更和部门特定变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/1cebba817257-change-report_v3-7-1_20201217.pdf)

#### 变更报告（xlsx） <a href="#zh-b0029" id="zh-b0029"></a>

此自动生成的 Excel 文件概述数据库 3.6 和 3.7.1 版之间未指定系统模型的单元过程数据集的变更。变更报告 XLS 可在 EcoQuery（ecoinvent 第 3 版数据库在线版本）的“文件”（Files）部分获取，供 ecoinvent 数据库被许可人使用。

#### 对应关系文件 <a href="#zh-b0031" id="zh-b0031"></a>

对应关系文件是一份电子表格，列出 3.6 和 3.7.1 版所有数据集，并匹配两版本间相互对应的数据集。

此 Excel 文件列出 ecoinvent 3.7.1 版数据库的全部活动和产品，包括大多数元数据，例如地理区域、ISIC 分类、活动类型、技术水平、产品类型和单位等。还列出数据库中全部地理区域、基本流交换和中间交换。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件](../assets/d0091c2e42d9-correspondence_file_eiv3.6_to_eiv3.7.1.xlsx)

#### ecoinvent 3.7.1 版活动概览，未指定系统模型（Undefined） <a href="#zh-b0035" id="zh-b0035"></a>

此 Excel 文件列出 ecoinvent 3.7.1 版数据库的全部活动和产品，包括大多数元数据，例如地理区域、ISIC 分类、活动类型、技术水平、产品类型和单位等。还列出数据库中全部地理区域、基本流交换和中间交换。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7.1. 活动概览，未指定系统模型（Undefined）](../assets/dc982e5aca4c-activity_overview_3.7.1_undefined_public-1.xlsx)

#### <strong>ecoinvent 3.7.1 版活动概览，APOS</strong> <a href="#zh-b0038" id="zh-b0038"></a>

此 Excel 文件列出 ecoinvent 3.7 版数据库中的全部活动，包括与替代点分配模型专门相关的元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7.1 活动概览，APOS](../assets/f58f787d6a1b-activity_overview_3.7.1_allocation_apos_public.xlsx)

#### ecoinvent 3.7.1 版活动概览，Consequential <a href="#zh-b0041" id="zh-b0041"></a>

此 Excel 文件列出数据库中的全部活动，包括与长期后果型替代系统模型专门相关的元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7.1. 活动概览，Consequential](../assets/00a2d23a2e4e-activity_overview_3.7.1_consequential_public.xlsx)

#### ecoinvent 3.7.1 版活动概览，Cut-off <a href="#zh-b0043" id="zh-b0043"></a>

此 Excel 文件列出数据库中的全部活动，包括与按分类截断的分配系统模型专门相关的元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7.1 活动概览，Cut-off](../assets/a1db8f35b9c8-activity_overview_3.7.1_allocation_cut_off_public.xlsx)

#### ecoinvent 3.7.1 版中的 LCIA 方法 <a href="#zh-b0045" id="zh-b0045"></a>

列出全部 LCIA 方法及其所有影响类别，以及 ecoinvent 提供的选定 LCI 累积结果。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7.1 中的 LCIA 方法](../assets/3ceafd157e8f-LCIA-methods-in-ecoinvent-3.7.1.xlsx)

### 已知问题 <a href="#zh-b0047" id="zh-b0047"></a>

此部分列出 ecoinvent 数据库 3.7.1 版中的全部已知数据错误。

#### 数据问题 <a href="#zh-b0048" id="zh-b0048"></a>

- RoW 地理区域的“electricity voltage transformation from high to medium voltage”和“electricity voltage transformation from medium to low voltage”活动出现在 Allocation, cut-off 和 APOS 系统模型中。由于这些系统模型不存在 RoW 电力市场，这些数据集的 LCIA 结果值为零，不应使用。
- AU、CA、CL、CN、ID、KZ、RU、US 和 ZM 地理区域的“copper mine operation and beneficiation, sulfide ore”活动中，来自环境的“Tellurium, in ground”（地下的碲；区室：“natural resource”；子区室：“in ground”）输入交换数量，与 GLO 地理区域的数量不一致。根据这些地理区域合计开采全球铜矿中所提取 Te 的 70% 这一假设（全球量在 GLO 数据集中建模），已调低当地地理区域的交换数量。未指定系统模型数据集的新数量如下表，将在 v3.9 发布时提供。

<table>
<tbody>
<tr>
<td><strong>数据集</strong></td>
<td><strong>单位</strong></td>
<td><strong>原数值</strong></td>
<td><strong>新数值</strong></td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, AU（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8968E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, CA（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9067E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, CL（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8997E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, CN（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9018E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, ID（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8935E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, KZ（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9096E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, RU（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8960E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, US（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8973E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, ZM（硫化矿铜矿开采及选矿） </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9021E-05 </p>
</td>
</tr>
</tbody>
</table>

- APOS 系统模型中没有“treatment of wastewater from grass refinery, capacity 5E9l/year, RoW”活动。这不影响结果值，因为数据库中未使用该活动及其参考产品。
- “glucose production, RER”（葡萄糖生产）数据集被错误地排除在此次发布之外。建议使用“glucose production, GLO”并调整供应链，使其采用 RER 活动。我们将在 3.8 版重新加入该数据集。
- “glued laminated timber production, average glue mix, CA-QC”数据集具有错误参考产品，即“glued laminated timber, for indoor use”。该参考产品在 3.7 版更名为“glued laminated timber, average glue mix”。3.7 版不存在“glued laminated timber, for indoor use”市场。
- “market for sawnwood, board, softwood, dried (u=10%), planed, CH”市场的运输距离不正确。必须删除数据集中的“transport, freight, light commercial vehicle”交换，并加入数量为 86.7105 metric ton\*km 的“transport, freight, lorry, unspecified”交换。
- “treatment of spent sawing slurry from Si-wafer cutting, RER and GLO”活动中，参考产品“spent sawing slurry from Si-wafer cutting”的数量不正确。原始单输出单元过程见 v2 报告（Jungbluth, N., Stucki, M., Frischknecht, R. (2009). Photovoltaics〔光伏〕. 收录于 Dones, R. 编等，Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz〔能源系统清单：能源系统生态比较及将能源系统纳入瑞士生命周期评价的基础〕. Ecoinvent report No. 6-XII）。
- 航空货运数据集（“transport, freight, aircraft, dedicated freight, […] haul”和“transport, freight, aircraft, belly-freight, […] haul”）在 ecoinvent v3.8 发布中与原数据提供者 INFRAS 合作更新。更新项目报告（Notten P.J., Althaus H-J. and Cox B., (2021) Life cycle inventories of global air freight – Global, Update 2021〔全球航空货运生命周期清单——全球，2021 年更新〕. ecoinvent Association, Zürich, Switzerland）可在 ecoinvent 网站的[SRI 成果](https://ecoinvent.org/activities/sri-project/)部分获取。更多信息见 3.8 版变更报告，其中提供如何修正数据的指导及影响评价相关变更的信息。
- “styrene production”（苯乙烯生产）数据集中向水和空气的苯排放过高。在 PlasticsEurope 的支持下，已确定可完全删除数据集中的向水苯排放，并将向空气苯排放降至 2.0E-07 kg。修正后的清单在 3.8 版引入。
- “methylene diphenyl diisocyanate production”（二苯基甲烷二异氰酸酯生产，GLO 和 RER）数据集将生成的盐酸作为废物处理，这不符合实际。盐酸是有价值的副产品，由 MDI 生产者使用或销售。ecoinvent 协会建议用户采用 PlasticsEurope 网站现有[ecoProfile](https://plasticseurope.org/sustainability/circularity/life-cycle-thinking/eco-profiles-set/)的 LCIA 结果值，或者删除废物中和、将 HCl 作为副产品处理，以修正 ecoinvent 单元过程。  
  修正数据集时，建议使用 ecoQuery 中的 未指定系统模型（Undefined）的数据集，并删除氢氧化钠输入和钠、氯化物输出交换。

#### <strong>Consequential 系统模型问题</strong> <a href="#zh-b0099" id="zh-b0099"></a>

“social”（社会）区室中存在三个基本流交换。由于 ecoinvent 尚未考虑社会影响，在单元过程和清单层面均可忽略这些交换。

{% endtab %}

{% tab title="English 原文" %}

## ecoinvent v3.7.1 was released in December 2020. It includes the same datasets as version 3.7 of the ecoinvent database. However, it includes two important corrections to specific datasets of version 3.7. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.7.1 was released on December 17th, 2020</strong>. Discover how to [upgrade to our latest version](licensing.md).

March 18th, 2024

This update of version 3.7 of the ecoinvent database features the same new and updated datasets, including two important corrections to the database.The release of version 3.7 of the ecoinvent database included more than 900 new and 1’000 updated datasets, including more than 100 new products. This update expands the coverage of the database in various sectors such as metals, fertilisers, forestry and wood, packaging materials, waste/recycling, and biogas supply chains, while the electricity market mixes are also updated. ecoinvent 3.7 included an error in the iron sinter production dataset.

<strong>ecoinvent v3.7.1 </strong>was released in December 2020 to  

- <strong>correct the iron sinter production dataset</strong>; in ecoinvent v3.7, this dataset includes an error in the order of magnitude of the estimated emissions for dioxins and particulate matter (PM). This error distorts the results of the ecoinvent database calculated using human health and ecotoxicity indicators from most methods.
- <strong>update the zinc mining dataset</strong>; the International Zinc Association shared an improvement on the modeling of this dataset after the release of ecoinvent v3.7, which significantly improves the results of the ecoinvent database. This improvement affects the results of the ecoinvent database calculated using mineral resource indicators.

The release of ecoinvent v3.7.1 affects the results given by ecoinvent v3.7 calculated using mineral resource or human health and ecotoxicity indicators depending on the methods used. <strong>Research and projects based on all other impact categories, including climate change, water depletion, cumulative energy demand, land use and land use change, fossil depletion, acidification, eutrophication, ionising radiation, renewable resources, stratospheric ozone depletion, photochemical oxidant formation, radioactive substances, and ozone layer depletion </strong>remain completely unaffected by the additional release.

A detailed [report of the affected impact categories](../assets/42659ab6e598-technical-report_v3-7-1_20201217-1.pdf) is available

### New and Updated Data <a href="#en-b0010" id="en-b0010"></a>

#### Metals <a href="#en-b0011" id="en-b0011"></a>

The Metals sector has been updated with new and updated data on copper, nickel, iron and steel, and scarce metals such as cobalt, rare earths, tungsten, and beryllium. Data contributors included EMPA (sponsored by the Swiss Federal Office for the Environment, BAFU), the Cobalt Institute and TU Graz. The datasets for aluminium in North America have also been revised with data contributed by the Aluminium Association of Canada.

#### Fertilisers <a href="#en-b0013" id="en-b0013"></a>

Data for fertilisers are included in the sectors for Agriculture, Animal Husbandry, and Chemicals. ecoinvent v3.7.1includes new and updated data on mineral fertiliser production from Yara International ASA and Fertilizers Europe, submitted in collaboration with Quantis (WFLDB). Further, the markets and market mixes for the fertilisers sector have been generally restructured and updated, separating now the provision of organic and mineral fertilisers for nutrient supply.

#### Energy <a href="#en-b0015" id="en-b0015"></a>

ecoinvent version 3.7.1 also introduces new data on biogas production and supply chains for Switzerland, obtained from a collaboration with Carbotech. Further, attributional electricity market mixes are updated to represent the situation in 2017 for most countries. In the case of US and Canada, the reference year is 2018. Data creation and review was done in collaboration with ETH Zurich and the Paul Scherrer Institute (PSI).

#### Wood <a href="#en-b0017" id="en-b0017"></a>

Following the release of ecoinvent v3.7.1, most of the datasets related to forestry activities and wood processing in the Forestry and Wood sector are updated. Further,new wood-based products have been added, such as cross-laminated timber, structural timber, three and five layered board, and tubular particleboard. This update was done jointly with Werner Umwelt & Entwicklung and was made possible due to a collaboration with the Swiss Federal Office for the Environment (BAFU).

#### Paper and Pulp <a href="#en-b0019" id="en-b0019"></a>

Version 3.7.1 introduces updates in data related to packaging material. Specifically, it includes updated data from the industry associations Pro-Carton, ECMA European Carton Makers Association, Eurosac and CEPI Eurokraft on cartonboard, kraft paper and paper sacks. RISE, Research Institutes of Sweden, made possible the transfer of the data between the associations and ecoinvent.

#### Waste Treatment and Recycling <a href="#en-b0021" id="en-b0021"></a>

With version 3.7.1, the Waste Treatment and Recycling sector has been enhanced with new data on recycling activities of packaging materials, namely a range of new regional data for Europe and Switzerland on the recycling of beverage cans and paperboard. This update uses literature data from case studies published by ETH Zurichand Carbotech.

#### Building and Construction Materials <a href="#en-b0023" id="en-b0023"></a>

ecoinvent v3.7.1 includes an updated version of glass wool mat datasets from ISOVER Saint Gobain; the data submission was done by Werner Umwelt & Entwicklung. This branded glass wool mat is now modeled with two alternative adhesives in the database.

### Relevant Documents and Files <a href="#en-b0025" id="en-b0025"></a>

#### Report of Changes (pdf) <a href="#en-b0026" id="en-b0026"></a>

This report covers all changes made in the ecoinvent database between version 3.6 (2019) and version 3.7.1 (2020). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Report of Changes](../assets/1cebba817257-change-report_v3-7-1_20201217.pdf)

#### Report of Changes (xlsx) <a href="#en-b0029" id="en-b0029"></a>

This automatically generated excel file provides an overview of changes made on the undefined unit process datasets between versions 3.6 and 3.7.1 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of EcoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### Correspondence File <a href="#en-b0031" id="en-b0031"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.6 and 3.7.1 and matches corresponding datasets between versions.

An excel file listing all the activities and products present in the ecoinvent version 3.7.1 database including most of the metadata (geography, ISIC classification, activity type, technology level, product type, unit, etc.). This file also includes a list of all geographies, elementary and intermediate exchanges present in the database.

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Correspondence File](../assets/d0091c2e42d9-correspondence_file_eiv3.6_to_eiv3.7.1.xlsx)

#### Activity Overview for ecoinvent Version 3.7.1, Undefined <a href="#en-b0035" id="en-b0035"></a>

An excel file listing all the activities and products present in the ecoinvent version 3.7.1 database including most of the metadata (geography, ISIC classification, activity type, technology level, product type, unit, etc.). This file also includes a list of all geographies, elementary and intermediate exchanges present in the database.”).

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Activity Overview for ecoinvent v3.7.1., Undefined](../assets/dc982e5aca4c-activity_overview_3.7.1_undefined_public-1.xlsx)

#### <strong>Activity Overview for ecoinvent Version 3.7.1, APOS</strong> <a href="#en-b0038" id="en-b0038"></a>

An excel file listing all the activities present in the ecoinvent version 3.7 database including metadata related specifically to the Allocation at the point of substitution.

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Activity Overview for ecoinvent v3.7.1, APOS](../assets/f58f787d6a1b-activity_overview_3.7.1_allocation_apos_public.xlsx)

#### Activity Overview for ecoinvent Version 3.7.1, Consequential <a href="#en-b0041" id="en-b0041"></a>

An excel file listing all the activities present in the database including metadata related specifically to the Substitution, consequential, long-term system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Activity Overview for ecoinvent v3.7.1., Consequential](../assets/00a2d23a2e4e-activity_overview_3.7.1_consequential_public.xlsx)

#### Activity Overview for ecoinvent Version 3.7.1, Cut-Off <a href="#en-b0043" id="en-b0043"></a>

An excel file which lists all the activities present in the database including metadata related specifically to the Allocation, cut-off by classification system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Activity Overview for ecoinvent v3.7.1, Cut-Off](../assets/a1db8f35b9c8-activity_overview_3.7.1_allocation_cut_off_public.xlsx)

#### LCIA Methods in ecoinvent Version 3.7.1 <a href="#en-b0045" id="en-b0045"></a>

List of all LCIA methods including all the impact categories as well as list of selected LCI cumulative results provided by ecoinvent.

![doc-icon](../assets/024d8f149226-doc-icon.png)   See [LCIA Methods in ecoinvent v3.7.1](../assets/3ceafd157e8f-LCIA-methods-in-ecoinvent-3.7.1.xlsx)

### Known Issues <a href="#en-b0047" id="en-b0047"></a>

This section lists all known data errors in version 3.7.1 of the ecoinvent database.

#### Data Issues <a href="#en-b0048" id="en-b0048"></a>

- The activities “electricity voltage transformation from high to medium voltage” and “electricity voltage transformation from medium to low voltage” for the RoW geography appear in the Allocation, cut-off and APOS system model. As the RoW markets for electricity do not exist for these system models, the datasets have LCIA scores of zero and should not be used.
- The exchange amount of the input from the environment “Tellurium, in ground” (compartment: “natural resource”; subcompartment: “in ground”) in the activity “copper mine operation and beneficiation, sulfide ore” for the geographies AU, CA, CL, CN, ID, KZ, RU, US, and ZM was found to be inconsistent with the amount in the GLO geography. The exchange amounts in the local geographies have been scaled down based on the assumption that these geographies extract 70% of the global Te that is extracted in copper ores (modeled in the GLO dataset). The new amounts for the undefined datasets are listed in the table below. They will be available with the release of v3.9.

<table>
<tbody>
<tr>
<td><strong>Dataset</strong></td>
<td><strong>Unit</strong></td>
<td><strong>Previous Value</strong></td>
<td><strong>New Value</strong></td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, AU </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8968E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, CA </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9067E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, CL </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8997E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, CN </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9018E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, ID </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8935E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, KZ </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9096E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, RU </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8960E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, US </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.8973E-05 </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, ZM </p>
</td>
<td>kg</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9021E-05 </p>
</td>
</tr>
</tbody>
</table>

- The activity “treatment of wastewater from grass refinery, capacity 5E9l/year, RoW” is not available in the APOS system model. This does not have any impact on the scores, as the activity and the respective reference product are not used within the database.
- The dataset “glucose production, RER” has been erroneously excluded from this release. We recommend users to use the dataset “glucose production, GLO” and to adjust the supply chain to refer to RER activities. We will re-introduce it for version 3.8.
- The dataset “glued laminated timber production, average glue mix, CA-QC” has a wrong reference product, namely “glued laminated timber, for indoor use”. This reference product was renamed in version 3.7 to “glued laminated timber, average glue mix”. In version 3.7, no market for glued “laminated timber, for indoor use” exists.
- The transport distances in the market for sawnwood, board, softwood, dried (u=10%), planed, CH are incorrect. The exchange transport, freight, light commercial vehicle has to be deleted from the dataset. The exchange “transport, freight, lorry, unspecified” with an amount of 86.7105 metric ton\*km has to be added to the dataset.
- The amount of the reference product “spent sawing slurry from Si-wafer cutting” in the activities “treatment of spent sawing slurry from Si-wafer cutting, RER and GLO” is incorrect. The original single output unit processes can be found at the v2 report (Jungbluth, N., Stucki, M., Frischknecht, R. (2009). Photovoltaics. In Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz. Ecoinvent report No. 6-XII).
- The air freight transport datasets (“transport, freight, aircraft, dedicated freight, […] haul” and “transport, freight, aircraft, belly-freight, […] haul”) are updated within the release of ecoinvent v3.8 in collaboration with INFRAS, the original data provider. An updated project report (Notten P.J., Althaus H-J. and Cox B., (2021) Life cycle inventories of global air freight – Global, Update 2021. ecoinvent Association, Zürich, Switzerland) is accessible in the [SRI results](https://ecoinvent.org/activities/sri-project/) section of the ecoinvent website. More information can be found in the Report of Changes for version 3.8. Within the report users can find indication on how to correct the data and information on relevant changes in impact assessment.
- In the dataset “styrene production”, the benzene emissions to water and to air are too high. With support of PlasticsEurope, it could be established that the benzene emissions to water can be removed completely from the dataset and the benzene emissions to air were decreased to 2.0E-07 kg. A corrected inventory was introduced in version 3.8
- The dataset “methylene diphenyl diisocyanate production” (GLO and RER) treats the formed hydrochloric acid as a waste, this does not reflect reality. Hydrochloric acid is a valuable by-product which is used or sold by the MDI producer.The ecoinvent association advices users to either use the LCIA scores from the current [ecoProfile](https://plasticseurope.org/sustainability/circularity/life-cycle-thinking/eco-profiles-set/) available on the PlasticsEurope website or to correct the unit process in ecoinvent by removing the waste neutralisation and treating HCl as a by-product.   
  To correct the ecoinvent dataset, we would advise user to use the undefined dataset available through ecoQuery and remove the exchanges of the input of sodium hydroxide and the outputs of sodium and chloride.

#### <strong>Consequential system model issues</strong> <a href="#en-b0099" id="en-b0099"></a>

Three elementary exchanges are found in the compartment “social”. These exchanges can be ignored, both at the unit process and the inventory level, as ecoinvent does not yet account for social impacts.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **已处理／已说明 · b0035**：统一 Undefined 中文表述。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-079)
- **已处理／已说明 · b0037**：统一 Undefined 中文表述。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-080)
- **已处理／已说明 · b0050**：统一 compartment 的数据库结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-081)
- **已处理／已说明 · b0050**：统一 sub-compartment 的数据库结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-082)
- **已处理／已说明 · b0098**：明确 Undefined 中文含义。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-083)
- **已处理／已说明 · b0100**：统一 compartment 的数据库结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-084)
