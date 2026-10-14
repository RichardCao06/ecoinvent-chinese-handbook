# 时间范围

对应官方格式类型：`TTimePeriod`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 时间段与整段有效性要分开判断 <a href="#read-ttimeperiod" id="read-ttimeperiod"></a>

`activityDescription/timePeriod` 采用 `TTimePeriod`。属性 `startDate` 和 `endDate` 是数据集有效时间段的完整日期，采用年-月-日；它们与文件创建、编辑和导出时间不同。属性 `isDataValidForEntirePeriod` 说明该活动的基本流交换和中间交换是否对所列整个时间段都有效，不能仅根据起止日期推定整段有效。

当 `isDataValidForEntirePeriod` 不为真时，可在元素 `comment` 中解释。这个 `TTextAndImage` 字段也可说明单元过程的时间相关性，例如较早数据是否仍适用于当前活动；还可说明为什么数据不覆盖整个期间、实际在哪些较短期间内有效。取数时应将起止日期、整段有效性标记和这段说明一并保存，否则会丢失日期区间内的重要限定。

## 怎样定位、使用与提取

按年份选择数据时，读取 startDate、endDate 和 isDataValidForEntirePeriod。日期范围覆盖目标年份，并不自动说明该段内每一天的数据都同样适用；不要把文件编辑时间当作清单年份。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/timePeriod`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TTimePeriod")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/timePeriod[1]",
  "attributes": {
    "startDate": "2025-01-01",
    "endDate": "2025-12-31",
    "isDataValidForEntirePeriod": "true"
  },
  "children_excerpt": []
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-ttimeperiod)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
