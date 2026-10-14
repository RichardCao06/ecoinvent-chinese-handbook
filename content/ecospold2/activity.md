# 活动（TActivity）

源文分组：Activity。本章完整收录 **20 条字段定义**。

XML 位置：`activityDescription/activity`。以 `activityDescription/`、`flowData/`、`modellingAndValidation/` 或 `administrativeInformation/` 开头的位置，均相对于 `/ecoSpold/activityDataset/`；`…` 表示可复用结构。

[阅读约定与 XSD 约束](reading-guide.md) · [全部字段索引](field-index.md) · [审校记录](translation-review.md)

> 本参考译自官方格式包 v1.0.13（所附 XSD version 为 2.0.13）。必填性和重复性先忠实保留原表，再单列 XSD 结构约束；不自动代表所有后续版本的模式。

{% hint style="warning" %}
本章含原文疑点；请阅读文末审校注记，尤其不要据此擅自修正字段名或数值定义。
{% endhint %}

{% tabs %}

{% tab title="中文" %}

## 结构说明

分组可重复：否；分组必填：是。

包含活动数据集的标识信息，包括名称和分类。

### `activityName` · FieldID 100 <a href="#field-100" id="field-100"></a>

局部 XML 位置：`TActivity/activityName`；ecoSpold1 对照编号：`401-rename`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString120` | 是 | 否 |

长度：120；多语言：是；主数据冗余字段：是。

本数据集所表示活动的名称。

**XSD 结构约束：** `minOccurs="1"`，`maxOccurs="unbounded"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@id` · FieldID 102 <a href="#field-102" id="field-102"></a>

局部 XML 位置：`TActivity/@id`；ecoSpold1 对照编号：`200-type`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

该活动的唯一标识符。UUID 数据类型是包含十六进制字符的 36 个字符长字符串，可确保标识符在全球范围内唯一。新条目的 UUID 必须由外部软件提供。网上有多种 UUID 生成器，大多数编程语言中也有相应实现。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@activityNameId` · FieldID 105 <a href="#field-105" id="field-105"></a>

局部 XML 位置：`TActivity/@activityNameId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 是 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对该活动的活动名称主数据条目的引用。

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@activityNameContextId` · FieldID 106 <a href="#field-106" id="field-106"></a>

局部 XML 位置：`TActivity/@activityNameContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对活动名称所属上下文的引用。

若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@type` · FieldID 110 <a href="#field-110" id="field-110"></a>

局部 XML 位置：`TActivity/@type`；ecoSpold1 对照编号：`201-type`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

表示本数据集所包含的数据种类（1 = 单元过程；2 = 已汇总的完整产品系统（System terminated））。数据提供方始终以单元过程形式录入数据。数据库生成的归因型和后果型数据集，既可按单元过程层级提供，也可作为汇总的完整系统数据集（即生命周期清单结果）提供；后者包含与该单元过程某一特定产品相关的产品系统中汇总的基本流交换和影响。完整产品系统包括通过中间交换链接的全部上游活动数据集，因此其自身不再包含任何中间交换，而仅包含环境交换和累积的影响评价结果。

**取值选项（原表）：** 1 = 单元过程；2 = 已汇总的完整产品系统（System terminated）

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@specialActivityType` · FieldID 115 <a href="#field-115" id="field-115"></a>

局部 XML 位置：`TActivity/@specialActivityType`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 是 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

特殊活动类型如下：
0 = “普通”转化活动。转化活动是将输入转化为不同输出的人类活动，例如硬煤矿将地下硬煤转化为可销售产品硬煤。此处采用最广义的转化活动概念，包括开采、生产、运输、消费和废物处理活动，即任何中间输出不同于中间输入的人类活动。引入“转化活动”这一概念，仅用于在后续活动建模和链接中，将这些“普通”活动与市场活动、生产及供应组合、进出口活动和修正数据集区分开。
1 = 市场活动。市场活动不转化输入，而仅将某转化活动的中间输出传递给以该中间输出作为输入的消费转化活动，例如将供应商处的硬煤传递至消费者处的硬煤。市场活动通常混合不同转化活动的类似中间输出，因此提供这些中间输出的消费组合。
10 = 市场组。市场组与市场之间的关系，类似于市场与转化活动之间的关系。在未指定系统模型中，市场组仅包含参考产品。链接算法将位于市场组地理范围内、且具有相同参考产品的供应市场添加为输入。
2 = 投入产出活动（IO activity）。IO 活动表示来自国家供给使用表的活动数据集，通常对应某一特定行业的供给和使用。
3 = 残余活动。在同一年及同一地理区域内，从某活动类别的供给使用数据（IO 活动）中减去该类别所有可用单元过程后，所得的活动即为残余活动。
4 = 生产组合。生产组合表示某地理区域内特定产品供应者按生产量加权的平均情况。
5 = 进口活动。进口活动表示某特定产品进入某特定地理区域的进口，仅用于国家层面的平衡核算，不参与任何自动生成的消费组合。进入行政约束市场的进口，以及来自部分孤立市场的进口，按普通转化活动建模，以便纳入相关市场活动（消费组合）。
6 = 供应组合。供应组合是在生产组合中加入某特定产品进入某特定地理区域的进口。
7 = 出口活动。出口活动表示国家生产组合的出口量，以该国范围为其地理位置，不参与任何自动生成的消费组合。为正确计算出口的价值，将市场活动所包含的相同活动和数据直接加入出口活动，包括运输活动、生产损失、批发商和零售商活动，以及产品税和补贴。
8 = 再出口活动。再出口活动表示某地理区域的再出口量，不参与任何自动生成的消费组合。
9 = 修正活动。修正活动是向产品系统添加两次的活动，一次带正流、一次带负流，以便将一个或多个交换从系统的一部分转移至另一部分，例如修正上游活动的下游效应，或修正分配造成的质量平衡偏差。更多说明见 ecoinvent《数据质量指南》中的“产品质量差异导致的下游变化”（Downstream changes caused by differences in product quality）和“分配修正”（Allocation corrections）章节。

**取值选项（原表）：** 0 = 普通转化活动（默认）；1 = 市场活动；10 = 市场组；2 = 投入产出活动（IO activity）；3 = 残余活动；4 = 生产组合；5 = 进口活动；6 = 供应组合；7 = 出口活动；8 = 再出口活动；9 = 修正活动

**XSD 结构约束：** `use="required"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `generalComment` · FieldID 120 <a href="#field-120" id="field-120"></a>

局部 XML 位置：`TActivity/generalComment`；ecoSpold1 对照编号：`492`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TTextAndImage` | 否 | 否 |

长度：—；多语言：是；主数据冗余字段：否。

用于提供数据集一般信息的文本和图像字段。这里只应填写性质较为一般、无法放入其他更具体说明字段的说明和引用。总体上，数据集中的信息应足以判断其是否适合某项特定应用。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

复合类型详情：[ `TTextAndImage` ](text-and-image.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@parentActivityId` · FieldID 130 <a href="#field-130" id="field-130"></a>

局部 XML 位置：`TActivity/@parentActivityId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

parentActivityId 是指向父活动数据集的 UUID。此字段填入 UUID 时，父活动数据集的全部字段内容均由子活动数据集承接；子活动数据集即通过 UUID 调用父数据集的活动。

子活动由其父活动派生（继承）而来，子过程中仅存储相对于父活动发生变化的内容。子活动数据集不能使用 EcoSpold02 模式进行验证，因为其大多数必填字段不会填写。更多细节请参阅有关 ecoinvent 数据库数据集继承的补充文档。

子活动数据集（"http://www.EcoInvent.org/EcoSpold02Child"）中的字段有 5 种填写方式：

1）将字段留空：此时采用父活动数据集中的值。

2）填入内容：此时采用填入的值，忽略父活动数据集中的值。

3）在字符串字段中填入包含 {{PARENTTEXT}} 的文本：此时，父活动数据集中的字段内容会插入子数据集所填文本的该位置。

4）在类型为 TTextAndImage 的字段中，同时支持 {{PARENTTEXT}} 和 {{text\_variables}}；后者允许在父数据集中定义文本变量，并在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

5）对于具有对应数学关系字段的数量（amount）字段，在 mathematicalRelation 字段中填入包含保留变量 PARENTVALUE 的内容，例如公式 PARENTVALUE\*0.5 会使原数量（amount）字段的值减半。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@parentActivityContextId` · FieldID 131 <a href="#field-131" id="field-131"></a>

局部 XML 位置：`TActivity/@parentActivityContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对父活动所属上下文的引用。

若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@inheritanceDepth` · FieldID 135 <a href="#field-135" id="field-135"></a>

局部 XML 位置：`TActivity/@inheritanceDepth`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

继承深度表示当前数据集可具有的父数据集最大数量。ecoinvent 上下文采用以下值：0 = 不是子数据集；1 = 地理子数据集；2 = 时间子数据集；3 = 宏观经济情景子数据集。

**XSD 结构约束：** `use="optional"`；`default="0"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `includedActivitiesStart` · FieldID 145 <a href="#field-145" id="field-145"></a>

局部 XML 位置：`TActivity/includedActivitiesStart`；ecoSpold1 对照编号：`402-type`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString32000` | 否 | 否 |

长度：32000；多语言：是；主数据冗余字段：否。

描述活动的起点。对于“system terminated”（已汇总的完整产品系统），起点始终是“从摇篮开始，即包含全部上游活动”（From cradle, i.e. including all upstream activities）。对于单元过程，可根据输入的性质描述起点，例如“从接收［如原材料 X］开始……”或“以［如劳动力和能源］输入为起点的服务”。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `includedActivitiesEnd` · FieldID 150 <a href="#field-150" id="field-150"></a>

局部 XML 位置：`TActivity/includedActivitiesEnd`；ecoSpold1 对照编号：`402-type`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TString32000` | 否 | 否 |

长度：32000；多语言：是；主数据冗余字段：否。

描述活动名称中未能不言自明的所包含活动，以及有意排除的活动或输入。例如，“application of pesticides”（农药施用）活动作为一项服务时排除农药本身，以便适用于多种有效成分。说明应以最后一个活动和／或交付点结束，例如“直至并包括将产品装载到货车上”。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `synonym` · FieldID 170 <a href="#field-170" id="field-170"></a>

局部 XML 位置：`TActivity/synonym`；ecoSpold1 对照编号：`491-type`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TSynonym` | 否 | 是 |

长度：80；多语言：是；主数据冗余字段：否。

名称的同义词列表。与一般多语言字符串不同，同义词可包含多个 xml:lang 属性值相同的元素。

允许 0..n 个条目，每个条目的最大长度为 80。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `tag` · FieldID 175 <a href="#field-175" id="field-175"></a>

局部 XML 位置：`TActivity/tag`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TTag` | 否 | 是 |

长度：40；多语言：否；主数据冗余字段：否。

tag 字段允许使用开放的关键词列表描述活动，可用于筛选、分组和搜索。validTags 文件引用提供预定义标签的列表；但若在 validTags 主文件中找不到某标签条目，语义验证程序应仅显示提示信息，而非错误。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="unbounded"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@energyValues` · FieldID 180 <a href="#field-180" id="field-180"></a>

局部 XML 位置：`TActivity/@energyValues`；ecoSpold1 对照编号：`203`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `integer` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

表示数据集中采用能源数值的方式。代码为：0 = 未指定（默认）；1 = 净（低位）热值；2 = 总（高位）热值。

此数据字段默认设为 0。

**取值选项（原表）：** 0 = 未指定（Undefined，默认）；1 = 低位热值（Net values）；2 = 高位热值（Gross values）

**XSD 结构约束：** `use="optional"`；`default="0"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@masterAllocationPropertyId` · FieldID 190 <a href="#field-190" id="field-190"></a>

局部 XML 位置：`TActivity/@masterAllocationPropertyId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

通过 UUID 引用本数据集所有交换的默认分配属性。可为每项交换覆盖该分配属性（见字段 1150：specificAllocationPropertyId）。

某特定输出的分配因子，等于该输出所声明的 TProperty 值乘以输出数量，再除以所有输出的相应 TProperty 值与输出数量乘积之和。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@masterAllocationPropertyContextId` · FieldID 191 <a href="#field-191" id="field-191"></a>

局部 XML 位置：`TActivity/@masterAllocationPropertyContextId`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TUuid` | 否 | 否 |

长度：36；多语言：否；主数据冗余字段：否。

对主分配属性所属上下文的引用。

若省略此属性，则改用数据集自身的上下文。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@masterAllocationPropertyIdOverwrittenByChild` · FieldID 192 <a href="#field-192" id="field-192"></a>

局部 XML 位置：`TActivity/@masterAllocationPropertyIdOverwrittenByChild`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `boolean` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

若必须在子数据集中移除对某主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设为 true。否则，移除引用会被解释为“保留父数据集的值”（Keep the Parent Value）。

**XSD 结构约束：** `use="optional"`。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `allocationComment` · FieldID 195 <a href="#field-195" id="field-195"></a>

局部 XML 位置：`TActivity/allocationComment`；ecoSpold1 对照编号：`2407`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `TTextAndImage` | 否 | 否 |

长度：—；多语言：是；主数据冗余字段：否。

用于进一步说明分配程序及所选分配属性的文本和图像字段。比较不同分配参数（如物理参数和经济参数）时，若分配因子恰好相同，也可在此报告。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。

复合类型详情：[ `TTextAndImage` ](text-and-image.md)。

**XSD 结构约束：** `minOccurs="0"`，`maxOccurs="1"`（未显式声明的值按 XSD 默认值列出）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@datasetIcon` · FieldID 200 <a href="#field-200" id="field-200"></a>

局部 XML 位置：`TActivity/@datasetIcon`；ecoSpold1 对照编号：`new`。

| 类型 | 必填 | 可重复 |
| --- | --- | --- |
| `anyURI` | 否 | 否 |

长度：—；多语言：否；主数据冗余字段：否。

数据集图标的 URL。图标用于快速识别特定数据集，也可用于产品品牌和公司徽标。图标并非数据集的直接组成部分，而是存储于本地或 ecoinvent 网络服务器，可通过 Http 协议获取。

**XSD 结构约束：** `use="optional"`（XSD 默认值）。

模式出处：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

{% endtab %}

{% tab title="English 原文" %}

## Structure

Group multiple occurrences：No；Group required：Yes。

Contains the identifying information of an activity dataset including name and classification.

### `activityName` · FieldID 100 <a href="#en-field-100" id="en-field-100"></a>

Local XML path：`TActivity/activityName`；ecoSpold1 mapping：`401-rename`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString120` | Yes | No |

Size：120；Multi language：Yes；Redundant master data：Yes。

A name for the activity that is represented by this dataset.

**XSD structural constraints：** `minOccurs="1"`，`maxOccurs="unbounded"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@id` · FieldID 102 <a href="#en-field-102" id="en-field-102"></a>

Local XML path：`TActivity/@id`；ecoSpold1 mapping：`200-type`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Unique identifier for this activity. The datat type UUID is a 36 characters string with hexadecimal characters and ensures a world-wide unique identifier. A UUID for a new item must be supplied by external software. There are several UUID generators on the web and implementations in most programming languages.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@activityNameId` · FieldID 105 <a href="#en-field-105" id="en-field-105"></a>

Local XML path：`TActivity/@activityNameId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | Yes | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the activity name master data entry for this activity.

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@activityNameContextId` · FieldID 106 <a href="#en-field-106" id="en-field-106"></a>

Local XML path：`TActivity/@activityNameContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the activity name.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@type` · FieldID 110 <a href="#en-field-110" id="en-field-110"></a>

Local XML path：`TActivity/@type`；ecoSpold1 mapping：`201-type`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

Indicates the kind of data (1 = Unit process; 2 = System terminated) that is represented by this dataset. Data are always entered by the data providers as Unit process. The database-generated, attributional and consequential datasets are available both at the unit process level and as aggregated (terminated) system dataset (i.e. the life cycle inventory results) containing the aggregated elementary exchanges and impacts of the product system related to one specific product from the unit process. The terminated product systems include all upstream activity datasets, as linked by the intermediate exchanges, and therefore do not themselves have any intermediate exchanges, only environmental exchanges and accumulated impact assessment results.

**Options (original table)：** 1 = Unit process; 2 = System terminated

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@specialActivityType` · FieldID 115 <a href="#en-field-115" id="en-field-115"></a>

Local XML path：`TActivity/@specialActivityType`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | Yes | No |

Size：—；Multi language：No；Redundant master data：No。

The special activity types are: 0 = “ordinary” transforming activities. Transforming activities are human activities that transform inputs, so that the output of the activity is different from the inputs, e.g. a hard coal mine that transforms hard coal in ground to the marketable product hard coal. Transforming activities are here understood in the widest possible sense, including extraction, production, transport, consumption and waste treatment activities, i.e. any human activity where the intermediate output is different from the intermediate input. The concept “transforming activities” is introduced here simply to distinguish – in the further modelling and linking of activities – these “ordinary” activities from the market activities, production and supply mixes, import and export activities, and correction datasets.1 = market activity. Market activities do not transform their inputs, but simply transfer the intermediate output from a transforming activity to the transforming activities that consume this intermediate output as an input, e.g. from hard coal at the supplier to hard coal at the consumer. Market activities typically mix similar intermediate outputs from different transforming activities. Market activities therefore supply consumption mixes of the intermediate outputs.10 = market group. Market groups are to markets what markets are to transforming activities. In the undefined system model a market group only contains a reference product. The linking algorithm will add supplying markets as inputs which are contained in the location of the market group and have the same reference product.2 = IO activity. An IO activity represents an activity dataset from a national supply-use table, i.e. typically the supply and use of one specific industry.3 = Residual activity. A residual activity is the resulting activity when subtracting all available unit processes within an activity class from the supply-use data (IO activity) of the same activity class, for the same year and geo-graphical area. 4 = production mix. A production mix represents the production-volume-weighted average of the suppliers of a specific product within a geographical area.5 = import activity. An import activity represents the import of a specified product to a specified geographical area, solely for use in national balancing (not contributing to any auto-generated consumption mixes). Imports to administratively constrained markets and from partly isolated markets are modelled as ordinary transforming activities in order to be included in the relevant market activities (consumption mixes).6 = supply mix. A supply mix is a production mix with the addition of the import of a specified product to a specified geographical area.7 = export activity. An export activity represents the export volume of a national production mix that has the national area as its geographical location and does not contribute to any auto-generated consumption mixes. To give the correct value of the export, the same activities and data that are included with the market activities are added directly to the export activity. This includes transport activities, production losses, wholesaler and retailer activities, and product taxes and subsidies.8 = re-export activity. A re-export activity represents the re-export volume of a geographical area and does not contribute to any auto-generated consumption mixes.9 = correction activity. A correction activity is an activity that is added twice to a product system, one with a positive and once with a negative flow, in order to move one or more exchanges from one part of the system to another, e.g. to correct for downstream effects of an upstream activity, or to correct a bias in the mass-balance introduced by an allocation. More details on this is provided in the Chapters on "Downstream changes caused by differences in product quality" and "Allocation corrections" in the ecoinvent Data Quality Guidelines.

**Options (original table)：** 0 = ordinary transforming activity (default), 1 = market activity, 10 = market group, 2 = IO activity, 3 = Residual activity, 4 = production mix, 5 = import activity, 6 = supply mix, 7 = export activity, 8 = re-export activity, 9 = correction activity

**XSD structural constraints：** `use="required"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `generalComment` · FieldID 120 <a href="#en-field-120" id="en-field-120"></a>

Local XML path：`TActivity/generalComment`；ecoSpold1 mapping：`492`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TTextAndImage` | No | No |

Size：—；Multi language：Yes；Redundant master data：No。

Text and image field for general information about the dataset. Only comments and references of more general nature that cannot be placed in any of the more specific comment fields, should be placed here. In general, the information in the dataset should be sufficient to judge the appropriateness of a dataset for a specific application.Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

List of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

Complex type details：[ `TTextAndImage` ](text-and-image.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@parentActivityId` · FieldID 130 <a href="#en-field-130" id="en-field-130"></a>

Local XML path：`TActivity/@parentActivityId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

The parentActivityId is a UUID to the parent activity dataset. When this field is filled with a UUID, all the field content from the parent activity dataset is taken over by the child activity dataset (the activity that calls the parent via the UUID).

Child activity is derived (inherited) from its parent activity and only the content changes in comparison to its parent are stored in the child process. Child activity datasets cannot be validated using the EcoSpold02 schema, since most of the required fields will not be filled. Please refer to the additional documentation regarding inheritance of datasets in the ecoinvent database for further details.

There are 5 ways to fill a field in a child activity dataset ("http://www.EcoInvent.org/EcoSpold02Child"):

1\) Leave a field blank: In this case, the value from the parent activity dataset applies.

2\) Fill in content: In this case, the filled in value applies, and the value from the parent activity dataset is ignored.

3\) In a string field, fill in content including the text {{PARENTTEXT}} in which case the  field content from the parent activity dataset is included at this place in the filled in text in the child dataset.

4\) In a field with type TTextAndImage, both {{PARENTTEXT}} and {{text\_variables}} are supported; the latter allows to define text variables in the parent dataset and use them in the text as {{variablename}}. If a parent textfield includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

5\) In an amount field with corresponding mathematical relation fields, fill in content in the mathematicalRelation field including the reserved variable PARENTVALUE, e.g. the formula PARENTVALUE\*0.5 results in halfing the value of the original amount field.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@parentActivityContextId` · FieldID 131 <a href="#en-field-131" id="en-field-131"></a>

Local XML path：`TActivity/@parentActivityContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the parent activity.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@inheritanceDepth` · FieldID 135 <a href="#en-field-135" id="en-field-135"></a>

Local XML path：`TActivity/@inheritanceDepth`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | No | No |

Size：—；Multi language：No；Redundant master data：No。

The inheritance depth expresses the maximum number of parent datasets for the current dataset. The following values are used in the ecoinvent context: 0 = not a child, 1 = a geography child, 2 = a temporal child, 3 = a macro-economic scenario child.

**XSD structural constraints：** `use="optional"`；`default="0"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `includedActivitiesStart` · FieldID 145 <a href="#en-field-145" id="en-field-145"></a>

Local XML path：`TActivity/includedActivitiesStart`；ecoSpold1 mapping：`402-type`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString32000` | No | No |

Size：32000；Multi language：Yes；Redundant master data：No。

Describes the starting point of the activity. For "system terminated"  the starting point is always "From cradle, i.e. including all upstream activities". For unit processes, the starting point may be described in terms of the nature of the inputs, e.g. "From reception of \[e.g. raw material X\]..." or "Service starting with the input of \[e.g. labour and energy\].

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `includedActivitiesEnd` · FieldID 150 <a href="#en-field-150" id="en-field-150"></a>

Local XML path：`TActivity/includedActivitiesEnd`；ecoSpold1 mapping：`402-type`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TString32000` | No | No |

Size：32000；Multi language：Yes；Redundant master data：No。

Describes the included activities to the extent that this is not self-explanatory from the activity name, as well as activities or inputs that are intentionally excluded, e.g. if the activity “application of pesticides” as a service excludes the pesticide, in order to be applicable for many different active ingredients. The description ends by mentioning the last activity and/or point of delivery, e.g. “until and including loading of the product on lorries”.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `synonym` · FieldID 170 <a href="#en-field-170" id="en-field-170"></a>

Local XML path：`TActivity/synonym`；ecoSpold1 mapping：`491-type`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TSynonym` | No | Yes |

Size：80；Multi language：Yes；Redundant master data：No。

List of synonyms for the name. Contrary to normal multi language strings, synonyms may contain more than one element with the same xml:lang attribute value.

0..n entries are allowed with a max. length of 80 each.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `tag` · FieldID 175 <a href="#en-field-175" id="en-field-175"></a>

Local XML path：`TActivity/tag`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TTag` | No | Yes |

Size：40；Multi language：No；Redundant master data：No。

The tag field allows an open list of keywords which describes the activity and can be used for filtering, grouping and searching. The validTags file reference provides a list of predefined tags, but the semantic validation procedure should only display an information (not an error) if a tag entry cannot be found in the validTags master file.

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="unbounded"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@energyValues` · FieldID 180 <a href="#en-field-180" id="en-field-180"></a>

Local XML path：`TActivity/@energyValues`；ecoSpold1 mapping：`203`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `integer` | No | No |

Size：—；Multi language：No；Redundant master data：No。

Indicates the way energy values are applied in the dataset. The codes are: 0=Undefined (default). 1=Net (lower) heating value. 2=Gross (higher) heating value.

This data field is by default set to 0.

**Options (original table)：** 0 = Undefined (default); 1 = Net values; 2 = Gross values

**XSD structural constraints：** `use="optional"`；`default="0"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@masterAllocationPropertyId` · FieldID 190 <a href="#en-field-190" id="en-field-190"></a>

Local XML path：`TActivity/@masterAllocationPropertyId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

References the default Allocation Property (via UUID) for all exchanges of this dataset. The Allocation Property can be overwritten for each exchange (see field 1150 specificAllocationPropertyId).

The allocation factor for a specific output is then the declared TProperty value for this output multiplied by the amount of the output divided by the sum of the all such multiplied TProperty values for all outputs.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@masterAllocationPropertyContextId` · FieldID 191 <a href="#en-field-191" id="en-field-191"></a>

Local XML path：`TActivity/@masterAllocationPropertyContextId`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TUuid` | No | No |

Size：36；Multi language：No；Redundant master data：No。

Reference to the context of the master allocation property.

If this attribute is omitted the context of the dataset itself will be used instead.

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@masterAllocationPropertyIdOverwrittenByChild` · FieldID 192 <a href="#en-field-192" id="en-field-192"></a>

Local XML path：`TActivity/@masterAllocationPropertyIdOverwrittenByChild`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `boolean` | No | No |

Size：—；Multi language：No；Redundant master data：No。

If a reference to a master data entity must be removed in a child dataset it is required to set the corresponding xxxOverwrittenByChild attribute to true. Otherwise the removed referenced will be interpreted as "Keep the Parent Value".

**XSD structural constraints：** `use="optional"`。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `allocationComment` · FieldID 195 <a href="#en-field-195" id="en-field-195"></a>

Local XML path：`TActivity/allocationComment`；ecoSpold1 mapping：`2407`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `TTextAndImage` | No | No |

Size：—；Multi language：Yes；Redundant master data：No。

Text and image field for further information about the allocation procedure and the allocation properties chosen. An eventual coincidence in allocation factors when comparing different allocation parameters (like physical and economic ones) may be reported here as well.Text and image fields are list of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

List of text, imageUri and variable elements. The text and imageUri elements can used to describe the current section and they can be combined in any order given by their index attribute. Text variables are defined by the variable elements, which may be used in the text as {{variablename}}. If a parent text field includes a variable, this variable may be redefined by the child activity dataset while keeping the rest of the parent text intact. This allows easy changes of text parts in child processes.

Complex type details：[ `TTextAndImage` ](text-and-image.md)。

**XSD structural constraints：** `minOccurs="0"`，`maxOccurs="1"` (undeclared values use XSD defaults)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

### `@datasetIcon` · FieldID 200 <a href="#en-field-200" id="en-field-200"></a>

Local XML path：`TActivity/@datasetIcon`；ecoSpold1 mapping：`new`。

| Type | Required | Multiple occurrence |
| --- | --- | --- |
| `anyURI` | No | No |

Size：—；Multi language：No；Redundant master data：No。

The URL of the dataset icon. A dataset icon serves a quick identification of the specific dataset, and may also be used for product brands and company logos. The icon is not directly part of the dataset, but is stored locally or on the ecoinvent web-server, from where it is retrievable via the Http protocol.

**XSD structural constraints：** `use="optional"` (XSD default)。

Schema source：[EcoSpold02MetaInformation.xsd](original/Schemas/datasets/EcoSpold02MetaInformation.xsd)，`TActivity`。

{% endtab %}

{% endtabs %}

## 翻译与审校注记

- **已处理／已说明 · `TActivity.110.description.0`**：System terminated 在此指已沿中间交换纳入全部上游活动并汇总的产品系统，不是停运或生命周期终结的系统。 译为“已汇总的完整产品系统”，并在枚举中保留 System terminated 对照；全文保留仅有环境交换及累积影响结果的限定。

- **已处理／已说明 · `TActivity.130.description.1`**：原文限制是子活动数据集不能用 EcoSpold02 模式验证，不是数据集不能被任何方式验证；子过程仅存储相对父过程变化的内容。 译文明确保留模式名称、验证限制及仅存储差异的范围，不推断继承展开后的验证行为。

- **待专家复核 · `TActivity.135.description.0`**：原文先把 inheritance depth 定义为父数据集最大数量，随后又以地理、时间和宏观经济情景子数据集类型说明 1、2、3，层数与类型之间的对应关系需核对继承规范。 保持原文定义和全部枚举编号，请依据继承专门文档确认各层级的允许嵌套关系。

- **已处理／已说明 · `TActivity.180.options`**：原译枚举“净值/总值”容易被理解为一般净总数值；同字段说明明确 Net/Gross 指低位/高位热值。已改为具体热值名称，保留 0、1、2 及默认值对应关系，并补充原英文标签。 采用修正后的热值枚举中文说明。

- **待专家复核 · `TActivity.120.description.0`**：本块及 TActivity.120.description.1、TActivity.195.description.0/.1、TTimePeriod.630.description.0/.1 的复用说明使用 imageUri，但 EcoSpold02DataTypes.xsd 的 TTextAndImage 实际元素名为 imageUrl（约第 940 行）。译文忠实保留 imageUri，未静默改变原文 XML 名。 请依据 TTextAndImage 的实际 XSD 元素定义统一官方说明中的 imageUri/imageUrl 命名。
