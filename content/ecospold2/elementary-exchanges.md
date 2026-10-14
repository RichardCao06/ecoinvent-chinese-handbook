# 基本流交换专用字段

对应官方格式类型：`TElementaryExchange`。本篇以文章解释该类型的 6 条字段；复合类型也会说明它们依附在哪个对象上。

## 基本流交换记录与环境的往来 <a href="#read-telementaryexchange" id="read-telementaryexchange"></a>

`TElementaryExchange` 表示单元过程与环境之间的基本流输入或输出，同样继承 `TCustomExchange` 的实例标识、数量、单位、来源和不确定性等共同字段。与中间产品的识别方式相对应，必需的 `elementaryExchangeId` 引用基本流的主数据条目，而可选的 `elementaryExchangeContextId` 指明该主数据所属上下文，省略时使用数据集自身上下文。取数时应保留这个基本流标识，同时保留交换实例 `id`；一个用于识别流，另一个用于识别本数据集中的具体记录。

基本流的分组值与中间交换不同：`inputGroup` 的有效值 4 表示来自环境，`outputGroup` 的有效值 4 表示流向环境。两者仍然只能选择一个，不能因为中间交换有材料、能源或参考产品分组，就把同一套编号移用于基本流。来自环境的资源获取、流向环境的释放，都要结合分组理解；数量的符号不能替代分组判定，也不应在未理解模型含义之前被删除。

必需的 `compartment` 提供区室与子区室的配对信息，由 `TCompartment` 的内部结构表达。原说明中的 `validCompartments` 所引用 XML 文档定义给定语言下有效的区室／子区室配对。可选的 `formula` 可补充化学式，例如分子式，但它不代替基本流主数据或区室。读取环境清单时，应同时取出流标识、名称、方向、数量、单位以及区室配对；不能仅按化学名称把不同区室的流合为一个“总排放”，然后假设可以直接使用同一个表征因子。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学示例：0.04 m3 水资源输入

[下载本段 XML](xml-examples/elementary-exchanges-01.xml)。

```xml
<elementaryExchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="9da6137e-52d1-5c5f-930a-fed238b20968" amount="0.04" unitId="ff547598-1a08-5b8b-904c-a0d8a4d032fd" elementaryExchangeId="376dc400-e4fb-5da8-a2fb-2f8c581892cb" elementaryExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" formula="H2O">
        <name xml:lang="zh">水，来自环境（教学）</name>
        <name xml:lang="en">Water, from environment (synthetic)</name>
        <unitName xml:lang="zh">m3</unitName>
        <unitName xml:lang="en">m3</unitName>
        <compartment subcompartmentId="9bfcfd12-1b84-56cf-8bd8-1abc71a30268" subcompartmentContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
          <compartment xml:lang="zh">自然资源</compartment>
          <compartment xml:lang="en">natural resource</compartment>
          <subcompartment xml:lang="zh">水</subcompartment>
          <subcompartment xml:lang="en">in water</subcompartment>
        </compartment>
        <inputGroup>4</inputGroup>
      </elementaryExchange>
```

片段来自教学构造数据，非真实 ecoinvent 记录。水资源输入由 inputGroup=4 表示 From Environment，不是从技术圈购买的水产品。 name/unitName 是继承共同字段；compartment 位于方向元素之前。基本流身份及区室、单位的 UUID 与有效上下文共同用于对照和汇总，名称只供展示。

### 示例 2：教学示例：1.5 kg 化石 CO2 向空气输出

[下载本段 XML](xml-examples/elementary-exchanges-02.xml)。

```xml
<elementaryExchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="8f3bf890-fe29-5b2f-9648-95e9e569b715" amount="1.5" unitId="a4800e12-54b1-5444-a6d0-b48a59529439" elementaryExchangeId="f420b314-c085-57e7-ba47-5cdfa839e9a3" formula="CO2" elementaryExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
        <name xml:lang="zh">二氧化碳，化石源（教学）</name>
        <name xml:lang="en">Carbon dioxide, fossil (synthetic)</name>
        <unitName xml:lang="zh">kg</unitName>
        <unitName xml:lang="en">kg</unitName>
        <compartment subcompartmentId="6bbb1a41-12de-5599-843e-cc02d4084a9a" subcompartmentContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
          <compartment xml:lang="zh">空气</compartment>
          <compartment xml:lang="en">air</compartment>
          <subcompartment xml:lang="zh">未指定</subcompartment>
          <subcompartment xml:lang="en">unspecified</subcompartment>
        </compartment>
        <outputGroup>4</outputGroup>
      </elementaryExchange>
```

片段来自教学构造数据，非真实 ecoinvent 记录。空气排放方向由 outputGroup=4 表示 To Environment，amount=1.5 kg 是直接交换数量。 name/unitName 是继承共同字段；compartment 位于方向元素之前。基本流身份及区室、单位的 UUID 与有效上下文共同用于对照和汇总，名称只供展示。

### 示例 3：教学示例：-0.1 kg 同一基本流的修正输出

[下载本段 XML](xml-examples/elementary-exchanges-03.xml)。

```xml
<elementaryExchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="fff82fe6-92c9-5f26-98e2-3b04663bc952" amount="-0.1" unitId="a4800e12-54b1-5444-a6d0-b48a59529439" elementaryExchangeId="f420b314-c085-57e7-ba47-5cdfa839e9a3" formula="CO2" elementaryExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
        <name xml:lang="zh">二氧化碳，化石源（教学）</name>
        <name xml:lang="en">Carbon dioxide, fossil (synthetic)</name>
        <unitName xml:lang="zh">kg</unitName>
        <unitName xml:lang="en">kg</unitName>
        <compartment subcompartmentId="6bbb1a41-12de-5599-843e-cc02d4084a9a" subcompartmentContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
          <compartment xml:lang="zh">空气</compartment>
          <compartment xml:lang="en">air</compartment>
          <subcompartment xml:lang="zh">未指定</subcompartment>
          <subcompartment xml:lang="en">unspecified</subcompartment>
        </compartment>
        <outputGroup>4</outputGroup>
      </elementaryExchange>
```

片段来自教学构造数据，非真实 ecoinvent 记录。负数量仍配 outputGroup=4，表示该输出记录的修正；不能因负号改为 input。 name/unitName 是继承共同字段；compartment 位于方向元素之前。基本流身份及区室、单位的 UUID 与有效上下文共同用于对照和汇总，名称只供展示。

### 示例 4：教学示例：0.2 kg 生物源 CO2 输出

[下载本段 XML](xml-examples/elementary-exchanges-04.xml)。

```xml
<elementaryExchange xmlns="http://www.EcoInvent.org/EcoSpold02" id="c0b41e55-61ce-5aad-909d-1d01846e83db" amount="0.2" unitId="a4800e12-54b1-5444-a6d0-b48a59529439" elementaryExchangeId="d951f598-3f40-57c4-ba76-71df73f1096b" formula="CO2" elementaryExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" unitContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
        <name xml:lang="zh">二氧化碳，生物源（教学）</name>
        <name xml:lang="en">Carbon dioxide, biogenic (synthetic)</name>
        <unitName xml:lang="zh">kg</unitName>
        <unitName xml:lang="en">kg</unitName>
        <compartment subcompartmentId="6bbb1a41-12de-5599-843e-cc02d4084a9a" subcompartmentContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
          <compartment xml:lang="zh">空气</compartment>
          <compartment xml:lang="en">air</compartment>
          <subcompartment xml:lang="zh">未指定</subcompartment>
          <subcompartment xml:lang="en">unspecified</subcompartment>
        </compartment>
        <outputGroup>4</outputGroup>
      </elementaryExchange>
```

片段来自教学构造数据，非真实 ecoinvent 记录。它的 elementaryExchangeId 与化石源 CO2 不同，即使 formula 同为 CO2，也保持独立 master 身份。 name/unitName 是继承共同字段；compartment 位于方向元素之前。基本流身份及区室、单位的 UUID 与有效上下文共同用于对照和汇总，名称只供展示。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`inputGroup`（FieldID 1600）**：字段 `inputGroup` 位于“教学示例：0.04 m3 水资源输入”的直接子元素 `inputGroup` 中，示例值为 `4`。水例的 inputGroup=4 表示从环境获取 0.04 m3 水资源；取整数码识别 input，与中间交换的技术圈输入区分。同一交换不能同时写 outputGroup，数量为正本身不决定方向。

**`outputGroup`（FieldID 1610）**：字段 `outputGroup` 位于“教学示例：1.5 kg 化石 CO2 向空气输出”的直接子元素 `outputGroup` 中，示例值为 `4`。化石 CO2 主输出和修正输出的 outputGroup 都为 4，表示向环境输出；分别读取 1.5 与 -0.1 的原符号后可在身份完全相同的条件下合计为 1.4，不能将负记录改判为环境输入。

**`@elementaryExchangeId`（FieldID 1615）**：字段 `elementaryExchangeId` 可在“教学示例：0.04 m3 水资源输入”根元素的 `elementaryExchangeId="376dc400-e4fb-5da8-a2fb-2f8c581892cb"` 属性中读到。化石源主输出与修正行共享 elementaryExchangeId，却有不同交换 id；生物源 CO2 使用另一个 master UUID。提取时先保留每行，汇总不得只按相同名称或化学式 CO2 合并。

**`@elementaryExchangeContextId`（FieldID 1616）**：字段 `elementaryExchangeContextId` 可在“教学示例：0.04 m3 水资源输入”根元素的 `elementaryExchangeContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 属性中读到。这个显式属性界定基本流 master 的上下文，省略时回退文件 context；汇总键至少同时保留基本流 ID/context、区室配对 ID/context 和单位 ID/context。

**`compartment`（FieldID 1660）**：字段 `compartment` 对应“教学示例：0.04 m3 水资源输入”的直接子元素 `compartment`，其中包含 `compartment` 子元素。水例的 compartment 子树表示资源/水，化石 CO2 例表示空气/未指定；应递归读取外层 compartment 内的 compartment、subcompartment 和配对 UUID，而非只取第一个文本或凭区室猜方向。

**`@formula`（FieldID 1670）**：字段 `formula` 可在“教学示例：0.04 m3 水资源输入”根元素的 `formula="H2O"` 属性中读到。水例为 H2O，CO2 各例为 CO2；formula 是化学式说明文本，不是数学关系、不执行，也不能据同式将不同来源或区室的基本流 master 合并。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/elementary-exchanges-01.xml").getroot()
FIELDS = {
    "1600": "inputGroup",
    "1610": "outputGroup",
    "1615": "@elementaryExchangeId",
    "1616": "@elementaryExchangeContextId",
    "1660": "compartment",
    "1670": "@formula",
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
LOCATIONS = ['es:flowData/es:elementaryExchange']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

要拿环境取水或污染物排放，遍历 elementaryExchange，并同时保留 elementaryExchangeId、有效上下文、inputGroup/outputGroup、compartment 和单位。负 amount 不会自动把输出变成输入；同名、不同区室或不同流 UUID 的记录不能直接相加。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`flowData/elementaryExchange`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TElementaryExchange")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **4 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/flowData[1]/elementaryExchange[1]",
  "attributes": {
    "id": "9da6137e-52d1-5c5f-930a-fed238b20968",
    "amount": "0.04",
    "unitId": "ff547598-1a08-5b8b-904c-a0d8a4d032fd",
    "elementaryExchangeId": "376dc400-e4fb-5da8-a2fb-2f8c581892cb"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "水，来自环境（教学）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}name",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Water, from environment (synthetic)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-telementaryexchange)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
