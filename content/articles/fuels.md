# 燃料

英文原题：Fuels  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/fuels)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-04-08

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 燃料几乎存在于每一种产品的生命周期中，例如用作过程能源、机械动力或运输服务能源。燃料供应可能涉及广泛的环境问题和社会问题。 <a href="#zh-b0002" id="zh-b0002"></a>

2025 年 5 月 5 日

[煤](#zh-b0007)  
[天然气](#zh-b0035)  
[石油](#zh-b0071)

许多燃料都是全球交易的重要商品。因此，有关从一次能源资源（化石源、核能或可再生来源）提取、生产和分配燃料的可靠数据，对大多数生命周期评价研究至关重要，但逐一收集这些数据十分困难。

ecoinvent 数据库包含大多数常见燃料类型的供应链信息。数据通常代表重要生产地区的开采和加工技术（主要为常规技术）的国家平均情况，以及采用多种运输方式运输原料或精制燃料的情况。化石燃料包括硬煤、褐煤、原油及精制石油产品、天然气和泥炭。来自生物质的可再生燃料通常称为生物燃料。ecoinvent 数据库包含以各种生物质原料生产气态（沼气/生物甲烷）、液态（生物乙醇、生物柴油或植物油甲酯）和固态生物燃料（能源用木制品）的信息，也提供核燃料铀的供应链数据。

### 煤 <a href="#zh-b0007" id="zh-b0007"></a>

煤是一种化石资源，由史前植物沉积物在高压和高温下转化而成，呈可燃的棕色至黑色沉积岩。所有大洲均有煤炭矿藏，但其丰度和质量在不同地区之间差异很大。

自工业革命以来，煤一直在全球能源生产中发挥重要作用。由于价格较低且资源丰富，煤是石油、天然气和可再生能源的经济替代品，但也是单位发电量排放最高的化石燃料。据 IEA 统计，煤仍是第二重要的一次能源载体，同时也是最大的人为二氧化碳排放源。此外，采煤废水可能呈酸性，含有多种污染物，并可能泄漏到环境中。

目前最大的煤炭储量位于澳大利亚、中国、印度、俄罗斯和美国。如今其他重要产煤国包括哥伦比亚、印度尼西亚和南非。

### 行业概览 <a href="#zh-b0011" id="zh-b0011"></a>

ecoinvent 数据库中的煤炭行业涵盖硬煤及褐煤（也称 brown coal）的开采与选煤。目前，数据库未按热值或应用（例如动力煤与炼焦煤）进一步区分质量或分类。这两种煤也会加工为用于产热的煤砖，而其原煤形式作为许多发电和产热数据集的投入。更多信息请参阅[能源行业](energy.md)。自[第 3.11 版](ecoinvent-version-3.11.md)起，褐煤和硬煤供应链依据 2022 年数据更新，并修订了采矿甲烷排放因子。硬煤开采新增四个欧洲地理区域，硬煤市场则扩展至 22 个新增欧洲地区，以及日本和韩国。

### 行业重点 <a href="#zh-b0013" id="zh-b0013"></a>

#### 硬煤 <a href="#zh-b0014" id="zh-b0014"></a>

硬煤生产按地区划分，例如澳大利亚、中国、印度尼西亚、印度、俄罗斯、南非、北美、南美、波兰、捷克、英国和挪威。对于印度和南非，开采与选煤分别建模为独立活动；其他地区则将这些步骤包含在同一个数据集中。在南非，矿山运行和选煤步骤进一步细分。采矿分为三种类型：拉铲露天开采、卡车与铲装设备露天开采，以及地下开采；选煤包括“洗煤”和“破碎与除矸”。

采矿过程本身高度耗能，并需要重型机械。有些矿山的能源需求由现场电厂满足。这些电厂燃烧杂质含量高的原煤，因此燃烧效率低、排放高，在 ecoinvent 中由“electricity production, hard coal, at coal mine power plant”活动表示。

开采和选煤之后，硬煤全球贸易在 ecoinvent 数据库中以进口活动表示，将生产地区与消费地区相应的市场活动链接。

#### 褐煤 <a href="#zh-b0018" id="zh-b0018"></a>

褐煤生产通过将欧洲和印度的露天开采与选煤合并的数据集表示。褐煤随后在许多国家用于产热和发电，也可加工为褐煤砖，以便运输，并常用于工业炉窑。

褐煤开采数据集包括采矿后的土地复垦、能源与水使用，以及过程中的排放和剥离废石。

### 数据提供者 <a href="#zh-b0021" id="zh-b0021"></a>

煤炭行业数据基于不同数据提供者的贡献，包括但不限于：

- [保罗谢勒研究所（PSI）](https://www.psi.ch/en)，瑞士
- [印度工业联合会](https://www.cii.in/)，印度
- [The Green House Company](https://tgh.co.za/)，南非

### 编辑 <a href="#zh-b0026" id="zh-b0026"></a>

- <strong>Christian Bauer</strong>，保罗谢勒研究所，瑞士
- <strong>Philippa Notten</strong>，The Green House Company，南非
- <strong>Christopher Oberschelp</strong>，苏黎世联邦理工学院，瑞士

### 相关来源 <a href="#zh-b0030" id="zh-b0030"></a>

数据库包含理解其内容背后建模与计算所需的全部信息，下列报告则提供进一步信息，帮助更好地理解该行业内的活动。

Dones, R., Bauer, C., Röder, A. (2007). Kohle（煤）. In: Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz（能源系统清单：能源系统生态比较及将其纳入瑞士生态平衡评价的基础）. Final report ecoinvent No. 6-VI, Paul Scherrer Institut Villigen, Swiss Centre for Life Cycle Inventories, Dübendorf, CH.

Ananth, P.V.K. and Tatia M. (2017). Life Cycle Inventories of Coal mining – India（印度煤炭开采生命周期清单）. ecoinvent Association, Zürich, Switzerland. 可在 SRI 项目成果中获取（需要注册）。

Notten, P. and Patel, I., (2017). Life Cycle Inventories of Coal mining and electricity production - South Africa（南非煤炭开采与发电生命周期清单）. ecoinvent Association, Zürich, Switzerland. 可在 SRI 项目成果中获取（需要注册）。

### 天然气 <a href="#zh-b0035" id="zh-b0035"></a>

天然气从石油开采早期被视为副产品，发展成为有价值的商品。近期事件，尤其在欧洲，凸显并增强了天然气供应的地缘政治重要性。如今，天然气在全球交易，以加压气体形式通过管道运输，或以液化天然气（LNG）形式由船舶运输。

天然气主要由甲烷组成。根据来源，还含有不同比例的乙烷、丙烷或丁烷，以及微量一氧化碳/二氧化碳、二氧化硫和氮氧化物。近年来，无论来自人类活动还是自然过程的甲烷向大气释放，都因其对全球变暖的贡献而受到广泛关注。因此，石油与天然气行业作为这些排放的主要人为来源，受到越来越严格的审视。天然气常被提出作为煤和石油的较低碳强度替代品，例如用于发电。然而，作为化石能源载体和强效温室气体，天然气的供应和燃烧仍可能对环境产生较大影响。

### 行业概览 <a href="#zh-b0038" id="zh-b0038"></a>

ecoinvent 数据库中的原油与天然气开采数据，在 2022 年发布第 3.9 版时的行业全面修订中进行了彻底更新。此次更新引入了统一建模方式：各生产国的石油和天然气生产分别表示为海上与陆上作业的平均联合（即伴生）生产。随后，2023 年第 3.10 版以 2021 年为参考年更新，将数据库中的生产国总数增至四十一个：

- petroleum and gas production, offshore（海上石油与天然气生产）：AE, AR, AU, AZ, BR, CA, CN, CO, DE, EC, EG, GB, ID, IN, IR, IT, KW, KZ, LY, MX, MY, NG, NL, NO, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, VE（三十六个地理区域）
- petroleum and gas production, onshore（陆上石油与天然气生产）：AE, AR, AU, AZ, BO, BR, CA, CN, CO, DE, DZ, EC, EG, GB, ID, IN, IQ, IR, IT, KW, KZ, LY, MX, MY, NG, NL, OM, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, UZ, VE（四十个地理区域）

开采过程的基础设施通过独立数据集表示。此外，还对高压和低压分配网络的建设及通过管道运输天然气的数据集进行建模。对于液化天然气（LNG）运输，ecoinvent 数据库包含天然气液化和气化过程。第 3.9 版更新改变了天然气产品（不含天然气液体）的参考条件：这些产品现在以标准立方米（Sm3）计量，定义为气体在 15°C（288.15°K）及大气压力（1.013 bar）下所占的体积。

### 行业重点 <a href="#zh-b0043" id="zh-b0043"></a>

#### 天然气供应 <a href="#zh-b0044" id="zh-b0044"></a>

2023 年第 3.10 版更新采用当时可得的最新全球年度统计数据，以反映 2021 年的全球供应情况。生产地理覆盖扩展至全球四十一个国家。合计而言，ecoinvent 数据库现覆盖全球原油产量的 96% 以上及天然气产量的 98% 以上。更新的关键内容包括来自世界银行<em>全球天然气火炬燃烧减排伙伴关系（GGFR）</em>的天然气火炬燃烧数据，以及来自国际能源署<em>《全球甲烷追踪报告 2022》</em>的天然气放空和逸散源甲烷排放数据。此外，依据 2021 年情况，为五十七个国家提供新增或更新的高压天然气供应数据，代表全球天然气消费量的 93%。第 3.10 版引入了十五个国家本地天然气分配（即低压）的消费组合，分别位于亚洲（中国、日本、韩国）、欧洲（比利时、法国、德国、意大利、荷兰、西班牙、瑞士、土耳其、英国）和北美（加拿大、墨西哥、美国）。

欧盟 27 国、挪威和土耳其的 2021 年天然气供应，依据 Eurostat 按贸易伙伴划分的进口统计建模。英国供应情况依据《英国能源统计摘要》（DUKES），世界其他地区则依据 bp 于 2022 年 6 月发布的《世界能源统计年鉴》。欧洲其他地区（RoE）和世界其他地区（RoW）的进口量，通过从相应地区总进口量中减去已单独建模的各国供应量之和计算。

#### 液化天然气 <a href="#zh-b0047" id="zh-b0047"></a>

液化天然气（LNG）压缩和气化的数据集由“natural gas production, liquefied”以及按来源区分、在需求地进行液化天然气进口和气化的活动表示。第 3.10 版更新将数据库中的 LNG 出口国增至十四个（AE, AU, DZ, EG, ID, MY, NG, NO, OM, PE, QA, RU, TT 和 US）。LNG 运输通过一个专门的运输数据集“transport, freight, sea, tanker for liquefied natural gas”建模；该数据集于 2019 年第 3.6 版建立，属于 SRI 项目的 LCI 部分。

#### 车用天然气 <a href="#zh-b0049" id="zh-b0049"></a>

不同压力下的天然气：低压（表压 &lt;0.1 bar）、中压（&gt;0.1 bar，&lt;1 bar）和高压（&gt;1bar），也提供“车用级”形式。这些数据集包含向车辆供应天然气所需的能源与基础设施，以及相关排放和损失。

#### 天然气燃烧 <a href="#zh-b0051" id="zh-b0051"></a>

天然气广泛纳入 ecoinvent 数据库的各个行业，包括能源与热生产、化学品、建筑材料和金属生产等。还提供特定燃烧活动，包括在燃气轮机、聚合物电解质膜燃料电池和固体氧化物燃料电池中使用天然气。

### 数据提供者 <a href="#zh-b0053" id="zh-b0053"></a>

天然气行业数据基于不同数据提供者的贡献，包括但不限于：

- <strong>ESU-services</strong>，瑞士
- <strong>产品生命周期与可持续转型国际参考中心</strong>（CIRAIG），加拿大
- <strong>保罗谢勒研究所</strong>（PSI），瑞士
- <strong>能源与环境研究所</strong>（IFEU），德国
- <strong>ACV Brazil</strong>，巴西

### 编辑 <a href="#zh-b0060" id="zh-b0060"></a>

- <strong>Eric Johnson</strong>（主编），Atlantic Consulting，瑞士
- <strong>Carl Vadenbo</strong>（联合编辑），ecoinvent Association，瑞士

### 相关来源 <a href="#zh-b0063" id="zh-b0063"></a>

数据库包含理解其内容背后建模与计算所需的全部信息，下列报告则提供进一步信息，帮助更好地理解该行业内的活动。

Bussa, M., Jungbluth, N., Meili, C., (2023).<strong>Life cycle inventories for long-distance transport and distribution of natural gas（天然气长距离运输与分配生命周期清单）</strong>. Schaffhausen, CH: ESU-services Ltd. 获取地址：<http://esu-services.ch/data/public-lci-reports/>

Faist Emmenegger, M., Del Duce, A., Moreno Ruiz, E., Brunner, F., (2017).<strong>Update of the European natural gas supply chains.（欧洲天然气供应链更新）</strong>Zurich, CH: ecoinvent Association.

Faist Emmenegger, M., Heck, T., Jungbluth, N., Tuchschmid, M., (2007).<strong>Erdgas. In: Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz.（天然气；载于《能源系统清单：能源系统生态比较及将其纳入瑞士生态平衡评价的基础》）</strong>

Meili, C., Jungbluth, N., Bussa , M., (2023).<strong>Life cycle inventories of crude oil and natural gas extraction（原油与天然气开采生命周期清单）</strong>. Schaffhausen, CH: ESU-services Ltd. 获取地址：<http://esu-services.ch/data/public-lci-reports/>

Notten, P.J., Althaus, H-J., Burke, M., Läderach, A., (2018).<strong>Life cycle inventories of global shipping – Global（全球航运生命周期清单）</strong>. Zurich, CH: ecoinvent Association.

Valebona, F., Rocha, T.B., Motta, F.L., (2020).<strong>Cornerstone Project. Recontextualization of Datasets: Methodology（Cornerstone 项目：数据集重新情境化方法）</strong>. Curitiba, BR: ACV Brazil.

### 石油 <a href="#zh-b0071" id="zh-b0071"></a>

在过去一个世纪中，石油（也称原油）已成为全球最重要的商品之一。由石油精炼得到的产品，其应用无处不在。一些应用显而易见，例如用于运输、机械或固定设施的汽油和柴油燃料。炼油厂的全部产品系列具有极广泛的用途，从道路表面材料到石油化学品。因此，几乎任何产品系统的生命周期都会以某种形式涉及石油产品。

### 行业概览 <a href="#zh-b0073" id="zh-b0073"></a>

ecoinvent 数据库包含原油开采、运输，以及将其精炼为液态和气态燃料及其他精制石油产品的数据。第 3.9 版对该行业进行了全面修订，2023 年第 3.10 版又进一步扩展，将生产数据覆盖增至四十一个国家。这些国家合计约占 2021 年全球石油产量的 96%，以及天然气产量的 98% 以上。所有按国家区分的开采数据集均采用共同方法创建，广泛依赖全球数据来源，以确保各地理区域之间具有高度一致性。各国的原油和天然气生产按平均联合（即伴生）生产建模，仅区分海上和陆上作业。

- petroleum and gas production, offshore（海上石油与天然气生产）：AE, AR, AU, AZ, BR, CA, CN, CO, DE, EC, EG, GB, ID, IN, IR, IT, KW, KZ, LY, MX, MY, NG, NL, NO, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, VE（36 个地理区域）
- petroleum and gas production, onshore（陆上石油与天然气生产）：AE, AR, AU, AZ, BO, BR, CA, CN, CO, DE, DZ, EC, EG, GB, ID, IN, IQ, IR, IT, KW, KZ, LY, MX, MY, NG, NL, OM, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, UZ, VE（40 个地理区域）

第 3.10 版更新新增巴西（BR）、哥伦比亚（CO）、印度（IN）、秘鲁（PE）和南非（ZA）原油的区域化消费组合，并更新瑞士（CH）、欧洲不含瑞士以及北美地区（RNA）的供应。这反映了这些地区及全球在 2021 年的石油供应情况。此外，在 2021 年发布第 3.8 版时，[Cornerstone 项目](https://ecoinvent.org/?s=cornerstone)已建立巴西炼油厂运行的国家特定投入。2019 年 ecoinvent 第 3.6 版在[SRI 项目](https://ecoinvent.org/activities/sri-project/)的 LCI 部分更新了炼油厂运行数据（CH 除外），并新增南非通过煤液化生产合成燃料的数据。

- petroleum refinery operations（炼油厂运行）：BR, CH, CO, Europe without Switzerland, GLO, IN, PE, ZA
- synthetic fuel production, from coal, high temperature Fisher-Tropsch operations（煤基高温费托合成燃料生产）：ZA

#### 原油质量与分类 <a href="#zh-b0080" id="zh-b0080"></a>

世界各地不同地下储层（油田）开采的原油，在质量上差异很大。原油分类常用的重要物理化学属性包括硫含量和美国石油学会比重（API 比重）。API 比重基于石油液体相对于水的密度的倒数，并换算为 API 度数，可用于比较不同油品的密度。原油类别的确切定义因来源和国家而异，例如 Jing 等（2020 年）采用以下分类范围：如表 1 所示，按 API 比重划分为轻质（API &gt;32°）、中质（22° &lt; API ≤32°）或重质（API ≤22°）；按硫（S）含量划分为低硫（≤0.5 wt% S）或高硫（&gt;0.5 wt% S）。对于 API 比重低于 10°、但黏度低于天然沥青的油品，有时使用“超重质原油”一词（USGS，2006 年）。

<table>
<tbody>
<tr>
<td><strong>类型</strong></td>
<td><strong>描述</strong></td>
<td> <strong>API 比重（°）</strong></td>
<td><strong>硫含量</strong></td>
</tr>
<tr>
<td rowspan="2"><strong>轻质</strong></td>
<td rowspan="2">
<ul>
<li>低密度、低黏度，室温下可流动；蜡含量低</li>
<li>轻质组分比例高</li>
<li>含可直接加工为汽油（石脑油）、煤油和优质柴油（瓦斯油）的烃类馏分</li>
</ul>
</td>
<td rowspan="2">&gt;32</td>
<td>≤0.5，低硫轻质</td>
</tr>
<tr>
<td>&gt;0.5，高硫轻质</td>
</tr>
<tr>
<td rowspan="2"><strong>中质</strong></td>
<td rowspan="2">
<ul>
<li>由于重组分比例较高，比轻质原油更重</li>
<li>多环芳烃（PAH）浓度较高</li>
<li>与较轻质原油相比，在环境中存留更长时间</li>
</ul>
</td>
<td rowspan="2">22-32</td>
<td>≤0.5，低硫中质</td>
</tr>
<tr>
<td>&gt;0.5，高硫中质</td>
</tr>
<tr>
<td rowspan="2"><strong>重质</strong></td>
<td rowspan="2">
<ul>
<li>高密度、高黏度，在正常储层条件下不易流入生产井</li>
<li>芳香烃和环烷烃相对于直链烷烃的比例高</li>
<li>氮、硫、氧和重金属含量高</li>
</ul>
</td>
<td rowspan="2">&lt;22</td>
<td>≤0.5，低硫重质</td>
</tr>
<tr>
<td>&gt;0.5，高硫重质</td>
</tr>
</tbody>
</table>

<strong>表 1</strong>——原油按 API 比重分类及描述，依据 Jing 等（2020 年；补充表 4）。

#### 长距离运输 <a href="#zh-b0102" id="zh-b0102"></a>

对于原油的区域和全球运输，提供陆上及海上管道、油驳、货车和远洋油轮运输数据。

#### 全球贸易 <a href="#zh-b0104" id="zh-b0104"></a>

ecoinvent 数据库中的数据目前既不区分不同原油质量，也不表示国际贸易流和区域供应组合。全球平均石油供应组合默认向所有需要石油的活动供给（除非数据集中另有规定）。

ecoinvent 数据库第 3.9 版引入了瑞士（CH）、欧洲不含瑞士以及北美地区（RNA）的区域特定供应组合。在此之前，仅对巴西炼油厂运行的石油供应进行了区域化建模，该数据在 2021 年第 3.8 版的 Cornerstone 项目中建立。虽然数据库未反映石油质量差异，但炼油厂运行建模考虑了相应地区炼油厂典型投入组合的质量特征。详情请参阅下文“石油精炼”。

能够考虑石油质量对炼油产品收率和资源需求的影响，是相对于此前版本的一项重大改进。

#### 石油精炼 <a href="#zh-b0108" id="zh-b0108"></a>

将原油精炼为液态和气态燃料及其他石油产品，涉及相互链接、相互依赖的复杂过程网络。为反映这一复杂性，2019 年 ecoinvent 数据库第 3.6 版更新采用了海德堡能源与环境研究所（ifeu）的科学家和行业专家开发的先进炼油模型。

#### 产品应用 <a href="#zh-b0110" id="zh-b0110"></a>

炼油厂产出的石油产品广泛用于众多工业行业。ecoinvent 数据库中的重要示例包括产热和发电，使用飞机、船舶、货车、汽车及其他方式运输货物和人员，农业与建筑设备，以及石油基化学品生产，而这些化学品又用于许多其他过程。

### 数据提供者 <a href="#zh-b0112" id="zh-b0112"></a>

- [能源与环境研究所（IFEU）](https://www.ifeu.de/en/)，德国
- [环境与过程系统工程（E&PSE）](http://www.epse.uct.ac.za/)研究组，南非开普敦大学
- [ACV Brazil](https://acvbrasil.com.br/)，巴西
- [ESU-services Ltd.](http://esu-services.ch/)，瑞士

### 编辑 <a href="#zh-b0117" id="zh-b0117"></a>

- <strong>Eric Johnson</strong>（主编），Atlantic Consulting，瑞士
- <strong>Christian Bauer</strong>（联合编辑），保罗谢勒研究所，瑞士
- <strong>Carl Vadenbo</strong>（联合编辑），ecoinvent Association，瑞士

### 相关来源 <a href="#zh-b0121" id="zh-b0121"></a>

Fehrenbach, H., Liebich, A., Abdalla, N., Biemann, K., Fröhlich, T., Simon, B., (2018).<strong>Life Cycle Inventories of Petroleum Refinery Operation（炼油厂运行生命周期清单）</strong>. Zurich, Switzerland: ecoinvent Association. 可在[SRI 项目成果](https://sri-lci.ecoinvent.org/)中获取（需要注册）。

Jing, Liang, et al., (2020).[Carbon intensity of global crude oil refining and mitigation potential（全球原油精炼碳强度与减缓潜力）](https://doi.org/10.1038/s41558-020-0775-3). Nature Climate Change 10.6: 526-532.

Jungbluth, N., (2007). Erdöl（石油）, in Dones R.,<strong>Sachbilanzen von Energiesystemen. Final report No. 6 ecoinvent data v2.0, 6（能源系统清单；最终报告第 6 号）</strong>. Dübendorf and Villigen, CH: Swiss Centre for LCI, PSI.

可在[ecoinvent 数据库第 2 版的“报告”（Reports）部分](ecoinvent-version-2.md)获取。

Meili, C., Jungbluth, N., Bussa, M., (2023a). L<strong>ife cycle inventories of crude oil and natural gas extraction（原油与天然气开采生命周期清单）</strong>. Schaffhausen, CH: ESU-services Ltd. 获取地址：<http://esu-services.ch/data/public-lci-reports/>

Meili, C., Jungbluth, N., Bussa, M., (2023b).<strong>Life cycle inventories of long-distance transport of crude oil（原油长距离运输生命周期清单）</strong>. Schaffhausen, CH: ESU-services Ltd. 获取地址：<http://esu-services.ch/data/public-lci-reports/>

Russo, V., von Blottnitz, H., (2018).<strong>Life Cycle Inventories of synthetic fuel production from coal and domestic fuel markets in South Africa（南非煤基合成燃料生产及国内燃料市场生命周期清单）</strong>. Zurich, CH: ecoinvent Association. 可在[SRI 项目成果](https://sri-lci.ecoinvent.org/)中获取（需要注册）。

Valebona, F., Rocha, T.B., Motta, F.L., (2020).<strong>Cornerstone Project. Recontextualization of Datasets: Methodology.（Cornerstone 项目：数据集重新情境化方法）</strong>Curitiba, BR: ACV Brazil.

{% endtab %}

{% tab title="English 原文" %}

## Fuels are part of virtually every product life cycle, for example through process energy, in machinery, or for transport services. The supply of fuels can be associated with a wide range of environmental problems and social issues. <a href="#en-b0002" id="en-b0002"></a>

May 5th, 2025

[Coal](#en-b0007)  
[Natural Gas](#en-b0035)  
[Petroleum](#en-b0071)

Many types of fuel are important commodities traded globally. Reliable data on the extraction, production, and distribution of fuels from primary energy resources (of fossil, nuclear, or renewable origin) is therefore crucial for most LCA studies, but very challenging to gather case-by-case.

The ecoinvent database contains supply chain information for most common fuel types. The data typically represents country-averages of (mainly conventional) extraction and processing technologies in important producing regions, as well as the transportation of crude or refined fuels via multiple modes of transport. Fossil fuels encompass hard coal, lignite, crude petroleum (oil), and refined petroleum products, natural gas, and peat. Renewable fuels derived from biomass are commonly referred to as biofuels. The ecoinvent database contains information on gaseous (biogas/biomethane), liquid (bioethanol, biodiesel or vegetable oil methyl ester), and solid biofuels (energy wood products) from various biomass feedstocks. Data is also available on the supply chains for uranium, a nuclear fuel.

### Coal <a href="#en-b0007" id="en-b0007"></a>

Coal is a fossil resource formed from prehistoric vegetation sediments that were transformed under high pressure and elevated temperatures into a combustible brownish to black sedimentary rock. Coal deposits are found on all continents; however, the abundance and quality of coal vary significantly between regions.

Since the industrial revolution, coal has continued to play a major role in global energy production. Due to its relatively low price and abundance, coal serves as an economic alternative to petroleum, natural gas, and renewables, however, it is also the fossil fuel with the highest emissions per unit of power produced. According to the IEA, coal remains the second-most important primary energy carrier, and simultaneously the largest anthropogenic source of carbon dioxide emissions. Additionally, wastewater from coal mining can be acidic and contain various pollutants that may leak into the environment.

The largest coal reserves are currently located in Australia, China, India, Russia, and the United States. Other important coal producers today include Colombia, Indonesia, and South Africa.

### Sector Overview <a href="#en-b0011" id="en-b0011"></a>

The coal sector in the ecoinvent database comprises the mining and preparation of hard coal and lignite (also known as brown coal). No further quality distinctions or classifications—such as heating value or by application (e.g., steam coal vs. coking coal)—are currently made in the ecoinvent database. Both coal types are also processed into briquettes for heat production, while the original/crude form is used as an input in many datasets for electricity and heat production. See the [energy sector](energy.md) for more information. Since [version 3.11](ecoinvent-version-3.11.md), supply chains for lignite and hard coal have been updated based on 2022 data, with revised methane emission factors for mining. Hard coal mining now includes four additional European geographies, while hard coal markets have expanded to 22 new European regions, as well as Japan and South Korea.

### Sector Highlights <a href="#en-b0013" id="en-b0013"></a>

#### Hard Coal <a href="#en-b0014" id="en-b0014"></a>

Production of hard coal is split into regions such as: Australia, China, Indonesia, India, Russia, South Africa, North America, South America, Poland, Czech Republic, United Kingdom, and Norway. For India and South Africa, the mining and preparation are modeled as separate activities, while for the other regions, these steps are contained in a single dataset. In South Africa, the mine operation and preparation steps are differentiated further. Mining is disaggregated into three types: open cast mining, dragline or truck, and shovel and underground mining, coal preparation includes “coal washing” and “crushing and destoning.”

The mining process itself is highly energy-intensive and requires heavy machinery. In some cases, energy demand at mines is met with on-site power plants. These are fired with raw coal, which is high in impurities and thus results in a low-efficiency combustion process with high emissions, represented in the ecoinvent activity “electricity production, hard coal, at coal mine power plant.”

After mining and preparation, the global trade of hard coal is represented in the ecoinvent database in the form of import activities, which link production regions to the corresponding market activities in consumer regions.

#### Lignite <a href="#en-b0018" id="en-b0018"></a>

Lignite production is represented in datasets combining open cast mining and preparation in Europe and India. Lignite is subsequently used for heat and electricity production in many countries. Alternatively, it can be processed into lignite briquettes, which enable easier transport and are often used in industrial furnaces.

The lignite mining datasets include land recultivation after mining, energy and water use, as well as emissions and spoils from the process.

### Data Providers <a href="#en-b0021" id="en-b0021"></a>

Data on the coal sector is based on contributions from different data providers, including (but not limited to):

- [Paul Scherrer Institute (PSI)](https://www.psi.ch/en), Switzerland
- [Confederation of Indian Industry](https://www.cii.in/), India
- [The Green House Company](https://tgh.co.za/), South Africa

### Editors <a href="#en-b0026" id="en-b0026"></a>

- <strong>Christian Bauer</strong>, Paul Scherrer Institut, Switzerland
- <strong>Philippa Notten</strong>, The Green House Company, South Africa
- <strong>Christopher Oberschelp</strong>, ETH Zürich, Switzerland

### Relevant Sources <a href="#en-b0030" id="en-b0030"></a>

While the database contains all the information needed to understand the modeling and calculations behind its contents, the reports below provide further information for an enhanced understanding of the activities within the sector.

Dones, R., Bauer, C., Röder, A. (2007). Kohle. In: Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz. Final report ecoinvent No. 6-VI, Paul Scherrer Institut Villigen, Swiss Centre for Life Cycle Inventories, Dübendorf, CH.

Ananth, P.V.K. and Tatia M. (2017). Life Cycle Inventories of Coal mining – India. ecoinvent Association, Zürich, Switzerland. Accessible at SRI project results (registration required).

Notten, P. and Patel, I., (2017). Life Cycle Inventories of Coal mining and electricity production - South Africa. ecoinvent Association, Zürich, Switzerland. Accessible at SRI project results (registration required).

### Natural Gas <a href="#en-b0035" id="en-b0035"></a>

Natural gas has evolved from being considered a by-product in the early days of oil extraction to a valuable commodity. Recent events, especially in Europe, have highlighted and amplified the geopolitical importance of natural gas supply. Today, natural gas is traded all over the world and transported through pipelines as pressurized gas or with ships in the form of liquefied natural gas (LNG).

Natural gas consists primarily of methane. Depending on origin, it also includes varying amounts of ethane, propane, or butane and traces of carbon monoxide/dioxide, sulfur dioxide, and nitrogen oxides. The release of methane into the atmosphere, both from human activities and natural processes, has gained much attention in recent years due to its contribution to global warming. As a result, the oil and gas industry has come under increasing scrutiny as a major anthropogenic source of these emissions. Natural gas is frequently put forward as a less carbon-intensive alternative to coal and oil, e.g., for electricity generation. However, as a fossil energy carrier and potent greenhouse gas, the supply and combustion of natural gas can still lead to high impacts on the environment.

### Sector Overview <a href="#en-b0038" id="en-b0038"></a>

The data on extraction of crude petroleum oil and natural gas in the ecoinvent database was completely revised within a sector overhaul for the release of version 3.9. in 2022. Introduced with this update, the production of petroleum and natural gas is consistently modeled as average combined (i.e., associated) from offshore and onshore operations in each country of production. With the reference year of 2021, the subsequent update for version 3.10 in 2023 increased the total number of production countries in the ecoinvent database to forty-one:

- petroleum and gas production, offshore: AE, AR, AU, AZ, BR, CA, CN, CO, DE, EC, EG, GB, ID, IN, IR, IT, KW, KZ, LY, MX, MY, NG, NL, NO, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, VE (thirty-six geographies)
- petroleum and gas production, onshore: AE, AR, AU, AZ, BO, BR, CA, CN, CO, DE, DZ, EC, EG, GB, ID, IN, IQ, IR, IT, KW, KZ, LY, MX, MY, NG, NL, OM, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, UZ, VE (forty geographies)

Infrastructure for extraction processes is represented in separate datasets. Additionally, datasets on the construction and transport of natural gas through pipelines for high- and low-pressure distribution networks are modeled. For the transport of natural gas in the form of liquefied natural gas (LNG), the ecoinvent database contains processes for the liquefaction and evaporation of natural gas. The update for 3.9 introduces a change to the reference conditions for natural gas products (except natural gas liquids): these products are now measured in standard cubic meters (Sm3), which is defined as the volume the gas takes up at 15°C (288.15°K) and atmospheric pressure (1.013 bar).

### Sector Highlights <a href="#en-b0043" id="en-b0043"></a>

#### Natural Gas Supply <a href="#en-b0044" id="en-b0044"></a>

With the update for 3.10 in 2023, the latest global annual statistics available were applied to reflect the global supply situation in 2021. The geographical coverage of production was expanded to a total of forty-one countries around the world. When combined, the ecoinvent database now covers more than 96% of the global production of crude petroleum oil and in excess of 98% of natural gas. Key features of the update are data on the flaring of natural gas from the <em>Global Gas Flaring Reduction Partnership (GGFR)</em> of the World Bank and on methane emissions from gas venting and fugitive emission sources from the International Energy Agency’s <em>Global Methane Tracker 2022</em>. In addition, new or updated natural gas supplies (at high pressure) are provided for fifty-seven countries, representing 93% of global gas consumption, based on the situation in 2021. Consumption mixes for local distribution of natural gas (i.e., at low pressure) are introduced for fifteen countries in Asia (China, Japan, and South Korea), Europe (Belgium, France, Germany, Italy, the Netherlands, Spain, Switzerland, Turkey, and the United Kingdom), and North America (Canada, Mexico, and the USA) with version 3.10.

The supply of natural gas in 2021 was modeled for EU-27 countries, Norway, and Turkey based on statistics on imports by trade partner from EuroStat. The supply situation in the United Kingdom was derived from the ‘Digest of UK Energy Statistics (DUKES), and on bp’s ‘Statistical Review of World Energy’ from June 2022’ for the rest of the world. Imports to Rest-of-Europe (RoE) and the Rest-of-the-World (RoW) geographies were calculated by subtracting the sum of country-specific supply modeled separately from the total import of the respective regions.

#### Liquefied Natural Gas <a href="#en-b0047" id="en-b0047"></a>

Datasets for the compression and evaporation of liquefied natural gas (LNG) are represented as “natural gas production, liquefied” and origin-specific activities for import and evaporation of liquefied natural gas at the place of demand. The update for version 3.10 expanded the number of LNG-exporting countries in the database to fourteen (AE, AU, DZ, EG, ID, MY, NG, NO, OM, PE, QA, RU, TT, and the US). LNG transport is modeled in a single dedicated transport dataset “transport, freight, sea, tanker for liquefied natural gas”, established for version 3.6 in 2019 (within the LCI component of the SRI program).

#### Natural Gas, Vehicle Grade <a href="#en-b0049" id="en-b0049"></a>

Natural gas at different pressures: low pressure (&lt;0.1 bar overpressure), medium pressure (&gt;0.1 bar, &lt; 1 bar), and high pressure (&gt;1bar) is also provided in “vehicle grade” form. These datasets include emissions, losses as well as energy and infrastructure required to supply natural gas for vehicles.

#### Burning of Natural Gas <a href="#en-b0051" id="en-b0051"></a>

Natural gas is integrated extensively across various sectors of the ecoinvent database. The sectors include i.a. energy and heat production, the production of chemicals, building materials, and metals. Specific combustion activities, including the burning of natural gas in gas turbines, polymer electrolyte membrane fuel cells, and solid oxide fuel cells, are also available.

### Data Providers <a href="#en-b0053" id="en-b0053"></a>

Data in the natural gas sector is based on contributions from different data providers. These include, but are not limited to:

- <strong>ESU-services</strong>, Switzerland
- <strong>International Reference Center for Life Cycle of Products and Sustainable Transition</strong> (CIRAIG), Canada
- <strong>Paul Scherrer Institute </strong>(PSI), Switzerland
- <strong>Institute for Energy and Environmental Research</strong> (IFEU), Germany
- <strong>ACV Brazil</strong>, Brazil

### Editors <a href="#en-b0060" id="en-b0060"></a>

- <strong>Eric Johnson</strong> (Main Editor), Atlantic Consulting, Switzerland
- <strong>Carl Vadenbo</strong> (Co-Editor), ecoinvent Association, Switzerland

### Relevant Sources <a href="#en-b0063" id="en-b0063"></a>

While the database contains all needed information to understand the modeling and calculations behind its contents, the reports below provide further information for enhanced understanding of the activities within the sector.

Bussa, M., Jungbluth, N., Meili, C., (2023). <strong>Life cycle inventories for long-distance transport and distribution of natural gas</strong>. Schaffhausen, CH: ESU-services Ltd. Available from: <http://esu-services.ch/data/public-lci-reports/>

Faist Emmenegger, M., Del Duce, A., Moreno Ruiz, E., Brunner, F., (2017). <strong>Update of the European natural gas supply chains.</strong> Zurich, CH: ecoinvent Association.

Faist Emmenegger, M., Heck, T., Jungbluth, N., Tuchschmid, M., (2007). <strong>Erdgas. In: Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz. </strong>

Meili, C., Jungbluth, N., Bussa , M., (2023). <strong>Life cycle inventories of crude oil and natural gas extraction</strong>. Schaffhausen, CH: ESU-services Ltd. Available from: <http://esu-services.ch/data/public-lci-reports/>

Notten, P.J., Althaus, H-J., Burke, M., Läderach, A., (2018). <strong>Life cycle inventories of global shipping – Global</strong>. Zurich, CH: ecoinvent Association.

Valebona, F., Rocha, T.B., Motta, F.L., (2020). <strong>Cornerstone Project. Recontextualization of Datasets: Methodology</strong>. Curitiba, BR: ACV Brazil.

### Petroleum <a href="#en-b0071" id="en-b0071"></a>

Petroleum (also referred to as crude oil or just crude) has established itself as one of the most important global commodities over the last century. The applications of products that can be refined from petroleum are omnipresent. Some are obvious, such as gasoline and diesel fuels for transportation, machinery, or stationary installations. The full product slate of the refinery finds uses in a vast range of applications, from road surfaces to petrochemicals. Hence, petroleum products can be encountered, in one form or another, in the life cycles of virtually any product system.

### Sector Overview <a href="#en-b0073" id="en-b0073"></a>

The ecoinvent database includes data on the extraction, transport, and refining of crude petroleum oil to liquid and gaseous fuels, as well as other refined petroleum products. An extensive overhaul of the sector for version 3.9 and then further expended for the release of version 3.10 of the database in 2023 increased the data coverage of the production to forty-one countries. Taken together, these countries represented approximately 96% of the global production of petroleum and over 98% of natural gas output in 2021. All country-specific extraction datasets have been created using a common approach, relying extensively on global data sources to ensure a high degree of consistency between the geographies covered. The production of crude petroleum oil and natural gas is modeled as the average combined (i.e., associated) production of oil and gas, only distinguishing between offshore and onshore operations, for each country.

- petroleum and gas production, offshore: AE, AR, AU, AZ, BR, CA, CN, CO, DE, EC, EG, GB, ID, IN, IR, IT, KW, KZ, LY, MX, MY, NG, NL, NO, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, VE (36 geographies)
- petroleum and gas production, onshore: AE, AR, AU, AZ, BO, BR, CA, CN, CO, DE, DZ, EC, EG, GB, ID, IN, IQ, IR, IT, KW, KZ, LY, MX, MY, NG, NL, OM, PE, PL, QA, RO, RU, SA, TH, TM, TR, TT, US, UZ, VE (40 geographies)

The update for version 3.10 included regionalized consumption mixes of crude petroleum oil in Brazil (BR), Colombia (CO), India (IN), Peru (PE), and South Africa (ZA), in addition to updating supply to Switzerland (CH), Europe without Switzerland, and the Region of North America (RNA). This reflects the petroleum supply situation in these regions and globally in 2021. In addition, a country-specific input to petroleum refinery operations in Brazil had already been established within the [Cornerstone project](https://ecoinvent.org/?s=cornerstone) for the release of version 3.8 in 2021. The data on petroleum refinery operation were updated (except for CH), alongside new data on synthetic fuel production from coal liquefaction in South Africa, within the LCI component of the [SRI programme](https://ecoinvent.org/activities/sri-project/) for ecoinvent version 3.6 in 2019.

- petroleum refinery operations: BR, CH, CO, Europe without Switzerland, GLO, IN, PE, ZA
- synthetic fuel production, from coal, high temperature Fisher-Tropsch operations: ZA

#### Quality and Classification of Crude Petroleum Oil <a href="#en-b0080" id="en-b0080"></a>

Crude petroleum extracted from different subterranean reservoirs (oil fields) around the world shows large variations in terms quality. Among the most important physio-chemical properties commonly used to classify crude oils are sulfur content and the American Petroleum Institute gravity (API gravity). API gravity is the inverse of a petroleum liquid’s density relative to that of water scaled to degrees API, and it can be used to compare the densities of different oil types. The exact definitions of crude oil classes differ between sources and countries, e.g., Jing et al. (2020) use the following ranges for classification: As indicated in Table 1, API gravity (as light: API &gt;32°; medium: 22° &lt; API ≤ 32°, or; heavy: API ≤ 22°) and sulfur (S) content (as sweet: ≤ 0.5 wt% S, or; and sour: &gt; 0.5 wt% S). The term ‘extra-heavy crude oil’ is sometimes used for oils with an API gravity less than 10°, but with lower viscosity than natural bitumen (USGS, 2006).

<table>
<tbody>
<tr>
<td><strong>Type</strong></td>
<td><strong>Description</strong></td>
<td> <strong>API gravity (°)</strong></td>
<td><strong>Sulfur content</strong></td>
</tr>
<tr>
<td rowspan="2"><strong>Light</strong></td>
<td rowspan="2">
<ul>
<li>Low density, low viscosity and that flows at room temperature; Low wax content</li>
<li>High proportion of light</li>
<li>Hydrocarbon fractions that can be directly processed into gasoline (naphtha), kerosene, and high-quality diesel (gas oil)</li>
</ul>
</td>
<td rowspan="2">&gt;32</td>
<td>≤ 0.5, Sweet Light</td>
</tr>
<tr>
<td>&gt; 0.5, Sour Light</td>
</tr>
<tr>
<td rowspan="2"><strong>Medium</strong></td>
<td rowspan="2">
<ul>
<li>Heavier than light crude oils due to a larger proportion of the heavier compounds</li>
<li>Higher concentration of PAHs</li>
<li>Persist in the environment for a longer period compared to lighter crude oils</li>
</ul>
</td>
<td rowspan="2">22-32</td>
<td>≤ 0.5, Sweet Medium</td>
</tr>
<tr>
<td>&gt; 0.5, Sour Medium</td>
</tr>
<tr>
<td rowspan="2"><strong>Heavy</strong></td>
<td rowspan="2">
<ul>
<li>High density, high viscosity and does not easily flow to production wells under normal reservoir conditions</li>
<li>High ratio of aromatics and naphthenes to linear alkanes</li>
<li>High amounts of nitrogen, sulfur, oxygen and heavy metals</li>
</ul>
</td>
<td rowspan="2">&lt;22</td>
<td>≤ 0.5, Sweet Heavy</td>
</tr>
<tr>
<td>&gt; 0.5, Sour Heavy</td>
</tr>
</tbody>
</table>

<strong>Table 1</strong>– Crude petroleum oil classification based on API gravity and description according to Jing et al. (2020; Supplementary Table 4).

#### Long Distance Transport <a href="#en-b0102" id="en-b0102"></a>

For the regional and global movements of crude petroleum oil, data on transport via onshore and offshore pipelines, barge tankers, lorries as well as transoceanic tankers are available.

#### Global Trade <a href="#en-b0104" id="en-b0104"></a>

The data in the ecoinvent database currently neither distinguish between different crude oil qualities nor represent international trade flows and regional supply mixes. The global average supply mix of petroleum supplies by default all petroleum-demanding activities (unless otherwise specified in the datasets).

Region-specific supply mixes for Switzerland (CH), Europe without Switzerland, and the Region of North America (RNA) were introduced with version 3.9 of the ecoinvent database. Prior to that, regionalized petroleum supply was only modeled for refinery operations in Brazil (established within the Cornerstone project for the release of version 3.8 in 2021). Although petroleum qualities are not reflected in the database, the modeling of petroleum refinery operations accounts for the quality characteristics of the typical input mix supplied to refineries in the respective region. Read “Petroleum Refining” below for more details.

The ability to consider the influence of petroleum quality on refinery product yields and resource requirements constitutes a major improvement compared to previous versions.

#### Petroleum Refining <a href="#en-b0108" id="en-b0108"></a>

The refining of crude petroleum oil to liquid and gaseous fuels, as well as other petroleum products, involves a complex network of interlinked and interdependent processes. To reflect this complexity, the update of version 3.6 of the ecoinvent database in 2019 applied/included an advanced refinery model developed by scientists and industry experts at the Institut für Energie- und Umweltforschung (ifeu), Heidelberg.

#### Product Applications <a href="#en-b0110" id="en-b0110"></a>

The petroleum products yielded in refineries are used in a wide range of applications across numerous industrial sectors. Among other prominent examples, the ecoinvent database includes data on the generation of heat and electricity, the transport of goods and people by aircraft, ships, lorries, cars, and other means, agricultural and construction equipment, and the production of petroleum-based chemicals, which in turn are used in many other processes.

### Data Providers <a href="#en-b0112" id="en-b0112"></a>

- [Institute for Energy and Environmental Research (IFEU)](https://www.ifeu.de/en/), Germany
- [Environmental and Process System Engineering (E&PSE)](http://www.epse.uct.ac.za/) research group at the University of Cape Town, South Africa
- [ACV Brazil](https://acvbrasil.com.br/), Brazil
- [ESU-services Ltd.](http://esu-services.ch/), Switzerland

### Editors <a href="#en-b0117" id="en-b0117"></a>

- <strong>Eric Johnson</strong> (Main Editor), Atlantic Consulting, Switzerland
- <strong>Christian Bauer </strong>(Co-Editor), Paul Scherrer Institut, Switzerland
- <strong>Carl Vadenbo</strong> (Co-Editor), ecoinvent Association, Switzerland

### Relevant Sources <a href="#en-b0121" id="en-b0121"></a>

Fehrenbach, H., Liebich, A., Abdalla, N., Biemann, K., Fröhlich, T., Simon, B., (2018). <strong>Life Cycle Inventories of Petroleum Refinery Operation</strong>. Zurich, Switzerland: ecoinvent Association. Accessible at [SRI project results](https://sri-lci.ecoinvent.org/) (registration required).

Jing, Liang, et al., (2020). [Carbon intensity of global crude oil refining and mitigation potential](https://doi.org/10.1038/s41558-020-0775-3). Nature Climate Change 10.6: 526-532.

Jungbluth, N., (2007). Erdöl, in Dones R., <strong>Sachbilanzen von Energiesystemen. Final report No. 6 ecoinvent data v2.0, 6</strong>. Dübendorf and Villigen, CH: Swiss Centre for LCI, PSI.

Accessible in the [Reports section of version 2. of the ecoinvent database](ecoinvent-version-2.md).

Meili, C., Jungbluth, N., Bussa, M., (2023a). L<strong>ife cycle inventories of crude oil and natural gas extraction</strong>. Schaffhausen, CH: ESU-services Ltd. Available from: <http://esu-services.ch/data/public-lci-reports/>

Meili, C., Jungbluth, N., Bussa, M., (2023b). <strong>Life cycle inventories of long-distance transport of crude oil</strong>. Schaffhausen, CH: ESU-services Ltd. Available from: <http://esu-services.ch/data/public-lci-reports/>

Russo, V., von Blottnitz, H., (2018). <strong>Life Cycle Inventories of synthetic fuel production from coal and domestic fuel markets in South Africa</strong>. Zurich, CH: ecoinvent Association. Accessible at [SRI project results](https://sri-lci.ecoinvent.org/) (registration required).

Valebona, F., Rocha, T.B., Motta, F.L., (2020). <strong>Cornerstone Project. Recontextualization of Datasets: Methodology.</strong> Curitiba, BR: ACV Brazil.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0015**：原文标点使三类采矿方式的边界不清；依据 dragline 与 truck and shovel 的工艺组合解释。 请对照南非采矿数据集名称确认三类技术划分。 [查看完整记录](../review/issues.md#issue-139)
- **待专家复核 · b0042**：开尔文的规范单位符号应为 K，而原文使用 °K；数值正确，译文保留原文单位写法便于追溯。 建议源文与译文同时将 °K 修正为 K。 [查看完整记录](../review/issues.md#issue-140)
- **待专家复核 · b0098**：表格重质原油边界为 <22，而 b0081 正文定义为 API ≤22°，在 22° 处不一致。 请依据 Jing 等原始表格核对边界；当前忠实保留各处原文。 [查看完整记录](../review/issues.md#issue-141)
- **待专家复核 · b0105**：本段称无区域供应组合，但紧接的 b0106 及前文 b0077 明确描述新增区域供应组合，可能为沿用旧版文字。 请核对该段适用版本后修订；译文暂保留源文陈述。 [查看完整记录](../review/issues.md#issue-142)
