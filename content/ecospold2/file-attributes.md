# 文件属性

对应官方格式类型：`TFileAttributes`。本篇以文章解释该类型的 13 条字段；复合类型也会说明它们依附在哪个对象上。

## 区分数据库发布版本、数据集修订版本和文件时间 <a href="#read-tfileattributes" id="read-tfileattributes"></a>

`administrativeInformation/fileAttributes` 采用 `TFileAttributes`，描述文件整体信息。属性 `majorRelease` 和 `minorRelease` 属于发布版本：主发布号在重大更新时加一，次发布号在两次重大更新之间的每次发布时加一。原文以每两年一次为重大更新的例子，但这不是由格式规定的固定发布日程。属性 `majorRevision` 和 `minorRevision` 则区分某个数据集本身的修订，独立于数据库发布版本。因此，程序应将发布版本和数据集修订版本分别保存，而不是拼成一个失去角色区分的版本字段。

`majorRevision` 反映数据集已获接受的变更，只能随时间增加，不得手动更改。在 ecoinvent 上下文中，活动变更通过审查并加入数据库后，它增加，同时将 `minorRevision` 重置为 `1`。`minorRevision` 描述提交审查前编辑过程中的版本；数据提供者每次将修改保存到本地或作为服务器草稿保存时，它自动增加。读取一份草稿与已接受版本时，应据此理解修订状态，不能把文件较新的时间戳直接等同于已接受的内容变更。

时间属性同样需要分开。`creationTimestamp` 是数据集创建时自动生成的日期时间，`lastEditTimestamp` 是保存数据集时自动生成的日期时间；`fileTimestamp` 是当前文件创建的日期时间。前两者描述数据集的创建和编辑，后者描述文件生成，它们都不替代 `timePeriod` 的数据有效日期。`fileGenerator` 说明创建文件的程序，最好包括软件版本；`internalSchemaVersion` 说明生成数据集所依据的内部模式版本。记录这些信息，有助于判断解析环境和追踪导出来源。

属性 `defaultLanguage` 为多语言字段指定默认语言，在完整数据 XSD 中省略时为 `en`；子差异文件省略该属性时应先处理继承，不能绕过父值直接取 `en`。每个多语言字段至少应有默认语言的值。提取活动名称等多语言元素时，应先选择相应语言内容，并保留语言标识，而不是把不同语言的重复元素当成重复数据。元素 `contextName` 是上下文名称，属性 `contextId` 是数据集所面向上下文的 UUID。上下文可用于限制信息访问范围，并决定解析引用时需要哪些主数据文件；它取代旧 ecoSpold01 的 quality network，ecoinvent 质量网络对应的上下文 ID 可在 `Context.xml` 中查找。

缺少 `contextId` 时，说明将文件视为独立数据集，主数据引用不能被解析为实际主数据内容。这与缺少某个可选的 `…ContextId` 属性不同：后者通常沿用数据集上下文，但前提是这个上下文已经可知。元素 `requiredContext` 可重复出现，采用 `TRequiredContextReference`，用于列明完整读取主数据引用所需的其他上下文。真正取数前，应先识别本文件的上下文及所需上下文，再尝试连接各个名称、地点、人员、来源和属性的 UUID。

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
