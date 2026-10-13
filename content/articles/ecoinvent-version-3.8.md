# ecoinvent 第 3.8 版

英文原题：ecoinvent Version 3.8  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.8)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-07-07

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.8 注重用户使用便利性，完善了文档，并通过约 360 个新增和 700 个更新数据集扩大了数据库的行业覆盖。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.8 于 2021 年 9 月 21 日发布</strong>。了解如何[升级到最新版本](licensing.md)。

2023 年 10 月 28 日

该版本还包含我们与 Rede ACV 合作改进数据库中巴西数据的首批成果。

ecoinvent 数据库第 3.8 版为数据用户提供更完善的产品和市场文档与信息，通过新增 EN15804 截断分配模型（“Allocation, cut-off, EN15804”）链接的数据（专门支持 EPD 从业人员），GHG Protocol 计算支持，以及约 360 个新增和 700 个更新数据集，涉及农业、竹材、电池、化学品与塑料、电子、金属、林业与木材、运输和电力。该版本还发布 Rede ACV 与 ecoinvent 合作的首批成果，旨在提高数据库中巴西数据的覆盖和准确性。

新增和更新所用的数据由 ETH、EMPA、普福尔茨海姆大学和 ACV Brazil 等多家机构提供。

### <strong>功能与文档</strong> <a href="#zh-b0008" id="zh-b0008"></a>

#### <strong>产品信息</strong> <a href="#zh-b0009" id="zh-b0009"></a>

此次更新旨在提高用户使用数据库的便利性。数据库中所有产品和服务现在都附有帮助识别的描述。这些信息包括数据库所采用的产品或服务定义。对于服务，其文档现已纳入有关使用方式的辅助信息。总体而言，ecoinvent v3.8 包含 3’300 种独特产品和服务。

#### <strong>市场信息</strong> <a href="#zh-b0011" id="zh-b0011"></a>

通过发布 ecoinvent v3.8，我们旨在改善数据库中市场数据集的描述和信息。具体而言，所有市场数据集均已审阅，其现有元信息已补充、纠正或完善，使数据库用户能够更一致、更准确地使用这些数据集，提高其可用性。

#### <strong>数据库概览</strong> <a href="#zh-b0013" id="zh-b0013"></a>

为更简洁地概览数据库内容，所包含活动的信息已集中至一个文件：“Database Overview for ecoinvent 3.8”。该文件包含以下信息：

- 各系统模型中的数据集列表，以及未链接和未分配数据集列表。在第 3.8 版中，每个数据集都已归入一个或多个行业，便于筛选可能属于不同领域的数据集。
- ecoinvent 数据库所用的地理区域。每个地理区域均赋予分类，并标明其所包含的地理区域。
- ecoinvent 为之计算影响得分的 LCIA 方法列表，包括方法版本，以及用于定义表征因子的原始来源。

#### <strong>增强对 GHG Protocol 的支持</strong> <a href="#zh-b0018" id="zh-b0018"></a>

通过 ecoinvent v3.8 更新，数据库现在可以按照 GHG Protocol 的范围 2 和范围 3 指南计算电力排放。为此，可在 ecoQuery 的“文件”（Files）部分找到一个附加文件。电子表格现分别提供发电活动和电力市场的范围 2 与范围 3 排放因子。排放因子依据 IPCC 2013 AR5 报告中的 GWP100（全球变暖潜势）数值计算，代表电力最终消费者的情况，采用基于所在地的报告方法，即代表电网平均排放因子。此外，新电子表格还提供按单种温室气体或温室气体组细分的排放量和排放因子。

#### <strong>面向 EPD 从业人员的新系统模型</strong> <a href="#zh-b0020" id="zh-b0020"></a>

鉴于环境产品声明（EPD）在建筑和制造业中日益重要，以及对标准化、准确、无误导地传达产品环境信息的需求，ecoinvent 协会引入了 EN15804 截断分配模型（“allocation, cut-off, EN15804”）。该系统模型有两个目标：一方面，帮助 EPD 从业人员遵守 EN15804&A2:2019 标准；另一方面，促进该标准各指标计算的协调一致。该系统模型完全符合 ISO 14025、ISO 21930 和 EN15804&A2:2019，提供这些标准要求的全部生命周期清单（LCI）指标，并遵循欧盟委员会规定的废物终止状态（end-of-waste）判定标准。

#### <strong>LCIA 方法</strong> <a href="#zh-b0022" id="zh-b0022"></a>

ecoinvent v3.8 新增了当时最新版本的 CML（v4.8 2016）和 EF（v3.0，以及针对[EN15804](https://eplca.jrc.ec.europa.eu/LCDN/EN15804.xhtml)调整的版本）LCIA 方法。全部已实施方法的影响类别详情，可在新数据库概览文件中找到。

### <strong>新增与更新的数据</strong> <a href="#zh-b0024" id="zh-b0024"></a>

#### <strong>巴西数据</strong> <a href="#zh-b0025" id="zh-b0025"></a>

Rede ACV（巴西 LCA 企业网络）与 ecoinvent 协会共同设立[Cornerstone 项目](https://ecoinvent.org/projects/cornerstone-project/)，以提高代表巴西关键供应链的背景数据的可用性和可获取性。Rede ACV 通过其承包方 ACV Brasil，以 ecoinvent 数据库现有内容为基础，开发代表巴西情况的区域化生命周期清单（LCI）数据。ecoinvent 3.8 数据涵盖原油和天然气开采、进口与分配，生物柴油生产（脂肪酸甲酯 FAME 的酯化），柴油分配（运输用），以及货车道路货运。较早的 ecoinvent 数据集也已为 v3.8 更新，以更好地反映巴西炼油厂运行的国家特定原油供应。

#### <strong>农业</strong> <a href="#zh-b0027" id="zh-b0027"></a>

该行业进行了小规模更新，表示扁豆和豌豆等新产品，并将农业服务重新情境化以适用于加拿大。此次更新数据由不列颠哥伦比亚大学和 Food Systems PRISM Laboratory 提供。

#### <strong>电池</strong> <a href="#zh-b0029" id="zh-b0029"></a>

ecoinvent v3.8 包含三种锂离子电池（NCA、NMC111、NMC811）及其生产的新数据集，由瑞士联邦材料科学与技术实验室（EMPA）创建，纳入了用于这三种电池的各种化学品，例如硫酸钴、焦亚硫酸钠、vinyl carbonate（碳酸乙烯类化合物）以及氧化物和氢氧化物。各电池部件（阴极、阳极、高低压系统、电芯和电池管理系统）分别拆分，并各自以独立数据集表示。此外，v3.8 更新还包含普福尔茨海姆大学创建的一个铅酸电池新数据集。

#### <strong>化学品与塑料</strong> <a href="#zh-b0031" id="zh-b0031"></a>

在 ecoinvent 3.8 中，我们继续更新数据并加强与行业的合作。苯乙烯生产数据在 PlasticsEurope 支持下更新，聚氨酯泡沫的新增和更新数据由 EUROPUR 提供。

#### <strong>电力</strong> <a href="#zh-b0033" id="zh-b0033"></a>

ecoinvent 3.8 包含大多数国家更新后的归因型电力市场，参考年为 2018 年；美国和加拿大的参考年则为 2019 年。此外，瑞士电力市场以及所有更新市场的变压损失（高压至中压、中压至低压）均已调整。数据创建和审核与苏黎世联邦理工学院及保罗谢勒研究所（PSI）合作完成。

#### <strong>电子</strong> <a href="#zh-b0035" id="zh-b0035"></a>

第 3.8 版包含消费电子设备的新数据集。依据最新文献数据，新增了智能手机和平板电脑数据集，并更新现有笔记本电脑数据集。针对移动设备，创建了新的印制线路板和液晶显示屏数据集。相应供应链中的部件已按需要调整。

#### <strong>林业与木材</strong> <a href="#zh-b0037" id="zh-b0037"></a>

木材行业新增竹林经营及竹质建筑材料（中间产品）生产数据，即竹竿、展平竹材和编织竹席。这些新数据集由 Edwin Zea Escamilla 博士在国际竹藤组织（INBAR）支持下开发。

#### <strong>金属</strong> <a href="#zh-b0039" id="zh-b0039"></a>

EMPA 在瑞士联邦环境局（BAFU）资助下为 ecoinvent 第 3.8 版提供金属行业新增和更新数据集。新增数据涵盖铍、铌铁以及从稀土尾矿生产氧化钪。EMPA 还更新了铬铁、碳酸锂、硫酸锶、钽、钛生产，以及重矿物砂开采数据。

#### <strong>运输</strong> <a href="#zh-b0041" id="zh-b0041"></a>

与 INFRAS 合作更新了航空货运（客机腹舱和专用货机）数据集。原有煤油消耗及相应排放量偏低（第 3.6 至 3.7.1 版）。

#### <strong>生物源碳资源修正</strong> <a href="#zh-b0043" id="zh-b0043"></a>

在按分类截断的分配模型（“allocation, cut-off by classification”）中，林业、木材、纸和纸板行业数据通过新增基本流交换，在分配后恢复生物源碳平衡，使这一过程能够透明追踪。

### <strong>相关文档与文件</strong> <a href="#zh-b0045" id="zh-b0045"></a>

#### <strong>变更报告</strong> <a href="#zh-b0046" id="zh-b0046"></a>

本报告涵盖 ecoinvent 数据库第 3.7.1 版（2020 年）至第 3.8 版（2021 年）之间的所有变化，同时反映全数据库范围的变化和各行业特定变化。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[变更报告](../assets/87f134eda0de-Change-Report-v3.8.pdf)

#### <strong>变更报告</strong> <a href="#zh-b0049" id="zh-b0049"></a>

此自动生成的 Excel 文件概览 ecoinvent 数据库第 3.7.1 版至第 3.8 版之间未指定系统模型的单元过程数据集的变化。XLS 变更报告可在 ecoQuery（ecoinvent 数据库第 3 版的在线版本）的“文件”（Files）部分找到，向数据库许可证持有人提供。

#### <strong>对应关系文件</strong> <a href="#zh-b0051" id="zh-b0051"></a>

对应关系文件是一个电子表格，列出第 3.7.1 版和第 3.8 版的全部数据集，并匹配不同版本之间的对应数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[对应关系文件](../assets/b50476fe0866-Correspondence-File-v3.7.1-v3.8.xlsx)

#### <strong>数据库概览文件</strong> <a href="#zh-b0054" id="zh-b0054"></a>

数据库概览文件描述数据库内容，包含以下信息：

- #### <strong>活动概览</strong> <a href="#zh-h26" id="zh-h26"></a>

三个[系统模型](system-models.md)各自的数据集列表，以及未链接和未分配数据集列表。在第 3.8 版中，每个数据集都已归入一个或多个行业，便于筛选可能属于不同领域的数据集。

- #### <strong>ecoinvent 地理区域</strong> <a href="#zh-h27" id="zh-h27"></a>

ecoinvent 数据库所用的地理区域。每个地理区域均赋予分类，并标明其所包含的地理区域。

- #### <strong>LCIA 方法</strong> <a href="#zh-h28" id="zh-h28"></a>

ecoinvent 为之计算影响得分的 LCIA 方法列表，包括方法版本，以及用于定义表征因子的原始来源。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[数据库概览文件](../assets/04194da4f83c-Database-Overview-for-ecoinvent-v3.8-1.xlsx)

### <strong>LCIA 实施报告</strong> <a href="#zh-b0063" id="zh-b0063"></a>

LCIA 实施报告记录第 3.8 版 LCIA 方法的实施。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[LCIA 实施报告](../assets/e0a7eed10e0f-LCIA-Implementation-v3.8.pdf)

#### <strong>其他文件与支持文档</strong> <a href="#zh-b0066" id="zh-b0066"></a>

有关 v3.8 文件及支持文档的更多信息，请参阅支持页面[ecoQuery 中的文件](files.md)。

### <strong>已知问题</strong> <a href="#zh-b0068" id="zh-b0068"></a>

本部分列出 ecoinvent 数据库第 3.8 版中的全部已知数据错误。

#### <strong>数据问题</strong> <a href="#zh-b0070" id="zh-b0070"></a>

- RoW 地理区域的“electricity voltage transformation from high to medium voltage”和“electricity voltage transformation from medium to low voltage”活动出现在 Cut-off 分配模型和 APOS 系统模型中。由于这些系统模型中不存在 RoW 电力市场，因此这些数据集的 LCIA 得分为零，不应使用。
- 在 AU、CA、CL、CN、ID、KZ、RU、US 和 ZM 地理区域，“copper mine operation and beneficiation, sulfide ore”活动中来自环境的“Tellurium, in ground”投入（区室：“natural resource”；子区室：“in ground”）的交换量，与 GLO 地理区域的交换量不一致。依据这些地区开采了全球铜矿中所提取碲（Te）的 70%（在 GLO 数据集中建模）这一假设，已相应下调局部地理区域的交换量。未指定系统模型数据集的新数值如下表所列，将随 v3.9 发布。

<table>
<tbody>
<tr>
<td>
<p><strong>数据集</strong> </p>
</td>
<td>
<p><strong>单位</strong> </p>
</td>
<td>
<p><strong>原数值</strong> </p>
</td>
<td>
<p><strong>新数值</strong> </p>
</td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, AU </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.8968E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, CA </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.9067E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, CL </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.8997E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, CN </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.9018E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, ID </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.8935E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, KZ </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.9096E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, RU </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.8960E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, US </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.8973E-05 </p></td>
</tr>
<tr>
<td><p>copper mine operation and beneficiation, sulfide ore, ZM </p></td>
<td><p>kg </p></td>
<td><p>2.0062E-04 </p></td>
<td><p>6.9021E-05 </p></td>
</tr>
</tbody>
</table>

  

- “styrene production”数据集在 PlasticsEurope 支持下于第 3.8 版更新。对三家生产商和四个生产场地开展了企业调查，随后移除了数据集中向水的苯排放，并将向空气的苯排放降低四个数量级。这一更新显著影响部分人体毒性指标（例如 ecological scarcity 2013, carcinogenic substances into air-total）。人体毒性影响类别（例如 ReCiPe Midpoint (H) – human toxicity）的另一项关键贡献是苯的材料投入。ecoinvent 数据库中的苯市场表示由催化重整、裂解汽油以及部分炼焦副产苯构成的组合。最后一种技术具有显著的人体毒性影响得分。市场份额将在后续发布中修订。
- “adipic acid production”数据集正在就生产过程中产生的一氧化二氮（N2O）排放进行审查。正在研究新的减排方法，以提高去除效率，从而降低 RER 和 GLO 两个数据集的 N2O 排放。
- “cathode production, NCA, for Li-ion battery”和“cathode production, NMC811 for Li-ion battery”数据集错误地使用了中间交换“NMC111 oxide”作为投入。对于 NCA 阴极生产，相应交换应为“NCA oxide”；对于 NMC811 阴极生产，则应为“NMC811”。这导致阴极生产数据集以及后续 NCA 和 NMC811 电芯与电池生产数据集的影响得分被高估。受影响数据集的正确得分已重新计算，可在 ecoQuery“文件”（Files）部分的以下文件中获取：[Corrected LCIA scores – Oxide input in cathode production, li-ion batteries v3.8.xlsx](https://v38.ecoquery.ecoinvent.org/File/File?fileName=ecoinvent+3.8+(2021)%2c+current%5csupporting+documents%5cCorrected+LCIA+scores+-+Oxide+input+in+cathode+production%2c+li-ion+batteries+v3.8.xlsx&hash=-1769755026&type=Files)
- “methylene diphenyl diisocyanate production”（GLO 和 RER）数据集将生成的盐酸视为废物，这不符合实际。盐酸是有价值的副产品，由 MDI 生产商使用或出售。ecoinvent 协会建议用户采用 PlasticsEurope 网站上现有 [ecoProfile](https://plasticseurope.org/sustainability/circularity/life-cycle-thinking/eco-profiles-set/) 中的 LCIA 得分，或通过移除废物中和处理并将 HCl 作为副产品，修正 ecoinvent 中的单元过程。  
  为修正 ecoinvent 数据集，我们建议用户使用 ecoQuery 提供的未指定系统模型数据集，移除氢氧化钠投入以及钠和氯化物输出的交换。

- 2021 年 9 月 21 日发布的“electricity emission factors – scope 2 – 3 in ecoinvent v3.8.xlsx”文件，已于 2022 年 12 月被更新版本替换。新文件“electricity emission factors – scope 2 – 3 in ecoinvent v3.8 (updated).xlsx”包含若干修正，其详细说明位于更新文件的“read me”工作表。更新文件可在 ecoQuery“文件”（Files）部分的 v3.8 支持文档下找到。

#### <strong>生命周期影响评价问题</strong> <a href="#zh-b0118" id="zh-b0118"></a>

- 在 EF v3.0 方法（EF v3.0、EF v3.0 no LT 和 EF v3.0 EN15804）中，“eutrophication: freshwater”影响类别的单位应为“kg P-Eq”，而非“kg PO4-Eq”。  
  对于部分不再更新但仍发布的 LCIA 方法，表征因子文件中未更新已经更名的基本流交换名称。这导致部分表征因子未被纳入第 3.8 版的实施。如果用户希望修正，可在“LCIA implementation 3.8.xlsx”文件中手动将下列交换的旧名称改为新名称：

<table>
<tbody>
<tr>
<td>
<p><strong>旧名称</strong> </p>
</td>
<td>
<p><strong>新名称</strong> </p>
</td>
</tr>
<tr>
<td><p>Tri-allate </p></td>
<td><p>Triallate </p></td>
</tr>
<tr>
<td><p>Flurochloridone </p></td>
<td><p>Fluorochloridone </p></td>
</tr>
<tr>
<td><p>Chlorotoluron </p></td>
<td><p>Chlortoluron </p></td>
</tr>
<tr>
<td><p>Thiophanat-methyl </p></td>
<td><p>Thiophanate-methyl </p></td>
</tr>
<tr>
<td><p>Cyfluthrin </p></td>
<td><p>Beta-cyfluthrin </p></td>
</tr>
</tbody>
</table>

<strong>关于 ecoinvent 三个归因型系统模型 PDF 文件所载文档错误的信息</strong>

- 我们发现 Cut-off、EN15804 或 APOS 系统模型中部分数据集的 PDF 存在问题，这些数据集在未指定系统模型形式下具有多个输出。具体而言，这些 PDF 错误报告了分配因子。错误仅涉及分配因子；得分和全部交换均报告正确。  
  请注意，此问题仅涉及少数 PDF，且<strong>不影响 ecoinvent 数据库。</strong>

{% endtab %}

{% tab title="English 原文" %}

## Focusing on user comfort, ecoinvent v3.8 includes enhanced documentation and expands the sectoral coverage of the ecoinvent database with around 360 new and 700 updated datasets. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.8 was released on September 21st 2021</strong>. Discover how to [upgrade to the latest version](licensing.md).

Oct 28th, 2023

It further encompasses the first results of our collaboration with Rede ACV on the database’s Brazilian data.

With version 3.8 of the ecoinvent database users of ecoinvent data can benefit from enhanced documentation and information on products and markets, data linked in the additional system model “Allocation, cut-off, EN15804ˮ, which supports specifically EPD practitioners, a calculation support to work with the GHG protocol as well as around 360 new and 700 updated datasets related to agriculture, bamboo, batteries, chemicals and plastics, electronics, metals, forestry and wood, transport, and electricity. This version also releases the first results of the collaboration between Rede ACV and ecoinvent, aimed at enhancing the coverage and accuracy of Brazilian data in the database.

The data used for the additions and updates were provided by various organizations, including ETH, EMPA, Pforzheim University, and ACV Brazil.

### <strong>Features and Documentation </strong> <a href="#en-b0008" id="en-b0008"></a>

#### <strong>Product Information </strong> <a href="#en-b0009" id="en-b0009"></a>

The update aims at offering comfort to the users while engaging with the database. All products and services included in the database now integrate a description that supports users in identifying them. The information includes a definition of the product or service as seen in the database. Regarding services, their documentation now incorporates supporting information on how to use them. Overall, ecoinvent v3.8 contains 3’300 unique products and services.

#### <strong>Market Information </strong> <a href="#en-b0011" id="en-b0011"></a>

With the release of ecoinvent v3.8, ecoinvent aims at improving the description and information in the market datasets included in the database. Specifically, all market datasets have been reviewed, and their existing meta information has been complemented, corrected, or completed, in order to make the use and usability of these datasets more coherent and precise for the users of the ecoinvent database.

#### <strong>Database Overview </strong> <a href="#en-b0013" id="en-b0013"></a>

To provide a more concise overview of the contents of the ecoinvent database, the information about the activities included has been centralized into one file; “Database Overview for ecoinvent 3.8”. The file contains the following information:

- The lists of datasets contained in each of the system models, as well as the list of unlinked and unallocated datasets. For version 3.8, each dataset has been assigned to one or more sectors, which helps filter for datasets that can belong to different sectors.
- The geographies used in the ecoinvent database. Each geography is assigned a classification, and the geographies that are contained in each geography are indicated.
- The list of the LCIA methods for which ecoinvent calculates impact scores. The version of the methods is indicated, and the original source used for defining the characterization factors is provided.

#### <strong>Enhanced Support for GHG Protocol </strong> <a href="#en-b0018" id="en-b0018"></a>

With the updates of ecoinvent v3.8, the ecoinvent database now offers the possibility to calculate emissions from electricity according to the Scope 2 and Scope 3 Guidance of the GHG Protocol. For that, an additional file can be found in the ‘Files’ section of ecoQuery. Separated scope 2 and 3 emission factors for electricity-producing activities and electricity markets are now available in a spreadsheet. Emission factors are calculated based on the GWP100 (global warming potential) values from the IPCC 2013 AR5 report. They are representative of the end consumers of electricity and refer to the location-based reporting method, i.e., they represent grid average emission factors. On top of this, the new spreadsheet also provides disaggregated emissions and emission factors for individual greenhouse gases or groups of greenhouse gases.

#### <strong>New System Model for EPD Practitioners </strong> <a href="#en-b0020" id="en-b0020"></a>

Acknowledging the increasing importance of Environmental Product Declarations (EPDs) in the construction and manufacturing sector and the need for standardized, accurate, non-misleading communication of the environmental information for products, the ecoinvent association introduced the ‘allocation, cut-off, EN15804’ system model. The aim of this system model is twofold; on the one hand, the ‘allocation, cut-off, EN15804’ facilitates the EPD practitioners to comply with the standard EN15804&A2:2019. On the other hand, the new system model contributes to a harmonization in the calculation of the indicators of the standard. The system model is fully compliant with ISO 14025, ISO 21930 and EN15804&A2:2019. It provides all Life Cycle Inventory (LCI) indicators required by the aforementioned standards and adheres to the end-of-waste criteria set by the European Commission.

#### <strong>LCIA Methods </strong> <a href="#en-b0022" id="en-b0022"></a>

With ecoinvent v3.8, the latest versions of CML (v4.8 2016) and EF (v3.0, and adapted for [EN15804](https://eplca.jrc.ec.europa.eu/LCDN/EN15804.xhtml)) were added to LCIA methods. More details about the impact categories of all implemented methods can be found in the new database overview file.

### <strong>New and Updated Data</strong> <a href="#en-b0024" id="en-b0024"></a>

#### <strong>Brazilian Data </strong> <a href="#en-b0025" id="en-b0025"></a>

The [Cornerstone project](https://ecoinvent.org/projects/cornerstone-project/) was set up between Rede ACV (the Brazilian business network for LCA) and the ecoinvent association to improve the availability and access to background data representing key supply chains for Brazil. Rede ACV, through its contractor ACV Brasil, departed from existing content in the ecoinvent database to develop regionalized life cycle inventory (LCI) data representative of the situation in Brazil. The data in ecoinvent 3.8 cover the extraction, import and distribution of crude petroleum oil and natural gas, production of biodiesel (esterification of fatty acid methyl ester, FAME), distribution of diesel (for transport), and road freight transport by lorry. Older ecoinvent datasets have been updated for v3.8 to better reflect the country-specific supply of crude petroleum oil to petroleum refinery operation in Brazil.

#### <strong>Agriculture </strong> <a href="#en-b0027" id="en-b0027"></a>

The sector features a small update with the representation of new products, such as lentils and peas, and the recontextualization of agricultural services for Canada. Data for these updates were provided by the University of British Columbia and the Food Systems PRISM Laboratory.

#### <strong>Batteries </strong> <a href="#en-b0029" id="en-b0029"></a>

ecoinvent v3.8 includes new datasets for three types of Li-Ion batteries (NCA, NMC111, NMC811) and their production. These datasets were created by the Swiss Federal Laboratories for Materials Science and Technology (EMPA) and incorporate various chemicals, such as cobalt sulphate, disodium disulphite, vinyl carbonate and oxides, and hydroxides for the three battery types. The individual battery components (cathode, anode, high and low voltage systems, cells and battery management systems) are split, and each is represented in an individual dataset. Complementary, a new dataset on lead-acid batteries created by the University of Pforzheim is also included in the v3.8 update.

#### <strong>Chemicals and Plastics </strong> <a href="#en-b0031" id="en-b0031"></a>

In ecoinvent 3.8, we continued our efforts to update data and strengthen the collaboration with the industry. Data for styrene production was updated with the support of PlasticsEurope, and new and updated data for polyurethane foam was provided by EUROPUR.

#### <strong>Electricity </strong> <a href="#en-b0033" id="en-b0033"></a>

ecoinvent 3.8 contains updated, attributional electricity markets for most countries with a reference year of 2018. In the case of the US and Canada, the reference year is 2019. Additionally, the Swiss electricity markets, as well as transformation losses (high to medium and medium to low voltage), for all updated markets were adjusted. Data creation and review was done in collaboration with ETH Zurich and the Paul Scherrer Institute (PSI).

#### <strong>Electronics </strong> <a href="#en-b0035" id="en-b0035"></a>

Version 3.8 includes new datasets on consumer electronic devices. Based on the latest literature data, datasets for smartphones and tablets were added, and the existing dataset for laptops was updated. For the mobile devices, datasets for a new printed wiring board and liquid crystal display were created. Components in the corresponding supply chain have been adjusted as needed.

#### <strong>Forestry and Wood </strong> <a href="#en-b0037" id="en-b0037"></a>

The Wood sector has been updated with new data for bamboo forestry and the production of (intermediate) bamboo construction materials. i.e., bamboo pole, flattened bamboo, and woven bamboo mat. These new datasets were developed by Dr. Edwin Zea Escamilla with the support of the International Organization for Bamboo and Rattan INBAR.

#### <strong>Metals </strong> <a href="#en-b0039" id="en-b0039"></a>

New and updated datasets for the metals sector have been provided by EMPA (sponsored by the Swiss Federal Office for the Environment, BAFU) for ecoinvent version 3.8. The new data cover the production beryllium, ferroniobium and scandium oxide produced from rare earth tailings. Updates were provided by EMPA for the production of ferrochromium, lithium carbonate, strontium sulfate, tantalum, titanium, as well as for the mining of heavy mineral sands.

#### <strong>Transport </strong> <a href="#en-b0041" id="en-b0041"></a>

In collaboration with INFRAS, the datasets for air freight (belly and dedicated) transport are updated. The consumption of kerosene and the corresponding emissions were too low (version 3.6 to 3.7.1).

#### <strong>Resource Correction for Biogenic Carbon </strong> <a href="#en-b0043" id="en-b0043"></a>

In the “allocation, cut-off by classification” system model, the data for the forestry, wood, paper and cardboard sectors, biogenic carbon balances are restored after allocation using a new elementary exchange that allows to follow the process transparently.

### <strong>Relevant Documents and Files</strong> <a href="#en-b0045" id="en-b0045"></a>

#### <strong>Report of Changes</strong> <a href="#en-b0046" id="en-b0046"></a>

This report covers all changes made in the ecoinvent database between version 3.7.1 (2020) and version 3.8 (2021). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/87f134eda0de-Change-Report-v3.8.pdf)

#### <strong>Report of Changes</strong> <a href="#en-b0049" id="en-b0049"></a>

This automatically generated excel file provides an overview of changes made on the undefined unit process datasets between versions 3.7.1 and 3.8 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### <strong>Correspondence File </strong> <a href="#en-b0051" id="en-b0051"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.7.1 and 3.8 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Correspondence File](../assets/b50476fe0866-Correspondence-File-v3.7.1-v3.8.xlsx)

#### <strong>Database Overview File </strong> <a href="#en-b0054" id="en-b0054"></a>

The Database Overview file describes the contents of the database. The following information is contained in the file:

- #### <strong>Activity Overview(s)</strong> <a href="#en-h26" id="en-h26"></a>

The lists of datasets contained in each of the three [system models](system-models.md), as well as the list of unlinked and unallocated datasets. For version 3.8, each dataset has been assigned to one or more sectors, which helps filter for datasets that can belong to different sectors.

- #### <strong>ecoinvent Geographies </strong> <a href="#en-h27" id="en-h27"></a>

The geographies used in the ecoinvent database. Each geography is assigned a classification, and the geographies that are contained in each geography are indicated.

- #### <strong>LCIA Methods</strong> <a href="#en-h28" id="en-h28"></a>

The list of the LCIA methods for which ecoinvent calculates impact scores. The version of the methods is indicated, and the original source used for defining the characterization factors is provided.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Database Overview File](../assets/04194da4f83c-Database-Overview-for-ecoinvent-v3.8-1.xlsx)

### <strong>LCIA Implementation Report</strong> <a href="#en-b0063" id="en-b0063"></a>

The LCIA implementation report documents the implementation of LCIA methods for version 3.8.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [LCIA Implementation Report](../assets/e0a7eed10e0f-LCIA-Implementation-v3.8.pdf)

#### <strong>Other Files and Support Documents</strong> <a href="#en-b0066" id="en-b0066"></a>

More information about v3.8's files and supporting documents can be found on our support page, [Files in ecoQuery](files.md).

### <strong>Known Issues</strong> <a href="#en-b0068" id="en-b0068"></a>

This section lists all known data errors in version 3.8 of the ecoinvent database.

#### <strong>Data Issues </strong> <a href="#en-b0070" id="en-b0070"></a>

- The activities “electricity voltage transformation from high to medium voltage” and “electricity voltage transformation from medium to low voltage” for the RoW geography appear in the Allocation, cut-off and APOS system model. As the RoW markets for electricity do not exist for these system models, the datasets have LCIA scores of zero and should not be used.
- The exchange amount of the input from the environment “Tellurium, in ground” (compartment: “natural resource”; subcompartment: “in ground”) in the activity “copper mine operation and beneficiation, sulfide ore” for the geographies AU, CA, CL, CN, ID, KZ, RU, US, and ZM was found to be inconsistent with the amount in the GLO geography. The exchange amounts in the local geographies have been scaled down based on the assumption that these geographies extract 70% of the global Te that is extracted in copper ores (modelled in the GLO dataset).The new amounts for the undefined datasets are listed in the table below. They will be available with the release of v3.9.

<table>
<tbody>
<tr>
<td>
<p><strong>Dataset</strong> </p>
</td>
<td>
<p><strong>Unit</strong> </p>
</td>
<td>
<p><strong>Previous Value</strong> </p>
</td>
<td>
<p><strong>New Value</strong> </p>
</td>
</tr>
<tr>
<td>
<p>copper mine operation and beneficiation, sulfide ore, AU </p>
</td>
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
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
<td>
<p>kg </p>
</td>
<td>
<p>2.0062E-04 </p>
</td>
<td>
<p>6.9021E-05 </p>
</td>
</tr>
</tbody>
</table>

  

- The dataset styrene production was updated with support from PlasticsEurope for version 3.8. A company survey of three producers and four sites was conducted, as a consequence the benzene emissions to water were removed from the dataset and the benzene emissions to air reduced by four orders of magnitude. This update had a significant impact on selected human toxicity indicators (e.g. ecological scarcity 2013, carcinogenic substances into air-total). The other key contribution to human toxicity impact categories, e.g. in ReCiPe Midpoint (H) – human toxicity, is the material input of benzene. The market for benzene in the ecoinvent database represents a mix of benzene produced through catalytic reforming and pyrolysis gasoline as well as a share produced as a by-product of coking. The latter technology has significant human toxicity impact scores. Market shares will be revised within upcoming releases.
- The dataset “adipic acid production” is under review regarding the dinitrogen monoxide (N2O) emissions generated during its production. New emission abatement methods are examined, which would improve the removal efficiency and therefore reduce N2O emissions in both the RER and GLO datasets.”
- “The datasets “cathode production, NCA, for Li-ion battery” and “cathode production, NMC811 for Li-ion battery” have an incorrect input of the intermediate exchange “NMC111 oxide”. For the NCA cathode production the exchange should be “NCA oxide” and for NMC811 cathode production “NMC811” respectively. This leads to an overestimation of impact scores for the cathode production datasets as well as the subsequent battery cell and battery production datasets for NCA and NMC811. The correct scores for the affected datasets were recalculated and are accessible in the “Files” section of ecoQuery in the file: [Corrected LCIA scores – Oxide input in cathode production, li-ion batteries v3.8.xlsx”](https://v38.ecoquery.ecoinvent.org/File/File?fileName=ecoinvent+3.8+(2021)%2c+current%5csupporting+documents%5cCorrected+LCIA+scores+-+Oxide+input+in+cathode+production%2c+li-ion+batteries+v3.8.xlsx&hash=-1769755026&type=Files)
- The dataset “methylene diphenyl diisocyanate production” (GLO and RER) treats the formed hydrochloric acid as a waste, this does not reflect reality. Hydrochloric acid is a valuable by-product which is used or sold by the MDI producer.The ecoinvent association advices users to either use the LCIA scores from the current [ecoProfile](https://plasticseurope.org/sustainability/circularity/life-cycle-thinking/eco-profiles-set/) available on the PlasticsEurope website or to correct the unit process in ecoinvent by removing the waste neutralisation and treating HCl as a by-product.   
  To correct the ecoinvent dataset, we would advise user to use the undefined dataset available through ecoQuery and remove the exchanges of the input of sodium hydroxide and the outputs of sodium and chloride.

- The file “electricity emission factors – scope 2 – 3 in ecoinvent v3.8.xlsx” published on the 21st of September 2021 has been replaced by an updated version in December 2022. The new file “electricity emission factors – scope 2 – 3 in ecoinvent v3.8 (updated).xlsx” contains several corrections which are described in detail in the “read me” tab of the updated file. The updated file can be found under the v3.8 supporting document in the Files section of ecoQuery.

#### <strong>Life Cycle Impact Assessment Issues </strong> <a href="#en-b0118" id="en-b0118"></a>

- In the EF v3.0 methods (EF v3.0, EF v3.0 no LT, and EF v3.0 EN15804), the unit for the impact category “eutrophication: freshwater” should be “kg P-Eq” instead of “kg PO4-Eq”.   
  For some LCIA methods which are no longer updated but still published, names of elementary exchanges that were renamed were not updated in the files containing the characterization factors. This caused some of the characterization factors to be excluded from the implementation used for version 3.8. If wished by the user, this could be updated manually by changing from the old to the new name in the “LCIA implementation 3.8.xlsx”-file for the following exchanges:

<table>
<tbody>
<tr>
<td>
<p><strong>Old name</strong> </p>
</td>
<td>
<p><strong>New name</strong> </p>
</td>
</tr>
<tr>
<td>
<p>Tri-allate </p>
</td>
<td>
<p>Triallate </p>
</td>
</tr>
<tr>
<td>
<p>Flurochloridone </p>
</td>
<td>
<p>Fluorochloridone </p>
</td>
</tr>
<tr>
<td>
<p>Chlorotoluron </p>
</td>
<td>
<p>Chlortoluron </p>
</td>
</tr>
<tr>
<td>
<p>Thiophanat-methyl </p>
</td>
<td>
<p>Thiophanate-methyl </p>
</td>
</tr>
<tr>
<td>
<p>Cyfluthrin </p>
</td>
<td>
<p>Beta-cyfluthrin </p>
</td>
</tr>
</tbody>
</table>

<strong>Information about errors in the documentation reported in the PDF files for the ecoinvent three attributional system models</strong>

- We have identified an issue in some pdfs of datasets in the cut-off, EN15804 or APOS system models that are multioutput datasets in their undefined form. Specifically, allocation factors were wrongly reported in these pdfs. The error only concerns the allocation factors, scores and all exchanges were reported correctly.   
  Please be informed that this issue only concerns a few pdfs, and <strong>it does not affect the ecoinvent database.</strong>

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0030**：原文名称不足以唯一确定电池电解液所指物质，可能是 vinylene carbonate；不能与 ethylene carbonate 混同。 请对照电池数据集中交换的正式化学名称确认；当前保留英文。 [查看完整记录](../review/issues.md#issue-085)
- **待专家复核 · b0057**：本版本已新增 EN15804 模型，但此处仍称三个系统模型，可能沿用旧版表述。 请核对附件所列模型数量；暂忠实保留原文。 [查看完整记录](../review/issues.md#issue-086)
- **已处理／已说明 · b0046**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-087)
- **已处理／已说明 · b0048**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-088)
- **已处理／已说明 · b0049**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-089)
- **已处理／已说明 · b0050**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-090)
- **待专家复核 · b0026**：原文把脂肪酸甲酯写为酯化对象，而 FAME 本身已是酯；可能原应描述通过酯化／酯交换生产 FAME。 当前译文保留原文，请核实所指生物柴油生产活动及工艺说明。 [查看完整记录](../review/issues.md#issue-091)
