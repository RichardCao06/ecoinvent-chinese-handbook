# 电池与电子产品

英文原题：Batteries and Electronics  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/batteries-electronics)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-12-15

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库的电池与电子产品部门包含 600 多个数据集，涵盖多种电池技术及组件的生产。 <a href="#zh-b0002" id="zh-b0002"></a>

2025年11月13日

这一部门与[金属](metals.md)、[化学品](chemicals-and-plastics.md)、[电力](energy.md)和[基础设施](infrastructures.md)部门有大量交叉。

电池广泛应用于笔记本电脑、台式计算机、电动自行车和电动汽车等领域。电池在固定式应用中也发挥着关键作用，例如支持电网运行，以及在离网场景中与可再生能源结合使用。电池市场正在快速增长，中国电动汽车销量的激增是主要推动因素。根据国际能源署《2024 年全球电动汽车展望》（[IEA, 2024](https://www.iea.org/reports/global-ev-outlook-2024)），2023 年锂离子电池需求达到 750 GWh，中国占电动汽车销量的 60%。

尽管电池通常被视为缓解气候变化的解决方案之一，但其生产可能造成环境损害。制造电池及其组件需要多种金属，而这些金属的开采可能产生严重的环境后果。此外，生产过程可能需要消耗大量能源，因此其整体可持续性受到关注。

### 部门概览 <a href="#zh-b0007" id="zh-b0007"></a>

电池与电子产品部门包含多种电池技术，覆盖完整供应链：从各类化学品和金属，到正极、负极、电芯和电池包的组装。用户可利用众多原材料数据，对其他类型电池建模，或调整现有电池模型。本部门多数数据集覆盖全球（GLO）和中国（CN）；部分特定数据集覆盖美国（US）、东亚（UN-EASIA）和欧洲（RER）。

### 部门亮点 <a href="#zh-b0009" id="zh-b0009"></a>

电池与电子产品部门涵盖多种电池技术，包括 NMC622（镍锰钴）、NMC532、NMC111、NMC811、NCA（镍钴铝）、LFP（磷酸铁锂）和 LMO（锰酸锂）等锂离子电池，以及铅酸电池、钠离子电池和镍氢电池。

数据库提供整个价值链的数据，包括正极活性材料（CAM）前驱体、CAM、集流体、负极活性材料（AAM）前驱体、AAM、电池管理系统（BMS）、电解液和隔膜等组件。这些组件通过组装形成正极、负极、电芯和电池包。此外，用户还可获取生产电解液所需盐类和溶剂的数据。

数据库提供多种负极活性材料，包括天然石墨、人造石墨和尖晶石型钛酸锂（LTO）。负极生产使用的是按一定比例混合的人造石墨和天然石墨。请注意，用户可以修改清单，在负极生产中采用不同的天然石墨／人造石墨比例，或使用尖晶石型钛酸锂。

### 数据提供者 <a href="#zh-b0013" id="zh-b0013"></a>

- [Empa](https://www.empa.ch/)

- [Tokai COBEX](https://tokaicobex.com/)

- [蒙特利尔理工学院（Polytechnique Montréal）](https://www.polymtl.ca/)

### 编辑 <a href="#zh-b0017" id="zh-b0017"></a>

- Jens Peters，RyC 研究教授，阿尔卡拉大学，马德里
- Ketan Vaidya，首席执行官，Verdatir AB，斯德哥尔摩
- Robert Istrate，工业生态学助理教授，莱顿大学

### 相关文献 <a href="#zh-b0021" id="zh-b0021"></a>

da Silva Lima, L., Wu, J., Cadena, E., Groombridge, A. S., & Dewulf, J. (2023). Towards environmentally sustainable battery anode materials: Life cycle assessment of mixed niobium oxide (XNOTM) and lithium-titanium-oxide (LTO)（迈向环境可持续的电池负极材料：混合氧化铌（XNOTM）和钛酸锂（LTO）的生命周期评价）. Sustainable Materials and Technologies, 37, e00654. <https://doi.org/10.1016/j.susmat.2023.e00654>

Dai, Q., Kelly, J. C., Gaines, L., & Wang, M. (2019). Life Cycle Analysis of Lithium-Ion Batteries for Automotive Applications（车用锂离子电池的生命周期分析）. Batteries, 5(2), 48. <https://doi.org/10.3390/batteries5020048>

Carrère, T., Khalid, U., Baumann, M., Bouzidi, M., & Allard, B. (2024). Carbon footprint assessment of manufacturing of synthetic graphite battery anode material for electric mobility applications（电动交通应用中人造石墨电池负极材料制造的碳足迹评价）. <em>Journal of Energy Storage</em>, <em>94</em>, 112356. <https://doi.org/10.1016/j.est.2024.112356>

{% endtab %}

{% tab title="English 原文" %}

## The batteries and electronics sector in the ecoinvent database comprises over 600 datasets, covering the production of various battery technologies and components. <a href="#en-b0002" id="en-b0002"></a>

13th November 2025

This sector overlaps significantly with the [metals](metals.md), [chemicals](chemicals-and-plastics.md), [electricity](energy.md), and [infrastructure](infrastructures.md) sectors.

Batteries are utilized in a wide range of applications, from laptops and computers to e-bikes and electric vehicles. They also play a crucial role in stationary applications, such as grid support and integration with renewable energy sources in off-grid settings. The market for batteries is experiencing rapid growth, particularly driven by the surge in electric vehicle sales in China. According to the Global EV Outlook 2024 by the International Energy Agency ([IEA, 2024](https://www.iea.org/reports/global-ev-outlook-2024)), the demand for Li-ion batteries reached 750 GWh in 2023, with China accounting for 60% of electric vehicle sales.

While batteries are often viewed as part of the solution to mitigate climate change, their production can lead to environmental damage. Manufacturing batteries and their components involves various metals, the mining of which can have severe environmental consequences. Additionally, the production processes can be energy-intensive, raising concerns about their overall sustainability.

### Sector Overview <a href="#en-b0007" id="en-b0007"></a>

The batteries and electronics sector comprises several technologies of batteries and covers the complete supply chain: from various chemicals and metals to the assembly of the cathode, anode, cell, and pack. Many raw materials are available to users to also model other types of batteries or adapt existing ones. The geographies covered in the sector are Global (GLO), and China (CN) for most of the datasets. The United States (US), East Asia (UN-EASIA), and Europe (RER) are covered for a few specific datasets.

### Sector Highlights <a href="#en-b0009" id="en-b0009"></a>

The batteries and electronics sector encompasses a variety of battery technologies, including lithium-ion types such as NMC622 (nickel manganese cobalt), NMC532, NMC111, NMC811, NCA (nickel cobalt aluminium), LFP (lithium iron phosphate), and LMO (lithium manganese oxide), as well as lead-acid, sodium-ion, and nickel-metal hybrid batteries.

The entire value chain is available and includes components like Cathode Active Material (CAM) precursors, CAMs, current collectors, Anode Active Material (AAM) precursors, AAMs, Battery Management System (BMS), electrolytes, and separators, which are assembled to create the cathode, anode, cell, and battery pack. Additionally, the necessary salts and solvents for producing electrolytes are available to users.

Several anode-active materials are available, including natural graphite, synthetic graphite, and lithium titanate spinel (LTO). Graphite (mix share of synthetic and natural) is then used in the anode production. Note that the user can choose to modify the inventories to include a different share of natural/synthetic graphite or lithium titanate spinel in the anode production.

### Data Providers <a href="#en-b0013" id="en-b0013"></a>

- [Empa](https://www.empa.ch/)

- [Tokai COBEX](https://tokaicobex.com/)

- [Polytechnique Montréal](https://www.polymtl.ca/)

### Editors <a href="#en-b0017" id="en-b0017"></a>

- Jens Peters, RyC Research Professor, University of Alcalá, Madrid
- Ketan Vaidya, Chief Executive Officer, Verdatir AB, Stockholm
- Robert Istrate, Assistant Professor of Industrial Ecology, Leiden University

### Relevant sources <a href="#en-b0021" id="en-b0021"></a>

da Silva Lima, L., Wu, J., Cadena, E., Groombridge, A. S., & Dewulf, J. (2023). Towards environmentally sustainable battery anode materials: Life cycle assessment of mixed niobium oxide (XNOTM) and lithium-titanium-oxide (LTO). Sustainable Materials and Technologies, 37, e00654. <https://doi.org/10.1016/j.susmat.2023.e00654>

Dai, Q., Kelly, J. C., Gaines, L., & Wang, M. (2019). Life Cycle Analysis of Lithium-Ion Batteries for Automotive Applications. Batteries, 5(2), 48. <https://doi.org/10.3390/batteries5020048>

Carrère, T., Khalid, U., Baumann, M., Bouzidi, M., & Allard, B. (2024). Carbon footprint assessment of manufacturing of synthetic graphite battery anode material for electric mobility applications. <em>Journal of Energy Storage</em>, <em>94</em>, 112356. <https://doi.org/10.1016/j.est.2024.112356>

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0010**：原文写作 nickel-metal hybrid，通常电池类别应为 nickel-metal hydride（镍氢）。依据上下文采用镍氢电池，需确认原文技术名称。 请技术专家核实该类电池名称及原文笔误。 [查看完整记录](../review/issues.md#issue-005)
