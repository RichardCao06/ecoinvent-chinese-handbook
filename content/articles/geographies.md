# 地理区域

英文原题：Geographies  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/geographies)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2026-03-12

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库中的每项活动均具有地理位置。 <a href="#zh-b0002" id="zh-b0002"></a>

2023 年 10 月 24 日

地理位置采用国际通用缩写表示。例如，瑞士的缩写为 CH，捷克为 CZ，中国为 CN。

![doc-icon](../assets/024d8f149226-doc-icon.png)请参阅[数据库概览文件](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)，获取全部活动及其地理区域的列表。同一文件还提供全部地理区域的列表。

有关地理区域如何创建和处理的更多信息，请参阅[此处](https://geography.ecoinvent.org/)。

作为背景数据库，我们旨在覆盖所选产品或服务最相关地理区域内的活动。地理覆盖取决于数据质量和可用性。因此，数据库中几乎每项活动也都在全球层面有所表示，采用全球（GLO）或世界其他地区（RoW）作为地理位置，以代表全球平均生产情况。当 ecoinvent 数据库未包含所需位置时，也可以使用这些地理位置。

### 地理分辨率 <a href="#zh-b0008" id="zh-b0008"></a>

[活动](activities-products.md)可以不同的地理分辨率提供，例如州、国家和洲。根据行业需求和各国特点，地理区域会作相应划分，以更好地反映实际情况。

例如，在电力行业，较大的国家（如美国、巴西、中国和印度）会划分为多个电网。因此，地理区域的定义旨在满足行业需求。

同一活动的地理区域不能重叠。例如，瑞士的一项活动不能与欧洲（RER）层面的同一活动同时存在，因为瑞士属于 RER。因此，会创建“欧洲，不包括瑞士”等地理区域。完全重叠和部分重叠情况会在地理区域文件中列出。

### 全球和世界其他地区的活动 <a href="#zh-b0012" id="zh-b0012"></a>

对于 ecoinvent 数据库中的大多数过程，会创建全球数据集以覆盖全球平均生产情况。理想情况下，会依据国际数据单独创建这一全球数据集，以准确反映全球平均条件。当无法获得全球平均生产数据时，全球数据集会根据多个本地数据集按生产量加权平均而创建，或通过复制本地数据集进行外推而创建。这类外推数据集的不确定性信息会相应调整。

如果同一活动同时存在全球数据集和更局部的数据集，则在[链接](glossary-l.md)后，即选择[系统模型](system-models.md)时，会创建 RoW 活动。RoW 代表从全世界剔除数据库中已有相应过程的所有局部地理区域后剩余的地区。因此，数据库中不同过程的 RoW 各不相同。当局部地理区域被加入数据库或从中删除时，同一过程的 RoW 也可能随数据库版本变化。当 RoW 参考产品的生产量低于全球数据集生产量的 0.5% 时，不生成 RoW 数据集；也就是说，当区域活动覆盖全部全球生产时，无需 RoW。

### 世界其他地区的计算示例 <a href="#zh-b0015" id="zh-b0015"></a>

假设某一活动在四个不同地区均有数据：美国（US）、印度（IN）、中国（CN）和全球（GLO）。

链接期间，通过复制全球数据集生成 RoW 生产活动。RoW 活动的生产量（PV）通过从全球生产量中减去各区域活动的生产量来计算：

PV RoW = PV GLO – PV US – PV IN – PV CN

在供应链中，新生成的 RoW 过程会与地理边界有重叠的其他过程连接。

<strong>编辑</strong>

<strong>Chris Mutel</strong>（主编），ecoinvent，瑞士

{% endtab %}

{% tab title="English 原文" %}

## Each activity present in the ecoinvent database has a geographic location. <a href="#en-b0002" id="en-b0002"></a>

Oct 24th, 2023

Geographic locations are reported using internationally accepted abbreviations. For example, Switzerland has the abbreviation CH, Czechia is CZ, and China is CN.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See the [database overview file](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx) for a full list of activities and their geographies. The list of all geographies is available in the same file.

To learn more about how geographies are created and processed, see [here](https://geography.ecoinvent.org/).

As a background database, the aim is to cover activities in the most relevant geographies for the selected product/service. Geography coverage is dependent on data quality and availability. Thus, almost every activity in the database is also represented at the global level, using geographical location global (GLO) or Rest-of-the-World (RoW), representing the average global production. These geographical locations can also be used in the case a desired location is not present in the ecoinvent database.

### Geographical Resolution <a href="#en-b0008" id="en-b0008"></a>

[Activities](activities-products.md) may be available with different geographical resolutions, e.g., state, country, and continent. Depending on the needs of the sector and the peculiarities of a country, geographies are shaped to better represent reality.

For electricity, for example, larger countries (e.g., the United States, Brazil, China, and India) are split into grids. Geography is therefore defined to meet the needs of the sector.

Geographies for the same activity cannot overlap. For example, an activity from Switzerland cannot coexist with the same activity at the European (RER) level since Switzerland is contained within RER. Therefore, geographies such as “Europe without Switzerland” are created. Full and partial overlaps are reported in the geography file.

### Global and Rest-of-the-World Activities <a href="#en-b0012" id="en-b0012"></a>

For the majority of processes in the ecoinvent database, a global dataset is created to cover the average global production. Ideally, this global dataset is created individually to accurately reflect the global average conditions based on international data. In cases where data on the average global production are not available, the global dataset is created as the weighted average (by production volume) of several local datasets, or it is extrapolated as a copy of a local dataset. The uncertainty information in such extrapolated datasets is adjusted accordingly.

If, for the same activity, both a global and a more local dataset exist, a RoW activity is created after [linking,](glossary-l.md) i.e., when a [system model](system-models.md) is selected. RoW represents the world minus all local geographies for which a process exists in the database. Thus, the RoW is different for different processes in the database. It may also change for the same process between versions of the database, i.e., when a local geography is added to, or removed from the database. The RoW dataset is not generated if the production volume of the reference product is &lt;0.5% of the production volume of the global dataset, i.e., if the regional activities cover all global production, RoW is not needed.

### Example Calculation of the Rest-of-the-World <a href="#en-b0015" id="en-b0015"></a>

Let us assume an activity is available for four different regions: the United States (US), India (IN), China (CN), and Global (GLO).

During the linking, the RoW production is generated as a copy of the global dataset. The production volume (PV) of the RoW activity is calculated by subtracting the production volume of the regional activities from the global volume:

PV RoW = PV GLO – PV US – PV IN – PV CN

In supply chains, the newly generated RoW process connects to other processes with overlapping geographical boundaries.

<strong>Editors </strong>

<strong>Chris Mutel </strong>(Main Editor), ecoinvent, Switzerland

{% endtab %}

{% endtabs %}
