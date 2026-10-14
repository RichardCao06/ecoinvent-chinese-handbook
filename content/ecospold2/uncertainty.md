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

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学对数正态分布

[下载本段 XML](xml-examples/uncertainty-01.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <lognormal meanValue="25" mu="3.2188758248682006" variance="0.01" varianceWithPedigreeUncertainty="0.04"/>
  <comment xml:lang="zh">教学构造：这里只保存分布参数，不产生交换量或抽样结果。</comment>
</uncertainty>
```

八种分布互斥：这个完整 uncertainty 片段仅选择 lognormal。25 是几何均值，mu 是 ln(x) 的算术均值；0.01 和 0.04 都是底层正态变量的方差，不是标准差。示例数字仅用于解释格式，不是 ecoinvent 数据；外层交换的 amount 需另读。

### 示例 2：教学正态分布

[下载本段 XML](xml-examples/uncertainty-02.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <normal meanValue="10" variance="1" varianceWithPedigreeUncertainty="1.44"/>
</uncertainty>
```

normal 的 meanValue=10 是原变量的算术均值，不是对数正态例子的几何均值；1 和 1.44 分别演示基础方差及含谱系不确定性的方差。读取这些参数不会执行抽样，也不会把均值当成额外一笔交换。

### 示例 3：三角分布的模式语法示例

[下载本段 XML](xml-examples/uncertainty-03.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <triangular minValue="1" mostLikelyValue="2" maxValue="4"/>
  <comment xml:lang="zh">仅演示 XSD 语法；原文关于 ecoinvent 中不得使用旧字段 #3797 的限定仍需另行核对。</comment>
</uncertainty>
```

当前 XSD 要求 triangular 同时填写下界、众数和上界，示例为 1、2、4。原文又要求均值由众数计算，并禁止在 ecoinvent 上下文使用旧字段 #3797；本例只演示当前类型的合法结构，不能据此取消原禁令或确认真实数据库允许任意填写众数。

### 示例 4：教学均匀分布

[下载本段 XML](xml-examples/uncertainty-04.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <uniform minValue="1" maxValue="3"/>
</uncertainty>
```

uniform 在 1 与 3 之间表示均匀分布。原说明称上下界倒置时交换两值；读取器仍应保存原始属性，而不是默默改写文件。这里采用有序边界，不展示未经实现的抽样算法。

### 示例 5：教学 Beta 分布

[下载本段 XML](xml-examples/uncertainty-05.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <beta minValue="0" mostFrequentValue="0.25" maxValue="1"/>
</uncertainty>
```

本例 a=0、m=0.25、b=1，满足 a≤m≤b。原公式 Shape1=1+4*((m-a)/(b-a))、Shape2=6-Shape1 在此给出 2 和 4，XML 本身仍存 a、m、b 而非两个 shape 属性。原文允许 a=b，却会使所列公式分母为零；该特殊情况没有在此示例中擅自定义。

### 示例 6：教学 Gamma 分布

[下载本段 XML](xml-examples/uncertainty-06.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <gamma shape="2" scale="3" minValue="1"/>
</uncertainty>
```

shape=2 和 scale=3 是形状与尺度，minValue=1 是加入样本的位置偏移。原说明要求使用所填值的绝对值；本例全部为正，避免引入负值处理歧义。尺度不是方差，位置偏移也不是交换的 amount；示例不执行抽样。

### 示例 7：教学二项分布

[下载本段 XML](xml-examples/uncertainty-07.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <binomial n="10" p="0.3"/>
</uncertainty>
```

binomial 的 n=10 表示独立试验次数，p=0.3 表示每次成功概率。它们是分布参数，不是 10 单位产品或 0.3 单位投入；需要抽样时仍须使用适当的概率模型。

### 示例 8：旧式未定义分布的教学存储示例

[下载本段 XML](xml-examples/uncertainty-08.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <undefined minValue="8" maxValue="12" standardDeviation95="2"/>
</uncertainty>
```

undefined 用于保存旧 EcoSpold01 数据而不指定一个现代分布族。8、12、2 仅展示旧字段的存储位置；standardDeviation95 的名称不能使 2 自动等同于正态标准差，也不能由这些值擅自重建分布。

### 示例 9：分布之后的五项谱系编码

[下载本段 XML](xml-examples/uncertainty-09.xml)。

```xml
<uncertainty xmlns="http://www.EcoInvent.org/EcoSpold02">
  <normal meanValue="10" variance="1" varianceWithPedigreeUncertainty="1.44"/>
  <pedigreeMatrix reliability="1" completeness="2" temporalCorrelation="1" geographicalCorrelation="2" furtherTechnologyCorrelation="2"/>
  <comment xml:lang="zh">谱系代码均为教学选择，不表示这些教学数据实际经过测量或审查。</comment>
</uncertainty>
```

pedigreeMatrix 放在唯一分布节点之后、comment 之前，是包含五个 1–5 整数评分的容器，不是一个整数值。代码只演示原规范中的类别；不能把五个评分相加当作方差，也不能据这个构造片段认定数据已被验证。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`comment`（FieldID 2010）**：对数正态例子的 `uncertainty/comment` 给出“这里只保存分布参数”的普通文本。按子元素读其文本并保留 `xml:lang`；它解释参数，不参与求和，也不是 `TTextAndImage`。

**`lognormal`（FieldID 2100）**：对数正态例子选择子元素 `lognormal`，其属性描述 ln(x) 的正态分布。先识别这个分布名再解释属性，同一个 `uncertainty` 不能同时塞入 `normal` 等第二种分布。

**`lognormal/@meanValue`（FieldID 2101）**：从 `lognormal/@meanValue` 读取 `25`，意思是原变量的几何均值。它不具有正态例子 `meanValue` 的算术均值含义，也不能代替外层交换数量。

**`lognormal/@mu`（FieldID 2102）**：从 `lognormal/@mu` 读取 `3.2188758248682006`，这是底层 ln(x) 正态变量的算术均值，示例约为 ln(25)。不能将这个对数参数当作原变量的平均数量。

**`lognormal/@variance`（FieldID 2103）**：`lognormal/@variance="0.01"` 保存底层正态变量的基础无偏方差。读取该字符串后应按方差参数解释，而非当成标准差或额外的 0.01 单位排放。

**`lognormal/@varianceWithPedigreeUncertainty`（FieldID 2104）**：`lognormal/@varianceWithPedigreeUncertainty="0.04"` 是包含基础和谱系不确定性的底层正态方差。它已经是合并后的参数，不能再无依据地加一次基础方差。

**`normal`（FieldID 2110）**：正态例子使用 `normal` 子元素而不包含其他分布。它描述原变量的正态分布；根据分布名选择参数化方式，不套用对数正态的 ln(x) 解释。

**`normal/@meanValue`（FieldID 2111）**：`normal/@meanValue="10"` 是原变量的算术均值。读取时与外层交换 `amount` 分别保存；是否一致需看数据定义，不能靠同名字段自动覆盖。

**`normal/@variance`（FieldID 2112）**：`normal/@variance="1"` 是基础无偏方差。若工具需要标准差，应明确采用方差到标准差的转换，不能把字符串 `1` 的字段类型改称标准差。

**`normal/@varianceWithPedigreeUncertainty`（FieldID 2113）**：`normal/@varianceWithPedigreeUncertainty="1.44"` 是含谱系不确定性的方差。此值与基础方差各有角色，读取时分别保留，不能仅取较大值而丢掉字段身份。

**`triangular`（FieldID 2120）**：三角例子包含 `triangular`，其完整语法为下界、众数、上界三个属性。原说明关于旧 #3797 的禁用与均值计算限定仍需遵守；这个类型校验示例不是解除限制的依据。

**`triangular/@minValue`（FieldID 2121）**：`triangular/@minValue="1"` 是该三角分布的最小值。应与同一个 `triangular` 内的众数和上界共同读取，不能与其他分布的下界拼成参数组。

**`triangular/@mostLikelyValue`（FieldID 2122）**：`triangular/@mostLikelyValue="2"` 是众数，非算术均值。当前 XSD 要求此属性，但原文禁止使用旧字段 #3797；保存语法示例值不等于确认其真实 ecoinvent 建模用法。

**`triangular/@maxValue`（FieldID 2123）**：`triangular/@maxValue="4"` 是该分布上界。取数时保留下界 1、众数 2、上界 4 的对应关系，不把最大可能值当作当前交换的确定数量。

**`uniform`（FieldID 2130）**：均匀例子以 `uniform` 子元素表达区间内的均匀分布。原说明提及倒置边界交换规则，示例未执行这一步；解析和后续分布构造应分开。

**`uniform/@minValue`（FieldID 2131）**：`uniform/@minValue="1"` 是本例下界。先按原始属性保存，再结合上界判断区间；不要因字段也叫 minValue 就混入三角或 Gamma 参数。

**`uniform/@maxValue`（FieldID 2132）**：`uniform/@maxValue="3"` 是本例上界，与同节点下界 1 配对。两值不是两笔交换，不能求和得到投入量。

**`beta`（FieldID 2140）**：Beta 例子使用 `beta`，存 a、m、b 三个量。0≤0.25≤1 满足原文条件；原公式的 a=b 分母问题仍留痕，不能把该 XML 片段当作处理退化分布的算法。

**`beta/@minValue`（FieldID 2141）**：`beta/@minValue="0"` 对应原公式中的 a。读取到零是合法示例值，不是属性缺失，必须与当前 Beta 节点的 m、b 一起保留。

**`beta/@mostFrequentValue`（FieldID 2142）**：`beta/@mostFrequentValue="0.25"` 对应 m，即最频繁值。它与三角分布的 mostLikelyValue 名称不同，应使用准确的 XML 属性名而非互相替换。

**`beta/@maxValue`（FieldID 2143）**：`beta/@maxValue="1"` 对应 b。该值限制分布区间，并参与原文形状参数公式的 b-a 分母；不是成功概率 p，也不是标准差。

**`gamma`（FieldID 2150）**：Gamma 例子使用 `gamma`，形状 2、尺度 3、位置偏移 1 都是正数。原文绝对值规则仍适用；这个片段保存参数而不实现随机数生成。

**`gamma/@shape`（FieldID 2151）**：`gamma/@shape="2"` 是形状参数。按 Gamma 参数保存，不能当成正态分布的方差或试验次数。

**`gamma/@scale`（FieldID 2152）**：`gamma/@scale="3"` 是尺度参数。工具若使用 rate 参数，须明确查其参数化约定，不能将 scale 原样塞到一个 rate 字段中。

**`gamma/@minValue`（FieldID 2153）**：`gamma/@minValue="1"` 是位置参数，原说明要求将其加至样本。它不同于均匀分布的区间下界角色；读取器本身不因此增加外层交换量。

**`binomial`（FieldID 2160）**：二项例子选择 `binomial` 子元素，其参数是 n 和 p。先识别二项分布再处理独立试验与成功概率，不把它当成连续数量区间。

**`binomial/@n`（FieldID 2161）**：`binomial/@n="10"` 是整数的独立试验次数。应按整数读取并结合概率解释，不以产品单位赋给它。

**`binomial/@p`（FieldID 2162）**：`binomial/@p="0.3"` 是每次试验成功概率，示例位于 0 与 1 之间。它不是百分数 30 的存储方式，也不是属性量或交换份额。

**`undefined`（FieldID 2170）**：旧数据例子选择 `undefined` 而不宣称正态、均匀等分布。读取器只保留三个旧字段，不能在没有额外依据时把它重新贴上某个分布标签。

**`undefined/@minValue`（FieldID 2171）**：`undefined/@minValue="8"` 保存旧数据的最小值。应连同原节点类型保留，避免仅按字段名与其他分布参数合并。

**`undefined/@maxValue`（FieldID 2172）**：`undefined/@maxValue="12"` 保存旧数据最大值。上下界可以作为旧信息被导出，但不足以唯一决定概率分布。

**`undefined/@standardDeviation95`（FieldID 2173）**：`undefined/@standardDeviation95="2"` 对应原说明中从均值两侧扩展、覆盖 95% 总体所需的值。旧式定义不能直接等同于常规正态标准差，也不擅自给出换算公式。

**`pedigreeMatrix`（FieldID 2270）**：谱系例子的 `pedigreeMatrix` 位于 `normal` 之后，它自身没有文本数值，而以五个属性保存评分。应保持它与这一分布的父子关系，不把容器当作另一种互斥分布。

**`pedigreeMatrix/@reliability`（FieldID 2271）**：`pedigreeMatrix/@reliability="1"` 的编码含义是基于测量且已验证的数据；这里只演示类别，不宣称教学数据真的达到该质量。把评分 1 与所对应字段一起保存。

**`pedigreeMatrix/@completeness`（FieldID 2272）**：`pedigreeMatrix/@completeness="2"` 表示在足以平衡正常波动的期间，具有所考虑市场超过 50% 相关场所的代表性数据。这个等级不是采样百分比 2%，也不是方差 2。

**`pedigreeMatrix/@temporalCorrelation`（FieldID 2273）**：`pedigreeMatrix/@temporalCorrelation="1"` 对应与数据集有效期间差异小于 3 年。不能把评分解释为数据年份；原文对恰好 15 年的边界未说明，示例避开该歧义。

**`pedigreeMatrix/@geographicalCorrelation`（FieldID 2274）**：`pedigreeMatrix/@geographicalCorrelation="2"` 对应包含研究区域的更大区域平均数据。该等级需结合研究区域解释，不是可与 geographyId 相互替换的地点 ID。

**`pedigreeMatrix/@furtherTechnologyCorrelation`（FieldID 2275）**：`pedigreeMatrix/@furtherTechnologyCorrelation="2"` 表示相同过程与材料、相同技术，但来自不同企业。保存这个类别，不自行把五项等级平均后称作附加方差。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/uncertainty-01.xml").getroot()
FIELDS = {
    "2010": "comment",
    "2100": "lognormal",
    "2101": "lognormal/@meanValue",
    "2102": "lognormal/@mu",
    "2103": "lognormal/@variance",
    "2104": "lognormal/@varianceWithPedigreeUncertainty",
    "2110": "normal",
    "2111": "normal/@meanValue",
    "2112": "normal/@variance",
    "2113": "normal/@varianceWithPedigreeUncertainty",
    "2120": "triangular",
    "2121": "triangular/@minValue",
    "2122": "triangular/@mostLikelyValue",
    "2123": "triangular/@maxValue",
    "2130": "uniform",
    "2131": "uniform/@minValue",
    "2132": "uniform/@maxValue",
    "2140": "beta",
    "2141": "beta/@minValue",
    "2142": "beta/@mostFrequentValue",
    "2143": "beta/@maxValue",
    "2150": "gamma",
    "2151": "gamma/@shape",
    "2152": "gamma/@scale",
    "2153": "gamma/@minValue",
    "2160": "binomial",
    "2161": "binomial/@n",
    "2162": "binomial/@p",
    "2170": "undefined",
    "2171": "undefined/@minValue",
    "2172": "undefined/@maxValue",
    "2173": "undefined/@standardDeviation95",
    "2270": "pedigreeMatrix",
    "2271": "pedigreeMatrix/@reliability",
    "2272": "pedigreeMatrix/@completeness",
    "2273": "pedigreeMatrix/@temporalCorrelation",
    "2274": "pedigreeMatrix/@geographicalCorrelation",
    "2275": "pedigreeMatrix/@furtherTechnologyCorrelation",
}
for field_id, relative_path in FIELDS.items():
    values = field_values(node, relative_path)
    print(field_id, relative_path, json.dumps(values, ensure_ascii=False))
```

换成完整 `.spold` 文件时，先使用本章定位路径选出目标节点，再把它作为 `node` 传入。例如属性 `@amount` 最终用 `.get("amount")` 读取；子元素 `unitName` 用带命名空间的 `.findall("es:unitName", ns)` 读取。嵌套路径先进入对应子元素，再取最后的属性；如 `lognormal/@variance`，不能在外层 `uncertainty` 上直接取 `variance`。复合类型的子元素不能只读外层 `.text`，其结构已保留在返回记录的 `xml` 中。

### 直接在完整 spold 中使用这些路径

沿用上一段的 `FIELDS` 字典与 `field_values`，下面改从完整文件选取本类型节点。先用配套 demo 运行，再把文件名改为自己的 `.spold`。XML 查找会返回全部同类节点；可选结构未提供时，匹配数为零，不会被填成数值零。多个路径代表同类型的不同使用位置，统计时按父路径区分。

```python
from read_section import load_dataset, NS

dataset = load_dataset("demo-product.spold", index=0)
LOCATIONS = ['.//es:uncertainty', './/es:productionVolumeUncertainty']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


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
