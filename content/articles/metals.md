# 金属

英文原题：Metals  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/metals)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-12-15

{% tabs %}

{% tab title="中文" %}

## 在 ecoinvent 数据库中，金属行业涵盖采矿、半成品金属产品生产，以及制造业中生产金属制成品的金属加工活动等经济活动。 <a href="#zh-b0002" id="zh-b0002"></a>

2024 年 10 月 7 日

金属在社会中无处不在，广泛用于各种应用，从建筑和制造等传统行业，到先进的现代电信和信息技术。此外，全球经济和技术发展持续推动对越来越多种金属的需求，其中许多金属在地球化学意义上稀缺，并作为贱金属生产的副产品出现。由此形成的金属行业具有复杂的全球贸易流，以及相互依赖、相互关联、跨国的生产链。

虽然金属产品对现代社会的运行至关重要，但其生产可能造成严重环境损害。采矿会破坏环境、耗竭自然资源，并可能使有毒物质扩散到环境中，而选矿和精炼金属生产通常需要大量能源。因此，在其他产品的供应链中使用金属，可能显著增加这些产品的环境影响。据[国际资源委员会](https://www.resourcepanel.org/)估计，金属生产约占全球气候变化影响的 10% 以及与颗粒物有关健康影响的 12%。

### 行业概览 <a href="#zh-b0006" id="zh-b0006"></a>

ecoinvent 数据库中的金属行业涵盖从自然资源开采与选矿，到金属和矿产商品生产的活动。特定金属（或多种金属）的生产以相互链接的活动链表示。生产链始于“mine operation”活动，该活动涵盖矿石开采和选矿，并产生一种或多种金属/矿物精矿。随后，精矿经过一个或多个活动加工，得到精炼金属。构成生产链的数据集数量因金属而异；有些生产链包含许多中间步骤、生产路线和最终产品，例如钢铁生产。另一些情况下，从采矿到精炼的所有生产活动汇总为一个活动，例如“cobalt production”。

对于部分金属，数据库提供基于不同技术的多种生产路线数据集。例如，原生铜生产有分别采用火法冶金和湿法冶金的两条数据集链，也提供利用回收废铜生产再生铜的数据集。因此，数据库用户可以选择通过特定生产路线生产的铜，例如火法冶金生产的原生铜；或者使用“market for copper, cathode”数据集，选择来自不同原生和再生来源的铜的组合。总计有超过 400 个金属生产相关数据集，生产超过 200 种不同产品。

### <strong>行业</strong><strong>重点</strong> <a href="#zh-b0009" id="zh-b0009"></a>

#### <strong>采矿和采石作业</strong> <a href="#zh-b0010" id="zh-b0010"></a>

数据库包含来自超过二十个地理区域的八十多个数据集，对从地下开采自然资源进行建模。其中一些数据集整合了从采矿到最终产品的多个生产链步骤，另一些则聚焦特定采矿作业。采矿和采石活动生产八十多种中间和最终矿产商品，例如金属精矿（如铜、铂族金属或稀土氧化物精矿）、精炼金属（如金、银或钴）和矿物骨料（如砂、砾石或白云石）。这些商品包括贱金属、贵金属（包括铂族金属）、稀土元素和其他矿产品。有些数据集代表全球平均情况，另一些具有区域特异性（例如稀土元素开采主要发生在中国）；对于铜或金等部分商品，还提供不同地理区域的数据集。

#### <strong>金属生产</strong> <a href="#zh-b0012" id="zh-b0012"></a>

金属精矿等原料商品经进一步精炼和选矿，成为最终金属产品。数据库考虑不同技术，例如原生铜生产有分别采用火法冶金和湿法冶金的两条数据集链。最终金属产品涵盖贱金属（铜、铅、镍、锌）、多种贵金属（例如金、银、铂族金属）和稀土元素氧化物。

#### <strong>金属加工</strong> <a href="#zh-b0014" id="zh-b0014"></a>

为获得板材、卷材和棒材等半成品及最终金属产品，精炼金属需要进一步加工。ecoinvent 数据库包含八十多项对部分加工步骤建模的活动，主要涉及铝、铁和钢。这些活动包括钻削、铣削、车削和挤压，以及通用金属加工数据。使用这些数据集，可以对生产特定金属零件所需的各个步骤进行建模。

#### <strong>回收利用和再生材料</strong> <a href="#zh-b0016" id="zh-b0016"></a>

金属和金属产品可回收利用，作为再生材料使用。ecoinvent 数据库通过所谓“treatment”处理活动表示这一点，例如“treatment of copper scrap by electrolytic refining”。这些活动的输出与原生生产的输出相对应，例如“copper, cathode”，并向市场数据集（例如“market for copper, cathode”）供应。“处理”活动连同处理采矿和冶炼过程中产生的尾矿及炉渣的活动，横跨金属行业与[废物管理行业](waste-management-and-recycling.md)。

#### 尾矿处理 <a href="#zh-b0018" id="zh-b0018"></a>

矿山尾矿是金属矿石开采与选矿过程中产生的主要废物，通常堆存于尾矿库。长期而言，这些尾矿库可能给周边环境带来风险，特别是硫化矿石产生的尾矿。含硫化物尾矿长期储存所导致的潜在环境影响取决于多种因素，例如尾矿组成、尾矿库特征和气候条件。

为涵盖金属采矿尾矿的潜在环境影响范围，ecoinvent 数据库包含对六种不同主产金属（如铜或镍）的含硫化物尾矿入库堆存建模的数据集，共覆盖十九个国家，这些国家占相应金属开采的主要份额。此外，还提供一个代表平均组成的含硫化物尾矿入库堆存数据集。

### 应用场景 <a href="#zh-b0021" id="zh-b0021"></a>

金属生产数据可用于生命周期评价、碳足迹（温室气体核算）和物质流分析研究，也可支持各种产品和服务的环境产品声明（EPD）。

### 数据提供者 <a href="#zh-b0023" id="zh-b0023"></a>

金属活动生命周期清单（LCI）数据集的主要提供者包括但不限于：

- [国际铝业协会（International Aluminium Institute）](https://international-aluminium.org/)
- [加拿大铝业协会（Association de l’aluminium du Canada）](https://aluminium.ca/)
- [国际锌业协会（International Zinc Association）](https://www.zinc.org/)
- [钴业协会（Cobalt Institute）](https://www.cobaltinstitute.org/)
- [印度工业联合会](https://www.cii.in/)（CII），印度
- [南非威特沃特斯兰德大学](https://www.wits.ac.za/)
- [瑞士联邦材料科学与技术实验室](https://www.empa.ch/)（Empa）
- [格拉茨技术大学（TU Graz）](https://www.tugraz.at/home/)
- [开普敦大学（UCT）](https://www.uct.ac.za/)
- [瑞士联邦理工学院](https://ethz.ch/en.html)（ETH）

### 编辑 <a href="#zh-b0035" id="zh-b0035"></a>

- <strong>Louis Brimacombe</strong>（主编），谢菲尔德大学，英国
- <strong>Robert Istrate</strong>，莱顿大学工业生态学助理教授
- <strong>Vanessa Schenker</strong>，苏黎世联邦理工学院生态系统设计教席博士后研究员
- <strong>Dieuwertje Schrijvers</strong>，WeLOOP 项目经理

### 相关来源 <a href="#zh-b0040" id="zh-b0040"></a>

Charikinya E., Broadhurst J., Dlamini R., Goga T., Harding K., Russo V., Viljoen D. and von Blottnitz H., (2019).<strong>Life Cycle Inventories of Primary Production of Precious and Scarce Metals – South Africa（南非贵金属及稀缺金属原生生产生命周期清单）</strong>. ecoinvent Association, Zürich, Switzerland. 可在[SRI 项目成果](https://sri-lci.ecoinvent.org/)中获取（需要注册）。

Soni H., (2019).<strong>Life Cycle Inventories of Iron and Steel – India（印度钢铁生命周期清单）</strong>. ecoinvent Association, Zürich, Switzerland. 可在[SRI 项目成果](https://sri-lci.ecoinvent.org/)中获取（需要注册）。

Classen, M., Althaus H.-J., Blaser, S., Tuchschmid, M., Jungbluth N., Doka, G., Faist Emmenegger, M., Scharnhorst, W., (2009).<strong>Life Cycle Inventories of Metals（金属生命周期清单）</strong>. Final report ecoinvent data v2.1, No 10. Dübendorf: Swiss Centre for Life Cycle Inventories. 可在[ecoinvent 数据库第 2 版的“报告”（Reports）部分](ecoinvent-version-2.md)获取。

{% endtab %}

{% tab title="English 原文" %}

## In the ecoinvent database, the metals sector comprises economic activities including mining, the production of semi-fabricated metal products up to the metal fabrication activities in the manufacturing sector that produce finished metal goods. <a href="#en-b0002" id="en-b0002"></a>

Oct 7th, 2024

Metals are ubiquitous in society and are used in a wide range of applications, from those in traditional sectors, such as construction and manufacturing, to those in advanced modern telecommunications and information technology. Furthermore, global economic and technological development continues to drive up demand for an ever-broadening array of metals, many of which are geochemically scarce and occur as by-products of base metal production. This has given rise to a metals sector that is characterized by complex global trade flows and interdependent, interconnected, and international production chains.

While metal products are vital to the functioning of modern-day societies, their production can cause severe environmental damage. Mining degrades the environment, depletes natural resources, and may lead to the dispersion of toxic substances in the environment, while mineral processing and production of refined metals often require significant amounts of energy. Consequently, the use of metals throughout the supply chains of other products may contribute significantly to the environmental impacts of those products. According to the [International Resource Panel](https://www.resourcepanel.org/), metal production is responsible for about 10% of global climate change and 12% of particulate matter-related health impacts.

### Sector Overview <a href="#en-b0006" id="en-b0006"></a>

In the ecoinvent database, the metals sector comprises activities from the mining and beneficiation of natural resources to the production of metal and mineral commodities. The production of a specific metal (or metals) is represented as a chain of linked activities. Chains start with “mine operation” activities that cover the mining and beneficiation of ores and yield one or multiple metal/mineral concentrates. Concentrates are subsequently processed through one or multiple activities to yield refined metals. The number of datasets that make up a production chain varies between metals, with some chains comprising many intermediate steps, production routes, and final products, such as iron and steel production. In other cases, all production activities from mining through to refining are aggregated into one single activity, such as “cobalt production.”

For some metals, datasets are available for multiple production routes based on different technologies. For instance, two chains of datasets are available for primary copper production through either pyrometallurgy or hydrometallurgy, while there are also datasets for secondary copper production from recovered copper scrap. Users of the database can, therefore, choose copper produced from a specific production route, such as primary copper produced by pyrometallurgy. Alternatively, they may select a mix of copper obtained from different primary and secondary sources, by using the dataset “market for copper, cathode.” In total, there are more than 400 datasets related to metals production producing more than 200 different products.

### <strong>S</strong><strong>ector Highlights</strong> <a href="#en-b0009" id="en-b0009"></a>

#### <strong>Mining and Quarrying Operations</strong> <a href="#en-b0010" id="en-b0010"></a>

The database contains more than eighty datasets from more than twenty geographies that model the extraction of natural resources from the ground. While some of these datasets integrate several steps of the production chain from mining to final product, others are focused on specific mining operations. Mining and quarrying activities produce more than eighty intermediate and final mineral commodities such as metal concentrates (e.g., copper, platinum group metal or rare earth oxide concentrates), refined metals (e.g., gold, silver, or cobalt), and mineral aggregates (e.g., sand, gravel, or dolomite). These commodities include base metals, precious metals (including platinum group metals), rare earth elements, and other mineral products. While some datasets are global averages, others are regionally specific (e.g., rare earth element mining mainly happens in China) and for some (e.g., copper or gold) different datasets for different geographies are available.

#### <strong>Metal Production</strong> <a href="#en-b0012" id="en-b0012"></a>

Raw commodities, such as metal concentrates, are further refined and beneficiated to final metal products. In the database, different technologies are considered. For instance, two chains of datasets are available for primary copper production through either pyrometallurgy or hydrometallurgy. Final metal products cover base metals (copper, lead nickel, zinc), several precious metals (e.g., gold, silver, platinum group metals), and rare earth element oxides.

#### <strong>Metal Working</strong> <a href="#en-b0014" id="en-b0014"></a>

To obtain semi-fabricated and final metal products, such as sheets, coils, and bars, the refined metal needs to undergo some additional processing. The ecoinvent database contains over eighty activities that model some of these steps, mainly for aluminium, iron, and steel. These activities include drilling, milling, turning, and extrusion, as well as data for generic metal working. With these datasets, it is possible to model the different steps required to produce specific metal parts.

#### <strong>Recycling and Secondary Materials</strong> <a href="#en-b0016" id="en-b0016"></a>

Metals and metal products can be recycled and used as secondary materials. In the ecoinvent database, this is represented by so-called “treatment” activities (e.g., “treatment of copper scrap by electrolytic refining”). The outputs of these activities correspond to those of primary production (e.g., “copper, cathode”) and supply the market datasets (e.g., “market for copper, cathode”). “Treatment” activities, together with activities to treat tailings and slags produced during mining and smelting, overlay the metals and [waste management sectors](waste-management-and-recycling.md).

#### Treatment of Tailings <a href="#en-b0018" id="en-b0018"></a>

Mine tailings are the main waste produced during the mining and beneficiation of metal ores and are typically deposited in tailings impoundments. In the long term, these impoundments can pose a risk to the surrounding environment, particularly in the case of tailings produced from sulfide ores. The potential environmental impacts resulting from the long-term storage of sulfidic tailings depend on a variety of factors, such as the composition of the tailings, the characteristics of the impoundment, and the climatic conditions.

To capture the range of potential environmental impacts related to tailings from metal mining, the ecoinvent database contains datasets that model the impoundment of sulfidic tailings for six different host metals (such as copper or nickel), covering in total nineteen countries, which account for the main shares of the mining of these metals. Additionally, a dataset for the impoundment of sulfidic tailings that represents an average composition is available.

### Use Cases <a href="#en-b0021" id="en-b0021"></a>

Data on metals production can be used in life cycle assessment, carbon footprint (greenhouse gas accounting), material flow analysis studies, and can support Environmental Product Declarations (EPDs) for various products and services.

### Data Providers <a href="#en-b0023" id="en-b0023"></a>

Notable providers of LCI datasets on metals activities include, but are not limited to:

- [International Aluminium Institute](https://international-aluminium.org/)
- [Association de l’aluminium du Canada](https://aluminium.ca/)
- [International Zinc Association](https://www.zinc.org/)
- [Cobalt Institute](https://www.cobaltinstitute.org/)
- [Confederation of Indian Industry](https://www.cii.in/) (CII), India
- [University of Witwatersrand, South Africa](https://www.wits.ac.za/)
- [Swiss Federal Laboratories for Materials, Science and Technology](https://www.empa.ch/) (Empa)
- [TU Graz](https://www.tugraz.at/home/)
- [University of Cape Town, UCT](https://www.uct.ac.za/)
- [Swiss Federal Institute of Technology](https://ethz.ch/en.html) (ETH)

### Editors <a href="#en-b0035" id="en-b0035"></a>

- <strong>Louis Brimacombe</strong> (Main Editor), University of Sheffield, United Kingdom
- <strong>Robert Istrate</strong>, Assistant Professor of Industrial Ecology, Leiden University
- <strong>Vanessa Schenker</strong>, Postdoctoral Researcher at the Chair of Ecological Systems Design, ETH Zurich
- <strong>Dieuwertje Schrijvers</strong>, Project Manager, WeLOOP

### Relevant Sources <a href="#en-b0040" id="en-b0040"></a>

Charikinya E., Broadhurst J., Dlamini R., Goga T., Harding K., Russo V., Viljoen D. and von Blottnitz H., (2019). <strong>Life Cycle Inventories of Primary Production of Precious and Scarce Metals – South Africa</strong>. ecoinvent Association, Zürich, Switzerland. Accessible at [SRI project results](https://sri-lci.ecoinvent.org/) (registration required).

Soni H., (2019). <strong>Life Cycle Inventories of Iron and Steel – India</strong>. ecoinvent Association, Zürich, Switzerland. Accessible at [SRI project results](https://sri-lci.ecoinvent.org/) (registration required).

Classen, M., Althaus H.-J., Blaser, S., Tuchschmid, M., Jungbluth N., Doka, G., Faist Emmenegger, M., Scharnhorst, W., (2009).<strong> Life Cycle Inventories of Metals</strong>. Final report ecoinvent data v2.1, No 10. Dübendorf: Swiss Centre for Life Cycle Inventories. Accessible in the [Reports section of version 2. of the ecoinvent database](ecoinvent-version-2.md).

{% endtab %}

{% endtabs %}
