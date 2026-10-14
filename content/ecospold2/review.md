# 审查

对应官方格式类型：`TReview`。本篇以文章解释该类型的 11 条字段；复合类型也会说明它们依附在哪个对象上。

## 审查记录：把意见、人员和所审版本对应起来 <a href="#read-treview" id="read-treview"></a>

`review` 位于 `modellingAndValidation` 中，采用 `TReview` 类型，记录开展鉴定性评审的人员、主要结果、结论和建议。父级允许多个 `review`，因此一份数据集可以有多位评审者或多条审查记录；读取时不能只取第一条便覆盖其余意见。另一方面，一条记录包含的姓名、日期和意见只证明它记录了一次评审，并不自动代表整个数据库已获官方认证。

每条评审由 `reviewerId` 引用人员主数据，原表将它对应到人员字段 3610；`reviewerContextId` 指定人员上下文，省略时采用数据集自身的上下文。`reviewerName` 记录名字和姓氏，`reviewerEmail` 记录完整电子邮件地址，`reviewDate` 是验证或评审日期。这些信息应共同保留，才能将意见对应到具体评审者及其时间，而不应只凭姓名文本匹配人员身份。

审查所针对的数据集版本由 `reviewedMajorRelease`、`reviewedMinorRelease`、`reviewedMajorRevision` 和 `reviewedMinorRevision` 四个整数属性分别记录，依次对应文件属性中的字段 3800、3805、3810、3815，即主发布、次发布、主修订和次修订部分。它们不是审查记录自身的编号，也不能只保留前两个数字。阅读时应把四部分版本与当前文件的版本信息对照：如果记录针对较早版本，就不能把其意见不加判断地解释为对当前修改后内容的审查结论。正常 XSD 中，这四项版本、评审者引用、姓名、邮件及日期在一条出现的 `review` 内均必填；子数据集需另按其对应模式判断。

详细意见存于可选的 `details`，它使用 `TTextAndImage`，因此可以按 `index` 组织文本与图像，并使用 `variable` 文本变量在继承数据集中改写局部内容。这里同样应以实际的 `imageUrl` 元素名读取，而不是原说明中混用的 `imageUri`。`otherDetails` 则是普通多语言文本，保存评审过程的进一步信息，例如数据集首次发布后补充的小幅修正。两者的结构不同，但都应与该条记录的人员和所审版本一起阅读，避免把发布后的补充说明误当成数值交换，或把历史意见移接到其他版本。

## 怎样定位、使用与提取

需要判断谁审查了哪个版本时，遍历每条 review，把审查人员、日期、被审版本和 details 放在同一记录中。不能以存在 review 节点就认定所有后续版本都被审过；具体审查结论要读意见文本。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`modellingAndValidation/review`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TReview")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-treview)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
