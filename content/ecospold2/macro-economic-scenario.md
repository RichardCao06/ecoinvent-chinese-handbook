# 宏观经济情景

对应官方格式类型：`TMacroEconomicScenario`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 情景是主数据引用，也可能是子数据集的变化依据 <a href="#read-tmacroeconomicscenario" id="read-tmacroeconomicscenario"></a>

`activityDescription/macroEconomicScenario` 采用 `TMacroEconomicScenario`。属性 `macroEconomicScenarioId` 指向有效情景列表中的宏观经济情景；`macroEconomicScenarioContextId` 指定该情景主数据所属上下文，省略时使用数据集自身的上下文。元素 `name` 是情景名称，供人阅读；不能用它替换情景 UUID 做唯一连接。

元素 `comment` 说明宏观经济子数据集与父数据集默认情景的差异。它是 `TString32000` 文本，而不是混合图片的 `TTextAndImage`。读取情景时，可先保留名称和引用，再结合活动的父数据集关系阅读这段差异说明；仅从名称无法知道哪些输入、输出或其他条件相对于父情景发生了变化。

## 怎样定位、使用与提取

提取情景名称或对比情景数据时，保留情景主数据引用及有效上下文，并阅读 comment。情景字段不是一项投入，不能直接用情景名称推导数量变化；有继承时仍须先展开。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/macroEconomicScenario`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TMacroEconomicScenario")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/macroEconomicScenario[1]",
  "attributes": {
    "macroEconomicScenarioId": "0984f81b-aa81-5830-b34b-99b00a49a684"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学情景"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching scenario"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tmacroeconomicscenario)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
