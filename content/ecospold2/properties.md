# 交换属性

对应官方格式类型：`TProperty`。本篇以文章解释该类型的 18 条字段；复合类型也会说明它们依附在哪个对象上。

## 交换属性：把产品特征与交换数量分开理解 <a href="#read-tproperty" id="read-tproperty"></a>

`TProperty` 附在交换的 `property` 元素中，描述干质量、含水率、价格、元素或物质含量等特征。中间交换和基本流交换都继承通用交换结构，因此都可具有这些属性。阅读一条属性时，首先用 `propertyId` 识别它引用的属性主数据，再读描述性文本 `name`；`propertyContextId` 指定该属性主数据所属的上下文，省略时采用数据集自身的上下文。UUID 引用和上下文确定的是属性身份，名称帮助人理解身份，不能仅靠同名文字认定两个属性一定相同。

属性的数值存于自身的 `amount`，其单位由 `unitId` 引用，`unitName` 提供单位名称，`unitContextId` 指明单位主数据上下文，省略时同样采用数据集上下文。这里的 `amount` 并不等于外层交换的 `amount`，也不保证与它具有相同单位；价格、含水率和干质量描述的量并不相同。取数时，应把属性定义、数值及单位一起读取，并核查其计量或归一化基准，不能直接把属性量加到投入输出清单中。`isDefiningValue` 为 true 时，属性值属于交换定义的一部分，与交换量之间具有不能针对不同数据集中个别实例改变的固定关系；它既不表示两个数值相等，也不是允许任意按比例改写所有属性的开关。

若属性不是手工指定的值，`mathematicalRelation` 可通过变量名或 `REF` 函数引用流、参数和属性的数值，计算结果写入本属性的 `amount`；`isCalculatedAmount` 为 true 表示这个数值来自该数学关系。`variableName` 则给本属性量一个可在数学关系中引用的名字。文档要求变量名以字母 a-z 开头，可以包含字母、数字和下划线，并且不区分大小写，例如 `calorific_Value` 与 `Calorific_value` 等同。所附 XSD 的 `TVariableName` 类型限定长度最多 40，并采用正则 `\w\S*`，它没有直接表达与文字规则完全等价的约束，因此不能仅凭 XSD 验证通过就认定变量名满足所有公式语言规则。读取已计算数值与重算公式是不同工作；字段定义本身不足以替代公式解析、引用解析和继承处理。

`uncertainty` 描述的是该属性值的不确定性，仍须按所选分布解释，而不是默认套用外层交换的不确定性。`sourceId` 引用记录该属性的有效来源或出版物，`sourceContextId` 指定来源上下文，省略时采用数据集上下文。对子数据集，如果要移除继承的来源引用，应将 `sourceIdOverwrittenByChild` 设为 true；仅让引用消失会按原文规则被解释为保留父值。`sourceYear` 记录出版或交流年份，网站来源记录最后访问；`sourceFirstAuthor` 通常填写第一作者的姓氏和名字缩写，例如 Einstein A.，而来源类型 `sourceType` 为 4、5、6、7 的现场测量、口头交流、个人书面交流或问卷调查，填写提供信息的人。最后，`comment` 可以补充该交换中这项具体属性的假设、说明和限制，使数值能够追溯到其证据。

## 怎样定位、使用与提取

需要干质量、含水率、价格或组成等信息，读取每个交换下的 property，同时保留所属交换实例路径、propertyId、单位和 amount。只有明确属性定义与计量基准后，才能决定是否与交换量相乘；属性不是额外物质流。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange/property`；`flowData/elementaryExchange/property`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TProperty")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/intermediateExchange[1]/property[1]",
  "attributes": {
    "propertyId": "157cb588-bc77-5666-9107-3791e5783446",
    "amount": "1",
    "unitId": "00875264-8155-513e-8182-437026535fcb",
    "isDefiningValue": "true"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "干质量（教学比例）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Dry mass (teaching ratio)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tproperty)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
