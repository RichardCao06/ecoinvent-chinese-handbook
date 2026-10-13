# ecoQuery 中的文件

英文原题：Files in ecoQuery  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/files)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过，含审校注记

原站修改日期：2025-12-02

{% hint style="warning" %}
本页含原文疑点，需领域专家核实。请同时阅读文末审校注记。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 在网页右上方的“文件”（Files）部分，您可以下载 ecoSpold2 格式的数据库。 <a href="#zh-b0002" id="zh-b0002"></a>

2025 年 11 月 5 日

在网页右上方的“文件”（Files）部分，您可以下载 ecoSpold2 格式的数据库。针对数据库的每个版本，您都可以找到各系统模型（此处以“xxx”表示）的 LCI 和 LCIA 结果文件，以及支持文档。对于 ecoinvent v3.12，可找到以下文件：

### ecoinvent v3.12：LCI 和 LCIA 结果 <a href="#zh-b0005" id="zh-b0005"></a>

- <strong>Electricity Analysis 3.12, xxx.xlsx：</strong>此文件可详细追踪市场、电压转换及发电之间的需求关系，包含按国家、电压等级和燃料细分的电力供应情况。

- <strong>ecoinvent 3.12\_xxx\_cumulative\_lci\_xlsx.7z：</strong>此文件包含所有数据集的生命周期清单（LCI）。

- <strong>ecoinvent 3.12\_xxx\_cumulative\_lcia\_xlsx.7z：</strong>此文件包含所有数据集的生命周期影响评价（LCIA）得分。

- <strong>ecoinvent 3.12\_xxx\_ecoSpold02.7z：</strong>此文件包含所有数据集的单元过程，采用 ecoSpold02 格式。

- <strong>ecoinvent 3.12\_xxx\_lci\_ecoSpold02.7z：</strong>此文件包含所有数据集的生命周期清单（LCI），采用 ecoSpold02 格式。

- <strong>ecoinvent 3.12\_xxx\_lcia\_ecoSpold02.7z：</strong>此文件包含所有数据集的生命周期影响评价（LCIA）得分，采用 ecoSpold02 格式。

- <strong>universal\_matrix\_export\_v3.12\_xxx.7z：</strong>对于各系统模型，universal\_matrix\_export 文件夹包含可按基于矩阵的计算方法计算 LCI 和 LCIA 的矩阵。

ecoSpold2 和 .xlsx 文件首先需要使用免费开源的文件压缩软件 7-Zip 解压。

xlsx 文件是由 Microsoft Excel 创建的 Excel 电子表格，也可由其他电子表格程序（如 OpenOffice Calc 或 Apple Numbers）导出。ecoSpold2 格式用于为 ecoinvent 第 3 版创建生命周期清单。数据类型扩展名 .spold 可改为 .xml，这样，任何活动的全部单元过程原始数据（UPR）、累积清单（LCI）和影响评价结果（LCIA）都可在任何 .xml 编辑器中查看。

### ecoinvent v3.12：支持文档 <a href="#zh-b0015" id="zh-b0015"></a>

- <strong>electricity emission factors - scope 2 - 3 in ecoinvent v3.12.7z</strong>：此文件包含一个 .xlsx 文件，列出电力市场和发电数据集的范围 2 和范围 3 排放因子（kg CO<sub>2</sub> 当量/kWh）及排放量（kg/kWh），并附有配套报告。

- <strong>Dry Mass and Carbon Content Properties v3.12.xlsx：</strong>此文件列出了各可用系统模型中所有数据集参考产品的干质量和碳含量（化石源与非化石源）属性。

- <strong>LUC-FLAG Emissions in Agriculture v3.12.xlsx：</strong>此文件提供农业数据集中与土地利用变化（LUC）有关的 FLAG 排放值，涵盖主要农产品。

- <strong>Market Composition v3.12.xlsx：</strong>此文件提供普通转化活动向各市场供应的份额，以及市场的生产量。
- <strong>ecoinvent 3.12\_LCIA\_implementation.7z：</strong>包含一个 .xlsx 文件，提供 ecoinvent 数据库中已实施的生命周期影响评价（LCIA）方法的信息，以及一份记录 ecoinvent 在实施 LCIA 方法时所作假设的报告。
- <strong>ecoinvent 3.12\_Change Report\_including Annexes.7z：</strong>此文件包含“Change Report v3.11.pdf”和“Change Report Annex v3.10.1 – v3.11.xlsx”，介绍 ecoinvent 数据库 v3.11 中实施的变化。

### <strong>更多支持</strong> <a href="#zh-b0022" id="zh-b0022"></a>

有关您的许可证类型是否包括 ecoinvent 文件和报告访问权限的更多信息，请查阅我们的[许可证常见问题](licensing.md)。

{% endtab %}

{% tab title="English 原文" %}

## In the Files section on the top right of the webpage, you can download the database in ecoSpold2 format. <a href="#en-b0002" id="en-b0002"></a>

Nov 5th, 2025

In the Files section on the top right of the webpage, you can download the database in ecoSpold2 format. For each version of the database, you can find files for each system model (here ‘xxx’) dealing with LCI and LCIA results, as well as supporting documents. For ecoinvent v3.12, you can find the following files:

### ecoinvent v3.12, LCI and LCIA Results <a href="#en-b0005" id="en-b0005"></a>

- <strong>Electricity Analysis 3.12, xxx.xlsx:</strong> This file allows for a detailed tracking of the demand between the market, voltage transformation, and electricity production. It includes a breakdown of electricity supply by country, voltage level, and fuel.

- <strong>ecoinvent 3.12\_xxx\_cumulative\_lci\_xlsx.7z:</strong> This file contains the Life Cycle Inventories (LCIs) of all datasets.

- <strong>ecoinvent 3.12\_xxx\_cumulative\_lcia\_xlsx.7z: </strong>This file contains the Life Cycle Impact Assessment (LCIA) scores of all datasets.

- <strong>ecoinvent 3.12\_xxx\_ecoSpold02.7z:</strong> This file contains the Unit Processes of all datasets in ecoSpold02 format.

- <strong>ecoinvent 3.12\_xxx\_lci\_ecoSpold02.7z:</strong> This file contains the Life Cycle Inventories (LCIs) of all datasets in ecoSpold02 format.

- <strong>ecoinvent 3.12\_xxx\_lcia\_ecoSpold02.7z:</strong> This file contains the Life Cycle Impact Assessment (LCIA) scores of all datasets in ecoSpold02 format.

- <strong>universal\_matrix\_export\_v3.12\_xxx.7z:</strong> For each system model, the universal\_matrix\_export folder contains the matrices that can be used for calculating the LCIs and LCIAs according to the matrix-based calculation approach.

The ecoSpold2 and .xlsx files first have to be extracted using 7-Zip, a free and open-source file archiver.

xlsx files are Excel spreadsheets created by Microsoft Excel, which can also be exported by another spreadsheet program, such as OpenOffice Calc or Apple Numbers. The ecoSpold2 format is used to create life cycle inventories for ecoinvent version 3. The data type .spold can be overwritten to .xml, and thus all the UPR, cumulative inventory (LCI), and results of the impact assessment (LCIA) of any activity can be viewed in any .xml editor.

### ecoinvent v3.12, Supporting Documents <a href="#en-b0015" id="en-b0015"></a>

- <strong>electricity emission factors - scope 2 - 3 in ecoinvent v3.12.7z</strong>: This file contains an .xlsx file which lists scope 2 and 3 emission factors (kg of CO<sub>2</sub> equivalent/kWh) and emissions (kg/kWh) for electricity markets and electricity production dataset and an associated report.

- <strong>Dry Mass and Carbon Content Properties v3.12.xlsx:</strong> This file shows the dry mass and carbon content (of both fossil and non-fossil origin) properties for the reference products of all datasets for available system models.

- <strong>LUC-FLAG Emissions in Agriculture v3.12.xlsx: </strong>This file provides FLAG emissions values related to land use change (LUC) in agricultural datasets. It includes the main agricultural products.

- <strong>Market Composition v3.12.xlsx:</strong> This file provides the shares that the ordinary transforming activities supply to each market, as well as the production volumes of the markets.
- <strong>ecoinvent 3.12\_LCIA\_implementation.7z:</strong> Contains an .xlsx file with information about the Life Cycle Impact Assessment (LCIA) methods implemented in the ecoinvent database and a report which documents the assumptions made by ecoinvent in the implementation of the LCIA methods.
- <strong>ecoinvent 3.12\_Change Report\_including Annexes.7z:</strong> This file contains the files “Change Report v3.11.pdf” and “Change Report Annex v3.10.1 – v3.11.xlsx which describe the changes implemented in the ecoinvent database v3.11.

### <strong>Additional Support</strong> <a href="#en-b0022" id="en-b0022"></a>

For more information about whether your license type includes access to the ecoinvent files and reports, please consult our [Licenses FAQ](licensing.md).

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **待专家复核 · b0021**：原文压缩包版本为 3.12，但其中报告名称与正文说明均为 3.11，可能沿用了上一版本描述。 暂忠实保留原文版本号；请核对实际附件内容后修订源文与译文。 [查看完整记录](../review/issues.md#issue-135)
- **已处理／已说明 · b0014**：将“累计清单”统一为指南和站内采用的“累积清单”。 已修正。 [查看完整记录](../review/issues.md#issue-136)
