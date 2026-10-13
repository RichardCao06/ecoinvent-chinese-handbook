# ecoSpold2

英文原题：ecoSpold2  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/ecospold2)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-09-26

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## ecoSpold2 格式用于创建 ecoinvent 第 3 版的生命周期清单。该格式规定标准生命周期清单中哪些字段为必填、哪些字段为可选。 <a href="#zh-b0002" id="zh-b0002"></a>

2023 年 10 月 30 日

在 2013 年 5 月发布的 ecoinvent 第 3 版中，ecoSpold2 格式取代了 ecoSpold1 格式。LCA 软件领域的新发展要求修订数据格式。ecoinvent 成立了一个临时专家工作组来指导修订过程，并在 ecoSpold 格式用户中开展了公开征求意见。征求意见的结果及反馈的处理方式见[这份公开报告](../assets/58422431916f-200905_ecospold1_open_hearing_feedback_with_comments_on_implementation_in_v2.pdf)。最终的 ecoSpold2 格式旨在以 XML 为基础表示生命周期评价的三个阶段：UPR、LCI 和 LCIA。

ecoSpold2 格式新增的功能包括：

- 交换的属性，如干质量、湿质量、碳含量等。
- 以新[公式语言](../assets/67941e148133-ecospold02_formula_language_specification.pdf)表示的数学关系，以及交换、属性和参数的变量名。
- 使用 UUID 引用某些字段。
- 新增产量字段。

如需比较 ecoSpold1 与 ecoSpold2，请参阅：[从 ecoSpold1 到 ecoSpold2 的变化](changes-ecospold1-to-ecospold2.md)。

目前，大多数使用 ecoinvent 数据库的[软件提供方](https://ecoinvent.org/partners/)都使用 ecoSpold2。开源 Python 框架 [Brightway2](https://docs.brightway.dev/en/latest/) 也支持导入 ecoSpold2。

#### <strong>配套文件和文档</strong> <a href="#zh-b0012" id="zh-b0012"></a>

该 ZIP 文件包含以下用于描述数据集和主数据文件的文件：

- 模式定义（xsd）
- 样式表（xsl）
- 便于用户阅读的格式说明（html）

![doc-icon](../assets/c7fb8198c9d5-doc-icon.png) [ecoSpold2 格式文档 [zip]](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/documentation_on_ecospold2_format.v1.0.13.zip)

该网页介绍 ecoinvent 数据库地理数据的创建与处理。

[ecoinvent 地理区域定义](https://geography.ecoinvent.org/)

适用于 ecoinvent v3 的 ecoEditor 简介。

![doc-icon](../assets/024d8f149226-doc-icon.png) [ecoEditor 用户手册 [pdf]](../assets/cc227411f20d-ecoeditor_introduction_20130503-1.pdf)

该文档解释这些字段的要求和预期内容，帮助恰当地编写数据集文档。

![doc-icon](../assets/024d8f149226-doc-icon.png) [数据集文档编写手册 [pdf]](../assets/592754ebf3e3-dataset_documentation_ecoinvent_3.pdf)

ecoSpold2 格式为交换、属性和参数引入了新的“mathematicalRelation”字段。该字段允许填写的内容见此文档。

![doc-icon](../assets/024d8f149226-doc-icon.png) [公式语言规范 [pdf]](../assets/67941e148133-ecospold02_formula_language_specification.pdf)

{% endtab %}

{% tab title="English 原文" %}

## The ecoSpold2 format is used to create life cycle inventories for ecoinvent version 3. This format sets up standards on what are mandatory and what are optional fields for a standard life cycle inventory. <a href="#en-b0002" id="en-b0002"></a>

Oct 30th, 2023

The ecoSpold2 format replaces the ecoSpold1 format for ecoinvent version 3 released in May 2013. New developments in the field of LCA software demanded a revision of the data format. An ad-hoc expert working group was formed by ecoinvent to guide the revision process and an open hearing has been conducted among users of the ecoSpold format. The result of this hearing and the way the input has been treated can be seen in [this public report](../assets/58422431916f-200905_ecospold1_open_hearing_feedback_with_comments_on_implementation_in_v2.pdf). The final ecospold2 format is designed to represent all three stages of life cycle assessment: UPR, LCI, and LCIA on an xml basis.

Among others, the ecospold2 format adds features such as:

- Properties of exchanges like dry mass, wet mass, carbon content etc.
- Mathematical relations in a new [formula language](../assets/67941e148133-ecospold02_formula_language_specification.pdf) and variable names for exchanges, properties, and parameters
- Use of UUIDs for referencing certain fields
- New fields for production volumes

For a comparison between ecospold1 and ecospold2 visit: [Changes ecospold1 to ecospold2](changes-ecospold1-to-ecospold2.md).

Today, ecospold2 is used by most of the [software providers](https://ecoinvent.org/partners/) that use the ecoinvent database. The open-source python framework [Brightway2](https://docs.brightway.dev/en/latest/) supports the import of ecospold2 as well.

#### <strong>Supporting Files and Documents</strong> <a href="#en-b0012" id="en-b0012"></a>

This zip file contains the following files describing datasets and master data files:

- schema definition (xsd)
- stylesheets (xsl)
- user-friendly description of the formats (html)

![doc-icon](../assets/c7fb8198c9d5-doc-icon.png)  [Documentation on ecoSpold2 format [zip]](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/documentation_on_ecospold2_format.v1.0.13.zip)

This webpage describes the creation and processing of geodata for the ecoinvent database.

[ecoinvent geography definitions](https://geography.ecoinvent.org/)

A short introduction to the ecoEditor for ecoinvent v3

![doc-icon](../assets/024d8f149226-doc-icon.png)  [ecoEditor User Manual [pdf]](../assets/cc227411f20d-ecoeditor_introduction_20130503-1.pdf)

This document assists in the proper documentation of datasets explaining the requirements and expectations for these fields.

![doc-icon](../assets/024d8f149226-doc-icon.png)  [Dataset Documentation Manual [pdf]](../assets/592754ebf3e3-dataset_documentation_ecoinvent_3.pdf)

The ecoSpold2 format introduces the new field “mathematicalRelation” for exchanges, properties and parameters. The allowed content for this field is described in this document.

![doc-icon](../assets/024d8f149226-doc-icon.png)  [Formula Language Specification [pdf]](../assets/67941e148133-ecospold02_formula_language_specification.pdf)

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **已处理／已说明 · b0009**：统一指南规定的产量术语。 已将生产量改为产量。 [查看完整记录](../review/issues.md#issue-122)
- **待专家复核 · b0004**：UPR、LCI 和 LCIA 此处描述三种数据形式；UPR 并非 ISO 所规定的 LCA 阶段。原文将其称为三个阶段，译文忠实保留，存在方法学用语歧义。 请技术编辑确认改为三种数据形式，并同步原文和译文。 [查看完整记录](../review/issues.md#issue-123)
