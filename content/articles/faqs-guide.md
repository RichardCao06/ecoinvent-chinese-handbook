# 常见问题

英文原题：Frequently Asked Questions  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/faqs-guide)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2026-09-15

{% tabs %}

{% tab title="中文" %}

## 查看常见问题（FAQ），快速获取常见问题的解答。 <a href="#zh-b0002" id="zh-b0002"></a>

点击以下目录，可跳转至相应问题。

### [<strong>使用 ecoinvent 数据库</strong>](#zh-b0032) <a href="#zh-b0004" id="zh-b0004"></a>

[- ecoinvent 数据库提供哪些内容？](#zh-b0033)

[- ecoinvent 数据库的数据来自哪里？](#zh-b0037)

[- 如何在 ecoQuery 中查找和查看数据集？](#zh-b0040)

[- 找不到所需数据集时应该怎么办？](#zh-b0043)

[- 什么是系统模型，如何选择？](#zh-b0045)

[- 为什么更换 ecoinvent 版本／系统模型／LCIA 方法后，我的影响结果发生变化？](#zh-b0048)

[- 有哪些影响评价方法可用，如何选择？](#zh-b0051)

[- 能否推荐我的研究应采用哪个数据集或系统模型？](#zh-b0054)

[- ecoinvent 如何处理土地利用和土地利用变化相关排放（FLAG 排放）？](#zh-b0057)

[- 如何核算生物源碳流？](#zh-b0060)

[- 如何使用 ecoinvent 数据报告范围 1、范围 2 和范围 3 温室气体排放？](#zh-b0063)

### [<strong>软件集成与下载</strong>](faqs-guide.md) <a href="#zh-b0016" id="zh-b0016"></a>

[- 如何将 ecoinvent 数据导入 LCA 软件（如 SimaPro、openLCA、Brightway）？](#zh-b0067)

[- 如何将我的数据映射至 ecoinvent 的过程和流？](#zh-b0070)

[- 如何从 ecoQuery 下载数据集及相关文件或报告？](#zh-b0072)

### [<strong>向 ecoinvent 提交数据</strong>](#zh-b0075) <a href="#zh-b0020" id="zh-b0020"></a>

[- 如何向 ecoinvent 提交自己的数据集？](#zh-b0076)

[- 我的使用场景需要哪种 ecoinvent 许可证？](#zh-b0079)

[- 我的许可证允许向合作者共享哪些数据或结果？](#zh-b0082)

[- 版本之间如何续订和升级？](#zh-b0085)

[- 哪些许可证包含 EN15804 数据集和系统模型的访问权限？](#zh-b0088)

### [<strong>账户与访问</strong>](faqs-guide.md) <a href="#zh-b0026" id="zh-b0026"></a>

[- 如何登录并访问 ecoinvent 数据库和 ecoQuery？](#zh-b0092)

[- 我无法登录或已失去访问权限，如何恢复访问？](#zh-b0095)

[- 如何激活新许可证？](#zh-b0097)

[- 如何将新许可证关联至我的账户或组织？](#zh-b0099)

[- 为什么我无法查看／下载许可证应涵盖的某个数据库版本？](#zh-b0101)

### <strong>使用 ecoinvent 数据库</strong> <a href="#zh-b0032" id="zh-b0032"></a>

#### <strong>ecoinvent 数据库提供哪些内容？</strong> <a href="#zh-b0033" id="zh-b0033"></a>

ecoinvent 数据库包含超过 26,000 个生命周期清单（LCI）数据集，覆盖能源、运输、农业、化学品、废物管理等部门的活动和产品。完整活动清单见 [v3.12 数据库概览](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)文件。

最新数据库版本的已知问题列于版本发布页面：[ecoinvent 第 3.12 版——已知问题。](ecoinvent-version-3.12.md)

进一步了解：[ecoinvent 数据库提供哪些内容](about.md)

#### <strong>ecoinvent 数据库的数据来自哪里？</strong> <a href="#zh-b0037" id="zh-b0037"></a>

数据通过与研究机构、学术界及行业的外部合作，以及个人研究者或企业直接提交进入数据库。所有数据集在发布前均经过内部和外部专家审阅。

进一步了解：[ecoinvent 数据库提供哪些内容](about.md)

#### <strong>如何在 ecoQuery 中查找和查看数据集？</strong> <a href="#zh-b0040" id="zh-b0040"></a>

登录 [ecoQuery](https://ecoquery.ecoinvent.org/)，选择版本及系统模型，然后通过搜索栏和筛选条件（部门、地理区域、活动类型、ISIC 类别）查找数据集。[v3.12 数据库概览](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)文件也有助于识别正确的活动和产品名称。

进一步了解：[在 ecoQuery 中搜索数据集](searching-for-datasets.md)

#### <strong>找不到所需数据集时应该怎么办？</strong> <a href="#zh-b0043" id="zh-b0043"></a>

首先查阅 [v3.12 数据库概览](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)文件，检查数据集是否以其他名称或在其他系统模型下存在。找到相关数据集后，在 [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff) 中打开并审阅其文档，以判断是否满足需求。若缺少完全对应的产品，您可考虑将已有数据集作为替代数据，或以 ecoinvent 数据集为起点创建自己的数据集。

#### <strong>什么是系统模型，如何选择？</strong> <a href="#zh-b0045" id="zh-b0045"></a>

系统模型规定从单元过程（UPR）计算生命周期清单（LCI）的方法规则，具体包括如何处理多输出活动（通过分配或替代），以及如何链接供应链。目前提供四种系统模型：Cut-off、EN15804、APOS 和 Consequential。系统模型的选择由用户负责。

进一步了解：[系统模型](system-models.md)和[不同系统模型及其采用的关键概念](system-models-1.md)[。](upr-lci-lcia.md)

#### <strong>为什么更换 ecoinvent 版本／系统模型／LCIA 方法后，我的影响结果发生变化？</strong> <a href="#zh-b0048" id="zh-b0048"></a>

LCIA 得分取决于数据集边界、交换数量、供应链链接和表征因子，而这些因素在不同版本、系统模型或影响评价方法之间均可能不同。每个新数据库版本都随附发布变更报告，可在对应[版本发布页面](../topics/version-3.md)公开获取。更详细的变更报告附件也向许可证持有者提供，位于 [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files) 的文件栏目。

进一步了解：[生命周期影响评价（LCIA）介绍](lcia-results.md)

#### <strong>有哪些影响评价方法可用，如何选择？</strong> <a href="#zh-b0051" id="zh-b0051"></a>

ecoinvent 实施多种 LCIA 方法，包括 IPCC 2021、EF v3.1、ReCiPe 2016、CML、TRACI 等。完整清单及详细信息见 LCIA 实施报告，可在对应[版本发布页面](../topics/version-3.md)公开获取。方法选择取决于研究目标和范围，ecoinvent 不规定应使用哪种方法。

进一步了解：[影响评价](impact-assessment.md)和[IPCC 方法使用指南](guidance-on-ipcc-methods.md)

#### <strong>能否推荐我的研究应采用哪个数据集或系统模型？</strong> <a href="#zh-b0054" id="zh-b0054"></a>

数据集、系统模型及影响评价方法的选择取决于您具体研究的目标和范围，由开展 LCA 的实践者负责。我们可以确认有哪些数据以及其结构，但不会为单项研究提供建模建议或验证其方法选择。对于项目特定的建模指导，您可考虑咨询独立 LCA 专家；使用 ecoinvent 数据的合作伙伴清单见我们的[合作伙伴](https://ecoinvent.org/partners/?_gl=1*teyc4k*_up*MQ..*_ga*MzczNDA4ODc4LjE3ODM2MDU4OTE.*_ga_C1J3MVCVZN*czE3ODM2MDU4OTAkbzEkZzAkdDE3ODM2MDU4OTAkajYwJGwwJGgw*_ga_3P8YT7402Y*czE3ODM2MDU4OTAkbzEkZzAkdDE3ODM2MDU4OTAkajYwJGwwJGgw)页面。

进一步了解：[系统模型](system-models.md)和[影响评价](impact-assessment.md)

#### <strong>ecoinvent 如何处理土地利用和土地利用变化相关排放（FLAG 排放）？</strong> <a href="#zh-b0057" id="zh-b0057"></a>

农业部门的土地利用变化（LUC）排放依据 PAS2050-1/ENVIFOOD 协议建模。农业数据集的 FLAG 特定排放值可通过 [ecoQuery](https://ecoquery.ecoinvent.org/) 配套文件“LUC-FLAG Emissions in Agriculture v3.12.xlsx”获取。该文件仅包含与 LUC 相关的 FLAG 排放。土地管理相关排放直接记录在作物生产数据集中，需要从这些数据集单独提取。目前林业数据集尚未核算 FLAG 排放。

进一步了解：[农业、渔业与畜牧业](agriculture-fishery-and-animal-husbandry.md)

#### <strong>如何核算生物源碳流？</strong> <a href="#zh-b0060" id="zh-b0060"></a>

在“IPCC 2021”方法中，生物源二氧化碳吸收和释放默认按 0/0 表征。对于要求 -1/+1 表征的标准（如 ISO 14067、EN 15804），可使用补充方法“IPCC 2021 (incl. biogenic CO2)”。该方法不应单独使用，对包含生物源 CO₂ 的得分也应谨慎处理。

进一步了解：[IPCC 方法使用指南](guidance-on-ipcc-methods.md)

#### <strong>如何使用 ecoinvent 数据报告范围 1、范围 2 和范围 3 温室气体排放？</strong> <a href="#zh-b0063" id="zh-b0063"></a>

GHG Protocol 将排放分为三个范围：范围 1（自有或受控来源的直接排放）、范围 2（外购能源）和范围 3（其他全部价值链排放）。ecoinvent 数据主要适用于范围 2 和范围 3 报告，提供二手活动数据和区域平均 LCIA 得分，以填补数据缺口。[ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files) 提供专门的电力排放因子电子表格（<em>electricity emission factors – scope 2 – 3.xlsx</em>）。

进一步了解：[范围 2 和范围 3 温室气体（GHG）排放报告](lcia-results.md)

### 

### <strong>软件集成与下载</strong> <a href="#zh-b0066" id="zh-b0066"></a>

#### <strong>如何将 ecoinvent 数据导入 LCA 软件（如 SimaPro、openLCA、Brightway）？</strong> <a href="#zh-b0067" id="zh-b0067"></a>

ecoinvent 数据库已集成到所有主流 LCA 软件工具中。如果您通过软件经销商访问 ecoinvent，数据库已直接整合进工具；请联系软件提供方获取导入或更新指导。对于直接集成，可从 [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files) 下载 ecoSpold2 格式的 ecoinvent 数据。

进一步了解：[ecoinvent 与 LCA 软件工具](ecoinvent-lca-software-tools.md)和[ecoinvent 数据格式介绍。](data-formats.md)

#### <strong>如何将我的数据映射至 ecoinvent 的过程和流？</strong> <a href="#zh-b0070" id="zh-b0070"></a>

建议以 [v3.12 数据库概览](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx)作为识别合适数据集的起点。在 [ecoQuery](https://ecoquery.ecoinvent.org/) 中审阅数据集文档，有助于确认过程范围和地理区域是否满足需求。若从旧版本迁移，相关[版本发布页面](../topics/version-3.md)提供的对应关系文件（Correspondence File）可映射相邻版本间的数据集。对于软件层级的 ID 映射，许可证持有者还可在 [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files) 获取变更报告附件。

#### <strong>如何从 ecoQuery 下载数据集及相关文件或报告？</strong> <a href="#zh-b0072" id="zh-b0072"></a>

在 [ecoQuery](https://ecoquery.ecoinvent.org/) 任一数据集页面的“导出”（Export）栏目，可将单个数据集导出为 ecoSpold2 格式。许可证持有者可在 ecoQuery 的[文件栏目](https://ecoquery.ecoinvent.org/3.12/cutoff/files)获取完整数据库文件、LCIA 结果及配套文档。部分项目的补充信息见[报告栏目](https://ecoquery.ecoinvent.org/3.12/cutoff/reports)。

进一步了解：[在 ecoQuery 中下载数据集](downloading-and-viewing-of-datasets.md)和[ecoQuery 中的文件](files.md)。

### <strong>向 ecoinvent 提交数据</strong> <a href="#zh-b0075" id="zh-b0075"></a>

#### <strong>如何向 ecoinvent 提交自己的数据集？</strong> <a href="#zh-b0076" id="zh-b0076"></a>

要提交数据集，请填写[联系我们表单](https://ecoinvent.org/contact-us/)，提供姓名、组织及拟提交数据类型的简要说明。ecoinvent 将随后联系您讨论细节，提供数据创建工具 ecoEditor 的访问权限，并协调编辑审阅。所有提交的数据集在发布前均接受独立专家审阅。数据作者保留版权，并在发布的数据集中署名。

进一步了解：[数据提交流程](data-submission-process.md)和[ecoEditor。](ecoeditor.md)

#### <strong>我的使用场景需要哪种 ecoinvent 许可证？</strong> <a href="#zh-b0079" id="zh-b0079"></a>

使用[许可证计算器](https://ecoinvent.org/licenses/#license-calculator)确定适合您使用场景的选项。

[进一步了解所有许可证类型与价格](licensing.md)。

#### <strong>我的许可证允许向合作者共享哪些数据或结果？</strong> <a href="#zh-b0082" id="zh-b0082"></a>

计算结果（如碳足迹）可通过静态形式向非许可证持有者共享，例如 PDF 报告。通过工具或应用共享结果需要额外的再许可协议。原始数据库数据不可共享。

进一步了解：[ecoinvent 最终用户许可协议（EULA）](eula.md)

#### <strong>版本之间如何续订和升级？</strong> <a href="#zh-b0085" id="zh-b0085"></a>

自 2025 年 4 月 1 日起购买的新许可证为年度订阅，对应购买时的数据库最新版本；必须每年续订以保持访问权限。现有永久许可证持有者可以继续续订维护服务，通过付费升级获取较新版本。续订和升级可通过您的[账户](https://accounts.ecoinvent.org/)管理。

进一步了解：[许可证与价格介绍](licensing.md)

#### <strong>哪些许可证包含 EN15804 数据集和系统模型的访问权限？</strong> <a href="#zh-b0088" id="zh-b0088"></a>

“Allocation, cut-off, EN15804”系统模型可作为所有许可证类型的附加项，默认并不包含。请通过[联系我们表单](https://ecoinvent.org/contact-us/)联系，以将其添加到您的许可证。

进一步了解：[许可证](https://ecoinvent.org/licenses/#license-calculator:~:text=Additional,on,-For)和[系统模型](system-models.md)

### 

### <strong>账户与访问</strong> <a href="#zh-b0091" id="zh-b0091"></a>

#### <strong>如何登录并访问 ecoinvent 数据库和 ecoQuery？</strong> <a href="#zh-b0092" id="zh-b0092"></a>

获得许可证后，使用您的凭据登录 ecoQuery。如果通过软件合作伙伴（如 SimaPro、openLCA）购买，您可能被分配了默认用户名；请查看登录指南中的示例及个性化设置说明。也可直接通过您的 LCA 软件工具访问数据库。

进一步了解：[如何登录并访问 ecoinvent 数据库](first-log-in-to-ecoinvent.md)。

#### <strong>我无法登录或已失去访问权限，如何恢复访问？</strong> <a href="#zh-b0095" id="zh-b0095"></a>

如果忘记用户名，请联系 [sales@ecoinvent.org](mailto:sales@ecoinvent.org)，提供姓名及组织。要重设密码，请使用 [ecoQuery 登录页面](https://ecoquery.ecoinvent.org/)的“忘记密码”选项。若访问权限已过期或被撤销，请联系 [sales@ecoinvent.org](mailto:sales@ecoinvent.org) 核查许可证状态。

#### <strong>如何激活新许可证？</strong> <a href="#zh-b0097" id="zh-b0097"></a>

直接从 ecoinvent 购买许可证后，您将收到包含激活说明的电子邮件。登录您的[账户](https://accounts.ecoinvent.org/)完成激活。如果通过软件合作伙伴购买，许可证由合作伙伴激活，请直接联系对方。

#### <strong>如何将新许可证关联至我的账户或组织？</strong> <a href="#zh-b0099" id="zh-b0099"></a>

许可证关联通过您的[账户](https://accounts.ecoinvent.org/)管理。如果无法关联许可证，或需要协助将其关联至组织，请联系 [sales@ecoinvent.org](mailto:sales@ecoinvent.org)。

#### <strong>为什么我无法查看／下载许可证应涵盖的某个数据库版本？</strong> <a href="#zh-b0101" id="zh-b0101"></a>

特定版本的访问权限取决于许可证类型。年度订阅许可证仅提供当前最新版本的访问权限。如果持有旧制永久许可证，您可访问购买时的版本，以及后续维护续订涵盖的版本。如果认为许可证应涵盖某个您无法访问的版本，请联系 [sales@ecoinvent.org](mailto:sales@ecoinvent.org)。

进一步了解：[许可证与价格介绍](licensing.md)

{% endtab %}

{% tab title="English 原文" %}

## Check our Frequently Asked Questions (FAQs) for fast answers to common issues. <a href="#en-b0002" id="en-b0002"></a>

Click through this list of contents to be taken to your question.

### [<strong>Using the ecoinvent Database</strong>](#en-b0032) <a href="#en-b0004" id="en-b0004"></a>

[- What is available in the ecoinvent database?](#en-b0033)

[- Where does the data in the ecoinvent database come from?](#en-b0037) 

[- How do I find and view datasets in ecoQuery?](#en-b0040)

[- What should I do if I cannot find the dataset I need?](#en-b0043)

[- What are system models, and how do I select one?](#en-b0045)

[- Why did my impact results change when I switched ecoinvent version/system model/LCIA method?](#en-b0048)

[- Which impact assessment methods are available, and how do I select one?](#en-b0051)

[- Can you recommend which dataset or system model to use for my study?](#en-b0054)

[- How does ecoinvent approach land use and land use change-related emissions (FLAG emissions)?](#en-b0057)

[- How are biogenic carbon flows accounted for?](#en-b0060)

[- How can I use ecoinvent data for Scope 1, Scope 2 and Scope 3 greenhouse gas reporting?](#en-b0063)

### [<strong>Software Integration & Downloads</strong>](faqs-guide.md) <a href="#en-b0016" id="en-b0016"></a>

[- How do I import ecoinvent data into my LCA software (e.g. SimaPro, openLCA, Brightway)?](#en-b0067)

[- How should I map my data to ecoinvent processes and flows?](#en-b0070)

[- How do I download datasets and related files or reports from ecoQuery?](#en-b0072)

### [<strong>Submitting Data to ecoinvent</strong>](#en-b0075) <a href="#en-b0020" id="en-b0020"></a>

[- How can I submit my own datasets to ecoinvent?](#en-b0076)

[- Which ecoinvent license do I need for my use case?](#en-b0079)

[- What data or results can I share with collaborators under my license?](#en-b0082)

[- How do renewals and upgrades work between versions?](#en-b0085)

[- Which licenses include access to EN15804 datasets and system models?](#en-b0088)

### [<strong>Accounts & Access</strong>](faqs-guide.md) <a href="#en-b0026" id="en-b0026"></a>

[- How do I log in and access the ecoinvent database and ecoQuery?](#en-b0092)

[- I cannot log in or have lost access. How do I restore access?](#en-b0095)

[- How do I activate a new license?](#en-b0097)

[- How do I link a new license to my account or organization?](#en-b0099)

[- Why can’t I see / download a specific version of the database that my license should cover?](#en-b0101)

### <strong>Using the ecoinvent Database</strong> <a href="#en-b0032" id="en-b0032"></a>

#### <strong>What is available in the ecoinvent database? </strong> <a href="#en-b0033" id="en-b0033"></a>

The ecoinvent database contains over 26,000 life cycle inventory (LCI) datasets covering activities and products across sectors like energy, transport, agriculture, chemicals, waste management, and more. A full list of activities is available in the [v3.12 Database Overview](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx) file.

Known issues for the latest database release are listed on the release page: [ecoinvent Version 3.12 – Known Issues.](ecoinvent-version-3.12.md)

Learn more here: [What is Available in the ecoinvent Database](about.md)

#### <strong>Where does the data in the ecoinvent database come from? </strong> <a href="#en-b0037" id="en-b0037"></a>

Data enters the database through external collaborations with research institutes, academia, and industry, as well as direct submissions from individual researchers or companies. All datasets undergo internal and external expert review before publication.

Learn more here: [What is Available in the ecoinvent Database](about.md)

#### <strong>How do I find and view datasets in ecoQuery?</strong> <a href="#en-b0040" id="en-b0040"></a>

Log in to [ecoQuery](https://ecoquery.ecoinvent.org/), select a version and system model, then use the search bar and filters (sector, geography, activity type, ISIC class) to find datasets. The [v3.12 Database Overview](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx) file also helps identify the correct activity and product names.

Learn more here: [Searching for Datasets in ecoQuery](searching-for-datasets.md)

#### <strong>What should I do if I cannot find the dataset I need?</strong> <a href="#en-b0043" id="en-b0043"></a>

Start by consulting the [v3.12 Database Overview](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx) file to check whether the dataset exists under a different name or in a different system model. If you find a relevant dataset, open it in [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff) and review the documentation to assess whether it fits your needs. If the exact product is absent, you may consider using one of the available datasets as a proxy, or creating your own dataset using an ecoinvent dataset as a starting point.

#### <strong>What are system models, and how do I select one?</strong> <a href="#en-b0045" id="en-b0045"></a>

System models define the methodological rules used to calculate life cycle inventories (LCIs) from unit processes (UPRs) — specifically how multi-output activities are handled (via allocation or substitution) and how supply chains are linked. Four system models are available: cut-off, EN15804, APOS, and consequential. The choice of system model is the user's responsibility.

Learn more here: [System Models](system-models.md) and [About Different System Models and the Key Concepts Applied](system-models-1.md)[.](upr-lci-lcia.md)

#### <strong>Why did my impact results change when I switched ecoinvent version/system model/LCIA method?</strong> <a href="#en-b0048" id="en-b0048"></a>

LCIA scores depend on dataset boundaries and exchange amounts, supply chain linking, and characterization factors — all of which may differ between versions, system models, or impact assessment methods. A Change Report is published with each new database version and is publicly available on the relevant [release page](../topics/version-3.md). A more detailed Change Report Annex is also available for licensees in the Files section of [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files).

Learn more here: [About Life Cycle Impact Assessment (LCIA)](lcia-results.md)

#### <strong>Which impact assessment methods are available, and how do I select one?</strong> <a href="#en-b0051" id="en-b0051"></a>

ecoinvent implements a range of LCIA methods including IPCC 2021, EF v3.1, ReCiPe 2016, CML, TRACI, and others. The full list with details is in the LCIA Implementation report, publicly available on the relevant [release page](../topics/version-3.md). The choice of method depends on the goal and scope of your study — ecoinvent does not prescribe which method to use.

Learn more here: [Impact Assessment](impact-assessment.md) and [Guidance on IPCC Methods](guidance-on-ipcc-methods.md)

#### <strong>Can you recommend which dataset or system model to use for my study?</strong> <a href="#en-b0054" id="en-b0054"></a>

The choice of dataset, system model, and impact assessment method depends on the goal and scope of your specific study—this is the responsibility of the practitioner conducting the LCA. We can confirm what data exists and how it's structured, but we don't provide modeling recommendations or validate methodological choices for individual studies. For project-specific modelling guidance, you may consider consulting an independent LCA expert—a list of partners who work with ecoinvent data is available on our [partners](https://ecoinvent.org/partners/?_gl=1*teyc4k*_up*MQ..*_ga*MzczNDA4ODc4LjE3ODM2MDU4OTE.*_ga_C1J3MVCVZN*czE3ODM2MDU4OTAkbzEkZzAkdDE3ODM2MDU4OTAkajYwJGwwJGgw*_ga_3P8YT7402Y*czE3ODM2MDU4OTAkbzEkZzAkdDE3ODM2MDU4OTAkajYwJGwwJGgw) page.

Learn more here: [System Models](system-models.md) and [Impact Assessment](impact-assessment.md)

#### <strong>How does ecoinvent approach land use and land use change-related emissions (FLAG emissions)?</strong> <a href="#en-b0057" id="en-b0057"></a>

Land use change (LUC) emissions in the agricultural sector are modelled following the PAS2050-1/ENVIFOOD protocol. FLAG-specific emission values for agricultural datasets are available as a supporting file on [ecoQuery](https://ecoquery.ecoinvent.org/) (‘LUC-FLAG Emissions in Agriculture v3.12.xlsx’). This file includes FLAG emissions related to LUC only. Land management–related emissions are inventoried directly in the crop production datasets and need to be extracted separately from those datasets. Forestry datasets do not currently account for FLAG emissions.

Learn more here: [Agriculture, Fishery and Animal Husbandry](agriculture-fishery-and-animal-husbandry.md)

#### <strong>How are biogenic carbon flows accounted for?</strong> <a href="#en-b0060" id="en-b0060"></a>

Biogenic carbon dioxide uptake and release are characterized as 0/0 by default in the "IPCC 2021" method. For standards that require -1/+1 characterization (e.g., ISO 14067, EN 15804), the complementary "IPCC 2021 (incl. biogenic CO2)" method is available — it should not be used as a stand-alone method, and scores including biogenic CO₂ should be handled with care.

Learn more here: [Guidance on IPCC Methods](guidance-on-ipcc-methods.md)

#### <strong>How can I use ecoinvent data for Scope 1, Scope 2 and Scope 3 greenhouse gas reporting?</strong> <a href="#en-b0063" id="en-b0063"></a>

The GHG Protocol divides emissions into three scopes: Scope 1 (direct emissions from owned or controlled sources), Scope 2 (purchased energy), and Scope 3 (all other value chain emissions). ecoinvent data is primarily relevant for Scope 2 and 3 reporting, providing secondary activity data and regional average LCIA scores to fill data gaps. A dedicated spreadsheet with electricity emission factors is available in [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files) (<em>electricity emission factors – scope 2 – 3.xlsx</em>).

Learn more here: [Scope 2 and 3 Greenhouse Gas (GHG) Emission Reporting](lcia-results.md)

### 

### <strong>Software Integration & Downloads</strong> <a href="#en-b0066" id="en-b0066"></a>

#### <strong>How do I import ecoinvent data into my LCA software (e.g. SimaPro, openLCA, Brightway)?</strong> <a href="#en-b0067" id="en-b0067"></a>

 The ecoinvent database is integrated in all leading LCA software tools. If you access ecoinvent through a software reseller, the database is incorporated directly into the tool — contact your software provider for guidance on importing or updating it. For direct integration, ecoinvent data is available in ecoSpold2 format, downloadable from [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files).

Learn more here: [ecoinvent and LCA Software Tools](ecoinvent-lca-software-tools.md) and [About ecoinvent Data Formats.](data-formats.md)

#### <strong>How should I map my data to ecoinvent processes and flows?</strong> <a href="#en-b0070" id="en-b0070"></a>

The [v3.12 Database Overview](../assets/30cb0c4dc3d6-Database-Overview-v3.12.xlsx) is the recommended starting point for identifying the right dataset. Reviewing the dataset documentation in [ecoQuery](https://ecoquery.ecoinvent.org/) helps confirm whether the process scope and geography fit your needs. If you are migrating from a previous version, the Correspondence File — available on the relevant [release page](../topics/version-3.md) — maps datasets between consecutive versions. For software-level ID mapping, the Change Report Annex is also available for licensees in [ecoQuery](https://ecoquery.ecoinvent.org/3.12/cutoff/files).

#### <strong>How do I download datasets and related files or reports from ecoQuery?</strong> <a href="#en-b0072" id="en-b0072"></a>

Individual datasets can be exported from [ecoQuery](https://ecoquery.ecoinvent.org/) in ecoSpold2 format via the Export section of any dataset page. Full database files, LCIA results, and supporting documents are available in the [Files section](https://ecoquery.ecoinvent.org/3.12/cutoff/files) of ecoQuery for licensees. Additional information for selected projects can be found in the [Reports section](https://ecoquery.ecoinvent.org/3.12/cutoff/reports).

Learn more here: [Downloading a Dataset in ecoQuery](downloading-and-viewing-of-datasets.md) and [Files in ecoQuery](files.md).

### <strong>Submitting Data to ecoinvent</strong> <a href="#en-b0075" id="en-b0075"></a>

#### <strong>How can I submit my own datasets to ecoinvent?</strong> <a href="#en-b0076" id="en-b0076"></a>

To submit datasets, fill in the [Contact Us form](https://ecoinvent.org/contact-us/) with your name, organisation, and a brief description of the type of data you want to submit. ecoinvent will follow up to discuss the details, provide access to the data creation tool ecoEditor, and coordinate the editorial review. All submitted datasets undergo independent expert review before publication. Data authors retain copyright and are credited in the published dataset.

Learn more here: [Data Submission Process](data-submission-process.md) and [ecoEditor.](ecoeditor.md)

#### <strong>Which ecoinvent license do I need for my use case?</strong> <a href="#en-b0079" id="en-b0079"></a>

Use the [license calculator](https://ecoinvent.org/licenses/#license-calculator) to identify the right option for your use case.

[Learn more about all license types and pricing](licensing.md).

#### <strong>What data or results can I share with collaborators under my license?</strong> <a href="#en-b0082" id="en-b0082"></a>

Calculated results (e.g., a carbon footprint) can be shared statically with non-licensees, for example in a PDF report. Sharing results through a tool or application requires an additional sublicensing agreement. Raw database data cannot be shared.

Learn more here: [ecoinvent End-User License Agreement (EULA)](eula.md)

#### <strong>How do renewals and upgrades work between versions?</strong> <a href="#en-b0085" id="en-b0085"></a>

New licenses purchased from April 1, 2025 onwards are annual subscriptions tied to the latest version of the database at the time of purchase, and must be renewed each year to maintain access. Existing perpetual license holders can continue to renew their maintenance to access newer versions via a paid upgrade. Renewals and upgrades can be managed via your [account](https://accounts.ecoinvent.org/).

Learn more here: [About Licenses and Pricing](licensing.md)

#### <strong>Which licenses include access to EN15804 datasets and system models?</strong> <a href="#en-b0088" id="en-b0088"></a>

The "Allocation, cut-off, EN15804" system model is available as an add-on to all license types. It is not included by default — please contact us via the [Contact Us form](https://ecoinvent.org/contact-us/) to add it to your license.

Learn more here: [Licenses](https://ecoinvent.org/licenses/#license-calculator:~:text=Additional,on,-For) and [System Models](system-models.md)

### 

### <strong>Accounts & Access</strong> <a href="#en-b0091" id="en-b0091"></a>

#### <strong>How do I log in and access the ecoinvent database and ecoQuery?</strong> <a href="#en-b0092" id="en-b0092"></a>

Once you have a license, log in to ecoQuery using your credentials. If you purchased through a software partner (e.g., SimaPro, openLCA), you may have been assigned a default username — check the login guide for examples and instructions on how to personalise it. The database can also be accessed directly through your LCA software tool.

Learn more here: [How to Login and Access the ecoinvent Database](first-log-in-to-ecoinvent.md).

#### <strong>I cannot log in or have lost access. How do I restore access?</strong> <a href="#en-b0095" id="en-b0095"></a>

If you have forgotten your username, contact [sales@ecoinvent.org](mailto:sales@ecoinvent.org) with your name and organisation. For password resets, use the forgotten password option on the [ecoQuery login page](https://ecoquery.ecoinvent.org/). If your access has expired or been revoked, contact [sales@ecoinvent.org](mailto:sales@ecoinvent.org) to check your license status.

#### <strong>How do I activate a new license?</strong> <a href="#en-b0097" id="en-b0097"></a>

After purchasing a license directly from ecoinvent, you will receive an email with activation instructions. Log in to your [account](https://accounts.ecoinvent.org/) to complete the activation. If you purchased through a software partner, your license is activated by the partner—contact them directly.

#### <strong>How do I link a new license to my account or organization?</strong> <a href="#en-b0099" id="en-b0099"></a>

License linking is managed via your [account](https://accounts.ecoinvent.org/). If you are unable to link a license or need help associating it with your organisation, contact [sales@ecoinvent.org](mailto:sales@ecoinvent.org).

#### <strong>Why can’t I see / download a specific version of the database that my license should cover?</strong> <a href="#en-b0101" id="en-b0101"></a>

Access to specific versions depends on your license type. Annual subscription licenses give access to the current latest version only. If you hold a legacy perpetual license, you have access to the version at the time of purchase, plus any versions covered by subsequent maintenance renewals. If you believe your license should cover a version you cannot access, contact [sales@ecoinvent.org](mailto:sales@ecoinvent.org).

Learn more here: [About Licenses and Pricing](licensing.md)

{% endtab %}

{% endtabs %}
