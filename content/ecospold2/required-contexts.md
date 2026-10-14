# 所需上下文引用

对应官方格式类型：`TRequiredContextReference`。本篇以文章解释该类型的 7 条字段；复合类型也会说明它们依附在哪个对象上。

## 解析跨上下文引用前，先核对主数据依赖 <a href="#read-trequiredcontextreference" id="read-trequiredcontextreference"></a>

每个 `requiredContext` 条目采用 `TRequiredContextReference`，说明读取文件所需的主数据上下文。属性 `requiredContextId` 引用主数据文件所属上下文，元素 `requiredContextName` 提供相应名称；属性 `requiredContextFileLocation` 是可选 URI，指向包含这一上下文主数据文件的目录。它给出的是主数据目录位置，不能直接当成某一条主数据对象的 UUID，也不应未经判断就当成单个 XML 文件路径。

这个条目也有属性 `majorRelease`、`minorRelease`、`majorRevision` 和 `minorRevision`。它们用于确保该活动所需的主数据条目在相应版本中存在，描述的是所依赖上下文的版本要求，不是当前数据集自己的版本。完整 XSD 要求主发布号与次发布号，主修订号与次修订号则为可选。读取程序需知道各上下文，并知道实际主数据文件在哪里；只有 UUID 文本而没有对应主数据文件，并不能完成引用解析。

原文另有一处结构要求与说明冲突：它称省略 `requiredContextId` 时应使用数据集自身上下文，但本版完整 XSD 把这个属性设为必填。因而，不能依据这句回退说明生成缺少该属性却宣称通过完整模式验证的文件。教程保留这项文档差异，具体适用条件需由数据方澄清；在实现当前完整模式时，应核对 `use="required"` 的实际要求。另须区分子差异模式：`EcoSpold02ChildDataTypes.xsd` 将 `requiredContextId` 及四个版本属性设为可选，也将 `requiredContextName` 设为可省略；这并不改变完整数据模式的必填要求。读取子记录时仍须结合继承及实际上下文，不能把省略值直接当成一个已经解析成功的主数据引用。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：一个主数据上下文依赖的完整片段

[下载本段 XML](xml-examples/required-contexts-01.xml)。

```xml
<requiredContext xmlns="http://www.EcoInvent.org/EcoSpold02" majorRelease="1" minorRelease="0" majorRevision="2" minorRevision="1" requiredContextId="d5a99c56-eb38-567d-badd-f9294284f8f6" requiredContextFileLocation="https://example.invalid/teaching/master-data/">
  <!-- 教学构造的依赖上下文与目录；不会解析真实主数据。 -->
  <requiredContextName xml:lang="zh">教学依赖主数据上下文</requiredContextName>
</requiredContext>
```

这个 requiredContext 在完整文档里嵌在 fileAttributes 中，不能直接当作 ecoSpold 根。所有值为教学构造；类型校验可以确认结构和词法，却不能确认版本对应的主数据真的存在。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@majorRelease`（FieldID 7810）**：示例 `majorRelease="1"` 是依赖上下文的主发布要求，用来核查所需主数据条目是否可用。读取后与依赖包的版本信息比较，不把它当作当前活动文件自身的 majorRelease。

**`@minorRelease`（FieldID 7820）**：`minorRelease="0"` 是该依赖的次发布要求。与依赖主发布部分配对，本普通类型中两项必填；字段说明未给出通用的版本兼容算法，不能自行认定任意更高版本都可安全替代。

**`@majorRevision`（FieldID 7830）**：`majorRevision="2"` 是依赖上下文的主修订要求，而非当前活动数据集接受变更的次数。它在普通 XSD 中可选；提取时区分省略与显式2，不把缺失自动补为0。

**`@minorRevision`（FieldID 7840）**：`minorRevision="1"` 是依赖上下文的次修订要求。与其他版本部分共同保留以核查主数据，这个可选值缺失时不能直接套用当前文件的 minorRevision。

**`@requiredContextId`（FieldID 7850）**：`requiredContextId="d5a99c56-eb38-567d-badd-f9294284f8f6"` 明确引用所需主数据上下文。原文说省略时用数据集上下文，但普通 XSD 将该属性设为必填，所以本例显式提供；不能擅自省略以消除原文与模式的矛盾，应由数据方澄清适用范围。

**`requiredContextName`（FieldID 7855）**：`requiredContextName` 子元素写“教学依赖主数据上下文”，是上述 UUID 的可读名称。读取全部语言条目；匹配依赖时依然依据 UUID 和版本，不只依赖名称相似。

**`@requiredContextFileLocation`（FieldID 7860）**：`requiredContextFileLocation="https://example.invalid/teaching/master-data/"` 是指向主数据目录的可选URI，不是一项数据集数量或某个具体流文件。保留地址并按自己的文件获取策略处理，本教学地址不会提供真实文件；URI存在不能证明依赖已加载，也不能替代上下文UUID。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/required-contexts-01.xml").getroot()
FIELDS = {
    "7810": "@majorRelease",
    "7820": "@minorRelease",
    "7830": "@majorRevision",
    "7840": "@minorRevision",
    "7850": "@requiredContextId",
    "7855": "requiredContextName",
    "7860": "@requiredContextFileLocation",
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
LOCATIONS = ['es:administrativeInformation/es:fileAttributes/es:requiredContext']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要解析跨上下文的主数据 UUID 时，遍历 requiredContext，每条保留引用 UUID、描述和完整版本标记。它列出依赖，不会把外部主数据内容自动嵌入 XML；缺少所需上下文时应报告无法完整解析，而不是编造名称或覆盖为当前上下文。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`administrativeInformation/fileAttributes/requiredContext`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TRequiredContextReference")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-trequiredcontextreference)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
