# 审查

对应官方格式类型：`TReview`。本篇以文章解释该类型的 11 条字段；复合类型也会说明它们依附在哪个对象上。

## 审查记录：把意见、人员和所审版本对应起来 <a href="#read-treview" id="read-treview"></a>

`review` 位于 `modellingAndValidation` 中，采用 `TReview` 类型，记录开展鉴定性评审的人员、主要结果、结论和建议。父级允许多个 `review`，因此一份数据集可以有多位评审者或多条审查记录；读取时不能只取第一条便覆盖其余意见。另一方面，一条记录包含的姓名、日期和意见只证明它记录了一次评审，并不自动代表整个数据库已获官方认证。

每条评审由 `reviewerId` 引用人员主数据，原表将它对应到人员字段 3610；`reviewerContextId` 指定人员上下文，省略时采用数据集自身的上下文。`reviewerName` 记录名字和姓氏，`reviewerEmail` 记录完整电子邮件地址，`reviewDate` 是验证或评审日期。这些信息应共同保留，才能将意见对应到具体评审者及其时间，而不应只凭姓名文本匹配人员身份。

审查所针对的数据集版本由 `reviewedMajorRelease`、`reviewedMinorRelease`、`reviewedMajorRevision` 和 `reviewedMinorRevision` 四个整数属性分别记录，依次对应文件属性中的字段 3800、3805、3810、3815，即主发布、次发布、主修订和次修订部分。它们不是审查记录自身的编号，也不能只保留前两个数字。阅读时应把四部分版本与当前文件的版本信息对照：如果记录针对较早版本，就不能把其意见不加判断地解释为对当前修改后内容的审查结论。正常 XSD 中，这四项版本、评审者引用、姓名、邮件及日期在一条出现的 `review` 内均必填；子数据集需另按其对应模式判断。

详细意见存于可选的 `details`，它使用 `TTextAndImage`，因此可以按 `index` 组织文本与图像，并使用 `variable` 文本变量在继承数据集中改写局部内容。这里同样应以实际的 `imageUrl` 元素名读取，而不是原说明中混用的 `imageUri`。`otherDetails` 则是普通多语言文本，保存评审过程的进一步信息，例如数据集首次发布后补充的小幅修正。两者的结构不同，但都应与该条记录的人员和所审版本一起阅读，避免把发布后的补充说明误当成数值交换，或把历史意见移接到其他版本。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：教学审查人员、目标版本与意见

[下载本段 XML](xml-examples/review-01.xml)。

```xml
<review xmlns="http://www.EcoInvent.org/EcoSpold02" reviewerId="00000000-0000-4000-8000-000000000106" reviewerContextId="00000000-0000-4000-8000-000000000100" reviewerName="Teaching Reviewer" reviewerEmail="demo@example.invalid" reviewDate="2025-03-01" reviewedMajorRelease="1" reviewedMinorRelease="0" reviewedMajorRevision="1" reviewedMinorRevision="1">
  <details><text index="1" xml:lang="zh">教学审查意见：仅演示目标版本、结论与建议的记录位置，不表示真实数据已通过人工审查。</text></details>
  <otherDetails xml:lang="zh">本例人员、日期和意见均虚构；后续修订不自动继承本次审查覆盖。</otherDetails>
</review>
```

这个完整 review 片段记录针对发布版本 1.0 内、数据集修订 1.1 的虚构审查。四个版本属性不是把数据库版本拼成 1.0.1.1，也不意味着文件后续修改已审。details 是富文本结构；otherDetails 是普通字符串。所有人员 UUID、姓名、邮箱和意见仅为教学，不是人工签核。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@reviewerId`（FieldID 3300）**：`review/@reviewerId="00000000-0000-4000-8000-000000000106"` 引用教学审查人员主数据。它不是录入者或来源 ID；真实读取须用对应人员主数据解释，不因这个虚构 UUID 存在而宣称人工审核。

**`@reviewerContextId`（FieldID 3301）**：`@reviewerContextId="00000000-0000-4000-8000-000000000100"` 限定审查人员的教学上下文。省略时沿用数据集上下文；姓名相同而上下文不同的人员不应直接合并。

**`@reviewerName`（FieldID 3305）**：`@reviewerName="Teaching Reviewer"` 保存人员姓名的冗余文本。它用于展示，身份依据仍是 reviewerId 与有效上下文，而不是人名字符串。

**`@reviewerEmail`（FieldID 3306）**：`@reviewerEmail="demo@example.invalid"` 是明确的教学邮箱。读取为联系信息，不进行发信，也不能把邮箱存在当成审查结论或认证。

**`@reviewDate`（FieldID 3310）**：`@reviewDate="2025-03-01"` 是本次虚构审查的完整日期，按 xsd:date 读取。它不同于活动有效期间、文件编辑时间，也不表示此日之后的修订均受审。

**`@reviewedMajorRelease`（FieldID 3320）**：`@reviewedMajorRelease="1"` 是被审对象所属数据库主发布号。应与文件的 majorRelease 比较，而非误读成数据集主修订号。

**`@reviewedMinorRelease`（FieldID 3325）**：`@reviewedMinorRelease="0"` 是被审对象的数据库次发布号，与前值共同指向教学发布 1.0。零是明确数值不是缺失；不同发布版本的审查不能自动通用。

**`@reviewedMajorRevision`（FieldID 3330）**：`@reviewedMajorRevision="1"` 是被审数据集主修订号，独立于发布号。应与 fileAttributes 的 majorRevision 及其他目标版本属性共同核对，不能把它解释成数据库 3.12 等发布版本。

**`@reviewedMinorRevision`（FieldID 3335）**：`@reviewedMinorRevision="1"` 是被审数据集次修订号，本例目标修订为 1.1。若文件已是其他修订，不能仅因同一 reviewerId 就断言本次意见覆盖新内容。

**`details`（FieldID 3340）**：`review/details/text` 的 index=1 中文意见是富文本中的一段。读取 details 的完整子树及文本顺序，而不是只看外层空白；其中写明本例不代表真实人工审查。

**`otherDetails`（FieldID 3350）**：`review/otherDetails` 存“后续修订不自动继承本次审查覆盖”的普通文本。它不是 TTextAndImage，不应到其下面查 text/imageUrl；与 details 同属该次 review 记录。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/review-01.xml").getroot()
FIELDS = {
    "3300": "@reviewerId",
    "3301": "@reviewerContextId",
    "3305": "@reviewerName",
    "3306": "@reviewerEmail",
    "3310": "@reviewDate",
    "3320": "@reviewedMajorRelease",
    "3325": "@reviewedMinorRelease",
    "3330": "@reviewedMajorRevision",
    "3335": "@reviewedMinorRevision",
    "3340": "details",
    "3350": "otherDetails",
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
LOCATIONS = ['es:modellingAndValidation/es:review']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要判断谁审查了哪个版本时，遍历每条 review，把审查人员、日期、被审版本和 details 放在同一记录中。不能以存在 review 节点就认定所有后续版本都被审过；具体审查结论要读意见文本。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`modellingAndValidation/review`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TReview")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

`demo-product.spold` 未提供该类节点，因此这个例子返回空列表 `[]`。这表示当前教学文件没有记录该信息，不能填成数值零，也不说明实际数据集永远没有此字段。换成包含该结构的完整文件后，代码会读取其实际属性和子节点；本章字段语义仍适用。

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-treview)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
