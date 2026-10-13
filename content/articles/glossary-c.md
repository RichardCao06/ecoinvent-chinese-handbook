# 术语表 C

英文原题：C  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/glossary-c)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

##

[CED](#zh-b0013)

[化学需氧量（COD）](#zh-b0015)

[子数据集](#zh-b0017)

[CIF](#zh-b0019)

[条件交换](#zh-b0021)

[受约束市场](#zh-b0023)

[消耗的水（即耗水量）](#zh-b0028)

[消费组合](#zh-b0030)

[冷却水](#zh-b0032)

[CPC（产品总分类）](#zh-b0034)

[CV](#zh-b0036)

### <strong>CED</strong> <a href="#zh-b0013" id="zh-b0013"></a>

累积能源需求（Cumulative Energy Demand）的缩写。

### <strong>化学需氧量（COD）</strong> <a href="#zh-b0015" id="zh-b0015"></a>

对水中无机物和有机物消耗氧量的间接度量。该指标通过使用化学氧化剂的实验室试验测定，因此不一定与生化需氧量相关。

### <strong>子数据集</strong> <a href="#zh-b0017" id="zh-b0017"></a>

子数据集中的数值可以设定为与父数据集中的对应数值关联。父数据集中此类关联数值发生变化时，子数据集中的数值也会自动变化。ecoinvent v3 数据库只允许地理继承，即某些地区数据集（例如巴西大豆生产）可以建模为全球数据集的子数据集。

### <strong>CIF</strong> <a href="#zh-b0019" id="zh-b0019"></a>

成本、保险费加运费（Cost Insurance and Freight）的缩写。

### <strong>条件交换</strong> <a href="#zh-b0021" id="zh-b0021"></a>

只在指定系统模型下启用的交换。

### <strong>受约束市场</strong> <a href="#zh-b0023" id="zh-b0023"></a>

一种市场：需求变化的全部或部分并不表现为供应的相应变化，而是表现为其他地方消费量的变化。

受约束市场数据集包含一个条件交换，该交换通过直接活动链接连接到受需求变化影响的消费活动。此交换只在考虑市场约束的特定系统模型中启用，例如后果型系统模型。

选择“按分类截断的分配模型（allocation, cut-off by classification）”、“替代点分配模型（allocation at the point of substitution，APOS）”或“EN15804 截断分配模型（allocation, cut-off, EN15804）”时，条件交换不启用，受约束市场的行为与其他市场相同。

如需了解此类市场在后果型链接中的行为，请参阅《数据质量指南》。

### <strong>消耗的水（即耗水量）</strong> <a href="#zh-b0028" id="zh-b0028"></a>

取用后未返回原水源的水，例如因蒸发、蒸散、进入产品或排放至其他流域或海洋而未返回。

### <strong>消费组合</strong> <a href="#zh-b0030" id="zh-b0030"></a>

市场活动的输出。

### <strong>冷却水</strong> <a href="#zh-b0032" id="zh-b0032"></a>

用于调节过程温度的水。这类水在多数情况下不与产品接触。

### <strong>CPC（产品总分类）</strong> <a href="#zh-b0034" id="zh-b0034"></a>

对包括货物和服务在内的所有产品进行全面分类的体系。产品总分类根据货物的物理特征或所提供服务的性质进行分类；CPC 所区分的每类货物或服务，其定义通常使其仅由 ISIC 定义的一种活动生产。ecoinvent 中心使用 CPC 分类对 ecoinvent 数据库中的产品（中间交换）进行分类。

### <strong>CV</strong> <a href="#zh-b0036" id="zh-b0036"></a>

变异系数（原文英文为 Coefficient of Variance）的缩写。

{% endtab %}

{% tab title="English 原文" %}

##

[CED](#en-b0013)

[Chemical Oxygen Demand (COD)](#en-b0015)

[Child Dataset](#en-b0017)

[CIF](#en-b0019)

[Conditional Exchange](#en-b0021)

[Constrained Market](#en-b0023)

[Consumed Water (= Water Consumption)](#en-b0028)

[Consumption Mix](#en-b0030)

[Cooling Water](#en-b0032)

[CPC (Central Product Classification)](#en-b0034)

[CV](#en-b0036)

### <strong>CED</strong> <a href="#en-b0013" id="en-b0013"></a>

Abbreviation for Cumulative Energy Demand

### <strong>Chemical Oxygen Demand (COD)</strong> <a href="#en-b0015" id="en-b0015"></a>

An indirect measure of the amount of oxygen used by inorganic and organic matter in water. The measure is a laboratory test based on a chemical oxidant and therefore does not necessarily correlate with biochemical oxygen demand.

### <strong>Child Dataset</strong> <a href="#en-b0017" id="en-b0017"></a>

In child datasets values can be set to relate to the corresponding value in the parent dataset. When such a related value is changed in the parent dataset it is automatically changed in the child dataset as well. Only geographical inheritance is allowed in the ecoinvent v3 database, i.e. some regional datasets (such as Brazilian soybean production) might be modelled as a child dataset of the global dataset.

### <strong>CIF</strong> <a href="#en-b0019" id="en-b0019"></a>

Abbreviation for Cost Insurance and Freight

### <strong>Conditional Exchange</strong> <a href="#en-b0021" id="en-b0021"></a>

Exchange that is only activated for a specified system model.

### <strong>Constrained Market </strong> <a href="#en-b0023" id="en-b0023"></a>

A market where all or part of a change in demand is not reflected in a corresponding change in supply, but instead in a change in consumption elsewhere.

Constrained market datasets include a conditional exchange with a direct activity link to the consumption activity that is affected by the change in demand. This exchange is activated only for specific system models that take into account market constraints, e.g. the consequential system model.

When the system models "allocation, cut-off by classification", "allocation at the point of substitution (APOS)" and "allocation, cut-off, EN15804" are chosen, the conditional exchange is not activated and the constrained markets behave like any other markets.

To understand how this market behaves during consequential linking, please see the Data Quality Guideline.

### <strong>Consumed Water (= Water Consumption)</strong> <a href="#en-b0028" id="en-b0028"></a>

Water withdrawal where release back to the source does not occur, e.g. due to evaporation, evapotranspiration, product integration or discharge into a different drainage basin or the sea.

### <strong>Consumption Mix</strong> <a href="#en-b0030" id="en-b0030"></a>

The output from a market activity.

### <strong>Cooling Water</strong> <a href="#en-b0032" id="en-b0032"></a>

Water that is used to regulate the temperature of a process. This type of water in most cases does not come in contact with the product.

### <strong>CPC (Central Product Classification)</strong> <a href="#en-b0034" id="en-b0034"></a>

Constitutes a comprehensive classification of all products, including goods and services. The central product classification is a classification based on the physical characteristics of goods or on the nature of the services rendered; each type of good or service distinguished in the CPC is defined in such a way that it is normally produced by only one activity as defined in ISIC. The CPC classification is used by the ecoinvent Centre for classification of products (intermediate exchanges) present in the ecoinvent database.

### <strong>CV</strong> <a href="#en-b0036" id="en-b0036"></a>

Abbreviation for Coefficient of Variance

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0037**：统计术语 CV 通常展开为 coefficient of variation，原文采用 variance。中文使用规范名称，并保留原文英文供核对。 确认术语定义是否指标准差与平均值之比，并修正原文英文展开。 [查看完整记录](../review/issues.md#issue-143)
