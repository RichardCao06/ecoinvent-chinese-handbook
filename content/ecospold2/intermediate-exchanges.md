# 中间交换专用字段

对应官方格式类型：`TIntermediateExchange`。本篇以文章解释该类型的 18 条字段；复合类型也会说明它们依附在哪个对象上。

## 中间交换如何连接产品与供应者 <a href="#read-tintermediateexchange" id="read-tintermediateexchange"></a>

`TIntermediateExchange` 表示单元过程中的产品、服务或废物输入与输出，连接活动与技术圈。它继承共同交换字段，因此一条记录既有交换实例的 `id` 和数量 `amount`，又有引用产品主数据的 `intermediateExchangeId`。后者为必需 UUID，回答“是哪一种中间产品”；可选的 `intermediateExchangeContextId` 指明产品主数据上下文，省略时使用数据集自身的上下文。产品名称相同，不等于实例相同，也不等于供应活动相同。

流向由 `inputGroup` 与 `outputGroup` 表达，XSD 使用二选一结构，每条中间交换只应具有其中一个。输入分组的 1 表示材料／燃料，2 表示电力／热，3 表示服务，5 表示未进一步指定的来自技术圈的流。输出分组的 0 表示参考产品，2 表示副产品，3 表示待处理材料，5 表示存量增加。读参考输出时，应识别 `outputGroup` 为 0 的记录，而不是按名称猜测或挑数值最大的输出。分组说明流向和角色，`amount` 的正负则是另一个维度；不能把所有正数都当输出、负数都当输入，也不能在读文件时不加区分地取绝对值。

参考输出提供理解交换数量的基准，但原始单元过程的参考数量不一定为 1。提取输入和排放后，若研究需要按单位参考产品表达，应先明确所选参考输出、它的数量和单位，以及所用系统模型和已经完成的分配状态，再按适用方法对相关数量作一致缩放。XML 读取本身不自动执行这一归一化；多输出记录也不能仅靠除以任意一个输出量，就当作已经完成产品间分配的结果。

供应者由可选的 `activityLinkId` 显式指定，它是活动链接，不能用本条交换的 `id` 或产品的 `intermediateExchangeId` 代替。`activityLinkContextId` 指明活动链接所属上下文，省略时使用数据集上下文；`activityLinkIdOverwrittenByChild` 则允许子数据集明确移除继承的链接，需设为 `true`，否则仍会保留父值。原说明写明，如果 `activityLinkId` 为空，供应活动由使用本活动地理和时间信息的链接规则确定。因此，空链接不代表没有供应者，更不能自行任选一个同名活动作为供应者。原表还给出“引用另一活动数据集的字段 105”的提示，但该数字在活动部分对应 `activityNameId`，而 XSD 将 `activityLinkId` 声明为 `TActivityIndexEntry` 引用；实现活动匹配时应核对活动索引，不能把这条提示当成交换实例、产品或活动名称标识可以互换的依据。

与每条交换的数量不同，可选的 `productionVolumeAmount` 表示按年计的产品产量，单位与该交换一致。它不是当前参考输出数量，也不是把清单归一化到单位产品时可直接使用的分母。`productionVolumeVariableName` 给产量提供公式简称，命名规则同样是字母 a-z 开头、允许字母数字下划线且不区分大小写。`productionVolumeMathematicalRelation` 通过变量名或 `REF` 引用流、参数和属性；这里有一项已记录的原文疑点：该字段说明把公式结果的目标写成 `amount`，而 XSD 单独定义了产量字段 `productionVolumeAmount`。教程保留这一差异，不根据这段说明把产量公式值写入普通交换数量；需要重新求值时，应确认具体软件的目标字段。

产量有一组独立的来源说明。`productionVolumeSourceId` 引用产量依据的有效来源，`productionVolumeSourceContextId` 指明其上下文，省略时使用数据集上下文。`productionVolumeSourceIdOverwrittenByChild` 设为 `true`，才明确表示在子数据集中移除该来源引用；缺少引用本身仍可能意味着继承父值。`productionVolumeSourceYear` 表示出版、交流或网站最后访问年份；`productionVolumeSourceFirstAuthor` 表示第一作者或现场测量、口头交流、个人书面交流及问卷来源的提供人员，规则对应 `sourceType` 为 4、5、6、7 的情况。可多语言填写的 `productionVolumeComment` 解释产量来源、假设和计算，可选的 `productionVolumeUncertainty` 则用分布及其参数和／或谱系信息记录产量不确定性。最后，可重复的 `classification` 通过分类配对描述产品所属类别。提取产量时应连同这一组依据保存，而不是拿交换的一般来源记录代替产量来源。

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
