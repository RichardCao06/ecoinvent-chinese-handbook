# 活动

对应官方格式类型：`TActivity`。本篇以文章解释该类型的 20 条字段；复合类型也会说明它们依附在哪个对象上。

## 先识别活动，再判断边界与继承 <a href="#read-tactivity" id="read-tactivity"></a>

读取一个活动数据集时，可先进入 `activityDescription/activity`。这个元素采用 `TActivity` 类型，回答“这是什么活动、记录了哪一层数据、边界在哪里”。元素 `activityName` 是供人阅读的活动名称；属性 `id` 是活动的 UUID，而 `activityNameId` 是对活动名称主数据条目的 UUID 引用。两种 UUID 的角色不同：前者识别活动，后者查找名称主数据，不能因为都使用 `TUuid` 就混作同一个键。该类型以 36 个字符表示 UUID；创建新条目的 UUID 需要由外部软件生成。`activityNameContextId` 指明名称主数据所属上下文，省略时使用数据集自身的上下文。因此，程序可以把名称提取为显示文本，但在追踪对象身份和解析主数据时，应同时保留相应 UUID 与上下文。

接下来读取属性 `type`，区分单元过程与汇总结果。`type=1` 表示单元过程，这是数据提供方录入数据的形式；`type=2` 表示 `System terminated`，即已经纳入上游活动并汇总的完整产品系统。这种系统记录与单元过程某一特定产品有关的累积生命周期清单及影响结果，已包含沿中间交换链接的全部上游活动。官方说明将这种产品系统描述为“自身没有中间交换，只有环境交换和累积影响评价结果”，强调上游供应结构已经汇总；但当前完整 XSD 的 `TFlowData` 仍要求至少一个 `intermediateExchange`，因为该元素的 `minOccurs` 未显式设置，默认值为 `1`。教学结果文件用这个元素承载参考输出，而不保留上游电力输入。因此，不能以是否存在任意中间交换判断 UPR，也不能仅凭 `type=2` 确认某份文件已提供 LCIA。这个说明与模式之间的差异需要保留；各种真实 LCI、LCIA 导出的具体内容仍须结合其来源和文件核对。这里的 terminated 不能理解成“设备停运”或“废物寿命终结”。在提取供应链连接或过程间产品流之前，先检查这一属性，避免把汇总清单当成保留供应商结构的单元过程。

属性 `specialActivityType` 进一步说明活动在数据库中的作用。值 `0` 是普通转化活动：输入被转化为不同的输出，范围包括开采、生产、运输、消费和废物处理。值 `1` 是市场活动：它不转化输入，而把生产者的中间输出传递给消费者，通常混合不同生产者的类似产品，形成消费组合。值 `10` 是市场组：它把市场再按区域汇集；在未指定系统模型中仅有参考产品，链接算法会加入地理范围内、参考产品相同的供应市场。值 `2` 是来自国家供给使用表的投入产出活动，通常表示特定行业的供给与使用；值 `3` 是残余活动，是从同一年、同一地区、同一活动类别的供给使用数据中减去已有单元过程后得到的部分。读取时应据此区分“生产产品的过程”“把产品连接起来的市场”和“统计表中的行业活动”。

其余类型描述组合、贸易和修正。`specialActivityType=4` 是某地区内供应者按生产量加权的生产组合；`5` 是指定产品进入指定地区的进口活动，仅用于国家平衡核算，不参与自动生成的消费组合。进入行政约束市场或来自部分孤立市场的进口，为纳入消费组合而按普通转化活动建模。值 `6` 是在生产组合中加入进口的供应组合。值 `7` 是国家生产组合的出口量，地理范围为该国，不参与自动消费组合；为得到正确出口价值，还直接纳入市场通常承担的运输、生产损失、批发零售活动、产品税和补贴。值 `8` 是地区的再出口量，同样不参与自动消费组合。值 `9` 是修正活动：它以正流和负流各加入一次，把交换从系统的一处移到另一处，用来修正上游活动的下游效应或分配造成的质量平衡偏差。不能把这些代码只当显示标签；它们解释了某些记录为何不直接代表普通生产。

判断活动是否适用于研究，还需读取边界说明。`includedActivitiesStart` 描述起点；对 `type=2`，起点始终为从摇篮开始并包括全部上游活动。对单元过程，它可描述原材料接收或服务所需投入等起点。`includedActivitiesEnd` 不只是终点名称，还说明活动中包含的步骤及有意排除的活动或输入，最后交代最后一道活动或交付点。例如，作为服务的农药施用可排除农药本身，从而适用于不同有效成分。`generalComment` 容纳无法放入更专门字段的一般说明和引用，信息应足以帮助判断数据集适用性。它是 `TTextAndImage`，读取时应考虑文本、图片与变量及其顺序；通用说明写 `imageUri`，但本版 XSD 的实际图像元素名是 `imageUrl`，这是文档命名不一致，解析时须对照实际模式。`synonym` 提供同义词，允许 `0..n` 个条目，每个最长 80 个字符，且同一 `xml:lang` 可以出现多条。`tag` 是用于筛选、分组和搜索的开放关键词列表；不在 `validTags` 主文件中的标签应产生提示信息，而不是语义验证错误。`datasetIcon` 是图标的 URI，可用于快速识别、品牌或公司徽标；图标存放于本地或网络服务器，通过 Http 获取，并非嵌入数据集本身。

若存在 `parentActivityId`，应先解析继承，再把当前文件当成完整记录取数。它引用父活动数据集；`parentActivityContextId` 指定父活动所在上下文，省略时使用当前数据集上下文。子活动承接父字段，只存储相对父活动的变化。空字段表示沿用父值，填写的新内容覆盖父值；字符串中的 `{{PARENTTEXT}}` 把父文本插入指定位置。`TTextAndImage` 还支持文本变量 `{{text_variables}}` 和引用形式 `{{variablename}}`，允许子活动重新定义变量而保留其他父文本。具有数学关系的数量字段可在 `mathematicalRelation` 中使用 `PARENTVALUE`，例如原说明中的 `PARENTVALUE*0.5` 将父数量减半。因而，子文件未写某字段不能直接解释为零值或不存在。原说明指出，子数据集不能按完整 EcoSpold02 活动的数据模式要求直接验证；官方包同时提供子模式。这里还要区分元素与类型的命名空间：根元素 `ecoSpold` 及其外层容器 `activityDataset`、`childActivityDataset` 都属于 `http://www.EcoInvent.org/EcoSpold02`；其中 `childActivityDataset` 使用属于 `http://www.EcoInvent.org/EcoSpold02Child` 的 `TActivityDataset` 类型，其内部 `activityDescription` 等元素也属于这个子命名空间。读取和校验应区分完整记录与差异记录，并按元素实际命名空间选择路径。

属性 `inheritanceDepth` 默认是 `0`。原说明将其定义为当前数据集的父数据集最大数量，又给出 `0` 为非子数据集、`1` 为地理子数据集、`2` 为时间子数据集、`3` 为宏观经济情景子数据集的解释。层数和类型的对应关系仍需依据继承专门规范确认；不能仅凭这一数值自行构造父链，实际父对象仍由 `parentActivityId` 引用。

能源和分配信息也属于活动描述。`energyValues` 默认 `0`，表示未指定；`1` 表示净值，即低位热值；`2` 表示总值，即高位热值。它声明能源数值的口径，不是另一笔能源交换。`masterAllocationPropertyId` 引用全数据集默认分配属性，`masterAllocationPropertyContextId` 指定该属性所属上下文，省略时沿用数据集上下文；某交换可通过自己的 `specificAllocationPropertyId` 覆盖这一默认属性。按原说明，某输出的分配因子等于该输出的 `TProperty` 值乘输出数量，再除以所有输出相应乘积的总和。`allocationComment` 解释分配程序和选择该属性的理由，也可说明采用物理、经济等不同参数却得到相同分配因子的情况。若子数据集要删除默认分配属性的引用，必须把 `masterAllocationPropertyIdOverwrittenByChild` 设为 `true`；单纯不写引用会被解释为保留父值。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学活动的身份、边界与默认分配属性

[下载本段 XML](xml-examples/activity-01.xml)。

```xml
<activity xmlns="http://www.EcoInvent.org/EcoSpold02" id="19d3e06c-2a4a-545d-b368-6470e75e1a27" activityNameId="b0ce0613-267e-5be2-82cd-160d5a5d5d4f" activityNameContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" type="1" specialActivityType="0" inheritanceDepth="0" energyValues="1" masterAllocationPropertyId="4df2fd06-35ca-5aa5-974e-aa71280a96ef" masterAllocationPropertyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" masterAllocationPropertyIdOverwrittenByChild="false" datasetIcon="https://example.invalid/teaching/product-icon.svg">
  <!-- 教学构造；UUID及分配属性不是实际ecoinvent主数据。 -->
  <activityName xml:lang="zh">教学产品单元过程</activityName>
  <synonym xml:lang="zh">教学材料生产</synonym>
  <synonym xml:lang="zh">构造产品制造</synonym>
  <includedActivitiesStart xml:lang="zh">从接收教学原料开始。</includedActivitiesStart>
  <includedActivitiesEnd xml:lang="zh">包括厂内加工和产品装车，不包括后续使用。</includedActivitiesEnd>
  <allocationComment><text index="1" xml:lang="zh">教学示意：默认使用指定属性进行分配；具体属性值须从各输出交换读取。</text></allocationComment>
  <generalComment><text index="1" xml:lang="zh">教学构造，非真实数据；用于展示活动元信息，不提供分配计算结果。</text></generalComment>
  <tag>teaching</tag>
  <tag>product</tag>
</activity>
```

这个 activity 片段通常放在 activityDescription 内。所有值均为教学构造；它依官方 TActivity 顺序放置子元素，必填身份属性完整，但不构成一份完整 .spold，也不证明虚构主数据引用可被解析。

### 示例 2：子活动引用与明确移除父分配属性

[下载本段 XML](xml-examples/activity-02.xml)。

```xml
<activity xmlns="http://www.EcoInvent.org/EcoSpold02" id="1e2c8927-d64d-5549-ada7-cef8f77ea70b" activityNameId="b0ce0613-267e-5be2-82cd-160d5a5d5d4f" activityNameContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" type="1" specialActivityType="0" parentActivityId="19d3e06c-2a4a-545d-b368-6470e75e1a27" parentActivityContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" inheritanceDepth="1" masterAllocationPropertyIdOverwrittenByChild="true">
  <!-- 教学构造：以普通类型的完整片段显示子活动引用及删除标记的位置；不是稀疏子文档。 -->
  <activityName xml:lang="zh">教学产品单元过程</activityName>
  <generalComment><text index="1" xml:lang="zh">教学地理子活动：移除从父活动继承的默认分配属性引用。</text></generalComment>
</activity>
```

第二个片段用 parentActivityId 指向第一个教学活动，inheritanceDepth=1 表示教学地理继承层级，并用 true 标记移除继承的分配属性，因此不再填写 masterAllocationPropertyId。这里为了展示普通类型中各属性位置而给出完整身份字段；真实稀疏子文档使用 EcoSpold02Child 模式和相应命名空间，不能把这个片段当作已经完成继承展开的整个文件。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`activityName`（FieldID 100）**：第一个示例的 `activityName` 子元素写着“教学产品单元过程”。按命名空间查找全部同名子元素，并同时读取 `xml:lang="zh"`；这是活动的可读名称，不是唯一身份。

**`@id`（FieldID 102）**：根元素上的 `id="19d3e06c-2a4a-545d-b368-6470e75e1a27"` 标识活动本身，第二例则有不同的子活动 UUID。用属性读取取得它；它不等于名称主数据 UUID，也不等于交换实例 UUID，比较记录时还要带上文件上下文及版本。

**`@activityNameId`（FieldID 105）**：`activityNameId="b0ce0613-267e-5be2-82cd-160d5a5d5d4f"` 引用活动名称主数据，两例可共用这一名称身份。提取该属性并与名称上下文配对，不能把它误用为 `activityLinkId` 所引用的活动实例身份。

**`@activityNameContextId`（FieldID 106）**：`activityNameContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 显式指定名称主数据上下文。若真实文件省略此可选属性，应使用 `fileAttributes/@contextId` 的有效上下文；文件自身也缺少上下文时，不能自行虚构可解析的主数据来源。

**`@type`（FieldID 110）**：示例的 `type="1"` 表示单元过程；`2` 表示系统终止数据集。读取整数码而不是用名称猜测阶段；原文将终止系统描述为包含全部上游的累计环境交换和影响结果，但实际导出仍需核对，不能只凭此码断定所有字段一定存在。

**`@specialActivityType`（FieldID 115）**：`specialActivityType="0"` 将本例标为普通转换活动，范围包括生产、运输等改变投入输出的活动。其他码为 1 市场、10 市场组、2 IO 活动、3 剩余活动、4 生产组合、5 进口、6 供应组合、7 出口、8 再出口、9 校正活动；保留编码以便筛选，不把本字段当成上一项的数据阶段。

**`generalComment`（FieldID 120）**：`generalComment/text` 的“教学构造，非真实数据”是活动的一般说明。先找 `generalComment`，再按 `text/@index` 和语言读取内容；图像实际元素名是 XSD 的 `imageUrl`，不是原说明混用的 `imageUri`，该源文疑点仍需保留。

**`@parentActivityId`（FieldID 130）**：第二例的 `parentActivityId="19d3e06c-2a4a-545d-b368-6470e75e1a27"` 明确引用第一例的父活动。提取后需要获取相应父数据集才能解释继承，不能仅以这个 UUID 声称父数据已经加载。真实子文档中的留空通常表示保留父值，填写内容表示覆盖，也有 `{{PARENTTEXT}}`、文本变量和公式 `PARENTVALUE` 等专门规则，不能用简单字典合并替代完整继承处理。

**`@parentActivityContextId`（FieldID 131）**：第二例的 `parentActivityContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 指定父活动引用的上下文。将它与父 UUID 一起保存；省略时才回退到子文件自身上下文，不能沿用名称上下文来替代。

**`@inheritanceDepth`（FieldID 135）**：两例的 `inheritanceDepth` 分别为 `0` 和 `1`，即非子活动与教学地理子活动。原文以该值表示最大父层数，ecoinvent 约定 2 为时间子活动、3 为宏观经济情景子活动；它是整数元信息，不是要求读取器凭数字构造缺失的父链。

**`includedActivitiesStart`（FieldID 145）**：第一个示例的 `includedActivitiesStart` 写“从接收教学原料开始”，指过程边界起点。它是可重复的多语言直接文本，读取元素文本与语言；终止系统的原文起点为从摇篮包含所有上游，本例 `type=1` 的厂门起点不能外推为累计范围。

**`includedActivitiesEnd`（FieldID 150）**：`includedActivitiesEnd` 说明包括厂内加工和装车，明确排除后续使用。读取直接文本，保留包含项、排除项和最终交付点；不能只把“装车”当作一句描述而遗漏使用阶段不在边界内这一限定。

**`synonym`（FieldID 170）**：示例有两个 `synonym`，均为 `xml:lang="zh"`，分别是“教学材料生产”和“构造产品制造”。必须读取全部同名元素；同义词允许同语言多条，每条最多 80 字符，不能按语言字典覆盖成最后一条。

**`tag`（FieldID 175）**：两个 `tag` 的值是 `teaching` 和 `product`，用于关键词筛选、分组与检索。读取全部直接文本；它们是开放标签，不是主数据 UUID，原文规定未在预定义标签表中找到时只提示信息，不据此判断格式错误。

**`@energyValues`（FieldID 180）**：第一个示例的 `energyValues="1"` 表示净值，即低位热值；2 表示总值或高位热值，0 表示未定义且是默认值。提取整数码后再解释能量口径，不能把这里的“净值”误当成正负交换求和所得的净排放。

**`@masterAllocationPropertyId`（FieldID 190）**：`masterAllocationPropertyId="4df2fd06-35ca-5aa5-974e-aa71280a96ef"` 引用所有交换的默认分配属性，真实属性值要从输出的 `property` 读取，个别交换还可用 `specificAllocationPropertyId` 覆盖。原文分配因子是某输出的属性值乘输出量，再除以全部相应输出乘积之和；片段没有输出数据，不能据 UUID 直接算出分配比例。

**`@masterAllocationPropertyContextId`（FieldID 191）**：`masterAllocationPropertyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 指明该默认分配属性的主数据上下文。与属性 UUID 一起提取；省略时采用文件自身上下文，不与父活动上下文自动视为同一含义。

**`@masterAllocationPropertyIdOverwrittenByChild`（FieldID 192）**：第一例的 `masterAllocationPropertyIdOverwrittenByChild="false"` 没有请求删除；第二例将它设为 `true` 且省略该引用，示意明确移除继承值。读取布尔词法值并保留缺失状态；单独省略引用通常表示保留父值，不能当作删除，真实操作仍须在正确的子文档继承流程中处理。

**`allocationComment`（FieldID 195）**：`allocationComment/text` 写明默认分配属性仅作示意、实际值要从输出交换读取。它是有索引的文本图像说明，不是公式求值字段；读取有序内容可了解分配依据和限制，不能从文字说明直接替换原有数量。

**`@datasetIcon`（FieldID 200）**：`datasetIcon` 是指向 `https://example.invalid/teaching/product-icon.svg` 的 URI 属性。它表示外部图标位置，不是 XML 内嵌图像；示例地址刻意不是真实资源，读取 URI 不等于图标可访问，也不应为提取数值自动下载图像。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/activity-01.xml").getroot()
FIELDS = {
    "100": "activityName",
    "102": "@id",
    "105": "@activityNameId",
    "106": "@activityNameContextId",
    "110": "@type",
    "115": "@specialActivityType",
    "120": "generalComment",
    "130": "@parentActivityId",
    "131": "@parentActivityContextId",
    "135": "@inheritanceDepth",
    "145": "includedActivitiesStart",
    "150": "includedActivitiesEnd",
    "170": "synonym",
    "175": "tag",
    "180": "@energyValues",
    "190": "@masterAllocationPropertyId",
    "191": "@masterAllocationPropertyContextId",
    "192": "@masterAllocationPropertyIdOverwrittenByChild",
    "195": "allocationComment",
    "200": "@datasetIcon",
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
LOCATIONS = ['es:activityDescription/es:activity']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要确认活动身份、单元过程或汇总结果、边界和继承关系时，先读取本节。显示名称用 activityName，关联对象用 id 与有效上下文；不要把 activityNameId 当成活动 UUID。遇到 parentActivityId 时先处理继承，再取数量。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/activity`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TActivity")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/activity[1]",
  "attributes": {
    "id": "19d3e06c-2a4a-545d-b368-6470e75e1a27",
    "activityNameId": "b0ce0613-267e-5be2-82cd-160d5a5d5d4f",
    "type": "1",
    "specialActivityType": "0"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}activityName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学产品单元过程"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}activityName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching product unit process"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tactivity)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
