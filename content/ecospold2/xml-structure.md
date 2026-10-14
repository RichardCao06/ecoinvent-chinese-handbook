# XML 结构、命名空间与继承


普通数据集的外层通常是 `ecoSpold/activityDataset`，下面依次组织活动描述 `activityDescription`、数量与结果 `flowData`、建模与审查 `modellingAndValidation`，以及管理信息 `administrativeInformation`。一个 `ecoSpold` 根元素可以包含多个数据集，因此“一个文件等于一个活动”只是某些导出的组织习惯，不能作为解析器的硬编码假设。

`activityDescription` 告诉你数量适用于什么活动、什么地区和时间、采用什么技术，以及哪些活动包含在系统边界内。`flowData` 告诉你投入、产出、环境交换、参数和指标值是多少。`modellingAndValidation` 帮助判断系统模型、代表性、数据怎样推算和是否经过审查。`administrativeInformation` 记录人员、来源、发布和修订、文件时间戳，以及解释主数据引用时所需的上下文。读取交换量后保留这些证据，才能在后续分析中判断两个数能否比较。

在 XML 中，`amount="25"` 这样的写法是属性，`<unitName>kWh</unitName>` 这样的写法是子元素。格式说明里的 `@amount` 用 `@` 表示属性；这个字符不是实际 XML 属性名。程序读取属性用 `.get("amount")`，读取子元素需要按路径查找，再读取其文本。

命名空间也必须参与查找。普通 ecoSpold2 元素使用 `http://www.EcoInvent.org/EcoSpold02`。当文件用 `xmlns="…"` 声明默认命名空间时，Python 中的标签实际包含该 URI；不带命名空间的 `find("flowData")` 往往找不到数据。URI 是标识符，不是每次读取时都要请求的网络地址。[Python ElementTree 文档](https://docs.python.org/3/library/xml.etree.elementtree.html)说明了默认命名空间、元素路径和属性的读取方式。

还有一种容器叫 `childActivityDataset`，记录相对于父数据集的差异。它与 `activityDataset` 两个容器本身都属于 EcoSpold02 命名空间，子数据集使用的类型和内部元素则来自 `EcoSpold02Child` 命名空间。若只有差异文件，应先按继承规则展开父数据，而不是把所有省略字段当作零。本文配套提取器会明确拒绝尚待展开的子数据集容器；完整普通数据集里的父级引用也应保留，不能随意删去。
