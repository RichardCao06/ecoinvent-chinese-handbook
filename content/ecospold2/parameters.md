# 参数

对应官方格式类型：`TParameter`。本篇以文章解释该类型的 12 条字段；复合类型也会说明它们依附在哪个对象上。

## 参数为交换公式提供可追溯的数值 <a href="#read-tparameter" id="read-tparameter"></a>

`TParameter` 保存供公式使用的数据集参数。参数不是物质输入或排放记录，即使也具有 `amount`，也不能混入基本流或中间交换的清单总量。必需的 `name` 是可多语言填写的描述性名称，必需的 `parameterId` 引用有效参数主数据；可选的 `parameterContextId` 指明参数所属上下文，省略时使用数据集上下文。必需的 `amount` 保存参数当前数值，是阅读公式时可用的已保存值，而非参数名称或 UUID。

参数的单位信息均为可选：`unitId` 引用参数数值的单位，`unitContextId` 指明单位上下文，省略时使用数据集上下文，`unitName` 是可多语言填写的单位名称。未提供单位时，不应自动补成质量单位，也不能仅凭字段名认定参数无量纲；应结合参数主数据和用途理解。可选的多语言 `comment` 提供针对该参数的一般说明，可选的 `uncertainty` 描述参数数值的不确定性，读参数值时可将这些解释和质量信息一起保存。

`variableName` 是可选的公式变量名。官方原说明在这一参数字段下沿用了“交换简称”和“交换量”的措辞，这项疑点已记录；从 `TParameter` 的用途看，不能据此认定它只能引用交换。文档列出的规则仍是以字母 a-z 开头，可含字母、数字和下划线，并不区分大小写；`calorific_Value` 与 `Calorific_value` 为相同变量名。另一项已记录差异是，`TVariableName` 的 XSD 限制为最大长度 40，并使用 `\w\S*` 模式，并未直接表达与这些文字规则完全等价的限制。XSD 验证通过，不意味着已经满足公式解析器或语义验证的全部命名要求。

可选的 `mathematicalRelation` 通过变量名或 `REF` 函数引用流、参数和属性的值，在给定变量值后，将结果写入参数自身的 `amount`。可选的 `isCalculatedAmount` 为 `true` 时，说明该数值由该数学关系计算得到；这一参数标记的 XSD 没有声明默认值，不能套用共同交换类型的默认设置。阅读现有文件时应区分直接记录的当前数值与其计算依据，只有在正确理解公式语言和依赖关系后，才重新计算参数。

## 怎样定位、使用与提取

要查看公式输入值，读取 parameter 的 amount、variableName、单位及数学关系。参数可供多个交换使用，并非一笔新增投入；公式作为文本保留，不执行 eval，也不要把参数量归一化为参考产品的额外交换。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/parameter`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TParameter")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/parameter[1]",
  "attributes": {
    "parameterId": "0c72e7c0-a190-5ba6-85ae-0b15236cc19d",
    "amount": "2.5",
    "unitId": "0489b6ee-11b9-577d-b8e0-1e45b6b2fcc1",
    "variableName": "electricity_intensity"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "电力强度（教学）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Electricity intensity (synthetic)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tparameter)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
