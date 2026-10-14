# 文件属性

对应官方格式类型：`TFileAttributes`。本篇以文章解释该类型的 13 条字段；复合类型也会说明它们依附在哪个对象上。

## 区分数据库发布版本、数据集修订版本和文件时间 <a href="#read-tfileattributes" id="read-tfileattributes"></a>

`administrativeInformation/fileAttributes` 采用 `TFileAttributes`，描述文件整体信息。属性 `majorRelease` 和 `minorRelease` 属于发布版本：主发布号在重大更新时加一，次发布号在两次重大更新之间的每次发布时加一。原文以每两年一次为重大更新的例子，但这不是由格式规定的固定发布日程。属性 `majorRevision` 和 `minorRevision` 则区分某个数据集本身的修订，独立于数据库发布版本。因此，程序应将发布版本和数据集修订版本分别保存，而不是拼成一个失去角色区分的版本字段。

`majorRevision` 反映数据集已获接受的变更，只能随时间增加，不得手动更改。在 ecoinvent 上下文中，活动变更通过审查并加入数据库后，它增加，同时将 `minorRevision` 重置为 `1`。`minorRevision` 描述提交审查前编辑过程中的版本；数据提供者每次将修改保存到本地或作为服务器草稿保存时，它自动增加。读取一份草稿与已接受版本时，应据此理解修订状态，不能把文件较新的时间戳直接等同于已接受的内容变更。

时间属性同样需要分开。`creationTimestamp` 是数据集创建时自动生成的日期时间，`lastEditTimestamp` 是保存数据集时自动生成的日期时间；`fileTimestamp` 是当前文件创建的日期时间。前两者描述数据集的创建和编辑，后者描述文件生成，它们都不替代 `timePeriod` 的数据有效日期。`fileGenerator` 说明创建文件的程序，最好包括软件版本；`internalSchemaVersion` 说明生成数据集所依据的内部模式版本。记录这些信息，有助于判断解析环境和追踪导出来源。

属性 `defaultLanguage` 为多语言字段指定默认语言，在完整数据 XSD 中省略时为 `en`；子差异文件省略该属性时应先处理继承，不能绕过父值直接取 `en`。每个多语言字段至少应有默认语言的值。提取活动名称等多语言元素时，应先选择相应语言内容，并保留语言标识，而不是把不同语言的重复元素当成重复数据。元素 `contextName` 是上下文名称，属性 `contextId` 是数据集所面向上下文的 UUID。上下文可用于限制信息访问范围，并决定解析引用时需要哪些主数据文件；它取代旧 ecoSpold01 的 quality network，ecoinvent 质量网络对应的上下文 ID 可在 `Context.xml` 中查找。

缺少 `contextId` 时，说明将文件视为独立数据集，主数据引用不能被解析为实际主数据内容。这与缺少某个可选的 `…ContextId` 属性不同：后者通常沿用数据集上下文，但前提是这个上下文已经可知。元素 `requiredContext` 可重复出现，采用 `TRequiredContextReference`，用于列明完整读取主数据引用所需的其他上下文。真正取数前，应先识别本文件的上下文及所需上下文，再尝试连接各个名称、地点、人员、来源和属性的 UUID。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：文件身份、四段版本与主数据依赖

[下载本段 XML](xml-examples/file-attributes-01.xml)。

```xml
<fileAttributes xmlns="http://www.EcoInvent.org/EcoSpold02" majorRelease="1" minorRelease="0" majorRevision="2" minorRevision="1" defaultLanguage="zh" creationTimestamp="2025-01-01T00:00:00Z" lastEditTimestamp="2025-02-01T10:00:00Z" internalSchemaVersion="2.0.13" fileGenerator="Teaching XML generator 1.0" fileTimestamp="2025-02-01T10:05:00Z" contextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
  <!-- 教学版本号和时间戳；不是实际ecoinvent发布记录。 -->
  <contextName xml:lang="zh">教学主数据上下文（虚构UUID）</contextName>
  <requiredContext majorRelease="1" minorRelease="0" majorRevision="2" minorRevision="1" requiredContextId="d5a99c56-eb38-567d-badd-f9294284f8f6" requiredContextFileLocation="https://example.invalid/teaching/master-data/">
    <requiredContextName xml:lang="zh">教学依赖主数据上下文</requiredContextName>
  </requiredContext>
</fileAttributes>
```

fileAttributes 位于 administrativeInformation。四段数字是教学版本，2.0.13 是所依的内部格式版本；contextName 先于 requiredContext，后者引用一个与本文件自身不同的教学主数据上下文。片段中的URI只展示目录位置，不表示文件可实际下载。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@majorRelease`（FieldID 3800）**：`majorRelease="1"` 是示例数据库主发布部分。读取整数并保留四段版本；原文说主要更新时递增，这里的1不是 ecoinvent 当前主版本，也不能据原文示例时间间隔预测真实发布日程。

**`@minorRelease`（FieldID 3805）**：`minorRelease="0"` 是两次主要更新之间的次发布部分。与 majorRelease 配对记录数据库发布版本；它不同于数据集编辑修订号，不能把四个整数只拼成前两段而丢掉修订身份。

**`@majorRevision`（FieldID 3810）**：`majorRevision="2"` 是本数据集的主修订部分，独立于数据库发布。原文规定接受数据集变更时由系统递增且不应手动改动，同时把 minorRevision 重置为1；本例的教学2不表示真实审核次数。

**`@minorRevision`（FieldID 3815）**：`minorRevision="1"` 表示当前编辑修订部分。原文规定保存本地或服务端草稿时自动增加，接受变更并增加主修订时重置为1；读取完整版本以区分编辑稿，不能把此数当作 XML 模式版本。

**`@defaultLanguage`（FieldID 3820）**：`defaultLanguage="zh"` 指定默认中文，示例的多语言文本均提供 zh 条目。读取属性后用于语言选择及回退；普通 XSD 省略时默认 en，但最小 XML 读取器不一定自动补齐模式默认值，需要明确实现回退。

**`@creationTimestamp`（FieldID 3830）**：`creationTimestamp="2025-01-01T00:00:00Z"` 是数据集建立时刻，Z 表示 UTC。按日期时间读取并保留时区，不把它当作活动数据适用起始日期。

**`@lastEditTimestamp`（FieldID 3840）**：`lastEditTimestamp="2025-02-01T10:00:00Z"` 是数据集最后保存时刻。它晚于创建时刻，但仍不是交换数据的采样年代；比较文件时把它与版本及编辑流程一起保留。

**`@internalSchemaVersion`（FieldID 3850）**：`internalSchemaVersion="2.0.13"` 说明文件基于该内部模式生成。读取字符串并选择对应模式核对结构，不能与 majorRelease=1 混为同一个版本，也不能把格式包v1.0.13与内部模式2.0.13写成同义编号。

**`@fileGenerator`（FieldID 3860）**：`fileGenerator="Teaching XML generator 1.0"` 给出生成软件及其教学版本。按属性保留文字帮助追溯导出工具，不据此推断数据库系统模型或数据内容已经审核。

**`@fileTimestamp`（FieldID 3870）**：`fileTimestamp="2025-02-01T10:05:00Z"` 是导出文件创建时刻，与10:00的最后编辑时刻不同。分别读取这两个日期时间，不能拿文件导出时间替换原数据的适用时间。

**`@contextId`（FieldID 3880）**：`contextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 是文件自身上下文，供缺少显式引用上下文的字段回退。读取后保存到数据集元信息；原文规定省略时视为独立数据集、主数据引用不可解引用，不能从 contextName 或名称文字猜补 UUID。

**`contextName`（FieldID 3885）**：`contextName` 子元素给出“教学主数据上下文（虚构UUID）”。读取元素文本与语言，是 contextId 的可读名称而非身份；旧格式质量网络由上下文机制替代，不能把这个名称当作旧质量网络数字字段。

**`requiredContext`（FieldID 3890）**：`requiredContext` 子元素引用另一个教学上下文 `d5a99c56-eb38-567d-badd-f9294284f8f6`，并携带所需版本及目录信息。要读取全部同名子元素，再进入它们的属性和 requiredContextName；它表示完整加载主数据所需的依赖，不是本文件 contextId 的替代值，解析整个文件前还需确认依赖实际可用。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/file-attributes-01.xml").getroot()
FIELDS = {
    "3800": "@majorRelease",
    "3805": "@minorRelease",
    "3810": "@majorRevision",
    "3815": "@minorRevision",
    "3820": "@defaultLanguage",
    "3830": "@creationTimestamp",
    "3840": "@lastEditTimestamp",
    "3850": "@internalSchemaVersion",
    "3860": "@fileGenerator",
    "3870": "@fileTimestamp",
    "3880": "@contextId",
    "3885": "contextName",
    "3890": "requiredContext",
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
LOCATIONS = ['es:administrativeInformation/es:fileAttributes']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要记录导出来源或匹配供应候选时，读取 fileAttributes，把数据库发布版本、数据集修订版本、contextId 及时间信息分别保存。不要用最新编辑时间替代研究年份，也不要把两个不同系统模型或发布版本里的同一活动 UUID 当成唯一同一候选。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`administrativeInformation/fileAttributes`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TFileAttributes")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/administrativeInformation[1]/fileAttributes[1]",
  "attributes": {
    "majorRelease": "1",
    "minorRelease": "0",
    "majorRevision": "1",
    "minorRevision": "1",
    "internalSchemaVersion": "2.0.13",
    "defaultLanguage": "zh",
    "creationTimestamp": "2025-01-01T00:00:00Z",
    "lastEditTimestamp": "2025-01-01T00:00:00Z",
    "fileTimestamp": "2025-01-01T00:00:00Z",
    "fileGenerator": "Synthetic tutorial generator",
    "contextId": "f71ac544-3bc8-5c15-8ea4-072d907663f1"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}contextName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学主数据上下文（虚构UUID）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}contextName",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching master-data context (synthetic UUIDs)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tfileattributes)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
