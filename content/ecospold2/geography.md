# 地理区域

对应官方格式类型：`TGeography`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 地理信息描述适用范围，也界定市场范围 <a href="#read-tgeography" id="read-tgeography"></a>

`activityDescription/geography` 采用 `TGeography`。属性 `geographyId` 引用有效地理位置主数据中的详细定义，`geographyContextId` 指定该引用的上下文，省略时使用数据集自身的上下文。元素 `shortname` 是这一地理位置的描述性简称，可用于报告和筛选；它不是替代 UUID 的主数据键。元素 `comment` 提供进一步的地理解释，采用 `TTextAndImage`，可说明边界划分的性质、非行政区域的界定方式以及市场边界的依据。

不要把 geography 一律理解为国家。它可表示活动的点位置、移动活动的线，或包含多个具体活动地点的分布式活动及生产组合的区域。对于市场和消费组合，它描述限制跨界进出口的市场边界。读取时可先提取 `shortname` 了解地理范围，再用 `geographyId` 及对应上下文解析主数据，最后结合 `comment` 判断该范围是否与研究对象一致；地理简称本身并不交代全部边界含义。

## 对照 XML 找到每个字段

以下是为本章构造的教学 XML 类型片段，不是真实 ecoinvent 记录。片段声明了默认命名空间，可独立解析；插入自己的 `.spold` 时应定位到本章所述父元素。这里展示该类型的结构，整个数据集的必填关系、继承和主数据引用仍需结合外层文件判断。

### 示例 1：区域引用及边界说明

[下载本段 XML](xml-examples/geography-01.xml)。

```xml
<geography xmlns="http://www.EcoInvent.org/EcoSpold02" geographyId="a099d998-acea-50db-a416-a5eaeaf6eb23" geographyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1">
  <!-- 教学构造，非真实区域。 -->
  <shortname xml:lang="zh">教学区域（虚构）</shortname>
  <comment><text index="1" xml:lang="zh">按教学厂区边界划定，不代表行政区域或真实市场范围。</text></comment>
</geography>
```

本例是 activityDescription 中的 geography 片段。它用地区 UUID 识别位置，用可读短名称和边界说明帮助理解；实际位置可能是点、线或面，市场活动还需解释市场边界。

### 顺着示例读取字段

下面按本类型的字段逐项对照。属性前的 `@` 只是参考文档的写法；XML 中没有这个字符。没有写出的可选项表示缺失，不能直接补成零。引用字段的有效上下文可能要从外层 `fileAttributes/@contextId` 取得，单独片段不会替你提供这项外层信息。

**`@geographyId`（FieldID 400）**：`geographyId="a099d998-acea-50db-a416-a5eaeaf6eb23"` 是合法地区主数据的引用位置，本例沿用教学 demo 的虚构区域 UUID。读取该属性后应到对应地区主数据取得详细几何信息；它本身既不是经纬度，也不能仅从 UUID 判断是国家或厂区。

**`@geographyContextId`（FieldID 401）**：`geographyContextId="f71ac544-3bc8-5c15-8ea4-072d907663f1"` 显式给出地区主数据上下文。解析地区身份时使用 UUID 加有效上下文；省略时回退到文件自身上下文，不把活动所在地文字直接当成引用依据。

**`shortname`（FieldID 410）**：`shortname` 写“教学区域（虚构）”，是所引用地区的简短名称。读取全部语言条目并选择需要的语言；短名称可以类似区域代码，但不是地区 UUID，不能把同名区域无条件合并。

**`comment`（FieldID 420）**：`comment/text` 解释教学厂区边界而非行政区域或真实市场范围。读取索引及语言后保留完整边界限定；市场活动可在这里说明边界理由，不能把一个地区名称直接解释为所有进口出口都自由发生。

### 按相同路径提取自己的字段

下面的字典逐项对应上面的 XML 字段。解压[XML 片段与读取代码 ZIP](attachments/ecospold2-xml-examples.zip)后，在解压目录运行；更换文件名即可阅读本章其他片段。返回值始终是列表：`[]` 表示未出现，属性保留原始字符串，子元素保留语言等属性、文字和完整 XML。多个语言或重复元素不会被悄悄丢弃。

```python
import json
import xml.etree.ElementTree as ET
from read_xml_fields import field_values

node = ET.parse("xml-examples/geography-01.xml").getroot()
FIELDS = {
    "400": "@geographyId",
    "401": "@geographyContextId",
    "410": "shortname",
    "420": "comment",
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
LOCATIONS = ['es:activityDescription/es:geography']
for location in LOCATIONS:
    nodes = dataset.findall(location, NS)
    print("父路径：", location, "匹配数：", len(nodes))
    for node in nodes:
        for field_id, relative_path in FIELDS.items():
            print(field_id, relative_path,
                  json.dumps(field_values(node, relative_path), ensure_ascii=False))
```


## 怎样定位、使用与提取

需要筛选地区或解释市场范围时，使用 geographyId 与有效上下文定位地理主数据，shortname 用作展示。不要把一个全球范围的数据集默认为具体国家；地区的适用解释还要结合 comment。

定位路径相对于完整的 `/ecoSpold/activityDataset`：`activityDescription/geography`。其中 `.//` 表示在当前数据集的后代中检索；返回结果会保留实际父路径，以区分不同交换或参数。

下载[教学 demo 与读取脚本 ZIP](demo/ecospold2-tutorial-demo.zip)，解压后在同一目录运行下面代码。`read_section.py` 使用 Python 标准库，返回全部匹配节点的属性和完整子节点树；它保留 UUID、原始数值字符串、语言标签和子节点顺序。代码仅展示前两条，变量 `records` 保留全部匹配记录。文件有多个普通数据集时，显式选择 `index`，或逐个遍历；子数据集应先展开继承。

原表名称前带 `@` 的是 XML 属性，去掉 `@` 后在返回记录的 `attributes` 中取值，例如 `record["attributes"].get("amount")`。没有 `@` 的字段是子元素，在 `children` 中按完整 `tag` 匹配；名称前的 `{http://www.EcoInvent.org/EcoSpold02}` 是命名空间。多语言字段保留多个子节点，`xml:lang` 在属性字典中写为 `{http://www.w3.org/XML/1998/namespace}lang`。更深的字段继续进入相应子节点的 `children`；缺失属性返回 `None`，不要补成零。

```python
import json
from read_section import load_dataset, read_section

dataset = load_dataset("demo-product.spold", index=0)
records = read_section(dataset, "TGeography")
print("匹配节点数：", len(records))
print(json.dumps(records[:2], ensure_ascii=False, indent=2))
```

## 对照 demo 理解读取结果

在 `demo-product.spold` 中实际匹配 **1 个节点**。下面是第一个节点的属性与前两个子节点的精选片段；子节点内部结构和其他节点仍保存在代码的完整返回值中。路径带有同级序号，便于回到原文件定位，序号不是主数据 UUID。

```json
{
  "path": "/ecoSpold/activityDataset/activityDescription[1]/geography[1]",
  "attributes": {
    "geographyId": "a099d998-acea-50db-a416-a5eaeaf6eb23",
    "geographyContextId": "f71ac544-3bc8-5c15-8ea4-072d907663f1"
  },
  "children_excerpt": [
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}shortname",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "zh"
      },
      "text": "教学区域（虚构）"
    },
    {
      "tag": "{http://www.EcoInvent.org/EcoSpold02}shortname",
      "attributes": {
        "{http://www.w3.org/XML/1998/namespace}lang": "en"
      },
      "text": "Teaching region (synthetic)"
    }
  ]
}
```

## 继续阅读

[提取与查询实践](extraction-practice.md)把数量读取、身份筛选与参考产品归一化连起来；[完整中文格式译表](format-reference.md#appendix-tgeography)用于核对本类型的字段次序、类型和原表标记。原文疑点见[审校记录](translation-review.md)。
