# 影响指标结果

对应官方格式类型：`TImpactIndicatorResult`。本篇以文章解释该类型的 11 条字段；复合类型也会说明它们依附在哪个对象上。

## 影响评价结果不是一条环境排放 <a href="#read-timpactindicatorresult" id="read-timpactindicatorresult"></a>

`TImpactIndicatorResult` 保存已经计算出的影响指标结果。它的必需字段 `amount` 是指标值，不是某种污染物的排放量，也不是未表征的资源消耗量；即使字段名与交换数量相同，读数含义也由所在类型决定。提取 LCIA 结果时，需要同时保留方法、类别、指标和单位，不能只取出一列数值，也不能把这些结果与基本流交换相加。

一条结果包含三层必需的主数据标识。`impactMethodId` 引用影响评价方法；`impactCategoryId` 按 XSD 引用方法中的影响类别；`impactIndicatorId` 引用具体影响指标。它们分别回答采用什么方法、结果属于什么类别、使用什么指标。这些 ID 均为 UUID，不能因显示名称近似而互相替代。原表字段 1820 的说明写作“对影响类别所属方法的引用”，但其 XSD 引用对象为 `TImpactMethodCategory`，与 `impactMethodId` 的 `TImpactMethod` 不同；这项源文矛盾已在审阅中记录，此处明确区分实际的类别引用与方法引用，没有改写原表译文。

可选的 `impactMethodContextId`、`impactCategoryContextId` 和 `impactIndicatorContextId` 分别指定方法、类别和指标主数据所在上下文，任何一个省略时，都使用数据集自身的上下文。结果也包含便于阅读的必需多语言文本：`impactMethodName` 为方法名称，`impactCategoryName` 为类别名称，`name` 为指标名称，`unitName` 为指标值的单位名称。选择语言时应按 `xml:lang` 读取这些名称，不应把多语言版本当成多条独立结果。

因此，读 LCIA 结果的一条可靠路径，是先用方法、类别和指标的标识及上下文确定这条结果的身份，再把 `amount` 与 `unitName` 配对，最后核对活动、产品和系统模型等外部背景及参考数量基准。这个类型自身没有交换的 `inputGroup`、`outputGroup`，也没有为结果另列 `unitId`；不能照搬读取排放交换的字段路径。不同方法、不同指标、不同单位或不同参考基准的结果，应先确认可比性，不能只因中文名称相似就合并或比较。

## 怎样定位、使用与提取

要拿已有碳足迹等结果，读取 impactIndicator，以方法、类别、指标三层 UUID 及有效上下文筛选，再保留 amount 与 unitName。该类型没有独立 unitId 字段，不能凭名称补出 UUID；文件没提供指标时应返回缺失，不能用 CO2 质量冒充影响结果。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/impactIndicator`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-lcia.spold", index=0)
records = read_section(dataset, "TImpactIndicatorResult")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-lcia.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/impactIndicator[1]",
  "attributes": {
    "impactIndicatorId": "9ce9802d-268d-5ac0-af08-ffca6dc91aa2",
    "impactMethodId": "496741dc-72ec-5f95-bedb-078512fde969",
    "impactCategoryId": "07a7bfca-c863-5fd0-a2bf-24aa3af0d959",
    "amount": "13.9"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}impactMethodName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学方法（非官方）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}impactMethodName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching method (synthetic, unofficial)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-timpactindicatorresult)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
