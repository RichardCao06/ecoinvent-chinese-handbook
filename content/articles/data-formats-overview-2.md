# ecoSpold1

英文原题：ecoSpold1  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/data-formats-overview-2)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

## ecoSpold1 格式用于 ecoinvent 第 2 版，后来被 ecoSpold2 取代。 <a href="#zh-b0002" id="zh-b0002"></a>

2023 年 10 月 26 日

### <strong>ecoSpold1 数据交换格式</strong> <a href="#zh-b0004" id="zh-b0004"></a>

该格式基于 XML（可扩展标记语言；原文写作 extended markup Language）及相关技术（XSL、XSLT、Schema）。

该数据格式作为 ecoinvent 项目的一部分开发。ecoinvent 第 2 版的内部应用也使用 ecoSpold1 格式。管理工具、编辑工具和服务器工具均使用该格式相互交换数据，也使用它与其他应用交换数据。

ecoinvent 第 2 版数据库的[在线平台](https://ecoquery.ecoinvent.org/login)和 ecoSpoldAccess 均支持并使用 ecoSpold1。

该数据交换格式列出可用于记录单个数据集（单元过程的 LCI 原始数据及元信息）的全部数据字段，并规定预期填写的内容。

该格式以国际 SPOLD 99 数据交换格式为基础，并根据 ISO 技术规范 ISO 14048 进行了调整。

[ecoSpold1 数据交换格式](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/ecospold1_data_exchange_format.zip)

### <strong>ecoSpold1 Access 宏的功能</strong> <a href="#zh-b0011" id="zh-b0011"></a>

ecoSpoldAccess 宏允许您在 Microsoft Excel 中打开 ecoSpold1 文件，进行有限的编辑，然后将其从 Microsoft Excel 格式重新导出为 ecoSpold1 格式。ecoSpoldAccess 加载项是针对 Windows XP 和 Excel 97 开发的。

然而，由于已迁移到 [ecoSpold2](ecospold2.md)，ecoSpoldAccess 加载项已停止维护，且与较新版本的 Microsoft Excel 不兼容。

请注意，将结果文件从 Microsoft Excel 转换为 ecoSpold1 可能需要一定时间（约十到二十分钟），具体取决于所用 Excel 的版本及其设置。如果遇到问题，且您需要 Microsoft Excel 文件来开展 LCA 计算，请[联系我们](https://ecoinvent.org/contact-us/)。

如果您只是希望查看文件，请访问 ecoinvent 第 2 版数据库，然后[登录](https://ecoinvent.org/database-login/)数据库在线平台即可。

### <strong>安装 ecoSpold1 Access 宏</strong> <a href="#zh-b0016" id="zh-b0016"></a>

下方提供两个链接，可获取 ecoSpoldAccess 宏及相应的许可协议。请选择最适合您的操作系统和 Microsoft Excel 版本的链接。

要在计算机上安装 ecoSpoldAccess 宏，请将 EcoSpoldSetup 文件下载至计算机，并运行该可执行文件。

#### <strong>功能</strong> <a href="#zh-b0019" id="zh-b0019"></a>

安装后，Microsoft Excel 中将新增“ecoSpoldAccess”按钮栏。  
要转换从 ecoinvent 数据库下载的 spold1 文件，请运行 Excel 并点击“ecoSpold2Excel”按钮。

#### <strong>卸载旧版本</strong> <a href="#zh-b0021" id="zh-b0021"></a>

如果您正在使用旧版 ecoSpold 软件，请务必先卸载所有旧版本，再安装新版本。

卸载旧版本的步骤见 [ecoSpold 文档](../assets/61e82dab93c7-200810_documentation_ecospold_1.3.pdf)。

#### <strong>系统要求</strong> <a href="#zh-b0024" id="zh-b0024"></a>

请确保您的系统满足以下安装 ecoSpoldAccess 的要求。

如果您的系统不满足操作系统要求，可以手动安装 Microsoft XML Parser 第 6 版。可从 [CNET](https://download.cnet.com/Microsoft-Core-XML-Services-MSXML-6-0/3000-7241_4-10725999.html) 免费下载（Microsoft Core XML Services (MSXML) 6.0）。

### <strong>下载 ecoSpold1 Access 宏</strong> <a href="#zh-b0027" id="zh-b0027"></a>

#### <strong>适用于 Excel 2003 的 ecoSpold Access</strong> <a href="#zh-b0028" id="zh-b0028"></a>

- 操作系统：Windows XP Service Pack 3 或 Windows Vista
- Microsoft Excel：2003 版

![doc-icon](../assets/024d8f149226-doc-icon.png) 下载 [ecoSpoldSetup 1.9.17](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/ecospold_setup.1.9.17.zip)

#### <strong>仅适用于 Excel XP 的 ecoSpold Access</strong> <a href="#zh-b0032" id="zh-b0032"></a>

- 操作系统：Windows XP Service Pack 3（不适用于 Vista 或更高版本！）
- Microsoft Excel：XP 版（仅限此版本！）

- 请注意，该版本已停止支持，无法在 Microsoft Vista 上运行，并且可能包含过时数据。

![doc-icon](../assets/024d8f149226-doc-icon.png) 下载 [ecoSpold 1.9.10](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/ecospold_setup.1.9.10.zip)

### <strong>配套文件和文档</strong> <a href="#zh-b0037" id="zh-b0037"></a>

更多信息见文档文件，可在您选定的安装目录的“ecospold\Doc”子目录中找到，也可在下方获取。

ecoSpold1 目录还包含 XML-Schema、ecoSpold1 数据格式说明以及示例文件。

请注意，示例文件仅包含编造的虚构数据。

R. Heijungs 开发了一款软件，可帮助在 CMLCA 与 ecoSpold1 之间转换均匀分布、三角分布、正态分布和对数正态分布这四种统计分布的表示形式。

- ![doc-icon](../assets/024d8f149226-doc-icon.png) 下载 [ecoSpold1 许可协议](../assets/ca185cb4a589-Licence-Agreement-ecoSpold1.pdf)
- ![doc-icon](../assets/024d8f149226-doc-icon.png) 下载 [ecoSpold1 文档](../assets/61e82dab93c7-200810_documentation_ecospold_1.3.pdf)
- ![doc-icon](../assets/024d8f149226-doc-icon.png) 下载 [ecoSpold1 修订公开征求意见](../assets/58422431916f-200905_ecospold1_open_hearing_feedback_with_comments_on_implementation_in_v2.pdf)

{% endtab %}

{% tab title="English 原文" %}

## The ecoSpold1 format was used in ecoinvent version 2 and was superseded by ecoSpold2. <a href="#en-b0002" id="en-b0002"></a>

Oct 26th, 2023

### <strong>The ecoSpold1 Data Exchange Format</strong> <a href="#en-b0004" id="en-b0004"></a>

It is based on XML (extended markup Language) and related technologies (XSL, XSLT, Schema).

The data format was developed as part of the ecoinvent projects. The ecoSpold1 format was used in ecoinvent version 2 internal applications as well. The administration tool, the editor tool, and the server tool used this format for the exchange of data, both amongst each other as well as with other applications.

The [online platform](https://ecoquery.ecoinvent.org/login) of the ecoinvent version 2 database and ecoSpoldAccess both support and use ecoSpold1.

The data exchange format lists all data fields available for the documentation of a single data set (LCI raw data and meta information of a unit process) and specifies the expected content.

It takes its pattern from the international SPOLD 99 data exchange format and has been adapted to the ISO Technical Specification ISO 14048.

[ecoSpold1 Data Exchange Format](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/ecospold1_data_exchange_format.zip)

### <strong>Features of the ecoSpold1 Access Macros</strong> <a href="#en-b0011" id="en-b0011"></a>

The ecoSpoldAccess macro allows you to open ecoSpold1 files in Microsoft Excel, edit them in a limited way and to export them back from Microsoft Excel format to the ecoSpold1 format. The ecoSpoldAccess add-in was developed for Windows XP and Excel 97.

However, due to the migration to [ecoSpold2](ecospold2.md), the ecoSpoldAccess add-in is no longer maintained and is not compatible with more recent versions of Microsoft Excel.

Please note that the conversion from Microsoft Excel to ecoSpold1 of results files may take some time (around ten to twenty minutes) depending on the Excel version used and its settings. If you encounter problems and you would need the Microsoft Excel files for LCA calculations, please [contact us](https://ecoinvent.org/contact-us/).

If you just want to look at the files, please visit the ecoinvent version 2 database then simply [login](https://ecoinvent.org/database-login/) to the online platform of the database.

### <strong>Installing the ecoSpold1 Access Macros</strong> <a href="#en-b0016" id="en-b0016"></a>

Below are two links to access the ecoSpoldAccess macro and the corresponding license agreement. Choose the link which best fits your operating system and version of Microsoft Excel.

To install the ecoSpoldAccess macro on your computer download the file EcoSpoldSetup to your computer and run the executable.

#### <strong>Functionality</strong> <a href="#en-b0019" id="en-b0019"></a>

The installation will add the button bar “ecoSpoldAccess” in Microsoft Excel.   
To convert spold1 files downloaded from the ecoinvent database, run Excel and click on the button “ecoSpold2Excel.”

#### <strong>Deinstall Older Versions</strong> <a href="#en-b0021" id="en-b0021"></a>

In case you are using an older versions of the ecoSpold software make sure to deinstall all old versions before installing the new one.

The procedure to deinstall previous versions is described in the [ecoSpold documentation](../assets/61e82dab93c7-200810_documentation_ecospold_1.3.pdf).

#### <strong>System Requirements</strong> <a href="#en-b0024" id="en-b0024"></a>

Please make sure that your system meets the following requirements to install the ecoSpoldAccess.

If your system does not meet the operating system requirements you can manually install the Microsoft xml Parser Version 6. It can be downloaded for free from [CNET](https://download.cnet.com/Microsoft-Core-XML-Services-MSXML-6-0/3000-7241_4-10725999.html) (Microsoft Core XML Services (MSXML) 6.0).

### <strong>Download the ecoSpold1 Access Macros</strong> <a href="#en-b0027" id="en-b0027"></a>

#### <strong>ecoSpold Access for Excel 2003</strong> <a href="#en-b0028" id="en-b0028"></a>

- Operating System: Windows XP Service Pack 3 or Windows Vista
- Microsoft Excel: Version 2003

![doc-icon](../assets/024d8f149226-doc-icon.png)  Download [ecoSpoldSetup 1.9.17](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/ecospold_setup.1.9.17.zip)

#### <strong>ecoSpold Access for Excel XP Only</strong> <a href="#en-b0032" id="en-b0032"></a>

- Operating system: Windows XP Service Pack 3 (not Vista or later!)
- Microsoft Excel: Version XP (only!)

- Please be aware that this version is no longer supported and will not work on Microsoft Vista and may contain out-of-date data.

![doc-icon](../assets/024d8f149226-doc-icon.png)  Download [ecoSpold 1.9.10](https://support.ecoinvent.org/hubfs/Knowledge%20Base/Resources/Data%20Formats/ecospold_setup.1.9.10.zip)

### <strong>Supporting Files and Documents</strong> <a href="#en-b0037" id="en-b0037"></a>

Further information is included in a documentation file which can be found in the subdirectory “ecospold\Doc” of the installation directory you selected or below.

The ecoSpold1 directory also contains the XML-Schema and a description of the ecoSpold1 data format along with sample files.

Please note that the sample files only contain fabricated, fictitious data.

R. Heijungs developed software that facilitates the conversion steps between CMLCA and ecoSpold1 of representations of the four statistical distributions uniform, triangular, normal, and lognormal.

- ![doc-icon](../assets/024d8f149226-doc-icon.png)  Download [ecoSpold1 License Agreement](../assets/ca185cb4a589-Licence-Agreement-ecoSpold1.pdf)
- ![doc-icon](../assets/024d8f149226-doc-icon.png)  Download [ecoSpold1 Documentation](../assets/61e82dab93c7-200810_documentation_ecospold_1.3.pdf)
- ![doc-icon](../assets/024d8f149226-doc-icon.png)  Download [Open hearing for ecoSpold1 revision](../assets/58422431916f-200905_ecospold1_open_hearing_feedback_with_comments_on_implementation_in_v2.pdf)

{% endtab %}

{% endtabs %}

## 翻译与审校注记 <a href="#review-notes" id="review-notes"></a>

- **已处理／已说明 · b0005**：原文将 XML 全称写为 extended，规范全称应为 Extensible Markup Language。 译文采用规范中文全称，并保留原文错误英文作为对照。 [查看完整记录](../review/issues.md#issue-011)
