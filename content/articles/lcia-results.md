# 关于生命周期影响评价（LCIA）

英文原题：About Life Cycle Impact Assessment (LCIA)  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/lcia-results)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

##

2024 年 2 月 1 日

### <strong>什么是生命周期影响评价（LCIA）？ecoinvent 数据库提供哪些方法？</strong> <a href="#zh-b0003" id="zh-b0003"></a>

了解生命周期影响评价（LCIA）以及 ecoinvent 中实施的 LCIA 方法的更多信息，请参阅[此处。](impact-assessment.md)

ecoinvent 提供按照 IPCC 2021 计算的 LCIA 得分（或“碳足迹”“排放因子”）。[此处提供相关指南](guidance-on-ipcc-methods.md)。

### 为何同一产品的 LCIA 结果会随版本变化？ <a href="#zh-b0006" id="zh-b0006"></a>

环境影响建模取决于大量假设，有时很难确定哪些假设最重要。同样，要了解改变某项假设会带来什么后果也十分困难。当某项影响得分在数据库不同版本之间发生变化时，需要开展详细分析，才能明确变化的确切来源。不过，潜在原因可归为三类：

#### 数据集更新 <a href="#zh-b0008" id="zh-b0008"></a>

当获得更新或质量更高的数据，或检测到错误时，会修改相关数据集中的数值。这可能涉及某些排放、自然资源和中间产品的数量或性质。如果数据集具有多个输出且采用经济分配，价格变化会影响该数据集的结果。分配方法本身也可能发生变化。

#### 供应链变化 <a href="#zh-b0010" id="zh-b0010"></a>

生命周期评价考虑产品和服务整个供应链的影响。若某个数据集发生变化，其他数据集的影响也会发生变化，对于电力、运输和基础设施等常用数据集尤其如此。要将一个数据集的变化与另一个数据集得分的变化联系起来，需要借助软件工具并仔细检查供应链。

#### 影响评价方法变化 <a href="#zh-b0012" id="zh-b0012"></a>

方法开发者提供的表征因子会定期更新，而 ecoinvent 对方法的实施有时也可能出现错误。影响得分显然对表征因子的变化敏感。

为帮助分析得分变化，数据库每个新版本都会编制变更报告。报告附件中的电子表格列出所有影响得分的数据集变化，Word 文档则说明这些变化的原因。该报告可在 ecoQuery 的“文件”（Files）部分获取。

#### “LT”和“No LT”是什么意思？ <a href="#zh-b0015" id="zh-b0015"></a>

简而言之，LT 表示长期，用于归类通常来自填埋场、在填埋发生超过 100 年后才释放至空气或渗入地下水的排放。

#### 二者有什么区别？ <a href="#zh-b0017" id="zh-b0017"></a>

LT 表示长期。如果某项排放在所考虑生命周期活动发生超过 100 年后才释放到环境中，则被归为“长期”排放。因此，“长期”分类的决定因素是排放释放到环境中的时刻，而不是其产生影响的时刻。这与例如农药在食物链中生物累积所引起的长期影响不同。

#### ecoinvent 为什么区分 LT 和 No LT？ <a href="#zh-b0019" id="zh-b0019"></a>

迄今，LCA 专家尚未就是否以及如何考虑长期排放达成共识。在争论解决之前，ecoinvent 允许用户自行决定是否纳入长期排放。因此，长期排放通过两个明确标记为“long-term”的子区室单独报告，即“air, low population density, long-term”（空气，低人口密度，长期）和“water, ground-, long-term”（水，地下水，长期）。这些交换仅存在于废物处理数据集中，其中假设填埋场的主动维护在 100 年后结束。由于长期排放在环境中的存在时间比短期排放少 100 年，其表征因子（CF）应较低。然而，大多数 LCIA 方法不区分时间范围。因此，有两种可行选项：

为短期和长期排放赋予相同的 CF，会高估影响。不给长期排放赋予 CF，则会低估影响。

ecoinvent 提供两种选项的结果，使您能够检验结论的敏感性。不包含长期排放的结果通过明确标记为“no-LT”的方法提供。

{% endtab %}

{% tab title="English 原文" %}

##

Feb 1st, 2024

### <strong>What is a Life Cycle Impact Assessment (LCIA)? Which Methods are Available in the ecoinvent Database?</strong> <a href="#en-b0003" id="en-b0003"></a>

Learn more about Life Cycle Impact Assessment (LCIA) and LCIA methods implemented in ecoinvent [here.](impact-assessment.md)

ecoinvent offers LCIA scores (or “carbon footprints” or “emission factors”) following IPCC 2021. [Guidance can be found here](guidance-on-ipcc-methods.md).

### Why do LCIA Results of a Product Change Between Versions? <a href="#en-b0006" id="en-b0006"></a>

Modeling of environmental impacts depends on an overwhelming number of assumptions, and it is sometimes hard to know which ones are the most important. It is equally difficult to know what are the consequences of changing an assumption. When confronted with an impact score changing across different versions of the database, a detailed analysis is required to know the exact sources of the change. However, the potential reasons can be grouped in three categories:

#### Dataset Updates <a href="#en-b0008" id="en-b0008"></a>

When newer or better quality data become available, or when an error is detected, values within the dataset at hand are changed. These can be quantities or nature of certain emissions, natural resource and intermediate products. If the dataset is multi-output and economic allocation is applied, a change in price will affect the results of the dataset. The allocation method might also have changed.

#### Supply Chain Changes <a href="#en-b0010" id="en-b0010"></a>

LCA takes into account the impact of the whole supply chain of products and services. If a dataset is changed, the impact of the other datasets will also be changed. This is especially true for commonly used datasets like electricity, transport and infrastructures. Linking a change in a dataset to a change of score in another dataset require a software tool and careful inspection of the supply chain.

#### Change in Impact Assessment Methods <a href="#en-b0012" id="en-b0012"></a>

The characterisation factors provided by the method developers are regularly updated, and sometimes, there is a mistake in the implementation made by ecoinvent. The impact scores are obviously sensitive to a change of characterisation factors.

To help analyze changes in scores, a change report is produced for each new version of the database. The spreadsheet in annex of the report lists all the dataset changes that affect scores, and the word document clarifies the reasons for those changes. This report is available in the file section of ecoQuery.

#### What Does 'LT' and 'No LT' Mean? <a href="#en-b0015" id="en-b0015"></a>

In a nutshell: LT stands for long-term and classifies emissions, usually from landfills, which are released into the air or leach into the groundwater more than 100 years after the landfilling happened.

#### What’s the Difference? <a href="#en-b0017" id="en-b0017"></a>

LT stands for long-term. An emission is classified as “long-term” if it is released to the environment more than 100 years after the activities considered in the life cycle took place. Decisive for the classification “long-term” is thus the moment at which an emission is released in the environment and not the moment at which it causes its impact. It is, therefore, different from long-term impacts that would be caused, for example, by the bioaccumulation of a pesticide in the food chain.

#### Why Does ecoinvent Distinguish Between LT and No LT? <a href="#en-b0019" id="en-b0019"></a>

So far no consensus has been reached among LCA experts if and how long-term emissions should be taken into account. Until the debate is settled, ecoinvent allows users to decide themselves whether to include it. Therefore, long-term emissions are reported separately via two subcompartments explicitly labeled as “long-term”, namely “air, low population density, long-term” and “water, ground-, long-term”. Those exchanges are exclusively present in waste treatment datasets, where it is assumed that the active landfill maintenance ends after 100 years. Since long term emissions are in the environment 100 years less than short term emissions, their CF should be lower. However, most LCIA methods do not provide a distinction of time horizons. Thus, two options are possible:

Attribute the same CF to both short term and long-term emissions, leading to an over-estimation of the impacts. Attribute no CF to the long-term emission, leading to an under-estimation of the impacts.

ecoinvent provides the results for both options, allowing you to test the sensitivity of your conclusions. The results without long-term emissions are available in methods explicitly labeled as “no-LT”.

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **已处理／已说明 · b0014**：统一文档名称为“变更报告”。 已修正。 [查看完整记录](../review/issues.md#issue-153)
