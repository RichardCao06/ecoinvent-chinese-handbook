# 数据录入者

对应官方格式类型：`TDataEntryBy`。本篇以文章解释该类型的 5 条字段；复合类型也会说明它们依附在哪个对象上。

## 录入者说明谁编制并提交了这份记录 <a href="#read-tdataentryby" id="read-tdataentryby"></a>

在 `administrativeInformation/dataEntryBy` 中，`TDataEntryBy` 记录编制数据集并将其录入数据库的人员。属性 `personId` 引用该人员，`personContextId` 指定人员主数据所属上下文，省略时使用数据集自身的上下文。属性 `personName` 和 `personEmail` 分别存储人员的名与姓以及完整电子邮件地址；它们用于显示和联系，身份连接仍依赖人员 ID 与上下文。

属性 `isActiveAuthor` 表示这位人员是否为数据集的活跃作者，完整数据 XSD 的默认值为 `false`。这里的活跃作者是后续维护中的联系角色：其他数据提供者今后修改数据集时，将征询此人的意见。它不能仅凭姓名是否出现在文件中推断，也不等同于版权人、审核人或原始数据采集者。取数时应保留这个标记，才能区分一般录入人员与需要在后续变更中联系的作者。

## 怎样定位、使用与提取

需要追溯数据录入人员时，读取 dataEntryBy 的人员 UUID、有效上下文及主数据冗余信息。录入者与原始数据生成者是不同角色；只凭人名不宜关联或去重人员记录。生成工具则读取文件属性的 fileGenerator。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`administrativeInformation/dataEntryBy`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TDataEntryBy")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/administrativeInformation[1]/dataEntryBy[1]",
  "attributes": {
    "personId": "2163e122-88c4-55e7-af84-00947e9b7b0a",
    "personName": "Teaching author",
    "personEmail": "demo@example.invalid",
    "isActiveAuthor": "false"
  },
  "children_excerpt": []
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tdataentryby)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
