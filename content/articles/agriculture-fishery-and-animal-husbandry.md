# 农业、渔业与畜牧业

英文原题：Agriculture, Fishery and Animal Husbandry  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/agriculture-fishery-and-animal-husbandry)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 农业、渔业与畜牧业所涵盖的人类活动显著依赖自然资本、经济资本和社会资本。 <a href="#zh-b0002" id="zh-b0002"></a>

2023 年 9 月 24 日

由于土地、水和劳动力等特定投入与资源的密集使用，该部门对自然资源和化石资源的耗竭有较大贡献。根据 IPCC 关于气候变化、荒漠化、土地退化、可持续土地管理、粮食安全和陆地生态系统温室气体通量的[特别报告](https://www.ipcc.ch/site/assets/uploads/2019/08/4.-SPM_Approved_Microsite_FINAL.pdf)，农业约占全部人为温室气体排放的 23%；其中，根据[粮农组织《通过畜牧业应对气候变化》报告](https://www.fao.org/3/i3437e/i3437e.pdf)，畜牧生产约占其 14.5%。

ecoinvent 数据库中，该部门包括多年生作物种植（如苹果、柑橘）；非多年生作物种植（如干草、牧草、谷物、豆类等）；作物油脂生产（如大豆油）；农业配套活动（如耕作、灌溉、喷洒）；农业副产品回收利用（如养分供应）；动物生产（如牛、猪）；作物加工活动（如制糖）；作物配套活动（如干燥、分选）；以及动物饲料生产。

覆盖的地理区域包括四十多个国家及多个国家内部的地区。主要生产国和／或地区包括巴西（BR）、印度（IN）、瑞士（CH）、南非（ZA）、加拿大（CA）、欧洲（RER）、美国（US）、澳大利亚（AU）、中国（CN）、秘鲁（PE）、厄瓜多尔（EC）等。

数据库还包含一些几乎专用于农业、但未归入该部门的数据集。肥料和农药生产数据集纳入[化学品与塑料部门](chemicals-and-plastics.md)。此外，用于纺织的作物生产涵盖于[纺织部门](textiles.md)。所有灌溉相关数据集均纳入[供水部门](water-supply.md)。

### <strong>部门亮点</strong> <a href="#zh-b0008" id="zh-b0008"></a>

#### <strong>作物生产</strong> <a href="#zh-b0009" id="zh-b0009"></a>

ecoinvent 数据库的农业部门包含多种多年生和非多年生作物的数据，既包括粮食作物，也包括纺织业和畜牧业所用的非粮食作物。有数据可用的作物包括棉花、苹果、番茄、小麦、玉米、大豆、可可、咖啡等。此外，数据还区分不同生产过程，包括投入水平不同（如耕作、灌溉等）的露地、温室和有机作物生产。作物生产数据集覆盖 5 大洲的 40 多个地理区域。

在排放及排放模型方面，所有作物生产相关数据集均遵循统一的建模方法。重金属排放采用 Agroscope 开发的 SALCA 方法计算。该方法依据作物生产期间的投入（肥料、农药等）以及作物吸收量，考虑镉、铜、锌、铅、镍、铬和汞向土壤及水体的排放。作物生产期间施肥导致的 CO2 大气排放采用 IPCC 排放因子计算，并假定肥料中的全部碳均以二氧化碳形式排放。关于农药、肥料及其他投入相关排放的补充建模说明见以下报告：

![doc-icon](../assets/024d8f149226-doc-icon.png) 下载 [ecoinvent 作物生产 LCI 计算工具报告](../assets/e270067e0ba3-Ecoinvent_Tool_Model_Description_20180130.pdf)

该部门依据经 Blonk consultants 和 Quantis intl. 调整的 PAS2050-1/ENVIFOOD 协议，对土地利用变化（LUC）进行建模。该方法利用土地利用统计和碳清单，恰当地处理 LUC 建模。该方法的详细说明见：

[![doc-icon](../assets/024d8f149226-doc-icon.png)](../assets/cc35352d4593-change_report_v3_3_final.pdf) 下载 [ecoinvent 第 3.3 版中对土地利用变化的考虑.pdf](../assets/c2b709cb8f7f-ConsiderationOfLandUseChange_ecoinventDatabase.pdf)

上述模型在农业生命周期清单（LCI）中一致应用，除非数据提供方能够提供更精确的建模方法。若采用了不同模型，相关信息可在对应数据集的元数据中获取。

#### 畜牧业 <a href="#zh-b0016" id="zh-b0016"></a>

ecoinvent 数据库的农业部门包含多种养殖肉类产品的信息，例如牛、鸡和猪。所包含的数据集涵盖动物饲养（BR、ZA 和 CA）、粪便管理及相关基础设施。数据集体现不同生产技术，例如使用或不使用饲料的牧场牛肉生产。此外，该部门还对断奶母犊牛、断奶犊牛等多种产品和副产品进行建模。

#### 渔业 <a href="#zh-b0018" id="zh-b0018"></a>

渔业部门于 ecoinvent v3.5 发布时引入数据库，其中包括在 SRI 项目框架下开发的数据。该部门包含 200 多个数据集，覆盖多种鱼类，以及捕捞和水产养殖这两种鱼类生产方式。

该部门涵盖一些消费最广泛的鱼类和鱼产品，以及特殊海产品（如鱼条）。此外，该部门包含不同鱼类捕捞和养殖过程的数据，以及生产供人食用的鱼罐头，以及鱼粉和鱼油的鱼类加工数据。

具体而言，该部门涵盖野生捕捞（PE、EC、ES、NA）和鱼类养殖过程（PE 和 RLA），并包含金枪鱼、无须鳕、鳀鱼、巴塔哥尼亚长尾鳕、小型中上层鱼类、罗非鱼和鳟鱼的价值链数据。此外，还体现拖网渔船、延绳钓渔船和围网渔船等不同技术。

野生捕捞数据集包含过程所用燃料及渔业活动的全部相关基础设施。此外，数据集恰当地记录了从环境中提取自然资源的情况（主要捕获鱼类及兼捕鱼类）。同时，该部门包含水产养殖信息，具体涵盖鱼饲料生产、基础设施及过程中使用的燃料。

#### 肥料与养分供应 <a href="#zh-b0023" id="zh-b0023"></a>

数据库的农业部门包含所有类型肥料（有机肥、无机肥、有机无机复混肥）的生产信息，并对其作出明确区分。

用户可在不同地理区域、不同层级上对肥料建模：工厂大门层级（urea）；产品市场层级（market for urea）；养分供应层级（nutrient N delivery from urea）；以及最终可能含有尿素的综合氮肥层级。各层级建立在前一层级的基础上，用户也可选择独立使用这些层级。该建模方式的更多信息见 ecoinvent 3.7 变更报告。

最后，该部门包含 30 多个国家特定的肥料消费组合（第 4 层级）。这些组合由最常用的肥料构成，提供汇总的养分物质。

矿物肥料制造记录于化学品部门。它涵盖主要活性物质：氨、尿素、硝酸铵、硫酸铵、硝酸钙、硝酸钾、硝酸磷铵、硝酸铵钙、磷酸一铵和磷酸二铵、磷酸、氮磷钾复合肥（NPK）及过磷酸盐肥料。

#### 农业及加工服务与基础设施 <a href="#zh-b0028" id="zh-b0028"></a>

该部门提供许多数据集，对使用重型设备的农业服务（如耕作、播种、收获、施肥、田间喷洒等）进行建模。这些数据集以过程中使用的柴油消耗量为基础，使用户能够调整数据并对特定情景建模。该部门的一部分也包含上述过程中所用设备的生产。此外，该部门还包含食品加工，相关数据集涉及干燥（谷物和咖啡）、分选（水果），以及鱼产品的罐装、冷冻和腌制。这些数据集纳入过程中使用的基础设施、能源消耗及相关废物的产生。

#### <strong>土地利用变化（LUC）</strong> <a href="#zh-b0030" id="zh-b0030"></a>

该部门依据 PAS2050-1/ENVIFOOD 协议对土地利用变化（LUC）进行建模。该方法利用土地利用统计和碳清单，恰当地处理 LUC 建模。该方法的详细说明见：

[![doc-icon](../assets/024d8f149226-doc-icon.png)](../assets/cc35352d4593-change_report_v3_3_final.pdf) 下载 [ecoinvent 第 3.3 版中对土地利用变化的考虑.pdf](../assets/c2b709cb8f7f-ConsiderationOfLandUseChange_ecoinventDatabase.pdf)

### <strong>数据提供方</strong> <a href="#zh-b0033" id="zh-b0033"></a>

ecoinvent 数据来自不同来源。农业、渔业与畜牧业部门的重要 LCI 数据集提供方包括（但不限于）：

- [Agroscope](https://www.nccs.admin.ch/nccs/en/home/the-nccs/about-the-nccs/organisation/members-and-partners/agroscope.html)，瑞士
- [EarthShift Global](https://www.earthshiftglobal.com/)，美国
- [ecoinvent 协会](https://www.ecoinvent.org)，瑞士
- [Embrapa](https://www.embrapa.br/en/international)，巴西
- [产品、服务与系统生命周期国际参考中心](https://ciraig.org/)（CIRAIG），加拿大
- [Lifecycles](https://www.lifecycles.com.au/)，澳大利亚
- [Quantis](https://quantis-intl.com/)，瑞士
- [瑞士联邦理工学院](https://ethz.ch/en.html)（ETH），瑞士
- [不列颠哥伦比亚大学](https://www.ubc.ca/)，加拿大
- [苏黎世应用科学大学](https://www.zhaw.ch/en/university/)（ZHAW），瑞士

### 编辑 <a href="#zh-b0045" id="zh-b0045"></a>

- <strong>Thomas Nemecek </strong>（主编），Agroscope，瑞士
- <strong>Assumpció Antón </strong>（共同编辑），IRTA（Institut de Reserca i Technologica Agroalimentaries），西班牙
- <strong>Jens Lansche </strong>（共同编辑）<strong>，</strong>Agroscope，瑞士
- <strong>Jürgen Reinhard</strong>（土地利用变化（LUC）主编），Quantis，瑞士
- <strong>Friederike Ziegler</strong> 和 <strong>Kristina Bergman </strong>（渔业主编），RISE 瑞典研究院

### <strong>相</strong><strong>关资料</strong> <a href="#zh-b0051" id="zh-b0051"></a>

Avadí, A., Vázquez-Rowe, I., (2019). <strong>Life Cycle Inventories of Wild Capture and Aquaculture（野生捕捞与水产养殖生命周期清单）</strong>，ecoinvent 协会，瑞士苏黎世。可在 [SRI 项目成果](https://sri-lci.ecoinvent.org/)中获取（需注册）。

{% endtab %}

{% tab title="English 原文" %}

## The Agriculture, Fishery, and Animal Husbandry sector represents a sphere of human activities characterized by a pronounced reliance on natural, economic, and social capitals. <a href="#en-b0002" id="en-b0002"></a>

Sept 24th, 2023

Due to the intensive use of specific inputs and resources such as land, water, and labor, this sector bears a substantive contribution to the depletion of both natural and fossil resources. Indeed, according to IPCC’s  [Special Report on Climate Change,](https://www.ipcc.ch/site/assets/uploads/2019/08/4.-SPM_Approved_Microsite_FINAL.pdf) Desertification, Land Degradation, Sustainable Land Management, Food Security, and Greenhouse Gas fluxes in Terrestrial Ecosystems, agriculture is responsible for approximately 23% of all human-induced greenhouse gas emissions, within, based on [FAO Report Tackling Climate Change Through Livestock](https://www.fao.org/3/i3437e/i3437e.pdf), livestock production accounts for circa 14.5% of them.

In the ecoinvent database, the sector includes, growing of perennial crops (e.g. apples, mandarins); growing of non-perennial crops (e.g. hay, grass, cereals, legumes etc.); production of oils from crops (e.g. soybean oil); supporting agricultural activities (e.g. tillage, irrigation, sprayer); recycling of agricultural by-products (e.g. nutrient supplies); animal production (e.g. cattle, swine); crop processing activities (e.g. sugar production); crop supporting activities (e.g. drying, sorting); production of animal feeds.

Geographies covered include more than forty countries and several regions within countries. Major producer countries and/or regions include Brazil (BR), India (IN), Switzerland, (CH), South Africa (ZA), Canada (CA), Europe (RER), United States (US), Australia (AU), China (CN), Peru (PE), Ecuador (EC), and many more.

The database also includes additional datasets that are used almost exclusively for agriculture but are not considered part of the sector. Datasets on fertilisers and pesticides production are included in the [Chemicals and Plastics sector](chemicals-and-plastics.md). Furthermore, crop production for crops meant to be used for textiles is covered in the [Textiles sector](textiles.md). All datasets related to irrigation are included in the [Water Supply sector](water-supply.md).

### <strong>Sector Highlights</strong> <a href="#en-b0008" id="en-b0008"></a>

#### <strong>Crop Production</strong> <a href="#en-b0009" id="en-b0009"></a>

The agriculture sector in the ecoinvent database includes data for several perennial and non-perennial crops, including food crops and non-food crops used in the textiles and animal farming industries. Crop examples, for which data are available, include cotton, apples, tomatoes, wheat, maize, soybean, cocoa, coffee etc. Additionally, data according to various production processes are presented, including open field-, greenhouse-, and organic crop production with different levels of inputs (e.g. tillage, irrigation etc.). Geographical coverage of the crop production datasets spans in more than 40 geographies across 5 continents.

Regarding emissions and emissions’ models, all crop production-related datasets are modeled following a homogeneous modeling approach. The calculation of heavy metal emissions is based on the SALCA method developed by Agroscope. The method considers cadmium, copper, zinc, lead, nickel, chromium and mercury emissions to soil and water, based on inputs during the crop production (fertilisers, pesticides etc.) as well as crop uptake. Calculation of air emissions of CO2 resulting from fertiliser application during crop production, is based on emission factors from IPCC, considering all carbon in the fertiliser emitted as carbon dioxide. Additional modeling for pesticide fertilizer and other input-related emissions is described in this report:

![doc-icon](../assets/024d8f149226-doc-icon.png)  Download [ecoinvent LCI Calculation tool for crop production report](../assets/e270067e0ba3-Ecoinvent_Tool_Model_Description_20180130.pdf)

The sector models the Land Use Change (LUC) according to the PAS2050-1/ENVIFOOD protocol, adapted by Blonk consultants and Quantis intl.. The methodology employs land use statistics and carbon inventories to properly address the modeling of LUC. The methodology is documented in detail here:

[![doc-icon](../assets/024d8f149226-doc-icon.png)](../assets/cc35352d4593-change_report_v3_3_final.pdf)  Download [Consideration of land use change in ecoinvent version 3.3.pdf](../assets/c2b709cb8f7f-ConsiderationOfLandUseChange_ecoinventDatabase.pdf)

The above-mentioned models are consistently applied in Agriculture Life Cycle Inventories (LCIs) unless the data providers are able to provide more precise modeling approaches. Where different models are adopted, the information is available in the metadata of the relevant datasets.

#### Animal Husbandry <a href="#en-b0016" id="en-b0016"></a>

Information about various farmed meat products are included in the agriculture sector of the ecoinvent database. Such products include cattle, chicken, swine. Datasets included cover raising of the animals (BR, ZA and CA), manure management, and relevant infrastructure. Different production technologies are represented, such as beef production on pasture with or without feed use. Further, the sector models various products and by-products, such as weaned heifers and weaned calves.

#### Fisheries <a href="#en-b0018" id="en-b0018"></a>

Including data developed within the framework of the SRI project, the Fisheries sector was introduced in the database with the release of ecoinvent v3.5. It comprises over 200 datasets, covering a wide range of fishes as well as both types of fish production, fish catching and aquaculture.

The sector covers some of the most consumed fish and fish products, as well as special seafood products (e.g. fish sticks). Further, the sector includes data on different processes of fish capture and fish farming, as well as data on fish processing to produce canned fish products meant for human consumption, fish meal and fish oil.

Specifically, the sector covers wild capture (PE, EC, ES, NA) and fish farms processes (PE and RLA), and includes data for the value chains of tuna, hake, anchovy, Patagonian grenadier, and small pelagic fish, tilapia and trout. Further, various technologies are represented, such as trawlers, long liners, and purse seiners.

The wild capture datasets include the fuels used in the process and all relevant infrastructure for the fishing activities. Further, the datasets properly capture the extraction of natural resources (fish main catch and by-catch) from the environment. At the same time, the sector includes information on aquafarming, specifically covering the production of fish feed, infrastructure and fuels used in the process.

#### Fertilisers and Nutrient Supplies <a href="#en-b0023" id="en-b0023"></a>

The Agriculture sector of the database accommodates information about the production of all types of fertilisers (organic, inorganic, organo-mineral) with a clear distinction between them.

Users can choose to model fertilisers in different geographies and at different levels: the gate factory level (urea); market for the product (market for urea); nutrient supply (nutrient N delivery from urea); and, finally, the aggregate N fertiliser that can contain urea. Each level builds on the previous while users can also choose to employ them independently. More information regarding this modeling is available in ecoinvent 3.7 report of changes.

Finally, the sector includes country specific fertiliser consumption mixes (level 4) for more than 30 countries. They comprise of the most used fertilisers that deliver the aggregated nutrient substance.

The manufacturing of mineral fertilisers is documented under the Chemicals sector. It covers the main active substances: ammonia, urea, ammonium nitrate, ammonium sulfate, calcium nitrate, potassium nitrate, ammonium nitrate phosphate, calcium ammonium nitrate, mono and di – ammonium phosphate, phosphoric acid, NPKs and superphosphates.

#### Agricultural and Processing Services and Infrastructure <a href="#en-b0028" id="en-b0028"></a>

The sector offers many datasets that model agricultural services (i.e.: tillage, sowing, harvesting, fertilising, field spraying and more) using heavy equipment. These datasets rely on the diesel consumption used for the process, effectively allowing users to make adjustments and model specific cases. Part of the sector also includes the production of the equipment used in the aforementioned processes. Further, the sector includes processing of food with various datasets such as drying (grains and coffee), sorting (fruits), canning, freezing and curing of fish products. Those datasets include the infrastructure employed in the process, energy consumption and production of relevant wastes.

#### <strong>Land Use Change (LUC)</strong> <a href="#en-b0030" id="en-b0030"></a>

The sector models the Land Use Change (LUC) according to the PAS2050-1/ENVIFOOD protocol. The methodology employs land use statistics and carbon inventories to properly address the modeling of LUC. The methodology is documented in detail here:

[![doc-icon](../assets/024d8f149226-doc-icon.png)](../assets/cc35352d4593-change_report_v3_3_final.pdf)  Download [Consideration of land use change in ecoinvent version 3.3.pdf](../assets/c2b709cb8f7f-ConsiderationOfLandUseChange_ecoinventDatabase.pdf)

### <strong>Data Providers</strong> <a href="#en-b0033" id="en-b0033"></a>

ecoinvent data originates from different sources. Notable providers of LCI datasets for the Agriculture, Fishery & Animal Husbandry sector include (but are not limited to):

- [Agroscope](https://www.nccs.admin.ch/nccs/en/home/the-nccs/about-the-nccs/organisation/members-and-partners/agroscope.html), Switzerland
- [EarthShift Global](https://www.earthshiftglobal.com/), United States
- [ecoinvent association](https://www.ecoinvent.org), Switzerland
- [Embrapa](https://www.embrapa.br/en/international), Brazil
- [International Reference Center for Life Cycle of Products, Services and Systems](https://ciraig.org/) (CIRAIG), Canada
- [Lifecycles](https://www.lifecycles.com.au/), Australia
- [Quantis](https://quantis-intl.com/), Switzerland
- [Swiss Federal Institute of Technology](https://ethz.ch/en.html) (ETH), Switzerland
- [University of British Columbia](https://www.ubc.ca/), Canada
- [Zürcher Hochschule für Angewandte Wissenschaften](https://www.zhaw.ch/en/university/) (ZHAW), Switzerland

### Editors <a href="#en-b0045" id="en-b0045"></a>

- <strong>Thomas Nemecek </strong>(Main Editor), Agroscope, Switzerland
- <strong>Assumpció Antón </strong>(Co-Editor), IRTA (Institut de Reserca i Technologica Agroalimentaries), Spain
- <strong>Jens Lansche </strong>(Co-Editor)<strong>, </strong>Agroscope, Switzerland
- <strong>Jürgen Reinhard</strong> (Main Editor for Land Use Change (LUC)), Quantis Switzerland
- <strong>Friederike Ziegler</strong> and <strong>Kristina Bergman </strong>(Main Editors for Fisheries ), RISE, Research Institute of Sweden

### <strong>R</strong><strong>elevant Sources</strong> <a href="#en-b0051" id="en-b0051"></a>

Avadí, A., Vázquez-Rowe, I., (2019). <strong>Life Cycle Inventories of Wild Capture and Aquaculture</strong>, ecoinvent association, Zürich, Switzerland. Accessible at [SRI project results](https://sri-lci.ecoinvent.org/) (registration required).

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0004**：原文将农业比例与畜牧业比例串联，并使用 of them，分母指代可能误导；所引两个报告的统计口径需核实，不能据此推算 23%×14.5%。 请专家核实原文引用的统计范围与分母；当前译文忠实保留原文关系。 [查看完整记录](../review/issues.md#issue-003)
- **已处理／已说明 · b0020**：原译文中“供人食用”可能同时限定鱼粉和鱼油，扩大了原文限定范围。 已以“以及”分开，明确仅鱼罐头带该限定。 [查看完整记录](../review/issues.md#issue-004)
