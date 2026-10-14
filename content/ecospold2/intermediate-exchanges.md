# 中间交换专用字段

对应官方格式类型：`TIntermediateExchange`。本篇以文章解释该类型的 18 条字段；复合类型也会说明它们依附在哪个对象上。

## 中间交换如何连接产品与供应者 <a href="#read-tintermediateexchange" id="read-tintermediateexchange"></a>

`TIntermediateExchange` 表示单元过程中的产品、服务或废物输入与输出，连接活动与技术圈。它继承共同交换字段，因此一条记录既有交换实例的 `id` 和数量 `amount`，又有引用产品主数据的 `intermediateExchangeId`。后者为必需 UUID，回答“是哪一种中间产品”；可选的 `intermediateExchangeContextId` 指明产品主数据上下文，省略时使用数据集自身的上下文。产品名称相同，不等于实例相同，也不等于供应活动相同。

流向由 `inputGroup` 与 `outputGroup` 表达，XSD 使用二选一结构，每条中间交换只应具有其中一个。输入分组的 1 表示材料／燃料，2 表示电力／热，3 表示服务，5 表示未进一步指定的来自技术圈的流。输出分组的 0 表示参考产品，2 表示副产品，3 表示待处理材料，5 表示存量增加。读参考输出时，应识别 `outputGroup` 为 0 的记录，而不是按名称猜测或挑数值最大的输出。分组说明流向和角色，`amount` 的正负则是另一个维度；不能把所有正数都当输出、负数都当输入，也不能在读文件时不加区分地取绝对值。

参考输出提供理解交换数量的基准，但原始单元过程的参考数量不一定为 1。提取输入和排放后，若研究需要按单位参考产品表达，应先明确所选参考输出、它的数量和单位，以及所用系统模型和已经完成的分配状态，再按适用方法对相关数量作一致缩放。XML 读取本身不自动执行这一归一化；多输出记录也不能仅靠除以任意一个输出量，就当作已经完成产品间分配的结果。

供应者由可选的 `activityLinkId` 显式指定，它是活动链接，不能用本条交换的 `id` 或产品的 `intermediateExchangeId` 代替。`activityLinkContextId` 指明活动链接所属上下文，省略时使用数据集上下文；`activityLinkIdOverwrittenByChild` 则允许子数据集明确移除继承的链接，需设为 `true`，否则仍会保留父值。原说明写明，如果 `activityLinkId` 为空，供应活动由使用本活动地理和时间信息的链接规则确定。因此，空链接不代表没有供应者，更不能自行任选一个同名活动作为供应者。原表还给出“引用另一活动数据集的字段 105”的提示，但该数字在活动部分对应 `activityNameId`，而 XSD 将 `activityLinkId` 声明为 `TActivityIndexEntry` 引用；实现活动匹配时应核对活动索引，不能把这条提示当成交换实例、产品或活动名称标识可以互换的依据。

与每条交换的数量不同，可选的 `productionVolumeAmount` 表示按年计的产品产量，单位与该交换一致。它不是当前参考输出数量，也不是把清单归一化到单位产品时可直接使用的分母。`productionVolumeVariableName` 给产量提供公式简称，命名规则同样是字母 a-z 开头、允许字母数字下划线且不区分大小写。`productionVolumeMathematicalRelation` 通过变量名或 `REF` 引用流、参数和属性；这里有一项已记录的原文疑点：该字段说明把公式结果的目标写成 `amount`，而 XSD 单独定义了产量字段 `productionVolumeAmount`。教程保留这一差异，不根据这段说明把产量公式值写入普通交换数量；需要重新求值时，应确认具体软件的目标字段。

产量有一组独立的来源说明。`productionVolumeSourceId` 引用产量依据的有效来源，`productionVolumeSourceContextId` 指明其上下文，省略时使用数据集上下文。`productionVolumeSourceIdOverwrittenByChild` 设为 `true`，才明确表示在子数据集中移除该来源引用；缺少引用本身仍可能意味着继承父值。`productionVolumeSourceYear` 表示出版、交流或网站最后访问年份；`productionVolumeSourceFirstAuthor` 表示第一作者或现场测量、口头交流、个人书面交流及问卷来源的提供人员，规则对应 `sourceType` 为 4、5、6、7 的情况。可多语言填写的 `productionVolumeComment` 解释产量来源、假设和计算，可选的 `productionVolumeUncertainty` 则用分布及其参数和／或谱系信息记录产量不确定性。最后，可重复的 `classification` 通过分类配对描述产品所属类别。提取产量时应连同这一组依据保存，而不是拿交换的一般来源记录代替产量来源。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学示例：25 kWh 电力输入及显式供应链接

[下载本段 XML](xml-examples/intermediate-exchanges-01.xml)。

```xml
<intermediateExchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="33697568-a16c-54ea-a6db-8275bf713e20" amount="25" unitId="a5533771-6995-50cd-b03c-7a2af998708e" intermediateExchangeId="cf4dd220-d849-5595-92fe-1dac1fcecae7" activityLinkId="44be1818-16fc-56f4-a988-9306a39129df" variableName="electricity_use" isCalculatedAmount="true" mathematicalRelation="electricity_intensity * 10" intermediateExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" activityLinkContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" activityLinkIdOverwrittenByChild="false">
        <name xml:lang="zh">教学电力</name>
        <name xml:lang="en">Teaching electricity</name>
        <unitName xml:lang="zh">kWh</unitName>
        <unitName xml:lang="en">kWh</unitName>
        <uncertainty>
          <lognormal meanValue="25" mu="3.2188758248682006" variance="0.01" varianceWithPedigreeUncertainty="0.04"/>
        </uncertainty>
        <inputGroup>2</inputGroup>
      </intermediateExchange>
```

片段取自教学主过程并补齐上下文与继承标志，不是实际 ecoinvent 数据。inputGroup=2 表示电力/热输入，amount=25 的单位为 kWh。id 标识这条交换实例；intermediateExchangeId 标识电力产品 master；activityLinkId 指向教学电力供应活动的 activity/@id，三者各有作用。共同字段 name、unitName、uncertainty 等遵循 TCustomExchange；末尾方向元素在扩展字段之后。

### 示例 2：教学示例：10 kg 参考输出与独立年度产量

[下载本段 XML](xml-examples/intermediate-exchanges-02.xml)。

```xml
<intermediateExchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="b8754d71-a0c7-5b08-a889-67d6f1146d58" amount="10" unitId="a4800e12-54b1-5444-a6d0-b48a59529439" intermediateExchangeId="c5a1fe25-46d4-5646-9d78-5c10b6bfdeae" intermediateExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" productionVolumeAmount="1000" productionVolumeSourceIdOverwrittenByChild="false" productionVolumeVariableName="annual_product_volume" productionVolumeSourceId="00000000-0000-4000-8000-000000001533" productionVolumeMathematicalRelation="100 * 10" productionVolumeSourceContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" productionVolumeSourceYear="2025" productionVolumeSourceFirstAuthor="Demo A.">
        <name xml:lang="zh">教学产品</name>
        <name xml:lang="en">Teaching product</name>
        <unitName xml:lang="zh">kg</unitName>
        <unitName xml:lang="en">kg</unitName>
        <property propertyId="157cb588-bc77-5666-9107-3791e5783446" amount="1" unitId="00875264-8155-513e-8182-437026535fcb" isDefiningValue="true">
          <name xml:lang="zh">干质量（教学比例）</name>
          <name xml:lang="en">Dry mass (teaching ratio)</name>
          <unitName xml:lang="zh">kg/kg</unitName>
          <unitName xml:lang="en">kg/kg</unitName>
        </property>
        <productionVolumeComment xml:lang="zh">教学年度产量：100 批，每批 10 kg；不代表真实产能。</productionVolumeComment><productionVolumeComment xml:lang="en">Synthetic annual output: 100 batches of 10 kg; not real capacity.</productionVolumeComment><productionVolumeUncertainty><normal meanValue="1000" variance="100" varianceWithPedigreeUncertainty="144"/></productionVolumeUncertainty><classification classificationId="00000000-0000-4000-8000-000000001540" classificationContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"><classificationSystem xml:lang="zh">教学产品分类</classificationSystem><classificationSystem xml:lang="en">Synthetic product classification</classificationSystem><classificationValue xml:lang="zh">教学产品 A</classificationValue><classificationValue xml:lang="en">Teaching product A</classificationValue></classification><outputGroup>0</outputGroup></intermediateExchange>
```

这是教学参考产品输出，outputGroup=0、amount=10 kg 给出本数据集的参考数量。productionVolumeAmount=1000 指年度产量，仍使用 kg，但时间尺度和作用不同，不可用 1000 代替归一化分母 10，也不把产量随交换量归一化。生产量来源、公式、不确定性和产品分类是扩展字段；dry mass 属性仍为 1 kg/kg。所有分类/来源 UUID 为教学标识。原文 productionVolumeMathematicalRelation 对结果写入 amount 的表述存在已记录的歧义；此例把产量结果明确写入 productionVolumeAmount。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`inputGroup`（FieldID 1500）**：字段 `inputGroup` 位于“教学示例：25 kWh 电力输入及显式供应链接”的直接子元素 `inputGroup` 中，示例值为 `2`。电力例的 inputGroup=2 标识 Electricity/Heat 输入；取整数码判断方向为 input。其他合法输入码为 1（材料/燃料）、3（服务）、5（未指定技术圈输入），同一交换只能有 inputGroup 或 outputGroup 中的一个。

**`outputGroup`（FieldID 1510）**：字段 `outputGroup` 位于“教学示例：10 kg 参考输出与独立年度产量”的直接子元素 `outputGroup` 中，示例值为 `0`。参考产品例的 outputGroup=0 标识 ReferenceProduct 输出；唯一正数量参考输出才可作为 amount 比例分母。其他输出码 2/3/5 分别表示副产品、待处理材料和库存增加，不能自动选为参考产品。

**`@intermediateExchangeId`（FieldID 1515）**：字段 `intermediateExchangeId` 可在“教学示例：25 kWh 电力输入及显式供应链接”根元素的 `intermediateExchangeId="cf4dd220-d849-5595-92fe-1dac1fcecae7"` 属性中读到。电力例中的 UUID 标识电力产品 master，参考输出例则指教学产品 master；它区别于交换 id，也区别于 activityLinkId。保留此属性及有效 master context 用于产品匹配。

**`@intermediateExchangeContextId`（FieldID 1516）**：字段 `intermediateExchangeContextId` 可在“教学示例：25 kWh 电力输入及显式供应链接”根元素的 `intermediateExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。这个显式上下文界定 intermediateExchangeId 所属的产品 master 空间；省略时回退 file context。跨文件匹配必须比较产品 UUID 与 context，不能只比名称“电力”。

**`@activityLinkId`（FieldID 1520）**：字段 `activityLinkId` 可在“教学示例：25 kWh 电力输入及显式供应链接”根元素的 `activityLinkId="44be1818-16fc-56f4-a988-9306a39129df"` 属性中读到。该 UUID 指向教学供应电力活动的 activity/@id，而非 activityNameId；官方字段文档中对 105 的旧交叉引用有疑点。提取器保存显式链接，并在同模型、同发布版本及上下文的导出候选中检查；空值不能自行随意选择供应者。

**`@activityLinkContextId`（FieldID 1521）**：字段 `activityLinkContextId` 可在“教学示例：25 kWh 电力输入及显式供应链接”根元素的 `activityLinkContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。此值给出 activityLinkId 所引用活动的上下文；省略时按文件 context 回退。它与产品 master context 分别保存，即使本教学例数值相同，也不能当成同一个字段。

**`@activityLinkIdOverwrittenByChild`（FieldID 1522）**：字段 `activityLinkIdOverwrittenByChild` 可在“教学示例：25 kWh 电力输入及显式供应链接”根元素的 `activityLinkIdOverwrittenByChild="false"` 属性中读到。此例 false 没有要求移除父供应活动引用；在子数据集里 true 加上省略 activityLinkId 才表示显式清除，而普通缺失可表示保留父值。读取后应在继承展开阶段解释该标志。

**`@productionVolumeAmount`（FieldID 1530）**：字段 `productionVolumeAmount` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeAmount="1000"` 属性中读到。参考输出例的 1000 是每年 1000 kg 的教学产量，不是本过程参考产品的 10 kg。读取原始年度产量，不用它作交换归一化分母，也不把产量除以 10。

**`@productionVolumeSourceIdOverwrittenByChild`（FieldID 1531）**：字段 `productionVolumeSourceIdOverwrittenByChild` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeSourceIdOverwrittenByChild="false"` 属性中读到。参考输出例 false 未要求清除父产量来源；该属性只控制 productionVolumeSourceId 的继承清除，不能与外层共同 sourceIdOverwrittenByChild 互换。

**`@productionVolumeVariableName`（FieldID 1532）**：字段 `productionVolumeVariableName` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeVariableName="annual_product_volume"` 属性中读到。`annual_product_volume` 是公式引用该产量数值的变量名；作为字符串保存，与普通交换 variableName 所引用的 amount 明确区分。

**`@productionVolumeSourceId`（FieldID 1533）**：字段 `productionVolumeSourceId` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeSourceId="00000000-0000-4000-8000-000000001533"` 属性中读到。此 UUID 引用年度产量的教学来源 master，而不是电力交换或普通数量的来源；提取时和 productionVolumeSourceContextId 一起保存以便追溯。

**`@productionVolumeMathematicalRelation`（FieldID 1534）**：字段 `productionVolumeMathematicalRelation` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeMathematicalRelation="100 * 10"` 属性中读到。`100 * 10` 是教学产量公式，对应 1000 kg/年。源文称结果写入 amount 的表述与 productionVolumeAmount 字段存在已记录歧义；此例明确保存产量字段的值和公式，读取时不覆盖 amount=10、不执行公式。

**`productionVolumeComment`（FieldID 1535）**：字段 `productionVolumeComment` 位于“教学示例：10 kg 参考输出与独立年度产量”的直接子元素 `productionVolumeComment` 中，示例值为 `教学年度产量：100 批，每批 10 kg；不代表真实产能。 / Synthetic annual output: 100 batches of 10 kg; not real capacity.`。中英文 productionVolumeComment 说明“100 批，每批 10 kg”的教学年度范围；读取全部语言的说明，区分年度产量假设与当前参考产品的过程数量。

**`@productionVolumeSourceContextId`（FieldID 1536）**：字段 `productionVolumeSourceContextId` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeSourceContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。该属性给出产量来源的上下文，省略时采用文件 context；它不替代普通 sourceContextId，两个来源引用应分别提取。

**`@productionVolumeSourceYear`（FieldID 1537）**：字段 `productionVolumeSourceYear` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeSourceYear="2025"` 属性中读到。`2025` 记录年度产量来源的出版、交流或访问年份；按原字符串保存，不能拿来替代 activityDescription/timePeriod。

**`@productionVolumeSourceFirstAuthor`（FieldID 1538）**：字段 `productionVolumeSourceFirstAuthor` 可在“教学示例：10 kg 参考输出与独立年度产量”根元素的 `productionVolumeSourceFirstAuthor="Demo A."` 属性中读到。`Demo A.` 是产量来源第一作者或沟通者的教学标签，供追溯产量假设；与共同数量来源作者即使相同也应分别存储。

**`productionVolumeUncertainty`（FieldID 1539）**：字段 `productionVolumeUncertainty` 对应“教学示例：10 kg 参考输出与独立年度产量”的直接子元素 `productionVolumeUncertainty`，其中包含 `normal` 子元素。productionVolumeUncertainty/normal 中 meanValue=1000、variance=100、varianceWithPedigreeUncertainty=144 描述年度产量的不确定性；它与交换 uncertainty 是两个不同子树，不要把其均值或方差写回普通 amount。

**`classification`（FieldID 1540）**：字段 `classification` 对应“教学示例：10 kg 参考输出与独立年度产量”的直接子元素 `classification`，其中包含 `classificationSystem` 子元素。classification 子元素将教学分类系统和“教学产品 A”配对，classificationId 引用分类值 master；保留分类 UUID、context 及多语言标签，用于产品分类检索，不能把它当成活动分类或方向码。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/intermediate-exchanges-01.xml").getroot()
FIELDS = {
    "1500": "inputGroup",
    "1510": "outputGroup",
    "1515": "@intermediateExchangeId",
    "1516": "@intermediateExchangeContextId",
    "1520": "@activityLinkId",
    "1521": "@activityLinkContextId",
    "1522": "@activityLinkIdOverwrittenByChild",
    "1530": "@productionVolumeAmount",
    "1531": "@productionVolumeSourceIdOverwrittenByChild",
    "1532": "@productionVolumeVariableName",
    "1533": "@productionVolumeSourceId",
    "1534": "@productionVolumeMathematicalRelation",
    "1535": "productionVolumeComment",
    "1536": "@productionVolumeSourceContextId",
    "1537": "@productionVolumeSourceYear",
    "1538": "@productionVolumeSourceFirstAuthor",
    "1539": "productionVolumeUncertainty",
    "1540": "classification",
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
LOCATIONS = ['es:flowData/es:intermediateExchange']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

要拿电力、材料、服务或参考产品，遍历 intermediateExchange，依据 inputGroup/outputGroup 确定方向，再匹配 intermediateExchangeId 与有效上下文。参考输出用 outputGroup=0；原始 quantity 保留符号，相对于参考量的比例见实践章。沿供应链查询还要核对 activityLinkId、模型和数据库发布版本。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/intermediateExchange`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TIntermediateExchange")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **2 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

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

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tintermediateexchange)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
