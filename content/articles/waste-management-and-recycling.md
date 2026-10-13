# 废物管理与回收利用

英文原题：Waste Management and Recycling  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/waste-management-and-recycling)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

## 现代经济体产生的废物量持续增加；若管理不当，将对生态系统和人类健康构成严重风险。 <a href="#zh-b0002" id="zh-b0002"></a>

2024 年 1 月 30 日

历史上，废物主要通过低成本填埋处置或焚烧处理。然而，废物复杂性和数量不断增加，加之社会对环境保护的压力日益增大，使所用废物管理技术和策略日趋多样化。产品设计者在产品开发期间考虑寿命终结阶段也越来越普遍。获取高质量的废物管理环境数据，是支持全社会更好决策的必要条件。

### <strong>部</strong><strong>门概况</strong> <a href="#zh-b0005" id="zh-b0005"></a>

ecoinvent 数据库的废物管理部门包含 2,500 多个数据集，涵盖众多产生废物和废水的部门的废物及废水管理。该部门可细分为固体废物管理（SWM）和废水处理（WWT）。SWM 涵盖处理、回收利用和处置（填埋）活动，WWT 则涵盖废水处理。SWM 和 WWT 均覆盖全球五十多个国家。

废物管理部门常与其他部门交叉。例如，为回收利用而回收的废物材料重新进入工业系统进行再加工（如废钢在电弧炉中回收利用，属于冶金活动）。同样，废物管理活动（如焚烧）产生的电力和热能进入电力与供热部门。类似地，WWT 产生的污泥可进入厌氧消化、焚烧、填埋、土地耕作处理等过程。

这里需要说明，ecoinvent 数据库中的“处理活动”指任何参考产品带负号的活动。这实际上表示该活动提供处理、回收利用或处置该参考产品的服务。因此，在 ecoinvent 数据库中，所有处理、回收利用和处置活动均属于“处理活动”。

在 ecoinvent 数据库的归因型系统模型中，副产品和废物仅依据其处理需求分类。由此分为普通副产品、废物、可回收物（Cut-off），以及待处理材料（mft）和非待处理材料（non-mft）（APOS）。除普通副产品和 non-mft 外，其他副产品和废物均可能进入“处理活动”，因此本文将其统称为“废物”。

### <strong>部门亮点</strong> <a href="#zh-b0010" id="zh-b0010"></a>

#### 固体废物管理 <a href="#zh-b0011" id="zh-b0011"></a>

ecoinvent 数据库中的 SWM 包含城市固体废物、废纸、废塑料、废玻璃等多种废物数据。

所有“处理活动”遵循相同的核心建模原则：依据废物组成及随处理方式和地理区域变化的特定排放因子，对直接排入环境的排放建模。此外，这些活动纳入材料（化学品）、能源输入及基础设施，并对相关副产品（电力、热、再生金属产品）建模。

可用处理方式分为：机械处理（分选、拆解、破碎等）；热处理（城市固体废物焚烧、危险废物焚烧）；处置（填埋、地下贮存、露天焚烧、露天堆放及尾矿的陆地处置）；以及生物处理（堆肥、厌氧消化）。

回收利用数据集指金属、玻璃和塑料等再生材料的生产。回收利用通常接续处理活动产生的产品和副产品。这些数据集纳入待加工材料、过程所需材料（化学品）、能源输入和基础设施，并对可用于后续生产过程的相关副产品建模。

最后，SWM 部门包含欧洲各国、巴西、哥伦比亚、秘鲁、印度和南非针对十二种以上废物的国家特定消费组合。这些组合使用户能够对国家特定的废物管理环境负荷建模。组合根据区域内各处理过程的可用性，纳入不同处理过程。

#### 废水处理 <a href="#zh-b0017" id="zh-b0017"></a>

ecoinvent 数据库的 WWT 子部门包含三十多种不同废水处理的数据。部分废水在不同处理能力的 WWT 设施中处理；此外，还包括来自多种工业过程的不同废水，例如混凝土生产废水、玻璃生产废水、乳清厌氧消化废水和玉米淀粉生产废水。

所有废水处理活动均依据废水组成对直接排入环境的排放建模。数据集包含材料（化学品）与能源输入及基础设施，并对相关副产品（废水污泥）建模。

#### 废物工具 <a href="#zh-b0020" id="zh-b0020"></a>

用于对废物部门数据集建模的所有工具均为开放获取，任何人都可免费使用。使用者可借助这些工具创建区域特定处理方式，以及部门内尚未包含的特定废物。工具输出 spold 文件或 xls 文件。

### <strong>数</strong><strong>据提供方</strong> <a href="#zh-b0022" id="zh-b0022"></a>

废物管理活动 LCI 数据集的重要提供方包括但不限于：

- [Doka Life Cycle Assessments](https://www.doka.ch/)（Gabor Doka）
- [瑞士联邦材料科学与技术实验室](https://www.empa.ch/)（Empa）
- [瑞士联邦理工学院](https://ethz.ch/en.html)（ETH）
- [Carbotech](http://www.carbotech.ch)，德国

### 编辑 <a href="#zh-b0028" id="zh-b0028"></a>

- <strong>Anders Damgaard</strong>（共同编辑），高级研究员，丹麦 DTU Sustain 环境与资源工程系
- <strong>Ivan Muñoz Ortiz</strong>（共同编辑），2.-0 LCA Consultants，西班牙
- <strong>Patricio Rodriguez</strong>（共同编辑，矿业废物）
- <strong>Gabor Doka</strong>（主编），Doka LCA，瑞士

### 相关资料 <a href="#zh-b0033" id="zh-b0033"></a>

尽管数据库已包含理解其内容背后建模和计算所需的全部信息，下列报告仍提供更多资料，以加深对本部门活动的理解。

Doka G., (2018). [ecoinvent v3.5 中城市废物处置区域化组合的清单参数](https://www.doka.ch/publications.htm)。2018 年 12 月。Doka Life Cycle Assessments，瑞士苏黎世。

Doka G., (2017). [区域化废物处理 LCI 计算工具——一般介绍](https://www.doka.ch/publications.htm)。Doka Life Cycle Assessments，瑞士苏黎世。

Doka G., (2017). [针对特定废物和气候的露天堆场及非卫生填埋生命周期清单模型](https://www.doka.ch/publications.htm)。Doka Life Cycle Assessments，瑞士苏黎世。

Doka G., (2017). [针对特定废物的露天焚烧生命周期清单模型](https://www.doka.ch/publications.htm)。Doka Life Cycle Assessments，瑞士苏黎世。

Doka G., (2017). [针对特定废物和气候的尾矿库生命周期清单模型](https://www.doka.ch/publications.htm)。Doka Life Cycle Assessments，瑞士苏黎世。

Doka G., (2015). [城市废物焚烧及残余物填埋与 FLUWA 飞灰处理的生命周期清单](https://www.doka.ch/publications.htm)。Doka Life Cycle Assessments，瑞士苏黎世。受伯尔尼 BAFU 瑞士联邦环境署委托。

Doka G., (2013). [废物处理服务生命周期清单更新——第二部分：废物焚烧](https://www.doka.ch/publications.htm)。Doka Life Cycle Assessments，苏黎世，2013。

Doka, G., & Hischier, R., (2005). [废物处理与长期排放评价](https://link.springer.com/article/10.1065%2Flca2004.12.181.9)。International Journal of Life Cycle Assessment, 10(1), 77–84。

Doka G., (2003). [废物处理服务生命周期清单。ecoinvent 报告 No. 13](https://www.doka.ch/publications.htm)。瑞士生命周期清单中心，迪本多夫，2003。

### 应用场景 <a href="#zh-b0044" id="zh-b0044"></a>

废物管理数据可用于[生命周期评价](ecoinvent-use-cases.md)、[碳足迹（温室气体核算）](scope-2-3-greenhouse-gas-ghg-emission-reporting.md)和物质流分析研究，也可支持各种产品和服务的[环境产品声明（EPD）](environmental-product-declarations-epds.md)。

  
  

###

{% endtab %}

{% tab title="English 原文" %}

## Modern economies are producing ever-increasing volumes of wastes, which, without appropriate management, poses a serious risk to ecosystems and human health. <a href="#en-b0002" id="en-b0002"></a>

Jan 30th, 2024

Historically, wastes were predominantly dealt with through low-cost disposal in a landfill or incineration. However, the increasing complexity and volume of waste, combined with growing societal pressures on environmental protection, has seen a diversification in the range of waste management technologies and strategies being utilized. It is also becoming more common for product designers to consider the end-of-life phase during product development. Having access to good quality environmental data on waste management is essential to support better decision making across society.

### <strong>S</strong><strong>ector Overview</strong> <a href="#en-b0005" id="en-b0005"></a>

The waste management sector in the ecoinvent database comprises of more than 2,500 datasets, covering the management of wastes and wastewaters from a wide variety of sectors producing them. The sector can be subdivided into solid waste management (SWM) and wastewater treatment (WWT). SWM covers treatment, recycling, and disposal (landfilling) activities, while WWT covers the treatment of wastewater. The geographies covered for both SWM and WWT include more than fifty countries across the globe.

The waste management sector frequently overlaps with other sectors. For instance, where waste materials are recovered for recycling, they are reintroduced into industrial systems for reprocessing (e.g., recycling of steel scrap takes place in an electric arc furnace, which is a metallurgical activity). Similarly, where electrical and thermal energy is generated from waste management activities (e.g., incineration), it feeds into the electricity and heat sectors. Similarly, sludge from WWT can be introduced to anaerobic digestion, incineration, landfill, landfarming, etc.

However, it is worth mentioning here, that the term “treatment activity,” as considered in the ecoinvent database, refers to any activity that has a reference product with a negative sign. This effectively means that the activity supplies the service of treating, recycling, or disposing the reference product. So, in the ecoinvent database all treatment-, recycling-, and disposal activities are “treatment activities.”

In the ecoinvent database, by-products and wastes are classified within attributional system models, exclusively by their need for treatment. As such, they are classified as ordinary by-products, wastes, recyclables (cut-off), and materials for treatment (mft) and non-materials for treatment (non-mft) (APOS). By-products and wastes, apart from ordinary by-products and non-mft’s, can potentially enter a “treatment activity,” so within this text we refer to them as “wastes.”

### <strong>Sector Highlights</strong> <a href="#en-b0010" id="en-b0010"></a>

#### Solid Waste Management <a href="#en-b0011" id="en-b0011"></a>

SWM in the ecoinvent database is covered with data for various wastes, such as municipal solid wastes, waste papers, waste plastics, waste glass among others.

All “treatment activities” follow the same core modeling principle; they model direct emissions to the environment based on the composition of the waste, as well as specific emission factors that vary between treatment and geographies. Further, they include material (chemicals), energy inputs, infrastructure, and model relevant by-products (electricity, heat, secondary metal products).

Treatments available are divided into: mechanical (sorting, dismantling, shredding, etc.); thermal (municipal solid waste incineration, hazardous waste incineration); disposal (landfilling, underground deposit, open burning and open dumping and disposal of tailings on land) and biological (composting, anaerobic digestion).

Regarding recycling datasets, they refer to the production of secondary materials such as metals, glass and plastics. Recycling is usually following products and by-products from treatment activities. They include materials to be processed, materials necessary for the process (chemicals), energy inputs, infrastructure and model relevant by-products that can be used into further production processes.

Finally, the SWM sector includes country specific consumption mixes for more than twelve wastes for the countries of Europe, Brazil, Colombia, Peru, India, and South Africa. Those mixes offer the possibility to users to model country specific burdens that arise from waste management. The mixes include different treatment processes based on the regional availability of them.

#### Wastewater Treatment <a href="#en-b0017" id="en-b0017"></a>

The WWT sub-sector in the ecoinvent database includes data for more than thirty different wastewater treatments. There are certain wastewaters that are treated in WWT facilities with various capacity and there are also different wastewaters from various industrial processes like wastewater from concrete production, wastewater from glass production, wastewater from anaerobic digestion of whey, wastewater from maize starch production.

All wastewater treatment activities model direct emissions to the environment based on the composition of the wastewater. The datasets include material (chemicals) and energy inputs infrastructure, and model relevant by-products (wastewater sludge).

#### Waste Tools <a href="#en-b0020" id="en-b0020"></a>

All the tools used to model datasets that are part of the waste sector are open access and freely available to everyone. People can use them and create regional specific treatments in addition to creating specific wastes that are not present in the sector. The tools deliver either spold files or xls files.

### <strong>D</strong><strong>ata Providers</strong> <a href="#en-b0022" id="en-b0022"></a>

Notable providers of LCI datasets on waste management activities include, but are not limited to

- [Doka Life Cycle Assessments](https://www.doka.ch/) (Gabor Doka)
- [Swiss Federal Laboratories for Materials, Science and Technology](https://www.empa.ch/) (Empa)
- [Swiss Federal Institute of Technology](https://ethz.ch/en.html) (ETH)
- [Carbotech](http://www.carbotech.ch), Germany

### Editors <a href="#en-b0028" id="en-b0028"></a>

- <strong>Anders Damgaard</strong> (Co-Editor), Senior Researcher, Department of Environmental and Resource Engineering, DTU Sustain, Denmark
- <strong>Ivan Muñoz Ortiz</strong> (Co-Editor), 2.-0 LCA Consultants, Spain
- <strong>Patricio Rodriguez</strong> (Co-Editor, mining wastes)
- <strong>Gabor Doka</strong> (Main Editor), Doka LCA, Switzerland

### Relevant Sources <a href="#en-b0033" id="en-b0033"></a>

While the database contains all needed information to understand the modeling and calculations behind its contents, the reports below provide further information for enhanced understanding of the activities within the sector.

Doka G., (2018). [Inventory parameters for regionalised mixes of municipal waste disposal in ecoinvent v3.5](https://www.doka.ch/publications.htm). December 2018. Doka Life Cycle Assessments, Zurich, Switzerland.

Doka G., (2017). [LCI calculation tools for regionalised waste treatment – General introduction](https://www.doka.ch/publications.htm). Doka Life Cycle Assessments, Zurich, Switzerland.

Doka G., (2017). [A model for waste-specific and climate-specific life cycle inventories of open dumps and unsanitary landfilling of waste](https://www.doka.ch/publications.htm). Doka Life Cycle Assessments, Zurich, Switzerland.

Doka G., (2017). [A model for waste-specific life cycle inventories of open burning of waste](https://www.doka.ch/publications.htm). Doka Life Cycle Assessments, Zurich, Switzerland.

Doka G., (2017). [A model for waste-specific and climate-specific life cycle inventories of tailings impoundments](https://www.doka.ch/publications.htm). Doka Life Cycle Assessments, Zurich, Switzerland.

Doka G., (2015). [Life cycle inventories of municipal waste incineration with residual landfill & FLUWA filter ash treatment](https://www.doka.ch/publications.htm). Doka Life Cycle Assessments, Zurich, Switzerland. Commissioned by BAFU Bundesamt für Umwelt, Berne.

Doka G., (2013). [Updates to Life Cycle Inventories of Waste Treatment Services – part II: waste incineration](https://www.doka.ch/publications.htm). Doka Life Cycle Assessments, Zurich, 2013.

Doka, G., & Hischier, R., (2005). [Waste treatment and assessment of long-term emissions](https://link.springer.com/article/10.1065%2Flca2004.12.181.9). International Journal of Life Cycle Assessment, 10(1), 77–84.

Doka G., (2003). [Life Cycle Inventories of Waste Treatment Services. ecoinvent report No. 13](https://www.doka.ch/publications.htm). Swiss Centre for Life Cycle Inventories, Dübendorf, 2003.

### Use Cases <a href="#en-b0044" id="en-b0044"></a>

Data on waste management can be used in [life cycle assessment](ecoinvent-use-cases.md), [carbon footprint (greenhouse gas accounting)](scope-2-3-greenhouse-gas-ghg-emission-reporting.md) and material flow analysis studies and can support [Environmental Product Declarations (EPDs)](environmental-product-declarations-epds.md) for various products and services.

  
  

###

{% endtab %}

{% endtabs %}
