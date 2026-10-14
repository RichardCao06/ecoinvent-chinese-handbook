# 转移系数

对应官方格式类型：`TTransferCoefficient`。本篇以文章解释该类型的 11 条字段；复合类型也会说明它们依附在哪个对象上。

## 转移系数：追踪特定投入对特定输出的贡献 <a href="#read-ttransfercoefficient" id="read-ttransfercoefficient"></a>

转移系数将一项特定投入与一项特定输出关联，记录该投入对该输出的贡献份额，用于根据投入量计算相应的输出贡献。在 XSD 中，`transferCoefficient` 定义在 `TCustomExchange` 内，因此中间交换和基本流交换都可以通过继承包含它，不能把它限制为只供中间产品使用。阅读时应同时保留容纳系数的交换和被引用交换的身份，才能知道所描述的是哪一条投入输出关系。

`exchangeId` 引用的是某个具体交换的 UUID，即交换实例的 `id`，不是产品主数据的 `intermediateExchangeId` 或基本流主数据的 `elementaryExchangeId`。同一主数据条目可能在同一个数据集中被多项交换引用，所以两种身份不能混用。系数自身的 `amount` 是转移系数数值；原说明要求将它与所引用交换的数量相乘，以得到该系数对应的数量贡献。这个 `amount` 不是另一笔投入量，也不是不加区分地分配整个过程环境影响的因子。不能仅凭一个系数的存在，就推出完整质量平衡、输出总量或通用过程计算算法。

`mathematicalRelation` 可以通过变量名或 `REF` 引用流、参数和属性来计算系数，结果写入这个系数的 `amount`；`isCalculatedAmount` 为 true 时表示该值是数学关系的计算结果。可选的 `uncertainty` 描述系数数值的不确定性，应与被引用交换数量的不确定性区分。取数时，可以读取已存系数与它的引用对象；若要进一步重新计算，必须另行处理引用、公式和不确定性，不能把它们合并成一个未经格式说明支持的计算规则。

证据链由 `sourceId`、`sourceContextId`、`sourceYear` 和 `sourceFirstAuthor` 组成。`sourceId` 指向有效来源，原选项说明将其关联到 `modellingAndValidation` 部分定义的来源；`sourceContextId` 指定来源的上下文，省略时使用数据集上下文；`sourceYear` 是出版或交流年份，网站记录最后访问；`sourceFirstAuthor` 是第一作者姓氏和名字缩写，现场测量、口头交流、个人书面交流和问卷调查，即 `sourceType` 为 4、5、6、7 时，则填写提供信息的人员。在子数据集中移除继承的来源引用，需要将 `sourceIdOverwrittenByChild` 设为 true，否则移除会被解释为保留父值。`comment` 用于每个系数的补充说明，读取时应与该系数而非其他交换的说明关联。

## 怎样定位、使用与提取

需要追踪某投入对某输出的贡献时，读取交换下的 transferCoefficient，保留外层交换 id 及内部 exchangeId 等引用。这个读取例子保存系数与表达式，不执行贡献计算；先弄清它引用的是哪个交换实例，而非把主数据 UUID 当成实例 id。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange/transferCoefficient`；`flowData/elementaryExchange/transferCoefficient`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TTransferCoefficient")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-ttransfercoefficient)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
