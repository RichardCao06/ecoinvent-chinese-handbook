# 数据生成者与发布

对应官方格式类型：`TDataGeneratorAndPublication`。本篇以文章解释该类型的 17 条字段；复合类型也会说明它们依附在哪个对象上。

## 原始数据来源、出版物与访问限制构成另一组管理信息 <a href="#read-tdatageneratorandpublication" id="read-tdatageneratorandpublication"></a>

`administrativeInformation/dataGeneratorAndPublication` 采用 `TDataGeneratorAndPublication`。这里的属性 `personId` 识别收集、汇编或发布原始数据的数据生成者，未必与 `dataEntryBy` 的录入者相同。`personContextId` 指向其人员上下文，省略时沿用数据集上下文；`personName` 和 `personEmail` 分别记录姓名和完整邮箱。读取两个人员组时，要保留各自所属的 XML 路径，即使字段都叫 `personId`，也不能把两种角色覆盖成同一个“作者”。原说明还将数据生成者解释为应获认可的数据来源及承担主要采集工作的个人或组织；当前人员引用须与相应人员主数据匹配。

属性 `dataPublishedIn` 表示发布程度：`0` 是数据本身未在别处发布，也是默认值；`1` 是部分单元过程或子系统已发布；`2` 是数据完整发布于所引用来源。`publishedSourceId` 引用记录数据的报告或来源，`publishedSourceContextId` 指定来源上下文，省略时使用数据集自身上下文。`publishedSourceYear` 记录出版或沟通年份，对网站记录最后访问时间；原文没有限定网站条目只能写年份，实际类型为 `TBaseString30`。`publishedSourceFirstAuthor` 给出第一作者的姓和名字缩写。对于 `sourceType=4, 5, 6, 7` 的现场测量、口头沟通、个人书面沟通和问卷，它记录沟通人员。`pageNumbers` 进一步定位文章或较大出版物中的相关页码。取数时，这些字段共同构成可追溯来源，不能用一个年份或第一作者文本替代来源主数据引用。

原说明出现的旧编号也有明确对应关系：`757` 是 `publishedSourceId` 的旧 SpoldID，当前 fieldId 为 `3520`；它引用的来源 `id` 的旧 SpoldID 是 `801`，当前 fieldId 为 `3110`。这些是编号体系之间的映射，而非需要替换的 XML 名称。在子数据集中，若要删除父数据集的来源引用，必须将 `publishedSourceIdOverwrittenByChild` 设为 `true`；仅省略 `publishedSourceId` 会沿用父引用。

版权和可访问性由不同属性表达。`isCopyrightProtected` 表示是否有著作权，原说明要求对应填写 `1` 或 `0`。`accessRestrictedTo` 默认 `0`，表示无访问限制；`1` 表示只有上下文定义的许可证持有者可访问；`2` 表示这些许可证持有者只能访问 LCI 结果，不能访问单元过程原始数据，而数据库管理员仍具有完整访问权限；`3` 表示只有指定组织及数据库管理员可访问。不能把版权标记当成公开许可，也不能从文件技术上可读推断有权公开传播其中数据。

当访问限制为 `3` 时，`companyId` 引用获准使用数据集的组织或机构，`companyContextId` 指定该组织上下文，省略时使用数据集上下文；`companyCode` 是对应公司的可选代码纯文本。原说明称其为 7 字母代码，`TCompanyCode` 的说明还称应使用大写字母，但本版 XSD 的实际约束只有最长 7 个字符，没有固定长度或字母字符模式；因此，通过 XSD 并不等于已经满足这项文字约定。原文条件 `759=3` 中的 `759` 是 `accessRestrictedTo` 的旧 SpoldID，当前 fieldId 为 `3550`，因此条件应理解为访问限制类别为 `3`，不是另一项编号为 759 的当前属性。若子数据集需要移除组织引用，必须把 `companyIdOverwrittenByChild` 设为 `true`，否则仍视为保留父值。这套规则让程序能够分别处理“继承已有引用”与“明确删除引用”。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：完整发布、出版证据与机构限制

[下载本段 XML](xml-examples/publication-01.xml)。

```xml
<dataGeneratorAndPublication xmlns="http://www.EcoInvent.org/EcoSpold02" personId="901bbfee-b5bd-5006-b40d-ca76e25c03ad" personContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" personName="Teaching generator" personEmail="generator@example.invalid" dataPublishedIn="2" publishedSourceId="a10d3603-b4bd-5a41-b7a0-1319aad7c28a" publishedSourceContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" publishedSourceIdOverwrittenByChild="false" publishedSourceYear="2025" publishedSourceFirstAuthor="Teaching A." pageNumbers="12-18" isCopyrightProtected="true" accessRestrictedTo="3" companyId="d10c3ee0-d8cf-5e58-bbbb-6747c4364856" companyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" companyCode="DEMOORG" companyIdOverwrittenByChild="false">
  <!-- 教学构造：虚构出版物和机构；不表示真实许可条件。 -->
</dataGeneratorAndPublication>
```

本例位于 administrativeInformation，全部字段均为属性。数据生成者不同于录入者；虚构出版物标为完整发表，访问限定给虚构机构。版权和访问限制是两种不同信息，不能相互推断。

### 示例 2：在子数据集明确移除继承来源和机构

[下载本段 XML](xml-examples/publication-02.xml)。

```xml
<dataGeneratorAndPublication xmlns="http://www.EcoInvent.org/EcoSpold02" personId="901bbfee-b5bd-5006-b40d-ca76e25c03ad" personContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1" personName="Teaching generator" personEmail="generator@example.invalid" dataPublishedIn="0" publishedSourceIdOverwrittenByChild="true" isCopyrightProtected="false" accessRestrictedTo="0" companyIdOverwrittenByChild="true">
  <!-- 教学构造：普通类型完整片段示意子数据集删除父来源与父机构引用的标记位置。 -->
</dataGeneratorAndPublication>
```

第二片段省略出版来源和机构 UUID，并各用 OverwrittenByChild=true 明确删除继承引用，同时教学设为未发表、公开访问。它只以普通类型完整字段展示属性位置与删除意图；真实稀疏子文档须在 EcoSpold02Child 模式中处理，并核查其他继承文字是否仍适用。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@personId`（FieldID 3500）**：第一例的 `personId="901bbfee-b5bd-5006-b40d-ca76e25c03ad"` 是收集、汇编或发表原始数据的生成者引用，与录入者的 UUID 不同。按属性提取并关联人员主数据，以追溯数据来源，不能把它误当为评审签名。

**`@personContextId`（FieldID 3501）**：`personContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 指定生成者的人员主数据上下文。与生成者 UUID 配对；可选属性省略时采用文件自身上下文。

**`@personName`（FieldID 3505）**：`personName="Teaching generator"` 给出生成者姓名，存于根属性。读取文字辅助理解，但识别人员仍用 UUID 和上下文，不能只按姓名合并不同角色。

**`@personEmail`（FieldID 3506）**：`personEmail="generator@example.invalid"` 给出生成者的完整邮箱属性。它与录入者邮箱不同，仅为教学构造；读取地址不能证明这个人在实际数据库中存在。

**`@dataPublishedIn`（FieldID 3510）**：第一例 `dataPublishedIn="2"` 表示数据已完整发表在引用来源中；第二例的 0 表示数据本身未在别处发表，1 表示某些单元过程或子系统数据已发表。读取码时同时保留出版来源字段，原表旧字段757对应来源引用，不能把编号当作当前 XML 属性。

**`@publishedSourceId`（FieldID 3520）**：`publishedSourceId="a10d3603-b4bd-5a41-b7a0-1319aad7c28a"` 引用记载数据集的出版报告。用 UUID 与有效来源上下文查找来源主数据；原表的“801”是旧编号引用，不是报告年份，也不是须填入属性的数字。

**`@publishedSourceContextId`（FieldID 3521）**：`publishedSourceContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 指向出版来源的上下文。它与人员上下文是不同引用角色，即使本例值相同也要分别保留；省略时才用数据集自身上下文。

**`@publishedSourceIdOverwrittenByChild`（FieldID 3522）**：第一例 `publishedSourceIdOverwrittenByChild="false"` 保留引用，第二例将它设为 true 并省略 publishedSourceId，示意删除父数据集继承的来源。读取布尔标记并识别缺失引用；仅省略来源而未设 true 通常表示保留父值，不能用空值删除。

**`@publishedSourceYear`（FieldID 3525）**：`publishedSourceYear="2025"` 记录出版或交流年份，类型是文字而非交换数量。网站来源应记最后访问时间；提取时保留原字符串，不将它与 timePeriod 的适用年份自动等同。

**`@publishedSourceFirstAuthor`（FieldID 3526）**：`publishedSourceFirstAuthor="Teaching A."` 示意第一作者姓氏加名字缩写。若来源类型是4现场测量、5口头交流、6个人书面交流或7问卷，应记录信息提供者；这里没有 sourceType，须关联真实来源主数据后判断，不能只凭作者格式猜来源类型。

**`@pageNumbers`（FieldID 3530）**：`pageNumbers="12-18"` 是报告中相关页码的文字范围。读取字符串供追溯，不将短横线当作数学减法，也不把页码作为影响指标数值。

**`@isCopyrightProtected`（FieldID 3540）**：第一例 `isCopyrightProtected="true"` 表示存在版权，第二例为 false。按 XML 布尔值读取，允许的词法形式还包括1和0；版权存在与否不能替代 accessRestrictedTo 的访问条件。

**`@accessRestrictedTo`（FieldID 3550）**：第一例的 `accessRestrictedTo="3"` 表示只允许指定机构和数据库管理员访问，第二例的0表示公开；1为许可证持有人，2为许可证持有人仅可访问LCI结果而非单元过程原数据、管理员可全部访问。原表条件中的759是该属性旧编号，不能当作新的 XML 字段。

**`@companyId`（FieldID 3560）**：`companyId="d10c3ee0-d8cf-5e58-bbbb-6747c4364856"` 在受限示例中引用允许使用数据的机构。以 UUID 加机构上下文查主数据，与 accessRestrictedTo=3 一起解释；公开访问的删除示例没有保留这个机构引用。

**`@companyContextId`（FieldID 3561）**：`companyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 是受限机构的主数据上下文。不要用生成者的人员引用替代机构引用；省略时仅按文件自身上下文回退。

**`@companyCode`（FieldID 3562）**：`companyCode="DEMOORG"` 是所引用虚构机构的7字母可读代码，不是 companyId 的替代键。读取文字辅助阅读并核对实际机构主数据，本教学码不能解释为真实许可方。

**`@companyIdOverwrittenByChild`（FieldID 3563）**：第一例 `companyIdOverwrittenByChild="false"` 不删除机构，第二例 true 配合省略 companyId，示意明确移除父机构引用。提取删除标记时还要核查访问限制及继承的机构代码等信息，不能只删除 UUID 就声称全部许可元信息已经一致。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/publication-01.xml").getroot()
FIELDS = {
    "3500": "@personId",
    "3501": "@personContextId",
    "3505": "@personName",
    "3506": "@personEmail",
    "3510": "@dataPublishedIn",
    "3520": "@publishedSourceId",
    "3521": "@publishedSourceContextId",
    "3522": "@publishedSourceIdOverwrittenByChild",
    "3525": "@publishedSourceYear",
    "3526": "@publishedSourceFirstAuthor",
    "3530": "@pageNumbers",
    "3540": "@isCopyrightProtected",
    "3550": "@accessRestrictedTo",
    "3560": "@companyId",
    "3561": "@companyContextId",
    "3562": "@companyCode",
    "3563": "@companyIdOverwrittenByChild",
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
LOCATIONS = ['es:administrativeInformation/es:dataGeneratorAndPublication']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要追溯原始来源、文献和访问限制时，读取 dataGeneratorAndPublication，并分别保留人员、文献引用和访问相关标记。引用 UUID 须通过相应上下文解析；读取脚本不会凭这些标记判定你拥有传播原始数据库数据的权限。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`administrativeInformation/dataGeneratorAndPublication`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TDataGeneratorAndPublication")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/administrativeInformation[1]/dataGeneratorAndPublication[1]",
  "attributes": {
    "personId": "2163e122-88c4-55e7-af84-00947e9b7b0a",
    "personName": "Teaching author",
    "personEmail": "demo@example.invalid",
    "isCopyrightProtected": "false",
    "dataPublishedIn": "0",
    "accessRestrictedTo": "0"
  },
  "children_excerpt": []
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tdatageneratorandpublication)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
