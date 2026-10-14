# 交换的通用字段

对应官方格式类型：`TCustomExchange`。本篇以文章解释该类型的 25 条字段；复合类型也会说明它们依附在哪个对象上。

## 先读交换的共同结构 <a href="#read-tcustomexchange" id="read-tcustomexchange"></a>

一个活动的数据不只是一个总数，而是一组说明“交换了什么、交换多少、用什么单位表示”的记录。`TCustomExchange` 定义中间交换与基本流交换共有的字段；`TIntermediateExchange` 和 `TElementaryExchange` 在它的基础上增加各自的信息。因此，读到具体交换时，既要读取该交换类型的专用字段，也要读取这些共同字段。下文用代码标出实际 XML 名称：属性写在元素的开始标签中，名称、说明等内容则由子元素承载。

识别一条记录时，先区分名称与标识。必需的 `name` 是交换名称，必需的 `id` 是这条交换实例的 UUID。它不是产品的 `intermediateExchangeId`，也不是基本流主数据的 `elementaryExchangeId`：同一数据集可以有多条交换引用同一个主数据条目，因此按产品或基本流标识去重会丢失交换实例。随后读取必需的 `amount`，它以 `TFloatNumber` 表示这条交换的数量；必需的 `unitId` 引用该数量的单位，必需的 `unitName` 提供便于阅读的单位名称。可选的 `unitContextId` 指明单位主数据所属上下文，省略时使用数据集自身的上下文。取数时应把交换实例标识、数量、单位标识及其上下文一起保留，以免把不同单位或不同主数据空间的同名记录合并。

`name`、`unitName` 和可选的 `comment` 可以用多种语言表达；`comment` 为这条交换提供一般说明。读取文本时，应根据 `xml:lang` 选择需要的语言，而不是把多个语言版本串成一个名称。可重复的 `synonym` 是同义词，每条最多 80 个字符，可有 0..n 条；与普通多语言字符串不同，同义词允许同一个 `xml:lang` 对应多个条目。可重复的 `tag` 则是供筛选、分组和搜索使用的开放关键词。原说明写明，`validTags` 主文件中找不到某个标签时，语义验证应提示信息，而不应把它当成错误。`casNumber` 是可选的化学品 CAS 编号；这份格式说明给出的形式为 `000000-00-0`，并允许第一组数字不足六位。CAS 编号帮助识别化学物质，但并不能替代交换实例标识、单位或基本流区室信息。

一些交换数量还带有计算关系。可选的 `variableName` 为交换数量提供公式中的简称；文档要求以字母 a-z 开头，可含字母、数字和下划线，且不区分大小写，例如 `calorific_Value` 与 `Calorific_value` 等同。可选的 `mathematicalRelation` 通过变量名或 `REF` 函数引用流、参数和属性，在给定一组变量值后，其计算结果写入 `amount`。当 `isCalculatedAmount` 为 `true` 时，`amount` 是 `mathematicalRelation` 或 `transferCoefficient` 的计算值；共同交换类型的 XSD 将这一标记默认设为 `false`。解析文件可以读取已保存的数量与公式，但重新求值需要支持对应公式语言，不能把公式字符串本身当成数值。

可重复的 `transferCoefficient` 将特定输入与特定输出关联，表示该输入中流向该输出的份额；按其专用结构说明，系数应乘以被引用交换的数量。可选的 `uncertainty` 用分布函数、参数和／或数据质量谱系信息描述交换数量的不确定性。可重复的 `property` 描述交换的干质量、含水率、价格或特定元素和物质的含量。这三类字段都是具有内部结构的元素，读数时不能只提取其标签文字，也不能把属性值、不确定性参数或转移系数直接相加到交换数量中。

可选的 `sourceId` 指向有效来源，`sourceContextId` 指明来源所属上下文，省略时使用数据集上下文。`sourceYear` 记录出版或交流年份；网站来源记录最后访问年份。`sourceFirstAuthor` 用姓和名字缩写记录第一作者，例如 Einstein A.；在现场测量、口头交流、个人书面交流和问卷调查这几类来源中，即 `sourceType` 为 4、5、6、7 时，记录提供信息的人员。`pageNumbers` 给出文章或较大型出版物中实际取数的页码。这组字段与数量一同读取，才能追溯某条交换的依据；`sourceYear` 不等于活动数据的有效年份。

若交换有独立的分配设置，`specificAllocationPropertyId` 指定分配所用属性，并覆盖数据集层面由 `masterAllocationPropertyId` 定义的默认设置；`specificAllocationPropertyContextId` 指明该属性所属上下文，省略时使用数据集上下文。这些字段说明应使用哪项属性，不能单凭它们自行构造一套新的分配算法。继承时还要读取 `sourceIdOverwrittenByChild` 与 `specificAllocationPropertyIdOverwrittenByChild`：子数据集要移除对应的主数据引用，必须把相应标记设为 `true`；否则，引用不再出现仍可能被解释为“保留父数据集的值”，不能据此判断它已被清空。

## 怎样定位、使用与提取

先统一读取交换实例 id、amount、unitId、name、unitName 及计算标记，再结合具体中间交换或基本流节点读取方向与对象身份。这里读取的 property、uncertainty 等仍属于当前交换，不能把子结构里的 amount 混进交换量总和。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange`；`flowData/elementaryExchange`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TCustomExchange")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **6 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/intermediateExchange[1]",
  "attributes": {
    "id": "b8754d71-a0c7-5b08-a889-67d6f1146d58",
    "amount": "10",
    "unitId": "a4800e12-54b1-5444-a6d0-b48a59529439",
    "intermediateExchangeId": "c5a1fe25-46d4-5646-9d78-5c10b6bfdeae"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学产品"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching product"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tcustomexchange)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
