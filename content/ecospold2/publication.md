# 数据生成者与发布

对应官方格式类型：`TDataGeneratorAndPublication`。本篇以文章解释该类型的 17 条字段；复合类型也会说明它们依附在哪个对象上。

## 原始数据来源、出版物与访问限制构成另一组管理信息 <a href="#read-tdatageneratorandpublication" id="read-tdatageneratorandpublication"></a>

`administrativeInformation/dataGeneratorAndPublication` 采用 `TDataGeneratorAndPublication`。这里的属性 `personId` 识别收集、汇编或发布原始数据的数据生成者，未必与 `dataEntryBy` 的录入者相同。`personContextId` 指向其人员上下文，省略时沿用数据集上下文；`personName` 和 `personEmail` 分别记录姓名和完整邮箱。读取两个人员组时，要保留各自所属的 XML 路径，即使字段都叫 `personId`，也不能把两种角色覆盖成同一个“作者”。原说明还将数据生成者解释为应获认可的数据来源及承担主要采集工作的个人或组织；当前人员引用须与相应人员主数据匹配。

属性 `dataPublishedIn` 表示发布程度：`0` 是数据本身未在别处发布，也是默认值；`1` 是部分单元过程或子系统已发布；`2` 是数据完整发布于所引用来源。`publishedSourceId` 引用记录数据的报告或来源，`publishedSourceContextId` 指定来源上下文，省略时使用数据集自身上下文。`publishedSourceYear` 记录出版或沟通年份，对网站记录最后访问时间；原文没有限定网站条目只能写年份，实际类型为 `TBaseString30`。`publishedSourceFirstAuthor` 给出第一作者的姓和名字缩写。对于 `sourceType=4, 5, 6, 7` 的现场测量、口头沟通、个人书面沟通和问卷，它记录沟通人员。`pageNumbers` 进一步定位文章或较大出版物中的相关页码。取数时，这些字段共同构成可追溯来源，不能用一个年份或第一作者文本替代来源主数据引用。

原说明出现的旧编号也有明确对应关系：`757` 是 `publishedSourceId` 的旧 SpoldID，当前 fieldId 为 `3520`；它引用的来源 `id` 的旧 SpoldID 是 `801`，当前 fieldId 为 `3110`。这些是编号体系之间的映射，而非需要替换的 XML 名称。在子数据集中，若要删除父数据集的来源引用，必须将 `publishedSourceIdOverwrittenByChild` 设为 `true`；仅省略 `publishedSourceId` 会沿用父引用。

版权和可访问性由不同属性表达。`isCopyrightProtected` 表示是否有著作权，原说明要求对应填写 `1` 或 `0`。`accessRestrictedTo` 默认 `0`，表示无访问限制；`1` 表示只有上下文定义的许可证持有者可访问；`2` 表示这些许可证持有者只能访问 LCI 结果，不能访问单元过程原始数据，而数据库管理员仍具有完整访问权限；`3` 表示只有指定组织及数据库管理员可访问。不能把版权标记当成公开许可，也不能从文件技术上可读推断有权公开传播其中数据。

当访问限制为 `3` 时，`companyId` 引用获准使用数据集的组织或机构，`companyContextId` 指定该组织上下文，省略时使用数据集上下文；`companyCode` 是对应公司的可选代码纯文本。原说明称其为 7 字母代码，`TCompanyCode` 的说明还称应使用大写字母，但本版 XSD 的实际约束只有最长 7 个字符，没有固定长度或字母字符模式；因此，通过 XSD 并不等于已经满足这项文字约定。原文条件 `759=3` 中的 `759` 是 `accessRestrictedTo` 的旧 SpoldID，当前 fieldId 为 `3550`，因此条件应理解为访问限制类别为 `3`，不是另一项编号为 759 的当前属性。若子数据集需要移除组织引用，必须把 `companyIdOverwrittenByChild` 设为 `true`，否则仍视为保留父值。这套规则让程序能够分别处理“继承已有引用”与“明确删除引用”。

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
