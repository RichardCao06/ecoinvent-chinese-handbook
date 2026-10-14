# 所需上下文引用

对应官方格式类型：`TRequiredContextReference`。本篇以文章解释该类型的 7 条字段；复合类型也会说明它们依附在哪个对象上。

## 解析跨上下文引用前，先核对主数据依赖 <a href="#read-trequiredcontextreference" id="read-trequiredcontextreference"></a>

每个 `requiredContext` 条目采用 `TRequiredContextReference`，说明读取文件所需的主数据上下文。属性 `requiredContextId` 引用主数据文件所属上下文，元素 `requiredContextName` 提供相应名称；属性 `requiredContextFileLocation` 是可选 URI，指向包含这一上下文主数据文件的目录。它给出的是主数据目录位置，不能直接当成某一条主数据对象的 UUID，也不应未经判断就当成单个 XML 文件路径。

这个条目也有属性 `majorRelease`、`minorRelease`、`majorRevision` 和 `minorRevision`。它们用于确保该活动所需的主数据条目在相应版本中存在，描述的是所依赖上下文的版本要求，不是当前数据集自己的版本。完整 XSD 要求主发布号与次发布号，主修订号与次修订号则为可选。读取程序需知道各上下文，并知道实际主数据文件在哪里；只有 UUID 文本而没有对应主数据文件，并不能完成引用解析。

原文另有一处结构要求与说明冲突：它称省略 `requiredContextId` 时应使用数据集自身上下文，但本版完整 XSD 把这个属性设为必填。因而，不能依据这句回退说明生成缺少该属性却宣称通过完整模式验证的文件。教程保留这项文档差异，具体适用条件需由数据方澄清；在实现当前完整模式时，应核对 `use="required"` 的实际要求。另须区分子差异模式：`EcoSpold02ChildDataTypes.xsd` 将 `requiredContextId` 及四个版本属性设为可选，也将 `requiredContextName` 设为可省略；这并不改变完整数据模式的必填要求。读取子记录时仍须结合继承及实际上下文，不能把省略值直接当成一个已经解析成功的主数据引用。

## 怎样定位、使用与提取

需要解析跨上下文的主数据 UUID 时，遍历 requiredContext，每条保留引用 UUID、描述和完整版本标记。它列出依赖，不会把外部主数据内容自动嵌入 XML；缺少所需上下文时应报告无法完整解析，而不是编造名称或覆盖为当前上下文。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`administrativeInformation/fileAttributes/requiredContext`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TRequiredContextReference")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-trequiredcontextreference)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
