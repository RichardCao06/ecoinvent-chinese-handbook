# ecoinvent 第 3.7 版和第 3.7.1 版

英文原题：ecoinvent Version 3.7 and 3.7.1  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.7)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库第 3.7 版于 2020 年 9 月发布，包含 900 多个新增和 1,000 个更新数据集。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.7 于 2020 年 9 月 17 日发布。</strong>

<strong>ecoinvent v3.7.1 于 2020 年 12 月 17 日发布。</strong>了解如何[升级至我们的最新版本](licensing.md)。

2023 年 10 月 27 日

为修正铁烧结生产数据集的重大错误，它被 ecoinvent v3.7.1 取代。

ecoinvent v3.7 通过 900 多个新增和 1,000 个更新数据集拓展数据范围，其中包含 100 多种新产品。此次更新扩展金属、肥料、林业与木材、包装材料、废物／回收及沼气供应链等多个部门的覆盖范围，也更新了电力市场组合。

第 3.7 版的更新和新增内容来自 ecoinvent 协会参与的各类项目及合作，包括瑞士联邦环境署 BAFU 资助的林业与木材部门全面修订和金属部门更新。其他更新来自与全球不同行业协会的合作。具体而言，ecoinvent 第 3.7 版纳入钴业协会和加拿大铝业协会提供的不同金属产品更新数据，以及 Eurosac、CEPI Eurokraft、Pro-Carton 和 ECMA 欧洲纸盒制造商协会提供的包装材料更新数据。肥料部门的合作方包括 Yara International ASA 和 Fertlizers Europe。

#### 重大问题 <a href="#zh-b0009" id="zh-b0009"></a>

已确认 ecoinvent v3.7 包含一个影响显著的问题。具体而言，铁烧结生产数据集估算的二噁英和颗粒物（PM）排放存在数量级错误。此错误使采用多数方法的人体健康和生态毒性指标计算的数据库结果失真。

所有其他影响类别，包括气候变化、水耗竭、累积能源需求、土地利用和土地利用变化、化石资源耗竭、酸化、富营养化、电离辐射、可再生资源、平流层臭氧消耗、光化学氧化剂形成、放射性物质和臭氧层消耗，均不受这些问题影响。

已提供关于该问题的[技术报告](../assets/7da8bd6a5b33-technical-report_v3-7-1_20201217.pdf)。

### ecoinvent 第 3.7.1 版 <a href="#zh-b0013" id="zh-b0013"></a>

为修正铁烧结生产数据集，ecoinvent v3.7.1 于 2020 年 12 月发布。

ecoinvent v3.7.1 重点修正铁烧结生产数据集。

借此机会，锌矿开采数据集也使用国际锌业协会在 ecoinvent v3.7 发布后提交的较新数据进行了更新。预计此次更新将显著改善数据库质量。较新数据解决该数据集此前建模的黄金开采量过高问题，并影响采用多数方法的矿物资源耗竭指标计算的数据库结果。此外，ecoinvent v3.7 的内容还有进一步更新或变更。

请注意：基于其他影响类别的研究和项目，包括气候变化、水耗竭、累积能源需求、土地利用和土地利用变化、化石资源耗竭、酸化、富营养化、电离辐射、可再生资源、平流层臭氧消耗、光化学氧化剂形成、放射性物质和臭氧层消耗，完全不受该问题影响。

### 新增及更新数据 <a href="#zh-b0018" id="zh-b0018"></a>

#### 金属 <a href="#zh-b0019" id="zh-b0019"></a>

金属部门增加并更新铜、镍、铁和钢，以及钴、稀土、钨和铍等稀缺金属的数据。数据贡献方包括 EMPA（由瑞士联邦环境署 BAFU 资助）、钴业协会和格拉茨工业大学（TU Graz）。北美铝数据集也根据加拿大铝业协会提供的数据修订。

#### 肥料 <a href="#zh-b0021" id="zh-b0021"></a>

肥料数据纳入农业、畜牧业及化学品部门。ecoinvent v3.7 包含 Yara International ASA 和 Fertilizers Europe 与 Quantis（WFLDB）合作提交的矿物肥料生产新增和更新数据。此外，肥料部门的市场和市场组合整体重构并更新，将养分供应中的有机肥与矿物肥供应分开。

#### 能源 <a href="#zh-b0023" id="zh-b0023"></a>

ecoinvent 第 3.7 版还引入与 Carbotech 合作获得的瑞士沼气生产和供应链新数据。此外，归因型电力市场组合已更新，多数国家反映 2017 年情况；美国和加拿大的参考年份为 2018 年。数据创建与审阅由苏黎世联邦理工学院及保罗谢勒研究所（PSI）合作完成。

#### 木材 <a href="#zh-b0025" id="zh-b0025"></a>

ecoinvent v3.7 发布后，林业与木材部门中大多数林业活动和木材加工相关数据集得到更新。此外，新增交叉层压木材、结构用木材、三层和五层板、空心刨花板等木质产品。该更新与 Werner Umwelt & Entwicklung 共同完成，并得益于瑞士联邦环境署（BAFU）的合作。

#### 纸和纸浆 <a href="#zh-b0027" id="zh-b0027"></a>

第 3.7 版更新包装材料相关数据，具体包括 Pro-Carton、ECMA 欧洲纸盒制造商协会、Eurosac 和 CEPI Eurokraft 提供的纸板、牛皮纸和纸袋更新数据。RISE 瑞典研究院促成这些协会与 ecoinvent 之间的数据传递。

#### 废物处理与回收利用 <a href="#zh-b0029" id="zh-b0029"></a>

第 3.7 版为废物处理与回收利用部门增添包装材料回收活动新数据，具体为欧洲和瑞士饮料罐及纸板回收的一系列新区域数据。此次更新使用苏黎世联邦理工学院和 Carbotech 发布案例研究的文献数据。

#### 建筑与建筑材料 <a href="#zh-b0031" id="zh-b0031"></a>

ecoinvent v3.7 包含 ISOVER Saint Gobain 玻璃棉毡数据集的更新版本，由 Werner Umwelt & Entwicklung 提交。数据库现为这一品牌的玻璃棉毡采用两种备选胶黏剂建模。

### 相关文档与文件 <a href="#zh-b0033" id="zh-b0033"></a>

#### 变更报告 <a href="#zh-b0034" id="zh-b0034"></a>

该报告涵盖 ecoinvent 数据库从第 3.6 版（2019）到第 3.7 版（2020）的全部变更，既反映全数据库变更，也反映各部门的特定变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/779846c080ea-change-report_v3-7_20200918.pdf)

#### 变更报告 <a href="#zh-b0037" id="zh-b0037"></a>

这份自动生成的 Excel 文件概述 ecoinvent 数据库第 3.6 版与第 3.7 版之间未指定系统模型的单元过程数据集变更。变更报告 XLS 文件可在 ecoinvent 数据库第 3 版在线平台 ecoQuery 的“文件”（Files）栏目中找到，供数据库许可证持有者使用。

#### 对应关系文件 <a href="#zh-b0039" id="zh-b0039"></a>

对应关系文件是一份电子表格，列出第 3.6 版和第 3.7 版的全部数据集，并匹配版本间的对应数据集。

<strong> ![doc-icon](../assets/024d8f149226-doc-icon.png) </strong>查看[v3.6 至 v3.7 对应关系文件](../assets/6c13576cd393-correspondence_file_eiv3.6_to_eiv3.7.xlsx)

<strong> ![doc-icon](../assets/024d8f149226-doc-icon.png) </strong>查看[v3.6 至 v3.7.1 对应关系文件](../assets/d0091c2e42d9-correspondence_file_eiv3.6_to_eiv3.7.1.xlsx)

#### ecoinvent 第 3.7 版活动概览：未指定系统模型 <a href="#zh-b0043" id="zh-b0043"></a>

一份 Excel 文件，列出 ecoinvent 第 3.7 版数据库的所有活动和产品，以及大部分元数据（地理区域、ISIC 分类、活动类型、技术水平、产品类型、单位等）。文件还包含数据库内所有地理区域、基本流交换和中间交换的清单。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7 活动概览：未指定系统模型](../assets/2206b86247db-activity_overview_3.7_undefined_public-1.xlsx)

#### ecoinvent 第 3.7 版活动概览：APOS <a href="#zh-b0046" id="zh-b0046"></a>

一份 Excel 文件，列出 ecoinvent 第 3.7 版数据库的所有活动，以及替代点分配模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7 活动概览：APOS](../assets/693c2cc417c3-activity_overview_3.7_allocation_apos_public.xlsx)

#### ecoinvent v3.7 活动概览：Consequential <a href="#zh-b0049" id="zh-b0049"></a>

一份 Excel 文件，列出数据库的所有活动，以及长期后果型替代系统模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7 活动概览：Consequential](../assets/4ca085e307af-activity_overview_3.7_consequential_public.xlsx)

#### ecoinvent 第 3.7 版活动概览：Cut-Off <a href="#zh-b0052" id="zh-b0052"></a>

一份 Excel 文件，列出数据库的所有活动，以及按分类截断的分配系统模型特有的相关元数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7 活动概览：Cut-Off](../assets/268b6abdb25e-activity_overview_3.7_allocation_cut_off_public.xlsx)

#### ecoinvent 第 3.7 版的 LCIA 方法 <a href="#zh-b0055" id="zh-b0055"></a>

列出所有 LCIA 方法及其全部影响类别，以及 ecoinvent 提供的部分累积 LCI 结果清单。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[ecoinvent v3.7 的 LCIA 方法](../assets/a86bd417337e-LCIA-methods-in-ecoinvent-3.7.xlsx)

### 已知问题 <a href="#zh-b0058" id="zh-b0058"></a>

本栏目列出 ecoinvent 数据库第 3.7 版所有已知数据错误。

#### 数据问题 <a href="#zh-b0060" id="zh-b0060"></a>

- RoW 地理区域的“electricity voltage transformation from high to medium voltage”和“electricity voltage transformation from medium to low voltage”活动出现在 Allocation, cut-off 和 APOS 系统模型中。由于这些系统模型没有 RoW 电力市场，数据集 LCIA 得分为零，不应使用。
- 在 AU、CA、CL、CN、ID、KZ、RU、US 和 ZM 地理区域的“copper mine operation and beneficiation, sulfide ore”活动中，环境输入“Tellurium, in ground”（区室：“natural resource”；子区室：“in ground”）的交换量与 GLO 地理区域不一致。各本地地理区域的交换量已向下缩放，依据的假设是这些区域开采的碲占全球铜矿石中所开采碲的 70%（全球量在 GLO 数据集中建模）。未指定系统模型数据集的新数量列于下表，将在 v3.9 发布时提供。

<table>
<tbody>
<tr>
<td><p><strong>数据集</strong></p></td>
<td><p><strong>单位</strong></p></td>
<td><p><strong>原数值</strong></p></td>
<td><p><strong>新数值</strong></p></td>
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

- “treatment of wastewater from grass refinery, capacity 5E9l/year, RoW”活动在 APOS 系统模型中不可用。由于数据库未使用该活动及其对应参考产品，这不会影响得分。
- “glucose production, RER”数据集被错误地排除在本次发布之外。建议用户使用“glucose production, GLO”，并调整供应链以引用 RER 活动。我们将在第 3.8 版重新引入该数据集。
- “glued laminated timber production, average glue mix, CA-QC”数据集的参考产品错误，为“glued laminated timber, for indoor use”。该参考产品在第 3.7 版重命名为“glued laminated timber, average glue mix”。第 3.7 版中不存在“glued laminated timber, for indoor use”的市场。
- “market for sawnwood, board, softwood, dried (u=10%), planed, CH”中的运输距离不正确。必须删除数据集中的“transport, freight, light commercial vehicle”交换，并新增数量为 86.7105 metric ton\*km 的“transport, freight, lorry, unspecified”交换。

- “treatment of spent sawing slurry from Si-wafer cutting, RER and GLO”活动中，参考产品“spent sawing slurry from Si-wafer cutting”的数量不正确。原始单一输出单元过程可在 v2 报告中找到（Jungbluth, N., Stucki, M., Frischknecht, R. (2009). Photovoltaics. In Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz. Ecoinvent report No. 6-XII）。
- 航空货运数据集（“transport, freight, aircraft, dedicated freight, […] haul”和“transport, freight, aircraft, belly-freight, […] haul”）在 ecoinvent v3.8 发布时，与原数据提供方 INFRAS 合作更新。更新后的项目报告（Notten P.J., Althaus H-J. and Cox B., (2021) Life cycle inventories of global air freight – Global, Update 2021（全球航空货运生命周期清单——全球，2021 年更新）。ecoinvent 协会，瑞士苏黎世）可在 ecoinvent 网站的[SRI 成果](https://ecoinvent.org/activities/sri-project/)栏目获取。更多信息见第 3.8 版变更报告，用户可在其中找到数据修正指导及影响评价相关变更信息。
- “styrene production”数据集向水体和大气排放的苯过高。在 PlasticsEurope 支持下，确认可从数据集中完全删除苯的水排放，并将其大气排放降至 2.0E-07 kg。修正后的清单已于第 3.8 版引入。
- 已确认“iron sinter production, RER”和“iron sinter production, GLO”数据集包含三项计算不一致的基本流交换（排放）：

“Particulates, &gt; 10 um”（颗粒物，&gt; 10 um）、  
“Particulates, &gt; 2.5 um, and &lt; 10um”（颗粒物，&gt; 2.5 um 且 &lt; 10um）以及  
“Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin”（二噁英，以 2,3,7,8-四氯二苯并对二噁英计）。

此外，数据集缺少“Particulates, &lt; 2.5 um”（颗粒物，&lt; 2.5 um）排放。

新增及修正的基本流交换及其对应数量列于下表。

<table>
<tbody>
<tr>
<td><p>基本流交换</p></td>
<td><p>数量</p></td>
<td><p>单位</p></td>
</tr>
<tr>
<td><p>Particulates, &gt; 10 um </p></td>
<td><p>9.38E-05 </p></td>
<td><p>kg </p></td>
</tr>
<tr>
<td><p>Particulates, &gt; 2.5 um, and &lt; 10um </p></td>
<td><p>1.96E-05 </p></td>
<td><p>kg </p></td>
</tr>
<tr>
<td><p>Particulates, &lt; 2.5 um </p></td>
<td><p>1.20E-04 </p></td>
<td><p>kg </p></td>
</tr>
<tr>
<td><p>Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin </p></td>
<td><p>1.55E-12 </p></td>
<td><p>kg </p></td>
</tr>
</tbody>
</table>

- 2020 年 11 月，我们收到国际锌业协会关于锌矿开采数据集建模的更新：“zinc mine operation, GLO”活动中，环境输入“Gold, in ground”（区室：“natural resource”；子区室：“in ground”）的交换量错误。由于它是多输出活动，归因型系统模型中的多个数据集受到该错误影响。根据数据提供方提交的修正数据，各系统模型的新数量列于下表，与 ecoinvent 数据库第 3.7.1 版发布的数量一致。

<table>
<tbody>
<tr>
<td><p>系统模型</p></td>
<td><p>参考产品</p></td>
<td><p>“Gold, in ground”的修正交换量（kg）</p></td>
</tr>
<tr>
<td><p>未指定系统模型（Undefined）</p></td>
<td><p>锌精矿（zinc concentrate）</p></td>
<td><p>0.00000104 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>混合铅锌精矿（bulk lead-zinc concentrate）</p></td>
<td><p>6.86335E-07 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>硫化矿铜精矿（copper concentrate, sulfide ore）</p></td>
<td><p>1.58859E-06 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>未精炼金（gold, unrefined）</p></td>
<td><p>0.040384363 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>未分选废铁（iron scrap, unsorted）</p></td>
<td><p>2.80535E-07 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>铅精矿（lead concentrate）</p></td>
<td><p>7.10915E-07 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>石灰（lime）</p></td>
<td><p>2.21215E-07 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>粉磨散装生石灰（quicklime, milled, loose）</p></td>
<td><p>1.45586E-07 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>砂（sand）</p></td>
<td><p>7.56292E-09 </p></td>
</tr>
<tr>
<td><p>替代点分配模型（Allocation, APOS）</p></td>
<td><p>锌精矿（zinc concentrate）</p></td>
<td><p>7.18478E-07 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>混合铅锌精矿（bulk lead-zinc concentrate）</p></td>
<td><p>6.88443E-07 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>硫化矿铜精矿（copper concentrate, sulfide ore）</p></td>
<td><p>1.59347E-06 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>未精炼金（gold, unrefined）</p></td>
<td><p>0.040508371 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>铅精矿（lead concentrate）</p></td>
<td><p>7.13098E-07 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>石灰（lime）</p></td>
<td><p>2.21895E-07 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>粉磨散装生石灰（quicklime, milled, loose）</p></td>
<td><p>1.46033E-07 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>砂（sand）</p></td>
<td><p>7.58615E-09 </p></td>
</tr>
<tr>
<td><p>截断分配模型（Allocation, cut-off）</p></td>
<td><p>锌精矿（zinc concentrate）</p></td>
<td><p>7.20684E-07 </p></td>
</tr>
<tr>
<td><p>后果型模型（Consequential）</p></td>
<td><p>锌精矿（zinc concentrate）</p></td>
<td><p>0.00000104 </p></td>
</tr>
</tbody>
</table>

- “methylene diphenyl diisocyanate production”数据集（GLO 和 RER）将生成的盐酸作为废物处理，这不符合实际。盐酸是 MDI 生产者使用或出售的有价值副产品。ecoinvent 协会建议用户使用 PlasticsEurope 网站当前[ecoProfile](https://plasticseurope.org/sustainability/circularity/life-cycle-thinking/eco-profiles-set/) 的 LCIA 得分，或通过移除废物中和处理、将 HCl 作为副产品处理来修正 ecoinvent 单元过程。  
  要修正 ecoinvent 数据集，建议使用 ecoQuery 提供的未指定系统模型数据集，并删除氢氧化钠输入以及钠和氯化物输出的交换。

#### <strong>后果型系统模型问题</strong> <a href="#zh-b0191" id="zh-b0191"></a>

- “social”环境区室中存在三个基本流交换。由于 ecoinvent 尚未核算社会影响，在单元过程和清单层级均可忽略这些交换。

{% endtab %}

{% tab title="English 原文" %}

## Version 3.7 of the ecoinvent database was published in September 2020. It features more than 900 new and 1,000 updated datasets. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.7 was released on September 17th, 2020. </strong>

<strong>ecoinvent v3.7.1 was released on December 17th, 2020.</strong> Discover how to [upgrade to our latest version](licensing.md).

Oct 27th, 2023

It was replaced by ecoinvent v3.7.1 to update a significant error in the iron sinter production dataset.

With ecoinvent v3.7, the ecoinvent data landscape widens with more than 900 new and 1,000 updated datasets, including more than 100 new products. This update expands the coverage of the database in various sectors such as metals, fertilisers, forestry and wood, packaging materials, waste/recycling, and biogas supply chains, while the electricity market mixes are also updated.

The updates and additions of version 3.7 come as the result of the ecoinvent association’s participation in various projects and collaborations. These included the overhaul of the Forestry and Wood sector and updates in the metal sector, both sponsored by the Swiss Federal Office for the Environment, BAFU. Further updates have resulted from collaborations with associations in different industrial sectors globally. Namely, ecoinvent version 3.7 integrates updated data on different metal products from the Cobalt Institute and the Aluminium Association of Canada, and updated data on packaging material from the industry associations Eurosac, CEPI Eurokraft, Pro-Carton, and ECMA European Carton Makers Association. For the fertilisers sector collaborations included those with Yara International ASA and Fertlizers Europe.

#### Important Issue <a href="#en-b0009" id="en-b0009"></a>

ecoinvent v3.7 has been identified to include an issue of significant effect. Specifically, the iron sinter production dataset includes an error in the order of magnitude of the estimated emissions for dioxins and particulate matter (PM). This error distorts the results of the ecoinvent database using human health and ecotoxicity indicators from most methods.

All other impact categories, including climate change, water depletion, cumulative energy demand, land use and land use change, fossil depletion, acidification, eutrophication, ionising radiation, renewable resources, stratospheric ozone depletion, photochemical oxidant formation, radioactive substances and ozone layer depletion, are not impacted by these issues.

A [technical report](../assets/7da8bd6a5b33-technical-report_v3-7-1_20201217.pdf) over this issue is available.

### ecoinvent Version 3.7.1 <a href="#en-b0013" id="en-b0013"></a>

To correct iron sinter production dataset, ecoinvent v3.7.1 is released in December 2020.

ecoinvent v3.7.1 focuses on correcting the iron sinter production dataset.

With this opportunity, the zinc mining dataset is also updated with newer data submitted by the International Zinc Association after the release of ecoinvent v3.7. This update is expected to significantly improve the quality of the database. The newer data address the high extraction of gold modeled in the dataset until now and affect the results of the database calculated using mineral resource depletion indicators from most methods. Otherwise, thereare further updates or changes of the content of ecoinvent v3.7.

Please note: Research and projects based on other impact categories, including  climate change, water depletion, cumulative energy demand, land use and land use change, fossil depletion, acidification, eutrophication, ionising radiation, renewable resources, stratospheric ozone depletion, photochemical oxidant formation, radioactive substances and ozone layer depletion, remain completely unaffected by the issue.

### New and Updated Data <a href="#en-b0018" id="en-b0018"></a>

#### Metals <a href="#en-b0019" id="en-b0019"></a>

The Metals sector has been updated with new and updated data on copper, nickel, iron and steel, and scarce metals such as cobalt, rare earths, tungsten, and beryllium. Data contributors included EMPA (sponsored by the Swiss Federal Office for the Environment, BAFU), the Cobalt Institute and TU Graz. The datasets for aluminium in North America have also been revised with data contributed by the Aluminium Association of Canada.

#### Fertilisers <a href="#en-b0021" id="en-b0021"></a>

Data for fertilisers are included in the sectors for Agriculture, Animal Husbandry, and Chemicals. ecoinvent v3.7 includes new and updated data on mineral fertiliser production from Yara International ASA and Fertilizers Europe, submitted in collaboration with Quantis (WFLDB). Further, the markets and market mixes for the fertilisers sector have been generally restructured and updated, separating now the provision of organic and mineral fertilisers for nutrient supply.

#### Energy <a href="#en-b0023" id="en-b0023"></a>

ecoinvent version 3.7 also introduces new data on biogas production and supply chains for Switzerland, obtained from a collaboration with Carbotech. Further, attributional electricity market mixes are updated to represent the situation in 2017 for most countries. In the case of US and Canada, the reference year is 2018. Data creation and review was done in collaboration with ETH Zurich and the Paul Scherrer Institute (PSI).

#### Wood <a href="#en-b0025" id="en-b0025"></a>

Following the release of ecoinvent v3.7, most of the datasets related to forestry activities and wood processing in the Forestry and Wood sector are updated. Further,  new wood-based products have been added, such as cross-laminated timber, structural timber, three and five layered board, and tubular particleboard. This update was done jointly with Werner Umwelt & Entwicklung and was made possible due to a collaboration with the Swiss Federal Office for the Environment (BAFU).

#### Paper and Pulp <a href="#en-b0027" id="en-b0027"></a>

Version 3.7 introduces updates in data related to packaging material. Specifically, it includes updated data from the industry associations Pro-Carton, ECMA European Carton Makers Association, Eurosac and CEPI Eurokraft on cartonboard, kraft paper and paper sacks. RISE, Research Institutes of Sweden, made possible the transfer of the data between the associations and ecoinvent.

#### Waste Treatment and Recycling <a href="#en-b0029" id="en-b0029"></a>

With version 3.7, the Waste Treatment and Recycling sector has been enhanced with new data on recycling activities of packaging materials, namely a range of new regional data for Europe and Switzerland on the recycling of beverage cans and paperboard. This update uses literature data from case studies published by ETH Zurich and Carbotech.

#### Building & Construction Materials <a href="#en-b0031" id="en-b0031"></a>

ecoinvent v3.7 includes an updated version of glass wool mat datasets from ISOVER Saint Gobain; the data submission was done by Werner Umwelt & Entwicklung. This branded glass wool mat is now modeled with two alternative adhesives in the database.

### Relevant Documents and Files <a href="#en-b0033" id="en-b0033"></a>

#### Report of Changes <a href="#en-b0034" id="en-b0034"></a>

This report covers all changes made in the ecoinvent database between version 3.6 (2019) and version 3.7 (2020). It reflects both the database-wide changes, as well as the sector-specific changes.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Report of Changes](../assets/779846c080ea-change-report_v3-7_20200918.pdf)

#### Report of Changes <a href="#en-b0037" id="en-b0037"></a>

This automatically generated excel file provides an overview of changes made on the undefined unit process datasets between versions 3.6 and 3.7 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### Correspondence File <a href="#en-b0039" id="en-b0039"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.6 and 3.7 and matches corresponding datasets between versions.

<strong> ![doc-icon](../assets/024d8f149226-doc-icon.png)  </strong>See [Correspondence File v3.6 to v3.7](../assets/6c13576cd393-correspondence_file_eiv3.6_to_eiv3.7.xlsx)

<strong> ![doc-icon](../assets/024d8f149226-doc-icon.png)  </strong>See [Correspondence File v3.6 to v3.7.1](../assets/d0091c2e42d9-correspondence_file_eiv3.6_to_eiv3.7.1.xlsx)

#### Activity Overview for ecoinvent Version 3.7, Undefined <a href="#en-b0043" id="en-b0043"></a>

An excel file listing all the activities and products present in the ecoinvent version 3.7 database including most of the metadata (geography, ISIC classification, activity type, technology level, product type, unit, etc.). This file also includes a list of all geographies, elementary and intermediate exchanges present in the database.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.7, Undefined](../assets/2206b86247db-activity_overview_3.7_undefined_public-1.xlsx)

#### Activity Overview for ecoinvent Version 3.7, APOS <a href="#en-b0046" id="en-b0046"></a>

An excel file listing all the activities present in the ecoinvent version 3.7 database including metadata related specifically to the Allocation at the point of substitution.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.7, APOS](../assets/693c2cc417c3-activity_overview_3.7_allocation_apos_public.xlsx)

#### Activity Overview for ecoinvent v3.7, Consequential <a href="#en-b0049" id="en-b0049"></a>

An excel file listing all the activities present in the database including metadata related specifically to the Substitution, consequential, long-term system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.7, Consequential](../assets/4ca085e307af-activity_overview_3.7_consequential_public.xlsx)

#### Activity Overview for ecoinvent Version 3.7, Cut-Off <a href="#en-b0052" id="en-b0052"></a>

An excel file which lists all the activities present in the database including metadata related specifically to the Allocation, cut-off by classification system model.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Activity Overview for ecoinvent v3.7, Cut-Off](../assets/268b6abdb25e-activity_overview_3.7_allocation_cut_off_public.xlsx)

#### LCIA Methods in ecoinvent Version 3.7 <a href="#en-b0055" id="en-b0055"></a>

List of all LCIA methods including all the impact categories as well as list of selected LCI cumulative results provided by ecoinvent.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [LCIA Methods in ecoinvent v3.7](../assets/a86bd417337e-LCIA-methods-in-ecoinvent-3.7.xlsx)

### Known Issues <a href="#en-b0058" id="en-b0058"></a>

This section lists all known data errors in version 3.7 of the ecoinvent database.

#### Data Issues <a href="#en-b0060" id="en-b0060"></a>

- The activities “electricity voltage transformation from high to medium voltage” and “electricity voltage transformation from medium to low voltage” for the RoW geography appear in the Allocation, cut-off and APOS system model. As the RoW markets for electricity do not exist for these system models, the datasets have LCIA scores of zero and should not be used.
- The exchange amount of the input from the environment “Tellurium, in ground” (compartment: “natural resource”; subcompartment: “in ground”) in the activity “copper mine operation and beneficiation, sulfide ore” for the geographies AU, CA, CL, CN, ID, KZ, RU, US, and ZM was found to be inconsistent with the amount in the GLO geography. The exchange amounts in the local geographies have been scaled down based on the assumption that these geographies extract 70% of the global Te that is extracted in copper ores (modeled in the GLO dataset).The new amounts for the undefined datasets are listed in the table below. They will be available with the release of v3.9.

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

- The activity “treatment of wastewater from grass refinery, capacity 5E9l/year, RoW” is not available in the APOS system model. This does not have any impact on the scores, as the activity and the respective reference product are not used within the database.
- The dataset “glucose production, RER” has been erroneously excluded from this release. We recommend users to use the dataset “glucose production, GLO” and to adjust the supply chain to refer to RER activities. We will re-introduce it for version 3.8.
- The dataset “glued laminated timber production, average glue mix, CA-QC” has a wrong reference product, namely “glued laminated timber, for indoor use”. This reference product was renamed in version 3.7 to “glued laminated timber, average glue mix”. In version 3.7, no market for glued “laminated timber, for indoor use” exists.
- The transport distances in the market for sawnwood, board, softwood, dried (u=10%), planed, CH are incorrect. The exchange transport, freight, light commercial vehicle has to be deleted from the dataset. The exchange “transport, freight, lorry, unspecified” with an amount of 86.7105 metric ton\*km has to be added to the dataset.

- The amount of the reference product “spent sawing slurry from Si-wafer cutting” in the activities “treatment of spent sawing slurry from Si-wafer cutting, RER and GLO” is incorrect. The original single output unit processes can be found at the v2 report (Jungbluth, N., Stucki, M., Frischknecht, R. (2009). Photovoltaics. In Dones, R. (Ed.) et al., Sachbilanzen von Energiesystemen: Grundlagen für den ökologischen Vergleich von Energiesystemen und den Einbezug von Energiesystemen in Ökobilanzen für die Schweiz. Ecoinvent report No. 6-XII).
- The air freight transport datasets (“transport, freight, aircraft, dedicated freight, […] haul” and “transport, freight, aircraft, belly-freight, […] haul”) are updated within the release of ecoinvent v3.8 in collaboration with INFRAS, the original data provider. An updated project report (Notten P.J., Althaus H-J. and Cox B., (2021) Life cycle inventories of global air freight – Global, Update 2021. ecoinvent Association, Zürich, Switzerland) is accessible in the [SRI results](https://ecoinvent.org/activities/sri-project/) section of the ecoinvent website. More information can be found in the Report of Changes for version 3.8. Within the report users can find indication on how to correct the data and information on relevant changes in impact assessment.
- In the dataset “styrene production”, the benzene emissions to water and to air are too high. With support of PlasticsEurope, it could be established that the benzene emissions to water can be removed completely from the dataset and the benzene emissions to air were decreased to 2.0E-07 kg. A corrected inventory was introduced in version 3.8
- The datasets “iron sinter production, RER” and “iron sinter production, GLO” have been identified to contain three inconsistently calculated elementary exchanges (emissions) for:

“Particulates, &gt; 10 um”,   
“Particulates, &gt; 2.5 um, and &lt; 10um” and   
“Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin”

In addition, the datasets lack of emissions for “Particulates, &lt; 2.5 um”.

The added and corrected elementary exchange/s and their respective amounts are presented in the table below. 

<table>
<tbody>
<tr>
<td>
<p>Elementary exchange </p>
</td>
<td>
<p>Amount </p>
</td>
<td>
<p>Unit </p>
</td>
</tr>
<tr>
<td>
<p>Particulates, &gt; 10 um </p>
</td>
<td>
<p>9.38E-05 </p>
</td>
<td>
<p>kg </p>
</td>
</tr>
<tr>
<td>
<p>Particulates, &gt; 2.5 um, and &lt; 10um </p>
</td>
<td>
<p>1.96E-05 </p>
</td>
<td>
<p>kg </p>
</td>
</tr>
<tr>
<td>
<p>Particulates, &lt; 2.5 um </p>
</td>
<td>
<p>1.20E-04 </p>
</td>
<td>
<p>kg </p>
</td>
</tr>
<tr>
<td>
<p>Dioxins, measured as 2,3,7,8-tetrachlorodibenzo-p-dioxin </p>
</td>
<td>
<p>1.55E-12 </p>
</td>
<td>
<p>kg </p>
</td>
</tr>
</tbody>
</table>

- In November 2020, we received an update from the International Zinc Association regarding the modeling of the zinc mining dataset: The exchange amount of the input from the environment “Gold, in ground” (compartment: “natural resource”; subcompartment: “in ground”) was found to be wrong in the activity “zinc mine operation, GLO”. As this is a multi-output activity, several datasets are affected by this error in the attributional system models. The new amounts in each system model, based on corrected data supplied by the data provider, are listed in the table below. These amounts correspond to those published in version 3.7.1 of the ecoinvent database.

<table>
<tbody>
<tr>
<td>
<p>System model </p>
</td>
<td>
<p>Reference product </p>
</td>
<td>
<p>Corrected exchange amount of “Gold, in ground” (kg) </p>
</td>
</tr>
<tr>
<td>
<p>Undefined </p>
</td>
<td>
<p>zinc concentrate </p>
</td>
<td>
<p>0.00000104 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>bulk lead-zinc concentrate </p>
</td>
<td>
<p>6.86335E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>copper concentrate, sulfide ore </p>
</td>
<td>
<p>1.58859E-06 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>gold, unrefined </p>
</td>
<td>
<p>0.040384363 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>iron scrap, unsorted </p>
</td>
<td>
<p>2.80535E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>lead concentrate </p>
</td>
<td>
<p>7.10915E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>lime </p>
</td>
<td>
<p>2.21215E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>quicklime, milled, loose </p>
</td>
<td>
<p>1.45586E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>sand </p>
</td>
<td>
<p>7.56292E-09 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, APOS </p>
</td>
<td>
<p>zinc concentrate </p>
</td>
<td>
<p>7.18478E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>bulk lead-zinc concentrate </p>
</td>
<td>
<p>6.88443E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>copper concentrate, sulfide ore </p>
</td>
<td>
<p>1.59347E-06 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>gold, unrefined </p>
</td>
<td>
<p>0.040508371 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>lead concentrate </p>
</td>
<td>
<p>7.13098E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>lime </p>
</td>
<td>
<p>2.21895E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>quicklime, milled, loose </p>
</td>
<td>
<p>1.46033E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>sand </p>
</td>
<td>
<p>7.58615E-09 </p>
</td>
</tr>
<tr>
<td>
<p>Allocation, cut-off </p>
</td>
<td>
<p>zinc concentrate </p>
</td>
<td>
<p>7.20684E-07 </p>
</td>
</tr>
<tr>
<td>
<p>Consequential </p>
</td>
<td>
<p>zinc concentrate </p>
</td>
<td>
<p>0.00000104 </p>
</td>
</tr>
</tbody>
</table>

- The dataset “methylene diphenyl diisocyanate production” (GLO and RER) treats the formed hydrochloric acid as a waste, this does not reflect reality. Hydrochloric acid is a valuable by-product which is used or sold by the MDI producer.The ecoinvent association advices users to either use the LCIA scores from the current [ecoProfile](https://plasticseurope.org/sustainability/circularity/life-cycle-thinking/eco-profiles-set/) available on the PlasticsEurope website or to correct the unit process in ecoinvent by removing the waste neutralisation and treating HCl as a by-product.   
  To correct the ecoinvent dataset, we would advise user to use the undefined dataset available through ecoQuery and remove the exchanges of the input of sodium hydroxide and the outputs of sodium and chloride.

#### <strong>Consequential System Model Issues</strong> <a href="#en-b0191" id="en-b0191"></a>

- Three elementary exchanges are found in the compartment “social”. These exchanges can be ignored, both at the unit process and the inventory level, as ecoinvent does not yet account for social impacts.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0016**：原文 otherwise 后断言还有更新，但可能遗漏 no，且 thereare 拼写粘连；是否为除上述之外没有进一步更新存在歧义。 请对照 3.7.1 技术报告核实该句是否遗漏否定词；当前译文按现有肯定句翻译。 [查看完整记录](../review/issues.md#issue-078)
