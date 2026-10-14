# 完整教程：读懂 XML 并提取数据

拿到一份 `.spold` 文件后，最有用的问题通常是：它描述哪个活动、为多少参考产品建立清单、消耗多少电力或材料、排放了什么、这些量的单位是什么，以及它是否已经包含上游过程或影响评价结果。回答这些问题，需要同时读懂 XML 的层级和生命周期清单的计量口径。单独搜索 `amount`，会把交换量、参数值、属性值和影响指标值混在一起。

这套教程从一份可下载、可运行的教学 demo 出发，先演示实际读取过程，再按文件结构解释官方格式说明中的全部 243 条字段。各章采用文章讲解；需要核对类型、长度和必填标记时，可读最后的[完整中文格式译表](format-reference.md)。

字段依据是官方 `EcoSpold02.html` 及同包 XSD：下载包名称为 v1.0.13，XSD 的 `version` 为 2.0.13。XML 模式版本与 ecoinvent 数据库版本应分别核对。本文提供该格式包的参考解释；读取实际文件时，还应核对其来源、系统模型、导出类型和适用模式。官方入口见 [ecoSpold2](https://support.ecoinvent.org/ecospold2)，原件见[格式包 ZIP](original/documentation_on_ecospold2_format.v1.0.13.zip)。



下面按 XML 的顺序展开完整字段讲解。关联字段放在同一段落中解释，便于把名称、引用、数量和证据连接起来。主 HTML 的 243 条定义都在这些段落中覆盖；基础文本类型内部的 `xml:lang`、`index` 等额外节点，还需要结合原包 XSD 阅读。


## 按问题进入教程

先读[判断 UPR、LCI 与 LCIA](data-levels.md)，确定数量的层级，再读[XML 结构、命名空间与继承](xml-structure.md)和[demo 读取演示](demo-walkthrough.md)。五组字段文章沿文件结构展开；[提取与查询实践](extraction-practice.md)提供完整代码和筛选方法。最后的[官方格式说明中文版本](format-reference.md)集中保留原始表格译文。

### 活动描述

[活动](activity.md) · [活动分类](classification.md) · [地理区域](geography.md) · [技术](technology.md) · [时间范围](time-period.md) · [宏观经济情景](macro-economic-scenario.md)

### 交换数据与结果

[交换的通用字段](exchanges.md) · [中间交换专用字段](intermediate-exchanges.md) · [基本流交换专用字段](elementary-exchanges.md) · [参数](parameters.md) · [影响指标结果](impact-indicators.md)

### 复合类型

[区室与子区室](compartments.md) · [不确定性与分布参数](uncertainty.md) · [交换属性](properties.md) · [转移系数](transfer-coefficients.md) · [文本、图像与文本变量](text-and-image.md)

### 建模与审查

[代表性](representativeness.md) · [审查](review.md)

### 管理信息

[数据录入者](data-entry.md) · [数据生成者与发布](publication.md) · [文件属性](file-attributes.md) · [所需上下文引用](required-contexts.md)
