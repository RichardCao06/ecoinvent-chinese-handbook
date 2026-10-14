# 技术

对应官方格式类型：`TTechnology`。本篇以文章解释该类型的 2 条字段；复合类型也会说明它们依附在哪个对象上。

## 技术水平要结合有效年份和地点阅读 <a href="#read-ttechnology" id="read-ttechnology"></a>

`activityDescription/technology` 采用 `TTechnology`。属性 `technologyLevel` 是粗粒度的技术分类，默认值为 `3`，可用于建模时选择特定技术水平的过程。值 `0` 为未指定，适用于没有技术水平的市场活动；`1` 为新兴技术，在某些方面技术性能优于现代技术，但纯按经济考虑投资时尚未成为最常安装的选择；`2` 为现代技术，是纯按经济考虑新增产能时采用的、竞争力最强的技术；`3` 为当前技术，介于现代与旧有之间；`4` 为旧有技术，是纯按经济考虑退役时正在退出使用、竞争力最低的技术；`5` 为过时技术，已经不再使用。

这些标签不是设备年龄。技术即使已存在很久，只要仍最有竞争力，就可以标为现代；技术即使出现较晚，也可能很快被更有竞争力的技术取代而标为旧有。同一技术可随数据有效年份变化等级，也可在同一年、不同地区具有不同等级。因此，读取 `technologyLevel` 时应同时读取时间和地理信息，不能将某地区某年的等级外推为全球永久属性。

元素 `comment` 采用 `TTextAndImage`，说明技术的性质、特征及单元过程的技术属性。若活动包含多个子活动，也应描述对应技术，并使用专业工艺名称。提取这段说明，是理解技术差异及决定是否采用数据的步骤；仅用技术等级整数无法替代工艺文档。

## 怎样定位、使用与提取

比较工艺与技术先进程度时，同时阅读 technologyLevel 和 comment。技术等级是适用性信息，不能作为交换量的系数；缺失或“未定义”也不等于零技术投入。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/technology`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TTechnology")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/technology[1]",
  "attributes": {
    "technologyLevel": "3"
  },
  "children_excerpt": []
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-ttechnology)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
