# ecoinvent 第 3.9.1 版

英文原题：ecoinvent Version 3.9.1  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.9.1)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-09-25

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.9.1 包含与 v3.9 相同的新增和更新数据集，同时纳入重要修正。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.9.1 于 2022 年 12 月 15 日发布</strong>。了解如何[升级到我们的最新版本](licensing.md)。

2023 年 10 月 29 日

第 3.9.1 版更新对某些 LCIA 方法的表征因子作出重要修正，并解决不确定性数据问题以及交换层面缺失元数据的问题。此更新于 2022 年 12 月发布，旨在修正 ecoinvent 第 3.9 版中发现的问题。这些问题可能影响某些方法的 LCIA 得分及数据可用性。

ecoinvent 第 3.9 版完善了文档并进一步更新排放因子，整合了 IPCC 2021 及其他 LCIA 方法。同时纳入约 1’099 个新增和 1’876 个更新数据集，包括约 271 种新产品。第 3.9 版更新的行业包括农业、电池、化学品、电力、金属、纸浆与纸、石油与天然气以及废物。

经确认，ecoinvent v3.9 包含可能影响某些方法 LCIA 得分或数据可用性的问题。

### 第 3.9 版至第 3.9.1 版的变化列表 <a href="#zh-b0008" id="zh-b0008"></a>

- <strong>全球变暖潜势指标变化</strong>  
  我们修正了以下方法中评价全球变暖潜势的指标的表征因子（包括相应“no LT”版本）：

- - <strong>ReCiPe 2016 v1.03</strong>
  - <strong>TRACI v2.1</strong>
  - <strong>EPS 2020d</strong>

这些修正导致按分类截断的分配模型（“Allocation, cut-off”）和后果型模型（“Consequential”）的 LCIA 得分显著变化，也影响“ReCiPe 2016 v1.03”方法的“total”指标。

其他评价全球变暖潜势的指标（例如 IPCC 2013 和 IPCC 2021、EF 3.0 和 EF 3.1）的得分均未较第 3.9 版发生变化。

- <strong>生态毒性和人体毒性指标变化</strong>  
  我们修订了某些 LCIA 方法中金属和农用化学品排放的表征因子。这使所有系统模型中下列方法评价生态毒性和人体毒性的指标的 LCIA 得分明显变化（包括相应“no LT”版本）：

- - <strong>CML v4.8 2016</strong>
  - <strong>EF v3.0 和 EF v3.1（包括相应 EN15804 版本）</strong>
  - <strong>TRACI v2.1</strong>

- <strong>EF v3.0 和 v3.1 海洋富营养化指标变化</strong>  
  我们从 EF v3.0 和 v3.1 方法（包括相应 EN15804 版本）的海洋富营养化指标中，移除了部分氮排放的表征因子。这使所有系统模型中该指标的 LCIA 得分明显下降。
- <strong>“ReCiPe 2016 v1.03”和“TRACI v2.1”名称或单位修正</strong>  
  我们修正了“ReCiPe 2016 v1.03”和“TRACI v2.1”方法中部分指标的名称或单位。这些修正不影响 LCIA 得分。

- <strong>数据集修正</strong>  
  JP（日本）的“market for natural gas, high pressure”数据集向空气排放“Mercury II”的数量有误。我们在第 3.9.1 版进行了修正，使评价人体毒性和向空气排放重金属的指标的 LCIA 得分下降。这些得分变化仅影响直接或间接消费该市场产品的数据集。
- <strong>不确定性数据“variance”数值变化</strong>  
  第 3.9 版中，使用对数正态分布时，“variance”字段含有错误值。这涉及可具有不确定性数据的所有数量类型（交换量、属性量、生产量和参数）。我们在 v3.9.1 中进行了修正。“varianceWithPedigreeUncertainty”字段未改变，且在第 3.9 版中是正确的。
- <strong>新增交换元数据信息</strong>  
  交换的部分元数据字段未包含在单元过程数据中（例如交换注释、生产量注释等）。我们已将其纳入第 3.9.1 版发布的数据。
- <strong>移除生产可回收材料的数据集</strong>  
  ecoinvent v3.9 中部分数据集在 Cut-off 和 EN15804 系统模型中生产可回收材料。由于这些数据集本不应存在，我们已在第 3.9.1 版将其移除。
- <strong>EN15804 数据集结束日期修正</strong>  
  EN15804 数据集结束日期的年份与其他系统模型所用年份不一致。我们已在第 3.9.1 版修正。

  

有关这些变化及其对 LCIA 得分影响的更详细说明，请参阅[变更报告](../assets/0c8a26bab4bd-Change-Report-v3.9.1.pdf)。

### 功能与文档 <a href="#zh-b0023" id="zh-b0023"></a>

#### 排放因子（LCIA 方法） <a href="#zh-b0024" id="zh-b0024"></a>

ecoinvent v3.9 整合了 IPCC 2021，将[欧洲生命周期评价平台的 EF 方法更新至 v3.1](https://eplca.jrc.ec.europa.eu/)，并实施生态稀缺性（2021）、ReCiPe（2016）、TRACI v2.1 和 EPS（2020）的最新版本。通过 ecoinvent v3.9，用户首次获得地壳稀缺性指标（2020）。采用这些新增和更新方法后，ecoinvent v3.9 提供了更及时的气候变化、矿产资源、土地利用、水资源耗竭、臭氧耗竭和淡水生态毒性等排放影响得分，以及用货币值表示的影响得分等。[进一步了解 ecoinvent 数据库包含的方法。](impact-assessment.md)

#### 产品信息 <a href="#zh-b0026" id="zh-b0026"></a>

自 ecoinvent v3.8 起，数据库中所有产品和服务均附有帮助用户识别的描述，包括数据库所采用的产品或服务定义。同时，服务文档包含使用方式的辅助信息。通过 ecoinvent v3.9，数据库范围内产品与服务信息的更新和扩充现已完成，包括更完善的产品特征。这一功能也在多种 LCA 软件工具中实施，为 LCA 从业人员提供更高透明度。详情请联系您的软件提供商。

#### 基本流交换的命名与标识符 <a href="#zh-b0028" id="zh-b0028"></a>

在 ecoinvent 参与[GLAD 项目](https://ecoinvent.org/projects/global-lca-data-access-glad-network/)后，ecoinvent v3.9 更新了全部基本流交换（环境流）列表的命名与标识符。具体而言，更新了交换名称、CAS 号、化学式和同义词。更新后的基本流交换列表得到改善，与其他数据库相应列表更加一致。这帮助使用 ecoinvent 数据库的建模人员更容易识别和选择评价所需数据，也提高数据库与全球其他数据库的互操作性，加强环境影响评价方面的协作。

### 新增与更新的数据 <a href="#zh-b0030" id="zh-b0030"></a>

#### 农业 <a href="#zh-b0031" id="zh-b0031"></a>

该行业更新引入加拿大和巴西生产的新作物数据。具体而言，ecoinvent v3.9 包含加拿大花斑豆、红腰豆、蚕豆和白芸豆等新作物生产数据，还引入巴西新产品花生的生产数据，并更新咖啡、甘蔗、大豆和玉米等巴西主要产品生产数据。这些更新数据由不列颠哥伦比亚大学（加拿大）和 Embrapa（巴西）提供。ecoinvent 3.9 还包含农药新增与更新数据，可能影响农业过程及产品的评价结果。

#### 电池 <a href="#zh-b0033" id="zh-b0033"></a>

ecoinvent v3.9 继续改进数据库中的电池表示。本年度更新新增磷酸铁锂电池技术数据集，扩充电池化学体系覆盖，目前包含 5 种重要技术。这些数据集由瑞士联邦材料科学与技术实验室（EMPA）创建，包含该类型电池专用部件及磷酸铁锂生产。此外，电池隔膜和电解液数据集也已更新。

#### 建筑与施工 <a href="#zh-b0035" id="zh-b0035"></a>

在 ecoinvent v3.9 中，该行业新增使用再生及废弃混合骨料的水泥与混凝土数据。此外，水泥与混凝土供应链引入了新的命名规则。其目标是使各地理区域命名一致，与行业标准命名对齐，并建立清晰结构，方便用户理解不同水泥和混凝土类型、选择属性适合其研究的产品。在更改命名的同时，还重构了水泥与混凝土生产的全球数据集，仅保留最能代表全球地理区域的数据集。

#### 化学品与塑料 <a href="#zh-b0037" id="zh-b0037"></a>

化学品行业更新纳入为 EF 倡议开发的 36 种新化学产品，主要是农药和增塑剂，包括乙烯利、三氯吡氧乙酸和己二酸二辛酯。

此外，ecoinvent v3.9 迈出了逐步改进数据库中氢气表示的第一步，具体引入了欧洲和全球的主要制氢技术（蒸汽重整）数据。

#### 电力 <a href="#zh-b0040" id="zh-b0040"></a>

ecoinvent v3.9 更新电力市场组合，以反映 2019 年情况。美国、加拿大和瑞士的电力组合则更新为反映 2020 年情况。瑞士数据更新基于该国国家数据，其余更新基于国际能源署（IEA）数据。

本年度，中国、印度和巴西的电力组合也分别更新，以反映 2020 年、2019 年和 2020 年的情况。这些更新依据国家统计数据进行，巴西的数据由 ACV Brasil 提供。此外，这些国家的所有子市场均已更新，以更好地表示各地区电力情况。中国国家电网公司（SGCC）的电力组合划分为六个子区域，更好地反映本地条件。同时，数据库中所有电力市场均调整以纳入这些更新。

ecoinvent v3.9 还更新了输电网络数据，具体更新输电基础设施数据，并在电力市场数据集中体现。对于有数据的国家，还新增架空、地下和海底电缆的独立数据。

ecoinvent v3.9 还基于签发机构协会（AIB）提供的数据引入剩余电力组合（residual mixes）。

#### 金属 <a href="#zh-b0045" id="zh-b0045"></a>

此次更新通过新增和更新数据扩充了金属行业覆盖，具体而言，ecoinvent v3.9 新增锑、硼酸盐、锗、锆和铪等金属产品数据。新增和更新数据集由瑞士联邦材料科学与技术实验室（EMPA）提供，获瑞士联邦环境局（BAFU）资助。

#### 纸浆与纸 <a href="#zh-b0047" id="zh-b0047"></a>

纸浆与纸行业新增并更新了用于生产包装材料和纸的产品，包括来自行业协会的数据。此次更新扩大了数据的地理覆盖。详情见[此处](pulp-and-paper.md)。

#### 石油与天然气 <a href="#zh-b0049" id="zh-b0049"></a>

ecoinvent v3.9 对天然气和原油供应数据进行了全面修订。

具体而言，该版本更新了数据库中天然气和原油供应链（生产、长距离运输和区域分配），以反映 2019 年全球供应情况。数据库新增不同国家和地区天然气及原油生产数据，扩大地理覆盖。合计而言，ecoinvent 数据库现覆盖全球原油产量的 90% 和天然气产量的近 80%。此外，更新引入北美和欧洲原油的区域消费组合，并依据 2019 年情况，新增或更新 44 个国家的天然气供应数据。

此次更新纳入世界银行全球天然气火炬燃烧减排伙伴关系（GGFR）的天然气火炬燃烧数据，以及国际能源署《甲烷追踪报告 2022》中天然气放空及逸散源甲烷排放数据。在瑞士联邦环境局（FOEN）、瑞士联邦能源局（SFOE）、瑞士天然气工业协会（Verband der Schweizerischen Gasindustrie，VSG）和 Avenergy Suisse（原 Erdöl-Vereinigung）早期委托研究的基础上，此次更新由 ecoinvent 协会委托 ESU-services Ltd. 编制。

#### 废物 <a href="#zh-b0053" id="zh-b0053"></a>

ecoinvent v3.9 引入废物行业全面修订的第一部分。具体而言，此次更新拆分废水处理链，使废水处理副产品及后续处理过程可见。

### 相关文档与文件 <a href="#zh-b0055" id="zh-b0055"></a>

#### 变更报告 <a href="#zh-b0056" id="zh-b0056"></a>

本报告涵盖 ecoinvent 数据库第 3.9 版（2022 年）至第 3.9.1 版（2022 年）之间的所有变化。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[变更报告](../assets/0c8a26bab4bd-Change-Report-v3.9.1.pdf)

#### 变更报告 <a href="#zh-b0059" id="zh-b0059"></a>

此自动生成的 Excel 文件概览 ecoinvent 数据库第 3.9 版至第 3.9.1 版之间未指定系统模型的单元过程数据集的变化。XLS 变更报告可在 ecoQuery（ecoinvent 数据库第 3 版的在线版本）的“文件”（Files）部分找到，向数据库许可证持有人提供。

#### 对应关系文件 <a href="#zh-b0061" id="zh-b0061"></a>

对应关系文件是一个电子表格，列出第 3.8 版和第 3.9.1 版的全部数据集，并匹配不同版本之间的对应数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[对应关系文件](../assets/0439269e189d-Correspondence-File-v3.8-v3.9.1-1.xlsx)

#### LCIA 实施报告 <a href="#zh-b0064" id="zh-b0064"></a>

LCIA 实施报告记录第 3.9 版和第 3.9.1 版 LCIA 方法的实施。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[LCIA 实施报告](../assets/bfc333634386-LCIA_implementation_3.9-and-3.9.1.pdf)

#### 数据库概览文件 <a href="#zh-b0067" id="zh-b0067"></a>

数据库概览文件描述数据库内容，包含以下信息：

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[数据库概览文件](../assets/34bb93e02a6f-Database-Overview-for-ecoinvent-v3.9.1-9.xlsx)

#### 活动概览 <a href="#zh-b0070" id="zh-b0070"></a>

三个[系统模型](system-models.md)各自的数据集列表，以及未链接和未分配数据集列表。在第 3.9.1 版中，每个数据集都已归入一个或多个行业，便于筛选可能属于不同领域的数据集。

#### ecoinvent 地理区域 <a href="#zh-b0072" id="zh-b0072"></a>

ecoinvent 数据库所用的地理区域。每个地理区域均赋予分类，并标明其所包含的地理区域。

#### LCIA 方法 <a href="#zh-b0074" id="zh-b0074"></a>

ecoinvent 为之计算影响得分的 LCIA 方法列表，包括方法版本，以及用于定义表征因子的原始来源。

本部分列出 ecoinvent 数据库第 3.9.1 版中的全部已知数据错误。

### 数据问题 <a href="#zh-b0077" id="zh-b0077"></a>

- RER 和 GLO 地理区域的“refrigerant R134a production”数据集对三氯乙烯和四氯乙烯氢氟化两条路线建模，但四氯乙烯氢氟化已不再与工业实际相关。目前正在审核这些数据集。

- 全球地理区域的“polydimethylsiloxane production”“dimethyldichlorosilane production”和“methylchloride production”数据集目前正在审核。文献表明，聚二甲基硅氧烷生产形成的盐酸会循环利用，作为氯甲烷生产的投入。当前 ecoinvent v3.9.1 中，聚二甲基硅氧烷生产形成的盐酸被中和并处置，而氯甲烷生产使用原生盐酸。
- GLO 和 RER 地理区域的“dimethyl sulfoxide production”数据集目前正在调查，以确保正确表示工业应用的技术。
- 氢市场目前正在审核。第 3.9.1 版包含“hydrogen production, steam reforming”数据集，但这一新生产技术暂未向液氢市场供给。计划在后续发布中改进生产和消费组合，包括修订气态和液态氢及其在不同行业的应用。
- 与当前液态及气态氢市场相比，新引入的蒸汽重整数据集的全球变暖潜势（IPCC 2021）高出 5 倍以上。这一 GWP 与文献一致（Antonini 等，2020 年）。
- “Carbon dioxide, in chemical industry”是氨生产的副产品，并通过直接活动链接直接供应“urea production”。在后果型系统模型中，“carbon dioxide, in chemical industry”没有替代的边际供应商，因此被删除。如果研究需要生产尿素所需的 CO2 数量（每生产 1 kg 尿素使用 0.77112 kg CO2），建议用户查看未指定系统模型版本的“urea production”。

- GLO 和 RER 地理区域的“acrylic acid production”数据集目前正在调查。
- 对于下列数据集，“natural gas, high pressure”和“natural gas, low pressure”中间交换的数量对应数据提供者最初定义的低位热值，并在这些交换的“heating value, net”属性中注明。这些热值未反映 v3.9.1 更新采用的天然气新低位热值（36MJ/m3）。

<table>
<tbody>
<tr>
<td>
<p><strong>数据集</strong> </p>
</td>
<td>
<p><strong>地理区域</strong> </p>
</td>
</tr>
<tr>
<td><p>clinker production（熟料生产） </p></td>
<td><p>BR; CH; CO; PE </p></td>
</tr>
<tr>
<td><p>electricity production, natural gas, combined cycle power plant（天然气联合循环电厂发电） </p></td>
<td><p>AR; IN-AP; IN-AS; IN-DL; IN-GA; IN-GJ; IN-HR; IN-KL; IN-MH; IN-PY; IN-RJ; IN-TN; IN-TR; IN-UP </p></td>
</tr>
<tr>
<td><p>electricity production, natural gas, conventional power plant（天然气常规电厂发电） </p></td>
<td><p>AR; IN-AP; IN-AS; IN-DL; IN-GA; IN-GJ; IN-HR; IN-KL; IN-MH; IN-PY; IN-RJ; IN-TN; IN-TR; IN-UP </p></td>
</tr>
<tr>
<td><p>evaporation of natural gas（天然气气化） </p></td>
<td><p>BR </p></td>
</tr>
<tr>
<td><p>heat and power co-generation, natural gas, conventional power plant, 100MW electrical（天然气常规电厂热电联产，电功率 100MW） </p></td>
<td><p>AR </p></td>
</tr>
<tr>
<td><p>market for natural gas, high pressure（高压天然气市场） </p></td>
<td><p>BR </p></td>
</tr>
<tr>
<td><p>natural gas, burned in gas turbine, for compressor station（用于压气站的天然气在燃气轮机中燃烧） </p></td>
<td><p>CA-AB; CA-QC; GLO </p></td>
</tr>
<tr>
<td><p>natural gas, high pressure, import from BO（从 BO 进口的高压天然气） </p></td>
<td><p>BR; GLO </p></td>
</tr>
<tr>
<td><p>synthetic fuel production, from coal, high temperature Fisher-Tropsch operations（煤基高温费托合成燃料生产） </p></td>
<td><p>ZA </p></td>
</tr>
</tbody>
</table>

  

- 对于下列数据集，用户应将“natural gas, high pressure”的低位热值视为 36MJ/m3，而不是目前“heating value, net”属性中的 39MJ/m3：

<table>
<tbody>
<tr>
<td>
<p><strong>数据集</strong> </p>
</td>
<td>
<p><strong>地理区域</strong> </p>
</td>
</tr>
<tr>
<td><p>hydrogen production, steam reforming（蒸汽重整制氢） </p></td>
<td><p>RER; GLO </p></td>
</tr>
<tr>
<td><p>kraft paper production（牛皮纸生产） </p></td>
<td><p>GLO </p></td>
</tr>
<tr>
<td><p>liquid packaging board production（液体包装纸板生产） </p></td>
<td><p>RER; GLO </p></td>
</tr>
<tr>
<td><p>steel production, electric, low-alloyed（电炉低合金钢生产） </p></td>
<td><p>GLO </p></td>
</tr>
</tbody>
</table>

- 在废水处理数据集的水平衡中发现了一个错误，涉及排放到环境中地表水子区室的水量。它主要影响全球（GLO）地理区域的数据集，对区域数据集的影响几乎可忽略。此问题将在下一个版本 3.10 中修正。

  同时，将在所有废水处理数据集中添加“Non-hazardous waste disposed”交换，作为清单指标，以方便 EN15804 系统模型实施。最后，随着用于生成处理数据集的内部废物工具更新，还将调整能源消耗。附件 Excel 文件列出将纳入第 3.10 版的全部变化。

  ![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[废水处理活动中水平衡失衡的已知问题](../assets/adb816446555-known-issue-v3.9.1-water-imbalances-in-wastewater-treatment-activities.xlsx)

#### LCIA 问题 <a href="#zh-b0118" id="zh-b0118"></a>

- ReCiPe 2016 的“total: …”类别得分存在问题。这些总值与各“human health|…”“ecosystem quality|…”和“natural resources|…”类别/指标之和不一致，不应使用这些总值，也不应将它们按这些分项之和手动计算。
- 子区室中存在影响得分的错误。受影响的活动和交换列于此[文件](../assets/34bb93e02a6f-Database-Overview-for-ecoinvent-v3.9.1-9.xlsx)，包括：

- 部分数据集错误地为某些排放使用带“long-term”标记的子区室。“long-term”子区室应仅用于 100 年后发生的排放，尤其是填埋场（渗滤，100–60’000 年）和铀矿开采与选矿场（尾矿氡排放，100–80’000 年）。正确子区室应为“air/non-urban air or from high stacks”，而非“air/low population density, long-term”；以及“water/ground-”，而非“water/ground-, long-term”。
- 部分数据集错误地使用“air/lower stratosphere + upper troposphere”子区室，该子区室应仅用于航空运输。正确子区室应为“air/unspecified”。
- 电力市场（高压、中压、低压）有效年份的注释已从一般注释移至生产量注释。有效年份也可在[电力行业页面图 3](energy.md)中找到。
- 锂辉石（LiAl(SiO3)2）的锂含量为 0.0376。在下列方法中将锂的 CF 应用于锂辉石时，可将此值作为换算因子：  
    
  \* CML v4.8 2016  
  \* Ecological Scarcity 2021  
  \* EPS 2020d  
  \* ReCiPe 2016  
    
  前三种方法尚未对锂辉石进行表征；ReCiPe 2016 中错误地使用锂的 CF（换算因子为 1）对其进行表征。

{% endtab %}

{% tab title="English 原文" %}

## The ecoinvent v3.9.1 contains the same new and updated datasets published in v3.9, but includes important corrections. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.9.1 was released on December 15th, 2022</strong>. Discover how to [upgrade to our latest version](licensing.md).

Oct 29th, 2023

The update 3.9.1 introduces important corrections in the characterization factors of certain LCIA methods, and addresses issues with uncertainty data as well as missing metadata at the level of exchanges.  The update was released in December 2022 to correct issues that were identified in ecoinvent version 3.9. The identified issues in v3.9 could potentially influence the LCIA scores of certain methods and affect the usability of the data.

ecoinvent version 3.9 includes enhanced documentation and further updated emission factors, integrating the IPCC 2021 method, among other LCIA methods. At the same time, it integrates around 1’099 new and 1’876 updated datasets, including around 271 new products. Sectors updated with version 3.9 included Agriculture, Batteries, Chemicals, Electricity, Metals, Pulp and Paper, Oil and Gas, and Waste.

ecoinvent v3.9 was identified to include issues that can potentially influence the LCIA scores of certain methods or might affect the usability of the data.

### List of Changes from Version 3.9 to Version 3.9.1 <a href="#en-b0008" id="en-b0008"></a>

- <strong>Changes in Global Warming Potential Indicators </strong>  
  We corrected the characterization factors of the indicators that assess global warming potential in the following methods (including their “no LT” counterpart):

- - <strong>ReCiPe 2016 v1.03 </strong>
  - <strong>TRACI v2.1 </strong>
  - <strong>EPS 2020d</strong>

These corrections result in significant changes in LCIA scores in the “Allocation, cut-off” and “Consequential” system models. This also affects the “total” indicators in the “ReCiPe 2016 v1.03” method.

None of the other indicators that assess global warming potential (such as IPCC 2013 and IPCC 2021, EF 3.0 and EF 3.1) have changes in scores compared to version 3.9.

- <strong>Changes in ecotoxicity and human toxicity indicators </strong>  
  We revised the characterization factors for emissions of metals and agrochemicals for certain LCIA methods. This resulted in noticeable changes in LCIA scores in all system models for indicators assessing ecotoxicity and human toxicity in the following methods (including their “no LT” counterpart):

- - <strong>CML v4.8 2016 </strong>
  - <strong>EF v3.0 and EF v3.1 (including their EN15804 counterpart) </strong>
  - <strong>TRACI v2.1 </strong>

- <strong>Changes in the marine eutrophication indicator in EF v3.0 and v3.1 </strong>  
  We removed the characterization factors for some emissions of nitrogen from the indicator that assesses marine eutrophication in the methods EF v3.0 and v3.1 (including their EN15804 counterpart). This resulted in a noticeable decrease in LCIA scores for that indicator in all system models.
- <strong>Correction of names or units in “ReCiPe 2016 v1.03” and “TRACI v2.1” </strong>  
  We corrected the name or unit of some indicators in the methods “ReCiPe 2016 v1.03” and “TRACI v2.1”. These corrections have no influence on LCIA scores.

- <strong>Dataset correction </strong>  
  The dataset “market for natural gas, high pressure” in JP (Japan) had a wrong amount for the emission of “Mercury II” to air. We corrected it for version 3.9.1, which results in a decrease in LCIA scores of indicators that assess human toxicity and emissions of heavy metals into air. These changes in scores affect only the datasets that are direct or indirect consumers of this market.
- <strong>Changes in the “variance” amount of uncertainty data </strong>  
  In version 3.9, the “variance” field contained the wrong value in the cases where the lognormal distribution is used. This concerns all types of quantities that can have uncertainty data (exchange amounts, property amounts, production volumes, and parameters). We corrected this in v3.9.1. The field “varianceWithPedigreeUncertainty” does not change and is correct in version 3.9.
- <strong>Addition of information on exchanges in metadata</strong>  
  Some metadata fields of exchanges were not included in the unit process data (for example, the exchange comment, production volume comment, etc). We have included them in the data published in version 3.9.1.
- <strong>Removal of datasets producing recyclables</strong>  
  Some datasets present in ecoinvent v3.9 were producing a recyclable material in the cut-off and EN15804 system models. As these datasets should not have existed, we have removed them in version 3.9.1.
- <strong>Corrected end date for EN15804 datasets</strong>  
  The year of the end date in the EN15804 datasets was not consistent with the year used in other system models. We corrected them for version 3.9.1.

  

For a more detailed description of the changes and their effects on the LCIA scores, please refer to the [Report of Changes](../assets/0c8a26bab4bd-Change-Report-v3.9.1.pdf).

### Features and documentation <a href="#en-b0023" id="en-b0023"></a>

#### Emission Factors (LCIA Methods) <a href="#en-b0024" id="en-b0024"></a>

ecoinvent v3.9 integrates IPCC 2021, updates the EF method by the [European Platform on Life Cycle Assessment to v3.1](https://eplca.jrc.ec.europa.eu/), and implements the latest versions of Ecological Scarcity (2021), ReCiPe (2016), TRACI v2.1, EPS (2020). With ecoinvent v3.9, Crustal Scarcity Indicator (2020) is now offered to ecoinvent users for the first time. With these new and updated methods, ecoinvent v3.9 offers more up-to-date emission scores on climate change, mineral resources, land use, water depletion, ozone depletion, and freshwater ecotoxicity, as well as impact scores expressed in monetary values, among other things. [Find out more information on the methods included in the ecoinvent database.](impact-assessment.md)

#### Product Information <a href="#en-b0026" id="en-b0026"></a>

Since ecoinvent v3.8, all products and services included in the database include a description that supports users in identifying them. The information includes a definition of the product or service as seen in the database. At the same time, the documentation of the services incorporates supporting information on how to use them. With ecoinvent v3.9, the database-wide update and expansion of the information on products and services is now complete, including enhanced product characteristics. This feature is also implemented in various LCA software tools, offering enhanced transparency to LCA practitioners. Please contact your software provider for more information.

#### Nomenclature and Identifiers of Elementary Exchanges <a href="#en-b0028" id="en-b0028"></a>

Following ecoinvent’s participation in the [GLAD project](https://ecoinvent.org/projects/global-lca-data-access-glad-network/), ecoinvent v3.9 updates the nomenclature and identifiers of the complete list of elementary exchanges (environmental flows). Specifically, ecoinvent v3.9 updates names, CAS numbers, formulas, and synonyms of the exchanges. The result of this update is an improved list of elementary exchanges that is now more aligned with the respective lists of other databases. This helps modelers using the ecoinvent database to more easily identify and choose the data needed for their assessments. This update also improves the interoperability of the ecoinvent database with other databases around the world and enhances collaboration in assessing environmental impacts.

### New and Updated Data <a href="#en-b0030" id="en-b0030"></a>

#### Agriculture <a href="#en-b0031" id="en-b0031"></a>

The sector features updates introducing data on new crops produced in Canada and Brazil. Specifically, ecoinvent v3.9 includes data on the production of new crops from Canada, such as pinto bean, red kidney bean, fava bean, and navy bean. Further, it introduces data on the production of new products (peanut) and updates data on the production of major products from Brazil, including coffee, sugar cane, soybean, and maize. Data for these updates were provided by the University of British Columbia (Canada) and Embrapa (Brazil). ecoinvent 3.9 also features new and updated data on pesticides, which may affect the results of assessments for agricultural processes and products.

#### Batteries <a href="#en-b0033" id="en-b0033"></a>

ecoinvent v3.9 continues the improvement of the representation of batteries in the ecoinvent database. This year’s update includes new datasets on the ‘Lithium, Iron, and Phosphate’ battery technology, thus expanding the coverage of battery chemistries, now including 5 important technologies. These datasets were created by the Swiss Federal Laboratories for Materials Science and Technology (EMPA) and include battery components specifically for this battery type, as well as the production of lithium iron phosphate. Complementary, the datasets for battery separator and electrolyte were updated.

#### Building and Construction <a href="#en-b0035" id="en-b0035"></a>

In ecoinvent v3.9, the sector is enhanced with new data for cement and concrete using recycled and waste mixed aggregates. Furthermore, new nomenclature rules have been introduced for the cement and concrete supply chains. The goal of these new rules is consistency across all geographies, alignment with the nomenclature used in industry standards, and a clear structure that can facilitate users' understanding of the different cement and concrete types and the selection of the product with the right properties for their study. Along with the change in nomenclature, the global datasets for cement and concrete production have also been restructured, and only the most representative datasets for the global geography have been maintained.

#### Chemicals and Plastics <a href="#en-b0037" id="en-b0037"></a>

The Chemicals sector is updated to include 36 new chemical products developed for the EF initiative, mainly pesticides and plasticizers, including ethephon, triclopyr, and dioctyl adipate.

Moreover, ecoinvent v3.9 takes the first step to gradually improve the representation of hydrogen in the ecoinvent database. Specifically, ecoinvent v3.9 introduces data on the main production technology for hydrogen (steam reforming) in Europe and the World.

#### Electricity <a href="#en-b0040" id="en-b0040"></a>

ecoinvent v3.9 updates the electricity market mixes to reflect the situation in 2019. In the case of the US, Canada, and Switzerland, the electricity mixes are updated to reflect the situation in 2020. The update of the Swiss data is based on Swiss national data, while the rest of this update is based on data from the International Energy Agency (IEA).

This year, the electricity mixes for China, India, and Brazil are also updated to reflect the situation in the countries in 2020, 2019, and 2020, respectively. These updates are performed based on national statistics, while in the case of Brazil, the data was provided by ACV Brasil. Moreover, all submarkets in these countries are updated, thus better representing the electricity situation in the various regions. The electricity mix for State Grid Corporation of China (SGCC) was split into its six subregions, now better reflecting the local conditions. At the same time, all electricity markets in the ecoinvent database are adjusted to include these updates.

ecoinvent v3.9 also updates the data on electricity transmission networks. Specifically, this version updates the data on the infrastructure used for electricity transmission, which is also reflected in the electricity market datasets. For the countries where data is available, this update also introduces separate data for aerial, underground, and subsea cables.

ecoinvent v3.9 further introduces residual mixes, based on data provided by the Association of Issuing Bodies (AIB).

#### Metals <a href="#en-b0045" id="en-b0045"></a>

This update expands the data coverage of the Metals sector with new and updated data. Specifically, ecoinvent v3.9 introduces data on new metal products, including antimony, borates, germanium, zirconium, and hafnium. New and updated datasets were provided by the Swiss Federal Laboratories for Materials Science and Technology, EMPA (sponsored by the Swiss Federal Office for the Environment, BAFU).

#### Pulp and Paper <a href="#en-b0047" id="en-b0047"></a>

The pulp and paper sector has been updated with new and updated products used to produce packaging materials and paper, including data from industry associations. This update expands the geographical coverage of the data. Find more information [here](pulp-and-paper.md).

#### Oil and Gas <a href="#en-b0049" id="en-b0049"></a>

ecoinvent v3.9 introduces an extensive overhaul of the data on natural gas and crude petroleum oil supply.

Specifically, this version includes an update on the natural gas and crude petroleum oil supply chains (production, long-distance transport, and regional distribution) in the ecoinvent database to reflect the global supply situation in 2019. The geographical coverage in the database is expanded with data on the production of natural gas and crude petroleum oil in different countries and regions. When combined, the ecoinvent database now covers 90% of the global production of crude oil and nearly 80% of natural gas. In addition, the update introduces regional consumption mixes for crude petroleum oil to North America and Europe, alongside new or updated natural gas supply to 44 countries, based on the situation in 2019.

The update integrates data on the flaring of natural gas from the Global Gas Flaring Reduction Partnership (GGFR) of the World Bank and on methane emissions from gas venting and fugitive emission sources from the International Energy Agency’s Methane Tracker 2022. Building on earlier studies commissioned by the Swiss Federal Office for the Environment (FOEN), the Swiss Federal Office for Energy (SFOE), the Swiss Gas Industry Association (Verband der Schweizerischen Gasindustrie, VSG), and Avenergy Suisse (previously Erdöl-Vereinigung), this update was commissioned by the ecoinvent Association and prepared by ESU-services Ltd.

#### Waste <a href="#en-b0053" id="en-b0053"></a>

ecoinvent v3.9 introduces the first part of the Waste sector overhaul. Specifically, this update disaggregates the wastewater treatment chains, allowing visibility of the by-products of wastewater treatment and its subsequent treatments.

### Relevant Documents and Files <a href="#en-b0055" id="en-b0055"></a>

#### Report of Changes <a href="#en-b0056" id="en-b0056"></a>

This report covers all changes made in the ecoinvent database between version 3.9 (2022) and version 3.9.1 (2022).

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/0c8a26bab4bd-Change-Report-v3.9.1.pdf)

#### Report of Changes <a href="#en-b0059" id="en-b0059"></a>

This automatically generated Excel file provides an overview of changes made to the undefined unit process datasets between versions 3.9 and 3.9.1 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### Correspondence File <a href="#en-b0061" id="en-b0061"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.8 and 3.9.1 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File](../assets/0439269e189d-Correspondence-File-v3.8-v3.9.1-1.xlsx)

#### LCIA Implementation Report <a href="#en-b0064" id="en-b0064"></a>

The LCIA Implementation Report documents the implementation of LCIA methods for versions 3.9 and 3.9.1

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [LCIA Implementation Report](../assets/bfc333634386-LCIA_implementation_3.9-and-3.9.1.pdf)

#### Database Overview File <a href="#en-b0067" id="en-b0067"></a>

The Database Overview file describes the contents of the database. The following information is contained in the file:

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Database Overview File](../assets/34bb93e02a6f-Database-Overview-for-ecoinvent-v3.9.1-9.xlsx)

#### Activity Overview(s) <a href="#en-b0070" id="en-b0070"></a>

The lists of datasets contained in each of the three [system models](system-models.md), as well as the list of unlinked and unallocated datasets. For version 3.9.1, each dataset has been assigned to one or more sectors, which helps filter for datasets that can belong to different sectors.

#### ecoinvent Geographies <a href="#en-b0072" id="en-b0072"></a>

The geographies used in the ecoinvent database. Each geography is assigned a classification, and the geographies that are contained in each geography are indicated.

#### LCIA Methods <a href="#en-b0074" id="en-b0074"></a>

The list of the LCIA methods for which ecoinvent calculates impact scores. The version of the methods is indicated, and the original source used for defining the characterization factors is provided.

This section lists all known data errors in version 3.9.1 of the ecoinvent database.

### Data Issues <a href="#en-b0077" id="en-b0077"></a>

- The dataset “refrigerant R134a production” for the RER and GLO geography models two pathways, the hydrofluorination of trichloroethylene and tetrachloroethylene, although hydrofluorination of tetrachloroethylene is no longer industrially relevant. The datasets are currently under review.

- The datasets “polydimethylsiloxane production”, “dimethyldichlorosilane production”, and “methylchloride production” for the Global geography are currently under review. Literature suggests that the hydrochloric acid, which is formed in the polydimethylsiloxane production, is recirculated to use as an input in the methylchloride production. In the current version of ecoinvent v3.9.1, the hydrochloric acid formed in the polydimethylsiloxane production is neutralised and disposed of, whilst the methylchloride production uses virgin hydrochloric acid.
- The dataset “dimethyl sulfoxide production” for the GLO and RER geography is currently under investigation to ensure it properly represents the industrially applied technology.
- The hydrogen market is currently under review. The dataset “hydrogen production, steam reforming” is included in version 3.9.1. The new production technology for now does not contribute to the market for hydrogen, liquid, the improvement of production and consumption mixes is planned for the following releases. The work will include the revision of hydrogen in both gaseous and liquid form and its utilisation in different industries.
- Compared to the current hydrogen markets – liquid and gaseous – the newly introduced steam reforming dataset has a global warming potential (IPCC 2021), which is more than 5 times higher. This GWP is in accordance with literature (Antonini et al., 2020).
- “Carbon dioxide, in chemical industry” is by-produced from ammonia production and directly supplies “urea production” with direct activity links. In the Consequential system model, “carbon dioxide, in chemical industry” has no alternative (marginal) supplier and thus it is dropped. Users are encouraged to check the undefined version of “urea production” in case the amount of CO2 (0.77112 kg of CO2 used per kg of Urea produced) needed to produce urea is needed for their study.

- The dataset “acrylic acid production” for the GLO and RER geography is currently under investigation.
- For the datasets listed below, the amount of the intermediate exchanges of “natural gas, high pressure” and “natural gas, low pressure” corresponds to the Lower Heating Value that was initially defined by the data provider and is indicated in the property, ‘heating value, net’ of these exchanges. The amount of these heating values does not reflect the new Lower Heating Value of natural gas (36MJ/m3) implemented with the v3.9.1 update.

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

- An error has been spotted in the water balance of wastewater treatment datasets. It is related to the amount of water emitted to the Environment, to the sub-compartment of surface water. It mostly affects datasets modelled in the global (GLO) geography, while it is almost negligible in the regional ones. This issue will be corrected in the next version of 3.10.

  Meanwhile, the exchange of “Non-hazardous waste disposed” will be added to all the wastewater treatment datasets as an inventory indicator to facilitate the implementation of EN15804 system model. Finally, adjustments in energy consumption will also be implemented as a result of updating the internal waste tool used to generate treatment datasets. All changes to be included in version 3.10 are presented in the Excel file attached.

  ![doc-icon](../assets/024d8f149226-doc-icon.png)   See [Known Issues Water Imbalances in Wastewater Treatment Activities](../assets/adb816446555-known-issue-v3.9.1-water-imbalances-in-wastewater-treatment-activities.xlsx)

#### LCIA Issues <a href="#en-b0118" id="en-b0118"></a>

- There are issues with the scores for “total: …” categories in ReCiPe 2016. These totals don’t match the sum of the single “human health|…”, “ecosystem quality|…” and “natural resources|…” categories|indicators and should not be used or calculated manually as these sums.
- There are mistakes in sub-compartments, which affect scores. The concerned activities and exchanges are listed in this [file](../assets/34bb93e02a6f-Database-Overview-for-ecoinvent-v3.9.1-9.xlsx). They include

- Datasets that mistakenly have a sub-compartment with the label “long-term” for some emissions. “long-term” sub-compartments are meant to be reserved for emissions occurring after 100 years; in particular, they are used for landfill sites (leaching, 100-60’000 years) and uranium mining and milling sites (radon emissions from tailings, 100-80’000 years). The correct sub-compartment would be “air/non-urban air or from high stacks” instead of “air/low population density, long-term” and “water/ground-“ instead of “water/ground-, long-term”.
- Datasets that mistakenly have the sub-compartment “air/lower stratosphere + upper troposphere”, which is meant to be reserved for air transport. The correct sub-compartment would be “air/unspecified”.
- The comment referencing the year of validity for the electricity market (high, medium, low voltage) has been moved from the general comment to the production volume comment. The year of validity can also be found in [Figure 3 on the electricity sector page](energy.md).
- Spodumene (LiAl(SiO3)2 has a Lithium content of 0.0376. This value can be used as a conversion factor when applying the CF of Lithium to Spodumene in the following methods:  
    
  \* CML v4.8 2016  
  \* Ecological Scarcity 2021  
  \* EPS 2020d  
  \* ReCiPe 2016  
    
  In the first three methods, Spodumene is not yet characterized; in ReCiPe 2016, it was wrongly characterized with the CF for Lithium (and a conversion factor of 1).

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0071**：该版本包含 EN15804 等四个系统模型，但此处仍称三个，可能沿用旧版说明。 请核对概览文件中的系统模型数量；暂保留原文。 [查看完整记录](../review/issues.md#issue-099)
- **待专家复核 · b0119**：原文 should not be used or calculated manually 的 not 同时作用于 used 和 calculated manually。正文保留两项否定，不能根据上下文将第二项改写为允许手工计算。原文 as these sums 的具体操作含义及数据方意图仍需确认。 请向数据方确认该句意图及正确处理操作；在确认前，不将原文解释为允许用户手动计算分项之和。 [查看完整记录](../review/issues.md#issue-100)
- **已处理／已说明 · b0124**：原文化学式外的左括号未闭合；译文补齐括号，化学式和数值保持原样。 建议源文补齐外层括号。 [查看完整记录](../review/issues.md#issue-101)
- **已处理／已说明 · b0022**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-102)
- **已处理／已说明 · b0056**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-103)
- **已处理／已说明 · b0058**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-104)
- **已处理／已说明 · b0059**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-105)
- **已处理／已说明 · b0060**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-106)
- **已处理／已说明 · b0088**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-107)
- **已处理／已说明 · b0090**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-108)
- **已处理／已说明 · b0092**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-109)
- **已处理／已说明 · b0094**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-110)
- **已处理／已说明 · b0096**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-111)
- **已处理／已说明 · b0098**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-112)
- **已处理／已说明 · b0100**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-113)
- **已处理／已说明 · b0102**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-114)
- **已处理／已说明 · b0104**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-115)
- **已处理／已说明 · b0109**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-116)
- **已处理／已说明 · b0111**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-117)
- **已处理／已说明 · b0113**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-118)
- **已处理／已说明 · b0115**：在完整保留可检索英文数据集名称的同时补充中文解释。 已补充。 [查看完整记录](../review/issues.md#issue-119)
- **已处理／已说明 · b0046**：本页标题为 3.9.1，明确保留此段原文的 v3.9 指称，以免读者将主要版本新增内容误认为补丁版本新增。 已显式恢复 ecoinvent v3.9。 [查看完整记录](../review/issues.md#issue-120)
- **已处理／已说明 · b0119**：原译“或需……手动计算”将原文 not 对 calculated manually 的否定改成肯定操作建议。重新核对并恢复两项否定；作者操作意图留在独立原文注记中待数据方确认。 已修正正文，并同步更新原文注记。 [查看完整记录](../review/issues.md#issue-121)
