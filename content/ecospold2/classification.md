# 活动分类

对应官方格式类型：`TClassification`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 用分类定位行业，不把名称当作主数据标识 <a href="#read-tclassification" id="read-tclassification"></a>

活动描述中的 `classification` 可重复出现，每一项采用 `TClassification`，把一个分类体系与其中的类别配对。元素 `classificationSystem` 给出体系名称，如原文示例 `ISIC Rev. 4`；`classificationValue` 给出活动在该体系中所属的类别。它们便于展示和筛选，但机器解析的主数据引用是属性 `classificationId`，指向有效分类列表中的分类值。`classificationContextId` 指定这个分类所属上下文，省略时采用数据集自身的上下文。取数时应逐项保留体系、类别和引用标识，不能假定只有一个分类，也不能将不同体系中看起来相同的类别文本合并为同一条主数据。

这里有一处需明确交代的原文差异：字段说明把 `classificationSystem` 和 `classificationValue` 称为可选纯文本值，而本版完整数据 XSD 将两个元素设为至少出现一次，官方 HTML 表格也标为必填。阅读已有文本与校验文件结构是不同操作；校验当前完整数据时应按所用 XSD 执行，不能根据说明中的“可选”自行删除元素。子数据集另有差异模式，其规则还需结合继承处理。

## 怎样定位、使用与提取

需要按行业或某个分类体系筛选活动时，把同一 classification 节点内的 classificationSystem 和 classificationValue 成对保存。不同体系的同名类别不能直接合并；应连同相应标识和上下文核对。这个类型也用于中间交换的产品分类，位置为 flowData/intermediateExchange/classification；返回的父路径用于区分活动分类与产品分类，按行业筛选活动时只取 activityDescription 下的记录。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/classification`；`flowData/intermediateExchange/classification`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TClassification")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tclassification)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
