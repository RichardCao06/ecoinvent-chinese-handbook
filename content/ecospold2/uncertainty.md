# 不确定性与分布参数

对应官方格式类型：`TUncertainty`。本篇以文章解释该类型的 38 条字段；复合类型也会说明它们依附在哪个对象上。

## 不确定性：先辨认分布，再读取它的参数 <a href="#read-tuncertainty" id="read-tuncertainty"></a>

交换、属性、参数和转移系数可以分别附带 `uncertainty`，中间交换的生产量则使用 `productionVolumeUncertainty`。这些元素采用同一个复合类型 `TUncertainty`，但描述的是各自所属数值的不确定性。读取时，先确定外层对象和它的单位，再进入不确定性结构；不能把这里的概率参数当成另一笔投入、排放或产品数量，加进生命周期清单。`comment` 用来补充这项不确定性的说明，也可能交代数据来源或选用分布的理由。

在这份正常数据集 XSD 中，`TUncertainty` 的 `xsd:choice` 要求从 `lognormal`、`normal`、`triangular`、`uniform`、`beta`、`gamma`、`binomial` 和 `undefined` 中恰好选择一个。原表把各分布行都列为必填，并不表示必须同时填写八种分布：只有被选择的分布，其内部必填属性才适用。选择组之外还可以有 `pedigreeMatrix` 和 `comment`。这也意味着仅有质量评分、却没有任何分布分支的结构，不能据此当作已满足正常模式中的完整 `uncertainty`。

`lognormal` 描述的是自然对数 `ln(x)` 服从正态分布的情况。它的 `meanValue` 是原数值尺度上的几何平均值，`mu` 是底层正态分布，也就是 `ln(x)` 的算术平均值。两者所处的尺度不同，不能把 `mu` 直接当作交换的确定数量。`variance` 是底层正态分布的无偏方差，`varianceWithPedigreeUncertainty` 则是包含基础和谱系不确定性的无偏方差；前者在 XSD 中可省略，后者必填，`meanValue` 和 `mu` 也必填。这里的方差既不是原变量 `x` 的算术方差，也不是标准差。原英文总述把符号 σ 称为方差，而常见统计记号用 σ 表示标准差、σ² 表示方差，这处符号歧义仍待澄清，不能据它自动对字段数值再平方或开方。

`normal` 直接描述数值本身的正态分布，所以它的 `meanValue` 是算术平均值，与 `lognormal/meanValue` 的几何平均值含义不同。`normal/variance` 是无偏方差，`normal/varianceWithPedigreeUncertainty` 是包含基础和谱系不确定性的无偏方差；前者可省略，后者和 `meanValue` 必填。原总述提到的 `MeanValue`、`Deviation` 是说明文字中的名称，当前分支实际存储的属性是 `meanValue`、`variance` 和 `varianceWithPedigreeUncertainty`，并没有 `Deviation` 属性。读方差时必须保留其平方尺度，不能把标准差直接填进 `variance`，也不能仅因它和均值位于同一节点便按相同数值含义解释。

对于 `triangular`，三个参数 `minValue`、`mostLikelyValue` 和 `maxValue` 分别给出最小值、众数和最大值。这里的众数是最可能出现的值，并不等于均值。原文要求使用三角分布时从 `mostLikelyValue` 计算 `meanValue`，又明确禁止在 ecoinvent 上下文使用 `mostLikelyValue` 字段 #3797；而当前 XSD 把字段 2122 的 `mostLikelyValue` 列为必填，并未在该分支声明 `meanValue`。#3797 与当前字段编号不同，这几句话的适用范围不能自行合并或撤销。在来源确认前，不应据此删除当前模式要求的属性，也不应声称单靠众数就能确定三角分布均值。

`uniform` 通过 `minValue` 和 `maxValue` 给出均匀分布区间，两个属性都必填。原文规定，若 `maxValue` 小于 `minValue`，应交换两者的值；这是该分布说明中的明确处理约定，不应外推成所有分布都允许随意重排参数。`beta` 则用 `minValue`、`mostFrequentValue` 和 `maxValue` 表示 a、m、b，分别是下界、最常出现的值和上界。原文给出的条件是 `((a <= m) and (m <= b)) or (a = b)`，形状参数计算式为 `Shape1 = 1 + 4 * ((m-a) / (b-a))` 和 `Shape2 = 6 - Shape1`。这三个属性是输入参数，`Shape1`、`Shape2` 是原文说明中的派生量，并非该分支声明的 XML 属性。源文允许 a=b，却未说明公式分母 b-a 为零时如何处理，不能直接把这个边界代入公式，或在教程中替官方实现编造退化分布算法。

`gamma` 的 `shape` 和 `scale` 分别是形状和尺度参数，`minValue` 是最小值或位置参数，三个属性都必填。原说明规定“这里输入的值将取绝对值使用”，同时规定将最小值参数的值加到所有抽样值上。取绝对值的规则是否也包括位置参数，原文没有明确说明；实现取数或抽样时应核对软件约定，不能自行限定这条规则的适用范围。它们描述分布形状、尺度和平移，并不是三笔交换数量。`binomial` 用整数属性 `n` 表示独立试验次数，用 `p` 表示每次试验的成功概率；两者都必填。读取它时也要先理解概率试验的含义，不能把 `n` 当作产品单位数，或把 `p` 当作市场份额。

`undefined` 是一个明确选择的遗留数据分支，不是省略分布或选择“未指定系统模型”的同义词。它用于保存 EcoSpold01 中分布未定义的旧记录，保留 `minValue`、`maxValue` 和 `standardDeviation95`。前两个属性表示最小值和最大值，后者在原文中仅被描述为从均值向两侧扩展、覆盖总体 95% 所需的值。原文没有交代它究竟是加性半宽、乘性因子还是其他约定，因此读取旧数据时应核查其历史定义，不能一概当成普通算术标准差。

`pedigreeMatrix` 将五项数据质量评价组合在一起。它本身不是一个评分数值，评分位于 `reliability`、`completeness`、`temporalCorrelation`、`geographicalCorrelation` 和 `furtherTechnologyCorrelation` 五个整数属性中。每项取值为 1–5；在正常 XSD 中，选择填写该容器后，五个属性都必须出现。原表把容器一行的类型列为 `integer`，但实际 XSD 使用含属性的复合结构，不能把它当成一个整数叶节点解析。质量评分可依既定方法转换为附加不确定性，再与基础不确定性结合；评分本身不是方差，也不能直接把五个评分相加当作 `varianceWithPedigreeUncertainty`。

`reliability` 关注证据的可靠程度：1 是基于测量且经过验证的数据；2 是部分基于假设但经过验证的数据，或基于测量但未验证的数据；3 是部分依靠有专业依据估算、且未验证的数据；4 是由行业专家等作出的有专业依据估算；5 是无专业依据估算，原说明称其为默认项。这里的默认说明不替代 XSD 对显式属性的要求。`completeness` 关注所考察市场场所和时间跨度：1 覆盖相关全部场所，且跨度足以平滑正常波动；2 覆盖 >50% 的相关场所，且跨度足够；3 覆盖仅部分场所、其比例 <<50%，或覆盖 >50% 但时间跨度较短；4 是仅一个相关场所的代表性数据，或部分场所且时间跨度较短的数据；5 是代表性未知，或仅少数场所且时间跨度较短的数据。

`temporalCorrelation` 将数据年代与数据集时间段字段 600–610 比较：1、2、3、4 分别对应相差不足 3、6、10、15 年，5 对应年代未知或相差超过 15 年。原说明没有明确恰好相差 15 年的归类，不能自行补造边界规则。`geographicalCorrelation` 的 1 是研究区域自身的数据，2 是包含研究区域的更大区域平均数据，3 是生产条件相似区域的数据，4 是生产条件略有相似之处区域的数据，5 是未知区域或明显不同区域的数据，例如用北美代替中东、用 OECD 欧洲代替俄罗斯。`furtherTechnologyCorrelation` 的 1 对应所研究企业、过程和材料，2 对应相同过程与材料及相同技术但不同企业，3 对应同类过程和材料但不同技术，4 对应相关过程或材料，5 对应实验室规模相关过程或不同技术的数据。完整读取这五项，才能理解质量评价的依据，而不能仅凭某一个低分判定整个数据集适用。

## 怎样定位、使用与提取

需要保留分布或开展抽样前，先读取分布子节点名称，再取其参数和 pedigreeMatrix。普通 uncertainty 与 productionVolumeUncertainty 的父节点不同，必须用路径区分；读取平均量不会自动开展抽样，方差也不能直接当标准差使用。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`.//uncertainty`；`.//productionVolumeUncertainty`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TUncertainty")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/intermediateExchange[2]/uncertainty[1]",
  "attributes": {},
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}lognormal",
      "attributes": {
        "meanValue": "25",
        "mu": "3.2188758248682006",
        "variance": "0.01",
        "varianceWithPedigreeUncertainty": "0.04"
      },
      "text": null
    }
  ]
}
```

外层不确定性节点通常没有分布参数属性，参数位于 `children` 中选中的分布节点。谱系矩阵是另一个子节点，应保留它与该分布的关系。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tuncertainty)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
