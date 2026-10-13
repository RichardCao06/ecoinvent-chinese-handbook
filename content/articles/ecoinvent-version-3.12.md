# ecoinvent 第 3.12 版

英文原题：ecoinvent Version 3.12  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.12)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-05-18

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库第 3.12 版继续扩充各行业的数据内容和地理覆盖。本次更新体现了我们持续致力于提供透明、全面环境数据的承诺。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.12 于 2025 年 11 月 5 日发布</strong>。了解如何[升级到我们的最新版本](licensing.md)。

2026 年 2 月 19 日

第 3.12 版对以下行业进行了新更新：化学品与塑料、燃料、金属、电力、林业与木材、纺织品、农业、运输、纸浆与纸，以及电池与电子。

[![webinar-icon](../assets/9c37f83e3b0d-webinar-icon.png)](https://youtu.be/t4p2foRfwAQ)  [观看“ecoinvent 第 3.12 版介绍”网络研讨会](https://share.hsforms.com/1oDkuJ0wkSBW9RH34nh_qrAbutpu)






![doc-icon](../assets/024d8f149226-doc-icon.png) [我们对 v3.12 问答环节问题的解答](../assets/642c4b5fa69a-ecoinvent-Introduction-to-version-3.12-Webinar-Q-A.pdf)

[![doc-icon](../assets/024d8f149226-doc-icon.png)](../assets/82c7659626d9-Webinar-introduction-to-ecoinvent-v3.11.pdf)  [下载涵盖 v3.12 全部更新的概览演示文稿](../assets/95000f85e0bd-Introduction-to-ecoinvent-v3.12.pdf)



### <strong>行业更新</strong> <a href="#zh-b0009" id="zh-b0009"></a>

#### <strong>农业、渔业与畜牧业</strong> <a href="#zh-b0010" id="zh-b0010"></a>

本年度，[农业、渔业与畜牧业部门](agriculture-fishery-and-animal-husbandry.md)聚焦通过技术修正进行多项改进，以提高农业数据质量。若干作物数据集的干质量、湿质量中的水质量和含水率参数已调整。为增强作物数据集元数据的一致性，产量信息已添加至一般注释或移至其中。主要向空气和水的排放已按数据提供者的建模方法统一并修正。最后，部分 RER 或 GLO 市场组成已更新。

#### <strong>电池</strong> <a href="#zh-b0012" id="zh-b0012"></a>

通过一系列技术修正及引入新的化学组分，[电池行业](batteries-electronics.md)得到进一步完善。在改进替代数据后，多个阴极和阳极数据集进行了统一，包括将聚氟乙烯替换为聚偏二氟乙烯、将乳胶替换为丁苯橡胶等中间交换调整。

若干 NMC 和 NCA 化学体系的交换属性和文档已更新，以提高化学准确性和透明度。其他改进包括明确制造废料、依据近期来源更新能源投入，以及在氢氧化物和氧化物前驱体文档中加入化学式。

最后，数据库新增若干与电池应用相关的化合物，扩大了阴极、阳极和电解液替代配方所用材料的覆盖范围。

#### <strong>化学品与塑料</strong> <a href="#zh-b0016" id="zh-b0016"></a>

ecoinvent v3.12 的[化学品与塑料行业](chemicals-and-plastics.md)已更新，显著改善以下物质的区域覆盖：（1）乙烯、丙烯及其均聚物（LDPE、LLDPE、HDPE 和聚丙烯）；（2）氯乙烯单体及其聚合物（乳液聚合和溶液聚合 PVC）；（3）丙烯酸；（4）环氧乙烷；（5）甲醇；（6）工业气体（氮气和氧气）等。这一针对性供应链改进增强了对多种化学品和塑料衍生物的表示，并延续此前版本已实现的区域扩展。

此外，ecoinvent v3.12 将此前版本中氰化氢、聚苯乙烯（通用型、高抗冲型和可发型）及聚丁二烯的汇总数据，替换为拆分后的单元过程，以便与 ecoinvent 背景数据准确链接。为配合这一拆分，新增和更新了苯乙烯单体生产数据，并相应更新了通过 PO/SM 工艺生产环氧丙烷的数据，涵盖新技术和更多区域。

此外，v3.12 引入由全球主要溴及溴基产品生产商[ICL Group](https://www.icl-group.com/)提供的以色列溴供应行业新数据。内部评价作为这一合作的补充，还覆盖了其他主要地区的溴生产。ecoinvent v3.12 另包含[工业技术中心 IPC](https://www.ct-ipc.com/)提供的关键聚合物加工服务新数据，即吹塑薄膜挤出（多种配置）和塑料袋制造，以扩大该领域的数据覆盖。

最后，ecoinvent v3.12 延续此前版本扩充产品组合的工作，纳入四十种此前未覆盖、具有不同用途的新产品。此外，针对关键有机产品组引入六个新通用数据集，涵盖基础前驱体、醇类、芳香族化合物、羧酸、酯类和未指定有机物，以替代原有且更笼统的“chemical, organic”流。未来发布将继续扩充特定化学品和塑料的产品覆盖，以及按官能团分类的通用数据集。

#### <strong>电力</strong> <a href="#zh-b0021" id="zh-b0021"></a>

ecoinvent 第 3.12 版采用第 3.6 至 3.11 版一贯使用的方法，更新[能源行业](energy.md)的电力市场数据集。与 v3.11 一致，[Enerdata](https://global-energy-data.enerdata.net/)是大多数地区发电的主要数据来源；例外包括能够获得详细国家数据的地区，以及采用欧盟委员会[Eurostat](https://ec.europa.eu/eurostat/databrowser/view/nrg_bal_peh__custom_14425791/default/table?lang=en)数据库的欧盟（EU）成员国。电力市场组合通常代表 2022 年，但 巴西（BR）、加拿大（CA）、中国（CN）、印度（IN）、瑞士（CH）和美国（U.S.）根据全面的国家统计更新至 2023 年。印度更新对应 2022 年 4 月至 2023 年 3 月的财政年度。此外，第 3.12 版欧洲剩余电力组合市场使用[AIB](https://www.aib-net.org/facts/european-residual-mix)统计数据，代表 2024 年。

此外，还进行了其他小幅修正和统一工作，以更新电力市场、变压和进口数据集的文档及元信息。

#### <strong>林业与木材</strong> <a href="#zh-b0024" id="zh-b0024"></a>

ecoinvent 第 3.12 版对[林业与木材行业](forestry-and-wood.md)进行了数据更新和改进。新增芬兰林业数据扩大了行业地理覆盖。数据由[芬兰森林工业联合会](https://metsateollisuus.fi/en/home/)提供，该项目与[芬兰自然资源研究所（Luke）](https://www.luke.fi/en)紧密合作完成。新增三个林业数据集：松树、云杉和桦树。这些数据集表示轮伐林业，合计覆盖芬兰年采伐面积的 97%。

此外，全行业的产品命名规范进行了统一。更新旨在消除物理产品特征与计量基准之间的混淆，二者并不总是相同。新命名规范更清楚地说明每种初级林产品的四项关键属性：实际是否含树皮（带皮或去皮）、实际含水状态（生材/干材）、在含树皮时树皮相关的计量基准（去皮计量/带皮计量），以及水分相关的计量基准（生材/干材）。

#### <strong>燃料</strong> <a href="#zh-b0027" id="zh-b0027"></a>

ecoinvent 新版本 3.12 的[燃料行业](fuels.md)更新，以第 3.9.1 版（2022 年）、第 3.10 版（2023 年）的石油与天然气全面修订，以及 v3.11（2024 年）天然气和石油供应组合新增/更新为基础。v3.12 更新了原油和天然气开采或生产数据，参考年为 2023 年，地理覆盖包括 40 个国家的陆上生产和 36 个国家的海上生产。此外，第 3.12 版对天然气液体生产和分馏数据集进行区域化，新增 18 个地理区域，覆盖全球天然气液体生产及后续分馏的 95%。本最新版本还新增五个氦生产地理区域，总计覆盖全球氦产量的 96%。

#### <strong>金属</strong> <a href="#zh-b0029" id="zh-b0029"></a>

在[金属行业](metals.md)中，钢、铝和锌合金生产的全面改进，填补了专门材料建模的重要缺口。

钢铁行业新增七个特定钢合金数据集，采用 100% 废钢投入的电弧炉（EAF）生产，分别对轴承钢、碳钢、渗碳钢、高强度低合金钢、结构钢和耐候钢建模。在材料选择对性能及可持续发展结果至关重要的行业中，这些数据集支持更准确的环境评价。

铝生产链采用[国际铝业协会](https://international-aluminium.org/)2019 年数据全面更新，涵盖从铝土矿开采到铸锭的完整价值链。此次更新包括改善地理覆盖、更新铝工业电力消费模式，以及通过完善市场组成数据，更好地表示进出口流。

与[国际锌业协会](https://www.zinc.org/)共同开发的欧洲 Zamak 锌合金生产新数据集，为这种广泛使用、主要由再生锌制造的合金提供详细清单。该数据集代表欧洲 Zamak 产量的约 76%，支持汽车零部件和消费品的环境足迹建模。

其他改进包括修正各种金属加工数据集，例如更新金属加工工厂能源投入、修正氧化锌生产交换以及完善钢铁生产文档。这些改进共同增强金属行业数据的技术严谨性和对生命周期评价从业人员的适用性。

#### <strong>纺织品</strong> <a href="#zh-b0035" id="zh-b0035"></a>

ecoinvent 数据库 v3.12 基于法国大麻生产者及加工者的一手数据，新增大麻数据集，扩充[纺织行业](textiles.md)。法国在欧洲（60%）及全球（50%）大麻纤维生产中占主导地位。建模数据代表法国全国生产的 98% 以上。新增拆分后的单元过程，包括大麻作物农业种植、大麻茎剥皮和纤维棉型化（将纤维切至适合纺纱的 40-50mm 长度）。项目合作伙伴[InterChanvre](https://www.interchanvre.org/interchanvre)提供了这些数据。

此外，现有欧洲亚麻数据通过在打麻过程中引入新的有价值副产品而更新，并进行了其他小幅修正以改善文档。欧洲亚麻数据集的修改与原项目合作伙伴[欧洲亚麻与大麻联盟](https://allianceflaxlinenhemp.eu/en)合作完成。其他修正包括对现有棉和聚酯数据集的多项小幅更新，以消除已发现的错误和不一致。多个纺织活动和产品的 ISIC 与 CPC 分类代码也已统一。

#### <strong>运输</strong> <a href="#zh-b0038" id="zh-b0038"></a>

v3.12 的[运输行业](transport.md)对五种运输方式中的三种——铁路、公路和海运——进行了更新与修正。主要目标是依据新获得的信息或发现的错误，开展针对性改进以提高行业数据质量。最小的更新是在有轨电车轨道和铁路中增加废物及废物处理；公路运输则修正了乘用车和货车制动磨损数量的错误。海运改进最多，纳入重质燃油（HFO）的新排放限值，以及最新[国际海事组织温室气体报告](https://www.imo.org/en/ourwork/environment/pages/fourth-imo-greenhouse-gas-study-2020.aspx)所载的船队组成。更新涵盖船舶生产、维护和使用。

#### <strong>废物管理与回收利用</strong> <a href="#zh-b0040" id="zh-b0040"></a>

第 3.12 版[废物管理与回收利用行业](waste-management-and-recycling.md)的更新主要是继第 3.9–3.11 版大量新增数据集之后的小幅修正与更新。这些修正基于内部和外部反馈，例如用户指出的小错误或更合理的假设。这些改进为用户提供更有代表性、更一致的清单。

用户指出，进入残余物填埋场的电弧炉炉渣产生了大量六价铬排放，导致 LCIA 毒性值较高。依据该特定炉渣的较新测量结果（[BAFU 与 Carbotech，2021 年](https://www.bafu.admin.ch/dam/bafu/en/dokumente/wirtschaft-konsum/externe-studien-berichte/life-cycle-inventories-of-steel-and-iron-processes.pdf.download.pdf/Life_Cycle_Inventories_of_Steel_and_Iron_Processes_2021.pdf)），模型降低了铬以六价铬形式浸出的可释放比例，因为铬更多以较稳定的三价铬形式结合。此次更新使废物和金属行业用户在生态毒性和人体毒性类别中得到较低影响得分。

通过统一处理活动及其相应市场的 ISIC 分类，改善了内部一致性，并向此前遗漏 EN15804 废物清单指标的数据集添加这些指标。其实施仍在与不同利益相关方协调，但当前在整个数据库中的纳入已保持一致。

v3.11 欧洲塑料回收大型项目使可回收聚合物可供其他数据集采用。经过全面评价和实施，产生塑料废物的特定欧洲数据集会将部分或全部废聚合物送至这些回收设施。其他修正包括纠正污泥土地施用中的碳矿化、塑料回收挥发性有机化合物（VOC）排放以及运输消耗的错误。纺织生产废水直接处置重新加入此前采用这一方式的地理区域（IN 和 BD）。元文档中的拼写错误和对错误活动的引用也已修正。

#### <strong>LCIA 方法更新</strong> <a href="#zh-b0045" id="zh-b0045"></a>

v3.12 的 LCIA 方法没有重大更新。不过，IPCC 和 EF 方法实施了若干小幅修正，USEtox 方法中的一项单位错误已纠正。此外，还添加了新增基本流的表征因子。更多详情请参阅下文“相关文档与文件”中的变更报告。

### <strong>相关文档与文件</strong> <a href="#zh-b0047" id="zh-b0047"></a>

#### <strong>变更报告</strong> <a href="#zh-b0048" id="zh-b0048"></a>

本报告涵盖 ecoinvent 数据库第 3.11 版（2024 年）至第 3.12 版（2025 年）之间的所有变化，同时反映全数据库范围的变化和各行业特定变化。

![doc-icon](../assets/024d8f149226-doc-icon.png) [参阅<strong>变更报告</strong>](../assets/83605407160d-Change-Report-v3.12.pdf)

#### <strong>对应关系文件</strong> <a href="#zh-b0051" id="zh-b0051"></a>

对应关系文件是一个电子表格，列出第 3.11 版和第 3.12 版的全部数据集，并匹配不同版本之间的对应数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png) [参阅<strong>对应关系文件（3.11 至 3.12）</strong>](../assets/43adfb73b32e-Correspondence-File-v3.11---v.3.12.xlsx)

#### <strong>数据库概览文件</strong> <a href="#zh-b0054" id="zh-b0054"></a>

数据库概览文件描述数据库内容，包含以下信息：

- <strong>活动概览</strong>

四个系统模型各自的数据集列表，包括未链接和未分配数据集列表。

- <strong>ecoinvent 地理区域</strong>

ecoinvent 数据库所用的地理区域。每个地理区域均赋予分类，并标明其所包含的地理区域。

- <strong>LCIA 方法</strong>

ecoinvent 为之计算影响得分的 LCIA 方法列表，包括方法版本，以及用于定义表征因子的原始来源。 

![doc-icon](../assets/024d8f149226-doc-icon.png) [参阅<strong>数据库概览文件</strong>](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)

#### <strong>LCIA 实施报告</strong> <a href="#zh-b0063" id="zh-b0063"></a>

LCIA 实施报告记录第 3.12 版 LCIA 方法的实施。

![doc-icon](../assets/024d8f149226-doc-icon.png) [参阅<strong>LCIA 实施报告</strong>](../assets/08f95eab812e-LCIA-Implementation-v3.12.pdf)

#### <strong>其他文件与支持文档</strong> <a href="#zh-b0066" id="zh-b0066"></a>

有关 v3.12 文件及支持文档的更多信息，请参阅支持页面[ecoQuery 中的文件](files.md)。

### v3.12 数据提供者 <a href="#zh-b0068" id="zh-b0068"></a>

- [AIB](https://www.aib-net.org/facts/european-residual-mix)
- [欧洲亚麻与大麻联盟（Alliance for European Flax-Linen & Hemp）](https://allianceflaxlinenhemp.eu/en)
- [工业技术中心 IPC（Centre Technique Industriel, IPC）](https://www.ct-ipc.com/)
- [Enerdata](https://global-energy-data.enerdata.net/)
- [ESU-services Ltd.](https://esu-services.ch/)
- [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/nrg_bal_peh__custom_14425791/default/table?lang=en)
- [芬兰森林工业联合会](https://metsateollisuus.fi/en/home/)（与[芬兰自然资源研究所（Luke）](https://www.luke.fi/en)合作）
- [ICL Group](https://www.icl-group.com/)
- [InterChanvre](https://www.interchanvre.org/interchanvre)
- [国际铝业协会（International Aluminium Institute）](https://international-aluminium.org/)
- [国际锌业协会（International Zinc Association）](https://www.zinc.org/)

### <strong>已知问题</strong> <a href="#zh-b0080" id="zh-b0080"></a>

本部分列出 ecoinvent 数据库第 3.12 版中的全部已知数据错误。

#### <strong>LCIA 问题</strong> <a href="#zh-b0082" id="zh-b0082"></a>

#### 与 LCIA 方法及其实施有关的已知问题记录在[我们的 LCIA GitHub 仓库](https://github.com/ecoinvent/lcia/blob/master/README.md#note-for-v312)中。 <a href="#zh-b0083" id="zh-b0083"></a>

#### <strong>废物市场出现非零得分</strong> <a href="#zh-b0084" id="zh-b0084"></a>

以下三个废物市场发现了程序错误：

- market for non-sulfidic overburden, off-site; GLO（场外非硫化物覆盖层市场）

- market for non-sulfidic tailing, off-site; GLO（场外非硫化物尾矿市场）

- market for spoil from hard coal mining; GLO（硬煤开采剥离废石市场）

这些市场完全由相应处理活动供给，不使用其他交换作为投入或输出。因此，它们应与相应处理活动具有相同的影响得分，多数指标通常为零。然而，在 Cut-off、Consequential 和 EN15804 系统模型下，大多数影响类别（例如 IPCC、EF、ReCiPe、TRACI）出现了很小的非零值。这一行为源于技术矩阵求逆期间数值求解器的不稳定性，使本应明确为零的位置出现微小的数值伪差。

此错误在第 3.9.1 版引入，此后一直存在。不过，由于非零值极小（例如 10<sup>–16</sup>至 10<sup>–25</sup>），其对得分的影响可忽略。此问题将在数据库下一次发布中修复。

#### <strong>数值不稳定性影响 LCI 数值</strong> <a href="#zh-b0091" id="zh-b0091"></a>

第 3.12 版计算期间，求解算法的异常行为影响了部分 LCI 数值。问题发生在技术矩阵求逆时：对病态矩阵进行数值求解，可能使部分列出现微小偏差。随后，该问题表现为某些缩放向量中出现意料之外但极小的需求，导致部分 LCI 数值计算错误。总体而言，对 LCI 数值本身的影响较小，用户可继续使用。不过，这些特定流几乎是少数中点影响类别的唯一贡献者，因此导致结果偏离预期的程度更明显。

具体而言，以下两个影响类别受到影响：

- Ecological Scarcity 2021 no LT-natural resources no LT-biotic resources no LT（生态稀缺性 2021，不含长期排放——自然资源，不含长期排放——生物资源，不含长期排放）

- Ecological Scarcity 2021-natural resources-biotic resources（生态稀缺性 2021——自然资源——生物资源）

此问题仅影响 Cut-off 系统模型。因此，建议用户<strong>不要使用</strong>这两个影响类别的结果。此错误将在数据库下一次发布中修正。

#### <strong>澳大利亚谷物碳平衡失衡</strong> <a href="#zh-b0097" id="zh-b0097"></a>

在不同地区的若干澳大利亚谷物数据集中，由于内含生物源碳被错误赋值，发现了碳平衡失衡。具体而言，相关数值错误地赋给了“Carbon dioxide, land transformation”流，而正确流应为“Carbon dioxide, non-fossil”。

对于工作表 1 中列出的数据集，“Carbon dioxide, non-fossil”基本流交换的数量已更新，用于推算残余物燃烧排放。对于工作表 2 中列出的数据集，特定流的注释已相应修正。

修正值见下方电子表格，将从 2026 年起在未来发布中实施。

![doc-icon](../assets/024d8f149226-doc-icon.png)参阅[澳大利亚谷物碳平衡失衡修正](../assets/98e680a1ed50-Known-Issue-v3.12_Australian-Cereal-Carbon-Corrections.xlsx)

#### <strong>Consequential 模型中铸造铝合金市场失衡</strong> <a href="#zh-b0102" id="zh-b0102"></a>

数据集“market for aluminium, cast alloy; GLO”发现质量平衡失衡。市场活动供应 1 kg 参考产品，但错误地仅链接至 0.312 kg 铝投入。  
  
此错误在第 3.11 版引入，仅影响后果型系统模型。  
  
建议用户在使用该数据集之前手动修正市场质量平衡，因为当前建模可能导致错误计算结果。  
  
此问题将在数据库下一次发布中修正。

{% endtab %}

{% tab title="English 原文" %}

## Version 3.12 of the ecoinvent database continues to expand the content and the geographical coverage of the data across various sectors. This update reflects our continued dedication to delivering transparent and comprehensive environmental data. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.12 was released on November 5th, 2025</strong>. Discover how to [upgrade to our latest version](licensing.md).

February 19th, 2026

Version 3.12 introduces new updates to the following sectors: chemicals and plastics, fuels, metals, electricity, forestry and wood, textiles, agriculture, transport, pulp and paper, and batteries and electronics.

[![webinar-icon](../assets/9c37f83e3b0d-webinar-icon.png)](https://youtu.be/t4p2foRfwAQ)  [Watch the "Introduction to ecoinvent Version 3.12" webinar](https://share.hsforms.com/1oDkuJ0wkSBW9RH34nh_qrAbutpu)






![doc-icon](../assets/024d8f149226-doc-icon.png) [Our answers to the v3.12 Q&A](../assets/642c4b5fa69a-ecoinvent-Introduction-to-version-3.12-Webinar-Q-A.pdf)

[![doc-icon](../assets/024d8f149226-doc-icon.png)](../assets/82c7659626d9-Webinar-introduction-to-ecoinvent-v3.11.pdf)  [Download our overview presentation covering all v3.12 updates](../assets/95000f85e0bd-Introduction-to-ecoinvent-v3.12.pdf)



### <strong>Sectorial Updates</strong> <a href="#en-b0009" id="en-b0009"></a>

#### <strong>Agriculture, Fishery, and Animal Husbandry</strong> <a href="#en-b0010" id="en-b0010"></a>

This year, the [agriculture, fishery, and animal husbandry sector](agriculture-fishery-and-animal-husbandry.md) focuses on several refinements through technical corrections to improve the quality of the data within the agricultural sector. Adjustments in dry mass, water in wet mass, and water content parameters have been made for several crop datasets. Yield information has been added or moved to the general comments to increase consistency in the datasets' metadata for crop datasets. Emissions mainly to air and water have been harmonized and corrected consistently with the modeling approach from the data provider. Finally, some market composition has been updated for RER or GLO.

#### <strong>Batteries</strong> <a href="#en-b0012" id="en-b0012"></a>

The [batteries sector](batteries-electronics.md) has been further refined through a series of technical corrections and the introduction of new chemical components. Multiple cathode and anode datasets were harmonized following proxy refinements, including the replacement of intermediate exchanges such as polyvinylfluoride with polyvinylidene fluoride and latex with styrene butadiene rubber.

Exchange properties and documentation were updated across several NMC and NCA chemistries to improve chemical accuracy and transparency. Additional improvements included clarifications on manufacturing scrap, updates of energy inputs to align with recent sources, and the inclusion of chemical formulas in the documentation of hydroxide and oxide precursors.

Finally, several new chemical compounds relevant to battery applications were added to the database, extending the coverage of materials used in alternative formulations of anodes, cathodes, and electrolytes.

#### <strong>Chemicals and Plastics</strong> <a href="#en-b0016" id="en-b0016"></a>

The [chemicals and plastics sector](chemicals-and-plastics.md) in ecoinvent v3.12 is updated to substantially improve the regional coverage for: (1) ethylene and propylene and their homopolymers (LDPE, LLDPE, HDPE, and polypropylene); (2) vinyl chloride monomer, and its polymers (emulsion- and solution-polymerized PVC); (3) acrylic acid; (4) ethylene oxide; (5) methanol, (6) industrial gases (nitrogen and oxygen); among others. This targeted supply chain enhancement improves the representation of diverse chemical and plastic derivatives and builds on the regional expansion already achieved in the previous versions.

Furthermore, ecoinvent v3.12 replaces previously aggregated data for hydrogen cyanide, polystyrenes (general purpose, high impact, and expandable polystyrene), and polybutadiene from previous database versions with disaggregated unit processes to enable accurate linking to the ecoinvent background data. To complement this disaggregation, new and updated data have been introduced for styrene monomer production and, consequently, propylene oxide via the PO/SM process, encompassing new technologies and additional regional coverage.

Moreover, v3.12 introduces new industry data covering the supply of bromine in Israel, provided by the [ICL Group](https://www.icl-group.com/), i.e., a major global producer of bromine and bromine-based products. This collaboration is complemented by an internal assessment to also cover bromine production in other major regions. Additionally, ecoinvent v3.12 features new data for key polymer processing services, provided by [Centre Technique Industriel, IPC](https://www.ct-ipc.com/), i.e., blown film extrusion (several configurations) and plastic bag making, to expand the ecoinvent data coverage in this domain.

Finally, ecoinvent v3.12 builds on the work completed in preceding versions for product portfolio expansion, to include forty new products of varied interest not previously covered. Additionally, six new generic datasets for key organic product groups—covering basic precursors, alcohols, aromatics, carboxylic acids, esters, and unspecified organics—are introduced to replace the legacy and more generic “chemical, organic” flow. Efforts to expand the product coverage further for both specific chemicals and plastics, as well as generic datasets based on functional groups, will continue in future releases.

#### <strong>Electricity</strong> <a href="#en-b0021" id="en-b0021"></a>

ecoinvent version 3.12 updates the [energy sector’s](energy.md) electricity market datasets with the consistent approach applied in ecoinvent versions 3.6 through 3.11. Consistent with v3.11, [Enerdata](https://global-energy-data.enerdata.net/) serves as the primary data source for electricity generation across most regions, with exceptions where detailed national data are available, and for European Union (EU) member states, where [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/nrg_bal_peh__custom_14425791/default/table?lang=en) database from the European Commission is used. The electricity market mixes generally represent the year 2022, except for Brazil (BR), Canada (CA), China (CN), India (IN), Switzerland (CH), and the United States (U.S.), which are updated to 2023 based on comprehensive national statistics. For India, the update corresponds to the fiscal year of April 2022-March 2023. Additionally, the European electricity residual mix markets in version 3.12 represent the year 2024 using statistics from [AIB](https://www.aib-net.org/facts/european-residual-mix).

Furthermore, additional minor corrections and harmonization efforts were carried out to update the documentation and meta information of electricity markets, transformation, and import datasets.

#### <strong>Forestry and Wood</strong> <a href="#en-b0024" id="en-b0024"></a>

The ecoinvent version 3.12 introduces data updates and enhancements to the [forestry and wood sector](forestry-and-wood.md). The geographical coverage of the sector was expanded by the introduction of Finnish forestry data. This data was provided by the [Finnish Forest Industries Federation](https://metsateollisuus.fi/en/home/), and the project was done in close collaboration with [Natural Resources Institute Finland (Luke)](https://www.luke.fi/en). Three forestry datasets are introduced: pine, spruce, and birch. The datasets represent rotation forestry. Together, they cover 97% of the annual harvested area in Finland.

Furthermore, the product naming conventions across the sector are harmonized. The goal of the update is to eliminate confusion between physical product characteristics and measurement basis, which are not always equivalent. The new naming convention more clearly states four key attributes for each primary forestry product: physical bark presence (with bark or debarked), physical moisture state (green/dry), measurement basis as related to bark if bark is present (under bark/over bark), and measurement basis for moisture (green/dry).

#### <strong>Fuels</strong> <a href="#en-b0027" id="en-b0027"></a>

The new ecoinvent version 3.12 in the [fuels sector](fuels.md) builds on the extensive oil and gas overhaul in versions 3.9.1 (2022), 3.10 (2023), and the addition/update of supply mixes of natural gas and petroleum in v3.11 (2024). The v3.12 brings an update for data on the extraction or production of crude petroleum oil and natural gas, with a geographical coverage of 40 countries for onshore production and 36 countries for offshore production, based on the reference year of 2023. Additionally, version 3.12 includes regionalization of natural gas liquids production and fractionation datasets, adding 18 new geographies covering 95% of global natural gas liquids production and subsequent fractionation. Five new geographies have also been added, for a total coverage of 96% of global helium production in this latest version.

#### <strong>Metals</strong> <a href="#en-b0029" id="en-b0029"></a>

In the [metals sector](metals.md), comprehensive improvements in steel, aluminium, and zinc alloy production address important gaps in specialized material modeling.

In the steel sector, seven new datasets for specific steel alloys based on 100% scrap input via Electric Arc Furnace (EAF) production have been added, providing differentiated modeling for bearing, carbon, case hardening, high-strength low-alloy, structural, and weathering steels. These datasets support more accurate environmental assessments in sectors where material selection is critical to performance and sustainability outcomes.

The aluminium production chain has been comprehensively updated with 2019 data from the [International Aluminium Institute](https://international-aluminium.org/), covering the entire value chain from bauxite mining to ingot casting. This update includes improved geographical coverage, updated electricity consumption patterns for the aluminium industry, and better representation of import/export flows through enhanced market composition data.

New datasets for Zamak production in Europe, developed with the [International Zinc Association](https://www.zinc.org/), provide detailed inventories for this widely used zinc alloy manufactured primarily from secondary zinc. The dataset represents approximately 76% of European Zamak production and supports environmental footprint modeling for automotive components and consumer products.

Additional improvements encompass corrections to various metal processing datasets, including updates to energy inputs in metal working factories, corrections to zinc oxide production exchanges, and refinements to steel production documentation. These enhancements collectively strengthen the technical rigor and applicability of the Metals sector data for life cycle assessment practitioners.

#### <strong>Textiles</strong> <a href="#en-b0035" id="en-b0035"></a>

The ecoinvent database v3.12 expands the [textiles sector](textiles.md) by introducing new hemp datasets based on primary data from French hemp producers and processors. France dominates both European (60%) and global (50%) hemp fiber production. The modelled data is representative of over 98% of the national French production. Disaggregated unit processes are introduced for agricultural cultivation of the hemp crop, decortication of the hemp stems, and cottonization of the fibres (cutting fibers to 40-50mm lengths suitable for textile spinning). Our project partner, [InterChanvre](https://www.interchanvre.org/interchanvre), supplied the data.

Additionally, existing European flax data was updated through the introduction of new valuable by-products in the scutching process, as well as other minor corrections to improve the documentation. Changes to the European flax datasets were carried out in collaboration with the original project partner, the [Alliance for European Flax-Linen & Hemp](https://allianceflaxlinenhemp.eu/en). Other corrections include various minor updates for existing cotton and polyester datasets to eliminate identified errors & inconsistencies. ISIC & CPC classification codes were also aligned for multiple textile activities and products.

#### <strong>Transport</strong> <a href="#en-b0038" id="en-b0038"></a>

The v3.12 [transport sector](transport.md) benefits from updates and corrections for three of its five modes: rail, road, and sea shipping. The main objective was to enhance the data quality of the sector through targeted improvements with newly available information, or by discovered errors. The smallest update relates to the addition of waste and waste handling in tram tracks and railways; meanwhile, the road benefited from a correction due to an error in an amount of brake wear for both passenger cars and lorries. Sea transport was the one with the highest level of improvement: the new emission limits of HFO were included, together with the fleet composition reported by the latest [International Maritime Organization GHG report](https://www.imo.org/en/ourwork/environment/pages/fourth-imo-greenhouse-gas-study-2020.aspx). The update covered the production, maintenance, and use of the ships.

#### <strong>Waste Management and Recycling</strong> <a href="#en-b0040" id="en-b0040"></a>

The scope of the [waste management and recycling sector](waste-management-and-recycling.md) updates for version 3.12 was mainly minor corrections and updates as a result of the large dataset additions made for versions 3.9-3.11. These corrections are based on both internal and external feedback, e.g., users highlighting minor errors or improved assumptions. These enhancements allow for more representative and consistent inventories for ecoinvent users.

Users highlighted a large Chromium VI emission from electric arc furnace slag going to residual material landfill, leading to high toxicity values in LCIA. Based on more recent measurements of the specific slag ([BAFU & Carbotech, 2021](https://www.bafu.admin.ch/dam/bafu/en/dokumente/wirtschaft-konsum/externe-studien-berichte/life-cycle-inventories-of-steel-and-iron-processes.pdf.download.pdf/Life_Cycle_Inventories_of_Steel_and_Iron_Processes_2021.pdf)), the availability of Chromium to leach as Chromium VI was reduced in the model (as it is rather more stably bound as Chromium III). ecoinvent users in the waste and metals sectors will find reduced impact scores in the ecotoxicity as well as human toxicity categories due to this update.

Internal consistency was improved by aligning the ISIC classifications of treatments and their respective markets, and EN15804 waste inventory indicators were added to datasets that previously had them omitted. The implementation of these indicators is still being aligned with different stakeholders; however, their inclusion is now consistent across the database.

The large project of plastic recycling in Europe for v3.11 led to recyclable polymers being available for other datasets to incorporate. A comprehensive assessment and implementation were made, so that specific European datasets generating plastic wastes would send (some or all of) their waste polymers to these recycling facilities. Other corrections were made to amend errors in carbon mineralisation of sludge use on land and in plastic recycling VOC emissions, as well as transport consumption. Direct disposal of wastewater from textile production was re-added to geographies (IN and BD), which used it previously. Meta documentation typos and references to wrong activities were amended.

#### <strong>LCIA Methods Updates</strong> <a href="#en-b0045" id="en-b0045"></a>

There were no major updates to LCIA methods for v3.12. However, several minor fixes were implemented for the IPCC and EF methods, and a unit error in the USEtox method was corrected. Additionally, characterization factors for new elementary flows were added. For more details, consult the Report of Changes in the Relevant Documents and Files below

### <strong>Relevant Documents and Files</strong> <a href="#en-b0047" id="en-b0047"></a>

#### <strong>Report of Changes</strong> <a href="#en-b0048" id="en-b0048"></a>

This report covers all changes made in the ecoinvent database between version 3.11 (2024) and version 3.12 (2025). It reflects both database-wide changes as well as sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png) [See <strong>Report of Changes</strong>](../assets/83605407160d-Change-Report-v3.12.pdf)

#### <strong>Correspondence File </strong> <a href="#en-b0051" id="en-b0051"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.11 and 3.12 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png) [See <strong>Correspondence File (3.11 to 3.12)</strong>](../assets/43adfb73b32e-Correspondence-File-v3.11---v.3.12.xlsx)

#### <strong>Database Overview File</strong> <a href="#en-b0054" id="en-b0054"></a>

The database overview file describes the contents of the database. The following information is contained in the file:

- <strong>Activity Overview(s)</strong>

The lists of datasets contained in each of the four system models, including the list of unlinked and unallocated datasets.

- <strong>ecoinvent Geographies</strong>

The geographies used in the ecoinvent database. Each geography is assigned a classification, and the geographies contained in each geography are indicated.

- <strong>LCIA Methods</strong>

The list of the LCIA methods for which ecoinvent calculates impact scores. The version of the methods is indicated, and the original source used for defining the characterization factors is provided. 

![doc-icon](../assets/024d8f149226-doc-icon.png) [See <strong>Database Overview File</strong>](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)

#### <strong>LCIA Implementation Report</strong> <a href="#en-b0063" id="en-b0063"></a>

The LCIA implementation report documents the implementation of LCIA methods for version 3.12.

![doc-icon](../assets/024d8f149226-doc-icon.png) [See <strong>LCIA Implementation Report</strong>](../assets/08f95eab812e-LCIA-Implementation-v3.12.pdf)

#### <strong>Other Files and Support Documents</strong> <a href="#en-b0066" id="en-b0066"></a>

More information about v3.12's files and supporting documents can be found on our support page, [Files in ecoQuery](files.md).

### v3.12 Data Providers <a href="#en-b0068" id="en-b0068"></a>

- [AIB](https://www.aib-net.org/facts/european-residual-mix)
- [Alliance for European Flax-Linen & Hemp](https://allianceflaxlinenhemp.eu/en)
- [Centre Technique Industriel, IPC](https://www.ct-ipc.com/)
- [Enerdata](https://global-energy-data.enerdata.net/)
- [ESU-services Ltd.](https://esu-services.ch/)
- [Eurostat](https://ec.europa.eu/eurostat/databrowser/view/nrg_bal_peh__custom_14425791/default/table?lang=en)
- [Finnish Forest Industries Federation](https://metsateollisuus.fi/en/home/) (in collaboration with [Natural Resources Institute Finland (Luke)](https://www.luke.fi/en))
- [ICL Group](https://www.icl-group.com/)
- [InterChanvre](https://www.interchanvre.org/interchanvre)
- [International Aluminium Institute](https://international-aluminium.org/)
- [International Zinc Association](https://www.zinc.org/)

### <strong>Known Issues</strong> <a href="#en-b0080" id="en-b0080"></a>

This section lists all known data errors in version 3.12 of the ecoinvent database.

#### <strong>LCIA Issues</strong> <a href="#en-b0082" id="en-b0082"></a>

#### Known issues related to LCIA methods and their implementation are documented on [our LCIA GitHub repository](https://github.com/ecoinvent/lcia/blob/master/README.md#note-for-v312). <a href="#en-b0083" id="en-b0083"></a>

#### <strong>Non-Zero Score Values to Waste Markets</strong> <a href="#en-b0084" id="en-b0084"></a>

A bug was identified in the three following waste markets:

- market for non-sulfidic overburden, off-site; GLO

- market for non-sulfidic tailing, off-site; GLO

- market for spoil from hard coal mining; GLO

These markets are supplied exclusively by the corresponding treatment activities, with no additional exchanges used as inputs or outputs. Therefore, they are expected to have the same impact scores as the treatments—typically zero for the majority of indicators. However, small non-zero values are observed across most impact categories (e.g., IPCC, EF, ReCiPe, TRACI) under the cut-off, consequential, and EN15804 system models. This behavior arises from numerical solver instability during the inversion of the technology matrix, leading to the appearance of minor numerical artifacts where a distinct zero was expected.

This bug was introduced in version 3.9.1 and has been present ever since. However, its impact on the scores is negligible, as the non-zero values are very small (e.g., 10<sup>–16</sup> to 10<sup>–25</sup>). The issue will be fixed in the next database release.

#### <strong>LCI Values Impacted by Numerical Instabilities</strong> <a href="#en-b0091" id="en-b0091"></a>

During the calculation of version 3.12, a misbehavior of the solving algorithm affected certain LCI values. The issue occurred during the matrix inversion of the technology matrix, where the numerical solving of ill-conditioned matrices can introduce tiny off-values in some columns. The issue then manifested itself as unexpected, albeit very small, demand in some scaling vectors. As a result, some LCI values were miscalculated. Overall, this has a minor effect on the LCI values themselves, and users may continue to use them. However, the specific flows are almost sole contributors to a few midpoint impact categories, leading to a more pronounced deviation from the expected result.

Specifically, the two following impact categories are affected:

- Ecological Scarcity 2021 no LT-natural resources no LT-biotic resources no LT

- Ecological Scarcity 2021-natural resources-biotic resources

This issue affects only the cut-off system model. Users are therefore advised <strong>not to use the results</strong> for these two impact categories. The bug will be corrected in the next database release.

#### <strong>Australian Cereal Carbon Imbalance</strong> <a href="#en-b0097" id="en-b0097"></a>

In several Australian cereal datasets across different regions, a carbon imbalance was identified due to the incorrect assignment of embodied biogenic carbon. Specifically, the value was mistakenly allocated to the flow "Carbon dioxide, land transformation" instead of the correct flow "Carbon dioxide, non-fossil".

For the datasets reported in sheet 1, the amount of the elementary exchange "Carbon dioxide, non-fossil" has been updated to derive the emissions from burning residues. For the datasets reported in sheet 2, the comments for specific flows have been corrected accordingly.

The corrected values are provided in the spreadsheet below and will be implemented in future releases from 2026 onwards.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Australian Cereal Carbon Imbalance Corrections](../assets/98e680a1ed50-Known-Issue-v3.12_Australian-Cereal-Carbon-Corrections.xlsx)

#### <strong>Imbalanced Market for Aluminium, Cast Alloy in Consequential</strong> <a href="#en-b0102" id="en-b0102"></a>

A mass imbalance was identified in the dataset “market for aluminium, cast alloy; GLO”. The market activity supplies 1 kg of reference product but is incorrectly linked to only 0.312 kg of aluminium input.  
  
This error was introduced in version 3.11 and affects only the consequential system model.  
  
Users are advised to manually correct the market mass balance before using the dataset, as the current modeling may lead to erroneous calculation results.  
  
The issue will be corrected in the next database release.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0017**：原文写 solution-polymerized，但常见工业 PVC 分类为乳液聚合与悬浮聚合；可能为源文术语错误，不能未经确认改为 suspension。 请根据实际 PVC 数据集技术说明确认；目前保留原文含义。 [查看完整记录](../review/issues.md#issue-045)
- **已处理／已说明 · b0018**：aggregated 指过程数据汇总，化学品语境下“聚合数据”容易与聚合反应混淆。 已改为“汇总数据”。 [查看完整记录](../review/issues.md#issue-046)
- **已处理／已说明 · b0044**：sludge use on land 指污泥在土地上施用，不宜混同土地利用类别。 已明确为“土地施用”。 [查看完整记录](../review/issues.md#issue-047)
- **已处理／已说明 · b0046**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-048)
- **已处理／已说明 · b0048**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-049)
- **已处理／已说明 · b0050**：统一文档名称。 已修正。 [查看完整记录](../review/issues.md#issue-050)
