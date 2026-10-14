# 地理区域

对应官方格式类型：`TGeography`。本篇以文章解释该类型的 4 条字段；复合类型也会说明它们依附在哪个对象上。

## 地理信息描述适用范围，也界定市场范围 <a href="#read-tgeography" id="read-tgeography"></a>

`activityDescription/geography` 采用 `TGeography`。属性 `geographyId` 引用有效地理位置主数据中的详细定义，`geographyContextId` 指定该引用的上下文，省略时使用数据集自身的上下文。元素 `shortname` 是这一地理位置的描述性简称，可用于报告和筛选；它不是替代 UUID 的主数据键。元素 `comment` 提供进一步的地理解释，采用 `TTextAndImage`，可说明边界划分的性质、非行政区域的界定方式以及市场边界的依据。

不要把 geography 一律理解为国家。它可表示活动的点位置、移动活动的线，或包含多个具体活动地点的分布式活动及生产组合的区域。对于市场和消费组合，它描述限制跨界进出口的市场边界。读取时可先提取 `shortname` 了解地理范围，再用 `geographyId` 及对应上下文解析主数据，最后结合 `comment` 判断该范围是否与研究对象一致；地理简称本身并不交代全部边界含义。

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
