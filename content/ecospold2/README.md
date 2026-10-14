# 读懂一份 ecoSpold2 文件：从 XML 结构到所需数据

拿到一份 `.spold` 文件后，最有用的问题通常是：它描述哪个活动、为多少参考产品建立清单、消耗多少电力或材料、排放了什么、这些量的单位是什么，以及它是否已经包含上游过程或影响评价结果。回答这些问题，需要同时读懂 XML 的层级和生命周期清单的计量口径。单独搜索 `amount`，会把交换量、参数值、属性值和影响指标值混在一起。

这篇文章从一份可下载、可运行的教学 demo 出发，先演示实际读取过程，再按文件结构解释官方格式说明中的全部 243 条字段。正文采用连续讲解；需要核对类型、长度和必填标记时，可读文末的原始 HTML 格式表中文译表，或使用[字段索引](field-index.md)。

字段依据是官方 `EcoSpold02.html` 及同包 XSD：下载包名称为 v1.0.13，XSD 的 `version` 为 2.0.13。XML 模式版本与 ecoinvent 数据库版本应分别核对。本文提供该格式包的参考解释；读取实际文件时，还应核对其来源、系统模型、导出类型和适用模式。官方入口见 [ecoSpold2](https://support.ecoinvent.org/ecospold2)，原件见[格式包 ZIP](original/documentation_on_ecospold2_format.v1.0.13.zip)。

## 一、首先确定文件里的量属于哪个层级

`.spold` 本身是 XML 数据，读取时可以直接解析，无需为了程序处理改扩展名。官方下载说明把 linked UPR、LCI 和 LCIA 列为不同的导出选项；这些文件外观相近，数值的范围却不同。[官方导出说明](https://support.ecoinvent.org/downloading-and-viewing-of-datasets)和[UPR、LCI、LCIA 的区别](https://support.ecoinvent.org/upr-lci-lcia)可帮助核对下载来源。

UPR 是单元过程层面的清单。它的电力输入是该过程所需的电力，它的基本流输出是该过程直接记录的环境交换。沿供应链接查到上游电力过程，并不等于这些上游排放已经包含在当前 UPR 的基本流里。LCI 则是沿产品系统求得的累积基本流清单；LCIA 是将相应清单按指定方法和指标进行表征等处理后得到的结果。因此，“某个文件中二氧化碳的 `amount`”与“某个文件中气候变化指标的 `amount`”可能具有完全不同的含义。

`activity/@type` 在所附规范里用 1 表示单元过程，用 2 表示汇总系统。这个字段有助于判断清单层级，但不能单凭一个数字确认导出到底是 LCI 还是 LCIA，也不能据此推断文件一定包含完整结果。实际读取还应结合下载选项、`flowData` 的内容、系统模型以及参考产品。有 `impactIndicator` 时，可以读取其中已提供的指标；没有它时，程序不能把某个基本流数量自动改称碳足迹。

第二个先要确认的问题是计量基准。一个清单可能围绕 1 kg 产品建立，也可能围绕 10 kg、1 kWh 或一项服务建立。应在中间交换中寻找 `outputGroup` 为 0 的参考输出，再读它的 `amount`、`unitName` 和产品 UUID。交换量除以参考输出量可以得到相对于该参考单位的算术比例，但这个动作不会执行分配、连接上游网络或进行影响评价。多参考输出、负参考量、零参考量以及未经分配的多功能数据集都需要额外处理，不能机械地除以第一行输出。

## 二、把 XML 看成活动描述、数量清单和证据的组合

普通数据集的外层通常是 `ecoSpold/activityDataset`，下面依次组织活动描述 `activityDescription`、数量与结果 `flowData`、建模与审查 `modellingAndValidation`，以及管理信息 `administrativeInformation`。一个 `ecoSpold` 根元素可以包含多个数据集，因此“一个文件等于一个活动”只是某些导出的组织习惯，不能作为解析器的硬编码假设。

`activityDescription` 告诉你数量适用于什么活动、什么地区和时间、采用什么技术，以及哪些活动包含在系统边界内。`flowData` 告诉你投入、产出、环境交换、参数和指标值是多少。`modellingAndValidation` 帮助判断系统模型、代表性、数据怎样推算和是否经过审查。`administrativeInformation` 记录人员、来源、发布和修订、文件时间戳，以及解释主数据引用时所需的上下文。读取交换量后保留这些证据，才能在后续分析中判断两个数能否比较。

在 XML 中，`amount="25"` 这样的写法是属性，`<unitName>kWh</unitName>` 这样的写法是子元素。格式说明里的 `@amount` 用 `@` 表示属性；这个字符不是实际 XML 属性名。程序读取属性用 `.get("amount")`，读取子元素需要按路径查找，再读取其文本。

命名空间也必须参与查找。普通 ecoSpold2 元素使用 `http://www.EcoInvent.org/EcoSpold02`。当文件用 `xmlns="…"` 声明默认命名空间时，Python 中的标签实际包含该 URI；不带命名空间的 `find("flowData")` 往往找不到数据。URI 是标识符，不是每次读取时都要请求的网络地址。[Python ElementTree 文档](https://docs.python.org/3/library/xml.etree.elementtree.html)说明了默认命名空间、元素路径和属性的读取方式。

还有一种容器叫 `childActivityDataset`，记录相对于父数据集的差异。它与 `activityDataset` 两个容器本身都属于 EcoSpold02 命名空间，子数据集使用的类型和内部元素则来自 `EcoSpold02Child` 命名空间。若只有差异文件，应先按继承规则展开父数据，而不是把所有省略字段当作零。本文配套提取器会明确拒绝尚待展开的子数据集容器；完整普通数据集里的父级引用也应保留，不能随意删去。

## 三、先用 demo 走通一次读取过程

[下载 demo、提取脚本及使用说明 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后即可按第五节运行。

配套的 [demo-product.spold](demo/demo-product.spold)、[demo-electricity.spold](demo/demo-electricity.spold) 和 [demo-lcia.spold](demo/demo-lcia.spold) 是本教程构造的数据，UUID、人员、数值和方法名称均用于教学。它们以注释明确标识来源，并已通过所附 XSD 的结构校验；配套提取器、教程短代码和查询脚本也已实际运行核验，具体命令及范围见配套审阅记录。模式校验检查的是结构与类型；它不认证物理清单的完整性、主数据是否属于真实 ecoinvent 上下文或结果是否符合某个正式评价方法。

主过程以 10 kg 教学产品为参考输出，输入 25 kWh 电力和 0.04 m3 环境水；向空气记录 1.5 kg 化石源二氧化碳、同一流与同一区室的一笔 -0.1 kg 修正，以及另一个 UUID 的 0.2 kg 生物源二氧化碳。电力输入链接到另一个教学活动，该活动以 1 kWh 电力为参考输出，直接记录 0.5 kg 化石源二氧化碳。

模拟结果文件用于演示怎样读取 `impactIndicator`。在这个教学练习中，人为约定化石源二氧化碳的指标系数为 1，生物源二氧化碳及用水的该指标系数为 0，并仅计入所列过程。于是主过程直接化石源量为 `1.5 - 0.1 = 1.4 kg`，所需电力的上游化石源量为 `25 × 0.5 = 12.5 kg`，教学产品系统的化石源总量为 `13.9 kg`。模拟指标写为 13.9 kg CO2-eq；相对于 1 kg 产品为 1.39 kg CO2-eq。这些系数是教学约定，不能据此套用真实数据库或某个官方 LCIA 方法。

### 对照 demo 阅读四个实际 XML 节点

下面的节点直接摘自配套教学文件，仅将较长的属性行折行。每个片段是该节点的完整结构；文件根元素、兄弟节点和管理信息请看完整 demo。

**参考产品：10 kg**

```xml
<intermediateExchange
    xmlns="http://www.EcoInvent.org/EcoSpold02"
    id="b8754d71-a0c7-5b08-a889-67d6f1146d58"
    amount="10"
    unitId="a4800e12-54b1-5444-a6d0-b48a59529439"
    intermediateExchangeId="c5a1fe25-46d4-5646-9d78-5c10b6bfdeae"
>
        <name xml:lang="zh">教学产品</name>
        <name xml:lang="en">Teaching product</name>
        <unitName xml:lang="zh">kg</unitName>
        <unitName xml:lang="en">kg</unitName>
        <property
            propertyId="157cb588-bc77-5666-9107-3791e5783446"
            amount="1"
            unitId="00875264-8155-513e-8182-437026535fcb"
            isDefiningValue="true"
        >
          <name xml:lang="zh">干质量（教学比例）</name>
          <name xml:lang="en">Dry mass (teaching ratio)</name>
          <unitName xml:lang="zh">kg/kg</unitName>
          <unitName xml:lang="en">kg/kg</unitName>
        </property>
        <outputGroup>0</outputGroup>
      </intermediateExchange>
```

**电力输入：25 kWh**

```xml
<intermediateExchange
    xmlns="http://www.EcoInvent.org/EcoSpold02"
    id="33697568-a16c-54ea-a6db-8275bf713e20"
    amount="25"
    unitId="a5533771-6995-50cd-b03c-7a2af998708e"
    intermediateExchangeId="cf4dd220-d849-5595-92fe-1dac1fcecae7"
    activityLinkId="44be1818-16fc-56f4-a988-9306a39129df"
    variableName="electricity_use"
    isCalculatedAmount="true"
    mathematicalRelation="electricity_intensity * 10"
>
        <name xml:lang="zh">教学电力</name>
        <name xml:lang="en">Teaching electricity</name>
        <unitName xml:lang="zh">kWh</unitName>
        <unitName xml:lang="en">kWh</unitName>
        <uncertainty>
          <lognormal
              meanValue="25"
              mu="3.2188758248682006"
              variance="0.01"
              varianceWithPedigreeUncertainty="0.04"
          />
        </uncertainty>
        <inputGroup>2</inputGroup>
      </intermediateExchange>
```

**化石源二氧化碳修正：仍是 outputGroup 输出**

```xml
<elementaryExchange
    xmlns="http://www.EcoInvent.org/EcoSpold02"
    id="fff82fe6-92c9-5f26-98e2-3b04663bc952"
    amount="-0.1"
    unitId="a4800e12-54b1-5444-a6d0-b48a59529439"
    elementaryExchangeId="f420b314-c085-57e7-ba47-5cdfa839e9a3"
    formula="CO2"
>
        <name xml:lang="zh">二氧化碳，化石源（教学）</name>
        <name xml:lang="en">Carbon dioxide, fossil (synthetic)</name>
        <unitName xml:lang="zh">kg</unitName>
        <unitName xml:lang="en">kg</unitName>
        <compartment subcompartmentId="6bbb1a41-12de-5599-843e-cc02d4084a9a">
          <compartment xml:lang="zh">空气</compartment>
          <compartment xml:lang="en">air</compartment>
          <subcompartment xml:lang="zh">未指定</subcompartment>
          <subcompartment xml:lang="en">unspecified</subcompartment>
        </compartment>
        <outputGroup>4</outputGroup>
      </elementaryExchange>
```

**模拟 LCIA 指标：13.9 kg CO2-eq**

```xml
<impactIndicator
    xmlns="http://www.EcoInvent.org/EcoSpold02"
    impactIndicatorId="9ce9802d-268d-5ac0-af08-ffca6dc91aa2"
    impactMethodId="496741dc-72ec-5f95-bedb-078512fde969"
    impactCategoryId="07a7bfca-c863-5fd0-a2bf-24aa3af0d959"
    amount="13.9"
>
        <impactMethodName xml:lang="zh">教学方法（非官方）</impactMethodName>
        <impactMethodName xml:lang="en">Teaching method (synthetic, unofficial)</impactMethodName>
        <impactCategoryName xml:lang="zh">教学化石CO2类别</impactCategoryName>
        <impactCategoryName xml:lang="en">Teaching fossil CO2 category</impactCategoryName>
        <name xml:lang="zh">教学GWP（构造）</name>
        <name xml:lang="en">Teaching GWP (synthetic)</name>
        <unitName xml:lang="zh">kg CO2-eq</unitName>
        <unitName xml:lang="en">kg CO2-eq</unitName>
      </impactIndicator>
```

### 先读参考产品，再读电力输入

打开主过程文件，在 `activityDescription/activity` 中读活动名称与 `id`；接着进入 `flowData`，找到 `intermediateExchange` 下 `outputGroup` 为 0 的那一行。该行的 `amount` 是 10，`unitName` 是 kg，`intermediateExchangeId` 是教学产品的主数据 UUID。这样才能确定下面所有清单数值的参考基准。

再找电力那一行。它也是 `intermediateExchange`，但有 `inputGroup`，因此是技术圈输入。该行的 25 是电力量，单位是 kWh；除以 10 kg 参考输出得到每 kg 产品 2.5 kWh。这里读取的是该活动所消耗的电力，不能把 25 当作电力产品的全国年度产量，也不能把该交换的 `id` 当作供应活动的 UUID。

这三个 ID 应连起来理解：交换 `id` 标识“本文件中的这一笔交换”，`intermediateExchangeId` 标识“交换的是哪个产品”，`activityLinkId` 标识“明确链接的供应活动”。demo 中电力输入的 `activityLinkId` 可以与电力 demo 的 `activity/@id` 配对，再确认后者的参考产品 UUID、上下文和模型一致。实际导出缺少目标活动时，你只能得到一条尚未解析的供应引用；同名电力字符串不能替代这次匹配。

### 再读环境交换，保留方向、区室和符号

水行属于 `elementaryExchange`，表示与环境的交换。在此 demo 中，它带 `inputGroup`，量为 0.04，单位为 m3，所以原记录是从环境取得 0.04 m3 水，相对于 1 kg 产品为 0.004 m3。应同时读 `compartment/compartment`、`compartment/subcompartment` 以及子区室 UUID，知道这笔水取自哪种环境区室。

化石源二氧化碳行同样属于 `elementaryExchange`，但带 `outputGroup`，流向空气。1.5 与 -0.1 两行都仍然是输出；负号表达这笔记录的修正方向，不会把 `outputGroup` 自动改成输入。应保留两行原记录，只有当你的汇总问题明确允许，并且主数据流 UUID 及其有效上下文、区室、子区室及其有效上下文、单位 UUID 及其有效上下文都一致时，才合并为净量 1.4 kg。`id` 不同说明它们是两个交换实例，不能把后一行当作重复数据丢掉。

生物源二氧化碳使用另一个流 UUID。即使两个名称都包含“Carbon dioxide”，也不能只靠名称关键字把它们合并。对于“该过程直接化石源二氧化碳排放是多少”这个问题，demo 的答案是每份参考输出 1.4 kg、每 kg 产品 0.14 kg。这个数只是 UPR 直接清单的净量，和模拟产品系统的 1.39 kg CO2-eq 指标不是同一个问题。

### 读结果时，先确认指标的身份

在模拟 LCIA 文件中，目标节点是 `flowData/impactIndicator`，不是某个 `elementaryExchange`。同时读 `impactMethodId`、`impactCategoryId`、`impactIndicatorId` 及其各自的 `impactMethodContextId`、`impactCategoryContextId`、`impactIndicatorContextId`，对应的名称，以及 `amount` 和 `unitName`。本版 `TImpactIndicatorResult` 没有 `unitId` 或 `unitContextId` 属性，因此单位应结合指标主数据定义核对，不能照搬交换字段的单位 UUID 路径。可选上下文省略时按规范采用数据集上下文；若数据集上下文也不可知，应保留尚未解析的身份状态。数值 13.9 的含义受方法、类别、指标、单位和参考输出共同限定；不能仅凭“气候变化”这个名称比较来自不同方法或版本的结果。

把这个文件的指标量除以它的 10 kg 参考输出，得到教学结果每 kg 产品 1.39 kg CO2-eq。实际文件可能已经以 1 单位参考产品规范化，因此每次都应先读该文件自身的参考输出，而不是把某个其他文件的参考量套过来。

## 四、沿文件结构理解每一组字段

下面按 XML 的顺序展开完整字段讲解。关联字段放在同一段落中解释，便于把名称、引用、数量和证据连接起来。主 HTML 的 243 条定义都在这些段落中覆盖；基础文本类型内部的 `xml:lang`、`index` 等额外节点，还需要结合原包 XSD 阅读。

### 4.1 活动描述：确定清单适用于什么活动

#### 先识别活动，再判断边界与继承 <a href="#read-TActivity" id="read-TActivity"></a>

读取一个活动数据集时，可先进入 `activityDescription/activity`。这个元素采用 `TActivity` 类型，回答“这是什么活动、记录了哪一层数据、边界在哪里”。元素 `activityName` 是供人阅读的活动名称；属性 `id` 是活动的 UUID，而 `activityNameId` 是对活动名称主数据条目的 UUID 引用。两种 UUID 的角色不同：前者识别活动，后者查找名称主数据，不能因为都使用 `TUuid` 就混作同一个键。该类型以 36 个字符表示 UUID；创建新条目的 UUID 需要由外部软件生成。`activityNameContextId` 指明名称主数据所属上下文，省略时使用数据集自身的上下文。因此，程序可以把名称提取为显示文本，但在追踪对象身份和解析主数据时，应同时保留相应 UUID 与上下文。

接下来读取属性 `type`，区分单元过程与汇总结果。`type=1` 表示单元过程，这是数据提供方录入数据的形式；`type=2` 表示 `System terminated`，即已经纳入上游活动并汇总的完整产品系统。这种系统记录与单元过程某一特定产品有关的累积生命周期清单及影响结果，已包含沿中间交换链接的全部上游活动。官方说明将这种产品系统描述为“自身没有中间交换，只有环境交换和累积影响评价结果”，强调上游供应结构已经汇总；但当前完整 XSD 的 `TFlowData` 仍要求至少一个 `intermediateExchange`，因为该元素的 `minOccurs` 未显式设置，默认值为 `1`。教学结果文件用这个元素承载参考输出，而不保留上游电力输入。因此，不能以是否存在任意中间交换判断 UPR，也不能仅凭 `type=2` 确认某份文件已提供 LCIA。这个说明与模式之间的差异需要保留；各种真实 LCI、LCIA 导出的具体内容仍须结合其来源和文件核对。这里的 terminated 不能理解成“设备停运”或“废物寿命终结”。在提取供应链连接或过程间产品流之前，先检查这一属性，避免把汇总清单当成保留供应商结构的单元过程。

属性 `specialActivityType` 进一步说明活动在数据库中的作用。值 `0` 是普通转化活动：输入被转化为不同的输出，范围包括开采、生产、运输、消费和废物处理。值 `1` 是市场活动：它不转化输入，而把生产者的中间输出传递给消费者，通常混合不同生产者的类似产品，形成消费组合。值 `10` 是市场组：它把市场再按区域汇集；在未指定系统模型中仅有参考产品，链接算法会加入地理范围内、参考产品相同的供应市场。值 `2` 是来自国家供给使用表的投入产出活动，通常表示特定行业的供给与使用；值 `3` 是残余活动，是从同一年、同一地区、同一活动类别的供给使用数据中减去已有单元过程后得到的部分。读取时应据此区分“生产产品的过程”“把产品连接起来的市场”和“统计表中的行业活动”。

其余类型描述组合、贸易和修正。`specialActivityType=4` 是某地区内供应者按生产量加权的生产组合；`5` 是指定产品进入指定地区的进口活动，仅用于国家平衡核算，不参与自动生成的消费组合。进入行政约束市场或来自部分孤立市场的进口，为纳入消费组合而按普通转化活动建模。值 `6` 是在生产组合中加入进口的供应组合。值 `7` 是国家生产组合的出口量，地理范围为该国，不参与自动消费组合；为得到正确出口价值，还直接纳入市场通常承担的运输、生产损失、批发零售活动、产品税和补贴。值 `8` 是地区的再出口量，同样不参与自动消费组合。值 `9` 是修正活动：它以正流和负流各加入一次，把交换从系统的一处移到另一处，用来修正上游活动的下游效应或分配造成的质量平衡偏差。不能把这些代码只当显示标签；它们解释了某些记录为何不直接代表普通生产。

判断活动是否适用于研究，还需读取边界说明。`includedActivitiesStart` 描述起点；对 `type=2`，起点始终为从摇篮开始并包括全部上游活动。对单元过程，它可描述原材料接收或服务所需投入等起点。`includedActivitiesEnd` 不只是终点名称，还说明活动中包含的步骤及有意排除的活动或输入，最后交代最后一道活动或交付点。例如，作为服务的农药施用可排除农药本身，从而适用于不同有效成分。`generalComment` 容纳无法放入更专门字段的一般说明和引用，信息应足以帮助判断数据集适用性。它是 `TTextAndImage`，读取时应考虑文本、图片与变量及其顺序；通用说明写 `imageUri`，但本版 XSD 的实际图像元素名是 `imageUrl`，这是文档命名不一致，解析时须对照实际模式。`synonym` 提供同义词，允许 `0..n` 个条目，每个最长 80 个字符，且同一 `xml:lang` 可以出现多条。`tag` 是用于筛选、分组和搜索的开放关键词列表；不在 `validTags` 主文件中的标签应产生提示信息，而不是语义验证错误。`datasetIcon` 是图标的 URI，可用于快速识别、品牌或公司徽标；图标存放于本地或网络服务器，通过 Http 获取，并非嵌入数据集本身。

若存在 `parentActivityId`，应先解析继承，再把当前文件当成完整记录取数。它引用父活动数据集；`parentActivityContextId` 指定父活动所在上下文，省略时使用当前数据集上下文。子活动承接父字段，只存储相对父活动的变化。空字段表示沿用父值，填写的新内容覆盖父值；字符串中的 `{{PARENTTEXT}}` 把父文本插入指定位置。`TTextAndImage` 还支持文本变量 `{{text_variables}}` 和引用形式 `{{variablename}}`，允许子活动重新定义变量而保留其他父文本。具有数学关系的数量字段可在 `mathematicalRelation` 中使用 `PARENTVALUE`，例如原说明中的 `PARENTVALUE*0.5` 将父数量减半。因而，子文件未写某字段不能直接解释为零值或不存在。原说明指出，子数据集不能按完整 EcoSpold02 活动的数据模式要求直接验证；官方包同时提供子模式。这里还要区分元素与类型的命名空间：根元素 `ecoSpold` 及其外层容器 `activityDataset`、`childActivityDataset` 都属于 `http://www.EcoInvent.org/EcoSpold02`；其中 `childActivityDataset` 使用属于 `http://www.EcoInvent.org/EcoSpold02Child` 的 `TActivityDataset` 类型，其内部 `activityDescription` 等元素也属于这个子命名空间。读取和校验应区分完整记录与差异记录，并按元素实际命名空间选择路径。

属性 `inheritanceDepth` 默认是 `0`。原说明将其定义为当前数据集的父数据集最大数量，又给出 `0` 为非子数据集、`1` 为地理子数据集、`2` 为时间子数据集、`3` 为宏观经济情景子数据集的解释。层数和类型的对应关系仍需依据继承专门规范确认；不能仅凭这一数值自行构造父链，实际父对象仍由 `parentActivityId` 引用。

能源和分配信息也属于活动描述。`energyValues` 默认 `0`，表示未指定；`1` 表示净值，即低位热值；`2` 表示总值，即高位热值。它声明能源数值的口径，不是另一笔能源交换。`masterAllocationPropertyId` 引用全数据集默认分配属性，`masterAllocationPropertyContextId` 指定该属性所属上下文，省略时沿用数据集上下文；某交换可通过自己的 `specificAllocationPropertyId` 覆盖这一默认属性。按原说明，某输出的分配因子等于该输出的 `TProperty` 值乘输出数量，再除以所有输出相应乘积的总和。`allocationComment` 解释分配程序和选择该属性的理由，也可说明采用物理、经济等不同参数却得到相同分配因子的情况。若子数据集要删除默认分配属性的引用，必须把 `masterAllocationPropertyIdOverwrittenByChild` 设为 `true`；单纯不写引用会被解释为保留父值。

#### 用分类定位行业，不把名称当作主数据标识 <a href="#read-TClassification" id="read-TClassification"></a>

活动描述中的 `classification` 可重复出现，每一项采用 `TClassification`，把一个分类体系与其中的类别配对。元素 `classificationSystem` 给出体系名称，如原文示例 `ISIC Rev. 4`；`classificationValue` 给出活动在该体系中所属的类别。它们便于展示和筛选，但机器解析的主数据引用是属性 `classificationId`，指向有效分类列表中的分类值。`classificationContextId` 指定这个分类所属上下文，省略时采用数据集自身的上下文。取数时应逐项保留体系、类别和引用标识，不能假定只有一个分类，也不能将不同体系中看起来相同的类别文本合并为同一条主数据。

这里有一处需明确交代的原文差异：字段说明把 `classificationSystem` 和 `classificationValue` 称为可选纯文本值，而本版完整数据 XSD 将两个元素设为至少出现一次，官方 HTML 表格也标为必填。阅读已有文本与校验文件结构是不同操作；校验当前完整数据时应按所用 XSD 执行，不能根据说明中的“可选”自行删除元素。子数据集另有差异模式，其规则还需结合继承处理。

#### 地理信息描述适用范围，也界定市场范围 <a href="#read-TGeography" id="read-TGeography"></a>

`activityDescription/geography` 采用 `TGeography`。属性 `geographyId` 引用有效地理位置主数据中的详细定义，`geographyContextId` 指定该引用的上下文，省略时使用数据集自身的上下文。元素 `shortname` 是这一地理位置的描述性简称，可用于报告和筛选；它不是替代 UUID 的主数据键。元素 `comment` 提供进一步的地理解释，采用 `TTextAndImage`，可说明边界划分的性质、非行政区域的界定方式以及市场边界的依据。

不要把 geography 一律理解为国家。它可表示活动的点位置、移动活动的线，或包含多个具体活动地点的分布式活动及生产组合的区域。对于市场和消费组合，它描述限制跨界进出口的市场边界。读取时可先提取 `shortname` 了解地理范围，再用 `geographyId` 及对应上下文解析主数据，最后结合 `comment` 判断该范围是否与研究对象一致；地理简称本身并不交代全部边界含义。

#### 技术水平要结合有效年份和地点阅读 <a href="#read-TTechnology" id="read-TTechnology"></a>

`activityDescription/technology` 采用 `TTechnology`。属性 `technologyLevel` 是粗粒度的技术分类，默认值为 `3`，可用于建模时选择特定技术水平的过程。值 `0` 为未指定，适用于没有技术水平的市场活动；`1` 为新兴技术，在某些方面技术性能优于现代技术，但纯按经济考虑投资时尚未成为最常安装的选择；`2` 为现代技术，是纯按经济考虑新增产能时采用的、竞争力最强的技术；`3` 为当前技术，介于现代与旧有之间；`4` 为旧有技术，是纯按经济考虑退役时正在退出使用、竞争力最低的技术；`5` 为过时技术，已经不再使用。

这些标签不是设备年龄。技术即使已存在很久，只要仍最有竞争力，就可以标为现代；技术即使出现较晚，也可能很快被更有竞争力的技术取代而标为旧有。同一技术可随数据有效年份变化等级，也可在同一年、不同地区具有不同等级。因此，读取 `technologyLevel` 时应同时读取时间和地理信息，不能将某地区某年的等级外推为全球永久属性。

元素 `comment` 采用 `TTextAndImage`，说明技术的性质、特征及单元过程的技术属性。若活动包含多个子活动，也应描述对应技术，并使用专业工艺名称。提取这段说明，是理解技术差异及决定是否采用数据的步骤；仅用技术等级整数无法替代工艺文档。

#### 时间段与整段有效性要分开判断 <a href="#read-TTimePeriod" id="read-TTimePeriod"></a>

`activityDescription/timePeriod` 采用 `TTimePeriod`。属性 `startDate` 和 `endDate` 是数据集有效时间段的完整日期，采用年-月-日；它们与文件创建、编辑和导出时间不同。属性 `isDataValidForEntirePeriod` 说明该活动的基本流交换和中间交换是否对所列整个时间段都有效，不能仅根据起止日期推定整段有效。

当 `isDataValidForEntirePeriod` 不为真时，可在元素 `comment` 中解释。这个 `TTextAndImage` 字段也可说明单元过程的时间相关性，例如较早数据是否仍适用于当前活动；还可说明为什么数据不覆盖整个期间、实际在哪些较短期间内有效。取数时应将起止日期、整段有效性标记和这段说明一并保存，否则会丢失日期区间内的重要限定。

#### 情景是主数据引用，也可能是子数据集的变化依据 <a href="#read-TMacroEconomicScenario" id="read-TMacroEconomicScenario"></a>

`activityDescription/macroEconomicScenario` 采用 `TMacroEconomicScenario`。属性 `macroEconomicScenarioId` 指向有效情景列表中的宏观经济情景；`macroEconomicScenarioContextId` 指定该情景主数据所属上下文，省略时使用数据集自身的上下文。元素 `name` 是情景名称，供人阅读；不能用它替换情景 UUID 做唯一连接。

元素 `comment` 说明宏观经济子数据集与父数据集默认情景的差异。它是 `TString32000` 文本，而不是混合图片的 `TTextAndImage`。读取情景时，可先保留名称和引用，再结合活动的父数据集关系阅读这段差异说明；仅从名称无法知道哪些输入、输出或其他条件相对于父情景发生了变化。

### 4.2 交换数据：从清单中读取数量和结果

#### 先读交换的共同结构 <a href="#read-TCustomExchange" id="read-TCustomExchange"></a>

一个活动的数据不只是一个总数，而是一组说明“交换了什么、交换多少、用什么单位表示”的记录。`TCustomExchange` 定义中间交换与基本流交换共有的字段；`TIntermediateExchange` 和 `TElementaryExchange` 在它的基础上增加各自的信息。因此，读到具体交换时，既要读取该交换类型的专用字段，也要读取这些共同字段。下文用代码标出实际 XML 名称：属性写在元素的开始标签中，名称、说明等内容则由子元素承载。

识别一条记录时，先区分名称与标识。必需的 `name` 是交换名称，必需的 `id` 是这条交换实例的 UUID。它不是产品的 `intermediateExchangeId`，也不是基本流主数据的 `elementaryExchangeId`：同一数据集可以有多条交换引用同一个主数据条目，因此按产品或基本流标识去重会丢失交换实例。随后读取必需的 `amount`，它以 `TFloatNumber` 表示这条交换的数量；必需的 `unitId` 引用该数量的单位，必需的 `unitName` 提供便于阅读的单位名称。可选的 `unitContextId` 指明单位主数据所属上下文，省略时使用数据集自身的上下文。取数时应把交换实例标识、数量、单位标识及其上下文一起保留，以免把不同单位或不同主数据空间的同名记录合并。

`name`、`unitName` 和可选的 `comment` 可以用多种语言表达；`comment` 为这条交换提供一般说明。读取文本时，应根据 `xml:lang` 选择需要的语言，而不是把多个语言版本串成一个名称。可重复的 `synonym` 是同义词，每条最多 80 个字符，可有 0..n 条；与普通多语言字符串不同，同义词允许同一个 `xml:lang` 对应多个条目。可重复的 `tag` 则是供筛选、分组和搜索使用的开放关键词。原说明写明，`validTags` 主文件中找不到某个标签时，语义验证应提示信息，而不应把它当成错误。`casNumber` 是可选的化学品 CAS 编号；这份格式说明给出的形式为 `000000-00-0`，并允许第一组数字不足六位。CAS 编号帮助识别化学物质，但并不能替代交换实例标识、单位或基本流区室信息。

一些交换数量还带有计算关系。可选的 `variableName` 为交换数量提供公式中的简称；文档要求以字母 a-z 开头，可含字母、数字和下划线，且不区分大小写，例如 `calorific_Value` 与 `Calorific_value` 等同。可选的 `mathematicalRelation` 通过变量名或 `REF` 函数引用流、参数和属性，在给定一组变量值后，其计算结果写入 `amount`。当 `isCalculatedAmount` 为 `true` 时，`amount` 是 `mathematicalRelation` 或 `transferCoefficient` 的计算值；共同交换类型的 XSD 将这一标记默认设为 `false`。解析文件可以读取已保存的数量与公式，但重新求值需要支持对应公式语言，不能把公式字符串本身当成数值。

可重复的 `transferCoefficient` 将特定输入与特定输出关联，表示该输入中流向该输出的份额；按其专用结构说明，系数应乘以被引用交换的数量。可选的 `uncertainty` 用分布函数、参数和／或数据质量谱系信息描述交换数量的不确定性。可重复的 `property` 描述交换的干质量、含水率、价格或特定元素和物质的含量。这三类字段都是具有内部结构的元素，读数时不能只提取其标签文字，也不能把属性值、不确定性参数或转移系数直接相加到交换数量中。

可选的 `sourceId` 指向有效来源，`sourceContextId` 指明来源所属上下文，省略时使用数据集上下文。`sourceYear` 记录出版或交流年份；网站来源记录最后访问年份。`sourceFirstAuthor` 用姓和名字缩写记录第一作者，例如 Einstein A.；在现场测量、口头交流、个人书面交流和问卷调查这几类来源中，即 `sourceType` 为 4、5、6、7 时，记录提供信息的人员。`pageNumbers` 给出文章或较大型出版物中实际取数的页码。这组字段与数量一同读取，才能追溯某条交换的依据；`sourceYear` 不等于活动数据的有效年份。

若交换有独立的分配设置，`specificAllocationPropertyId` 指定分配所用属性，并覆盖数据集层面由 `masterAllocationPropertyId` 定义的默认设置；`specificAllocationPropertyContextId` 指明该属性所属上下文，省略时使用数据集上下文。这些字段说明应使用哪项属性，不能单凭它们自行构造一套新的分配算法。继承时还要读取 `sourceIdOverwrittenByChild` 与 `specificAllocationPropertyIdOverwrittenByChild`：子数据集要移除对应的主数据引用，必须把相应标记设为 `true`；否则，引用不再出现仍可能被解释为“保留父数据集的值”，不能据此判断它已被清空。

#### 中间交换如何连接产品与供应者 <a href="#read-TIntermediateExchange" id="read-TIntermediateExchange"></a>

`TIntermediateExchange` 表示单元过程中的产品、服务或废物输入与输出，连接活动与技术圈。它继承共同交换字段，因此一条记录既有交换实例的 `id` 和数量 `amount`，又有引用产品主数据的 `intermediateExchangeId`。后者为必需 UUID，回答“是哪一种中间产品”；可选的 `intermediateExchangeContextId` 指明产品主数据上下文，省略时使用数据集自身的上下文。产品名称相同，不等于实例相同，也不等于供应活动相同。

流向由 `inputGroup` 与 `outputGroup` 表达，XSD 使用二选一结构，每条中间交换只应具有其中一个。输入分组的 1 表示材料／燃料，2 表示电力／热，3 表示服务，5 表示未进一步指定的来自技术圈的流。输出分组的 0 表示参考产品，2 表示副产品，3 表示待处理材料，5 表示存量增加。读参考输出时，应识别 `outputGroup` 为 0 的记录，而不是按名称猜测或挑数值最大的输出。分组说明流向和角色，`amount` 的正负则是另一个维度；不能把所有正数都当输出、负数都当输入，也不能在读文件时不加区分地取绝对值。

参考输出提供理解交换数量的基准，但原始单元过程的参考数量不一定为 1。提取输入和排放后，若研究需要按单位参考产品表达，应先明确所选参考输出、它的数量和单位，以及所用系统模型和已经完成的分配状态，再按适用方法对相关数量作一致缩放。XML 读取本身不自动执行这一归一化；多输出记录也不能仅靠除以任意一个输出量，就当作已经完成产品间分配的结果。

供应者由可选的 `activityLinkId` 显式指定，它是活动链接，不能用本条交换的 `id` 或产品的 `intermediateExchangeId` 代替。`activityLinkContextId` 指明活动链接所属上下文，省略时使用数据集上下文；`activityLinkIdOverwrittenByChild` 则允许子数据集明确移除继承的链接，需设为 `true`，否则仍会保留父值。原说明写明，如果 `activityLinkId` 为空，供应活动由使用本活动地理和时间信息的链接规则确定。因此，空链接不代表没有供应者，更不能自行任选一个同名活动作为供应者。原表还给出“引用另一活动数据集的字段 105”的提示，但该数字在活动部分对应 `activityNameId`，而 XSD 将 `activityLinkId` 声明为 `TActivityIndexEntry` 引用；实现活动匹配时应核对活动索引，不能把这条提示当成交换实例、产品或活动名称标识可以互换的依据。

与每条交换的数量不同，可选的 `productionVolumeAmount` 表示按年计的产品产量，单位与该交换一致。它不是当前参考输出数量，也不是把清单归一化到单位产品时可直接使用的分母。`productionVolumeVariableName` 给产量提供公式简称，命名规则同样是字母 a-z 开头、允许字母数字下划线且不区分大小写。`productionVolumeMathematicalRelation` 通过变量名或 `REF` 引用流、参数和属性；这里有一项已记录的原文疑点：该字段说明把公式结果的目标写成 `amount`，而 XSD 单独定义了产量字段 `productionVolumeAmount`。教程保留这一差异，不根据这段说明把产量公式值写入普通交换数量；需要重新求值时，应确认具体软件的目标字段。

产量有一组独立的来源说明。`productionVolumeSourceId` 引用产量依据的有效来源，`productionVolumeSourceContextId` 指明其上下文，省略时使用数据集上下文。`productionVolumeSourceIdOverwrittenByChild` 设为 `true`，才明确表示在子数据集中移除该来源引用；缺少引用本身仍可能意味着继承父值。`productionVolumeSourceYear` 表示出版、交流或网站最后访问年份；`productionVolumeSourceFirstAuthor` 表示第一作者或现场测量、口头交流、个人书面交流及问卷来源的提供人员，规则对应 `sourceType` 为 4、5、6、7 的情况。可多语言填写的 `productionVolumeComment` 解释产量来源、假设和计算，可选的 `productionVolumeUncertainty` 则用分布及其参数和／或谱系信息记录产量不确定性。最后，可重复的 `classification` 通过分类配对描述产品所属类别。提取产量时应连同这一组依据保存，而不是拿交换的一般来源记录代替产量来源。

#### 基本流交换记录与环境的往来 <a href="#read-TElementaryExchange" id="read-TElementaryExchange"></a>

`TElementaryExchange` 表示单元过程与环境之间的基本流输入或输出，同样继承 `TCustomExchange` 的实例标识、数量、单位、来源和不确定性等共同字段。与中间产品的识别方式相对应，必需的 `elementaryExchangeId` 引用基本流的主数据条目，而可选的 `elementaryExchangeContextId` 指明该主数据所属上下文，省略时使用数据集自身上下文。取数时应保留这个基本流标识，同时保留交换实例 `id`；一个用于识别流，另一个用于识别本数据集中的具体记录。

基本流的分组值与中间交换不同：`inputGroup` 的有效值 4 表示来自环境，`outputGroup` 的有效值 4 表示流向环境。两者仍然只能选择一个，不能因为中间交换有材料、能源或参考产品分组，就把同一套编号移用于基本流。来自环境的资源获取、流向环境的释放，都要结合分组理解；数量的符号不能替代分组判定，也不应在未理解模型含义之前被删除。

必需的 `compartment` 提供区室与子区室的配对信息，由 `TCompartment` 的内部结构表达。原说明中的 `validCompartments` 所引用 XML 文档定义给定语言下有效的区室／子区室配对。可选的 `formula` 可补充化学式，例如分子式，但它不代替基本流主数据或区室。读取环境清单时，应同时取出流标识、名称、方向、数量、单位以及区室配对；不能仅按化学名称把不同区室的流合为一个“总排放”，然后假设可以直接使用同一个表征因子。

#### 参数为交换公式提供可追溯的数值 <a href="#read-TParameter" id="read-TParameter"></a>

`TParameter` 保存供公式使用的数据集参数。参数不是物质输入或排放记录，即使也具有 `amount`，也不能混入基本流或中间交换的清单总量。必需的 `name` 是可多语言填写的描述性名称，必需的 `parameterId` 引用有效参数主数据；可选的 `parameterContextId` 指明参数所属上下文，省略时使用数据集上下文。必需的 `amount` 保存参数当前数值，是阅读公式时可用的已保存值，而非参数名称或 UUID。

参数的单位信息均为可选：`unitId` 引用参数数值的单位，`unitContextId` 指明单位上下文，省略时使用数据集上下文，`unitName` 是可多语言填写的单位名称。未提供单位时，不应自动补成质量单位，也不能仅凭字段名认定参数无量纲；应结合参数主数据和用途理解。可选的多语言 `comment` 提供针对该参数的一般说明，可选的 `uncertainty` 描述参数数值的不确定性，读参数值时可将这些解释和质量信息一起保存。

`variableName` 是可选的公式变量名。官方原说明在这一参数字段下沿用了“交换简称”和“交换量”的措辞，这项疑点已记录；从 `TParameter` 的用途看，不能据此认定它只能引用交换。文档列出的规则仍是以字母 a-z 开头，可含字母、数字和下划线，并不区分大小写；`calorific_Value` 与 `Calorific_value` 为相同变量名。另一项已记录差异是，`TVariableName` 的 XSD 限制为最大长度 40，并使用 `\w\S*` 模式，并未直接表达与这些文字规则完全等价的限制。XSD 验证通过，不意味着已经满足公式解析器或语义验证的全部命名要求。

可选的 `mathematicalRelation` 通过变量名或 `REF` 函数引用流、参数和属性的值，在给定变量值后，将结果写入参数自身的 `amount`。可选的 `isCalculatedAmount` 为 `true` 时，说明该数值由该数学关系计算得到；这一参数标记的 XSD 没有声明默认值，不能套用共同交换类型的默认设置。阅读现有文件时应区分直接记录的当前数值与其计算依据，只有在正确理解公式语言和依赖关系后，才重新计算参数。

#### 影响评价结果不是一条环境排放 <a href="#read-TImpactIndicatorResult" id="read-TImpactIndicatorResult"></a>

`TImpactIndicatorResult` 保存已经计算出的影响指标结果。它的必需字段 `amount` 是指标值，不是某种污染物的排放量，也不是未表征的资源消耗量；即使字段名与交换数量相同，读数含义也由所在类型决定。提取 LCIA 结果时，需要同时保留方法、类别、指标和单位，不能只取出一列数值，也不能把这些结果与基本流交换相加。

一条结果包含三层必需的主数据标识。`impactMethodId` 引用影响评价方法；`impactCategoryId` 按 XSD 引用方法中的影响类别；`impactIndicatorId` 引用具体影响指标。它们分别回答采用什么方法、结果属于什么类别、使用什么指标。这些 ID 均为 UUID，不能因显示名称近似而互相替代。原表字段 1820 的说明写作“对影响类别所属方法的引用”，但其 XSD 引用对象为 `TImpactMethodCategory`，与 `impactMethodId` 的 `TImpactMethod` 不同；这项源文矛盾已在审阅中记录，此处明确区分实际的类别引用与方法引用，没有改写原表译文。

可选的 `impactMethodContextId`、`impactCategoryContextId` 和 `impactIndicatorContextId` 分别指定方法、类别和指标主数据所在上下文，任何一个省略时，都使用数据集自身的上下文。结果也包含便于阅读的必需多语言文本：`impactMethodName` 为方法名称，`impactCategoryName` 为类别名称，`name` 为指标名称，`unitName` 为指标值的单位名称。选择语言时应按 `xml:lang` 读取这些名称，不应把多语言版本当成多条独立结果。

因此，读 LCIA 结果的一条可靠路径，是先用方法、类别和指标的标识及上下文确定这条结果的身份，再把 `amount` 与 `unitName` 配对，最后核对活动、产品和系统模型等外部背景及参考数量基准。这个类型自身没有交换的 `inputGroup`、`outputGroup`，也没有为结果另列 `unitId`；不能照搬读取排放交换的字段路径。不同方法、不同指标、不同单位或不同参考基准的结果，应先确认可比性，不能只因中文名称相似就合并或比较。

### 4.3 复合类型：解释区室、属性、不确定性和文本

#### 区室配对决定环境流的具体位置 <a href="#read-TCompartment" id="read-TCompartment"></a>

`TCompartment` 用来说明一条基本流属于哪一组区室与子区室。“区室”既可表达环境接收介质，也可用于自然资源分类，因此本文采用已交叉审阅确定的“区室／子区室”术语。内部的 `compartment` 和 `subcompartment` 是必需的多语言名称，提供所引用配对的纯文本表示；前者是区室名，后者是更细的子区室名。原表分别将它们追溯到字段 5315 和 5325，不应把这些跨表编号误读成该数据集里的交换编号。

必需的 `subcompartmentId` 是配对引用的 UUID，必须在有效区室清单中定义，原表指向字段 5330。可选的 `subcompartmentContextId` 指明子区室所属上下文，省略时使用数据集自身上下文。因而读数时应把配对标识及上下文与显示名称一起保存：显示名称有助于理解，主数据引用用于一致匹配。外层基本流的 `compartment` 元素与内层区室名称的 `compartment` 元素同名，但处于不同结构位置；提取时应按层级识别，避免把整个配对结构当成一段普通文字。

#### 不确定性：先辨认分布，再读取它的参数 <a href="#read-TUncertainty" id="read-TUncertainty"></a>

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

#### 交换属性：把产品特征与交换数量分开理解 <a href="#read-TProperty" id="read-TProperty"></a>

`TProperty` 附在交换的 `property` 元素中，描述干质量、含水率、价格、元素或物质含量等特征。中间交换和基本流交换都继承通用交换结构，因此都可具有这些属性。阅读一条属性时，首先用 `propertyId` 识别它引用的属性主数据，再读描述性文本 `name`；`propertyContextId` 指定该属性主数据所属的上下文，省略时采用数据集自身的上下文。UUID 引用和上下文确定的是属性身份，名称帮助人理解身份，不能仅靠同名文字认定两个属性一定相同。

属性的数值存于自身的 `amount`，其单位由 `unitId` 引用，`unitName` 提供单位名称，`unitContextId` 指明单位主数据上下文，省略时同样采用数据集上下文。这里的 `amount` 并不等于外层交换的 `amount`，也不保证与它具有相同单位；价格、含水率和干质量描述的量并不相同。取数时，应把属性定义、数值及单位一起读取，并核查其计量或归一化基准，不能直接把属性量加到投入输出清单中。`isDefiningValue` 为 true 时，属性值属于交换定义的一部分，与交换量之间具有不能针对不同数据集中个别实例改变的固定关系；它既不表示两个数值相等，也不是允许任意按比例改写所有属性的开关。

若属性不是手工指定的值，`mathematicalRelation` 可通过变量名或 `REF` 函数引用流、参数和属性的数值，计算结果写入本属性的 `amount`；`isCalculatedAmount` 为 true 表示这个数值来自该数学关系。`variableName` 则给本属性量一个可在数学关系中引用的名字。文档要求变量名以字母 a-z 开头，可以包含字母、数字和下划线，并且不区分大小写，例如 `calorific_Value` 与 `Calorific_value` 等同。所附 XSD 的 `TVariableName` 类型限定长度最多 40，并采用正则 `\w\S*`，它没有直接表达与文字规则完全等价的约束，因此不能仅凭 XSD 验证通过就认定变量名满足所有公式语言规则。读取已计算数值与重算公式是不同工作；字段定义本身不足以替代公式解析、引用解析和继承处理。

`uncertainty` 描述的是该属性值的不确定性，仍须按所选分布解释，而不是默认套用外层交换的不确定性。`sourceId` 引用记录该属性的有效来源或出版物，`sourceContextId` 指定来源上下文，省略时采用数据集上下文。对子数据集，如果要移除继承的来源引用，应将 `sourceIdOverwrittenByChild` 设为 true；仅让引用消失会按原文规则被解释为保留父值。`sourceYear` 记录出版或交流年份，网站来源记录最后访问；`sourceFirstAuthor` 通常填写第一作者的姓氏和名字缩写，例如 Einstein A.，而来源类型 `sourceType` 为 4、5、6、7 的现场测量、口头交流、个人书面交流或问卷调查，填写提供信息的人。最后，`comment` 可以补充该交换中这项具体属性的假设、说明和限制，使数值能够追溯到其证据。

#### 转移系数：追踪特定投入对特定输出的贡献 <a href="#read-TTransferCoefficient" id="read-TTransferCoefficient"></a>

转移系数将一项特定投入与一项特定输出关联，记录该投入对该输出的贡献份额，用于根据投入量计算相应的输出贡献。在 XSD 中，`transferCoefficient` 定义在 `TCustomExchange` 内，因此中间交换和基本流交换都可以通过继承包含它，不能把它限制为只供中间产品使用。阅读时应同时保留容纳系数的交换和被引用交换的身份，才能知道所描述的是哪一条投入输出关系。

`exchangeId` 引用的是某个具体交换的 UUID，即交换实例的 `id`，不是产品主数据的 `intermediateExchangeId` 或基本流主数据的 `elementaryExchangeId`。同一主数据条目可能在同一个数据集中被多项交换引用，所以两种身份不能混用。系数自身的 `amount` 是转移系数数值；原说明要求将它与所引用交换的数量相乘，以得到该系数对应的数量贡献。这个 `amount` 不是另一笔投入量，也不是不加区分地分配整个过程环境影响的因子。不能仅凭一个系数的存在，就推出完整质量平衡、输出总量或通用过程计算算法。

`mathematicalRelation` 可以通过变量名或 `REF` 引用流、参数和属性来计算系数，结果写入这个系数的 `amount`；`isCalculatedAmount` 为 true 时表示该值是数学关系的计算结果。可选的 `uncertainty` 描述系数数值的不确定性，应与被引用交换数量的不确定性区分。取数时，可以读取已存系数与它的引用对象；若要进一步重新计算，必须另行处理引用、公式和不确定性，不能把它们合并成一个未经格式说明支持的计算规则。

证据链由 `sourceId`、`sourceContextId`、`sourceYear` 和 `sourceFirstAuthor` 组成。`sourceId` 指向有效来源，原选项说明将其关联到 `modellingAndValidation` 部分定义的来源；`sourceContextId` 指定来源的上下文，省略时使用数据集上下文；`sourceYear` 是出版或交流年份，网站记录最后访问；`sourceFirstAuthor` 是第一作者姓氏和名字缩写，现场测量、口头交流、个人书面交流和问卷调查，即 `sourceType` 为 4、5、6、7 时，则填写提供信息的人员。在子数据集中移除继承的来源引用，需要将 `sourceIdOverwrittenByChild` 设为 true，否则移除会被解释为保留父值。`comment` 用于每个系数的补充说明，读取时应与该系数而非其他交换的说明关联。

#### 文本和图像：按顺序组织说明，用文本变量继承局部内容 <a href="#read-TTextAndImage" id="read-TTextAndImage"></a>

`TTextAndImage` 是一般说明、技术描述和审查详细意见等字段采用的复合结构。实际 XSD 将它定义为可以多次出现的 `xsd:choice`，其中可交错选择 `text`、`imageUrl` 和 `variable`；这与不确定性中恰选一种分布的选择组不同。它可以包含多个文本和图像片段，而不是一次性固定为“一个文本加一张图”。原英文说明多次使用 `imageUri`，但所附 XSD 的实际图像元素名是 `imageUrl`。教程取数应按实际元素名识别，源文这一不一致仍在审校注记中保留，不能据说明文字生成一个并不存在的 `imageUri` 元素。

`text` 是描述当前部分的自由文本，使用 `TIndexedString32000` 类型，其 `index` 属性指定显示顺序。`imageUrl` 保存图像 URI，也有必填的整数 `index`，用来把图像插入文本之间。还原正文时，必须结合这些顺序值，而不是分别收集全部文本和全部图片后拼接。多语言文本还可能带有 `xml:lang`，取数时应保存语言信息，不能将不同语言片段无条件混成一篇说明。具体位置上的索引唯一性和其他条件，应以包含该字段的 XSD 声明为准。

`variable` 则是 `TNamedString32000` 类型的文本变量定义：其必填 `name` 属性给出变量名，元素文本给出变量值，正文可以通过 `{{variablename}}` 引用它。子活动数据集可以重新定义父文本中的变量值，同时保持其余父文本不变；这是修改继承说明中局部内容的机制。它与交换、属性或参数的数学 `variableName` 不同，也不是 `mathematicalRelation` 的数值公式参数。读取文本变量不意味着要运行算术求值；同样，`variable` 没有文本和图像所用的 `index` 属性，不能照搬这两类片段的排序方式处理它。

### 4.4 建模与审查：判断结果的依据

#### 代表性：理解数据代表的总体，以及样本如何形成 <a href="#read-TRepresentativeness" id="read-TRepresentativeness"></a>

`representativeness` 位于 `modellingAndValidation` 中，采用 `TRepresentativeness` 类型，记录数据集的代表性和数据如何采样或计算。它帮助读者判断数据能否服务于研究中的地区、技术和时间条件，而不是为每项交换提供一个新的数量。首先，`systemModelId` 引用所用系统模型，`systemModelContextId` 指定该模型的上下文，省略时采用数据集自身的上下文；`systemModelName` 是该引用的纯文本名称。这些信息说明活动数据集如何链接成产品系统。原文举出的 `undefined`、`attributional, average current suppliers, revenue allocation` 和 `consequential, small-scale, long-term decisions` 是该历史格式说明中的模型描述，不能未经核对就视为当前全部系统模型名称或完整清单。在正常 XSD 中，只要此可选结构出现，模型引用和模型名称便是其内部必填项。

`percent` 表示所采样数据占活动拟代表总体的百分比。该总体由地理区域、技术和时间范围共同确定，因此读取百分比之前，要先知道它针对的是哪个总体；它不是这个活动对产品系统的贡献率，也不是供应市场的份额。原表和 XSD 都将最大值规定为 100，但未填写这一可选属性，不代表覆盖比例为零或百分之百。

`samplingProcedure` 描述量化交换所用的采样和计算程序，应说明某些基本流交换或中间交换是否采用不同于一般程序的做法，以及组合不同采样程序可能产生的问题。这里有一个需要对照模式的源文疑点：英文说明随后混入了文本和图像字段的通用描述，但实际 XSD 把 `samplingProcedure` 定义为 `TString32000` 多语言文本，而不是 `TTextAndImage`。读取它应保留文本和语言，不应因为这段通用说明就尝试读取嵌套的 `text`、`imageUrl` 或 `variable`。

`extrapolations` 记录数据从其他时间、其他地理区域或其他技术外推而来的情况，以及外推如何实施。说明应交代单个交换是否采用不同的外推方法；如果把一个国家运行活动的数据用于另一个国家，可以在这里注明原始代表性，并记录外推引起的均值变化。读取这段内容后，才能把样本覆盖、原始来源和当前适用范围联系起来；不能仅因模型名称或地区代码符合要求，就跳过采样及外推说明。

#### 审查记录：把意见、人员和所审版本对应起来 <a href="#read-TReview" id="read-TReview"></a>

`review` 位于 `modellingAndValidation` 中，采用 `TReview` 类型，记录开展鉴定性评审的人员、主要结果、结论和建议。父级允许多个 `review`，因此一份数据集可以有多位评审者或多条审查记录；读取时不能只取第一条便覆盖其余意见。另一方面，一条记录包含的姓名、日期和意见只证明它记录了一次评审，并不自动代表整个数据库已获官方认证。

每条评审由 `reviewerId` 引用人员主数据，原表将它对应到人员字段 3610；`reviewerContextId` 指定人员上下文，省略时采用数据集自身的上下文。`reviewerName` 记录名字和姓氏，`reviewerEmail` 记录完整电子邮件地址，`reviewDate` 是验证或评审日期。这些信息应共同保留，才能将意见对应到具体评审者及其时间，而不应只凭姓名文本匹配人员身份。

审查所针对的数据集版本由 `reviewedMajorRelease`、`reviewedMinorRelease`、`reviewedMajorRevision` 和 `reviewedMinorRevision` 四个整数属性分别记录，依次对应文件属性中的字段 3800、3805、3810、3815，即主发布、次发布、主修订和次修订部分。它们不是审查记录自身的编号，也不能只保留前两个数字。阅读时应把四部分版本与当前文件的版本信息对照：如果记录针对较早版本，就不能把其意见不加判断地解释为对当前修改后内容的审查结论。正常 XSD 中，这四项版本、评审者引用、姓名、邮件及日期在一条出现的 `review` 内均必填；子数据集需另按其对应模式判断。

详细意见存于可选的 `details`，它使用 `TTextAndImage`，因此可以按 `index` 组织文本与图像，并使用 `variable` 文本变量在继承数据集中改写局部内容。这里同样应以实际的 `imageUrl` 元素名读取，而不是原说明中混用的 `imageUri`。`otherDetails` 则是普通多语言文本，保存评审过程的进一步信息，例如数据集首次发布后补充的小幅修正。两者的结构不同，但都应与该条记录的人员和所审版本一起阅读，避免把发布后的补充说明误当成数值交换，或把历史意见移接到其他版本。

### 4.5 管理信息：保留来源和版本证据

#### 录入者说明谁编制并提交了这份记录 <a href="#read-TDataEntryBy" id="read-TDataEntryBy"></a>

在 `administrativeInformation/dataEntryBy` 中，`TDataEntryBy` 记录编制数据集并将其录入数据库的人员。属性 `personId` 引用该人员，`personContextId` 指定人员主数据所属上下文，省略时使用数据集自身的上下文。属性 `personName` 和 `personEmail` 分别存储人员的名与姓以及完整电子邮件地址；它们用于显示和联系，身份连接仍依赖人员 ID 与上下文。

属性 `isActiveAuthor` 表示这位人员是否为数据集的活跃作者，完整数据 XSD 的默认值为 `false`。这里的活跃作者是后续维护中的联系角色：其他数据提供者今后修改数据集时，将征询此人的意见。它不能仅凭姓名是否出现在文件中推断，也不等同于版权人、审核人或原始数据采集者。取数时应保留这个标记，才能区分一般录入人员与需要在后续变更中联系的作者。

#### 原始数据来源、出版物与访问限制构成另一组管理信息 <a href="#read-TDataGeneratorAndPublication" id="read-TDataGeneratorAndPublication"></a>

`administrativeInformation/dataGeneratorAndPublication` 采用 `TDataGeneratorAndPublication`。这里的属性 `personId` 识别收集、汇编或发布原始数据的数据生成者，未必与 `dataEntryBy` 的录入者相同。`personContextId` 指向其人员上下文，省略时沿用数据集上下文；`personName` 和 `personEmail` 分别记录姓名和完整邮箱。读取两个人员组时，要保留各自所属的 XML 路径，即使字段都叫 `personId`，也不能把两种角色覆盖成同一个“作者”。原说明还将数据生成者解释为应获认可的数据来源及承担主要采集工作的个人或组织；当前人员引用须与相应人员主数据匹配。

属性 `dataPublishedIn` 表示发布程度：`0` 是数据本身未在别处发布，也是默认值；`1` 是部分单元过程或子系统已发布；`2` 是数据完整发布于所引用来源。`publishedSourceId` 引用记录数据的报告或来源，`publishedSourceContextId` 指定来源上下文，省略时使用数据集自身上下文。`publishedSourceYear` 记录出版或沟通年份，对网站记录最后访问时间；原文没有限定网站条目只能写年份，实际类型为 `TBaseString30`。`publishedSourceFirstAuthor` 给出第一作者的姓和名字缩写。对于 `sourceType=4, 5, 6, 7` 的现场测量、口头沟通、个人书面沟通和问卷，它记录沟通人员。`pageNumbers` 进一步定位文章或较大出版物中的相关页码。取数时，这些字段共同构成可追溯来源，不能用一个年份或第一作者文本替代来源主数据引用。

原说明出现的旧编号也有明确对应关系：`757` 是 `publishedSourceId` 的旧 SpoldID，当前 fieldId 为 `3520`；它引用的来源 `id` 的旧 SpoldID 是 `801`，当前 fieldId 为 `3110`。这些是编号体系之间的映射，而非需要替换的 XML 名称。在子数据集中，若要删除父数据集的来源引用，必须将 `publishedSourceIdOverwrittenByChild` 设为 `true`；仅省略 `publishedSourceId` 会沿用父引用。

版权和可访问性由不同属性表达。`isCopyrightProtected` 表示是否有著作权，原说明要求对应填写 `1` 或 `0`。`accessRestrictedTo` 默认 `0`，表示无访问限制；`1` 表示只有上下文定义的许可证持有者可访问；`2` 表示这些许可证持有者只能访问 LCI 结果，不能访问单元过程原始数据，而数据库管理员仍具有完整访问权限；`3` 表示只有指定组织及数据库管理员可访问。不能把版权标记当成公开许可，也不能从文件技术上可读推断有权公开传播其中数据。

当访问限制为 `3` 时，`companyId` 引用获准使用数据集的组织或机构，`companyContextId` 指定该组织上下文，省略时使用数据集上下文；`companyCode` 是对应公司的可选代码纯文本。原说明称其为 7 字母代码，`TCompanyCode` 的说明还称应使用大写字母，但本版 XSD 的实际约束只有最长 7 个字符，没有固定长度或字母字符模式；因此，通过 XSD 并不等于已经满足这项文字约定。原文条件 `759=3` 中的 `759` 是 `accessRestrictedTo` 的旧 SpoldID，当前 fieldId 为 `3550`，因此条件应理解为访问限制类别为 `3`，不是另一项编号为 759 的当前属性。若子数据集需要移除组织引用，必须把 `companyIdOverwrittenByChild` 设为 `true`，否则仍视为保留父值。这套规则让程序能够分别处理“继承已有引用”与“明确删除引用”。

#### 区分数据库发布版本、数据集修订版本和文件时间 <a href="#read-TFileAttributes" id="read-TFileAttributes"></a>

`administrativeInformation/fileAttributes` 采用 `TFileAttributes`，描述文件整体信息。属性 `majorRelease` 和 `minorRelease` 属于发布版本：主发布号在重大更新时加一，次发布号在两次重大更新之间的每次发布时加一。原文以每两年一次为重大更新的例子，但这不是由格式规定的固定发布日程。属性 `majorRevision` 和 `minorRevision` 则区分某个数据集本身的修订，独立于数据库发布版本。因此，程序应将发布版本和数据集修订版本分别保存，而不是拼成一个失去角色区分的版本字段。

`majorRevision` 反映数据集已获接受的变更，只能随时间增加，不得手动更改。在 ecoinvent 上下文中，活动变更通过审查并加入数据库后，它增加，同时将 `minorRevision` 重置为 `1`。`minorRevision` 描述提交审查前编辑过程中的版本；数据提供者每次将修改保存到本地或作为服务器草稿保存时，它自动增加。读取一份草稿与已接受版本时，应据此理解修订状态，不能把文件较新的时间戳直接等同于已接受的内容变更。

时间属性同样需要分开。`creationTimestamp` 是数据集创建时自动生成的日期时间，`lastEditTimestamp` 是保存数据集时自动生成的日期时间；`fileTimestamp` 是当前文件创建的日期时间。前两者描述数据集的创建和编辑，后者描述文件生成，它们都不替代 `timePeriod` 的数据有效日期。`fileGenerator` 说明创建文件的程序，最好包括软件版本；`internalSchemaVersion` 说明生成数据集所依据的内部模式版本。记录这些信息，有助于判断解析环境和追踪导出来源。

属性 `defaultLanguage` 为多语言字段指定默认语言，在完整数据 XSD 中省略时为 `en`；子差异文件省略该属性时应先处理继承，不能绕过父值直接取 `en`。每个多语言字段至少应有默认语言的值。提取活动名称等多语言元素时，应先选择相应语言内容，并保留语言标识，而不是把不同语言的重复元素当成重复数据。元素 `contextName` 是上下文名称，属性 `contextId` 是数据集所面向上下文的 UUID。上下文可用于限制信息访问范围，并决定解析引用时需要哪些主数据文件；它取代旧 ecoSpold01 的 quality network，ecoinvent 质量网络对应的上下文 ID 可在 `Context.xml` 中查找。

缺少 `contextId` 时，说明将文件视为独立数据集，主数据引用不能被解析为实际主数据内容。这与缺少某个可选的 `…ContextId` 属性不同：后者通常沿用数据集上下文，但前提是这个上下文已经可知。元素 `requiredContext` 可重复出现，采用 `TRequiredContextReference`，用于列明完整读取主数据引用所需的其他上下文。真正取数前，应先识别本文件的上下文及所需上下文，再尝试连接各个名称、地点、人员、来源和属性的 UUID。

#### 解析跨上下文引用前，先核对主数据依赖 <a href="#read-TRequiredContextReference" id="read-TRequiredContextReference"></a>

每个 `requiredContext` 条目采用 `TRequiredContextReference`，说明读取文件所需的主数据上下文。属性 `requiredContextId` 引用主数据文件所属上下文，元素 `requiredContextName` 提供相应名称；属性 `requiredContextFileLocation` 是可选 URI，指向包含这一上下文主数据文件的目录。它给出的是主数据目录位置，不能直接当成某一条主数据对象的 UUID，也不应未经判断就当成单个 XML 文件路径。

这个条目也有属性 `majorRelease`、`minorRelease`、`majorRevision` 和 `minorRevision`。它们用于确保该活动所需的主数据条目在相应版本中存在，描述的是所依赖上下文的版本要求，不是当前数据集自己的版本。完整 XSD 要求主发布号与次发布号，主修订号与次修订号则为可选。读取程序需知道各上下文，并知道实际主数据文件在哪里；只有 UUID 文本而没有对应主数据文件，并不能完成引用解析。

原文另有一处结构要求与说明冲突：它称省略 `requiredContextId` 时应使用数据集自身上下文，但本版完整 XSD 把这个属性设为必填。因而，不能依据这句回退说明生成缺少该属性却宣称通过完整模式验证的文件。教程保留这项文档差异，具体适用条件需由数据方澄清；在实现当前完整模式时，应核对 `use="required"` 的实际要求。另须区分子差异模式：`EcoSpold02ChildDataTypes.xsd` 将 `requiredContextId` 及四个版本属性设为可选，也将 `requiredContextName` 设为可省略；这并不改变完整数据模式的必填要求。读取子记录时仍须结合继承及实际上下文，不能把省略值直接当成一个已经解析成功的主数据引用。

## 五、用 Python 提取成可分析的数据

理解 demo 后，可以先用很短的程序复现三个动作：按命名空间进入活动数据集，找到参考输出，再读取电力或环境交换的属性。这些例子直接处理 XML，不会求解产品系统，也不会执行公式字符串。

### 最小例子：读活动、参考产品和原始交换量

在下载了 demo 的目录运行下面代码，或把 `demo-product.spold` 改为自己的文件路径。这个短例子只演示读取一个普通活动数据集；后面的完整提取器会遍历文件中的全部普通数据集。

```python
from decimal import Decimal
import xml.etree.ElementTree as ET

ns = {"es": "http://www.EcoInvent.org/EcoSpold02"}
root = ET.parse("demo-product.spold").getroot()
dataset = root.find("es:activityDataset", ns)
if dataset is None:
    raise ValueError("需要普通 activityDataset；子数据集须先展开继承")

activity = dataset.find("es:activityDescription/es:activity", ns)
flow = dataset.find("es:flowData", ns)
if activity is None or flow is None:
    raise ValueError("缺少活动描述或 flowData")
print("活动 UUID：", activity.get("id"))

reference_rows = []
for exchange in flow.findall("es:intermediateExchange", ns):
    group_text = exchange.findtext("es:outputGroup", namespaces=ns)
    if group_text is not None and int(group_text) == 0:
        reference_rows.append(exchange)
if len(reference_rows) != 1:
    raise ValueError("请明确处理参考输出缺失或多个参考输出的情况")
reference = reference_rows[0]
reference_amount = Decimal(reference.attrib["amount"])
if not reference_amount.is_finite() or reference_amount <= 0:
    raise ValueError("这个简单比例示例需要有限且正的参考输出量")

for tag in ("intermediateExchange", "elementaryExchange"):
    for exchange in flow.findall("es:" + tag, ns):
        raw = exchange.attrib["amount"]
        quantity = Decimal(raw)
        if not quantity.is_finite():
            raise ValueError("交换量必须是有限数字")
        names = [n.text for n in exchange.findall("es:name", ns)]
        units = [n.text for n in exchange.findall("es:unitName", ns)]
        print(tag, exchange.get("id"), names, raw, units,
              "相对于一个参考单位：", quantity / reference_amount)
```

属性用 `exchange.attrib["amount"]` 读取，是为了让缺少必需数量时明确报错；对于本来可选的 `activityLinkId`，则可用 `.get("activityLinkId")` 保留缺失状态。缺失不是零，`"0"` 也不是缺失。程序用 `is None` 判断节点是否存在，不用节点的真假值，以免把无子元素的合法节点判断成不存在。

这个例子把所有语言的名称和单位都显示出来。正式筛选时，应选用明确的语言回退策略并保留原文，而不是每次只读第一个 `name`。真正识别对象时，还应优先采用 UUID、上下文、区室和单位，名称用于阅读和辅助检索。

### 完整提取器：保留关系，而不是把所有 amount 摊成一列

[下载提取脚本 extract_ecospold.py](demo/extract_ecospold.py)。它只使用 Python 标准库。将脚本与下载的 demo 放在同一目录后，可以先分别运行以下命令：

```sh
python3 extract_ecospold.py demo-product.spold --out output-upr --kind upr --language zh
python3 extract_ecospold.py demo-lcia.spold --out output-lcia --kind lcia --language zh
```

要在本次导出范围内解析供应引用，可把两个 UPR demo 放入同一个目录，再对该目录运行脚本。文件夹读取会递归收集 `.spold` 和 `.xml` 文件；建议把不同数据库版本、系统模型和导出阶段分开放置，以便解释候选链接。`--kind` 是使用者提供的来源信息；它不会把 UPR 变成 LCI，也不会凭 `type` 自动猜测下载类型。未明确时使用默认的 `unknown`，把不确定性保留在结果中。

脚本写出的 `metadata.json` 保留活动、地区、时间、模型、上下文和版本信息；`exchanges.csv` 逐行保留交换实例、产品或基本流 UUID、原量、单位、方向分组及相对于参考输出的比例。它另外导出 `parameters.csv`、`properties.csv` 和 `impacts.csv`，避免把参数值、属性值和 LCIA 指标值混成同一类数量。`uncertainty.json` 保留分布和属性结构；`supplier-links.json` 表示供应引用在当前导出范围内是否找到候选。

归一化列只是一条交换量与唯一正参考输出量的比例。原始字符串仍保留，负号仍保留；属性、参数和年度产量不会自动跟着交换量缩放。如果没有参考输出、参考输出为零或负值，或存在多个参考输出，脚本不给出一个假装明确的规范化结果。也不展开继承或计算分配。

这些 CSV 可以用于后续筛选或导入自己的数据表，但请同时带上元数据。比如比较两个文件的电力输入时，先确认两者的参考产品和单位、系统模型、地区、年份，以及数据集是普通单元过程还是累积结果。只拼接“名称、amount”两列，会丢掉这些决定数值含义的条件。

### 把问题变成明确的查询：电力、直接排放和现成影响指标

下面把“拿到自己想要的数据”落实成三个可以运行的查询。先将 `extract_ecospold.py`、`demo-product.spold`、`demo-electricity.spold` 和 `demo-lcia.spold` 放在同一目录，再[下载查询脚本 query_demo.py](demo/query_demo.py)，或将下面完整代码保存为该目录中的 `query_demo.py`。在该目录运行 `python3 query_demo.py` 即可，全部依赖都来自 Python 标准库，无需安装 pip 包。代码通过 `Path(__file__).resolve().parent` 找到同目录文件，因此保存为脚本后，也可以从其他工作目录运行它。

三个文件及代码中的所有 UUID 都是教学构造，不是 ecoinvent 的真实数据或真实对象标识。用于自己的文件时，第一步应读出其元数据和候选记录，确认活动、产品或基本流、区室、单位、系统模型和导出阶段，再从实际 XML 与对应主数据中确认 UUID 及上下文；不能把下面的教学 UUID 直接套在真实数据上。代码中的预期行数和预期数值也是针对教学文件的核对条件，改用自己的文件时，应按研究目标重新定义这些条件。

第一项查询从 `exchanges` 取电力中间交换的 `input` 行，同时匹配产品 UUID、有效上下文及单位 UUID、有效上下文。主 UPR 的参考输出为 10 kg 教学产品，所以电力原量 25 kWh 对应的 `normalized_amount` 是 2.5 kWh/kg 教学产品。代码虽然一起读取了供给电力的教学 UPR，却先以活动 UUID、上下文和唯一 `dataset_key` 限定主产品过程；供给过程自身的排放不会进入本过程的直接排放查询。`kind='upr'` 是我们根据文件来源声明的阶段，不会触发网络计算。

第二项查询取主 UPR 的化石源 CO₂ 基本流 `output`。筛选键包含流 UUID 与有效上下文、子区室 UUID 与有效上下文、单位 UUID 与有效上下文这六项身份信息，另明确要求基本流输出分组。区室的“空气”和子区室的“未指定”由这里选定的子区室主数据身份确定，名称只用于解释。有效上下文指显式引用上下文，或引用属性省略时回退到文件自身上下文；提取器已完成这一步。两个不同交换实例的原量 1.5 和 -0.1 都保持 `output`，方向由分组定义，不能因负号改成输入，也不能取绝对值。按同一完整键汇总，两行净量为 1.4 kg，归一化净量为 0.14 kg/kg 教学产品。生物源 CO₂ 有另一个流 UUID，其 0.2 kg 单独显示并排除在化石源净量之外。这里有意要求恰好两条教学记录；在真实文件中多条同键记录可能是合法的，应保留交换实例，明确汇总口径后再求和，不能无条件只拿第一条或删除重复名称。

第三项查询从 `impacts` 读取现成的模拟 LCIA 指标，逐层匹配方法、类别、指标各自的 UUID 与有效上下文，并核对 `unitName` 为 `kg CO2-eq`。这种指标字段以单位名称记录单位，不应凭空补上交换量所用的单位 UUID。教学文件中的原指标量是 13.9 kg CO2-eq，参考输出同样为 10 kg，归一化量是 1.39 kg CO2-eq/kg 教学产品。它来自文件中已存的 `impactIndicator/@amount`，不是把前面的直接 CO₂ 净量当成任意气候指标，也不是本程序算出了完整 LCIA。

三个查询都先检查结果数量：预期唯一的活动、电力或指标若缺失或多匹配，会明确报错；预期的两条化石记录也核对数量及实例 UUID。没有唯一正参考输出，或 `normalized_amount` 缺失时，代码拒绝给出归一化量。原量和归一化量使用 `Decimal`，求和保留符号，整个代码不执行公式文本。下面的数值检查用于复现教学结果；归一化只是相对于参考输出的算术比例，不能代替分配、继承展开、上游网络求解或影响评价计算。

```python
#!/usr/bin/env python3
"""查询教学构造数据；只读已存数值，不执行公式或计算产品系统。"""
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path

from extract_ecospold import extract


# 以下 UUID 全部来自随文教学 demo，不能用于筛选真实 ecoinvent 数据。
DEMO = Path(__file__).resolve().parent
CONTEXT = "f71ac544-3bc8-5c15-8ea4-072d907663f1"
PRODUCT_ACTIVITY = "19d3e06c-2a4a-545d-b368-6470e75e1a27"
LCIA_ACTIVITY = "fc37834f-30b0-5563-b8f5-16fb8683b395"
ELECTRICITY = "cf4dd220-d849-5595-92fe-1dac1fcecae7"
FOSSIL_CO2 = "f420b314-c085-57e7-ba47-5cdfa839e9a3"
BIOGENIC_CO2 = "d951f598-3f40-57c4-ba76-71df73f1096b"
AIR_UNSPECIFIED = "6bbb1a41-12de-5599-843e-cc02d4084a9a"
KG = "a4800e12-54b1-5444-a6d0-b48a59529439"
KWH = "a5533771-6995-50cd-b03c-7a2af998708e"
METHOD = "496741dc-72ec-5f95-bedb-078512fde969"
CATEGORY = "07a7bfca-c863-5fd0-a2bf-24aa3af0d959"
INDICATOR = "9ce9802d-268d-5ac0-af08-ffca6dc91aa2"


def require_count(rows, expected, label):
    if len(rows) != expected:
        raise ValueError(f"{label}：预期 {expected} 行，实际 {len(rows)} 行；请核对缺失或多匹配")
    return rows


def quantity(raw, label):
    if raw is None or str(raw).strip() == "":
        raise ValueError(f"{label}：数值缺失，不能替换为零")
    try:
        value = Decimal(raw)
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"{label}：不是有效十进制数 {raw!r}") from exc
    if not value.is_finite():
        raise ValueError(f"{label}：数值必须有限")
    return value


def normalized(row):
    if row.get("normalization_status") != "unique-positive-reference":
        raise ValueError("没有唯一正参考输出，不能使用 normalized_amount")
    return quantity(row.get("normalized_amount"), "normalized_amount")


def expect(actual, expected, label):
    if actual != Decimal(expected):
        raise ValueError(f"{label}：教学结果应为 {expected}，实际为 {actual}")


def dataset_meta(result, activity_id, label):
    matches = [m for m in result["metadata"]
               if m["activity_id"] == activity_id and m["context_id"] == CONTEXT]
    meta = require_count(matches, 1, label)[0]
    norm = meta["normalization"]
    if norm["status"] != "unique-positive-reference":
        raise ValueError(f"{label}：参考输出缺失、多条、零值或负值")
    expect(quantity(norm["reference_amount"], "参考数量"), "10", label + "参考数量")
    refs = [r for r in result["exchanges"]
            if r["dataset_key"] == meta["dataset_key"]
            and r["exchange_id"] == norm["reference_exchange_id"]]
    ref = require_count(refs, 1, "参考交换实例")[0]
    if (ref["unit_id"], ref["unit_context_id"], ref["unit_name"]) != (KG, CONTEXT, "kg"):
        raise ValueError("教学参考输出的单位应为指定上下文的 kg")
    return meta


def elementary_key(row):
    # 三个对象各用 UUID + 有效上下文；有效上下文已由提取器处理省略回退。
    return (row["flow_id"], row["flow_context_id"],
            row["subcompartment_id"], row["subcompartment_context_id"],
            row["unit_id"], row["unit_context_id"])


def main():
    upr = extract([DEMO / "demo-product.spold", DEMO / "demo-electricity.spold"],
                  language="zh", kind="upr")
    meta = dataset_meta(upr, PRODUCT_ACTIVITY, "教学产品 UPR")
    # 限定主 UPR，供应过程的直接排放不混入本过程直接排放。
    rows = [r for r in upr["exchanges"] if r["dataset_key"] == meta["dataset_key"]]
    print("教学产品基准：10 kg（唯一正参考输出）")

    electricity = [r for r in rows if r["exchange_kind"] == "intermediateExchange"
                   and r["direction"] == "input"
                   and (r["flow_id"], r["flow_context_id"], r["unit_id"], r["unit_context_id"])
                   == (ELECTRICITY, CONTEXT, KWH, CONTEXT)]
    power = require_count(electricity, 1, "指定电力输入")[0]
    expect(quantity(power["amount"], "电力原量"), "25", "电力原量")
    expect(normalized(power), "2.5", "电力归一化量")
    print(f"电力 input：{power['amount']} kWh；normalized_amount={normalized(power)} kWh/kg 教学产品")

    fossil_key = (FOSSIL_CO2, CONTEXT, AIR_UNSPECIFIED, CONTEXT, KG, CONTEXT)
    fossil = [r for r in rows if r["exchange_kind"] == "elementaryExchange"
              and r["direction"] == "output" and r["group_code"] == 4
              and elementary_key(r) == fossil_key]
    require_count(fossil, 2, "教学化石 CO₂ 输出记录")
    if len({r["exchange_id"] for r in fossil}) != 2:
        raise ValueError("化石 CO₂ 的交换实例 UUID 重复")
    amounts = [quantity(r["amount"], "化石 CO₂ 原量") for r in fossil]
    if sorted(amounts) != sorted([Decimal("1.5"), Decimal("-0.1")]):
        raise ValueError("教学化石 CO₂ 应保留 1.5 和 -0.1 两行，不改负号或方向")
    with localcontext() as ctx:
        ctx.prec = 50
        net = sum(amounts, Decimal("0"))
        net_normalized = sum((normalized(r) for r in fossil), Decimal("0"))
    expect(net, "1.4", "化石 CO₂ 净量")
    expect(net_normalized, "0.14", "化石 CO₂ 归一化净量")
    for r in fossil:
        print(f"化石 CO₂ {r['direction']} 行：amount={r['amount']} kg；normalized_amount={normalized(r)} kg/kg 教学产品")
    print(f"直接化石 CO₂ 净量：{net} kg；normalized 净量={net_normalized} kg/kg 教学产品")

    bio_key = (BIOGENIC_CO2, CONTEXT, AIR_UNSPECIFIED, CONTEXT, KG, CONTEXT)
    bio = require_count([r for r in rows if r["exchange_kind"] == "elementaryExchange"
                         and r["direction"] == "output" and elementary_key(r) == bio_key],
                        1, "教学生物源 CO₂ 输出")[0]
    expect(quantity(bio["amount"], "生物源 CO₂"), "0.2", "生物源 CO₂")
    print(f"生物源 CO₂ 排除：{bio['amount']} kg；未计入化石 CO₂ 净量")

    lcia = extract([DEMO / "demo-lcia.spold"], language="zh", kind="lcia")
    lcia_meta = dataset_meta(lcia, LCIA_ACTIVITY, "教学模拟 LCIA")
    impact_key = (METHOD, CONTEXT, CATEGORY, CONTEXT, INDICATOR, CONTEXT, "kg CO2-eq")
    impacts = [r for r in lcia["impacts"] if r["dataset_key"] == lcia_meta["dataset_key"]
               and (r["impactMethodId"], r["impactMethodContextId"],
                    r["impactCategoryId"], r["impactCategoryContextId"],
                    r["impactIndicatorId"], r["impactIndicatorContextId"], r["unit_name"])
               == impact_key]
    impact = require_count(impacts, 1, "指定方法/类别/指标及单位")[0]
    expect(quantity(impact["amount"], "模拟 LCIA 原量"), "13.9", "模拟 LCIA 原量")
    expect(normalized(impact), "1.39", "模拟 LCIA 归一化量")
    print(f"模拟 LCIA 指标：{impact['amount']} {impact['unit_name']}；normalized_amount={normalized(impact)} kg CO2-eq/kg 教学产品")


if __name__ == "__main__":
    main()
```

运行后，电力查询显示 `25` 和 `2.5`；两条化石 CO₂ 输出分别显示原量 `1.5`、`-0.1` 以及归一化量 `0.15`、`-0.01`，净量为 `1.4` 和 `0.14`；生物源 `0.2` 明确排除；模拟 LCIA 显示 `13.9` 和 `1.39`。保留这些原行、筛选键及参考输出，才可以解释这个数从哪个过程、哪类流和哪个基准而来。


### 按你的问题筛选数据

如果想取电力消耗，应筛选中间交换中的输入，并以明确的产品 UUID 或经过确认的产品集合识别电力，然后核对 kWh、MJ 等单位。单靠名称含有 electricity 的字符串筛选可以用于初步查找，但最终统计应核对产品身份；供给市场、电压等级和不同产品不应被无条件视作相同对象。相对于参考产品的比率取 `normalized_amount`，原始清单量取 `amount`，并把参考输出的单位带在结果旁。

如果想取某种污染物的直接排放，应筛选基本流输出，匹配其基本流主数据 UUID 及有效上下文、区室、子区室及其有效上下文，以及单位 UUID 及有效上下文，并保留正负记录。同名物质在水、土壤或不同空气子区室的环境意义可能不同。聚合时先说明是在统计毛记录、净量还是某组区室；示例中化石源与生物源 CO2 也要分别处理。

如果想取材料属性，例如某交换的干质量，应在 `properties.csv` 找到其所属交换实例，再匹配属性 UUID 与单位，阅读属性定义后决定怎样与交换量组合。属性量可能按单位产品给出，也可能有其他语义。不能因为“dry mass”这个名称就无条件执行“交换量乘属性值”，更不能把属性量当作一笔额外的投入或排放。

如果想取现成的碳足迹或其他影响指标，应在 `impacts.csv` 按方法、类别和指标 UUID 筛选，保留单位及参考输出。如果文件没有该指标，空结果表示文件没有提供它；需要获得相应 LCIA 导出或按适用方法另行计算。不能把 CO2 物质量之和替换成任意气候变化指标，也不能把多个不同单位或层级的指标相加。

如果想沿上游找供应过程，应先看供应引用是否明确、目标产品与上下文是否一致，以及目标是否在当前导出中。匹配到一个文件，只表示找到了这条引用的候选，不代表全系统已经闭合。在真实数据库中，多个参考产品、模型、地区、时间和版本可能让同一活动 UUID 对应多个候选；缺失引用也可能要依靠数据库的链接规则。完整产品系统还可能有循环和多功能过程，需要适当的清单计算工具处理，不能用这个读取脚本的候选连接代替网络求解。

### 把公式和不确定性当作另一个层次的信息

demo 中的电力参数为每 kg 产品 2.5 kWh，交换量则为 25 kWh。它们之间的关系写在数学关系字段里。提取脚本会读出参数、交换量和公式文本；它不会用 Python 的 `eval()` 执行公式。ecoSpold 的公式语言有自身规则，且变量名、继承和取值范围需要按规范解析。对于已提供 `amount` 的导出，读取器应先保留该量及是否为计算量的标记，而不是用一个随意实现的公式求值器覆盖它。

demo 中的对数正态分布分别记录 meanValue、mu、基础方差和含谱系不确定性的方差。读取平均交换量不等于做了一次蒙特卡洛抽样；把方差当作标准差也会改变分布。本文解释这些字段，并把原始参数保留在独立 JSON 中。需要传播不确定性时，应选用正确的分布参数化和适用工具，先处理规范里的原文疑点。

## 六、从“拿到一个数”走到“拿到可解释的数据”

一条可用的数据至少应能回答：对象由哪个 UUID 标识、来自哪个数据集和模型、数量与单位是什么、投入或产出由什么分组定义、基准参考产品是多少、地区和时间是什么，以及这个量是直接清单还是累积清单或影响指标。需要追溯时，还应带上来源、计算标记、相关参数、属性和不确定性。

实际操作时，可以先把文件中的交换全部导出，保留原行和元数据，再建立面向具体问题的筛选条件。每次汇总都记录匹配字段和单位换算依据。这样，读者看到某个结果时，可以回到 XML 找到它的来源，也可以知道它为什么适用于当前问题，而不是只能相信一张脱离上下文的数字表。

字段叙述完成 AI 交叉审阅；三份 demo 已通过官方 XSD 结构校验，提取器的 12 项回归测试、命令行导出、本文短代码与查询脚本均已实际运行核验。具体命令、反例及范围见[本文配套的教程审阅记录](tutorial-review.md)。官方原文和模式之间的具体歧义仍按原样留痕，见[字段审校记录](translation-review.md)和[本文配套的教程审阅记录](tutorial-review.md)。审核记录不代表人工专家签核或 ecoinvent 官方认证。

## 附录：原始 HTML 格式表的中文翻译

下面保留原表的十列结构、字段次序、FieldID、旧 SpoldID、取值选项和逐行说明，只把自然语言翻译为中文。这里的必填与重复标记来自原表，不擅自用编者理解改写；实现解析器时，还须结合正文所述父元素、分支和 XSD 约束。

可以[下载独立的中文 HTML 译表](attachments/EcoSpold02.zh.html)，或查看[官方英文 HTML 原件](original/Format%20description/EcoSpold02.html)。原件及完整模式保存在[官方格式包](original/documentation_on_ecospold2_format.v1.0.13.zip)中。附录便于逐项核对，前面的正文负责解释读法、使用场景和取数步骤。

{% tabs %}
{% tab title="中文" %}

本文档提供 EcoSpold02 模式的简化视图。开发者还应查阅模式文件，以确保正确实现该格式。

为区分 Xml 属性与元素，属性名称以“@”为前缀。

“SpoldID, version 1”列中编号后添加的标记，用于表示相对于 EcoSpold01 的变化。

“SpoldID, version 1”列用于帮助查找 EcoSpold01 字段。讨论该格式时，请使用新的“fieldId”列。

以下第 1 版 SpoldId 已在 EcoSpold02 格式中移除：

205	languageCode, 206	localLanguageCode, 208	impactAssessmentResult 400	datasetRelatesToProduct, 403	unit, 404	amount 490	localName, 493	infrastructureProcess, 494	infrastructureIncluded, 495	category, 496	subCategory, 497	localCategory, 498	localSubCategory, 499	formula 502	CASNumber 727	uncertaintyAdjustments, 761	countryCode 2401	referenceToCoProduct, 2403	allocationMethod, 2404	fraction, 2492	referenceToInputOutput 3506	category, 3507	subCategory, 3508	infrastructureProcess, 3509	localCategory, 3510	localSubCategory 3703	location, 3709	standardDeviation95, 3711	formula, 3794	localName, 3795	minValue, 3796	maxValue, 3797	mostLikelyValue 5807	companyCode, 5808	countryCode

{% endtab %}


{% tab title="English 原文" %}

This documentation provides a simplified view of the EcoSpold02 schemata. Developers should consult the schema files as well to make sure the format is implemented correctly.

To distinguish Xml attributes from elements attribute names are prefixed by &quot;@&quot;.

Additions behind the numbers in the &quot;SpoldID, version 1&quot; column are used to indicate changes compared to EcoSpold01.

The &quot;SpoldID, version 1&quot; column is used to help find EcoSpold01 fields. Please use the new &quot;fieldId&quot; column for communications regarding the format.

The following version 1 SpoldIds have been removed in the EcoSpold02 format:

205	languageCode, 206	localLanguageCode, 208	impactAssessmentResult 400	datasetRelatesToProduct, 403	unit, 404	amount 490	localName, 493	infrastructureProcess, 494	infrastructureIncluded, 495	category, 496	subCategory, 497	localCategory, 498	localSubCategory, 499	formula 502	CASNumber 727	uncertaintyAdjustments, 761	countryCode 2401	referenceToCoProduct, 2403	allocationMethod, 2404	fraction, 2492	referenceToInputOutput 3506	category, 3507	subCategory, 3508	infrastructureProcess, 3509	localCategory, 3510	localSubCategory 3703	location, 3709	standardDeviation95, 3711	formula, 3794	localName, 3795	minValue, 3796	maxValue, 3797	mostLikelyValue 5807	companyCode, 5808	countryCode

{% endtab %}

{% endtabs %}

<h3><a href="#appendix-TActivity" id="appendix-TActivity"></a>活动（TActivity）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含活动数据集的标识信息，包括名称和分类。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="100"><td>activityName</td><td>100</td><td>401-rename</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TActivity.100.description.0"><td></td><td colspan="9">本数据集所表示活动的名称。</td></tr>
<tr data-field-id="102"><td>@id</td><td>102</td><td>200-type</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.102.description.0"><td></td><td colspan="9">该活动的唯一标识符。UUID 数据类型是包含十六进制字符的 36 个字符长字符串，可确保标识符在全球范围内唯一。新条目的 UUID 必须由外部软件提供。网上有多种 UUID 生成器，大多数编程语言中也有相应实现。</td></tr>
<tr data-field-id="105"><td>@activityNameId</td><td>105</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.105.description.0"><td></td><td colspan="9">对该活动的活动名称主数据条目的引用。</td></tr>
<tr data-field-id="106"><td>@activityNameContextId</td><td>106</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.106.description.0"><td></td><td colspan="9">对活动名称所属上下文的引用。</td></tr>
<tr data-source-block="TActivity.106.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="110"><td>@type</td><td>110</td><td>201-type</td><td>1 = 单元过程；2 = 已汇总的完整产品系统（System terminated）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.110.description.0"><td></td><td colspan="9">表示本数据集所包含的数据种类（1 = 单元过程；2 = 已汇总的完整产品系统（System terminated））。数据提供方始终以单元过程形式录入数据。数据库生成的归因型和后果型数据集，既可按单元过程层级提供，也可作为汇总的完整系统数据集（即生命周期清单结果）提供；后者包含与该单元过程某一特定产品相关的产品系统中汇总的基本流交换和影响。完整产品系统包括通过中间交换链接的全部上游活动数据集，因此其自身不再包含任何中间交换，而仅包含环境交换和累积的影响评价结果。</td></tr>
<tr data-field-id="115"><td>@specialActivityType</td><td>115</td><td>new</td><td>0 = 普通转化活动（默认）；1 = 市场活动；10 = 市场组；2 = 投入产出活动（IO activity）；3 = 残余活动；4 = 生产组合；5 = 进口活动；6 = 供应组合；7 = 出口活动；8 = 再出口活动；9 = 修正活动</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.115.description.0"><td></td><td colspan="9">特殊活动类型如下：
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
9 = 修正活动。修正活动是向产品系统添加两次的活动，一次带正流、一次带负流，以便将一个或多个交换从系统的一部分转移至另一部分，例如修正上游活动的下游效应，或修正分配造成的质量平衡偏差。更多说明见 ecoinvent《数据质量指南》中的“产品质量差异导致的下游变化”（Downstream changes caused by differences in product quality）和“分配修正”（Allocation corrections）章节。</td></tr>
<tr data-field-id="120"><td>generalComment</td><td>120</td><td>492</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.120.description.0"><td></td><td colspan="9">用于提供数据集一般信息的文本和图像字段。这里只应填写性质较为一般、无法放入其他更具体说明字段的说明和引用。总体上，数据集中的信息应足以判断其是否适合某项特定应用。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TActivity.120.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-field-id="130"><td>@parentActivityId</td><td>130</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.130.description.0"><td></td><td colspan="9">parentActivityId 是指向父活动数据集的 UUID。此字段填入 UUID 时，父活动数据集的全部字段内容均由子活动数据集承接；子活动数据集即通过 UUID 调用父数据集的活动。</td></tr>
<tr data-source-block="TActivity.130.description.1"><td></td><td colspan="9">子活动由其父活动派生（继承）而来，子过程中仅存储相对于父活动发生变化的内容。子活动数据集不能使用 EcoSpold02 模式进行验证，因为其大多数必填字段不会填写。更多细节请参阅有关 ecoinvent 数据库数据集继承的补充文档。</td></tr>
<tr data-source-block="TActivity.130.description.2"><td></td><td colspan="9">子活动数据集（&quot;http://www.EcoInvent.org/EcoSpold02Child&quot;）中的字段有 5 种填写方式：</td></tr>
<tr data-source-block="TActivity.130.description.3"><td></td><td colspan="9">1）将字段留空：此时采用父活动数据集中的值。</td></tr>
<tr data-source-block="TActivity.130.description.4"><td></td><td colspan="9">2）填入内容：此时采用填入的值，忽略父活动数据集中的值。</td></tr>
<tr data-source-block="TActivity.130.description.5"><td></td><td colspan="9">3）在字符串字段中填入包含 {{PARENTTEXT}} 的文本：此时，父活动数据集中的字段内容会插入子数据集所填文本的该位置。</td></tr>
<tr data-source-block="TActivity.130.description.6"><td></td><td colspan="9">4）在类型为 TTextAndImage 的字段中，同时支持 {{PARENTTEXT}} 和 {{text_variables}}；后者允许在父数据集中定义文本变量，并在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TActivity.130.description.7"><td></td><td colspan="9">5）对于具有对应数学关系字段的数量（amount）字段，在 mathematicalRelation 字段中填入包含保留变量 PARENTVALUE 的内容，例如公式 PARENTVALUE*0.5 会使原数量（amount）字段的值减半。</td></tr>
<tr data-field-id="131"><td>@parentActivityContextId</td><td>131</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.131.description.0"><td></td><td colspan="9">对父活动所属上下文的引用。</td></tr>
<tr data-source-block="TActivity.131.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="135"><td>@inheritanceDepth</td><td>135</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.135.description.0"><td></td><td colspan="9">继承深度表示当前数据集可具有的父数据集最大数量。ecoinvent 上下文采用以下值：0 = 不是子数据集；1 = 地理子数据集；2 = 时间子数据集；3 = 宏观经济情景子数据集。</td></tr>
<tr data-field-id="145"><td>includedActivitiesStart</td><td>145</td><td>402-type</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.145.description.0"><td></td><td colspan="9">描述活动的起点。对于“system terminated”（已汇总的完整产品系统），起点始终是“从摇篮开始，即包含全部上游活动”（From cradle, i.e. including all upstream activities）。对于单元过程，可根据输入的性质描述起点，例如“从接收［如原材料 X］开始……”或“以［如劳动力和能源］输入为起点的服务”。</td></tr>
<tr data-field-id="150"><td>includedActivitiesEnd</td><td>150</td><td>402-type</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.150.description.0"><td></td><td colspan="9">描述活动名称中未能不言自明的所包含活动，以及有意排除的活动或输入。例如，“application of pesticides”（农药施用）活动作为一项服务时排除农药本身，以便适用于多种有效成分。说明应以最后一个活动和／或交付点结束，例如“直至并包括将产品装载到货车上”。</td></tr>
<tr data-field-id="170"><td>synonym</td><td>170</td><td>491-type</td><td></td><td>TSynonym</td><td>80</td><td>是</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.170.description.0"><td></td><td colspan="9">名称的同义词列表。与一般多语言字符串不同，同义词可包含多个 xml:lang 属性值相同的元素。</td></tr>
<tr data-source-block="TActivity.170.description.1"><td></td><td colspan="9">允许 0..n 个条目，每个条目的最大长度为 80。</td></tr>
<tr data-field-id="175"><td>tag</td><td>175</td><td>new</td><td></td><td>TTag</td><td>40</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.175.description.0"><td></td><td colspan="9">tag 字段允许使用开放的关键词列表描述活动，可用于筛选、分组和搜索。validTags 文件引用提供预定义标签的列表；但若在 validTags 主文件中找不到某标签条目，语义验证程序应仅显示提示信息，而非错误。</td></tr>
<tr data-field-id="180"><td>@energyValues</td><td>180</td><td>203</td><td>0 = 未指定（Undefined，默认）；1 = 低位热值（Net values）；2 = 高位热值（Gross values）</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.180.description.0"><td></td><td colspan="9">表示数据集中采用能源数值的方式。代码为：0 = 未指定（默认）；1 = 净（低位）热值；2 = 总（高位）热值。</td></tr>
<tr data-source-block="TActivity.180.description.1"><td></td><td colspan="9">此数据字段默认设为 0。</td></tr>
<tr data-field-id="190"><td>@masterAllocationPropertyId</td><td>190</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.190.description.0"><td></td><td colspan="9">通过 UUID 引用本数据集所有交换的默认分配属性。可为每项交换覆盖该分配属性（见字段 1150：specificAllocationPropertyId）。</td></tr>
<tr data-source-block="TActivity.190.description.1"><td></td><td colspan="9">某特定输出的分配因子，等于该输出所声明的 TProperty 值乘以输出数量，再除以所有输出的相应 TProperty 值与输出数量乘积之和。</td></tr>
<tr data-field-id="191"><td>@masterAllocationPropertyContextId</td><td>191</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.191.description.0"><td></td><td colspan="9">对主分配属性所属上下文的引用。</td></tr>
<tr data-source-block="TActivity.191.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="192"><td>@masterAllocationPropertyIdOverwrittenByChild</td><td>192</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.192.description.0"><td></td><td colspan="9">若必须在子数据集中移除对某主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设为 true。否则，移除引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="195"><td>allocationComment</td><td>195</td><td>2407</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TActivity.195.description.0"><td></td><td colspan="9">用于进一步说明分配程序及所选分配属性的文本和图像字段。比较不同分配参数（如物理参数和经济参数）时，若分配因子恰好相同，也可在此报告。文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TActivity.195.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-field-id="200"><td>@datasetIcon</td><td>200</td><td>new</td><td></td><td>anyURI</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TActivity.200.description.0"><td></td><td colspan="9">数据集图标的 URL。图标用于快速识别特定数据集，也可用于产品品牌和公司徽标。图标并非数据集的直接组成部分，而是存储于本地或 ecoinvent 网络服务器，可通过 Http 协议获取。</td></tr>
</tbody></table>
<h3><a href="#appendix-TClassification" id="appendix-TClassification"></a>分类（TClassification）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>包含用于指定活动分类的分类配对信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="300"><td>classificationSystem</td><td>300</td><td>501</td><td></td><td>TString255</td><td>255</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TClassification.300.description.0"><td></td><td colspan="9">所用分类体系的名称，例如 ISIC Rev. 4。这是所引用分类体系（字段 320）的可选纯文本值。</td></tr>
<tr data-field-id="310"><td>classificationValue</td><td>310</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TClassification.310.description.0"><td></td><td colspan="9">活动在所指定分类体系中所属的类别。这是所引用分类值（字段 320）的可选纯文本值。</td></tr>
<tr data-field-id="320"><td>@classificationId</td><td>320</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TClassification.320.description.0"><td></td><td colspan="9">对分类体系中某分类值的引用。该值必须在有效分类列表中定义（见字段 5160）。</td></tr>
<tr data-field-id="321"><td>@classificationContextId</td><td>321</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TClassification.321.description.0"><td></td><td colspan="9">对分类所属上下文的引用。</td></tr>
<tr data-source-block="TClassification.321.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
</tbody></table>
<h3><a href="#appendix-TGeography" id="appendix-TGeography"></a>地理区域（TGeography）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含过程地理适用范围的信息。地理区域可以是活动所在的点位置、描述移动活动的一条线，或分布式活动或生产组合覆盖的区域；该区域包含多个位于具体地点的活动。对于市场（消费组合），地理区域描述市场边界，跨越这些边界的进口和出口受到限制。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="400"><td>@geographyId</td><td>400</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TGeography.400.description.0"><td></td><td colspan="9">引用有效地点文件，该文件包含详细的地理区域信息。</td></tr>
<tr data-field-id="401"><td>@geographyContextId</td><td>401</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TGeography.401.description.0"><td></td><td colspan="9">引用该地理区域所属的上下文。</td></tr>
<tr data-source-block="TGeography.401.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="410"><td>shortname</td><td>410</td><td>662</td><td></td><td>TString40</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TGeography.410.description.0"><td></td><td colspan="9">geographyId 所引用地点的描述性简称，例如 EcoSpold 第 1 版的地区代码。</td></tr>
<tr data-field-id="420"><td>comment</td><td>420</td><td>663</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TGeography.420.description.0"><td></td><td colspan="9">用于进一步解释地理区域的文本和图像字段。尤其在描述区域时，可以说明地理边界划定的性质，特别是在该区域不是行政区的情况下。这里也可提供市场边界的划定依据。文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。</td></tr>
<tr data-source-block="TGeography.420.description.1"><td></td><td colspan="9">文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。</td></tr>
</tbody></table>
<h3><a href="#appendix-TTechnology" id="appendix-TTechnology"></a>技术（TTechnology）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>描述已收集数据所对应的技术。文本应包含识别活动数据所依据技术的属性和特征所需的信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="500"><td>@technologyLevel</td><td>500</td><td>new</td><td>0 = 未指定（undefined）, 1 = 新兴（New）, 2 = 现代（Modern）, 3 = 当前（Current，默认）, 4 = 旧有（Old）, 5 = 过时（Outdated）</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTechnology.500.description.0"><td></td><td colspan="9">对所描述活动的技术进行大致分类的标签，可在建模时用于选择具有特定技术水平的过程。所用代码如下：0=未指定（Undefined）。用于没有技术水平的市场活动。1=新兴（New）。用于在某些方面被认为技术上优于现代技术，但在投资纯粹依据经济考虑时尚未成为最普遍安装选择的技术。2=现代（Modern）。用于在投资纯粹依据经济考虑时，当前新增产能所采用的技术（最有竞争力的技术）。3=当前（Current，默认）。用于介于现代和旧有之间的技术。4=旧有（Old）。用于在退役纯粹依据经济考虑时，当前正在退出使用的技术（竞争力最低的技术）。5=过时（Outdated）。用于已不再使用的技术。这些术语并不一定反映技术的年代。如果一项技术仍最有竞争力，即使已有百年历史，也可以属于现代技术；如果一项技术很快被其他更有竞争力的技术取代，即使出现时间相对较短，也可以属于旧有技术。技术水平是相对于“时间段”（Time Period）所给数据有效年份而言的。在时间序列中，同一技术的技术水平可随时间改变。即使在同一年，同一技术在不同地理位置也可被赋予不同技术水平。</td></tr>
<tr data-field-id="510"><td>comment</td><td>510</td><td>692</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TTechnology.510.description.0"><td></td><td colspan="9">用于描述活动技术的文本和图像字段。文本应包含识别活动数据所依据技术的属性和特征所需的信息，描述该单元过程的技术属性。如果活动包含多个子活动，也应报告相应技术。描述应使用专业命名。文本和图像字段是 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
<tr data-source-block="TTechnology.510.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
</tbody></table>
<h3><a href="#appendix-TTimePeriod" id="appendix-TTimePeriod"></a>时间范围（TTimePeriod）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>描述数据集有效时间段的开始日期和结束日期。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="600"><td>@startDate</td><td>600</td><td>601</td><td></td><td>date</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.600.description.0"><td></td><td colspan="9">数据集有效时间段的开始日期，以完整日期（年-月-日）表示。</td></tr>
<tr data-field-id="610"><td>@endDate</td><td>610</td><td>602</td><td></td><td>date</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.610.description.0"><td></td><td colspan="9">数据集有效时间段的结束日期，以完整日期（年-月-日）表示。</td></tr>
<tr data-field-id="620"><td>@isDataValidForEntirePeriod</td><td>620</td><td>603</td><td></td><td>boolean</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.620.description.0"><td></td><td colspan="9">表示活动数据（在流数据下报告的基本流交换和中间交换）是否在所述整个时间段内有效。如果不是，可在“comment”中说明。</td></tr>
<tr data-field-id="630"><td>comment</td><td>630</td><td>611</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TTimePeriod.630.description.0"><td></td><td colspan="9">用于进一步说明所报告数据时间有效性的文本和图像字段。例如，可包括以下信息：
- 所涉及单元过程的时间相关性有多强（例如，4 年前的数据是否仍适用于今天运行的活动）；
- 数据为何不在整个时间段内有效，以及数据在哪些较短时间段内有效。
文本和图像字段为 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
<tr data-source-block="TTimePeriod.630.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前章节，并可按其 index 属性指定的顺序任意组合。文本变量通过 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。若父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父文本的其余部分不变。这样便于修改子过程中的部分文本。</td></tr>
</tbody></table>
<h3><a href="#appendix-TMacroEconomicScenario" id="appendix-TMacroEconomicScenario"></a>宏观经济情景（TMacroEconomicScenario）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>引用本数据集所用的宏观经济情景。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="700"><td>@macroEconomicScenarioId</td><td>700</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TMacroEconomicScenario.700.description.0"><td></td><td colspan="9">对有效情景列表中定义的某宏观经济情景的引用（见字段 3715）。</td></tr>
<tr data-field-id="701"><td>@macroEconomicScenarioContextId</td><td>701</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TMacroEconomicScenario.701.description.0"><td></td><td colspan="9">对宏观经济情景所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="720"><td>name</td><td>720</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TMacroEconomicScenario.720.description.0"><td></td><td colspan="9">本数据集所属宏观经济情景的名称。</td></tr>
<tr data-field-id="740"><td>comment</td><td>740</td><td>new</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TMacroEconomicScenario.740.description.0"><td></td><td colspan="9">描述宏观经济子数据集与父数据集默认情景的差异。</td></tr>
</tbody></table>
<h3><a href="#appendix-TCustomExchange" id="appendix-TCustomExchange"></a>交换的通用字段（TCustomExchange）</h3>
<p>原表分组可重复：是；原表分组必填：是。</p>
<p>本部分包含两种交换类型共同使用的元素。中间交换或与环境的交换各自特有的元素，列于下方相应部分。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1000"><td>name</td><td>1000</td><td>3702</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1000.description.0"><td></td><td colspan="9">交换的名称。</td></tr>
<tr data-field-id="1005"><td>@id</td><td>1005</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1005.description.0"><td></td><td colspan="9">该交换的唯一标识符。不能使用 intermediateExchangeId 或 elementaryExchangeId 来标识某个交换，因为数据集中的多个交换可以引用同一个主数据条目。</td></tr>
<tr data-field-id="1020"><td>@amount</td><td>1020</td><td>3707</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1020.description.0"><td></td><td colspan="9">基本流交换或中间交换的数量。</td></tr>
<tr data-field-id="1030"><td>@unitId</td><td>1030</td><td>3706</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1030.description.0"><td></td><td colspan="9">对该数量所用单位的引用。</td></tr>
<tr data-field-id="1031"><td>@unitContextId</td><td>1031</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1031.description.0"><td></td><td colspan="9">对单位所属上下文的引用。</td></tr>
<tr data-source-block="TCustomExchange.1031.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1035"><td>unitName</td><td>1035</td><td>3706</td><td></td><td>TString40</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1035.description.0"><td></td><td colspan="9">该数量所用单位的名称。</td></tr>
<tr data-field-id="1040"><td>@variableName</td><td>1040</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1040.description.0"><td></td><td colspan="9">变量名是交换的简称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific_Value 与 Calorific_value 等同）。</td></tr>
<tr data-field-id="1050"><td>@isCalculatedAmount</td><td>1050</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1050.description.0"><td></td><td colspan="9">如果为 true，则 amount 字段的值为 mathematicalRelation 或 transferCoefficient 的计算值。</td></tr>
<tr data-field-id="1060"><td>@mathematicalRelation</td><td>1060</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1060.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TCustomExchange.1060.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="1100"><td>@casNumber</td><td>1100</td><td>3701</td><td></td><td>TCasNumber</td><td>11</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1100.description.0"><td></td><td colspan="9">注明化学文摘社（CAS）编号。CAS 编号的格式为 000000-00-0，其中第一组数字不必完整，即允许少于六位数字。</td></tr>
<tr data-field-id="1110"><td>comment</td><td>1110</td><td>3792</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1110.description.0"><td></td><td colspan="9">可对每个单独的交换添加一般注释。</td></tr>
<tr data-field-id="1120"><td>@sourceId</td><td>1120</td><td>3715</td><td>引用在建模与验证部分定义的来源。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1120.description.0"><td></td><td colspan="9">对有效来源的引用。</td></tr>
<tr data-field-id="1121"><td>@sourceContextId</td><td>1121</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1121.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TCustomExchange.1121.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1122"><td>@sourceIdOverwrittenByChild</td><td>1122</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1122.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1125"><td>@sourceYear</td><td>1125</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1125.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="1126"><td>@sourceFirstAuthor</td><td>1126</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1126.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="1130"><td>@pageNumbers</td><td>1130</td><td>3716</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1130.description.0"><td></td><td colspan="9">如果数据来自文章或较长出版物中的特定页面，则填写相关页码。</td></tr>
<tr data-field-id="1150"><td>@specificAllocationPropertyId</td><td>1150</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1150.description.0"><td></td><td colspan="9">引用分配所使用的属性（Property）。这会覆盖由 masterAllocationPropertyId 定义、适用于整个数据集的默认设置。</td></tr>
<tr data-field-id="1151"><td>@specificAllocationPropertyContextId</td><td>1151</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1151.description.0"><td></td><td colspan="9">对属性所属上下文的引用。</td></tr>
<tr data-source-block="TCustomExchange.1151.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1152"><td>@specificAllocationPropertyIdOverwrittenByChild</td><td>1152</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1152.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1200"><td>transferCoefficient</td><td>1200</td><td>new</td><td></td><td>TTransferCoefficient</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1200.description.0"><td></td><td colspan="9">转移系数将特定输入与特定输出关联，并记录该特定输入中流向该特定输出的份额。</td></tr>
<tr data-source-block="TCustomExchange.1200.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1300"><td>uncertainty</td><td>1300</td><td>3708</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1300.description.0"><td></td><td colspan="9">以分布函数及其参数和/或数据质量谱系数据的形式提供不确定性信息。</td></tr>
<tr data-source-block="TCustomExchange.1300.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1400"><td>property</td><td>1400</td><td>new</td><td></td><td>TProperty</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1400.description.0"><td></td><td colspan="9">交换的属性，例如干质量、含水率、价格、特定元素或物质的含量。</td></tr>
<tr data-source-block="TCustomExchange.1400.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1450"><td>tag</td><td>1450</td><td>new</td><td></td><td>TTag</td><td>40</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCustomExchange.1450.description.0"><td></td><td colspan="9">tag 字段允许使用开放式关键词列表描述活动，可用于筛选、分组和搜索。validTags 文件引用提供预定义标签列表；但如果 validTags 主文件中找不到某个标签条目，语义验证过程应仅显示提示信息，而不应报错。</td></tr>
<tr data-field-id="1470"><td>synonym</td><td>1470</td><td>new</td><td></td><td>TSynonym</td><td>80</td><td>是</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCustomExchange.1470.description.0"><td></td><td colspan="9">名称的同义词列表。与普通多语言字符串不同，同义词可包含多个具有相同 xml:lang 属性值的元素。</td></tr>
<tr data-source-block="TCustomExchange.1470.description.1"><td></td><td colspan="9">允许 0..n 个条目，每个条目的最大长度为 80。</td></tr>
</tbody></table>
<h3><a href="#appendix-TIntermediateExchange" id="appendix-TIntermediateExchange"></a>中间交换专用字段（TIntermediateExchange）</h3>
<p>原表分组可重复：是；原表分组必填：是。</p>
<p>包含仅适用于中间交换的字段，是交换部分之外的附加字段。中间交换是单元过程中记录的产品或废物投入和输出，以及相应的相关信息。</p>
<p>对于中间交换，本部分扩展交换部分。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1500"><td>inputGroup</td><td>1500</td><td>3503</td><td>1 = 材料/燃料（Materials/Fuels）；2 = 电力/热（Electricity/Heat）；3 = 服务（Services）；5 = 来自技术圈，未指定（From Technosphere (unspecified)）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1500.description.0"><td></td><td colspan="9">注明输入流的种类。代码如下：1=材料/燃料（Materials/Fuels），2=电力/热（Electricity/Heat），3=服务（Services），5=来自技术圈，未指定（From Technosphere (unspecified)）。</td></tr>
<tr data-source-block="TIntermediateExchange.1500.description.1"><td></td><td colspan="9">每个交换只能具有 inputGroup 或 outputGroup 中的一个，以表示流的方向。</td></tr>
<tr data-field-id="1510"><td>outputGroup</td><td>1510</td><td>3504</td><td>0 = 参考产品（ReferenceProduct）；2 = 副产品（By-product）；3 = 待处理材料（Material for Treatment）；5 = 存量增加（Stock Additions）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1510.description.0"><td></td><td colspan="9">注明输出流的种类。代码如下：0=参考产品（ReferenceProduct），2=副产品（By-product），3=待处理材料（MaterialForTreatment），5=存量增加（Stock Additions）。</td></tr>
<tr data-source-block="TIntermediateExchange.1510.description.1"><td></td><td colspan="9">每个交换只能具有 inputGroup 或 outputGroup 中的一个，以表示流的方向。</td></tr>
<tr data-field-id="1515"><td>@intermediateExchangeId</td><td>1515</td><td>3793</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1515.description.0"><td></td><td colspan="9">引用该中间交换的主数据条目。</td></tr>
<tr data-field-id="1516"><td>@intermediateExchangeContextId</td><td>1516</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1516.description.0"><td></td><td colspan="9">对中间交换所属上下文的引用。</td></tr>
<tr data-source-block="TIntermediateExchange.1516.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1520"><td>@activityLinkId</td><td>1520</td><td>3715</td><td>引用字段 105（位于另一个活动数据集中）。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1520.description.0"><td></td><td colspan="9">显式引用供应该中间产品的活动。如果此字段为空，则由链接规则确定该活动；该规则使用本活动的地理和时间信息。</td></tr>
<tr data-field-id="1521"><td>@activityLinkContextId</td><td>1521</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1521.description.0"><td></td><td colspan="9">对活动链接所属上下文的引用。</td></tr>
<tr data-source-block="TIntermediateExchange.1521.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1522"><td>@activityLinkIdOverwrittenByChild</td><td>1522</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1522.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1530"><td>@productionVolumeAmount</td><td>1530</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1530.description.0"><td></td><td colspan="9">按年表示的产品产量，单位与该交换相同。</td></tr>
<tr data-field-id="1531"><td>@productionVolumeSourceIdOverwrittenByChild</td><td>1531</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1531.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="1532"><td>@productionVolumeVariableName</td><td>1532</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1532.description.0"><td></td><td colspan="9">变量名是交换产量的简称，用于在数学关系（公式）中引用产量数值。变量可包含字母、数字和下划线（_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific_Value 与 Calorific_value 等同）。</td></tr>
<tr data-field-id="1533"><td>@productionVolumeSourceId</td><td>1533</td><td>new</td><td>引用在建模与验证部分定义的来源。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1533.description.0"><td></td><td colspan="9">对有效来源的引用。</td></tr>
<tr data-field-id="1534"><td>@productionVolumeMathematicalRelation</td><td>1534</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1534.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TIntermediateExchange.1534.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="1535"><td>productionVolumeComment</td><td>1535</td><td>724</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1535.description.0"><td></td><td colspan="9">可对产量数据的数据来源、假设和计算添加一般注释。</td></tr>
<tr data-field-id="1536"><td>@productionVolumeSourceContextId</td><td>1536</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1536.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TIntermediateExchange.1536.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1537"><td>@productionVolumeSourceYear</td><td>1537</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TIntermediateExchange.1537.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="1538"><td>@productionVolumeSourceFirstAuthor</td><td>1538</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TIntermediateExchange.1538.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="1539"><td>productionVolumeUncertainty</td><td>1539</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TIntermediateExchange.1539.description.0"><td></td><td colspan="9">以分布函数及其参数和/或数据质量谱系数据的形式提供不确定性信息。</td></tr>
<tr data-source-block="TIntermediateExchange.1539.description.1"><td></td><td colspan="9">格式定义见下方的复杂类型部分。</td></tr>
<tr data-field-id="1540"><td>classification</td><td>1540</td><td>new</td><td></td><td>TClassification</td><td></td><td>是</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TIntermediateExchange.1540.description.0"><td></td><td colspan="9">包含用于界定产品的分类配对。</td></tr>
</tbody></table>
<h3><a href="#appendix-TElementaryExchange" id="appendix-TElementaryExchange"></a>基本流交换专用字段（TElementaryExchange）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>包含仅适用于基本流交换的字段（除交换部分的字段之外）。与环境的交换是作为单元过程输入和输出记录的基本流，并包含其相关信息。</p>
<p>当交换发生于活动与环境之间时，此部分扩展交换部分。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1600"><td>inputGroup</td><td>1600</td><td>3503</td><td>4 = 来自环境（From Environment）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1600.description.0"><td></td><td colspan="9">表示输入流的类型。代码为：4=来自环境（From Environment）。</td></tr>
<tr data-source-block="TElementaryExchange.1600.description.1"><td></td><td colspan="9">对于每个交换，只能存在 inputGroup 或 outputGroup 中的一个，以表明流的方向。</td></tr>
<tr data-source-block="TElementaryExchange.1600.description.2"><td></td><td colspan="9">此字段相当于字段 1500，但有效值集合不同。</td></tr>
<tr data-field-id="1610"><td>outputGroup</td><td>1610</td><td>3504</td><td>4 = 流向环境（ToEnvironment）</td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1610.description.0"><td></td><td colspan="9">表示输出流的类型。代码为：4=流向环境（ToEnvironment）。</td></tr>
<tr data-source-block="TElementaryExchange.1610.description.1"><td></td><td colspan="9">对于每个交换，只能存在 inputGroup 或 outputGroup 中的一个，以表明流的方向。</td></tr>
<tr data-source-block="TElementaryExchange.1610.description.2"><td></td><td colspan="9">此字段相当于字段 1510，但有效值集合不同。</td></tr>
<tr data-field-id="1615"><td>@elementaryExchangeId</td><td>1615</td><td>3793</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1615.description.0"><td></td><td colspan="9">引用此基本流交换的主数据条目。</td></tr>
<tr data-field-id="1616"><td>@elementaryExchangeContextId</td><td>1616</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TElementaryExchange.1616.description.0"><td></td><td colspan="9">引用该基本流交换所属的上下文。</td></tr>
<tr data-source-block="TElementaryExchange.1616.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1660"><td>compartment</td><td>1660</td><td>new</td><td></td><td>TCompartment</td><td></td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TElementaryExchange.1660.description.0"><td></td><td colspan="9">交换的区室及子区室名称。validCompartments 所引用的 XML 文档包含给定语言下有效的区室／子区室配对的定义。</td></tr>
<tr data-field-id="1670"><td>@formula</td><td>1670</td><td>3711</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TElementaryExchange.1670.description.0"><td></td><td colspan="9">可以填写化学式，例如分子式。</td></tr>
</tbody></table>
<h3><a href="#appendix-TParameter" id="appendix-TParameter"></a>参数（TParameter）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>供公式使用的数据集参数。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1700"><td>name</td><td>1700</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TParameter.1700.description.0"><td></td><td colspan="9">参数的描述性名称。</td></tr>
<tr data-field-id="1705"><td>@parameterId</td><td>1705</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1705.description.0"><td></td><td colspan="9">对有效主数据参数的引用。</td></tr>
<tr data-field-id="1706"><td>@parameterContextId</td><td>1706</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1706.description.0"><td></td><td colspan="9">对参数所属上下文的引用。</td></tr>
<tr data-source-block="TParameter.1706.description.1"><td></td><td colspan="9">若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1710"><td>@amount</td><td>1710</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1710.description.0"><td></td><td colspan="9">参数的当前值。</td></tr>
<tr data-field-id="1712"><td>@unitId</td><td>1712</td><td>3706</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TParameter.1712.description.0"><td></td><td colspan="9">对参数数量单位的引用。</td></tr>
<tr data-field-id="1713"><td>@unitContextId</td><td>1713</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TParameter.1713.description.0"><td></td><td colspan="9">对单位所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1714"><td>unitName</td><td>1714</td><td>3706</td><td></td><td>TString40</td><td>40</td><td>否</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TParameter.1714.description.0"><td></td><td colspan="9">参数数量的单位名称。</td></tr>
<tr data-field-id="1715"><td>@variableName</td><td>1715</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1715.description.0"><td></td><td colspan="9">变量名是交换的简短名称，用于在数学关系（公式）中引用交换量。变量可包含字母、数字和下划线（_）。变量名必须以字母（a-z）开头。变量名不区分大小写（calorific_Value 与 Calorific_value 相同）。</td></tr>
<tr data-field-id="1720"><td>@mathematicalRelation</td><td>1720</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1720.description.0"><td></td><td colspan="9">定义数学公式，通过变量名或 REF 函数引用流、参数或属性的值。</td></tr>
<tr data-source-block="TParameter.1720.description.1"><td></td><td colspan="9">将采用一组特定变量值计算得到的公式结果写入 amount 字段。</td></tr>
<tr data-field-id="1725"><td>@isCalculatedAmount</td><td>1725</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1725.description.0"><td></td><td colspan="9">若为 true，则 amount 字段的值为 mathematicalRelation 的计算值。</td></tr>
<tr data-field-id="1730"><td>uncertainty</td><td>1730</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TParameter.1730.description.0"><td></td><td colspan="9">参数数量的不确定性。</td></tr>
<tr data-field-id="1740"><td>comment</td><td>1740</td><td>new</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TParameter.1740.description.0"><td></td><td colspan="9">可对每个单独参数填写一般说明。</td></tr>
</tbody></table>
<h3><a href="#appendix-TImpactIndicatorResult" id="appendix-TImpactIndicatorResult"></a>影响指标结果（TImpactIndicatorResult）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>计算得到的影响指标。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="1800"><td>@impactIndicatorId</td><td>1800</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1800.description.0"><td></td><td colspan="9">对影响指标的引用。</td></tr>
<tr data-field-id="1801"><td>@impactIndicatorContextId</td><td>1801</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1801.description.0"><td></td><td colspan="9">对影响指标所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1810"><td>@impactMethodId</td><td>1810</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1810.description.0"><td></td><td colspan="9">对影响指标所属方法的引用。</td></tr>
<tr data-field-id="1811"><td>@impactMethodContextId</td><td>1811</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1811.description.0"><td></td><td colspan="9">对影响评价方法所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1815"><td>impactMethodName</td><td>1815</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1815.description.0"><td></td><td colspan="9">影响评价方法的名称。</td></tr>
<tr data-field-id="1820"><td>@impactCategoryId</td><td>1820</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1820.description.0"><td></td><td colspan="9">对影响类别所属方法的引用。</td></tr>
<tr data-field-id="1821"><td>@impactCategoryContextId</td><td>1821</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1821.description.0"><td></td><td colspan="9">对影响类别所属上下文的引用。若省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="1825"><td>impactCategoryName</td><td>1825</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1825.description.0"><td></td><td colspan="9">影响类别的名称。</td></tr>
<tr data-field-id="1830"><td>@amount</td><td>1830</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TImpactIndicatorResult.1830.description.0"><td></td><td colspan="9">影响指标的值。</td></tr>
<tr data-field-id="1840"><td>name</td><td>1840</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1840.description.0"><td></td><td colspan="9">影响指标的名称。</td></tr>
<tr data-field-id="1850"><td>unitName</td><td>1850</td><td>new</td><td></td><td>TString40</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TImpactIndicatorResult.1850.description.0"><td></td><td colspan="9">影响指标数量的单位名称。</td></tr>
</tbody></table>
<h3><a href="#appendix-TCompartment" id="appendix-TCompartment"></a>区室与子区室（TCompartment）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>包含用于指定交换的区室配对。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="330"><td>compartment</td><td>330</td><td>new</td><td></td><td>TCompartmentName</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCompartment.330.description.0"><td></td><td colspan="9">区室名称。这是所引用区室（字段 5315）的纯文本值。</td></tr>
<tr data-field-id="340"><td>subcompartment</td><td>340</td><td>new</td><td></td><td>TCompartmentName</td><td>40</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TCompartment.340.description.0"><td></td><td colspan="9">子区室名称。这是所引用子区室（字段 5325）的纯文本值。</td></tr>
<tr data-field-id="350"><td>@subcompartmentId</td><td>350</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCompartment.350.description.0"><td></td><td colspan="9">引用区室／子区室配对。该配对必须在有效区室列表中定义（见字段 5330）。</td></tr>
<tr data-field-id="351"><td>@subcompartmentContextId</td><td>351</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TCompartment.351.description.0"><td></td><td colspan="9">引用该子区室所属的上下文。</td></tr>
<tr data-source-block="TCompartment.351.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
</tbody></table>
<h3><a href="#appendix-TUncertainty" id="appendix-TUncertainty"></a>不确定性（TUncertainty）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>必须从以下不确定性方法（对数正态、正态、……、未定义分布）中恰好选择一种。TUncertainty 复杂类型用于多个位置，因此，一个数据集可在不同位置包含多个 uncertainty 元素。但每个具有不确定性信息的元素只能包含一个 uncertainty 元素。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="2010"><td>comment</td><td>2010</td><td>3792</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2010.description.0"><td></td><td colspan="9">可对每项不确定性信息填写一般说明。</td></tr>
<tr data-field-id="2100"><td>lognormal</td><td>2100</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2100.description.0"><td></td><td colspan="9">具有平均值 μ（Mu 参数）和方差 σ（Variance 参数）的对数正态分布，是对特征值的自然对数 ln(x) 而非 x 值进行描述的正态分布。</td></tr>
<tr data-field-id="2101"><td>@meanValue</td><td>2101</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2101.description.0"><td></td><td colspan="9">几何平均值。</td></tr>
<tr data-field-id="2102"><td>@mu</td><td>2102</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2102.description.0"><td></td><td colspan="9">底层正态分布的算术平均值。</td></tr>
<tr data-field-id="2103"><td>@variance</td><td>2103</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2103.description.0"><td></td><td colspan="9">底层正态分布的无偏方差。</td></tr>
<tr data-field-id="2104"><td>@varianceWithPedigreeUncertainty</td><td>2104</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2104.description.0"><td></td><td colspan="9">底层正态分布的无偏方差，包括基础不确定性和谱系不确定性。</td></tr>
<tr data-field-id="2110"><td>normal</td><td>2110</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2110.description.0"><td></td><td colspan="9">正态分布，也称“高斯”分布。它是一族具有相同一般形式的分布，其位置参数和尺度参数不同，分别为均值（MeanValue）和标准差（Deviation）。</td></tr>
<tr data-field-id="2111"><td>@meanValue</td><td>2111</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2111.description.0"><td></td><td colspan="9">算术平均值。</td></tr>
<tr data-field-id="2112"><td>@variance</td><td>2112</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2112.description.0"><td></td><td colspan="9">无偏方差。</td></tr>
<tr data-field-id="2113"><td>@varianceWithPedigreeUncertainty</td><td>2113</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2113.description.0"><td></td><td colspan="9">无偏方差，包括基础不确定性和谱系不确定性。</td></tr>
<tr data-field-id="2120"><td>triangular</td><td>2120</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2120.description.0"><td></td><td colspan="9">参数为 minValue、mostLikelyValue 和 maxValue。</td></tr>
<tr data-source-block="TUncertainty.2120.description.1"><td></td><td colspan="9">采用三角不确定性分布时，应根据 mostLikelyValue 计算 meanValue。在 ecoinvent 上下文中，不得使用 mostLikelyValue 字段（#3797）。</td></tr>
<tr data-field-id="2121"><td>@minValue</td><td>2121</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2121.description.0"><td></td><td colspan="9">最小值。</td></tr>
<tr data-field-id="2122"><td>@mostLikelyValue</td><td>2122</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2122.description.0"><td></td><td colspan="9">众数。</td></tr>
<tr data-field-id="2123"><td>@maxValue</td><td>2123</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2123.description.0"><td></td><td colspan="9">最大值。</td></tr>
<tr data-field-id="2130"><td>uniform</td><td>2130</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2130.description.0"><td></td><td colspan="9">minValue 与 maxValue 参数之间的均匀分布。如果 maxValue 参数小于 minValue 参数，则交换两者的值。</td></tr>
<tr data-field-id="2131"><td>@minValue</td><td>2131</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2131.description.0"><td></td><td colspan="9">最小值。</td></tr>
<tr data-field-id="2132"><td>@maxValue</td><td>2132</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2132.description.0"><td></td><td colspan="9">最大值。</td></tr>
<tr data-field-id="2140"><td>beta</td><td>2140</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2140.description.0"><td></td><td colspan="9">Beta 分布使用 minValue（a）、maxValue（b）和 mostFrequentValue（m）参数，计算底层 Gamma 分布的两个形状参数。参数必须满足条件：((a &lt;= m) and (m &lt;= b)) or (a = b)。形状参数按以下公式计算：Shape1 = 1 + 4 * ((m-a) / (b-a))。Shape2 = 6 - Shape1。</td></tr>
<tr data-field-id="2141"><td>@minValue</td><td>2141</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2141.description.0"><td></td><td colspan="9">最小值（a）。</td></tr>
<tr data-field-id="2142"><td>@mostFrequentValue</td><td>2142</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2142.description.0"><td></td><td colspan="9">最常出现的值（m）。</td></tr>
<tr data-field-id="2143"><td>@maxValue</td><td>2143</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2143.description.0"><td></td><td colspan="9">最大值（b）。</td></tr>
<tr data-field-id="2150"><td>gamma</td><td>2150</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2150.description.0"><td></td><td colspan="9">Gamma 分布使用尺度参数和形状参数。这里输入的值将取绝对值使用。minimum 参数的值将加到所有抽样值上。</td></tr>
<tr data-field-id="2151"><td>@shape</td><td>2151</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2151.description.0"><td></td><td colspan="9">形状参数。</td></tr>
<tr data-field-id="2152"><td>@scale</td><td>2152</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2152.description.0"><td></td><td colspan="9">尺度参数。</td></tr>
<tr data-field-id="2153"><td>@minValue</td><td>2153</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2153.description.0"><td></td><td colspan="9">最小值（位置参数）。</td></tr>
<tr data-field-id="2160"><td>binomial</td><td>2160</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2160.description.0"><td></td><td colspan="9">二项分布使用 n 和 p 参数。</td></tr>
<tr data-field-id="2161"><td>@n</td><td>2161</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2161.description.0"><td></td><td colspan="9">独立试验次数。</td></tr>
<tr data-field-id="2162"><td>@p</td><td>2162</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2162.description.0"><td></td><td colspan="9">每次试验的成功概率。</td></tr>
<tr data-field-id="2170"><td>undefined</td><td>2170</td><td>new</td><td></td><td></td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2170.description.0"><td></td><td colspan="9">此“分布”可用于保存 EcoSpold01 格式的旧数据；该格式复用 minValue、maxValue 和 standardDeviation95 字段，存储未定义分布的数据。</td></tr>
<tr data-field-id="2171"><td>@minValue</td><td>2171</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2171.description.0"><td></td><td colspan="9">最小值。</td></tr>
<tr data-field-id="2172"><td>@maxValue</td><td>2172</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2172.description.0"><td></td><td colspan="9">最大值。</td></tr>
<tr data-field-id="2173"><td>@standardDeviation95</td><td>2173</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2173.description.0"><td></td><td colspan="9">从均值向两侧延伸、为覆盖总体 95% 所需的值。</td></tr>
<tr data-field-id="2270"><td>pedigreeMatrix</td><td>2270</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2270.description.0"><td></td><td colspan="9">数据质量指标提供数据质量的定性评价。该评价可转换为定量的附加不确定性，并加到基础不确定性上。pedigreeMatrix 元素将 5 个数据质量指标分组，其自身不包含数据。</td></tr>
<tr data-field-id="2271"><td>@reliability</td><td>2271</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2271.description.0"><td></td><td colspan="9">1=基于测量且经过验证的数据。</td></tr>
<tr data-source-block="TUncertainty.2271.description.1"><td></td><td colspan="9">2=部分基于假设且经过验证的数据，或基于测量但未经过验证的数据。</td></tr>
<tr data-source-block="TUncertainty.2271.description.2"><td></td><td colspan="9">3=部分基于有专业依据的估算、但未经过验证的数据。</td></tr>
<tr data-source-block="TUncertainty.2271.description.3"><td></td><td colspan="9">4=有专业依据的估算，例如由行业专家作出的估算。</td></tr>
<tr data-source-block="TUncertainty.2271.description.4"><td></td><td colspan="9">5=无专业依据的估算（默认）。</td></tr>
<tr data-field-id="2272"><td>@completeness</td><td>2272</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2272.description.0"><td></td><td colspan="9">1=来自所考察市场相关全部场所的代表性数据，时间跨度足以平滑正常波动。</td></tr>
<tr data-source-block="TUncertainty.2272.description.1"><td></td><td colspan="9">2=来自所考察市场相关场所中 &gt;50% 的代表性数据，时间跨度足以平滑正常波动。</td></tr>
<tr data-source-block="TUncertainty.2272.description.2"><td></td><td colspan="9">3=仅来自所考察市场相关部分场所（&lt;&lt;50%）的代表性数据，或来自 &gt;50% 的场所但时间跨度较短的数据。</td></tr>
<tr data-source-block="TUncertainty.2272.description.3"><td></td><td colspan="9">4=仅来自所考察市场相关一个场所的代表性数据，或来自部分场所但时间跨度较短的数据。</td></tr>
<tr data-source-block="TUncertainty.2272.description.4"><td></td><td colspan="9">5=代表性未知，或来自少数场所且时间跨度较短的数据。</td></tr>
<tr data-field-id="2273"><td>@temporalCorrelation</td><td>2273</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2273.description.0"><td></td><td colspan="9">1=与数据集的时间期间（字段 600-610）相差不足 3 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.1"><td></td><td colspan="9">2=与数据集的时间期间（字段 600-610）相差不足 6 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.2"><td></td><td colspan="9">3=与数据集的时间期间（字段 600-610）相差不足 10 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.3"><td></td><td colspan="9">4=与数据集的时间期间（字段 600-610）相差不足 15 年。</td></tr>
<tr data-source-block="TUncertainty.2273.description.4"><td></td><td colspan="9">5=数据年代未知，或与数据集的时间期间（字段 600-610）相差超过 15 年。</td></tr>
<tr data-field-id="2274"><td>@geographicalCorrelation</td><td>2274</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2274.description.0"><td></td><td colspan="9">1=来自研究区域的数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.1"><td></td><td colspan="9">2=来自包含研究区域的更大区域的平均数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.2"><td></td><td colspan="9">3=来自生产条件相似区域的数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.3"><td></td><td colspan="9">4=来自生产条件略有相似之处的区域的数据。</td></tr>
<tr data-source-block="TUncertainty.2274.description.4"><td></td><td colspan="9">5=来自未知区域或明显不同区域的数据，例如以北美代替中东、以 OECD 欧洲代替俄罗斯。</td></tr>
<tr data-field-id="2275"><td>@furtherTechnologyCorrelation</td><td>2275</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TUncertainty.2275.description.0"><td></td><td colspan="9">1=来自所研究企业、过程和材料的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.1"><td></td><td colspan="9">2=来自所研究过程和材料（即相同技术），但企业不同的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.2"><td></td><td colspan="9">3=来自所研究过程和材料，但技术不同的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.3"><td></td><td colspan="9">4=有关相关过程或材料的数据。</td></tr>
<tr data-source-block="TUncertainty.2275.description.4"><td></td><td colspan="9">5=有关实验室规模相关过程的数据，或来自不同技术的数据。</td></tr>
</tbody></table>
<h3><a href="#appendix-TProperty" id="appendix-TProperty"></a>属性（TProperty）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>用于指定交换属性的格式。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="2300"><td>@propertyId</td><td>2300</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2300.description.0"><td></td><td colspan="9">引用该属性的主数据条目。</td></tr>
<tr data-field-id="2301"><td>@propertyContextId</td><td>2301</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2301.description.0"><td></td><td colspan="9">对属性所属上下文的引用。</td></tr>
<tr data-source-block="TProperty.2301.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2310"><td>name</td><td>2310</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TProperty.2310.description.0"><td></td><td colspan="9">属性的描述性名称。</td></tr>
<tr data-field-id="2320"><td>@unitId</td><td>2320</td><td>3706</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2320.description.0"><td></td><td colspan="9">对该数量所用单位的引用。</td></tr>
<tr data-field-id="2321"><td>@unitContextId</td><td>2321</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2321.description.0"><td></td><td colspan="9">对单位所属上下文的引用。</td></tr>
<tr data-source-block="TProperty.2321.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2325"><td>unitName</td><td>2325</td><td>3706</td><td></td><td>TString40</td><td>40</td><td>否</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TProperty.2325.description.0"><td></td><td colspan="9">属性量所用单位的名称。</td></tr>
<tr data-field-id="2330"><td>@amount</td><td>2330</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2330.description.0"><td></td><td colspan="9">属性的值。</td></tr>
<tr data-field-id="2335"><td>@isDefiningValue</td><td>2335</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2335.description.0"><td></td><td colspan="9">如果此字段为 true，则该属性值是交换定义的一部分，因此与交换量之间具有固定关系；不能针对该交换在不同数据集中的个别实例改变这一关系。</td></tr>
<tr data-field-id="2340"><td>@mathematicalRelation</td><td>2340</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2340.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TProperty.2340.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="2345"><td>@isCalculatedAmount</td><td>2345</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2345.description.0"><td></td><td colspan="9">如果为 true，则 amount 字段的值为 mathematicalRelation 的计算值。</td></tr>
<tr data-field-id="2350"><td>@variableName</td><td>2350</td><td>new</td><td></td><td>TVariableName</td><td>40</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2350.description.0"><td></td><td colspan="9">定义变量名，以便在 mathematicalrelation（数学关系）中引用属性量。</td></tr>
<tr data-source-block="TProperty.2350.description.1"><td></td><td colspan="9">变量名必须以字母（a-z）开头，可包含字母、数字和下划线（_）。变量名不区分大小写（calorific_Value 与 Calorific_value 等同）。</td></tr>
<tr data-field-id="2360"><td>uncertainty</td><td>2360</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2360.description.0"><td></td><td colspan="9">属性值的不确定性。</td></tr>
<tr data-field-id="2370"><td>@sourceId</td><td>2370</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2370.description.0"><td></td><td colspan="9">对有效来源的引用，指明记录该属性的出版物。</td></tr>
<tr data-field-id="2371"><td>@sourceContextId</td><td>2371</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2371.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TProperty.2371.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2372"><td>@sourceIdOverwrittenByChild</td><td>2372</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TProperty.2372.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="2375"><td>@sourceYear</td><td>2375</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2375.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="2376"><td>@sourceFirstAuthor</td><td>2376</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TProperty.2376.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="2380"><td>comment</td><td>2380</td><td>new</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TProperty.2380.description.0"><td></td><td colspan="9">可对某个特定交换的每项单独属性添加一般注释。</td></tr>
</tbody></table>
<h3><a href="#appendix-TTransferCoefficient" id="appendix-TTransferCoefficient"></a>转移系数（TTransferCoefficient）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>用于根据投入量计算输出量的转移系数。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="2400"><td>@exchangeId</td><td>2400</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2400.description.0"><td></td><td colspan="9">引用某个交换的 UUID。</td></tr>
<tr data-field-id="2410"><td>@amount</td><td>2410</td><td>new</td><td></td><td>TFloatNumber</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2410.description.0"><td></td><td colspan="9">应将转移系数的数值与所引用交换的数量相乘。</td></tr>
<tr data-field-id="2420"><td>@mathematicalRelation</td><td>2420</td><td>new</td><td></td><td>TBaseString32000</td><td>32000</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2420.description.0"><td></td><td colspan="9">定义一个数学公式，通过变量名或 REF 函数引用流、参数或属性的数值。</td></tr>
<tr data-source-block="TTransferCoefficient.2420.description.1"><td></td><td colspan="9">将公式在一组特定变量值下的计算结果写入 amount 字段。</td></tr>
<tr data-field-id="2425"><td>@isCalculatedAmount</td><td>2425</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2425.description.0"><td></td><td colspan="9">如果为 true，则 amount 字段的值为 mathematicalRelation 的计算值。</td></tr>
<tr data-field-id="2430"><td>uncertainty</td><td>2430</td><td>new</td><td></td><td>TUncertainty</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2430.description.0"><td></td><td colspan="9">转移系数数值的不确定性。</td></tr>
<tr data-field-id="2440"><td>@sourceId</td><td>2440</td><td>new</td><td>引用在 modellingAndValidation 部分定义的来源。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2440.description.0"><td></td><td colspan="9">对有效来源的引用。</td></tr>
<tr data-field-id="2441"><td>@sourceContextId</td><td>2441</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2441.description.0"><td></td><td colspan="9">对来源所属上下文的引用。</td></tr>
<tr data-source-block="TTransferCoefficient.2441.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="2442"><td>@sourceIdOverwrittenByChild</td><td>2442</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2442.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用会被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="2445"><td>@sourceYear</td><td>2445</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TTransferCoefficient.2445.description.0"><td></td><td colspan="9">分别注明出版年份或信息交流年份。对于网站，填写最后访问的年份。</td></tr>
<tr data-field-id="2446"><td>@sourceFirstAuthor</td><td>2446</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TTransferCoefficient.2446.description.0"><td></td><td colspan="9">以姓氏和名字缩写注明第一作者（例如 Einstein A.）。对于现场测量、口头交流、个人书面交流和问卷调查（sourceType=4, 5, 6, 7），此处填写提供信息的人员姓名。</td></tr>
<tr data-field-id="2450"><td>comment</td><td>2450</td><td>3792</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TTransferCoefficient.2450.description.0"><td></td><td colspan="9">可对每个单独的转移系数添加一般注释。</td></tr>
</tbody></table>
<h3><a href="#appendix-TTextAndImage" id="appendix-TTextAndImage"></a>文本与图像（TTextAndImage）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>text、imageUri 和 variable 元素的列表。这些元素可按任意顺序组合。必须通过 text 和 imageUrl 元素的 index 属性指定它们在结果中的所需顺序。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3900"><td>text</td><td>3900</td><td>new</td><td></td><td>TIndexedString32000</td><td>32000</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTextAndImage.3900.description.0"><td></td><td colspan="9">用于描述当前部分的自由文本。其 index 属性用于规定文本和图像元素的特定顺序。</td></tr>
<tr data-field-id="3910"><td>imageUrl</td><td>3910</td><td>new</td><td></td><td>anyURI</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTextAndImage.3910.description.0"><td></td><td colspan="9">可用于在文本之间插入图像。其 index 属性用于规定文本和图像元素的特定顺序。</td></tr>
<tr data-field-id="3920"><td>variable</td><td>3920</td><td>new</td><td></td><td>TNamedString32000</td><td>32000</td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TTextAndImage.3920.description.0"><td></td><td colspan="9">定义本部分 text 元素中使用的变量名及其值。派生数据集可以覆盖这些定义，以改变变量值。</td></tr>
</tbody></table>
<h3><a href="#appendix-TRepresentativeness" id="appendix-TRepresentativeness"></a>代表性（TRepresentativeness）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>包含数据集信息的代表性，以及数据如何采样和／或计算的信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3000"><td>@systemModelId</td><td>3000</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3000.description.0"><td></td><td colspan="9">系统模型描述如何将活动数据集链接成产品系统。ecoinvent 网络中的部分选项为：&#x27;undefined&#x27;（未指定系统模型）、&#x27;attributional, average current suppliers, revenue allocation&#x27;（归因型、当前供应商平均组合、按收入分配）、&#x27;consequential, small-scale, long-term decisions&#x27;（后果型、小规模、长期决策）。</td></tr>
<tr data-field-id="3001"><td>@systemModelContextId</td><td>3001</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3001.description.0"><td></td><td colspan="9">引用该系统模型所属的上下文。</td></tr>
<tr data-source-block="TRepresentativeness.3001.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3005"><td>systemModelName</td><td>3005</td><td>new</td><td></td><td>TString120</td><td>120</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TRepresentativeness.3005.description.0"><td></td><td colspan="9">所引用系统模型（字段 3000）的纯文本值。</td></tr>
<tr data-field-id="3010"><td>@percent</td><td>3010</td><td>722</td><td>最大值为 100。</td><td>TPercent</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3010.description.0"><td></td><td colspan="9">所采样数据占该活动拟代表总体的百分比；该总体由 Geography、Technology 和 Time Period 下的字段确定。</td></tr>
<tr data-field-id="3030"><td>samplingProcedure</td><td>3030</td><td>725</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3030.description.0"><td></td><td colspan="9">描述用于量化交换的采样和计算程序的文本。应说明特定基本流交换和中间交换的采样程序是否不同于一般程序，并指出组合不同采样程序可能产生的问题。文本和图像字段由 text、imageUri 和 variable 元素列表组成。text 和 imageUri 元素可用于描述当前部分，并可按照其 index 属性确定的顺序任意组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 形式使用。如果父文本字段包含变量，子活动数据集可以重新定义该变量，同时保持父文本的其余内容不变。这样便可轻松修改子过程中的部分文本。</td></tr>
<tr data-field-id="3040"><td>extrapolations</td><td>3040</td><td>726</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.0"><td></td><td colspan="9">描述从另一时间期间、另一地理区域或另一技术外推数据的情况，以及这些外推的具体实施方式。</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.1"><td></td><td colspan="9">应说明是否在单个交换层面进行了不同的外推。</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.2"><td></td><td colspan="9">如果将代表某一国家运行活动的数据用于另一国家的活动，可在这里注明其原始代表性。</td></tr>
<tr data-source-block="TRepresentativeness.3040.description.3"><td></td><td colspan="9">也可在这里说明外推导致的均值变化。</td></tr>
</tbody></table>
<h3><a href="#appendix-TReview" id="appendix-TReview"></a>审查（TReview）</h3>
<p>原表分组可重复：是；原表分组必填：否。</p>
<p>包含开展鉴定性评审（critical review）的人员信息，以及评审的主要结果、结论和提出的建议。</p>
<p>允许多名评审者。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3300"><td>@reviewerId</td><td>3300</td><td>5616</td><td>引用字段 3610。</td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3300.description.0"><td></td><td colspan="9">注明开展评审的人员。</td></tr>
<tr data-field-id="3301"><td>@reviewerContextId</td><td>3301</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3301.description.0"><td></td><td colspan="9">对评审者所属上下文的引用。</td></tr>
<tr data-source-block="TReview.3301.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3305"><td>@reviewerName</td><td>3305</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TReview.3305.description.0"><td></td><td colspan="9">人员的名字和姓氏。</td></tr>
<tr data-field-id="3306"><td>@reviewerEmail</td><td>3306</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TReview.3306.description.0"><td></td><td colspan="9">人员的完整电子邮件地址。</td></tr>
<tr data-field-id="3310"><td>@reviewDate</td><td>3310</td><td>new</td><td></td><td>date</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3310.description.0"><td></td><td colspan="9">验证或评审日期。</td></tr>
<tr data-field-id="3320"><td>@reviewedMajorRelease</td><td>3320</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3320.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3800。</td></tr>
<tr data-field-id="3325"><td>@reviewedMinorRelease</td><td>3325</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3325.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3805。</td></tr>
<tr data-field-id="3330"><td>@reviewedMajorRevision</td><td>3330</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3330.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3810。</td></tr>
<tr data-field-id="3335"><td>@reviewedMinorRevision</td><td>3335</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TReview.3335.description.0"><td></td><td colspan="9">经验证或评审的数据集版本。引用字段 3815。</td></tr>
<tr data-field-id="3340"><td>details</td><td>3340</td><td>5615</td><td></td><td>TTextAndImage</td><td></td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TReview.3340.description.0"><td></td><td colspan="9">用于记录数据集评审者注释的文本和图像字段。文本和图像字段是 text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
<tr data-source-block="TReview.3340.description.1"><td></td><td colspan="9">text、imageUri 和 variable 元素的列表。text 和 imageUri 元素可用于描述当前部分，并可按照各自 index 属性指定的任意顺序组合。文本变量由 variable 元素定义，可在文本中以 {{variablename}} 的形式使用。如果父数据集的文本字段包含变量，子活动数据集可重新定义该变量，同时保持父数据集其余文本不变。这样便于修改子过程中的局部文本。</td></tr>
<tr data-field-id="3350"><td>otherDetails</td><td>3350</td><td>5619</td><td></td><td>TString32000</td><td>32000</td><td>否</td><td>否</td><td>是</td><td>否</td></tr>
<tr data-source-block="TReview.3350.description.0"><td></td><td colspan="9">包含评审过程的进一步信息，例如数据集首次发布后补充的小幅修正。</td></tr>
</tbody></table>
<h3><a href="#appendix-TDataEntryBy" id="appendix-TDataEntryBy"></a>数据录入者（TDataEntryBy）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含数据集作者的信息，即将数据录入数据库格式的人员，也是对数据负责的人员。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3400"><td>@personId</td><td>3400</td><td>302</td><td>条目必须与字段 3610 中的现有条目一致。</td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataEntryBy.3400.description.0"><td></td><td colspan="9">编制数据集并将其录入数据库的人员的 ID 编号。</td></tr>
<tr data-field-id="3401"><td>@personContextId</td><td>3401</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataEntryBy.3401.description.0"><td></td><td colspan="9">对人员所属上下文的引用。</td></tr>
<tr data-source-block="TDataEntryBy.3401.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3403"><td>@isActiveAuthor</td><td>3403</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataEntryBy.3403.description.0"><td></td><td colspan="9">此字段定义字段 3400 指定的人员是否为本数据集的活跃作者（active author）。其他数据提供者今后修改数据集时，将征询该活跃作者的意见。</td></tr>
<tr data-field-id="3405"><td>@personName</td><td>3405</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataEntryBy.3405.description.0"><td></td><td colspan="9">人员的名字和姓氏。</td></tr>
<tr data-field-id="3406"><td>@personEmail</td><td>3406</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataEntryBy.3406.description.0"><td></td><td colspan="9">人员的完整电子邮件地址。</td></tr>
</tbody></table>
<h3><a href="#appendix-TDataGeneratorAndPublication" id="appendix-TDataGeneratorAndPublication"></a>数据生成者与发布（TDataGeneratorAndPublication）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含谁收集、汇编或发布原始数据的信息。此人与 &#x27;DataEntryBy&#x27; 中的人可能相同，也可能不同。此外，还包含数据集所依据出版物的类型及数据集可访问性的信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3500"><td>@personId</td><td>3500</td><td>751</td><td>数据生成者的 ID 编号，即收集、汇编或发布原始数据的个人或组织的编号。数据生成者与作者（见 &#x27;DataEntryBy&#x27;）可能相同，也可能不同。此字段旨在确认并引用数据来源，以及承担主要数据收集工作的个人或组织。</td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3500.description.0"><td></td><td colspan="9">生成数据集的个人的 ID 编号。该编号必须对应于相应数据集中所列某个人的 ID 编号。</td></tr>
<tr data-field-id="3501"><td>@personContextId</td><td>3501</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3501.description.0"><td></td><td colspan="9">引用该人员所属的上下文。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3501.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3505"><td>@personName</td><td>3505</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3505.description.0"><td></td><td colspan="9">人员的名和姓。</td></tr>
<tr data-field-id="3506"><td>@personEmail</td><td>3506</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>是</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3506.description.0"><td></td><td colspan="9">人员的完整电子邮件地址。</td></tr>
<tr data-field-id="3510"><td>@dataPublishedIn</td><td>3510</td><td>756</td><td>0 = 数据本身未在其他地方发布（默认）；1 = 部分单元过程或子系统的数据已发布；2 = 数据已完整发布于某来源中（引用字段 757）。</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3510.description.0"><td></td><td colspan="9">表示数据集是否已发布：未发布、部分发布或完整发布。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3510.description.1"><td></td><td colspan="9">代码为：0=数据本身未发布（默认）；1=部分单元过程或子系统的数据已发布；2=数据已完整发布于 &#x27;referenceToPublishedSource&#x27; 中。</td></tr>
<tr data-field-id="3520"><td>@publishedSourceId</td><td>3520</td><td>757</td><td>引用 801。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3520.description.0"><td></td><td colspan="9">记录该数据集的报告的 ID 编号。</td></tr>
<tr data-field-id="3521"><td>@publishedSourceContextId</td><td>3521</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3521.description.0"><td></td><td colspan="9">引用该已发布来源所属的上下文。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3521.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3522"><td>@publishedSourceIdOverwrittenByChild</td><td>3522</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3522.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
<tr data-field-id="3525"><td>@publishedSourceYear</td><td>3525</td><td>new</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3525.description.0"><td></td><td colspan="9">分别表示出版年份或沟通年份。对于网站，表示最后访问年份。</td></tr>
<tr data-field-id="3526"><td>@publishedSourceFirstAuthor</td><td>3526</td><td>new</td><td></td><td>TBaseString40</td><td>40</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3526.description.0"><td></td><td colspan="9">以姓和名字缩写标明第一作者，例如 Einstein A.。对于现场测量、口头沟通、个人书面沟通和问卷（&#x27;sourceType&#x27;=4, 5, 6, 7），这里填写沟通人员的姓名。</td></tr>
<tr data-field-id="3530"><td>@pageNumbers</td><td>3530</td><td>762</td><td></td><td>TBaseString30</td><td>30</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3530.description.0"><td></td><td colspan="9">若数据取自文章或较大型出版物的特定页面，则填写相关页码。</td></tr>
<tr data-field-id="3540"><td>@isCopyrightProtected</td><td>3540</td><td>758</td><td></td><td>boolean</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3540.description.0"><td></td><td colspan="9">表示是否存在著作权。应相应填写 &#x27;1&#x27;（是）或 &#x27;0&#x27;（否）。</td></tr>
<tr data-field-id="3550"><td>@accessRestrictedTo</td><td>3550</td><td>759</td><td>0=公开；1=被许可人；2=仅结果；3=受限制。</td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.0"><td></td><td colspan="9">表示数据集可能存在的访问限制。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.1"><td></td><td colspan="9">所用代码为：0=公开；1=被许可人；2=仅结果；3=受限制。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.2"><td></td><td colspan="9">accessRestrictedTo=0：无访问限制。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.3"><td></td><td colspan="9">accessRestrictedTo=1：只有许可证持有者（由上下文定义）可以访问。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.4"><td></td><td colspan="9">accessRestrictedTo=2：许可证持有者（由上下文定义）可以访问 LCI 结果，但不能访问单元过程原始数据。数据库管理员具有完整访问权限。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3550.description.5"><td></td><td colspan="9">accessRestrictedTo=3：只有 &#x27;companyCode&#x27; 指定的组织和数据库管理员可以访问。</td></tr>
<tr data-field-id="3560"><td>@companyId</td><td>3560</td><td>760</td><td>如果 759=3。</td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3560.description.0"><td></td><td colspan="9">引用允许使用此数据集的组织／机构；数据集使用限于该组织／机构。</td></tr>
<tr data-field-id="3561"><td>@companyContextId</td><td>3561</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3561.description.0"><td></td><td colspan="9">引用该公司所属的上下文。</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3561.description.1"><td></td><td colspan="9">如果省略此属性，则改用数据集自身的上下文。</td></tr>
<tr data-field-id="3562"><td>@companyCode</td><td>3562</td><td>760</td><td>如果 759=3。</td><td>TCompanyCode</td><td>7</td><td>否</td><td>否</td><td>否</td><td>是</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3562.description.0"><td></td><td colspan="9">所引用公司（字段 3560）的可选 7 字母代码的纯文本值。</td></tr>
<tr data-field-id="3563"><td>@companyIdOverwrittenByChild</td><td>3563</td><td>new</td><td></td><td>boolean</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TDataGeneratorAndPublication.3563.description.0"><td></td><td colspan="9">如果必须在子数据集中移除对某个主数据实体的引用，则必须将相应的 xxxOverwrittenByChild 属性设置为 true。否则，移除该引用将被解释为“保留父数据集的值”（Keep the Parent Value）。</td></tr>
</tbody></table>
<h3><a href="#appendix-TFileAttributes" id="appendix-TFileAttributes"></a>文件属性（TFileAttributes）</h3>
<p>原表分组可重复：否；原表分组必填：是。</p>
<p>包含关于整个文件的元信息。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="3800"><td>@majorRelease</td><td>3800</td><td>202</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3800.description.0"><td></td><td colspan="9">每次重大更新时，主发布版本号加一，例如每两年一次。</td></tr>
<tr data-field-id="3805"><td>@minorRelease</td><td>3805</td><td>202</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3805.description.0"><td></td><td colspan="9">在两次重大更新之间，每次发布时次发布版本号加一。</td></tr>
<tr data-field-id="3810"><td>@majorRevision</td><td>3810</td><td>207</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3810.description.0"><td></td><td colspan="9">修订号针对每个数据集单独设定，独立于整个数据库的发布版本，用于区分数据库主／次发布版本内的数据集不同版本。主修订号反映数据集已接受变更的数量，只能随时间增加，不得手动更改。在 ecoinvent 上下文中，每当活动变更加入数据库（即通过审查流程后），主修订号都会增加，同时将次修订号重置为 1。</td></tr>
<tr data-field-id="3815"><td>@minorRevision</td><td>3815</td><td>207</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3815.description.0"><td></td><td colspan="9">次修订号描述数据集在提交审查前编辑过程中的版本。在 ecoinvent 上下文中，每当数据提供者将对数据集的修改保存到本地，或作为草稿保存到 ecoinvent 服务器时，次修订号都会自动增加。每当主修订号增加（即数据集变更被审查者接受）时，次修订号重置为“1”。</td></tr>
<tr data-field-id="3820"><td>@defaultLanguage</td><td>3820</td><td>new</td><td></td><td>string</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3820.description.0"><td></td><td colspan="9">该数据集所有多语言字段的默认语言。每个多语言字段至少应包含默认语言的值。如果未提供 defaultLanguage，则使用默认值（&quot;en&quot;）。</td></tr>
<tr data-field-id="3830"><td>@creationTimestamp</td><td>3830</td><td>204a</td><td>数据集创建时间。</td><td>dateTime</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3830.description.0"><td></td><td colspan="9">数据集创建时自动生成的日期。</td></tr>
<tr data-field-id="3840"><td>@lastEditTimestamp</td><td>3840</td><td>204b</td><td>数据集最后编辑时间。</td><td>dateTime</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3840.description.0"><td></td><td colspan="9">数据集保存时自动生成的日期。</td></tr>
<tr data-field-id="3850"><td>@internalSchemaVersion</td><td>3850</td><td>new</td><td></td><td>TBaseString80</td><td>80</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3850.description.0"><td></td><td colspan="9">数据集基于此内部模式版本生成。</td></tr>
<tr data-field-id="3860"><td>@fileGenerator</td><td>3860</td><td>new</td><td></td><td>TBaseString255</td><td>255</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3860.description.0"><td></td><td colspan="9">对创建此文件的程序的描述，最好包含版本。</td></tr>
<tr data-field-id="3870"><td>@fileTimestamp</td><td>3870</td><td>new</td><td></td><td>dateTime</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3870.description.0"><td></td><td colspan="9">此文件创建的时间和日期。</td></tr>
<tr data-field-id="3880"><td>@contextId</td><td>3880</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3880.description.0"><td></td><td colspan="9">表示此数据集所面向的上下文。该信息例如用于将数据集信息的可访问性限制在一个特定上下文内，并确定访问它所需的主数据文件。如果省略此属性，则假定该数据集为独立数据集，且无法解析主数据引用以取得所引用内容。</td></tr>
<tr data-source-block="TFileAttributes.3880.description.1"><td></td><td colspan="9">上下文取代 ecoSpold01 的质量网络（字段 id 304）。ecoinvent 质量网络的上下文 ID 可在 Context.xml 主数据文件中找到。</td></tr>
<tr data-field-id="3885"><td>contextName</td><td>3885</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>否</td><td>是</td><td>是</td></tr>
<tr data-source-block="TFileAttributes.3885.description.0"><td></td><td colspan="9">字段 3880 所引用上下文的名称。</td></tr>
<tr data-source-block="TFileAttributes.3885.description.1"><td></td><td colspan="9">上下文取代 ecoSpold01 的质量网络（字段 id 304）。ecoinvent 质量网络的上下文 ID 可在 Context.xml 主数据文件中找到。</td></tr>
<tr data-field-id="3890"><td>requiredContext</td><td>3890</td><td>new</td><td></td><td>TRequiredContextReference</td><td></td><td>是</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TFileAttributes.3890.description.0"><td></td><td colspan="9">引用加载本文档所必需的上下文，以完整保留文档中的所有主数据引用。</td></tr>
</tbody></table>
<h3><a href="#appendix-TRequiredContextReference" id="appendix-TRequiredContextReference"></a>所需上下文引用（TRequiredContextReference）</h3>
<p>原表分组可重复：否；原表分组必填：否。</p>
<p>此类型用于指定：若要使用数据集引用的主数据读取该数据集，必须了解哪些上下文。</p>
<p>此类型可用于表明：读取该数据集需要来自不同上下文的主数据条目。读取数据集的软件必须识别这些上下文，并知道各上下文的实际主数据文件位于何处。</p>
<table class="format-table">
<thead><tr><th>名称</th><th>FieldID</th><th>SpoldID（第 1 版）</th><th>取值选项</th><th>类型</th><th>长度</th><th>可重复</th><th>必填</th><th>多语言</th><th>主数据冗余字段</th></tr></thead>
<tbody>
<tr data-field-id="7810"><td>@majorRelease</td><td>7810</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7810.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7820"><td>@minorRelease</td><td>7820</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7820.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7830"><td>@majorRevision</td><td>7830</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7830.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7840"><td>@minorRevision</td><td>7840</td><td>new</td><td></td><td>integer</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7840.description.0"><td></td><td colspan="9">此版本号可用于确保某活动所需的主数据条目已经存在。</td></tr>
<tr data-field-id="7850"><td>@requiredContextId</td><td>7850</td><td>new</td><td></td><td>TUuid</td><td>36</td><td>否</td><td>是</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7850.description.0"><td></td><td colspan="9">引用该主数据文件所属的上下文。</td></tr>
<tr data-source-block="TRequiredContextReference.7850.description.1"><td></td><td colspan="9">如果省略此属性，应改用数据集自身的上下文。</td></tr>
<tr data-field-id="7855"><td>requiredContextName</td><td>7855</td><td>new</td><td></td><td>TString80</td><td>80</td><td>否</td><td>是</td><td>是</td><td>是</td></tr>
<tr data-source-block="TRequiredContextReference.7855.description.0"><td></td><td colspan="9">字段 7850 所引用上下文的名称。</td></tr>
<tr data-field-id="7860"><td>@requiredContextFileLocation</td><td>7860</td><td>new</td><td></td><td>anyURI</td><td></td><td>否</td><td>否</td><td>否</td><td>否</td></tr>
<tr data-source-block="TRequiredContextReference.7860.description.0"><td></td><td colspan="9">指向包含此上下文主数据文件的目录的可选 URI 引用。</td></tr>
</tbody></table>
