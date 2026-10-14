# 用 demo 走通读取过程


[下载 demo、提取脚本及使用说明 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后即可按[提取与查询实践](extraction-practice.md)运行。

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
