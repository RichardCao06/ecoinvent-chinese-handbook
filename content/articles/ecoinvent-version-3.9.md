# ecoinvent 3.9 版

英文原题：ecoinvent Version 3.9  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.9)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-09-15

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库 3.9 版包含广泛更新，从为关键经济部门提供最新可用数据、扩展数据库的部门和地理覆盖范围，到改善用户体验。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.9 于 2022 年 10 月 13 日发布</strong>。了解如何[升级到最新版本](licensing.md)。

2023年10月28日

该版本已被 ecoinvent v3.9.1 替代，以修正可能影响某些方法的 LCIA 结果值或数据可用性的问题。

ecoinvent v3.9 改进了文档并进一步更新排放因子，整合 IPCC 2021 及其他 LCIA 方法。此外，数据库在 v3.9 中新增约 1,099 个数据集，更新约 1,876 个数据集，包括约 271 种新产品。

3.9 版更新的部门包括农业、电池、化学品、电力、金属、制浆造纸、石油天然气和废物。

<strong>重要信息</strong>

我们在数据库 3.9 版中发现了若干问题，涉及部分已发布数据，可能影响某些方法的 LCIA 结果值或数据可用性。

我们于 2022 年 12 月发布 3.9.1 版以修正这些问题。有关受影响的数据库部分及所作变更，请参阅[3.9.1 版发布页面](ecoinvent-version-3.9.1.md)。

<strong>建议 ecoinvent 用户自 v3.9.1 发布起采用该版本。</strong>不过，对于使用不受变更影响数据的用户，ecoinvent v3.9 仍可使用。

### 功能与文档 <a href="#zh-b0012" id="zh-b0012"></a>

#### 排放因子（LCIA 方法） <a href="#zh-b0013" id="zh-b0013"></a>

ecoinvent v3.9 整合 IPCC 2021，将[欧洲生命周期评价平台的 EF 方法更新到 v3.1](https://eplca.jrc.ec.europa.eu/EnvironmentalFootprint.html)，并实施 Ecological Scarcity（2021）、ReCiPe（2016）、TRACI v2.1 和 EPS（2020）的最新版本。v3.9 还首次向用户提供 Crustal Scarcity Indicator（2020，地壳稀缺性指标）。借助这些新增和更新的方法，v3.9 提供气候变化、矿产资源、土地利用、水资源耗竭、臭氧耗竭、淡水生态毒性等方面更新的排放结果值，以及以货币价值表示的影响结果值等。[了解这些方法的更多信息。](impact-assessment.md)

#### 产品信息 <a href="#zh-b0015" id="zh-b0015"></a>

自 v3.8 起，数据库中的全部产品和服务都有描述，帮助用户识别它们。这些信息包含数据库所采用的产品或服务定义；服务文档还包含如何使用服务的支持信息。到 v3.9，整个数据库的产品和服务信息更新与扩展已完成，包括改进的产品特征信息。多种 LCA 软件工具也实施了此功能，提高 LCA 实践者获得的信息透明度。更多信息请联系您的软件供应商。

#### 基本流交换的命名和标识符 <a href="#zh-b0017" id="zh-b0017"></a>

在参与[GLAD 项目](https://ecoinvent.org/projects/global-lca-data-access-glad-network/)后，ecoinvent v3.9 更新了全部基本流交换（环境流）的命名和标识符，包括交换名称、CAS 编号、化学式和同义词。更新后的基本流交换列表与其他数据库对应列表更加一致，帮助使用 ecoinvent 的建模人员更容易识别和选择评价所需数据。更新还提高了 ecoinvent 与全球其他数据库的互操作性，并加强环境影响评价合作。

### 新增和更新的数据 <a href="#zh-b0019" id="zh-b0019"></a>

#### 农业 <a href="#zh-b0020" id="zh-b0020"></a>

本部门更新引入加拿大和巴西生产的新作物数据。具体而言，v3.9 新增加拿大花斑菜豆、红芸豆、蚕豆和白芸豆等作物生产数据；新增巴西新产品（花生）生产数据，并更新咖啡、甘蔗、大豆和玉米等主要产品数据。这些更新的数据由不列颠哥伦比亚大学（加拿大）和 Embrapa（巴西）提供。ecoinvent 3.9 还新增和更新农药数据，可能影响农业过程和产品的评价结果。

#### 电池 <a href="#zh-b0022" id="zh-b0022"></a>

v3.9 继续改进数据库中的电池表示。今年更新新增“锂、铁、磷酸盐”（磷酸铁锂）电池技术数据集，将电池化学体系覆盖扩展到 5 种重要技术。这些数据集由瑞士联邦材料科学与技术实验室（EMPA）创建，包括此类电池的专用组件及磷酸铁锂生产。此外，电池隔膜和电解液数据集也进行了更新。

#### 建筑与施工 <a href="#zh-b0024" id="zh-b0024"></a>

v3.9 新增了使用再生骨料和废物混合骨料的水泥及混凝土数据。还为水泥和混凝土供应链引入新的命名规则，旨在确保所有地理区域的一致性、与行业标准名称一致，并建立清晰结构，帮助用户理解不同水泥和混凝土类型并为研究选择具备合适性能的产品。随着命名变更，全球水泥和混凝土生产数据集也进行了重组，仅保留全球地理区域中最具代表性的数据集。

#### 化学品和塑料 <a href="#zh-b0026" id="zh-b0026"></a>

化学品部门新增为 EF 倡议开发的 36 种化学产品，主要是农药和增塑剂，包括乙烯利、三氯吡氧乙酸和己二酸二辛酯。数据按照[ecoinvent 的方法](introduction-to-the-database.md)整合。

此外，v3.9 迈出了逐步改进数据库氢表示的第一步，新增欧洲和全球氢的主要生产技术（蒸汽重整）数据。

#### 电力 <a href="#zh-b0029" id="zh-b0029"></a>

v3.9 更新电力市场组合，以反映 2019 年状况；美国、加拿大和瑞士的电力组合更新为反映 2020 年状况。瑞士更新采用其国家数据，其余更新采用国际能源署（IEA）数据。

今年，中国、印度和巴西的电力组合也分别更新为反映 2020、2019 和 2020 年状况。更新采用国家统计，巴西数据由 ACV Brasil 提供。这些国家的全部子市场也进行了更新，以更准确地表示各地区电力状况。中国国家电网公司（SGCC）的电力组合细分为六个子区域，更好地反映当地情况。同时，数据库中的所有电力市场均作出调整，纳入这些更新。

v3.9 还更新输电网络数据，具体更新输电基础设施数据，并在电力市场数据集中反映。对于有可用数据的国家，还分别提供架空、地下和海底电缆数据。

v3.9 进一步引入基于发证机构协会（AIB）提供数据的剩余电力组合。

#### 金属 <a href="#zh-b0034" id="zh-b0034"></a>

此次更新通过新增和更新数据扩展金属部门覆盖。v3.9 引入锑、硼酸盐、锗、锆和铪等新金属产品数据。新增和更新数据集由瑞士联邦材料科学与技术实验室 EMPA 提供，并由瑞士联邦环境署 BAFU 资助。

#### 制浆造纸 <a href="#zh-b0036" id="zh-b0036"></a>

制浆造纸部门新增和更新用于包装材料及纸张生产的产品数据，包括行业协会数据。本次更新扩展数据的地理覆盖范围。更多信息见[此处](pulp-and-paper.md)。

#### 石油与天然气 <a href="#zh-b0038" id="zh-b0038"></a>

v3.9 对天然气和原油供应数据进行了全面修订。

具体更新数据库中天然气和原油供应链（生产、长距离运输及地区分销），以反映全球 2019 年供应状况。新增不同国家和地区的天然气和原油生产数据，扩展地理覆盖范围。总体上，数据库现覆盖全球原油生产的 90% 和天然气生产的近 80%。此外，更新引入北美和欧洲的地区原油消费组合，并根据 2019 年状况新增或更新 44 个国家的天然气供应。

更新整合世界银行全球天然气火炬燃烧减排伙伴关系（GGFR）的天然气火炬燃烧数据，以及国际能源署 Methane Tracker 2022 的天然气放空和逸散源甲烷排放数据。本次更新以瑞士联邦环境署（FOEN）、瑞士联邦能源署（SFOE）、瑞士天然气行业协会（Verband der Schweizerischen Gasindustrie，VSG）及 Avenergy Suisse（原 Erdöl-Vereinigung）委托的早期研究为基础，由 ecoinvent 协会委托 ESU-services Ltd. 编制。

#### 废物 <a href="#zh-b0042" id="zh-b0042"></a>

v3.9 引入废物部门全面修订的第一部分，将废水处理链细分，使用户能够查看废水处理副产品及其后续处理。

### 相关文档和文件 <a href="#zh-b0044" id="zh-b0044"></a>

#### 变更报告 <a href="#zh-b0045" id="zh-b0045"></a>

本报告涵盖数据库 3.8 版（2021）与 3.9 版（2022）之间的全部变更，包括数据库整体变更及部门特定变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/103695c5a046-Change-Report-v3.9.pdf)

#### 变更报告 <a href="#zh-b0048" id="zh-b0048"></a>

此自动生成的 Excel 文件概述数据库 3.8 与 3.9 版之间未指定系统模型的单元过程数据集的变更。变更报告 XLS 可在 ecoQuery（ecoinvent 第 3 版数据库在线版本）的“文件”（Files）部分获取，供数据库被许可人使用。

#### 对应关系文件 <a href="#zh-b0050" id="zh-b0050"></a>

对应关系文件是一份电子表格，列出 3.8 和 3.9 版全部数据集，并匹配两版本间相互对应的数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件](../assets/2d743037fc47-Correspondence-File-v3.8-v3.9.xlsx)

#### LCIA 实施报告 <a href="#zh-b0053" id="zh-b0053"></a>

LCIA 实施报告记录 3.9 版 LCIA 方法的实施。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[LCIA 实施报告](../assets/6976cb25e45b-LCIA_implementation_3.9.pdf)

#### 数据库概览文件 <a href="#zh-b0056" id="zh-b0056"></a>

数据库概览文件描述数据库内容，包含以下信息：

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[数据库概览文件](../assets/bd9f67e8b5ab-Database-Overview-for-ecoinvent-v3.9.xlsx)

#### 活动概览 <a href="#zh-b0059" id="zh-b0059"></a>

分别列出三种[系统模型](system-models.md)中包含的数据集，以及未链接和未分配的数据集。3.9 版为每个数据集分配了一个或多个部门，有助于筛选可能属于不同部门的数据集。

#### ecoinvent 地理区域 <a href="#zh-b0061" id="zh-b0061"></a>

数据库中使用的地理区域。每个地理区域均具有分类，并标明其所包含的地理区域。

#### LCIA 方法 <a href="#zh-b0063" id="zh-b0063"></a>

列出 ecoinvent 计算影响结果值所采用的 LCIA 方法，注明方法版本，并提供用于确定表征因子的原始来源。

### 已知问题 <a href="#zh-b0065" id="zh-b0065"></a>

此部分列出 ecoinvent 数据库 3.9 版的全部已知数据错误。

#### 数据问题 <a href="#zh-b0067" id="zh-b0067"></a>

- RER 和 GLO 的“refrigerant R134a production”数据集对三氯乙烯和四氯乙烯氢氟化两条路线建模，但四氯乙烯氢氟化已不再具有工业代表性。目前正在审查这些数据集。
- 全球地理区域的“polydimethylsiloxane production”、“dimethyldichlorosilane production”和“methylchloride production”数据集目前正在审查。文献表明，聚二甲基硅氧烷生产中形成的盐酸会循环回用，作为氯甲烷生产的输入。在当前 v3.9 中，聚二甲基硅氧烷生产形成的盐酸经中和后处置，而氯甲烷生产使用新制盐酸。
- GLO 和 RER 的“dimethyl sulfoxide production”（二甲基亚砜生产）数据集目前正在核查，以确保正确表示工业采用的技术。
- 氢市场目前正在审查。“hydrogen production, steam reforming”数据集已纳入 3.9 版，但这一新生产技术目前尚未向液氢市场供货。计划在后续版本中改进生产与消费组合，工作将包括气态和液态氢及其在不同行业用途的修订。
- 与目前的液态和气态氢市场相比，新引入的蒸汽重整数据集的全球变暖潜势（IPCC 2021）高出 5 倍以上。该 GWP 与文献一致（Antonini et al., 2020）。

- “carbon dioxide, in chemical industry”是氨生产的副产品，通过直接活动链接直接供应“urea production”。在 Consequential 系统模型中，它没有替代（边际）供应商，因此被删除。研究需要尿素生产所需 CO2 数量时，建议核查“urea production”的未指定系统模型（Undefined）形式：每生产 1 kg 尿素使用 0.77112 kg CO2。
- JP 的“market for natural gas, high pressure”数据集中，向“air/urban air close to ground”排放的“Mercury II”数量不正确。正确数量为 4.0788E-13 kg。
- “Allocation, cut-off, EN15804”系统模型数据集的“期末”（End of Period）字段日期不正确。正确日期可在[数据库概览](../assets/bd9f67e8b5ab-Database-Overview-for-ecoinvent-v3.9.xlsx)文件的“EN15804 AO”工作表中找到。
- GLO 和 RER 的“acrylic acid production”（丙烯酸生产）数据集目前正在核查。
- 对于下列数据集，“natural gas, high pressure”和“natural gas, low pressure”中间交换的数量对应于数据提供者最初定义的低位热值，该值列于交换的“heating value, net”（低位热值）属性。这些热值未反映 v3.9 更新采用的天然气新低位热值（36MJ/m3）。

<table>
<tbody>
<tr>
<td><p><strong>数据集</strong> </p></td>
<td><p><strong>地理区域</strong> </p></td>
</tr>
<tr>
<td>
<p>clinker production（熟料生产） </p>
</td>
<td>
<p>BR; CH; CO; PE </p>
</td>
</tr>
<tr>
<td>
<p>electricity production, natural gas, combined cycle power plant（天然气联合循环电厂发电） </p>
</td>
<td>
<p>AR; IN-AP; IN-AS; IN-DL; IN-GA; IN-GJ; IN-HR; IN-KL; IN-MH; IN-PY; IN-RJ; IN-TN; IN-TR; IN-UP </p>
</td>
</tr>
<tr>
<td>
<p>electricity production, natural gas, conventional power plant（天然气常规电厂发电） </p>
</td>
<td>
<p>AR; IN-AP; IN-AS; IN-DL; IN-GA; IN-GJ; IN-HR; IN-KL; IN-MH; IN-PY; IN-RJ; IN-TN; IN-TR; IN-UP </p>
</td>
</tr>
<tr>
<td>
<p>evaporation of natural gas（天然气蒸发） </p>
</td>
<td>
<p>BR </p>
</td>
</tr>
<tr>
<td>
<p>heat and power co-generation, natural gas, conventional power plant, 100MW electrical（天然气常规电厂热电联产，100MW 电功率） </p>
</td>
<td>
<p>AR </p>
</td>
</tr>
<tr>
<td>
<p>market for natural gas, high pressure（高压天然气市场） </p>
</td>
<td>
<p>BR </p>
</td>
</tr>
<tr>
<td>
<p>natural gas, burned in gas turbine, for compressor station（压缩站燃气轮机燃烧天然气） </p>
</td>
<td>
<p>CA-AB; CA-QC; GLO </p>
</td>
</tr>
<tr>
<td>
<p>natural gas, high pressure, import from BO（从 BO 进口的高压天然气） </p>
</td>
<td>
<p>BR; GLO </p>
</td>
</tr>
<tr>
<td>
<p>synthetic fuel production, from coal, high temperature Fisher-Tropsch operations（煤制合成燃料，高温费托工艺） </p>
</td>
<td>
<p>ZA </p>
</td>
</tr>
</tbody>
</table>

  

- 对于下列数据集，用户应将“natural gas, high pressure”的低位热值视为 36MJ/m3，而不是当前“heating value, net”属性的 39MJ/m3：

  

<table>
<tbody>
<tr>
<td><p><strong>数据集</strong> </p></td>
<td><p><strong>地理区域</strong> </p></td>
</tr>
<tr>
<td>
<p>hydrogen production, steam reforming（蒸汽重整制氢） </p>
</td>
<td>
<p>RER; GLO </p>
</td>
</tr>
<tr>
<td>
<p>kraft paper production（牛皮纸生产） </p>
</td>
<td>
<p>GLO </p>
</td>
</tr>
<tr>
<td>
<p>liquid packaging board production（液体包装纸板生产） </p>
</td>
<td>
<p>RER; GLO </p>
</td>
</tr>
<tr>
<td>
<p>steel production, electric, low-alloyed（电炉低合金钢生产） </p>
</td>
<td>
<p>GLO </p>
</td>
</tr>
</tbody>
</table>

部分子区室存在错误，影响结果值。受影响的活动和交换列于此[文件](../assets/320865b24326-known-issues_sub-compartments.xlsx)中，包括：  

- 部分数据集错误地将某些排放的子区室标为“long-term”（长期）。“long-term”子区室应专用于 100 年以后发生的排放，尤其用于填埋场（浸出，100-60’000 年）和铀矿开采及磨矿场（尾矿氡排放，100-80’000 年）。正确子区室应为“air/non-urban air or from high stacks”，而非“air/low population density, long-term”；以及“water/ground-”，而非“water/ground-, long-term”。
- 部分数据集错误地采用“air/lower stratosphere + upper troposphere”子区室，该子区室应专用于航空运输。正确子区室应为“air/unspecified”。

请谨慎使用所列活动的结果值。

  

<strong>生命周期影响评价</strong><strong>问</strong><strong>题</strong>

- ReCiPe 2016 的“total: …”类别结果值存在问题。这些总值与单项“human health|…”、“ecosystem quality|…”和“natural resources|…”类别／指标之和不一致，不应使用，也不应手工计算为这些数值之和。
- 在 ReCiPe 中点方法中，“climate change”影响类别的指标名称应为：“ReCiPe 2016 v1.03, midpoint (I)”对应“global warming potential (GWP20)”，“ReCiPe 2016 v1.03, midpoint (H)”对应“global warming potential (GWP100)”（“no LT”方法也如此）。
- 在 ReCiPe 中点方法中，“ionising radiation”影响类别的单位应为“kBq Co-60-Eq”，而非“kg Co-60-Eq”（“no LT”方法也如此）。
- 在 TRACI 方法中，“particulate matter formation”影响类别的单位应为“kg PM2.5-Eq”，而非“PM2.5-Eq”（“no LT”方法也如此）。
- 锂辉石（原文化学式：LiAl(SiO3)2）的锂含量为 0.0376。下列方法中，将锂的 CF 应用于锂辉石时，可将此值用作换算因子：  
    
  \* CML v4.8 2016  
  \* Ecological Scarcity 2021  
  \* EPS 2020d  
  \* ReCiPe 2016。  
    
  前三种方法尚未表征锂辉石；ReCiPe 2016 则错误地采用锂的 CF 和换算因子 1 进行表征。

<strong>系统模型问题</strong>

- 请注意，ecoinvent 3.9 当前不包含替代点分配（APOS）系统模型。

{% endtab %}

{% tab title="English 原文" %}

## Version 3.9 of the ecoinvent database includes a wide range of updates, from bringing the latest available data in key economic sectors and expanding the sectoral and geographical coverage of the database to improving the user experience. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.9 was released on October 13th, 2022</strong>. Discover how to [upgrade to our latest version](licensing.md).

Oct 28th, 2023

It was replaced by ecoinvent v3.9.1 to correct issues that potentially influence the LCIA scores of certain methods or the usability of the data.

ecoinvent v3.9 includes enhanced documentation and further updated emission factors, integrating the IPCC 2021, among other LCIA methods. Further, with ecoinvent v3.9 the ecoinvent database integrates around 1’099 new and 1’876 updated datasets, including around 271 new products.

Sectors updated with version 3.9 include Agriculture, Batteries, Chemicals, Electricity, Metals, Pulp and Paper, Oil and Gas, and Waste.

<strong>Important Information </strong>

We have identified some issues in version 3.9 of the ecoinvent database. They affected parts of the published data and can potentially influence the LCIA scores of certain methods or might affect the usability of the data.

We published version 3.9.1 in December 2022 to correct these issues. For more information about which parts of the database are concerned and about the changes that we have made, please refer to the [release page of version 3.9.1.](ecoinvent-version-3.9.1.md)

<strong>We recommend ecoinvent users to work with ecoinvent v3.9.1 from its release onwards.</strong> However, for ecoinvent users working with data that are not affected by the changes, ecoinvent v3.9 will remain available.

### Features & Documentation <a href="#en-b0012" id="en-b0012"></a>

#### Emission Factors (LCIA Methods) <a href="#en-b0013" id="en-b0013"></a>

ecoinvent v3.9 integrates IPCC 2021, updates the EF method by the [European Platform on Life Cycle Assessment to v3.1](https://eplca.jrc.ec.europa.eu/EnvironmentalFootprint.html), and implements the latest versions of Ecological Scarcity (2021), ReCiPe (2016), TRACI v2.1, EPS (2020). With ecoinvent v3.9, Crustal Scarcity Indicator (2020) is now offered to ecoinvent users for the first time. With these new and updated methods, ecoinvent v3.9 offers more up-to-date emission scores on climate change, mineral resources, land use, water depletion, ozone depletion, and freshwater ecotoxicity, as well as impact scores expressed in monetary values, among other things. [Find out more information on the methods .](impact-assessment.md)

#### Product Information <a href="#en-b0015" id="en-b0015"></a>

Since ecoinvent v3.8, all products and services included in the database include a description that supports users in identifying them. The information includes a definition of the product or service as seen in the database. At the same time, the documentation of the services incorporates supporting information on how to use them. With ecoinvent v3.9, the database-wide update and expansion of the information on products and services is now complete, including enhanced product characteristics. This feature is also implemented in various LCA software tools, offering enhanced transparency to LCA practitioners. Please contact your software provider for more information.

#### Nomenclature and Identifiers of Elementary Exchanges <a href="#en-b0017" id="en-b0017"></a>

Following ecoinvent’s participation in the [GLAD project](https://ecoinvent.org/projects/global-lca-data-access-glad-network/), ecoinvent v3.9 updates the nomenclature and identifiers of the complete list of elementary exchanges (environmental flows). Specifically, ecoinvent v3.9 updates names, CAS numbers, formulas, and synonyms of the exchanges. The result of this update is an improved list of elementary exchanges that is now more aligned with the respective lists of other databases. This helps modelers using the ecoinvent database to easier identify and choose the data needed for their assessments. This update also improves the interoperability of the ecoinvent database with other databases around the world and enhances collaboration in assessing environmental impacts.

### New and Updated Data <a href="#en-b0019" id="en-b0019"></a>

#### Agriculture <a href="#en-b0020" id="en-b0020"></a>

The sector features updates introducing data on new crops produced in Canada and Brazil. Specifically, ecoinvent v3.9 includes data on the production of new crops from Canada, such as pinto bean, red kidney bean, fava bean, and navy bean. Further, it introduces data on the production of new products (peanut) and updates data on the production of major products from Brazil, including coffee, sugar cane, soybean, and maize. Data for these updates were provided by the University of British Columbia (Canada) and Embrapa (Brazil). ecoinvent 3.9 also features new and updated data on pesticides, which may affect the results of assessments for agricultural processes and products.

#### Batteries <a href="#en-b0022" id="en-b0022"></a>

ecoinvent v3.9 continues the improvement of the representation of batteries in the ecoinvent database. This year’s update includes new datasets on the ‘Lithium, Iron, and Phosphate’ battery technology, thus, expanding the coverage of battery chemistries now including 5 important technologies. These datasets were created by the Swiss Federal Laboratories for Materials Science and Technology (EMPA) and include battery components specifically for this type of battery as well as the production of lithium iron phosphate. Complementary, the datasets for battery separator and electrolyte were updated.

#### Building and Construction <a href="#en-b0024" id="en-b0024"></a>

In ecoinvent v3.9, the sector is enhanced with new data for cement and concrete using recycled and waste mixed aggregates. Furthermore, new nomenclature rules have been introduced for the cement and concrete supply chains. The goal of these new rules is consistency across all geographies, alignment with the nomenclature used in industry standards and a clear structure that can facilitate the users understanding of the different cement and concrete types and the selection of the product with the right properties for their study. Along with the change in nomenclature, the global datasets for cement and concrete production have also been restructured and only the most representative datasets for the global geography have been maintained.

#### Chemicals and Plastics <a href="#en-b0026" id="en-b0026"></a>

The Chemicals sector is updated to include 36 new chemical products developed for the EF initiative, mainly pesticides and plasticizers, including ethephon, triclopyr, and dioctyl adipate. The data is integrated following the [ecoinvent approach](introduction-to-the-database.md).

Moreover, ecoinvent v3.9 takes the first step to gradually improve the representation of hydrogen in the ecoinvent database. Specifically, ecoinvent v3.9 introduces data on the main production technology for hydrogen (steam reforming) in Europe and the World.

#### Electricity <a href="#en-b0029" id="en-b0029"></a>

ecoinvent v3.9 updates the electricity market mixes to reflect the situation in 2019. In the case of the US, Canada, and Switzerland the electricity mixes are updated to reflect the situation in 2020. The update of the Swiss data is based on Swiss national data, while the rest of this update is based on data from the International Energy Agency (IEA).

This year, the electricity mixes for China, India, and Brazil are also updated to reflect the situation in the countries in 2020, 2019, and 2020 respectively. These updates are performed, based on national statistics, while in the case of Brazil the data was provided by ACV Brasil. Moreover, all submarkets in these countries are updated, thus better representing the electricity situation in the various regions. The electricity mix for State Grid Corporation of China (SGCC) was split into its six subregions, now better reflecting the local conditions. At the same time, all electricity markets in the ecoinvent database are adjusted to include these updates.

ecoinvent v3.9 also updates the data on electricity transmission networks. Specifically, this version updates the data on the infrastructure used for electricity transmission, which is also reflected in the electricity market datasets. For the countries where data is available, this update also introduces separate data for aerial, underground, and subsea cables.

ecoinvent v3.9 further introduces residual mixes, based on data provided by the Association of Issuing Bodies (AIB).

#### Metals <a href="#en-b0034" id="en-b0034"></a>

This update expands the data coverage of the Metals sector with new and updated data. Specifically, ecoinvent v3.9 introduces data on new metal products, including antimony, borates, germanium, zirconium and hafnium. New and updated datasets were provided by the Swiss Federal Laboratories for Materials Science and Technology, EMPA (sponsored by the Swiss Federal Office for the Environment, BAFU).

#### Pulp and Paper <a href="#en-b0036" id="en-b0036"></a>

The Pulp and Paper sector has been updated with new and updated on products used to produce packaging materials and paper, including data from industry associations. This update expands the geographical coverage of the data. Find more information [here](pulp-and-paper.md).

#### Oil and Gas <a href="#en-b0038" id="en-b0038"></a>

ecoinvent v3.9 introduces an extensive overhaul of the data on natural gas and crude petroleum oil supply.

Specifically, this version includes an update on the natural gas and crude petroleum oil supply chains (production, long-distance transport, and regional distribution) in the ecoinvent database to reflect the global supply situation in 2019. The geographical coverage in the database is expanded with data on the production of natural gas and crude petroleum oil in different countries and regions. When combined, the ecoinvent database now covers 90% of the global production of crude oil and nearly 80% of natural gas. In addition, the update introduces regional consumption mixes for crude petroleum oil to North America and Europe, alongside new or updated natural gas supply to 44 countries, based on the situation in 2019.

The update integrates data on the flaring of natural gas from the Global Gas Flaring Reduction Partnership (GGFR) of the World Bank and on methane emissions from gas venting and fugitive emission source from the International Energy Agency’s Methane Tracker 2022. Building on earlier studies commissioned by the Swiss Federal Office for the Environment (FOEN), the Swiss Federal Office for Energy (SFOE), the Swiss Gas Industry Association (Verband der Schweizerischen Gasindustrie, VSG), and Avenergy Suisse (previously Erdöl-Vereinigung), this update was commissioned by the ecoinvent Association and prepared by ESU-services Ltd.

#### Waste <a href="#en-b0042" id="en-b0042"></a>

ecoinvent v3.9 introduces the first part of the Waste sector overhaul. Specifically, this update disaggregates the wastewater treatment chains, allowing visibility of the by-products of waste-water treatment and its subsequent treatments.

### Relevant Documents and Files <a href="#en-b0044" id="en-b0044"></a>

#### Report of Changes <a href="#en-b0045" id="en-b0045"></a>

This report covers all changes made in the ecoinvent database between version 3.8 (2021) and version 3.9 (2022). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/103695c5a046-Change-Report-v3.9.pdf)

#### Report of Changes <a href="#en-b0048" id="en-b0048"></a>

This automatically generated excel file provides an overview of changes made on the undefined unit process datasets between versions 3.8 and 3.9 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### Correspondence File <a href="#en-b0050" id="en-b0050"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.8 and 3.9 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File](../assets/2d743037fc47-Correspondence-File-v3.8-v3.9.xlsx)

#### LCIA Implementation Report <a href="#en-b0053" id="en-b0053"></a>

The LCIA implementation report documents the implementation of LCIA methods for versions 3.9.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [LCIA Implementation Report](../assets/6976cb25e45b-LCIA_implementation_3.9.pdf)

#### Database Overview File <a href="#en-b0056" id="en-b0056"></a>

The database overview file describes the contents of the database. The following information is contained in the file:

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Database Overview File](../assets/bd9f67e8b5ab-Database-Overview-for-ecoinvent-v3.9.xlsx)

#### Activity Overview(s) <a href="#en-b0059" id="en-b0059"></a>

The lists of datasets contained in each of the three [system models](system-models.md), as well as the list of unlinked and unallocated datasets. For version 3.9, each dataset has been assigned to one or more sectors, which helps filter for datasets that can belong to different sectors.

#### ecoinvent Geographies <a href="#en-b0061" id="en-b0061"></a>

The geographies used in the ecoinvent database. Each geography is assigned a classification, and the geographies that are contained in each geography are indicated.

#### LCIA Methods <a href="#en-b0063" id="en-b0063"></a>

The list of the LCIA methods for which ecoinvent calculates impact scores. The version of the methods is indicated, and the original source used for defining the characterization factors is provided.

### Known Issues <a href="#en-b0065" id="en-b0065"></a>

This section lists all known data errors in version 3.9 of the ecoinvent database.

#### Data Issues <a href="#en-b0067" id="en-b0067"></a>

- The dataset “refrigerant R134a production” for the RER and GLO geography models two pathways, the hydrofluorination of trichloroethylene and tetrachloroethylene, although hydrofluorination of tetrachloroethylene is no longer industrially relevant. The datasets are currently under review.
- The datasets “polydimethylsiloxane production”, “dimethyldichlorosilane production” and “methylchloride production” for the Global geography are currently under review. Literature suggests that the hydrochloric acid, which is formed in the polydimethylsiloxane production, is recirculated to use as an input in the methylchloride production. In the current version of ecoinvent v3.9, the hydrochloric acid formed in the polydimethylsiloxane production is neutralised and disposed, whilst the methylchloride production uses virgin hydrochloric acid.
- The dataset “dimethyl sulfoxide production” for the GLO and RER geography is currently under investigation to ensure it properly represents the industrially applied technology.
- The hydrogen market is currently under review. The dataset “hydrogen production, steam reforming” is included in version 3.9. The new production technology for now does not contribute to the market for hydrogen, liquid, the improvement of production and consumption mixes are planned for the following releases. The work will include the revision of hydrogen in both gaseous and liquid form and its utilisation in different industries.
- Compared to the current hydrogen markets – liquid and gaseous – the newly introduced steam reforming dataset has a global warming potential (IPCC 2021) which is more than 5 times higher. This GWP is in accordance with literature (Antonini et al., 2020).

- “carbon dioxide, in chemical industry” is by-produced from ammonia production and directly supplies “urea production” with direct activity links. In the Consequential system model, “carbon dioxide, in chemical industry” has no alternative (marginal) supplier and thus it is dropped. Users are encouraged to check the undefined version of “urea production” in case the amount of CO2 (0.77112 kg of CO2 used per kg of Urea produced) needed to produce urea is needed for their study.
- The amount of ‘Mercury II’ to air/urban air close to ground is incorrect in the dataset “market for natural gas, high pressure” for JP. The correct amount is 4.0788E-13 kg.
- The field “End of Period” in the datasets of the system model “Allocation, cut-off, EN15804” displays an incorrect date. The correct “End of Period” date can be found in the [Database overview](../assets/bd9f67e8b5ab-Database-Overview-for-ecoinvent-v3.9.xlsx) file in the tab “EN15804 AO”
- The dataset “acrylic acid production” for the GLO and RER geography is currently under investigation.
- For the datasets listed below, the amount of the intermediate exchanges of “natural gas, high pressure” and “natural gas, low pressure” corresponds to the Lower Heating Value that was initially defined by the data provider and is indicated in the property ‘heating value, net’ of these exchanges. The amount of these heating values does not reflect the new Lower Heating Value of natural gas (36MJ/m3) implemented with the v3.9 update.

<table>
<tbody>
<tr>
<td>
<p><strong>Dataset</strong> </p>
</td>
<td>
<p><strong>Geography</strong> </p>
</td>
</tr>
<tr>
<td>
<p>clinker production </p>
</td>
<td>
<p>BR; CH; CO; PE </p>
</td>
</tr>
<tr>
<td>
<p>electricity production, natural gas, combined cycle power plant </p>
</td>
<td>
<p>AR; IN-AP; IN-AS; IN-DL; IN-GA; IN-GJ; IN-HR; IN-KL; IN-MH; IN-PY; IN-RJ; IN-TN; IN-TR; IN-UP </p>
</td>
</tr>
<tr>
<td>
<p>electricity production, natural gas, conventional power plant </p>
</td>
<td>
<p>AR; IN-AP; IN-AS; IN-DL; IN-GA; IN-GJ; IN-HR; IN-KL; IN-MH; IN-PY; IN-RJ; IN-TN; IN-TR; IN-UP </p>
</td>
</tr>
<tr>
<td>
<p>evaporation of natural gas </p>
</td>
<td>
<p>BR </p>
</td>
</tr>
<tr>
<td>
<p>heat and power co-generation, natural gas, conventional power plant, 100MW electrical </p>
</td>
<td>
<p>AR </p>
</td>
</tr>
<tr>
<td>
<p>market for natural gas, high pressure </p>
</td>
<td>
<p>BR </p>
</td>
</tr>
<tr>
<td>
<p>natural gas, burned in gas turbine, for compressor station </p>
</td>
<td>
<p>CA-AB; CA-QC; GLO </p>
</td>
</tr>
<tr>
<td>
<p>natural gas, high pressure, import from BO </p>
</td>
<td>
<p>BR; GLO </p>
</td>
</tr>
<tr>
<td>
<p>synthetic fuel production, from coal, high temperature Fisher-Tropsch operations </p>
</td>
<td>
<p>ZA </p>
</td>
</tr>
</tbody>
</table>

  

- For the following datasets, the user should consider as a LHV for “natural gas, high pressure” 36MJ/m3 instead of 39MJ/m3 that is currently the value of the property ‘heating value, net’:

  

<table>
<tbody>
<tr>
<td>
<p><strong>Dataset</strong> </p>
</td>
<td>
<p><strong>Geography</strong> </p>
</td>
</tr>
<tr>
<td>
<p>hydrogen production, steam reforming </p>
</td>
<td>
<p>RER; GLO </p>
</td>
</tr>
<tr>
<td>
<p>kraft paper production </p>
</td>
<td>
<p>GLO </p>
</td>
</tr>
<tr>
<td>
<p>liquid packaging board production </p>
</td>
<td>
<p>RER; GLO </p>
</td>
</tr>
<tr>
<td>
<p>steel production, electric, low-alloyed </p>
</td>
<td>
<p>GLO </p>
</td>
</tr>
</tbody>
</table>

There are mistakes in sub-compartments, which affect scores. The concerned activities and exchanges are listed in this [file](../assets/320865b24326-known-issues_sub-compartments.xlsx). They include:  

- datasets that mistakenly have a sub-compartment with the label “long-term” for some emissions. “long-term” sub-compartments are meant to be reserved for emissions occurring after 100 years, in particular they are used for landfill sites (leaching, 100-60’000 years) and uranium mining and milling sites (radon emissions from tailings, 100-80’000 years). The correct sub-compartment would be “air/non-urban air or from high stacks” instead of “air/low population density, long-term” and “water/ground-“ instead of “water/ground-, long-term”.
- datasets that mistakenly have the sub-compartment “air/lower stratosphere + upper troposphere”, which is meant to be reserved for air transport. The correct sub-compartment would be “air/unspecified”.

Please be careful with scores for the activities listed.

  

<strong>Life Cycle Impact Assessment </strong><strong>I</strong><strong>ssues</strong>

- There are issues with the scores for “total: …” categories in ReCiPe 2016. These totals don’t match the sum of the single “human health|…”, “ecosystem quality|…” and “natural resources|…” categories|indicators and should not be used or calculated manually as these sums.
- In the ReCiPe midpoint methods, the indicator names for the “climate change” impact category should be “global warming potential (GWP20)” for “ReCiPe 2016 v1.03, midpoint (I)” and “global warming potential (GWP100)” for “ReCiPe 2016 v1.03, midpoint (H)” (also for “no LT”).
- In the ReCiPe midpoint methods, the unit for the “ionising radiation” impact category should be “kBq Co-60-Eq” instead of “kg Co-60-Eq” (also for “no LT”).
- In the TRACI method, the unit for the “particulate matter formation” impact category should be “kg PM2.5-Eq” instead of “PM2.5-Eq” (also for “no LT”).
- Spodumene (LiAl(SiO3)2 has a Lithium content of 0.0376. This value can be used as a conversion factor when applying the CF of Lithium to Spodumene in the following methods:  
    
  \* CML v4.8 2016  
  \* Ecological Scarcity 2021  
  \* EPS 2020d  
  \* ReCiPe 2016.  
    
  In the first three methods, Spodumene is not yet characterized; in ReCiPe 2016, it was wrongly characterized with the CF for Lithium (and a conversion factor of 1).

<strong>System Model Issues</strong>

- Please note that, currently, ecoinvent 3.9 does not include the Allocation at the Point of Substitution (APOS) system model.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0113**：原文语法上禁止使用并禁止手工求和，但可能本意是“不应使用，应手工求和”。两种解读对用户操作影响重大，译文严格保留原文禁止措辞。 请向方法实施人员确认是禁止手工求和还是建议手工求和，并修订原文。 [查看完整记录](../review/issues.md#issue-092)
- **已处理／已说明 · b0073**：明确 Undefined 原始数据形式。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-093)
- **已处理／已说明 · b0077**：统一 heating value, net 为低位热值。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-094)
- **已处理／已说明 · b0109**：统一 compartment/sub-compartment 结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-095)
- **已处理／已说明 · b0109**：统一 sub-compartment 结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-096)
- **已处理／已说明 · b0110**：统一 sub-compartment 结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-097)
- **已处理／已说明 · b0120**：统一 compartment/sub-compartment 结构术语。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-098)
