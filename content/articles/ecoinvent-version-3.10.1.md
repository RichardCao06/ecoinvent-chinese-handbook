# ecoinvent 第 3.10.1 版

英文原题：ecoinvent Version 3.10.1  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-version-3.10.1)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2026-09-15

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoinvent v3.10.1 于 2024 年 11 月发布，包含与数据库第 3.10 版相同的数据集，同时对第 3.10 版特定数据集作出两项重要修正。 <a href="#zh-b0002" id="zh-b0002"></a>

<strong>ecoinvent v3.10.1 于 2024 年 11 月 19 日与 v3.11 同时发布</strong>。了解如何[升级至我们的最新版本](licensing.md)。

2025 年 9 月 24 日

此次对 ecoinvent 数据库[第 3.10 版](ecoinvent-version-3.10.md)的更新包含第 3.10 版发布的相同新增及更新数据集，但作出两项重要修正：

- <strong>修正焦炭生产中某些大气排放的数量</strong>：

在所有系统模型中，CN 的“coke production, wet quenching”和 RoW 的“coke production”数据集，部分环境排放的交换数量错误。修正交换量见文件：[焦炭 3.10 修正：所有系统模型](../assets/182a4019c27b-Known-Issue-Correction_Coke_3.10_All-System-Models.xlsx)

焦炭是大多数供应链使用的燃料，因此该错误影响数据库第 3.10 版中大多数数据集的得分。

v3.10 中许多数据集在以下影响类别的得分过高：

- 生态系统质量
- 生态毒性
- 人体健康
- 人体毒性

为说明这些影响类别在数据库中的受影响程度，以下指标描述“Allocation, cut-off”系统模型的得分受该问题影响的情况：

614 个指标中有 91 个明显受影响：v3.10 中至少 1% 数据集的得分比 v3.10.1 修正后得分高出至少 5%。最极端的得分差异出现在 ReCiPe 和 EF 方法中。对于这些方法，v3.10 的得分平均为正确得分的 2–3 倍，约 90% 的数据集得分比修正后得分高出至少 5%。

所有其他影响类别，包括气候变化，完全不受该问题影响。

- <strong>巴西电力市场产量错误：</strong>

第 3.10 版发现巴西电力市场产量（PV）的数量级错误。巴西（BR）电力市场供应拉丁美洲地区（RLA）市场组：v3.10 的 BR 市场产量仅为正确值的 1/1,000。因此，巴西市场对 RLA 市场组的贡献远低于应有水平。

v3.10 显著低估许多数据集的土地利用相关气候变化及生物源气候变化影响。对于这些指标，在“Allocation, cut-off”系统模型中，约 60% 数据集的得分比修正后得分低至少 5%。

用水指标得分也被低估，但程度较小（约 5% 的数据库受影响）。总气候变化仅约 15 个数据集受影响。

后果型系统模型使用前瞻数据对未来电力市场组合建模，因此不受该问题影响；所有其他系统模型均受影响。

有关第 3.10.1 版所实施变更的更多细节，请参阅变更报告。

所有系统模型下第 3.10 版与第 3.10.1 版得分的详细比较，可在 ecoQuery 文件页面中 v3.10.1 的配套文档栏目获取。

第 3.10 版更新的部门包括农业、建筑与施工、化学品、电力、林业与木材、燃料、金属、包装、纸浆与纸以及废物。ecoinvent v3.10 还包含新的影响评价方法和分类。

### <strong>分类</strong> <a href="#zh-b0025" id="zh-b0025"></a>

v3.10 为产品引入 [HS（协调制度）2017](https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2017-edition.aspx) 分类。除 CPC（产品总分类）外，该分类有助于对交换分类，并支持产品与交换的匹配。由于分类体系的设计，基础设施和服务交换不纳入 HS 2017 分类。

### <strong>部门更新</strong> <a href="#zh-b0027" id="zh-b0027"></a>

#### <strong>农业、渔业与畜牧业</strong> <a href="#zh-b0028" id="zh-b0028"></a>

ecoinvent 第 3.10 版带来一轮新且前景良好的更新，亮点是为澳大利亚和美国这两个农业生产大国新增全面的作物生产数据。澳大利亚的新地区现已提供大麦粒、玉米粒、燕麦粒和小麦粒等作物数据，更准确地体现其农业状况。美国新增多个州的玉米粒、甜玉米、马铃薯、大豆及各类田间作业数据，扩展信息范围。此外，新增亚麻生产和打麻的欧洲平均数据（RER）。第 3.10 版引入 FLAG／非 FLAG 排放的补充文档，为农业部门提供额外支持，帮助用户更好地理解并依据 SBTi 目标评价排放相关环境影响。最后，第 3.10 版进一步提升部分农产品的数据质量，并审阅加拿大扁豆及豌豆生产的肥料输入数据。

#### <strong>建筑与施工</strong> <a href="#zh-b0030" id="zh-b0030"></a>

第 3.10 版为 ecoinvent 数据库的建筑与施工部门带来丰富改进，包括大量新数据和多项更新。我们为突尼斯地理范围增加熟料及多种水泥生产的全面信息，以及相应市场活动。瑞士市场数据库删除了不符合当前建筑材料生产实际的过时活动，并提供熟料和水泥生产（包括波特兰水泥、CEM II/A、CEM II/B）及其相应市场活动的更新数据。厄瓜多尔地区新增大量覆盖土坯砖、黏土砖、熟料、水泥、混凝土砌块及黏土屋面瓦等建筑材料生产的数据集，以及相应市场活动。

#### <strong>化学品与塑料</strong> <a href="#zh-b0032" id="zh-b0032"></a>

化学品部门更新了重要化学前体及其衍生物的数据表示，包括短链烯烃（乙烯、丙烯、丁烯、丁二烯）、单环芳烃（苯、甲苯和二甲苯［对位、邻位、混合］）、环氧乙烷和乙二醇。代表欧洲条件的行业数据由 [Plastics Europe](https://plasticseurope.org/) 提供。其他主要更新包括扩展乙烯、丙烯、氢气及甲醇的技术和地理覆盖范围。具体而言，ecoinvent v3.10 引入中国、美国和欧洲数据。

此外，ecoinvent v3.10 引入更新的行业数据，涵盖 [Euro Chlor](https://www.eurochlor.org/) 提供的氯和氢氧化钠供需数据，以及 [ISOPA](https://www.isopa.org/) 提供的二异氰酸酯（二苯基甲烷二异氰酸酯和甲苯二异氰酸酯）及聚醚多元醇（短链和长链）数据。

该版本还引入远低于环境温度的工艺流工业制冷供应数据，温度为 –15、–25、–45、–55、–100 和 –160°C。

最后，ecoinvent v3.10 的化学品部门迈向全面内容更新。该更新遵循 ecoinvent 标准方法，重点涉及命名、文档、技术相关性、清单完整性和协调一致。

#### <strong>能源</strong> <a href="#zh-b0037" id="zh-b0037"></a>

ecoinvent v3.10 更新电力市场组合，以反映 2020 年情况。巴西、中国、美国、加拿大和瑞士的特定情况则更新为 2021 年；印度更新为 2019 年 4 月／2020 年 3 月财政年度。所有特定情况基于国家统计，其余国家基于全球统计。

除进一步的小幅修正外，还开展协调工作，更新电力市场、变压和进口数据集的文档及元信息。

ecoinvent v3.10 还引入小型风电设施生产数据集。

#### <strong>林业与木材</strong> <a href="#zh-b0041" id="zh-b0041"></a>

林业与木材部门新增三个与厄瓜多尔竹林经营、竹竿生产及展平竹生产相关的数据集。数据由 Empa（瑞士联邦材料科学与技术实验室）提供。

#### <strong>燃料</strong> <a href="#zh-b0043" id="zh-b0043"></a>

新版本显著扩展石油和天然气部门的地理覆盖范围。油气生产数据集现覆盖 41 个不同地理区域，相比之下 v3.9.1 为 27 个。此次更新使覆盖范围超过全球原油生产的 96% 和天然气产出的 98%。纳入澳大利亚、阿曼和土库曼斯坦等国家的数据，显著改善该部门表示；这些国家尤其是亚洲经济体天然气供应的重要贡献方。新版本反映 2021 年供应状况（此前为 2019 年）。

#### <strong>金属</strong> <a href="#zh-b0045" id="zh-b0045"></a>

此次更新通过新增和更新数据扩展金属部门覆盖范围。具体而言，ecoinvent v3.10 引入热喷涂数据（大气等离子喷涂（APS）、超音速火焰喷涂（HVOF）和冷喷涂（CS））。稀土氧化物价格也已更新。

#### <strong>纸浆和纸</strong> <a href="#zh-b0047" id="zh-b0047"></a>

纸浆和纸部门新增三个饮料纸盒生产相关数据集。此外，欧洲地区的瓦楞纸板生产数据集依据欧洲瓦楞纸板制造商联合会（FEFCO）及 Cepi ContainerBoard（CCB）的最新研究更新。

#### <strong>废物管理与回收利用</strong> <a href="#zh-b0049" id="zh-b0049"></a>

第 3.10 版继续推进废物部门全面修订的第二阶段，重点拆分 450 多个固体废物处理数据集。用户现在可看到处理活动完整供应链被拆分为独立数据集。所有副产品透明报告，排放恰当地分配至产生这些排放的对应活动，并新增本地废物运输距离。此外，通过在更多国家增加固体废物处理数据集，扩展该部门地理覆盖范围。

### <strong>相关文档与文件</strong> <a href="#zh-b0051" id="zh-b0051"></a>

#### <strong>变更报告</strong> <a href="#zh-b0052" id="zh-b0052"></a>

该报告涵盖 ecoinvent 数据库第 3.10 版（2023）与第 3.10.1 版（2024）之间的全部变更。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[变更报告](../assets/7139151e80d4-Change-Report-v3.10.1.pdf)

#### <strong>变更报告</strong> <a href="#zh-b0055" id="zh-b0055"></a>

这份自动生成的 Excel 文件概述 ecoinvent 数据库第 3.9 版与第 3.10.1 版之间未指定系统模型的单元过程数据集变更。变更报告 XLS 文件可在 ecoinvent 数据库第 3 版在线平台 ecoQuery 的“文件”（Files）栏目中找到，供数据库许可证持有者使用。

#### <strong>对应关系文件</strong> <a href="#zh-b0057" id="zh-b0057"></a>

对应关系文件是一份电子表格，列出第 3.10 版和第 3.10.1 版的全部数据集，并匹配版本间的对应数据集。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[对应关系文件](../assets/bd57a6dc654d-Correspondence-File-v3.10---v.3.10.1.xlsx)

#### <strong>数据库概览文件</strong> <a href="#zh-b0060" id="zh-b0060"></a>

数据库概览文件描述数据库内容，包含以下信息：

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[数据库概览文件](../assets/be8e63e767cc-Database-Overview-for-ecoinvent-v3.10.1.xlsx)

#### <strong>LCIA 实施报告</strong> <a href="#zh-b0063" id="zh-b0063"></a>

LCIA 实施报告记录第 3.10 版和第 3.10.1 版 LCIA 方法的实施情况。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[LCIA 实施报告](../assets/f9702d5ab70f-LCIA-implementation-3.10.1.pdf)

#### 第 3.10 版网络研讨会资源 <a href="#zh-b0066" id="zh-b0066"></a>

[![webinar-icon](../assets/9c37f83e3b0d-webinar-icon.png)](https://youtu.be/t4p2foRfwAQ) [观看“ecoinvent 第 3.10 版简介”网络研讨会](https://youtu.be/t4p2foRfwAQ)

![doc-icon](../assets/024d8f149226-doc-icon.png) [下载 v3.10 常见问题解答](../assets/15fd4ad3835e-Webinar-3.10-faqs.pdf)

![doc-icon](../assets/024d8f149226-doc-icon.png) [下载涵盖 v3.10 所有更新的概览演示文稿](../assets/8f59298dbb92-Webinar-introduction-to-ecoinvent-3.10-final.pdf)

#### 已知问题 <a href="#zh-b0070" id="zh-b0070"></a>

本栏目列出 ecoinvent 数据库第 3.10.1 版所有已知数据错误。

#### 数据问题 <a href="#zh-b0072" id="zh-b0072"></a>

<strong>阿根廷（AR）大豆生产</strong>数据集中，生命周期清单的草甘膦使用量存在问题（与其他地理区域相比相差 3 个数量级）。与数据提供方开展内部调查后，确定草甘膦施用量的正确数值为 2.34kg/ha；以 2.6 t/ha 的产量计算，相当于每 kg 大豆 0.0009 kg。

US 地理区域（US-IA、US-IL、US-IN、US-MN、US-NE、US-SD、US-WI）的所有玉米粒生产数据集，其“packaging, for fertilisers”输入报告量在数量级及数值方面存在问题。为修正此问题，将数据集申报的肥料量乘以 0,1kg 再除以 50 kg，最后再除以各作物产量，得到正确的肥料包装 kg 数量（0,1 kg 是一个可装 50 kg 固体肥料塑料袋的重量）。最后，请考虑将<strong>废聚乙烯</strong>数量更新为农药包装与肥料包装之和。

正确数值见下表，最后一列给出新数值。

<table>
<tbody>
<tr>
<td><strong>地理区域</strong></td>
<td><strong>施用肥料质量（kg/ha）</strong></td>
<td><strong>产量（kg/ha）</strong></td>
<td><strong>每 kg 玉米对应的肥料量（kg）</strong></td>
<td><strong>肥料包装（packaging, for fertilisers）（kg）</strong></td>
</tr>
<tr>
<td>US-IA</td>
<td>612.845</td>
<td>12137.68</td>
<td>5.05E-02</td>
<td>1.01E-04</td>
</tr>
<tr>
<td>US-IL</td>
<td>904.376</td>
<td><p>12283.61</p></td>
<td>7.36E-02</td>
<td>1.47E-04</td>
</tr>
<tr>
<td>US-IN</td>
<td>790.638</td>
<td>11255.79</td>
<td>7.02E-02</td>
<td><p>1.40E-04</p></td>
</tr>
<tr>
<td>US-NE</td>
<td>598.361</td>
<td>11619.32</td>
<td>5.15E-02</td>
<td>1.03E-04</td>
</tr>
<tr>
<td>US-MN</td>
<td>657.264</td>
<td>11412.19</td>
<td>5.76E-02</td>
<td>1.15E-04</td>
</tr>
<tr>
<td>US-SD</td>
<td>470.343</td>
<td>9576.76</td>
<td><p>4.91E-02</p></td>
<td><p>9.82E-05</p></td>
</tr>
<tr>
<td>US-WI</td>
<td>544.923</td>
<td>10655.84</td>
<td><p>5.11E-02</p></td>
<td><p>1.02E-04</p></td>
</tr>
</tbody>
</table>

下表所列活动的“land use change, annual crop”数值与其说明中的特定句子“LUC 应为零，因为过去 20 年种植玉米的面积下降”不一致。请不要采信该句；它将被删除。

<table>
<tbody>
<tr>
<td><strong>文件名（filename）</strong></td>
<td><strong>活动 ID（activityId）</strong></td>
<td><strong>活动名称（activityName）</strong></td>
<td><strong>地理区域（geography）</strong></td>
<td><strong>组别（group）</strong></td>
<td><p><strong>交换名称</strong></p></td>
</tr>
<tr>
<td><p>becfba64-77bf-5885-91eb-346f93c15cf0.spold</p></td>
<td>88ad76d4-bee8-5047-a67c-cbd7759908cf </td>
<td>玉米粒生产（maize grain production）</td>
<td>US-IL</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>ba70db93-bb64-5389-9fe8-6534aa2f8d98.spold</td>
<td>56db0342-ef06-58a0-9354-8565a56e725b</td>
<td>玉米粒生产（maize grain production）</td>
<td>US-IN</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>994fbb30-77ce-5368-828f-e35bddcf14fa.spold</td>
<td>468ab631-18ec-5253-94e3-e5d38e2d0b4c</td>
<td>玉米粒生产（maize grain production）</td>
<td>US-MN</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>4c4b8fdf-9880-54ee-a24c-8ca481541ddd.spold</td>
<td>08e4501f-d2d1-5c1b-915a-2fb6ab55dfba</td>
<td>玉米粒生产（maize grain production）</td>
<td>US-NE</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>41709364-8c82-5ba6-b8b7-3963692cb6c7.spold</td>
<td>16685855-520d-5bf7-afdb-ba21dd628014</td>
<td>玉米粒生产（maize grain production）</td>
<td>US-SD</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>bb8fb857-2e4d-5c13-8dca-17bef2dda2ed.spold</td>
<td>c37ecb96-fd3e-586f-98b3-e7d74be86a84</td>
<td>玉米粒生产（maize grain production）</td>
<td>US-WI</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>9c78858b-53b1-5e36-9cf9-e14e34cfac53.spold</td>
<td>17ddc472-36d2-5136-ba64-e0bf3463e898</td>
<td>大豆生产（soybean production）</td>
<td>US-IA</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>dca15df1-60b6-5a72-a46f-a8d3c5eaba9a.spold</td>
<td>c3b36dee-8291-5815-bd98-ce098417d897</td>
<td>大豆生产（soybean production）</td>
<td>US-IL</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>d2629e96-e19c-50fa-b9a7-5e1fccb7fbf7.spold</td>
<td>1df2e771-0fdc-5cc9-848e-c9d18e17e110</td>
<td>大豆生产（soybean production）</td>
<td>US-IN</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>08af5cbf-676e-5ca8-8a4f-012db12323a4.spold</td>
<td>3509aedc-8ffc-5206-90e1-ff10e24b04fc</td>
<td>大豆生产（soybean production）</td>
<td>US-MN</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>d91d68be-3484-54d8-94a8-b150a4fdee8a.spold</td>
<td>c42b3dfd-33ed-5bdf-be7b-1fc1cc5b5d10</td>
<td>大豆生产（soybean production）</td>
<td>US-ND</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>d1172bcf-7ca5-5189-9f28-eca5c73e57df.spold</td>
<td>a0bf8ef6-2bf0-5422-bc8a-831c0c99538e</td>
<td><p>大豆生产（soybean production）</p></td>
<td>US-NE</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>63242618-2ff4-59bd-830c-c3af5262eaaa.spold</td>
<td>82dc5349-8138-5f0d-aa63-8190f0707f28</td>
<td>大豆生产（soybean production）</td>
<td>US-OH</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>83589be6-6e7d-5269-bb68-14d9d9854610.spold</td>
<td>19cd67e4-2809-5802-914f-0b16d8389310</td>
<td>甜玉米生产（sweet corn production）</td>
<td>US-CA</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>59b4654c-fffd-59b3-9b69-277f9983a20f.spold</td>
<td>7aedd13e-cd86-5023-ac26-c0b604e7279c</td>
<td>甜玉米生产（sweet corn production）</td>
<td>US-FL</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>03258297-358f-5c69-b8d1-a98b53bda391.spold</td>
<td><p>6228ecf0-3afb-57e5-a782-0aa27512175d</p></td>
<td>甜玉米生产（sweet corn production）</td>
<td>US-MN</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>aae4299a-842d-59ea-9ce7-dc511f930f6e.spold</td>
<td><p>d4fe5ffb-f4cc-5342-bf10-44af3a70329a</p></td>
<td>甜玉米生产（sweet corn production） </td>
<td>US-OR</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>6298f492-0e55-515f-8e87-46f2d0d005fa.spold</td>
<td>20175ff7-1d4c-54b4-bcf1-d7edbae18ca9</td>
<td>甜玉米生产（sweet corn production）</td>
<td>US-WA</td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
<tr>
<td>8dc185fb-6c98-5f1a-ad56-c7d51aaf9ee0.spold</td>
<td>a539f6f2-0090-5175-a640-e7d3df1fb9ee</td>
<td>甜玉米生产（sweet corn production）</td>
<td><p>US-WI</p></td>
<td>来自技术圈（From Technosphere）</td>
<td>土地利用变化，一年生作物（land use change, annual crop）</td>
</tr>
</tbody>
</table>

#### <strong>LCIA 问题</strong> <a href="#zh-b0237" id="zh-b0237"></a>

<strong>生态毒性：淡水</strong>

“USEtox v2.13, endpoint”方法中，“ecotoxicity: freshwater”影响类别的单位应为“PDF.m3.day”，而非“PDF.m3.yr”。

<strong>非化石甲烷（Methane, non-fossil）及非化石一氧化碳（Carbon monoxide, non-fossil）</strong>

<em>EFv3.x EN15804</em> 方法实施中，“Methane, non-fossil”和“Carbon monoxide, non-fossil”的表征因子（CF）存在问题。虽然[方法网站](https://eplca.jrc.ec.europa.eu/LCDN/EN15804.html)仅提及生物源二氧化碳的差异，以 -1/+1 表征因子核算它会产生影响：IPCC 对生物源排放的表征因子低于化石排放，因为 a）氧化（降解为二氧化碳）对应的是此前已从大气移除的二氧化碳；b）“对于生物源甲烷，土壤吸收和部分氧化产物的去除相当于一个大气 CO2 汇”（[IPCC 报告](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/#7.6.1.3)）。因此，若对生物源碳吸收与释放表征（如 <em>EF v3.x EN15804</em> 方法），生物源甲烷排放的表征因子，以及 <em>EF v3.0 EN15804</em> 中一氧化碳排放的表征因子，将高于采用 IPCC 表征因子的 <em>EF v3.x</em> 方法。当前实施与正确实施应如下所示：

<table>
<tbody>
<tr>
<td><p>基本流</p></td>
<td><p>EF v3.1</p></td>
<td><p>EF v3.1 EN15804</p></td>
<td><p>EF v3.0</p></td>
<td><p>EF v3.0 EN15804</p></td>
</tr>
<tr>
<td colspan="5"><p>当前实施</p></td>
</tr>
<tr>
<td><p>非化石一氧化碳（Carbon monoxide, non-fossil）</p></td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td><p>0</p></td>
<td><p>0</p></td>
</tr>
<tr>
<td><p>非化石甲烷（Methane, non-fossil）</p></td>
<td><p>27</p></td>
<td><p>27</p></td>
<td><p>34</p></td>
<td><p>34</p></td>
</tr>
<tr>
<td colspan="5"><p>正确实施</p></td>
</tr>
<tr>
<td><p>非化石一氧化碳（Carbon monoxide, non-fossil）</p></td>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td><p>0</p></td>
<td><p>1.57</p></td>
</tr>
<tr>
<td><p>非化石甲烷（Methane, non-fossil）</p></td>
<td><p>27</p></td>
<td><p>29.8</p></td>
<td><p>34</p></td>
<td><p>36.8</p></td>
</tr>
</tbody>
</table>

感谢 [GreenDelta](https://www.greendelta.com/about-us/team-2-2/) 的 Conrad Spindler 发现并解释此问题。

<strong>锂辉石</strong>

锂辉石（原文化学式：LiAl(SiO3)2）的锂含量为 0.0376。在下列方法中将锂的表征因子应用于锂辉石时，可使用该值作为转换因子：  
  
\* CML v4.8 2016。  
\* Ecological Scarcity 2021。  
\* EPS 2020d。  
\* ReCiPe 2016。  
  
前三种方法尚未对锂辉石表征；ReCiPe 2016 则错误地采用锂的表征因子（转换因子为 1）对锂辉石表征。

#### <strong>澳大利亚谷物碳不平衡</strong> <a href="#zh-b0268" id="zh-b0268"></a>

在不同地区的若干澳大利亚谷物数据集中，发现由于内含生物源碳归属错误而造成的碳不平衡。具体而言，该数值被错误分配至“Carbon dioxide, land transformation”流，而正确流应为“Carbon dioxide, non-fossil”。

对于工作表 1 所列数据集，已更新基本流交换“Carbon dioxide, non-fossil”的数量，以推导残余物焚烧排放。对于工作表 2 所列数据集，已相应修正特定流的说明。

修正数值见以下电子表格，并将在 2026 年起的未来版本中实施。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[澳大利亚谷物碳不平衡修正](../assets/98e680a1ed50-Known-Issue-v3.12_Australian-Cereal-Carbon-Corrections.xlsx)

{% endtab %}

{% tab title="English 原文" %}

## ecoinvent v3.10.1 was released in November 2024. It includes the same datasets as version 3.10 of the ecoinvent database, however, it also includes two important corrections to specific datasets of version 3.10. <a href="#en-b0002" id="en-b0002"></a>

<strong>ecoinvent v3.10.1 was released on November 19th, 2024, at the same time as v3.11</strong>. Discover how to [upgrade to our latest version](licensing.md).

September 24th, 2025

This update of [version 3.10](ecoinvent-version-3.10.md) of the ecoinvent database features the same new and updated datasets as published in version 3.10, but with two important corrections:

- <strong>Correction of amounts of certain emissions to air in coke production</strong>:

The exchange amounts were wrong for some emissions to the environment in the datasets for “coke production, wet quenching” in CN and “coke production” in RoW, in all system models. The corrected exchange amounts can be found in this file: [Correction Coke 3.10 All System Models](../assets/182a4019c27b-Known-Issue-Correction_Coke_3.10_All-System-Models.xlsx)

As coke is a fuel used in most supply chains, this error affects the scores of the majority of datasets in version 3.10 of the database.

The scores of many datasets are too high in v3.10 for the following impact categories:

- ecosystem quality
- ecotoxicity
- human health
- human toxicity

To illustrate the extent to which the database is affected for those impact categories, the following metrics describe how scores are affected by this issue in the “Allocation, cut-off” system model:

91 indicators (out of 614) are noticeably affected, with 1% or more of the datasets in v3.10 having a score at least 5% higher compared to the corrected score in v3.10.1. The most extreme score differences occur in the ReCiPe and EF methods. For those methods, on average, scores are 2-3 times too high in v3.10, with ~90% of the datasets having a score at least 5% higher compared to the corrected score.

It is important to mention that all other impact categories, including climate change, are completely unaffected by this issue.

- <strong>Wrong production volumes in markets for electricity in Brazil:</strong>

A mistake in the order of magnitude of the production volumes (PVs) of the Brazilian electricity markets was found in version 3.10. The Brazilian (BR) electricity markets supply Region Latin America (RLA) market groups: PVs of the BR markets are 1,000 times too small in v3.10. Consequently, the contribution of Brazilian markets to the RLA market groups is much smaller in v3.10 than it should be.

Land use-related climate change and biogenic climate change impacts are significantly underestimated in v3.10 for many datasets. For those indicators, in the “Allocation, cut-off” system model, ~60% of the datasets have scores at least 5% too small compared to corrected scores.

The scores of water use indicators are also underestimated, but to a lesser extent (~5% of the database affected). Total climate change is affected for only ~15 datasets.

As the consequential system model uses prospective data for modeling future electricity market mixes, it is not affected by this issue, but all other system models are affected.

For more details about the changes implemented for version 3.10.1, please refer to the Report of Changes.

A detailed comparison of the scores between version 3.10 and version 3.10.1 for all system models is available in the supporting documents section of v3.10.1 on the files page in ecoQuery.

Sectors updated with version 3.10 include agriculture, building and construction, chemicals, electricity, forestry and wood, fuels, metals, packaging, pulp and paper, and waste. ecoinvent v3.10 also includes new impact assessment methods and classifications.

### <strong>Classifications</strong> <a href="#en-b0025" id="en-b0025"></a>

With v3.10, ecoinvent introduced the [HS (Harmonised Systems) 2017](https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2017-edition.aspx) classification for products. In addition to the CPC (Central Product Classification), this classification helps categorize exchanges and can support matching products to the exchanges. Due to the design of the classification system, Infrastructure and Service exchanges are not classified in HS 2017.

### <strong>Sectorial Updates</strong> <a href="#en-b0027" id="en-b0027"></a>

#### <strong>Agriculture, Fishery and Animal Husbandry</strong> <a href="#en-b0028" id="en-b0028"></a>

ecoinvent is back with a fresh and promising update in version 3.10. The highlight of this update is the addition of comprehensive data on new crop production in two major countries for agricultural production – Australia and the United States. For Australia, data on crops like barley grain, maize grain, oat grain, and wheat grain are now available from new regions, ensuring a more accurate representation of their agricultural landscape. In the United States, the update brings data on maize grain, sweet corn, potato, soybean, and various field operations from new states, expanding the scope of information. Beyond that, average European data (RER) for Flax production and scutching are added. Version 3.10 introduces supplementing documentation for FLAG/non-FLAG emissions, providing additional support for the agricultural sector, and empowering users to better understand and assess environmental impacts related to emissions based on SBTi’s targets. Finally, Version 3.10 takes a step further by enhancing the quality of data for some agricultural products, and reviewing fertilizers’ input data for Lentil and Pea production in Canada.

#### <strong>Building and Construction</strong> <a href="#en-b0030" id="en-b0030"></a>

The 3.10 update brings rich enhancements to the Building and Construction sector of the ecoinvent database, including a wealth of new data and several updates. We have added comprehensive information on clinker and various types of cement production for the Tunisia geographical scope, as well as their corresponding market activities. The Swiss market database has been updated removing obsolete activities not compliant with the current production of building materials and now shows updated figures for clinker and cement production (including Portland, CEM II/A, CEM II/B) with their corresponding market activities. For the Ecuador region, we’ve introduced extensive datasets covering construction materials like adobe bricks, clay bricks, clinker, cement, concrete blocks, and clay roof tiles production, together with their corresponding market activities.

#### <strong>Chemicals and Plastics</strong> <a href="#en-b0032" id="en-b0032"></a>

The Chemicals sector is updated to improve the data representation for essential chemical precursors and their derivatives, such as short-chain alkenes (ethylene, propylene, butene, and butadiene), monocyclic aromatics (benzene, toluene, and xylenes [p-, o-, mixed]), ethylene oxide, and ethylene glycol. Industry data for European conditions was provided by [Plastics Europe](https://plasticseurope.org/). Additional key updates comprise of technological and geographical coverage expansion for ethylene, propylene, hydrogen, and methanol. Specifically, ecoinvent v3.10 introduces data for China, United States, and Europe.

Moreover, ecoinvent v3.10 introduces updated industry data covering the supply and demand of chlorine and sodium hydroxide, provided by [Euro Chlor](https://www.eurochlor.org/), diisocyanates (methylene diphenyl diisocyanate and toluene diisocyanate) and polyether polyols (short- and long-chain), provided by [ISOPA](https://www.isopa.org/).

This version also introduces data for industrial cooling supply for process streams at temperatures well below ambient, i.e., –15, –25, –45, –55, –100, and –160°C.

Finally, the Chemicals sector in ecoinvent v3.10 takes a step toward a comprehensive content update. This content update focuses on nomenclature, documentation, technological relevance, inventory completeness, and harmonization following the standard ecoinvent approach.

#### <strong>Energy</strong> <a href="#en-b0037" id="en-b0037"></a>

ecoinvent v3.10 updates the electricity market mixes to reflect the situation in 2020. In the specific cases of Brasil, China, USA, Canada, and Switzerland the electricity mixes are updated to reflect the situation in 2021. India was updated to represent the fiscal year of April 2019/March 2020. All specific cases are based on national while the remaining countries are based on global statistics.

Besides additional minor corrections, harmonization efforts were performed in order to update documentation and meta information of electricity markets, transformation and import datasets.

ecoinvent v3.10 further introduces datasets on the production of a small-scale wind power plant.

#### <strong>Forestry and Wood</strong> <a href="#en-b0041" id="en-b0041"></a>

The Forestry and Wood sector has been enhanced with the addition of three new datasets related to bamboo forestry, bamboo pole production, and flattened bamboo production in Ecuador. The data was provided by Empa (Swiss Federal Laboratories for Materials Science and Technology).

#### <strong>Fuels</strong> <a href="#en-b0043" id="en-b0043"></a>

The new version significantly expands the geographical coverage of the Oil and Gas sector. There are oil and gas production datasets from 41 different geographies, compared to the previous 27 in v3.9.1. This update increases the coverage to more than 96% of the global production of crude petroleum oil and more than 98% of natural gas output. By incorporating data from countries such as Australia, Oman, and Turkmenistan, which are key contributors to natural gas supply especially in Asian economies, we have greatly improved the representation of the sector. The new release reflects the supply situation in 2021 (previously 2019).

#### <strong>Metals</strong> <a href="#en-b0045" id="en-b0045"></a>

This update expands the data coverage of the Metals sector with new and updated data. Specifically, ecoinvent v3.10 introduces data on thermal spraying (Atmospheric Plasma Spray (APS), High Velocity OxyFuel (HVOF), and Cold Spray (CS)). Prices of rare earth oxides are also updated.

#### <strong>Pulp and Paper</strong> <a href="#en-b0047" id="en-b0047"></a>

The Pulp and Paper sector has been updated with three new datasets related to beverage carton production. Additionally, the corrugated board production datasets in the European region have been updated in accordance with the latest study conducted by the European Federation of Corrugated Board Manufacturers (FEFCO) and Cepi ContainerBoard (CCB).

#### <strong>Waste Management and Recycling</strong> <a href="#en-b0049" id="en-b0049"></a>

In version 3.10, the waste sector continues to evolve by carrying on with the second phase of the sector overhaul. The updates focus on disaggregating more than 450 solid waste treatment datasets. The users are now able to see the entire supply chain of treatment activities broken down into separate datasets. All the by-products are transparently reported, emissions are properly allocated in the respective activities generating them, while local waste transport distances are added. Moreover, the geographical coverage of the sector is enhanced, by adding solid waste treatment datasets in more other countries.

### <strong>Relevant Documents and Files</strong> <a href="#en-b0051" id="en-b0051"></a>

#### <strong>Report of Changes</strong> <a href="#en-b0052" id="en-b0052"></a>

This report covers all changes made in the ecoinvent database between version 3.10 (2023) and 3.10.1 (2024).

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Report of Changes](../assets/7139151e80d4-Change-Report-v3.10.1.pdf)

#### <strong>Report of Changes</strong> <a href="#en-b0055" id="en-b0055"></a>

This automatically generated Excel file provides an overview of changes made on the undefined unit process datasets between versions 3.9 and 3.10.1 of the ecoinvent database. The Report of Changes XLS can be found in the «Files» section of ecoQuery, the online version of the ecoinvent database version 3. It is available to licensees of the ecoinvent database.

#### <strong>Correspondence File </strong> <a href="#en-b0057" id="en-b0057"></a>

The correspondence file is a spreadsheet that lists all datasets in versions 3.10 and 3.10.1 and matches corresponding datasets between versions.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Correspondence File](../assets/bd57a6dc654d-Correspondence-File-v3.10---v.3.10.1.xlsx)

#### <strong>Database Overview File</strong> <a href="#en-b0060" id="en-b0060"></a>

The database overview file describes the contents of the database. The following information is contained in the file:

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Database Overview File](../assets/be8e63e767cc-Database-Overview-for-ecoinvent-v3.10.1.xlsx)

#### <strong>LCIA Implementation Report</strong> <a href="#en-b0063" id="en-b0063"></a>

The LCIA Implementation Report documents the implementation of LCIA methods for versions 3.10 and 3.10.1.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [LCIA Implementation Report](../assets/f9702d5ab70f-LCIA-implementation-3.10.1.pdf)

#### Version 3.10 Webinar Resources <a href="#en-b0066" id="en-b0066"></a>

[![webinar-icon](../assets/9c37f83e3b0d-webinar-icon.png)](https://youtu.be/t4p2foRfwAQ)  [Watch the "Introduction to ecoinvent version 3.10" webinar](https://youtu.be/t4p2foRfwAQ)

![doc-icon](../assets/024d8f149226-doc-icon.png)  [Download our answers to the v3.10 FAQs](../assets/15fd4ad3835e-Webinar-3.10-faqs.pdf)

![doc-icon](../assets/024d8f149226-doc-icon.png)  [Download our overview presentation covering all v3.10 updates](../assets/8f59298dbb92-Webinar-introduction-to-ecoinvent-3.10-final.pdf)

#### Known Issues <a href="#en-b0070" id="en-b0070"></a>

This section lists all known data errors in version 3.10.1 of the ecoinvent database.

#### Data Issues <a href="#en-b0072" id="en-b0072"></a>

The dataset of <strong>soybean production in Argentina (AR)</strong> reports an issue in the amount of glyphosate (3 orders of magnitude in comparison with other geographies) used in the life cycle inventory. After an internal investigation with the data provider, the right value to use for glyphosate application is 2.34kg/ha which results in 0.0009 kg/kg Soybean with a yield of 2.6 t/ha.

For all datasets of maize grain production for the US geographies (US-IA; US-IL; US-IN; US-MN; US-NE; US-SD; US-WI) the amount reported for “packaging, for fertilisers” inputs have an issue in terms of order of magnitude and value. To solve the latter, the amount of fertilizers declared in the datasets was multiplied by 0,1kg and divided by 50 kg. Finally, it is divided again per the yield of each crop to have the right amount of kg of packing for fertiliser (0,1 kg represents the weight of a plastic bag, that can deliver 50 kg of solid fertilisers). Finally, consider updating the amount of <strong>Waste Polyethylene </strong>as a sum of packaging of pesticide and fertiliser.

The right values are provided in the table below. The last column provides the new values.

<table>
<tbody>
<tr>
<td><strong>Geo</strong></td>
<td><strong>Mass of fertilizers applied (kg/ha)</strong></td>
<td><strong>Yield (kg/ha)</strong></td>
<td><strong>Fertilizers (kg) per kg of maize</strong></td>
<td><strong>Packaging, for fertilisers (kg)</strong></td>
</tr>
<tr>
<td>US-IA</td>
<td>612.845</td>
<td>12137.68</td>
<td>5.05E-02</td>
<td>1.01E-04</td>
</tr>
<tr>
<td>US-IL</td>
<td>904.376</td>
<td>
<p>12283.61</p>
</td>
<td>7.36E-02</td>
<td>1.47E-04</td>
</tr>
<tr>
<td>US-IN</td>
<td>790.638</td>
<td>11255.79</td>
<td>7.02E-02</td>
<td>
<p>1.40E-04</p>
</td>
</tr>
<tr>
<td>US-NE</td>
<td>598.361</td>
<td>11619.32</td>
<td>5.15E-02</td>
<td>1.03E-04</td>
</tr>
<tr>
<td>US-MN</td>
<td>657.264</td>
<td>11412.19</td>
<td>5.76E-02</td>
<td>1.15E-04</td>
</tr>
<tr>
<td>US-SD</td>
<td>470.343</td>
<td>9576.76</td>
<td>
<p>4.91E-02</p>
</td>
<td>
<p>9.82E-05</p>
</td>
</tr>
<tr>
<td>US-WI</td>
<td>544.923</td>
<td>10655.84</td>
<td>
<p>5.11E-02</p>
</td>
<td>
<p>1.02E-04</p>
</td>
</tr>
</tbody>
</table>

For those activities reported in the table below, there is an inconsistency between the value of the land use change, annual crop, and the specific sentence in their comment “LUC should be zero because the area planted with corn decreased in the last 20 years”. Please, do not consider the sentence. It will be removed.

<table>
<tbody>
<tr>
<td><strong>filename</strong></td>
<td><strong>activityId</strong></td>
<td><strong>activityName</strong></td>
<td><strong>geography</strong></td>
<td><strong>group</strong></td>
<td>
<p><strong>exchange name</strong></p>
</td>
</tr>
<tr>
<td>
<p>becfba64-77bf-5885-91eb-346f93c15cf0.spold</p>
</td>
<td>88ad76d4-bee8-5047-a67c-cbd7759908cf </td>
<td>maize grain production</td>
<td>US-IL</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>ba70db93-bb64-5389-9fe8-6534aa2f8d98.spold</td>
<td>56db0342-ef06-58a0-9354-8565a56e725b</td>
<td>maize grain production</td>
<td>US-IN</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>994fbb30-77ce-5368-828f-e35bddcf14fa.spold</td>
<td>468ab631-18ec-5253-94e3-e5d38e2d0b4c</td>
<td>maize grain production</td>
<td>US-MN</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>4c4b8fdf-9880-54ee-a24c-8ca481541ddd.spold</td>
<td>08e4501f-d2d1-5c1b-915a-2fb6ab55dfba</td>
<td>maize grain production</td>
<td>US-NE</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>41709364-8c82-5ba6-b8b7-3963692cb6c7.spold</td>
<td>16685855-520d-5bf7-afdb-ba21dd628014</td>
<td>maize grain production</td>
<td>US-SD</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>bb8fb857-2e4d-5c13-8dca-17bef2dda2ed.spold</td>
<td>c37ecb96-fd3e-586f-98b3-e7d74be86a84</td>
<td>maize grain production</td>
<td>US-WI</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>9c78858b-53b1-5e36-9cf9-e14e34cfac53.spold</td>
<td>17ddc472-36d2-5136-ba64-e0bf3463e898</td>
<td>soybean production</td>
<td>US-IA</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>dca15df1-60b6-5a72-a46f-a8d3c5eaba9a.spold</td>
<td>c3b36dee-8291-5815-bd98-ce098417d897</td>
<td>soybean production</td>
<td>US-IL</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>d2629e96-e19c-50fa-b9a7-5e1fccb7fbf7.spold</td>
<td>1df2e771-0fdc-5cc9-848e-c9d18e17e110</td>
<td>soybean production</td>
<td>US-IN</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>08af5cbf-676e-5ca8-8a4f-012db12323a4.spold</td>
<td>3509aedc-8ffc-5206-90e1-ff10e24b04fc</td>
<td>soybean production</td>
<td>US-MN</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>d91d68be-3484-54d8-94a8-b150a4fdee8a.spold</td>
<td>c42b3dfd-33ed-5bdf-be7b-1fc1cc5b5d10</td>
<td>soybean production</td>
<td>US-ND</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>d1172bcf-7ca5-5189-9f28-eca5c73e57df.spold</td>
<td>a0bf8ef6-2bf0-5422-bc8a-831c0c99538e</td>
<td>
<p>soybean production</p>
</td>
<td>US-NE</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>63242618-2ff4-59bd-830c-c3af5262eaaa.spold</td>
<td>82dc5349-8138-5f0d-aa63-8190f0707f28</td>
<td>soybean production</td>
<td>US-OH</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>83589be6-6e7d-5269-bb68-14d9d9854610.spold</td>
<td>19cd67e4-2809-5802-914f-0b16d8389310</td>
<td>sweet corn production</td>
<td>US-CA</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>59b4654c-fffd-59b3-9b69-277f9983a20f.spold</td>
<td>7aedd13e-cd86-5023-ac26-c0b604e7279c</td>
<td>sweet corn production</td>
<td>US-FL</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>03258297-358f-5c69-b8d1-a98b53bda391.spold</td>
<td>
<p>6228ecf0-3afb-57e5-a782-0aa27512175d</p>
</td>
<td>sweet corn production</td>
<td>US-MN</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>aae4299a-842d-59ea-9ce7-dc511f930f6e.spold</td>
<td>
<p>d4fe5ffb-f4cc-5342-bf10-44af3a70329a</p>
</td>
<td>sweet corn production </td>
<td>US-OR</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>6298f492-0e55-515f-8e87-46f2d0d005fa.spold</td>
<td>20175ff7-1d4c-54b4-bcf1-d7edbae18ca9</td>
<td>sweet corn production</td>
<td>US-WA</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
<tr>
<td>8dc185fb-6c98-5f1a-ad56-c7d51aaf9ee0.spold</td>
<td>a539f6f2-0090-5175-a640-e7d3df1fb9ee</td>
<td>sweet corn production</td>
<td>
<p>US-WI</p>
</td>
<td>From Technosphere</td>
<td>land use change, annual crop</td>
</tr>
</tbody>
</table>

#### <strong>LCIA Issues</strong> <a href="#en-b0237" id="en-b0237"></a>

<strong>ecotoxicity: freshwater</strong>

The unit for the impact category “ecotoxicity: freshwater” in the “USEtox v2.13, endpoint” methods should be “PDF.m3.day” instead of “PDF.m3.yr”.

<strong>“Methane, non-fossil” and “Carbon monoxide, non-fossil”</strong>

There is an issue with characterization factors (CFs) for “Methane, non-fossil” and “Carbon monoxide, non-fossil” in the <em>EFv3.x EN15804</em> method implementations. While the [method website](https://eplca.jrc.ec.europa.eu/LCDN/EN15804.html) only mentions differences for biogenic carbon dioxide, accounting for it with -1/+1 CFs has consequences: IPCC CFs are lower for biogenic emissions (compared to fossil ones) because a) oxidation (decay into carbon dioxide) replaces carbon dioxide that has been removed from the atmosphere and b) “for biogenic methane the soil uptake and removal of partially oxidized products is equivalent to a sink of atmospheric CO2” ([IPCC report](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/#7.6.1.3)). Accordingly, if biogenic carbon uptake and release are characterized (as in <em>EF v3.x EN15804</em> methods), CFs for biogenic methane (and in the case <em>of EF v3.0 EN15804</em> also carbon monoxide) emissions are higher than in the <em>EF v3.x</em> methods, which use IPCC CFs. This is how the current and the correct implementation would look like:

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
</tr>
<tr>
<td colspan="5">
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
</tr>
<tr>
<td colspan="5">
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

#### <strong>Australian Cereal Carbon Imbalance</strong> <a href="#en-b0268" id="en-b0268"></a>

In several Australian cereal datasets across different regions, a carbon imbalance was identified due to the incorrect assignment of embodied biogenic carbon. Specifically, the value was mistakenly allocated to the flow "Carbon dioxide, land transformation" instead of the correct flow "Carbon dioxide, non-fossil".

For the datasets reported in sheet 1, the amount of the elementary exchange "Carbon dioxide, non-fossil" has been updated to derive the emissions from burning residues. For the datasets reported in sheet 2, the comments for specific flows have been corrected accordingly.

The corrected values are provided in the spreadsheet below and will be implemented in future releases from 2026 onwards.

![doc-icon](../assets/024d8f149226-doc-icon.png) See [Australian Cereal Carbon Imbalance Corrections](../assets/98e680a1ed50-Known-Issue-v3.12_Australian-Cereal-Carbon-Corrections.xlsx)

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0056**：本页其他报告及对应文件说明比较 3.10 与 3.10.1，这里却写 3.9，可能为原文复制错误，也可能确实指另一汇总文件。 保留原文版本号，请核实 ecoQuery 的 XLS 文件覆盖范围。 [查看完整记录](../review/issues.md#issue-035)
- **已处理／已说明 · b0267**：原文化学式外层括号未闭合；译文已补全中文说明括号，化学式本身不变。 已修复中文括号，编辑原文时可补全外层右括号。 [查看完整记录](../review/issues.md#issue-036)
- **已处理／已说明 · b0017**：统一产量术语。 已修正。 [查看完整记录](../review/issues.md#issue-037)
- **已处理／已说明 · b0018**：避免中文“小1,000倍”歧义，以1/1,000明确原文比例。 已修正。 [查看完整记录](../review/issues.md#issue-038)
- **已处理／已说明 · b0015**：“高出至”表达不清，改为明确终值倍数。 已修正。 [查看完整记录](../review/issues.md#issue-039)
- **已处理／已说明 · b0267**：补全中文说明括号，不更改化学式。 已修正。 [查看完整记录](../review/issues.md#issue-040)
