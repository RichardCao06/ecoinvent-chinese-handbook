# 不确定性与分布参数（TUncertainty）

源文分组：TUncertainty。本章完整收录 **38 条字段定义**。

XML 位置：`…/uncertainty`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% hint style="warning" %}
本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：否。

必须从以下不确定性方法（对数正态、正态、……、未定义分布）中恰好选择一种。TUncertainty 复杂类型用于多个位置，因此，一个数据集可在不同位置包含多个 uncertainty 元素。但每个具有不确定性信息的元素只能包含一个 uncertainty 元素。

**XSD 阅读提示：** 每个 `uncertainty` 元素在 `lognormal`、`normal`、`triangular`、`uniform`、`beta`、`gamma`、`binomial`、`undefined` 中恰选一种分布。以下属性所属的分布由“局部 XML 位置”区分；`pedigreeMatrix` 是独立的可选元素。

### `comment` · FieldID 2010 <a href="#field-2010" id="field-2010"></a>

局部 XML 位置：`TUncertainty/comment`；ecoSpold1 对照编号：`3792`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString32000` | 否 | 否 |

长度：32000；多语言：是；主数据冗余字段：否。

可对每项不确定性信息填写一般说明。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `lognormal` · FieldID 2100 <a href="#field-2100" id="field-2100"></a>

局部 XML 位置：`TUncertainty/lognormal`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

具有平均值 μ（Mu 参数）和方差 σ（Variance 参数）的对数正态分布，是对特征值的自然对数 ln(x) 而非 x 值进行描述的正态分布。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@meanValue` · FieldID 2101 <a href="#field-2101" id="field-2101"></a>

局部 XML 位置：`TUncertainty/lognormal/@meanValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

几何平均值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@mu` · FieldID 2102 <a href="#field-2102" id="field-2102"></a>

局部 XML 位置：`TUncertainty/lognormal/@mu`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

底层正态分布的算术平均值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@variance` · FieldID 2103 <a href="#field-2103" id="field-2103"></a>

局部 XML 位置：`TUncertainty/lognormal/@variance`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

底层正态分布的无偏方差。

**XSD 结构约束：** `use="optional"`（XSD 默认值）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@varianceWithPedigreeUncertainty` · FieldID 2104 <a href="#field-2104" id="field-2104"></a>

局部 XML 位置：`TUncertainty/lognormal/@varianceWithPedigreeUncertainty`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

底层正态分布的无偏方差，包括基础不确定性和谱系不确定性。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `normal` · FieldID 2110 <a href="#field-2110" id="field-2110"></a>

局部 XML 位置：`TUncertainty/normal`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

正态分布，也称“高斯”分布。它是一族具有相同一般形式的分布，其位置参数和尺度参数不同，分别为均值（MeanValue）和标准差（Deviation）。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@meanValue` · FieldID 2111 <a href="#field-2111" id="field-2111"></a>

局部 XML 位置：`TUncertainty/normal/@meanValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

算术平均值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@variance` · FieldID 2112 <a href="#field-2112" id="field-2112"></a>

局部 XML 位置：`TUncertainty/normal/@variance`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

无偏方差。

**XSD 结构约束：** `use="optional"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@varianceWithPedigreeUncertainty` · FieldID 2113 <a href="#field-2113" id="field-2113"></a>

局部 XML 位置：`TUncertainty/normal/@varianceWithPedigreeUncertainty`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

无偏方差，包括基础不确定性和谱系不确定性。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `triangular` · FieldID 2120 <a href="#field-2120" id="field-2120"></a>

局部 XML 位置：`TUncertainty/triangular`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

参数为 minValue、mostLikelyValue 和 maxValue。

采用三角不确定性分布时，应根据 mostLikelyValue 计算 meanValue。在 ecoinvent 上下文中，不得使用 mostLikelyValue 字段（#3797）。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2121 <a href="#field-2121" id="field-2121"></a>

局部 XML 位置：`TUncertainty/triangular/@minValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最小值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@mostLikelyValue` · FieldID 2122 <a href="#field-2122" id="field-2122"></a>

局部 XML 位置：`TUncertainty/triangular/@mostLikelyValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

众数。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2123 <a href="#field-2123" id="field-2123"></a>

局部 XML 位置：`TUncertainty/triangular/@maxValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最大值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `uniform` · FieldID 2130 <a href="#field-2130" id="field-2130"></a>

局部 XML 位置：`TUncertainty/uniform`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

minValue 与 maxValue 参数之间的均匀分布。如果 maxValue 参数小于 minValue 参数，则交换两者的值。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2131 <a href="#field-2131" id="field-2131"></a>

局部 XML 位置：`TUncertainty/uniform/@minValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最小值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2132 <a href="#field-2132" id="field-2132"></a>

局部 XML 位置：`TUncertainty/uniform/@maxValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最大值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `beta` · FieldID 2140 <a href="#field-2140" id="field-2140"></a>

局部 XML 位置：`TUncertainty/beta`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

Beta 分布使用 minValue（a）、maxValue（b）和 mostFrequentValue（m）参数，计算底层 Gamma 分布的两个形状参数。参数必须满足条件：((a &lt;= m) and (m &lt;= b)) or (a = b)。形状参数按以下公式计算：Shape1 = 1 + 4 \* ((m-a) / (b-a))。Shape2 = 6 - Shape1。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2141 <a href="#field-2141" id="field-2141"></a>

局部 XML 位置：`TUncertainty/beta/@minValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最小值（a）。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@mostFrequentValue` · FieldID 2142 <a href="#field-2142" id="field-2142"></a>

局部 XML 位置：`TUncertainty/beta/@mostFrequentValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最常出现的值（m）。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2143 <a href="#field-2143" id="field-2143"></a>

局部 XML 位置：`TUncertainty/beta/@maxValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最大值（b）。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `gamma` · FieldID 2150 <a href="#field-2150" id="field-2150"></a>

局部 XML 位置：`TUncertainty/gamma`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

Gamma 分布使用尺度参数和形状参数。这里输入的值将取绝对值使用。minimum 参数的值将加到所有抽样值上。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@shape` · FieldID 2151 <a href="#field-2151" id="field-2151"></a>

局部 XML 位置：`TUncertainty/gamma/@shape`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

形状参数。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@scale` · FieldID 2152 <a href="#field-2152" id="field-2152"></a>

局部 XML 位置：`TUncertainty/gamma/@scale`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

尺度参数。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2153 <a href="#field-2153" id="field-2153"></a>

局部 XML 位置：`TUncertainty/gamma/@minValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最小值（位置参数）。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `binomial` · FieldID 2160 <a href="#field-2160" id="field-2160"></a>

局部 XML 位置：`TUncertainty/binomial`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

二项分布使用 n 和 p 参数。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@n` · FieldID 2161 <a href="#field-2161" id="field-2161"></a>

局部 XML 位置：`TUncertainty/binomial/@n`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

独立试验次数。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@p` · FieldID 2162 <a href="#field-2162" id="field-2162"></a>

局部 XML 位置：`TUncertainty/binomial/@p`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

每次试验的成功概率。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `undefined` · FieldID 2170 <a href="#field-2170" id="field-2170"></a>

局部 XML 位置：`TUncertainty/undefined`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| — | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

此“分布”可用于保存 EcoSpold01 格式的旧数据；该格式复用 minValue、maxValue 和 standardDeviation95 字段，存储未定义分布的数据。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2171 <a href="#field-2171" id="field-2171"></a>

局部 XML 位置：`TUncertainty/undefined/@minValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最小值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2172 <a href="#field-2172" id="field-2172"></a>

局部 XML 位置：`TUncertainty/undefined/@maxValue`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

最大值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@standardDeviation95` · FieldID 2173 <a href="#field-2173" id="field-2173"></a>

局部 XML 位置：`TUncertainty/undefined/@standardDeviation95`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TFloatNumber` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

从均值向两侧延伸、为覆盖总体 95% 所需的值。

**XSD 结构约束：** `use="required"`。该字段位于 `xsd:choice` 分支内；出现条件须结合父级结构判断。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `pedigreeMatrix` · FieldID 2270 <a href="#field-2270" id="field-2270"></a>

局部 XML 位置：`TUncertainty/pedigreeMatrix`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

数据质量指标提供数据质量的定性评价。该评价可转换为定量的附加不确定性，并加到基础不确定性上。pedigreeMatrix 元素将 5 个数据质量指标分组，其自身不包含数据。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@reliability` · FieldID 2271 <a href="#field-2271" id="field-2271"></a>

局部 XML 位置：`TUncertainty/pedigreeMatrix/@reliability`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

1=基于测量且经过验证的数据。

2=部分基于假设且经过验证的数据，或基于测量但未经过验证的数据。

3=部分基于有专业依据的估算、但未经过验证的数据。

4=有专业依据的估算，例如由行业专家作出的估算。

5=无专业依据的估算（默认）。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@completeness` · FieldID 2272 <a href="#field-2272" id="field-2272"></a>

局部 XML 位置：`TUncertainty/pedigreeMatrix/@completeness`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

1=来自所考察市场相关全部场所的代表性数据，时间跨度足以平滑正常波动。

2=来自所考察市场相关场所中 &gt;50% 的代表性数据，时间跨度足以平滑正常波动。

3=仅来自所考察市场相关部分场所（&lt;&lt;50%）的代表性数据，或来自 &gt;50% 的场所但时间跨度较短的数据。

4=仅来自所考察市场相关一个场所的代表性数据，或来自部分场所但时间跨度较短的数据。

5=代表性未知，或来自少数场所且时间跨度较短的数据。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@temporalCorrelation` · FieldID 2273 <a href="#field-2273" id="field-2273"></a>

局部 XML 位置：`TUncertainty/pedigreeMatrix/@temporalCorrelation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

1=与数据集的时间期间（字段 600-610）相差不足 3 年。

2=与数据集的时间期间（字段 600-610）相差不足 6 年。

3=与数据集的时间期间（字段 600-610）相差不足 10 年。

4=与数据集的时间期间（字段 600-610）相差不足 15 年。

5=数据年代未知，或与数据集的时间期间（字段 600-610）相差超过 15 年。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@geographicalCorrelation` · FieldID 2274 <a href="#field-2274" id="field-2274"></a>

局部 XML 位置：`TUncertainty/pedigreeMatrix/@geographicalCorrelation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

1=来自研究区域的数据。

2=来自包含研究区域的更大区域的平均数据。

3=来自生产条件相似区域的数据。

4=来自生产条件略有相似之处的区域的数据。

5=来自未知区域或明显不同区域的数据，例如以北美代替中东、以 OECD 欧洲代替俄罗斯。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@furtherTechnologyCorrelation` · FieldID 2275 <a href="#field-2275" id="field-2275"></a>

局部 XML 位置：`TUncertainty/pedigreeMatrix/@furtherTechnologyCorrelation`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

1=来自所研究企业、过程和材料的数据。

2=来自所研究过程和材料（即相同技术），但企业不同的数据。

3=来自所研究过程和材料，但技术不同的数据。

4=有关相关过程或材料的数据。

5=有关实验室规模相关过程的数据，或来自不同技术的数据。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：No。

Of the following uncertainty methods (lognormal, normal, ..., undefined) exactly one must be selected. The TUncertainty complex type is used in several places, so one dataset may contain several uncertainty elements in distinct places. But each element which has uncertainty may only contain one.

**XSD reading note:** Each uncertainty element selects exactly one of lognormal, normal, triangular, uniform, beta, gamma, binomial, or undefined. Local XML paths distinguish distribution-specific attributes; pedigreeMatrix is a separate optional element.

### `comment` · FieldID 2010 <a href="#en-field-2010" id="en-field-2010"></a>

Local XML path：`TUncertainty/comment`；ecoSpold1 mapping：`3792`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString32000` | No | No |

Size：32000；Multi language：Yes；Redundant master data：No。

A general comment can be made about each uncertainty information

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `lognormal` · FieldID 2100 <a href="#en-field-2100" id="en-field-2100"></a>

Local XML path：`TUncertainty/lognormal`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The Lognormal-distribution with average value μ (Mu parameter) and variance σ (Variance parameter) is a Normal-distribution, shaping the natural logarithm of the characteristic values ln(x) instead of x-values.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@meanValue` · FieldID 2101 <a href="#en-field-2101" id="en-field-2101"></a>

Local XML path：`TUncertainty/lognormal/@meanValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Geometric mean

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@mu` · FieldID 2102 <a href="#en-field-2102" id="en-field-2102"></a>

Local XML path：`TUncertainty/lognormal/@mu`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Arithmetic mean of the underlying normal distribution

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@variance` · FieldID 2103 <a href="#en-field-2103" id="en-field-2103"></a>

Local XML path：`TUncertainty/lognormal/@variance`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Unbiased variance of the underlying normal distribution

**XSD structural constraints：** `use="optional"` (XSD default). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@varianceWithPedigreeUncertainty` · FieldID 2104 <a href="#en-field-2104" id="en-field-2104"></a>

Local XML path：`TUncertainty/lognormal/@varianceWithPedigreeUncertainty`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Unbiased variance of the underlying normal distribution, basic uncertainty with pedigree uncertainty

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `normal` · FieldID 2110 <a href="#en-field-2110" id="en-field-2110"></a>

Local XML path：`TUncertainty/normal`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Normal (also known as "Gaussian") distribution. It is a family of distributions of the same general form, differing in their location and scale parameters: the mean ("MeanValue") and standard deviation ("Deviation"), respectively.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@meanValue` · FieldID 2111 <a href="#en-field-2111" id="en-field-2111"></a>

Local XML path：`TUncertainty/normal/@meanValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Arithemtic mean

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@variance` · FieldID 2112 <a href="#en-field-2112" id="en-field-2112"></a>

Local XML path：`TUncertainty/normal/@variance`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Unbiased variance

**XSD structural constraints：** `use="optional"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@varianceWithPedigreeUncertainty` · FieldID 2113 <a href="#en-field-2113" id="en-field-2113"></a>

Local XML path：`TUncertainty/normal/@varianceWithPedigreeUncertainty`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Unbiased variance, basic uncertainty with pedigree uncertainty

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `triangular` · FieldID 2120 <a href="#en-field-2120" id="en-field-2120"></a>

Local XML path：`TUncertainty/triangular`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Parameter are minValue, mostLikelyValue, maxValue.

In case of triangular uncertainty distribution, the meanValue shall be calculated from the mostLikelyValue. The field mostLikelyValue (#3797) must not be used in the ecoinvent context.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2121 <a href="#en-field-2121" id="en-field-2121"></a>

Local XML path：`TUncertainty/triangular/@minValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Minimum value

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@mostLikelyValue` · FieldID 2122 <a href="#en-field-2122" id="en-field-2122"></a>

Local XML path：`TUncertainty/triangular/@mostLikelyValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Mode

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2123 <a href="#en-field-2123" id="en-field-2123"></a>

Local XML path：`TUncertainty/triangular/@maxValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Maximum value

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `uniform` · FieldID 2130 <a href="#en-field-2130" id="en-field-2130"></a>

Local XML path：`TUncertainty/uniform`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Uniform distribution of values between the minValue and the maxValue parameter. If the maxValue parameter is smaller than the minValue parameter their values will be swapped.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2131 <a href="#en-field-2131" id="en-field-2131"></a>

Local XML path：`TUncertainty/uniform/@minValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Minimum value

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2132 <a href="#en-field-2132" id="en-field-2132"></a>

Local XML path：`TUncertainty/uniform/@maxValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Maximum value

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `beta` · FieldID 2140 <a href="#en-field-2140" id="en-field-2140"></a>

Local XML path：`TUncertainty/beta`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Beta distribution using minValue (a), maxValue (b) and mostFrequentValue (m) parameters to calculate the two shape parameters of the underlying Gamma distributions. The parameters must follow this condition: ((a &lt;= m) and (m &lt;= b)) or (a = b). The shape values will be calculated by these formulas: Shape1 = 1 + 4 \* ((m-a) / (b-a)). Shape2 = 6 - Shape1.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2141 <a href="#en-field-2141" id="en-field-2141"></a>

Local XML path：`TUncertainty/beta/@minValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Minimum value (a)

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@mostFrequentValue` · FieldID 2142 <a href="#en-field-2142" id="en-field-2142"></a>

Local XML path：`TUncertainty/beta/@mostFrequentValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Most Frequent value (m)

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2143 <a href="#en-field-2143" id="en-field-2143"></a>

Local XML path：`TUncertainty/beta/@maxValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Maximum value (b)

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `gamma` · FieldID 2150 <a href="#en-field-2150" id="en-field-2150"></a>

Local XML path：`TUncertainty/gamma`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Gamma distribution using scale and shape parameter. Absolute values of the values entered here will be used. The value of the minimum parameter will be added to all samples.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@shape` · FieldID 2151 <a href="#en-field-2151" id="en-field-2151"></a>

Local XML path：`TUncertainty/gamma/@shape`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Shape parameter

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@scale` · FieldID 2152 <a href="#en-field-2152" id="en-field-2152"></a>

Local XML path：`TUncertainty/gamma/@scale`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Scale parameter

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2153 <a href="#en-field-2153" id="en-field-2153"></a>

Local XML path：`TUncertainty/gamma/@minValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Minimum value (location parameter)

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `binomial` · FieldID 2160 <a href="#en-field-2160" id="en-field-2160"></a>

Local XML path：`TUncertainty/binomial`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Binomial distribution using n and p parameter.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@n` · FieldID 2161 <a href="#en-field-2161" id="en-field-2161"></a>

Local XML path：`TUncertainty/binomial/@n`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Number of independant trials

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@p` · FieldID 2162 <a href="#en-field-2162" id="en-field-2162"></a>

Local XML path：`TUncertainty/binomial/@p`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Probability of success in each trial

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `undefined` · FieldID 2170 <a href="#en-field-2170" id="en-field-2170"></a>

Local XML path：`TUncertainty/undefined`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| — | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

This "distribution" can be used to hold legacy data of the EcoSpold01 format which reused the minValue, maxValue and standardDeviation95 fields to store undefined distribution data.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="1"` (undeclared values use XSD defaults). This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@minValue` · FieldID 2171 <a href="#en-field-2171" id="en-field-2171"></a>

Local XML path：`TUncertainty/undefined/@minValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Minimum value

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@maxValue` · FieldID 2172 <a href="#en-field-2172" id="en-field-2172"></a>

Local XML path：`TUncertainty/undefined/@maxValue`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Maximum value

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@standardDeviation95` · FieldID 2173 <a href="#en-field-2173" id="en-field-2173"></a>

Local XML path：`TUncertainty/undefined/@standardDeviation95`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TFloatNumber` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The value, extended from both sides of the mean, that would be necessary to cover 95% of the population

**XSD structural constraints：** `use="required"`. This field is within an xsd:choice branch; interpret occurrence in its parent structure。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `pedigreeMatrix` · FieldID 2270 <a href="#en-field-2270" id="en-field-2270"></a>

Local XML path：`TUncertainty/pedigreeMatrix`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | No | No |

Size：—；Multi language：No；Redundant master data：No。

The data quality indicators provides a qualitative assessment of data quality. This can be converted to a quantitative additional uncertainty, which can be added to the basic uncertainty. The pedigreeMatrix element groups the 5 data quality indicators and contains no data itself.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@reliability` · FieldID 2271 <a href="#en-field-2271" id="en-field-2271"></a>

Local XML path：`TUncertainty/pedigreeMatrix/@reliability`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

1=Verified data based on measurements

2=Verified data partly based on assumptions OR nonverified data based on measurements

3=Non-verified data partly based on qualified estimates

4=Qualified estimate (e.g. by industrial expert)

5=Non-qualified estimate (default)

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@completeness` · FieldID 2272 <a href="#en-field-2272" id="en-field-2272"></a>

Local XML path：`TUncertainty/pedigreeMatrix/@completeness`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

1=Representative data from all sites relevant for the market considered over an adequate period to even out normal fluctuations

2=Representative data from &gt;50% of the sites relevant for the market considered over an adequate period to even out normal fluctuations

3=Representative data from only some sites (&lt;&lt;50%) relevant for the market considered OR &gt;50% of sites but from shorter periods

4=Representative data from only one site relevant for the market considered OR some sites but from shorter periods

5=Representativeness unknown or data from a small number of sites AND from shorter periods

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@temporalCorrelation` · FieldID 2273 <a href="#en-field-2273" id="en-field-2273"></a>

Local XML path：`TUncertainty/pedigreeMatrix/@temporalCorrelation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

1=Less than 3 years of difference to the time period of the dataset (fields 600-610)

2=Less than 6 years of difference to the time period of the dataset (fields 600-610)

3=Less than 10 years of difference to the time period of the dataset (fields 600-610)

4=Less than 15 years of difference to the time period of the dataset (fields 600-610)

5=Age of data unknown or more than 15 years of difference to the time period of the dataset (fields 600-610)

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@geographicalCorrelation` · FieldID 2274 <a href="#en-field-2274" id="en-field-2274"></a>

Local XML path：`TUncertainty/pedigreeMatrix/@geographicalCorrelation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

1=Data from area under study

2=Average data from larger area in which the area under study is included

3=Data from area with similar production conditions

4=Data from are with slightly similar production conditions

5=Data from unknown OR distinctly different area (north america instead of middle east, OECD-Europe instead of Russia)

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

### `@furtherTechnologyCorrelation` · FieldID 2275 <a href="#en-field-2275" id="en-field-2275"></a>

Local XML path：`TUncertainty/pedigreeMatrix/@furtherTechnologyCorrelation`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

1=Data from enterprises, processes and materials under study

2=Data from processes and materials under study  (i.e. identical technology) but from different enterprises

3=Data from processes and materials under study but from different technology

4=Data on related processes or materials

5=Data on related processes on laboratory scale or from different technology

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02DataTypes.xsd](original/Schemas/datasets/EcoSpold02DataTypes.xsd)，`TUncertainty`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **待专家复核 · `TUncertainty.2100.description.0`**：原文将 σ 称为 variance（方差），而常见对数正态分布记号以 σ 为底层正态分布标准差、σ²为方差；同组字段则明确为 variance。译文忠实保留原符号及“方差”，不能据此自动将参数平方或开方。 以对应 XSD 字段定义及读取软件实际实现确认 Mu/Variance 参数的尺度；请技术编辑澄清原文 σ 的定义。

- **待专家复核 · `TUncertainty.2120.description.1`**：原文要求从 mostLikelyValue 计算 meanValue，同时禁止在 ecoinvent 上下文使用 mostLikelyValue（#3797）。官方 EcoSpold02DataTypes.xsd 的 triangular 类型却将当前 @mostLikelyValue（fieldId=2122）设为 required；#3797 与当前编号不同，禁令适用对象及与模式必填要求的关系尚不清楚。三角分布均值也不能仅由众数单独确定。正文保留 shall/must not 及 #3797，不擅自撤销禁令。 请向数据方确认 #3797 是否仅指旧格式字段、当前 @mostLikelyValue 的提交规则及 meanValue 的具体含义；勿将众数直接当作三角分布均值。证据：Schemas/datasets/EcoSpold02DataTypes.xsd 的 triangular 定义。

- **待专家复核 · `TUncertainty.2140.description.0`**：原文允许退化条件 a=b，但所列 Shape1 公式含分母 b-a，此条件下会出现除零；原文未说明退化分布如何处理。译文完整保留条件和公式。 核实实现是否对 a=b 单独生成常数样本，或是否应要求 a<b；确认前不要直接按常规形状公式计算该边界情况。

- **待专家复核 · `TUncertainty.2173.description.0`**：原文仅将旧格式 standardDeviation95 描述为从均值两侧扩展、覆盖总体95%所需的值，未说明它是加性半宽度、乘性因子或其他量，不能一概理解成普通标准差。译文不额外指定计算形式。 读取 EcoSpold01 遗留数据时核对具体旧分布及字段约定，勿无条件将该值作为算术标准差。

- **待专家复核 · `TUncertainty.2110.description.0`**：原文将正态分布参数称为 MeanValue 和 Deviation，但官方 XSD 中当前 normal 类型的属性为 meanValue、variance 和 varianceWithPedigreeUncertainty，没有 Deviation。原文的标准差概念说明不等同于当前字段的方差存储约定。 正文保留原文参数名称；实现时对照 fieldId=2111/2112/2113 的 XSD 定义，不将标准差直接写入 variance 字段。请数据方澄清旧参数名称与当前属性的关系。
