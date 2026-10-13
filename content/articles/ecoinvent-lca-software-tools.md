# ecoinvent 与 LCA 软件工具

英文原题：ecoinvent and LCA Software Tools  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecoinvent-lca-software-tools)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

##

2023年9月27日

### <strong>哪些软件工具集成了 ecoinvent 数据？</strong> <a href="#zh-b0003" id="zh-b0003"></a>

ecoinvent 数据库已集成到所有领先的 LCA 软件工具及许多简化的生态设计工具中。

### <strong>SimaPro、GaBi、Umberto、openLCA 等软件与 ecoinvent 数据库有什么区别？</strong> <a href="#zh-b0005" id="zh-b0005"></a>

ecoinvent 数据库是生命周期清单（LCI）数据库。SimaPro、GaBi、Umberto 和 openLCA 是不同软件供应商提供的[LCA 软件工具](https://ecoinvent.org/partners/)。ecoinvent 数据库已在所有领先软件工具中实施。当整个 ecoinvent 数据库被纳入某一软件工具时，该供应商就是 ecoinvent 数据库的经销商。用户可以通过这些经销商获取 ecoinvent 数据库许可证和更新。这些 LCA 软件也可能包含其他数据库。

### <strong>为什么某产品在 ecoinvent 数据库中的 LCIA 结果值与我的软件工具中的不同？</strong> <a href="#zh-b0007" id="zh-b0007"></a>

#### <strong>表征因子的变化</strong> <a href="#zh-b0008" id="zh-b0008"></a>

影响评价方法会定期更新，以反映最新科学进展、新增的因果机制和更新的数据等。ecoinvent 使用方法开发者发布的结果，计算所求得生命周期清单（LCI）的环境影响。

影响评价方法的实施并不总是直接且无歧义。方法开发者计算表征因子（CF）时所采用的假设，往往与 LCI 结果不兼容。

例如，有些方法要求准确掌握排放因子的地理位置，以选择合适的 CF。

其他方法需要有关排放某些属性的信息，例如水质。有些方法会表征水或材料的耗散性使用，但 LCI 中没有直接包含这些信息。

对于化学品、土地利用和材料开采基本流交换，方法开发者使用的命名规则往往与 ecoinvent 不同。在多数情况下，CAS 编号可提供帮助，但并非总有 CAS 编号；对农药等某些物质，商品名称存在歧义，且含有多种活性物质，因此会列出多个 CAS 编号。

某些方法没有为某种物质在 ecoinvent 中的所有子区室提供 CF。例如，如果方法没有明确提及地下水的 CF，那么化学品排放到地下水时，是否应使用与排放到地表水时相同的 CF？

不同参与者（方法开发者、数据库管理者和软件开发者）对如何解决歧义可能有不同意见。

最后，在管理和汇总大量来自不同来源的信息时，人为错误也难以完全避免。

#### <strong>ecoinvent 与 LCA 软件中的结果值不同</strong> <a href="#zh-b0017" id="zh-b0017"></a>

由于上述原因，ecoinvent 使用的 CF 有时与软件中的不同。ecoinvent 无权强制其他 LCA 参与者采用其实施选择。LCA 社群中的参与者大致按专业分为清单和影响评价两个领域。在清单中实施影响评价方法，恰好处于这两个专业的交界，因而存在难以协调之处。对于这一特定任务，并没有作为权威的监管机构。

#### <strong>透明的实施过程</strong> <a href="#zh-b0019" id="zh-b0019"></a>

ecoinvent 已开始采取以下措施，以提高透明度：

- 改进 LCIA 实施文档。ecoQuery 的文件部分包含详细实施报告，说明 CF 的来源及其如何映射到 ecoinvent 基本流交换。这些报告经过独立专家或方法开发者审查。
- 记录与软件之间的实施差异。ecoinvent 已开始与软件开发者合作，以尽量减少这些差异。发布之前，会向软件开发者分享实施方案并识别差异。双方讨论差异的来源，持有许可证的用户可在 ecoQuery 文件部分获取相关电子表格。

#### <strong>在哪里获取 LCIA 结果和支持文档</strong> <a href="#zh-b0023" id="zh-b0023"></a>

所有文档和支持文件都位于 ecoQuery 的文件部分，持有有效 ecoinvent 许可证的数据库用户可以访问。

#### <strong>为什么我的软件中的系统模型名称不同？</strong> <a href="#zh-b0025" id="zh-b0025"></a>

软件供应商使用的术语不总是与 ecoinvent 数据库的术语一致。

例如，在 8.5 版发布前，SimaPro 使用与 ecoinvent 不同的名称。“Allocation cut-off by classification”（按分类截断的分配）称为“Allocation, recycled content”（分配，再生材料含量，简称 Alloc Rec）。“Allocation, default”（分配，默认）在 ecoinvent 3.2 版中更名为“Allocation at the point of substitution”（替代点分配，APOS），而 SimaPro 在 8.5 版之前仍使用旧名称，简称 Alloc Def。“Substitution, Consequential, Long-Term”（长期后果型替代）则简称“Consequential”（后果型，Conseq）。

在 SimaPro [8.5 版](https://www.pre-sustainability.com/download/manuals/SimaPro85WhatIsNew.pdf)中，名称已与 ecoinvent 统一。

{% endtab %}

{% tab title="English 原文" %}

##

Sep 27th, 2023

### <strong>Which Software Tools Integrate the ecoinvent Data?</strong> <a href="#en-b0003" id="en-b0003"></a>

The ecoinvent database is integrated in all leading LCA software tools as well as many simplified ecodesign tools.

### <strong>What is the Difference Between SimaPro or GaBi, Umberto, openLCA, etc. and the ecoinvent Database?</strong> <a href="#en-b0005" id="en-b0005"></a>

The ecoinvent database is a Life Cycle Inventory (LCI) database. SimaPro, GaBi, Umberto and openLCA are [LCA software tools](https://ecoinvent.org/partners/) provided by different software providers. The ecoinvent database is implemented in all of the leading software tools. When the whole ecoinvent database is incorporated into a particular software tool, the provider acts as a reseller of the ecoinvent database. Users can acquire licenses and updates of the ecoinvent database through these resellers. These LCA software may also include other databases.

### <strong>Why is the LCIA Score of a Certain Product not the Same in the ecoinvent Database and in my Software Tool?</strong> <a href="#en-b0007" id="en-b0007"></a>

#### <strong>Changes to the Characterisation Factors</strong> <a href="#en-b0008" id="en-b0008"></a>

Impact assessment methods are regularly updated to reflect the newest scientific advances, the inclusion of new mechanisms of cause-and-effect, newer data, etc. ecoinvent uses the results published by method developers to calculate the impacts of the calculated life cycle inventories (LCI).

The implementation of impact assessment methods is not always straightforward and unambiguous. The method developers often calculate characterisation factors (CFs) with assumptions that are not compatible with the results of LCIs.

For example, some methods require precise knowledge of the geographical location of an emission factor to select the appropriate CF.

Other methods ask for information about some properties of the emissions, like water quality. Some methods characterize for example dissipative use of water or materials when this information is not directly present in the LCI.

Method developers often use different naming conventions than ecoinvent for chemicals, land use, and material extraction elementary exchanges. In most cases, a CAS number can help, but these are not always present, or for some substances like pesticides, commercial names are ambiguous, contain a mix of active substances, and therefore report more than one CAS number.

Some methods do not carry CFs for a substance in all the sub-compartments present in ecoinvent. For example, should a chemical emission to groundwater receive the same CF as the same emission to surface water, if the groundwater CF is not explicitly mentioned in the method?

Different actors (method developers, database managers, software developers) might have different opinions about how to resolve ambiguities.

Finally, plain old human mistakes are bound to happen when managing and aggregating a large quantity of information coming from disparate sources.

#### <strong>Different Scores in ecoinvent and the LCA Software </strong> <a href="#en-b0017" id="en-b0017"></a>

For all these reasons, CFs used by ecoinvent sometimes differ from what is found in software. ecoinvent is not in a position to impose its implementation choices on the other actors in LCA. The actors in the LCA community are mostly divided by their specialization: inventory and impact assessment. The implementation of impact assessment methods on the inventory sits uncomfortably at the interface of these two specializations. There is no regulatory body acting as an authority for this particular task.

#### <strong>Transparent Implementation</strong> <a href="#en-b0019" id="en-b0019"></a>

ecoinvent has started taking the following steps in the direction of greater transparency:

- Better LCIA implementation documentation. The file section of ecoQuery contains a detailed implementation report, showing the source of the CFs and how they were mapped to the ecoinvent elementary exchanges. These reports are reviewed by independent experts or by the method developer.
- Documentation of implementation differences with software. ecoinvent has started to engage with software developers to minimize those differences. Prior to a release, the implementation is shared to the software and differences are identified. The source of these differences is discussed, and a spreadsheet is available in the file section of ecoQuery for users with a license.

#### <strong>Where to Find the LCIA Results and Supporting Documents </strong> <a href="#en-b0023" id="en-b0023"></a>

All the documentation and supporting files are available in the files section in the ecoQuery accessible to the users of the database who hold a valid ecoinvent license.

#### <strong>Why are System Models Named Differently in my Software? </strong> <a href="#en-b0025" id="en-b0025"></a>

The terminology used by software providers does not always match the one used in the ecoinvent database.

For example, before the release of version 8.5, SimaPro used different names from ecoinvent. “Allocation cut-off by classification” was named “Allocation, recycled content” (Alloc Rec). “Allocation, default” was renamed “Allocation at the point of substitution” (APOS) in ecoinvent version 3.2., while, SimaPro, until version 8.5, used the old naming abbreviated as Alloc Def. “Substitution, Consequential, Long-Term” is simply called “Consequential” (Conseq).

In SimaPro [version 8.5](https://www.pre-sustainability.com/download/manuals/SimaPro85WhatIsNew.pdf), the names have been harmonized with ecoinvent.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **已处理／已说明 · b0014**：统一 sub-compartment 的数据库结构术语，避免与一般环境介质概念混淆。 已修正译稿并重新核对原文。 [查看完整记录](../review/issues.md#issue-013)
