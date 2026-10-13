# 数据库简介

英文原题：Introduction to the Database  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/introduction-to-the-database)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-11-05

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库包含超过 26,000 个可靠的生命周期清单数据集，覆盖多个部门。 <a href="#zh-b0002" id="zh-b0002"></a>

2025 年 11 月 5 日

在[此处](ecoinvent-version-3.12.md)查看 ecoinvent 数据库最新版本的更新。

这些部门包括农业和畜牧业、建筑与施工、化学品与塑料、能源、林业与木材、金属、纺织、运输、旅游住宿、废物处理与回收利用、供水，以及其他工业部门。

在[此处](sector-overview.md)查看全部部门。

ecoinvent 数据库中的每个活动均对应一个地理位置。地理位置也称“[地理区域](geographies.md)”，采用国际通用缩写，并作为数据集名称的一部分。由于 ecoinvent 是背景数据库，其目标是覆盖所选产品或服务最相关地理区域中的活动。同时，地理覆盖范围取决于数据质量和可获得性。因此，数据库中几乎每个活动都有一个代表全球过程的数据集，即全球平均生产。

ecoinvent 数据库中的每个数据集均提供若干影响评价方法（如“IPCC 2021”“EF v3.1”或“ReCiPe”）及相应影响类别（如“气候变化”“人体毒性”“用水”或“土地利用”）的[生命周期影响评价](upr-lci-lcia.md)（LCIA）得分。

数据库的结构允许用户追踪其产品整个供应链的影响，并理解所得结果。此外，该结构提供灵活性，允许根据用户需求以不同方式使用数据。除了单个产品的[LCIA](upr-lci-lcia.md) 影响评价得分（数据库基础知识：影响评价），<strong>用户还可能关注排放特征、物料清单、物质流、质量核算、水核算和碳核算，或平均技术组合等。</strong>

ecoinvent 数据库是代表工业或农业过程的活动库，每个活动都产生相应产品。每个活动也可称为[单元过程（UPR）](upr-lci-lcia.md)。ecoinvent 数据库最新版本包含超过 25,000 个过程，覆盖所有[经济部门](sector-overview.md)的约 3,500 种不同产品。

ecoinvent 数据库中的过程代表某地理位置内的平均生产条件，而非特定企业或特定场址的条件。例如，数据库包含厄瓜多尔香蕉平均生产的过程，而非某家水果公司某个农场的香蕉生产。此外，所含产品主要是中间产品，而非最终消费品。例如，数据库包含小麦粉，但不包含用该面粉制成的意大利面。

### 数据库概览 <a href="#zh-b0012" id="zh-b0012"></a>

数据库概览文件描述数据库的内容，其中包含以下信息：

- #### 活动概览 <a href="#zh-h4" id="zh-h4"></a>

  未指定系统模型数据以及四种[系统模型](system-models.md)各自的活动概览，提供相应系统模型在数据库中可用的全部数据集清单。可按活动名称，或使用联合国产业分类体系 ISIC（所有经济活动的国际标准产业分类）搜索特定过程的数据集。此外，每个数据集被归入一个或多个部门（如电力、木材、运输等），便于识别属于同一部门的过程。也可根据数据集所生产的产品搜索，使用产品名称或产品的 CPC（产品总分类）进行检索。
- #### ecoinvent 地理区域 <a href="#zh-h5" id="zh-h5"></a>

  列出 ecoinvent 数据库中使用的[地理区域](geographies.md)，提供地理区域类型（国家、地区等），以及各地理区域相互重叠情况的信息。
- #### <strong>LCIA 方法</strong> <a href="#zh-h6" id="zh-h6"></a>

  列出 ecoinvent 计算影响得分所采用的[生命周期影响评价（LCIA）方法](upr-lci-lcia.md)的全部指标，提供方法版本，以及查找不同方法文档和表征因子原始来源的信息。

### 数据质量指南 <a href="#zh-b0017" id="zh-b0017"></a>

数据质量指南描述 ecoinvent 数据库建模所依据的方法体系。该文档包含所用 LCA 方法、数据库总体结构、数据提交具体指南、审阅流程说明以及系统模型详细说明等信息。

![doc-icon](../assets/024d8f149226-doc-icon.png) 查看[数据质量指南](../assets/ef4af7c44cd6-dataqualityguideline_ecoinvent_3_20130506.pdf)

{% endtab %}

{% tab title="English 原文" %}

## The ecoinvent database contains more than 26,000 reliable life cycle inventory datasets, covering a range of sectors. <a href="#en-b0002" id="en-b0002"></a>

Nov 5th, 2025

See the updates on the newest version of the ecoinvent database [here](ecoinvent-version-3.12.md).

These include agriculture and animal husbandry, building and construction, chemicals and plastics, energy, forestry and wood, metals, textiles, transport, touristic accommodation, waste treatments and recycling, and water supply, among other industrial sectors.

See all sectors [here](sector-overview.md)

Each activity in the ecoinvent database is attributed to a geographic location. Geographic locations, otherwise referred to as "[geographies](geographies.md)," are reported using internationally accepted abbreviations as part of the dataset’s name. As the ecoinvent database is a background database, the aim is to cover activities in the most relevant geographies for the selected product or service. At the same time, geographic coverage is dependent on data quality and availability. Thus, almost every activity in the database features a dataset representing the process globally, meaning the average global production.

For each dataset in the ecoinvent database, [Life Cycle Impact Assessment](upr-lci-lcia.md) (LCIA) scores for several impact assessment methods (such as “IPCC 2021”, “EF v3.1”, or “ReCiPe”) and corresponding impact categories (such as “climate change,” “human toxicity,” “water use,” or “land use”) are available.

The structure of the database allows users to trace the impacts of their products throughout the supply chain and understand their results. Moreover, it grants flexibility as it allows different uses of the data depending on the users’ needs. Apart from the [LCIA](upr-lci-lcia.md) Database Fundamentals Impact Assessment scores for individual products, <strong>users may, for example, also be interested in emission profiles, bills of materials, material flows, mass, water and carbon accounts, or average technology mixes. </strong>

The ecoinvent database is a library of activities representing industrial or agricultural processes, each generating a resulting product. Each of these activities can also be called a [unit process (UPR)](upr-lci-lcia.md). Over 25,000 processes covering around 3,500 distinct products across all [economic sectors](sector-overview.md) are included in the latest version of the ecoinvent database.

The processes in the ecoinvent database represent the average production conditions within a geographical location, rather than company-specific or site-specific conditions. For example, the ecoinvent database would contain a process for the average banana production in Ecuador, rather than for banana production at the farm of a specific fruit company. Furthermore, the contained products are primarily intermediate products rather than final consumer products. For example, the database would contain wheat flour but not pasta made from that flour.

### Database Overview <a href="#en-b0012" id="en-b0012"></a>

The database overview file describes the contents of the database. The following information is contained in the file:

- #### Activity Overview <a href="#en-h4" id="en-h4"></a>

  The activity overview for the undefined data and each of the four [system models](system-models.md) provide a list of all datasets that are available in the database for the respective system model. Datasets for specific processes can be searched for by activity name or by using the United Nations industry classification system, ISIC (International Standard Industrial Classification of All Economic Activities). Additionally, each dataset is assigned to one or more sectors (e.g., Electricity, Wood, Transport, etc.), which allows to easily identify processes that belong to the same sector. Datasets can also be searched based on the product(s) they produce, either using the product name or based on the CPC (Central Product Classification) of the product.
- #### ecoinvent Geographies <a href="#en-h5" id="en-h5"></a>

  The [geographies](geographies.md) used in the ecoinvent database are listed. The type of geography (country, region, etc.) is provided, as well as information about how the geographies overlap each other.
- #### <strong>LCIA Methods</strong> <a href="#en-h6" id="en-h6"></a>

  The list of all indicators of the [life cycle impact assessment (LCIA) methods](upr-lci-lcia.md) for which ecoinvent calculates impact scores is given. The versions of the methods are provided, as well as information on where to find the documentation and original source of the characterisation factors of the different methods.

### Data Quality Guidelines <a href="#en-b0017" id="en-b0017"></a>

The Data Quality Guidelines describe the methodology behind the modeling of the ecoinvent database. This document contains information on the applied LCA methodology, the general structure of the database, specific guidelines for data submission, a description of the review process, as well as a detailed description of the system models.

![doc-icon](../assets/024d8f149226-doc-icon.png)  See [Data Quality Guidelines](../assets/ef4af7c44cd6-dataqualityguideline_ecoinvent_3_20130506.pdf)

{% endtab %}

{% endtabs %}
