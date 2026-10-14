# 文本、图像与文本变量

对应官方格式类型：`TTextAndImage`。本篇以文章解释该类型的 3 条字段；复合类型也会说明它们依附在哪个对象上。

## 文本和图像：按顺序组织说明，用文本变量继承局部内容 <a href="#read-ttextandimage" id="read-ttextandimage"></a>

`TTextAndImage` 是一般说明、技术描述和审查详细意见等字段采用的复合结构。实际 XSD 将它定义为可以多次出现的 `xsd:choice`，其中可交错选择 `text`、`imageUrl` 和 `variable`；这与不确定性中恰选一种分布的选择组不同。它可以包含多个文本和图像片段，而不是一次性固定为“一个文本加一张图”。原英文说明多次使用 `imageUri`，但所附 XSD 的实际图像元素名是 `imageUrl`。教程取数应按实际元素名识别，源文这一不一致仍在审校注记中保留，不能据说明文字生成一个并不存在的 `imageUri` 元素。

`text` 是描述当前部分的自由文本，使用 `TIndexedString32000` 类型，其 `index` 属性指定显示顺序。`imageUrl` 保存图像 URI，也有必填的整数 `index`，用来把图像插入文本之间。还原正文时，必须结合这些顺序值，而不是分别收集全部文本和全部图片后拼接。多语言文本还可能带有 `xml:lang`，取数时应保存语言信息，不能将不同语言片段无条件混成一篇说明。具体位置上的索引唯一性和其他条件，应以包含该字段的 XSD 声明为准。

`variable` 则是 `TNamedString32000` 类型的文本变量定义：其必填 `name` 属性给出变量名，元素文本给出变量值，正文可以通过 `{{variablename}}` 引用它。子活动数据集可以重新定义父文本中的变量值，同时保持其余父文本不变；这是修改继承说明中局部内容的机制。它与交换、属性或参数的数学 `variableName` 不同，也不是 `mathematicalRelation` 的数值公式参数。读取文本变量不意味着要运行算术求值；同样，`variable` 没有文本和图像所用的 `index` 属性，不能照搬这两类片段的排序方式处理它。

## 怎样定位、使用与提取

需要提取说明正文时，遍历同一父节点的 children 读取 text、imageUrl 和 variable 等内容，同时保留 index、xml:lang 与变量名。children 保留原始 XML 顺序；组织展示内容时，应按 index 与语言关联和排序。这里只读取字段内容，不访问图像链接；继承的 PARENTTEXT 或文本变量要在解析继承之后展开。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/activity/generalComment`；`activityDescription/activity/allocationComment`；`activityDescription/geography/comment`；`activityDescription/technology/comment`；`activityDescription/timePeriod/comment`；`modellingAndValidation/review/details`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TTextAndImage")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/activity[1]/generalComment[1]",
  "attributes": {},
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}text",
      "attributes": {
        "index": "1",
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学构造，非 ecoinvent 真实数据。仅用于格式、读数和算术比例演示。参考数量不是默认1；不据此演示分配、完整LCI或官方LCIA算法。"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}text",
      "attributes": {
        "index": "2",
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Synthetic teaching data, not real ecoinvent data. Format and arithmetic-ratio demonstration only; no allocation or official LCI/LCIA algorithm."
    }
  ]
}
```

这里的外层说明节点可能没有属性，具体文字在 `children` 中的 `text` 节点；继续查看其子节点，而不要因为外层 `text` 是空白就认为说明不存在。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-ttextandimage)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
