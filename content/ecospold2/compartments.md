# 区室与子区室

对应官方格式类型：`TCompartment`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 区室配对决定环境流的具体位置 <a href="#read-tcompartment" id="read-tcompartment"></a>

`TCompartment` 用来说明一条基本流属于哪一组区室与子区室。“区室”既可表达环境接收介质，也可用于自然资源分类，因此本文采用已交叉审阅确定的“区室／子区室”术语。内部的 `compartment` 和 `subcompartment` 是必需的多语言名称，提供所引用配对的纯文本表示；前者是区室名，后者是更细的子区室名。原表分别将它们追溯到字段 5315 和 5325，不应把这些跨表编号误读成该数据集里的交换编号。

必需的 `subcompartmentId` 是配对引用的 UUID，必须在有效区室清单中定义，原表指向字段 5330。可选的 `subcompartmentContextId` 指明子区室所属上下文，省略时使用数据集自身上下文。因而读数时应把配对标识及上下文与显示名称一起保存：显示名称有助于理解，主数据引用用于一致匹配。外层基本流的 `compartment` 元素与内层区室名称的 `compartment` 元素同名，但处于不同结构位置；提取时应按层级识别，避免把整个配对结构当成一段普通文字。

## 怎样定位、使用与提取

要统计某环境介质的排放，定位 elementaryExchange/compartment，配对读取 compartment 与 subcompartment。提取时保留外层基本流的 UUID、单位与方向；区室节点本身没有一笔可加入总量的交换 amount。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/elementaryExchange/compartment`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TCompartment")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **4 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/elementaryExchange[1]/compartment[1]",
  "attributes": {
    "subcompartmentId": "9bfcfd12-1b84-56cf-8bd8-1abc71a30268"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}compartment",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "自然资源"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}compartment",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "natural resource"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tcompartment)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
