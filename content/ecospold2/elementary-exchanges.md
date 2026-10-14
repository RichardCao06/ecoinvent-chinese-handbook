# 基本流交换专用字段

对应官方格式类型：`TElementaryExchange`。本篇以文章解释该类型的 6 条字段；复合类型也会说明它们依附在哪个对象上。

## 基本流交换记录与环境的往来 <a href="#read-telementaryexchange" id="read-telementaryexchange"></a>

`TElementaryExchange` 表示单元过程与环境之间的基本流输入或输出，同样继承 `TCustomExchange` 的实例标识、数量、单位、来源和不确定性等共同字段。与中间产品的识别方式相对应，必需的 `elementaryExchangeId` 引用基本流的主数据条目，而可选的 `elementaryExchangeContextId` 指明该主数据所属上下文，省略时使用数据集自身上下文。取数时应保留这个基本流标识，同时保留交换实例 `id`；一个用于识别流，另一个用于识别本数据集中的具体记录。

基本流的分组值与中间交换不同：`inputGroup` 的有效值 4 表示来自环境，`outputGroup` 的有效值 4 表示流向环境。两者仍然只能选择一个，不能因为中间交换有材料、能源或参考产品分组，就把同一套编号移用于基本流。来自环境的资源获取、流向环境的释放，都要结合分组理解；数量的符号不能替代分组判定，也不应在未理解模型含义之前被删除。

必需的 `compartment` 提供区室与子区室的配对信息，由 `TCompartment` 的内部结构表达。原说明中的 `validCompartments` 所引用 XML 文档定义给定语言下有效的区室／子区室配对。可选的 `formula` 可补充化学式，例如分子式，但它不代替基本流主数据或区室。读取环境清单时，应同时取出流标识、名称、方向、数量、单位以及区室配对；不能仅按化学名称把不同区室的流合为一个“总排放”，然后假设可以直接使用同一个表征因子。

## 怎样定位、使用与提取

要拿环境取水或污染物排放，遍历 elementaryExchange，并同时保留 elementaryExchangeId、有效上下文、inputGroup/outputGroup、compartment 和单位。负 amount 不会自动把输出变成输入；同名、不同区室或不同流 UUID 的记录不能直接相加。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/elementaryExchange`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TElementaryExchange")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **4 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/elementaryExchange[1]",
  "attributes": {
    "id": "9da6137e-52d1-5c5f-930a-fed238b20968",
    "amount": "0.04",
    "unitId": "ff547598-1a08-5b8b-904c-a0d8a4d032fd",
    "elementaryExchangeId": "376dc400-e4fb-5da8-a2fb-2f8c581892cb"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "水，来自环境（教学）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Water, from environment (synthetic)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-telementaryexchange)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
