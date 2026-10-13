# ecoinvent 3.11 版

英文原题：ecoinvent Version 3.11  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.11)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-09-15

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库 3.11 版以更广泛的数据支持用户，为可持续发展领域创造新的可能。本次更新新增超过 2,066 个数据集，更新超过 4,497 个数据集。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.11 于 2024 年 11 月 19 日发布</strong>。了解如何[升级到最新版本](licensing.md)。

<strong>ecoinvent v3.12 于 2025 年 11 月 5 日发布。</strong>了解如何[升级到最新版本](licensing.md)。

2025年9月24日

3.11 版为以下部门带来重要更新：燃料、能源、化学品与塑料、电池、金属、建筑与施工、废物、农业、林业、制浆造纸和运输。

[![webinar-icon](../assets/9c37f83e3b0d-webinar-icon.png)](https://youtu.be/t4p2foRfwAQ) [观看“ecoinvent 3.11 版介绍”网络研讨会](https://youtu.be/rlDdWB51Wfs)



![doc-icon](../assets/024d8f149226-doc-icon.png) [下载 3.11 常见问题解答](../assets/c294d225037a-Webinar-introduction-to-ecoinvent-v3.11-FAQ.pdf)

![doc-icon](../assets/024d8f149226-doc-icon.png) [下载涵盖 3.11 全部更新的概览演示文稿](../assets/c29a5e16a923-Webinar-introduction-to-ecoinvent-v3.11.pdf)

### <strong>部门更新</strong> <a href="#zh-b0010" id="zh-b0010"></a>

#### <strong>燃料</strong> <a href="#zh-b0011" id="zh-b0011"></a>

新的 ecoinvent 3.11 版以[3.9.1](ecoinvent-version-3.9.1.md)（2022）和[3.10](ecoinvent-version-3.10.md)（2023）版石油与天然气全面修订为基础，根据 2023 年供应状况，新增或更新 57 个国家的高压天然气供应，覆盖全球天然气消费的 88%。v3.11 还修订陆上／海上管道运输及液化天然气（LNG）海运距离估算，以改进地区化。瑞士、欧洲不含瑞士、北美地区（RNA）、巴西（BR）、哥伦比亚（CO）、印度（IN）、秘鲁（PE）和南非（ZA）的原油供应组合已更新，反映 2023 年贸易状况。此次更新采用 2023 年最新贸易统计，体现近年地缘政治变化导致的天然气供应链调整，尤其是欧洲市场的变化。

此外，3.11 版[燃料部门](fuels.md)根据 2022 年数据更新褐煤和硬煤供应链，修订采矿甲烷排放因子并更新产量。为加强地区化，硬煤开采活动新增 4 个欧洲地理区域，硬煤市场活动新增 22 个欧洲地理区域，并新增日本和韩国分别划分的市场。还新增多个硬煤进口活动，更准确、详细地表示全球煤炭贸易流。最后，所有硬煤和褐煤数据集的元信息均已更新、修正和统一。

#### <strong>能源</strong> <a href="#zh-b0014" id="zh-b0014"></a>

ecoinvent 3.11 更新[能源部门](energy.md)电力市场组合，以反映 2021 年状况。巴西、中国、美国、加拿大和瑞士更新为反映 2022 年状况；印度更新为表示 2021 年 4 月／2022 年 3 月的财政年度。这些特定国家均采用国家统计，其余国家采用全球统计。从 3.11 版起，全球统计基于[enerdata](https://www.enerdata.net/) 数据库。剩余电力组合反映 2023 年最新数据。

除其他小幅修正外，还开展一致化工作，更新电力市场、变压和进口数据集的文档及元信息。

#### <strong>化学品</strong> <a href="#zh-b0017" id="zh-b0017"></a>

v3.11 的[化学品部门](chemicals-and-plastics.md)更新了关键化学前驱体的数据表示，例如一氧化碳、乙酸及其酯、丙烯酸酯、异丙苯、硝基苯、2,4-二硝基甲苯、苯胺、光气和双酚 A。因此，这项针对供应链的改进也改善了异氰酸酯、聚氨酯、环氧树脂和聚碳酸酯等多种化学品及塑料衍生物的表示。

此外，v3.11 将此前数据库版本中氯甲烷、甲基丙烯酸甲酯和聚甲基丙烯酸甲酯的聚合数据替换为细分单元过程，以便准确链接到 ecoinvent 背景数据。

v3.11 还引入[欧洲乙烯基制造商委员会](https://pvc.org/)提供的氯乙烯供应及聚氯乙烯生产更新行业数据，以及[欧洲 UP/VE 树脂协会](https://www.upresins.org/)提供的不饱和聚酯（UP）和环氧乙烯基酯（VE）树脂数据，包括：（1）基于双酚 A 环氧树脂的 VE 树脂；（2）基于双环戊二烯、间苯二甲酸、马来酸、邻苯二甲酸及再生聚对苯二甲酸乙二醇酯的 UP 树脂。此外，v3.11 包含[工业技术中心 IPC](https://www.ct-ipc.com/)提供的复合材料制造新数据，即压制、模塑、拉挤、手工／手糊及纤维缠绕过程，扩展该领域的数据覆盖。

最后，v3.11 化学品部门在前版工作基础上更新现有数据，并尽可能扩展地理覆盖，还新增此前未覆盖的 18 种产品。具体引入亚洲（汇总地区或单个国家）及美国的部分化学品数据。这项工作将在后续发布中继续。

#### <strong>电池</strong> <a href="#zh-b0022" id="zh-b0022"></a>

[电池部门](batteries-electronics.md)新增中国和全球地理区域的两种锂离子电池化学体系：NMC532（镍钴锰）和 NMC622。新数据集包括正极活性材料前驱体（NMC 氢氧化物）、正极活性材料（NMC 氧化物）、正极、电芯和电池包，采用与数据库其他锂离子电池相同的方法建模。还开发了尖晶石型钛酸锂新活动，作为另一种负极活性材料。为支持新的电池技术，另开发了钠离子电池电解液数据集。

中国地理区域的人造石墨生产路线基于与[Tokai COBEX](https://tokaicobex.com/)的合作，并参照新发表论文进行了更新。数据库也新增中国电池应用天然石墨生产。

最后，电池部门迈出了全面内容更新的一步，重点更新市场数据集，并统一锂离子电池组件产量。

#### <strong>金属</strong> <a href="#zh-b0026" id="zh-b0026"></a>

此次更新以新增和更新数据扩展并改进[金属部门](metals.md)覆盖。v3.11 引入欧洲取向电工钢（GOES）生产数据，以及用作 GOES 生产原料的含硅 3.2% 合金钢生产数据集。新增中国低品级和高品级镓生产两个数据集（由[EMPA](https://www.empa.ch/)提供）。现有金属部门覆盖的改进包括更新金属含量和价格等属性、补充缺失交换或重命名交换。约 60 种金属产品价格根据 ISE（[稀土与战略金属研究所](https://en.institut-seltene-erden.de/)）数据库更新；100 多种金属产品更新或新增金属含量属性。采矿数据集补充此前缺失的脉石交换，改善相关影响评价。最后，部分废金属交换重命名，提高命名清晰度，帮助用户更容易识别相关交换。

#### <strong>建筑与施工</strong> <a href="#zh-b0028" id="zh-b0028"></a>

v3.11 为数据库[建筑与施工部门](building-and-construction.md)带来大量改进，包括丰富的新数据及多项更新。与[加拿大国家研究委员会（NRC）](https://nrc.canada.ca/en)和[加拿大水泥协会（CAC）](http://www.cement.ca/)合作开发石灰石开采与初级破碎、熟料生产及水泥制造新数据集，覆盖加拿大平均生产（CA）和安大略省专门数据（CA-ON）。石灰石开采和破碎数据集构成后续同地理范围熟料制造数据集的基础。熟料数据集又用于创建四个通用（GU）和通用石灰石（GUL）水泥数据集，符合 CSA A3001 标准，并参考 ASTM C150、ASTM C595 等其他相关北美标准。此外，v3.11 新增内部开发的加拿大（CA）一体化水泥厂数据集，全面表示熟料和水泥组合生产所用设施与机械，覆盖全部主要生产阶段。

此外，v3.11 更新了本部门若干现有数据集。石灰石和石灰产品供应链已修订，修改上游活动和产品名称及属性，并更新产量及相应市场份额。其他更新包括修订石灰砂浆、水泥砂浆、50MPa 混凝土、多种混凝土砌块、石灰石、水硬性石灰、生石灰、砂、砾石、双层和三层玻璃、沥青密封层、页岩砖及保温抹灰材料的生产活动。

#### <strong>废物管理与回收</strong> <a href="#zh-b0031" id="zh-b0031"></a>

3.11 版[废物部门](waste-management-and-recycling.md)新增和更新多种数据，涵盖广泛主题。欧盟 27 国、瑞士、挪威、冰岛和英国的城市固体废物（MSW）处理数据集现已完全地区化，以当地生成废物的定制元素组成和组分构成为基础，且每个国家都有更新的当地处理技术组合。相应市场也采用地区化运输距离，并在需要时采用地区化损失。

塑料回收领域同样作出广泛变更。与[Plastics Recyclers Europe](https://www.plasticsrecyclers.eu/)合作新增数据，对欧洲废塑料机械回收建模。涉及的聚合物包括废聚乙烯（PE）、聚乙烯／聚丙烯（PE/PP）、高密度聚乙烯（HDPE）、低密度聚乙烯（LDPE）、聚苯乙烯（PS）、聚对苯二甲酸乙二醇酯（PET）、聚氯乙烯（PVC）、聚丙烯（PP）、丙烯腈－丁二烯－苯乙烯（ABS）、ABS／聚苯乙烯（ABS/PS），以及来自家庭、工业、农业、商业、建筑与拆除、废电气电子设备（WEEE）等不同来源的混合塑料。此外，与[阿里云—Energy Experts（Alibaba Cloud – Energy Experts）](http://www.alibabacloud.com/en/product/energy-expert)合作建模中国废聚酯化学回收。废聚酯来自纺织生产工业活动，经化学处理制成 PET 颗粒。另一类化学回收是英国废混合塑料的水热处理，数据由[Mura Technology](https://muratechnology.com/)与[华威大学](https://warwick.ac.uk/)合作提供。

另新增两种处理过程：一是欧洲和全球纺织生产废水处理；二是中国天然石墨采矿的石墨尾矿处理。最后，所有废物和废金属采用统一命名，明确金属副产品的去向，例如通过焚烧、填埋等处理，或回收后再利用。

#### <strong>农业</strong> <a href="#zh-b0035" id="zh-b0035"></a>

在[农业部门](agriculture-fishery-and-animal-husbandry.md)，3.11 通过与[Agroscope](https://www.agroscope.admin.ch/agroscope/en/home.html)的密切合作，全面更新瑞士农业生产。此次发布包含苹果和梨等果树、大麦、玉米和小麦等谷物、胡萝卜等根类蔬菜、花椰菜等十字花科蔬菜，以及豌豆和蚕豆等富含蛋白质豆类作物的详细数据集。覆盖瑞士山区、丘陵和平原子区域的常规及有机农业方式，共新增 136 个数据集，提供更深入的瑞士农业信息。

#### <strong>林业与木材</strong> <a href="#zh-b0037" id="zh-b0037"></a>

3.11 的[林业与木材部门](forestry-and-wood.md)更新侧重现有数据和文档，尤其是林业活动产量。此外，数据库范围的生物源碳修正也影响本部门。

#### <strong>制浆造纸</strong> <a href="#zh-b0039" id="zh-b0039"></a>

[制浆造纸部门](pulp-and-paper.md)新增三个快餐应用纸基包装相关数据集，对纸杯及杯盖、汉堡包装纸和薯条盒等餐具生产建模。数据由[EPPA](https://eppa-eu.org/)（欧洲纸包装联盟）提供。饮料纸盒加工、牛皮纸及纸袋生产的现有活动采用近期行业数据更新。饮料纸盒加工数据由[ACE](https://www.beveragecarton.eu/)（饮料纸盒与环境联盟）及[ifeu](https://www.ifeu.de/en/)（能源与环境研究所）提供；牛皮纸相关数据由[CEPI Eurokraft 和 Eurosac](https://www.cepi-eurokraft.org/)与[RISE](https://www.ri.se/en)（瑞典研究院）合作提供。

#### <strong>运输</strong> <a href="#zh-b0041" id="zh-b0041"></a>

3.11 版[运输部门](transport.md)有三项主要更新。首先更新欧洲及全球在用乘用车车队，提高在用车队的代表性。第二，通过所有运输数据集采用标准命名，提高数据集清晰度和可访问性，使差异更容易识别。第三，新增欧洲及全球航空器维护数据集，依据各数据集不同航程类型定制的飞行和维护计划。

### <strong>LCIA 方法更新</strong> <a href="#zh-b0043" id="zh-b0043"></a>

3.11 版更新并平衡非化石碳流，特别关注生物源碳吸收。这使遵循 IPCC 的气候变化影响评价能够以 -1/+1 表征非化石二氧化碳的清除／释放，符合 ISO 14067 等某些标准和指南的要求。实施方式是在现有“IPCC 2021”方法之外引入补充方法“IPCC 2021 (incl. biogenic CO2)”。两种方法的影响类别可以映射到标准和指南。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[IPCC 方法使用指南](guidance-on-ipcc-methods.md)

此外，EN15804 影响评价已重组并重命名，以更接近标准中的命名，帮助用户找到正确指标。

### <strong>相关文档和文件</strong> <a href="#zh-b0047" id="zh-b0047"></a>

#### <strong>变更报告</strong> <a href="#zh-b0048" id="zh-b0048"></a>

本报告涵盖数据库 3.10 版（2023）与 3.11 版（2024）之间的全部变更，包括数据库整体变更和部门特定变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/b05ee1a65d32-Change-Report-v3.11.pdf)

#### <strong>对应关系文件</strong> <a href="#zh-b0051" id="zh-b0051"></a>

对应关系文件是一份电子表格，列出 3.10 和 3.11 版全部数据集，并匹配两版本间相互对应的数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件（3.10 至 3.11）](../assets/c827eab44ad7-Correspondence-File-v3.10---v.3.11.xlsx)

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件（3.10.1 至 3.11）](../assets/8b779e1f37c9-Correspondence-File-v3.10.1---v.3.11.xlsx)

#### <strong>数据库概览文件</strong> <a href="#zh-b0055" id="zh-b0055"></a>

数据库概览文件描述数据库内容，包含以下信息：

- <strong>活动概览</strong>

分别列出四种系统模型中包含的数据集，也包括未链接和未分配的数据集清单。

- <strong>ecoinvent 地理区域</strong>

数据库中使用的地理区域。每个地理区域均具有分类，并标明其所包含的地理区域。

- <strong>LCIA 方法</strong>

列出 ecoinvent 计算影响结果值所采用的 LCIA 方法，注明方法版本，并提供用于确定表征因子的原始来源。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[数据库概览文件](../assets/066ac4ecf765-Database-Overview-for-ecoinvent-v3.11-6-.xlsx)

#### <strong>LCIA 实施报告</strong> <a href="#zh-b0064" id="zh-b0064"></a>

LCIA 实施报告记录 3.11 版 LCIA 方法的实施。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[LCIA 实施报告](../assets/957bf4cc0635-LCIA-implementation-3.11.pdf)

### 3.11 数据提供者 <a href="#zh-b0067" id="zh-b0067"></a>

- [Agroscope](https://www.agroscope.admin.ch/agroscope/en/home.html)
- [阿里云—Energy Experts（Alibaba Cloud – Energy Experts）](http://www.alibabacloud.com/en/product/energy-expert)
- [饮料纸盒与环境联盟（ACE）](https://www.beveragecarton.eu/)
- [CEPI Eurokraft 和 Eurosac](https://www.cepi-eurokraft.org/)（与[RISE〔瑞典研究院〕合作）](https://www.ri.se/en)
- [加拿大水泥协会（CAC）](http://www.cement.ca/)
- [工业技术中心 IPC](https://www.ct-ipc.com/)
- [Climate TRACE](https://climatetrace.org/)
- [EMPA](https://www.empa.ch/)
- [enerdata](https://www.enerdata.net/)
- [ESU-services Ltd.](https://esu-services.ch/)
- [欧洲乙烯基制造商委员会](https://pvc.org/)
- [欧洲纸包装联盟（EPPA）](https://eppa-eu.org/)
- [欧洲 UP/VE 树脂协会](https://www.upresins.org/)
- [德国航空航天中心（DLR）](https://www.dlr.de/en)
- [ifeu（能源与环境研究所）](https://www.ifeu.de/en/)
- [稀土与战略金属研究所](https://en.institut-seltene-erden.de/)
- [联合研究中心（JRC）](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/joint-research-centre_en)
- [Mura Technology](https://muratechnology.com/)（与[华威大学合作）](https://warwick.ac.uk/)
- [加拿大国家研究委员会（NRC）](https://nrc.canada.ca/en)
- [Plastics Recyclers Europe](https://www.plasticsrecyclers.eu/)
- [Tokai COBEX](https://tokaicobex.com/)

### <strong>已知问题</strong> <a href="#zh-b0089" id="zh-b0089"></a>

此部分列出 ecoinvent 数据库 3.11 版的全部已知数据错误。

#### 数据集：printed wiring board production, for surface mounting（表面贴装用印制线路板生产） <a href="#zh-b0091" id="zh-b0091"></a>

- <em>printed wiring board production, for surface mounting, Pb containing surface（含铅表面）</em>
- <em>printed wiring board production, for surface mounting, Pb free surface（无铅表面）</em>

<strong>此问题在数据库 3.11 版中发现。</strong>

这两个数据集在 3.8 版中错误应用了变更，导致其中几乎所有交换数量都被低估。

为解决此问题，重新分析了第 2 版报告引用的原始来源，并修正数值。与 v3.11 结果值相比，变更会使 GWP 结果值增加约 100% 以上。其他影响类别（如 ADP）也受影响，部分结果值预计增加 100% 至 250%。

请注意，这些数据集也用于以下数据集，因此后者的结果值可能受到影响：

- printed wiring board production, mounted mainboard, laptop computer, Pb free, GLO（笔记本电脑无铅已装配主板生产）
- printed wiring board production, mounted mainboard, desktop computer, Pb free, GLO（台式计算机无铅已装配主板生产）
- printed wiring board production, surface mounted, unspecified, Pb free, GLO（无铅表面贴装印制线路板生产，未指定）
- computer production, desktop, without screen, GLO（不含显示器的台式计算机生产）
- printed wiring board production, mounted mainboard, desktop computer, Pb containing, GLO（台式计算机含铅已装配主板生产）
- printed wiring board production, surface mounted, unspecified, Pb containing, GLO（含铅表面贴装印制线路板生产，未指定）
- printed wiring board production, mounted mainboard, laptop computer, Pb containing, GLO”（笔记本电脑含铅已装配主板生产）

#### <strong>数据集：calcium carbonate production, precipitated（沉淀碳酸钙生产）</strong> <a href="#zh-b0105" id="zh-b0105"></a>

<strong>现告知您数据库 3.11 版中发现的以下问题：</strong>

此数据集在 3.8 版中所作变更导致了下述非预期问题。

自 3.8 版起，沉淀碳酸钙生产清单计入聚合系统的输入和输出，从“limestone, crushed, washed”（破碎并洗涤的石灰石）开始，生产纯“calcium carbonate, precipitated”（沉淀碳酸钙），简化了此前按顺序过程步骤建模的方式。在此系统中（v3.8–3.11 发布），化学中间产物不再单独计入，因此可在各过程阶段内部消费。例如，“limestone calcination”（石灰石煅烧）产生的二氧化碳可在“hydrated lime carbonization”（熟石灰碳酸化）中回用。这与典型工业过程配置不同，后者在石灰石煅烧时排放二氧化碳，再由技术圈输入二氧化碳供熟石灰碳酸化使用。此外，3.8 版更新热力和电力输入，将前版数据集的通用能源输入替换为以下[报告](https://www.eula.eu/wp-content/uploads/2019/02/A-Competitive-and-Efficient-Lime-Industry-Summary_0.pdf)的数值。但这些值反映每千克石灰石加工为生石灰的排放，而非每千克纯碳酸钙生产的排放。

为解决这些问题，将恢复 3.7.1 版清单结构，并更新相关输入和输出流表示。该数据将在 3.12 版发布。预计主要产品“calcium carbonate, precipitated”的 LCIA 结果值将显著变化，例如 GWP 结果值接近增至三倍；下游使用中的影响贡献变化较小，限于塑料回收和制浆造纸相关的部分产品组，例如 GWP 变化范围分别为 1–5% 和 1–16%。我们正在完善数据，为即将发布的版本作准备，感谢您的耐心等待。

使用 ecoinvent 3.8 至 3.11 版进行评价时，如果采用“calcium carbonate, precipitated”，或此产品在研究系统中占重要地位，建议使用 3.7.1 版 LCIA 结果值，或相应调整清单。

#### APOS 中中间交换的 ID 不唯一 <a href="#zh-b0111" id="zh-b0111"></a>

<strong>2025 年 3 月 19<sup>日</sup>：</strong>每个中间交换（IE）都有唯一 ID，在各系统模型完成链接时生成。但在“替代点分配”（Allocation at the point of Substitution，APOS）系统模型中，发现部分 IE 的 ID 不唯一。受影响的流如下：

· electricity, high voltage（高压电力）

· electricity, high voltage, aluminium industry（铝业高压电力）

· electricity, high voltage, renewable energy products（可再生能源产品高压电力）

此问题仅影响 ID 生成，不影响包含这些 IE 的数据集的任何结果值或清单。因此，即使存在重复 ID，仍建议有需要的用户使用包含这些流的数据集。

<strong>更新：2025 年 5 月 14<sup>日</sup>：</strong>此问题已解决，ecoQuery 上发布的数据集已更新。使用这些 ID 进行建模调整或识别的用户，建议联系支持团队获取更新 ID。

#### <strong>LCIA 问题</strong> <a href="#zh-b0118" id="zh-b0118"></a>

<strong>eutrophication: terrestrial（陆地富营养化）</strong>

“EN15804+A2 - Core impact categories and indicators”方法中“eutrophication: terrestrial”影响类别的单位应为“mol N-Eq”，而非“mol H+-Eq”。

<strong>ecotoxicity: freshwater（淡水生态毒性）</strong>

“USEtox v2.13, endpoint”方法中“ecotoxicity: freshwater”影响类别的单位应为“PDF.m3.day”，而非“PDF.m3.yr”。

<strong>“Methane, non-fossil”（非化石甲烷）和“Carbon monoxide, non-fossil”（非化石一氧化碳）</strong>

<em>EFv3.x EN15804</em> 方法实施中，“Methane, non-fossil”和“Carbon monoxide, non-fossil”的表征因子（CF）存在问题。虽然[方法网站](https://eplca.jrc.ec.europa.eu/LCDN/EN15804.html)仅提及生物源二氧化碳的差异，但以 -1/+1 CF 计入生物源二氧化碳会产生相关影响：IPCC 对生物源排放的 CF 低于化石排放，因为 a）其氧化（分解为二氧化碳）替代了此前已从大气清除的二氧化碳，且 b）“对于生物源甲烷，土壤吸收和部分氧化产物的清除相当于大气 CO2 的汇”（[IPCC 报告](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/#7.6.1.3)）。因此，如果表征生物源碳吸收和释放（如<em>EF v3.x EN15804</em> 方法），生物源甲烷排放的 CF（<em>EF v3.0 EN15804</em> 中还包括一氧化碳）就会高于采用 IPCC CF 的<em>EF v3.x</em> 方法。包含生物源 CO2 的 IPCC 2021 实施也存在同样问题。当前和正确实施如下：

<table>
<tbody>
<tr>
<td><p>基本流</p></td>
<td><p>EF v3.1</p></td>
<td><p>EF v3.1 EN15804</p></td>
<td><p>EF v3.0</p></td>
<td><p>EF v3.0 EN15804</p></td>
<td><p>IPCC 2021 excl. biogenic CO2（排除生物源 CO2）</p></td>
<td><p>IPCC 2021 incl. biogenic CO2（包含生物源 CO2）</p></td>
<td><p>IPCC 2021 excl. biogenic CO2, incl. SLCFs（排除生物源 CO2，包含 SLCF）</p></td>
<td><p>IPCC 2021 incl. biogenic CO2, Incl. SLCFs（包含生物源 CO2 和 SLCF）</p></td>
</tr>
<tr>
<td colspan="9"><p>当前实施</p></td>
</tr>
<tr>
<td><p>Carbon monoxide, non-fossil（非化石一氧化碳）</p></td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>2.491</p>
</td>
<td>
<p>2.491</p>
</td>
</tr>
<tr>
<td><p>Methane, non-fossil（非化石甲烷）</p></td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>34</p>
</td>
<td>
<p>34</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
</tr>
<tr>
<td colspan="9"><p>正确实施</p></td>
</tr>
<tr>
<td><p>Carbon monoxide, non-fossil（非化石一氧化碳）</p></td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>1.57</p>
</td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>2.491</p>
</td>
<td>
<p>4.0624</p>
</td>
</tr>
<tr>
<td><p>Methane, non-fossil（非化石甲烷）</p></td>
<td>
<p>27</p>
</td>
<td>
<p>29.8</p>
</td>
<td>
<p>34</p>
</td>
<td>
<p>36.8</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>29.8</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>29.8</p>
</td>
</tr>
</tbody>
</table>

感谢[GreenDelta](https://www.greendelta.com/about-us/team-2-2/) 的 Conrad Spindler 发现并解释此问题。

<strong>锂辉石</strong>

锂辉石（原文化学式：LiAl(SiO3)2）的锂含量为 0.0376。下列方法中，将锂的 CF 应用于锂辉石时，可将此值用作换算因子：  
  
\* CML v4.8 2016。  
\* Ecological Scarcity 2021。  
\* EPS 2020d，  
\* ReCiPe 2016。  
  
前三种方法尚未表征锂辉石；ReCiPe 2016 则错误地采用锂的 CF 和换算因子 1 进行表征。

#### <strong>澳大利亚谷物碳不平衡</strong> <a href="#zh-b0167" id="zh-b0167"></a>

澳大利亚不同地区多个谷物数据集因产品所含生物源碳的错误归属而出现碳不平衡。具体而言，该数值被误分配至“Carbon dioxide, land transformation”流，而正确流应为“Carbon dioxide, non-fossil”。

对于工作表 1 所列数据集，已更新“Carbon dioxide, non-fossil”基本流交换数量，以求得残留物燃烧产生的排放。对于工作表 2 所列数据集，已相应修正特定流的说明。

修正值列于下方电子表格，并将在 2026 年起的后续版本中实施。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[澳大利亚谷物碳不平衡修正](../assets/98e680a1ed50-Known-Issue-v3.12_Australian-Cereal-Carbon-Corrections.xlsx)

{% endtab %}

{% tab title="English 原文" %}

## Supporting our users with a broader spectrum of data, version 3.11 of the ecoinvent database creates new possibilities for the field of sustainability. This update features more than 2,066 new and 4,497 updated datasets. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.11 was released on November 19th, 2024</strong>. Discover how to [upgrade to our latest version](licensing.md).

<strong>ecoinvent v3.12 was released on November 5th, 2025.</strong> Discover how to [upgrade to our latest version](licensing.md).

September 24th, 2025

Version 3.11 introduces brilliant new updates to the following sectors: fuels, energy, chemicals and plastics, batteries, metals, building and construction, waste, agriculture, forestry, pulp and paper, and transport.

[![webinar-icon](../assets/9c37f83e3b0d-webinar-icon.png)](https://youtu.be/t4p2foRfwAQ)  [Watch the "Introduction to ecoinvent version 3.11" webinar](https://youtu.be/rlDdWB51Wfs)



![doc-icon](../assets/024d8f149226-doc-icon.png) [Download our answers to the 3.11 FAQs](../assets/c294d225037a-Webinar-introduction-to-ecoinvent-v3.11-FAQ.pdf)

![doc-icon](../assets/024d8f149226-doc-icon.png)  [Download our overview presentation covering all 3.11 updates](../assets/c29a5e16a923-Webinar-introduction-to-ecoinvent-v3.11.pdf)

### <strong>Sectorial Updates</strong> <a href="#en-b0010" id="en-b0010"></a>

#### <strong>Fuels</strong> <a href="#en-b0011" id="en-b0011"></a>

The new ecoinvent version 3.11 builds on the extensive oil and gas overhaul in versions [3.9.1](ecoinvent-version-3.9.1.md) (2022) and [3.10](ecoinvent-version-3.10.md) (2023). New or updated natural gas supplies at high pressure are provided for 57 countries, representing 88% of global gas consumption, based on the supply situation in 2023. Furthermore, the estimates for onshore/offshore pipeline transport and LNG shipping distances have been revised in v3.11 for improved regionalization. The supply mixes for crude petroleum oil in Switzerland, Europe without Switzerland, the Region of North America (RNA), Brazil (BR), Colombia (CO), India (IN), Peru (PE), and South Africa (ZA) are updated to reflect the trade situation in 2023. Based on the latest trade statistics for 2023, this update reflects the effect of shifts in the natural gas supply chain due to geopolitical developments in recent years, especially in the European market.

Additionally, version 3.11’s [fuels sector](fuels.md) includes updated supply chains for lignite and hard coal based on 2022 data, with revised methane emission factors for mining and updated production volumes. To enhance regionalization, hard coal mining activities have been expanded to include 4 new European geographies, while hard coal market activities now encompass 22 new geographies within Europe, as well as newly differentiated markets in Japan and South Korea. Several new hard coal import activities have also been added, providing a more accurate and detailed representation of global coal trade flows. Lastly, meta information has been updated, corrected, and harmonized across all hard coal and lignite datasets.

#### <strong>Energy</strong> <a href="#en-b0014" id="en-b0014"></a>

ecoinvent 3.11 updates the [energy sector’s](energy.md) electricity market mixes to reflect the situation in 2021. In the specific cases of Brazil, China, USA, Canada, and Switzerland the electricity mixes are updated to reflect the situation in 2022. India was updated to represent the fiscal year of April 2021/March 2022. All specific cases are based on national statistics, while the remaining countries are based on global statistics. Starting with version 3.11, the global statistics are based on statistics from the [enerdata](https://www.enerdata.net/) database. The residual mixes reflect the newest data from 2023.

Besides additional minor corrections, harmonization efforts were performed to update documentation and meta information of electricity markets, transformation, and import datasets.

#### <strong>Chemicals</strong> <a href="#en-b0017" id="en-b0017"></a>

The [chemicals sector](chemicals-and-plastics.md) in ecoinvent v3.11 is updated to improve the data representation for key chemical precursors, such as carbon monoxide, acetic acid and its esters, acrylic esters, cumene, nitrobenzene, 2,4-dinitrotoluene, aniline, phosgene, and bisphenol A. Hence, this dedicated supply chain enhancement improves the representation for various chemical and plastic derivatives, including isocyanates, polyurethanes, epoxy resins, and polycarbonates.

Furthermore, ecoinvent v3.11 replaces previously aggregated data for methyl chloride, methyl methacrylate, and polymethyl methacrylate from previous database versions with disaggregated unit processes to enable accurate linking to the ecoinvent background data.

Moreover, v3.11 introduces updated industry data covering the supply vinyl chloride and polyvinyl chloride production, provided by the [European Council of Vinyl Manufacturers](https://pvc.org/), and unsaturated polyester (UP) and epoxy vinyl ester (VE) resins, provided by the [European UP/VE Resins Association](https://www.upresins.org/). This includes (1) VE resins based on bisphenol A epoxy, and (2) UP resins based on dicyclopentadiene, isophthalic acid, maleic and o-phthalic acids, as well as recycled polyethylene terephthalate. Additionally, ecoinvent v3.11 features new data for composite manufacturing, provided by [Centre Technique Industriel, IPC](https://www.ct-ipc.com/), i.e., compression, molding, pultrusion, manual/hand processes, and filament winding processes, to expand the ecoinvent data coverage in this domain.

Finally, the chemicals sector in ecoinvent v3.11 builds on the work completed in preceding versions by updating existing data and expanding their geographical coverage whenever possible, as well as including 18 new products not previously covered. Specifically, ecoinvent v3.11 introduces data for selected chemicals in Asia either as aggregate regions or as individual countries and in the United States. These efforts will continue for future releases.

#### <strong>Batteries</strong> <a href="#en-b0022" id="en-b0022"></a>

The [batteries sector](batteries-electronics.md) has been updated with two new chemistries of Li-ion batteries: NMC532 (nickel cobalt manganese) and NMC622 for Chinese and Global geographies. The new datasets include the cathode active material precursor (NMC hydroxide), the cathode active material (NMC oxide), the cathode, the cell, and the battery pack. These are modeled following the same approach as the other Li-ion batteries in the database. A new activity for lithium titanate spinel was developed as an additional anode active material. Additionally, to support new battery technologies, a dataset for sodium-ion battery electrolyte was developed.

The production route for synthetic graphite production in the Chinese geography was updated based on a collaboration with [Tokai COBEX](https://tokaicobex.com/) and in line with a newly published paper. The production of natural graphite in China for battery application was also added to the database.

Finally, the batteries sector takes a step towards a comprehensive content update focused on market dataset updates and harmonization of the production volume of Li-ion battery components.

#### <strong>Metals</strong> <a href="#en-b0026" id="en-b0026"></a>

This update expands and improves the data coverage of the [metals sector](metals.md) with new and updated data. ecoinvent v3.11 introduces data on the production of grain-oriented electrical steel (GOES) in Europe and a related dataset on the production of a 3.2% silicon alloy steel used as feedstock in the production of GOES. Two datasets on gallium production in China are added: low-grade and high-grade (data provided by [EMPA](https://www.empa.ch/)). Improvements in the current coverage of the metals sector encompass a variety of aspects, namely the update of properties such as metal content and prices, the addition of missing exchanges, or their renaming. Prices were updated for approximately 60 metal products based on the ISE ([Institute of Rare Earths and Strategic Metals](https://en.institut-seltene-erden.de/)) database. Metal content properties were updated or added to more than 100 metal products. Mining datasets were updated with the integration of previously missing gangue exchanges, hence improving the impact assessment of those datasets. Finally, some metal scrap exchanges were renamed to improve clarity, enabling users to identify the relevant metal scrap exchange more easily.

#### <strong>Building and Construction</strong> <a href="#en-b0028" id="en-b0028"></a>

The v3.11 update brings rich enhancements to the [building and construction sector](building-and-construction.md) of the ecoinvent database, including a wealth of new data and several updates. New datasets for limestone extraction and primary crushing, clinker production, and cement manufacturing were developed through a collaboration with the [National Research Council of Canada (NRC)](https://nrc.canada.ca/en) and the [Cement Association of Canada (CAC)](http://www.cement.ca/). These datasets cover both average Canadian production (CA) and specific data for Ontario (CA-ON). Datasets about limestone extraction and crushing form the basis for subsequent datasets on clinker manufacturing, which share the same geographical scope. The clinker datasets, in turn, are used to create four additional datasets for general use (GU) and general use limestone (GUL) cement, in accordance with the CSA A3001 standard, while also referencing other relevant North American standards such as ASTM C150 and ASTM C595. Additionally, an internally developed dataset on integrated cement plants in Canada (CA) is introduced in v3.11, offering a comprehensive representation of the facilities and machinery used for manufacturing both clinker and cement mixes, covering all major stages of production.

Furthermore, several updates on existing datasets of the sector have been performed for v3.11. The supply chain of limestone and lime products has been revised, where the names and properties of the upstream activities and products have been modified, and the production volumes, and therefore the market shares, have been updated. Other updates include the revision of the production activities of lime mortar, cement mortar, concrete 50MPa, concrete block (several), limestone, hydraulic lime, quicklime, sand, gravel, glazing (double and triple), bitumen seal, shale brick, and thermal plaster.

#### <strong>Waste Management and Recycling</strong> <a href="#en-b0031" id="en-b0031"></a>

In version 3.11, the [waste sector](waste-management-and-recycling.md) is enhanced with various data additions and updates, covering a wide range of topics. The datasets modeling the treatment of municipal solid waste (MSW) in the 27 EU countries, Switzerland, Norway, Iceland, and the United Kingdom are now fully regionalized. They are based on customized elemental and fractional composition of waste being regionally generated, while each country has an updated, local technology treatment mix. The respective markets also employ regionalized transport distances and regionalized losses when needed.

Extensive changes are implemented also in the field of plastic recycling. New data is added to model mechanical recycling of waste plastic in Europe, in collaboration with [Plastics Recyclers Europe](https://www.plasticsrecyclers.eu/). The modeled polymers include waste polyethylene (PE), polyethylene/polypropylene (PE/PP), high-density polyethylene (HDPE), low-density polyethylene (LDPE), polystyrene (PS), polyethylene terephthalate (PET), polyvinylchloride (PVC), polypropylene (PP), acrylonitrile-butadiene-styrene (ABS), acrylonitrile-butadiene-styrene/ polystyrene (ABS/PS), and mixed plastics generated from many different sources like household, industrial, agricultural, commercial, construction and demolition, WEEE (waste electrical and electronic equipment), etc. On top of that, chemical recycling of waste polyester is modeled in China in collaboration with [Alibaba Cloud – Energy Experts](http://www.alibabacloud.com/en/product/energy-expert). Waste polyester is sourced from industrial activities of textile production and it is chemically treated into polyethylene terephthalate pellets. Another type of chemical recycling is incorporated by modeling hydrothermal treatment of waste mixed plastics in the United Kingdom. The data is provided by [Mura Technology](https://muratechnology.com/) in collaboration with the [University of Warwick](https://warwick.ac.uk/).

Moreover, two more treatment processes are added. The first covers the treatment of wastewater generated during textile production in Europe and global geography. The second represents the treatment of graphite tailings from mining operations of natural graphite in China. Finally, a harmonized nomenclature is applied to all waste and scrap metals to clarify the fate of metal by-products, for example, if the flow is treated via incineration, landfill, etc., or if it gets recycled to be reused.

#### <strong>Agriculture</strong> <a href="#en-b0035" id="en-b0035"></a>

In the [agriculture sector](agriculture-fishery-and-animal-husbandry.md), 3.11 unveils a comprehensive update on Swiss agricultural production, made possible by our close collaboration with [Agroscope](https://www.agroscope.admin.ch/agroscope/en/home.html). This release includes detailed datasets covering fruit-bearing trees like apple and pear, cereal grains such as barley, maize, wheat, and root, and cruciferous vegetables including carrots and cauliflower, as well as protein-rich legume crops like peas and fava beans. Conventional and organic farming methods are covered across Switzerland’s mountain, hill, and plain subregions, contributing to a total of 136 new datasets—providing deeper insights into Swiss farming.

#### <strong>Forestry and Wood</strong> <a href="#en-b0037" id="en-b0037"></a>

The updates in the [forestry and wood sector](forestry-and-wood.md) in 3.11 are focused on updating existing data and documentation, particularly the production volumes of forestry activities. Additionally, the sector was affected by biogenic carbon corrections which were performed on a database-wide scale.

#### <strong>Pulp and Paper</strong> <a href="#en-b0039" id="en-b0039"></a>

The [pulp and paper sector](pulp-and-paper.md) has been enhanced with the addition of three new datasets related to paper-based packaging for fast food applications. The activities model the production of various tableware, such as paper cups and lids, burger wraps, and fry boxes. The data was provided by [EPPA](https://eppa-eu.org/) (European Paper Packaging Alliance). Existing activities related to beverage carton converting, and kraft paper and paper sack production were updated with recent industry data. The data for beverage carton converting was provided by [ACE](https://www.beveragecarton.eu/) (The Alliance for Beverage Cartons and the Environment) and by [ifeu](https://www.ifeu.de/en/) (Institut für Energie- und Umweltforschung). The kraft paper-related data was provided by [CEPI Eurokraft and Eurosac](https://www.cepi-eurokraft.org/) in collaboration with [RISE](https://www.ri.se/en) (Research Institutes of Sweden).

#### <strong>Transport</strong> <a href="#en-b0041" id="en-b0041"></a>

The [transport sector](transport.md) in version 3.11 benefits from three main updates. The first update is of the circulating fleet of passenger cars in Europe and on a global scale, aiming to improve the representativeness of the circulating fleet. The second update aims to improve the clarity and accessibility of datasets. By adopting a standardized nomenclature for all transport datasets, it is possible to identify the differences between datasets more easily. The third update includes new datasets related to the maintenance of aircraft on a European and global scale. The datasets are based on flight and maintenance schedules tailored for the different haulage that each dataset has.

### <strong>LCIA Methods Updates</strong> <a href="#en-b0043" id="en-b0043"></a>

For version 3.11, non-fossil carbon flows were updated and balanced with special attention to biogenic carbon uptake. This allows characterizing non-fossil carbon dioxide with -1/+1 for removals/releases when assessing climate change impacts following IPCC, which is demanded by some standards and guidelines such as ISO 14067. The implementation of this was done by introducing a complementary method (“IPCC 2021 (incl. biogenic CO2)”) to the existing one (“IPCC 2021”). Impact categories from the two methods can be mapped to standards and guidelines.

![doc-icon](../assets/024d8f149226-doc-icon.png) See the [Guidance on IPCC Methods](guidance-on-ipcc-methods.md)

Furthermore, the EN15804 impact assessment was restructured and renamed to be closer to the nomenclature in the standard. This will help users find the right indicator.

### <strong>Relevant Documents and Files</strong> <a href="#en-b0047" id="en-b0047"></a>

#### <strong>Report of Changes</strong> <a href="#en-b0048" id="en-b0048"></a>

This report covers all changes made in the ecoinvent database between version 3.10 (2023) and 3.11 (2024). It reflects both database-wide changes, as well as sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Report of Changes](../assets/b05ee1a65d32-Change-Report-v3.11.pdf)

#### <strong>Correspondence File </strong> <a href="#en-b0051" id="en-b0051"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.10 and 3.11 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Correspondence File (3.10 to 3.11)](../assets/c827eab44ad7-Correspondence-File-v3.10---v.3.11.xlsx)

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Correspondence File (3.10.1 to 3.11)](../assets/8b779e1f37c9-Correspondence-File-v3.10.1---v.3.11.xlsx)

#### <strong>Database Overview File</strong> <a href="#en-b0055" id="en-b0055"></a>

The database overview file describes the contents of the database. The following information is contained in the file:

- <strong>Activity Overview(s)</strong>

The lists of datasets contained in each of the four system models, including the list of unlinked and unallocated datasets.

- <strong>ecoinvent Geographies</strong>

The geographies used in the ecoinvent database. Each geography is assigned a classification, and the geographies contained in each geography are indicated.

- <strong>LCIA Methods</strong>

The list of the LCIA methods for which ecoinvent calculates impact scores. The version of the methods is indicated, and the original source used for defining the characterization factors is provided. 

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Database Overview File](../assets/066ac4ecf765-Database-Overview-for-ecoinvent-v3.11-6-.xlsx)

#### <strong>LCIA Implementation Report</strong> <a href="#en-b0064" id="en-b0064"></a>

The LCIA implementation report documents the implementation of LCIA methods for version 3.11.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [LCIA Implementation Report](../assets/957bf4cc0635-LCIA-implementation-3.11.pdf)

### 3.11 Data Providers <a href="#en-b0067" id="en-b0067"></a>

- [Agroscope](https://www.agroscope.admin.ch/agroscope/en/home.html)
- [Alibaba Cloud – Energy Experts](http://www.alibabacloud.com/en/product/energy-expert)
- [Alliance for Beverage Cartons and the Environment (ACE)](https://www.beveragecarton.eu/)
- [CEPI Eurokraft and Eurosac](https://www.cepi-eurokraft.org/) (in collaboration with [RISE (Research Institutes of Sweden))](https://www.ri.se/en)
- [Cement Association of Canada (CAC)](http://www.cement.ca/)
- [Centre Technique Industriel, IPC](https://www.ct-ipc.com/)
- [Climate TRACE](https://climatetrace.org/)
- [EMPA](https://www.empa.ch/)
- [enerdata](https://www.enerdata.net/)
- [ESU-services Ltd.](https://esu-services.ch/)
- [European Council of Vinyl Manufacturers](https://pvc.org/)
- [European Paper Packaging Alliance (EPPA)](https://eppa-eu.org/)
- [European UP/VE Resins Association](https://www.upresins.org/)
- [German Aerospace Center (DLR)](https://www.dlr.de/en)
- [ifeu (Institut für Energie- und Umweltforschung)](https://www.ifeu.de/en/)
- [Institute of Rare Earths and Strategic Metals](https://en.institut-seltene-erden.de/)
- [Joint Research Center (JRC)](https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/joint-research-centre_en)
- [Mura Technology](https://muratechnology.com/) (in collaboration with the [University of Warwick)](https://warwick.ac.uk/)
- [National Research Council of Canada (NRC)](https://nrc.canada.ca/en)
- [Plastics Recyclers Europe](https://www.plasticsrecyclers.eu/)
- [Tokai COBEX](https://tokaicobex.com/)

### <strong>Known Issues</strong> <a href="#en-b0089" id="en-b0089"></a>

This section lists all known data errors in version 3.11 of the ecoinvent database.

#### Datasets: printed wiring board production, for surface mounting <a href="#en-b0091" id="en-b0091"></a>

- <em>printed wiring board production, for surface mounting, Pb containing surface</em>
- <em>printed wiring board production, for surface mounting, Pb free surface</em>

<strong>This issue was identified in version 3.11 of the ecoinvent database.</strong>

For these two datasets, changes were incorrectly applied in version 3.8 and resulted in an underestimation of the quantities of almost all exchanges within these two datasets.

To address this issue, the original sources cited in the version 2 report were analyzed again, and values were corrected. Compared to scores of v3.11, the changes will increase the GWP scores by more than around 100 %. Other impact categories are also affected (e.g., ADP), with some score increase expected, ranging from 100 % to 250%.

Note that these datasets are also used in the following datasets and could subsequently affect their scores:

- printed wiring board production, mounted mainboard, laptop computer, Pb free, GLO
- printed wiring board production, mounted mainboard, desktop computer, Pb free, GLO
- printed wiring board production, surface mounted, unspecified, Pb free, GLO
- computer production, desktop, without screen, GLO
- printed wiring board production, mounted mainboard, desktop computer, Pb containing, GLO
- printed wiring board production, surface mounted, unspecified, Pb containing, GLO
- printed wiring board production, mounted mainboard, laptop computer, Pb containing, GLO”

#### <strong>Dataset: calcium carbonate production, precipitated</strong> <a href="#en-b0105" id="en-b0105"></a>

<strong>We want to inform you of the following issue identified in version 3.11 of the ecoinvent database:</strong>

For this dataset, changes made in version 3.8 resulted in an unintended issue that is discussed next.

Since version 3.8, the inventory of precipitated calcium carbonate production accounts for the inputs and outputs of an aggregated system—starting with “limestone, crushed, washed” to produce pure “calcium carbonate, precipitated”—which simplified the previous modeling of sequential process steps. In this system (i.e., published in v3.8 – 3.11), chemical intermediates are no longer accounted separately, and thus, could be consumed internally at various process stages. For example, carbon dioxide generated during “limestone calcination” could be reused in the “hydrated lime carbonization”. This contrasts typical industrial process configurations, where carbon dioxide is emitted during the “limestone calcination” and then consumed as an input from the technosphere for the “hydrated lime carbonization”. Furthermore, the inputs for heat and electricity were updated for version 3.8: generic energy inputs in the previous version of the datasets were replaced with values from the following [report](https://www.eula.eu/wp-content/uploads/2019/02/A-Competitive-and-Efficient-Lime-Industry-Summary_0.pdf). These values, however, reflect emissions per kilogram of limestone processed into quicklime, not per kilogram of pure calcium carbonate produced.

To address these issues, a rollback to the version 3.7.1 inventory structure will be implemented, along with an updated representation of relevant input and output flows. This data will be published in version 3.12. Significant changes in LCIA scores are expected for the main product “calcium carbonate, precipitated” (e.g., a nearly threefold increase in the GWP score), while the change in impact contribution in downstream uses are minor and limited to certain product groups related to plastic recycling and pulp & paper production—for example, GWP changes are in the range of 1–5% and 1–16%, respectively. We appreciate your patience as we work to refine and prepare the data for the upcoming release.

If ecoinvent users conduct an assessment using “calcium carbonate, precipitated”—or if this product plays a significant role in the system under study—while using ecoinvent versions 3.8 to 3.11, we recommend using LCIA scores from version 3.7.1 or adapting its inventory accordingly.

#### Non-unique IDs of intermediate exchanges in APOS <a href="#en-b0111" id="en-b0111"></a>

<strong>19<sup>th</sup> March 2025: </strong>Each Intermediate Exchange (IE) has a unique ID that is generated in each system model once linking is performed. However, in the system model of “Allocation at the point of Substitution” (APOS), some IEs were identified to have non-unique IDs. The affected flows are the following:

·         electricity, high voltage

·         electricity, high voltage, aluminium industry

·         electricity, high voltage, renewable energy products

This issue impacts only the generation of IDs and does not affect any of the scores or the inventories of the datasets including these IEs. Therefore, users are still encouraged to leverage datasets including the affected flows if they wish, even though they have duplicate IDs.

<strong>UPDATE 14<sup>th</sup> May 2025: </strong>This issue has been resolved, and the published datasets on ecoQuery have been updated. Users implementing these IDs for any modeling adaptation and identification purposes are encouraged to contact our support team and ask to be provided with the updated IDs.

#### <strong>LCIA Issues</strong> <a href="#en-b0118" id="en-b0118"></a>

<strong>eutrophication: terrestrial</strong>

The unit for the impact category “eutrophication: terrestrial” in the method “EN15804+A2 - Core impact categories and indicators” should be “mol N-Eq” instead of “mol H+-Eq”.

<strong>ecotoxicity: freshwater</strong>

The unit for the impact category “ecotoxicity: freshwater” in the “USEtox v2.13, endpoint” methods should be “PDF.m3.day” instead of “PDF.m3.yr”.

<strong>“Methane, non-fossil” and “Carbon monoxide, non-fossil”</strong>

There is an issue with characterization factors (CFs) for “Methane, non-fossil” and “Carbon monoxide, non-fossil” in the <em>EFv3.x EN15804</em> method implementations. While the [method website](https://eplca.jrc.ec.europa.eu/LCDN/EN15804.html) only mentions differences for biogenic carbon dioxide, accounting for it with -1/+1 CFs has consequences: IPCC CFs are lower for biogenic emissions (compared to fossil ones) because a) oxidation (decay into carbon dioxide) replaces carbon dioxide that has been removed from the atmosphere and b) “for biogenic methane the soil uptake and removal of partially oxidized products is equivalent to a sink of atmospheric CO2” ([IPCC report](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/#7.6.1.3)). Accordingly, if biogenic carbon uptake and release is characterized (as in <em>EF v3.x EN15804</em> methods), CFs for biogenic methane (and in case <em>of EF v3.0 EN15804</em> also carbon monoxide) emissions are higher than in the <em>EF v3.x</em> methods, which use IPCC CFs. The same issue exists for the IPCC 2021 implementations, including biogenic CO2. This is how the current and the correct implementation would look:

<table>
<tbody>
<tr>
<td>
<p>Elementary flow</p>
</td>
<td>
<p>EF v3.1</p>
</td>
<td>
<p>EF v3.1 EN15804</p>
</td>
<td>
<p>EF v3.0</p>
</td>
<td>
<p>EF v3.0 EN15804</p>
</td>
<td>
<p>IPCC 2021 excl. biogenic CO2</p>
</td>
<td>
<p>IPCC 2021 incl. biogenic CO2</p>
</td>
<td>
<p>IPCC 2021 excl. biogenic CO2, incl. SLCFs</p>
</td>
<td>
<p>IPCC 2021 incl. biogenic CO2, Incl. SLCFs</p>
</td>
</tr>
<tr>
<td colspan="9">
<p>Current implementation</p>
</td>
</tr>
<tr>
<td>
<p>Carbon monoxide, non-fossil</p>
</td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>0</p>
</td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>2.491</p>
</td>
<td>
<p>2.491</p>
</td>
</tr>
<tr>
<td>
<p>Methane, non-fossil</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>34</p>
</td>
<td>
<p>34</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>27</p>
</td>
</tr>
<tr>
<td colspan="9">
<p>Correct implementation</p>
</td>
</tr>
<tr>
<td>
<p>Carbon monoxide, non-fossil</p>
</td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>0</p>
</td>
<td>
<p>1.57</p>
</td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>2.491</p>
</td>
<td>
<p>4.0624</p>
</td>
</tr>
<tr>
<td>
<p>Methane, non-fossil</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>29.8</p>
</td>
<td>
<p>34</p>
</td>
<td>
<p>36.8</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>29.8</p>
</td>
<td>
<p>27</p>
</td>
<td>
<p>29.8</p>
</td>
</tr>
</tbody>
</table>

 Thanks to Conrad Spindler from [GreenDelta](https://www.greendelta.com/about-us/team-2-2/) for noticing and explaining.

<strong>Spodumene</strong>

Spodumene (LiAl(SiO3)2 has a Lithium content of 0.0376. This value can be used as a conversion factor when applying the CF of Lithium to Spodumene in the following methods:  
  
\* CML v4.8 2016.  
\* Ecological Scarcity 2021.  
\* EPS 2020d,  
\* ReCiPe 2016.  
  
In the first three methods, Spodumene is not yet characterized; in ReCiPe 2016, it was wrongly characterized with the CF for Lithium (and a conversion factor of 1).

#### <strong>Australian Cereal Carbon Imbalance</strong> <a href="#en-b0167" id="en-b0167"></a>

In several Australian cereal datasets across different regions, a carbon imbalance was identified due to the incorrect assignment of embodied biogenic carbon. Specifically, the value was mistakenly allocated to the flow "Carbon dioxide, land transformation" instead of the correct flow "Carbon dioxide, non-fossil".

For the datasets reported in sheet 1, the amount of the elementary exchange "Carbon dioxide, non-fossil" has been updated to derive the emissions from burning residues. For the datasets reported in sheet 2, the comments for specific flows have been corrected accordingly.

The corrected values are provided in the spreadsheet below and will be implemented in future releases from 2026 onwards.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Australian Cereal Carbon Imbalance Corrections](../assets/98e680a1ed50-Known-Issue-v3.12_Australian-Cereal-Carbon-Corrections.xlsx)

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0109**：原文 threefold increase 可能指结果变为约三倍，也可能被解读为增加约三倍（变为四倍）；上下文通常采用前者，译文采取“增至三倍”表述。 对照原始修正清单或向数据开发者确认该倍数指终值倍数还是增量倍数。 [查看完整记录](../review/issues.md#issue-041)
- **待专家复核 · b0023**：原文括号元素次序为 nickel cobalt manganese，而 NMC 常用展开次序为 nickel manganese cobalt；NMC532 的元素比例不可依据这处括号顺序重新解释。 请根据实际正极材料化学式核对元素次序与比例，原文和译文目前保留原括号说法。 [查看完整记录](../review/issues.md#issue-042)
- **已处理／已说明 · b0033**：原文只给出 Alibaba Cloud – Energy Experts，未提供“能耗宝”中文品牌名；保留英文品牌，避免未经核实的名称对应。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-043)
- **已处理／已说明 · b0069**：原文只给出 Alibaba Cloud – Energy Experts，未提供“能耗宝”中文品牌名；保留英文品牌，避免未经核实的名称对应。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-044)
