# 从 ecoSpold1 到 ecoSpold2 的变化

英文原题：Changes ecoSpold1 to ecoSpold2  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/changes-ecospold1-to-ecospold2)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

## 对于 2013 年 5 月发布的 ecoinvent 数据库新版本 3，ecoSpold 格式 2 取代了 ecoSpold 格式 1。 <a href="#zh-b0002" id="zh-b0002"></a>

2023 年 10 月 30 日

### <strong>结构变化</strong> <a href="#zh-b0004" id="zh-b0004"></a>

在 ecoSpold1 中，三种数据集（基本流、过程和影响类别）均采用同一数据集结构处理。在 ecoSpold2 中，这三种数据集采用各自独立的数据集定义。“过程”改称“活动”；“基本流”改称“与环境的交换”。“基本流”“产品和废物”以及“位置”均有主列表。通过 UUID 引用这些主列表中的条目。

### <strong>便于数据库维护和扩展</strong> <a href="#zh-b0006" id="zh-b0006"></a>

- 可在活动数据集之间设置父子关系
- 可使用 GIS 坐标表示地理信息
- 可在数值字段中使用公式和变量
- 在数据集中使用 UUID 进行内部引用
- 新增用于声明预测活动的宏观经济情景的字段

### <strong>替代建模方式及与 ILCD 的数据交换</strong> <a href="#zh-b0012" id="zh-b0012"></a>

提供了对替代建模选项以及与 ILCD 格式进行数据交换的更好支持：

- 可声明活动所采用的市场模型（归因型或后果型）
- 活动（过程）名称与单一产品输出名称之间的直接关联已不再使用
- 减少必填字段的数量
- 新增用于声明活动技术水平的字段（新兴、现代、当前、旧有、过时）
- 新增用于将活动声明为市场活动的字段
- 增加通配元素，以便更简单地扩展格式

### <strong>支持质量、能量和货币平衡</strong> <a href="#zh-b0020" id="zh-b0020"></a>

- 取消了过程/活动的类别与子类别概念，转而引入声明多种分类体系、标签及交换的多种属性的选项，例如价格、干质量、含水率、能量含量、元素组成或物质组成。
- 新增用于声明年产量的字段
- 新增输出类型：“资本品增加”

- 新增用于声明产品转移系数（相对于投入的输出）的字段

### <strong>支持不同语言版本</strong> <a href="#zh-b0025" id="zh-b0025"></a>

现在可以为所有文本字段添加不同语言版本。

### <strong>支持更完善的文档记录</strong> <a href="#zh-b0027" id="zh-b0027"></a>

- 可添加图像
- 可添加多名验证者
- 使不确定性信息字段更通用，并为数据质量谱系矩阵增加数值字段

{% endtab %}

{% tab title="English 原文" %}

## The ecoSpold format 2 replaces the ecoSpold format 1 for the new version 3 of the ecoinvent database released in May 2013. <a href="#en-b0002" id="en-b0002"></a>

Oct 30th, 2023

### <strong>Structural Change </strong> <a href="#en-b0004" id="en-b0004"></a>

In ecoSpold1 the three types of datasets (elementary flow, process, and impact category) were all handled within the same dataset structure. In ecoSpold2, separate dataset definitions are applied for these three. “Process” is called “Activity”. “Elementary flows” are called “Exchanges with environment”. Master lists are available for “Elementary flows” as well as for “Products and Wastes” and “Locations”. The references to entries in these master lists will be made through UUIDs.

### <strong>Facilitating Database Maintenance and Extension</strong> <a href="#en-b0006" id="en-b0006"></a>

- Option for parent-child relationships between activity datasets
- Option for expressing geographical information using GIS coordinates
- Option to use formulas and variables in numerical fields
- Use of UUIDs for internal references in datasets
- New field to declare macro-economic scenario for forecasted activities

### <strong>Alternative Modeling and Data Exchange with ILCD</strong> <a href="#en-b0012" id="en-b0012"></a>

Better support for alternative modeling options and data exchange with the ILCD format is provided:

- Option to declare the market model (attributional, consequential) used for an activity
- The direct linking of an activity (process) name and single product output name has become obsolete.
- Reduction of the number of required fields
- New field to declare technology level for activities (new, modern, current, old, outdated)
- New field to declare an activity as a market activity
- Addition of joker elements to enable simpler extension of the format

### <strong>Support for Mass, Energy and Monetary Balances </strong> <a href="#en-b0020" id="en-b0020"></a>

- The category/subcategory concept for processes/activities has been dropped. Instead, options have been introduced to declare multiple classification schemes, tags, and multiple properties of exchanges, e.g. price, dry mass, water content, energy content, elementary or substance composition
- New field to declare annual production volume
- New output type: “addition to capital goods”

- New field to declare product transfer coefficients (outputs relative to inputs)

### <strong>Support for Language Versions</strong> <a href="#en-b0025" id="en-b0025"></a>

You now have the option to add language versions for all text fields.

### <strong>Support for Better Documentation</strong> <a href="#en-b0027" id="en-b0027"></a>

- Option to add images
- Option to add more than one validator
- Fields for uncertainty information made more general and adding numerical fields for the pedigree matrix

{% endtab %}

{% endtabs %}
