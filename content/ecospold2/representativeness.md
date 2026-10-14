# 代表性

对应官方格式类型：`TRepresentativeness`。本篇以文章解释该类型的 6 条字段；复合类型也会说明它们依附在哪个对象上。

## 代表性：理解数据代表的总体，以及样本如何形成 <a href="#read-trepresentativeness" id="read-trepresentativeness"></a>

`representativeness` 位于 `modellingAndValidation` 中，采用 `TRepresentativeness` 类型，记录数据集的代表性和数据如何采样或计算。它帮助读者判断数据能否服务于研究中的地区、技术和时间条件，而不是为每项交换提供一个新的数量。首先，`systemModelId` 引用所用系统模型，`systemModelContextId` 指定该模型的上下文，省略时采用数据集自身的上下文；`systemModelName` 是该引用的纯文本名称。这些信息说明活动数据集如何链接成产品系统。原文举出的 `undefined`、`attributional, average current suppliers, revenue allocation` 和 `consequential, small-scale, long-term decisions` 是该历史格式说明中的模型描述，不能未经核对就视为当前全部系统模型名称或完整清单。在正常 XSD 中，只要此可选结构出现，模型引用和模型名称便是其内部必填项。

`percent` 表示所采样数据占活动拟代表总体的百分比。该总体由地理区域、技术和时间范围共同确定，因此读取百分比之前，要先知道它针对的是哪个总体；它不是这个活动对产品系统的贡献率，也不是供应市场的份额。原表和 XSD 都将最大值规定为 100，但未填写这一可选属性，不代表覆盖比例为零或百分之百。

`samplingProcedure` 描述量化交换所用的采样和计算程序，应说明某些基本流交换或中间交换是否采用不同于一般程序的做法，以及组合不同采样程序可能产生的问题。这里有一个需要对照模式的源文疑点：英文说明随后混入了文本和图像字段的通用描述，但实际 XSD 把 `samplingProcedure` 定义为 `TString32000` 多语言文本，而不是 `TTextAndImage`。读取它应保留文本和语言，不应因为这段通用说明就尝试读取嵌套的 `text`、`imageUrl` 或 `variable`。

`extrapolations` 记录数据从其他时间、其他地理区域或其他技术外推而来的情况，以及外推如何实施。说明应交代单个交换是否采用不同的外推方法；如果把一个国家运行活动的数据用于另一个国家，可以在这里注明原始代表性，并记录外推引起的均值变化。读取这段内容后，才能把样本覆盖、原始来源和当前适用范围联系起来；不能仅因模型名称或地区代码符合要求，就跳过采样及外推说明。

## 怎样定位、使用与提取

需要解释系统模型、样本总体或外推依据时，读取 representativeness 的全部字段，尤其保留 systemModelId 与上下文。比较数量之前先核对模型；百分比或外推描述是代表性元数据，不是清单中另一项数量。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`modellingAndValidation/representativeness`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TRepresentativeness")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/modellingAndValidation[1]/representativeness[1]",
  "attributes": {
    "systemModelId": "a381359e-f5e9-58f7-90b2-e0f2251938a1",
    "systemModelContextId": "f71ac544-3bc8-5c15-8ea4-072d907663f1"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}systemModelName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学约定系统（非官方模型）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}systemModelName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching convention (not an official model)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-trepresentativeness)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
