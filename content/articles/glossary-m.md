# 术语表 M

英文原题：M  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/glossary-m)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

##

[市场活动](#zh-b0006)

[mft / non-mft](#zh-b0011)

[MO](#zh-b0014)

[多输出活动](#zh-b0016)

### 市场活动 <a href="#zh-b0006" id="zh-b0006"></a>

市场活动将产品或服务（中间交换）从生产它的一个或多个转化活动转移到消费它的转化活动。转化活动是否向某个市场活动供货，由两者的地理区域决定。市场活动可以覆盖全球地理区域（GLO）或某个特定地区。一般规则是：向市场供货的转化活动位于同一地理边界内，且其产品没有全部通过直接活动链接由另一个转化活动消费。各转化活动的供应份额由其产量决定。不过，对于具有更详细信息的市场，可以针对每个系统模型手动指定各供应份额。

因此，市场活动提供某一产品在给定地区的平均消费组合；对于采用边际供应商的系统模型，则提供边际消费组合。

除所转移的产品或服务之外，市场活动还可能包含用于模拟产品平均运输、运输造成的直接排放，以及来自该市场自身的输入的交换。来自市场自身的输入表示产品运输和储存过程中发生的损失。

关于市场活动的更多信息，请参阅此[页面](market-activities.md)。

### mft / non-mft <a href="#zh-b0011" id="zh-b0011"></a>

mft 表示“待处理材料”（material for treatment），non-mft 表示“非待处理材料”（material not for treatment）。这是 APOS 系统模型对产品进行分类的两个类别。顾名思义，在 APOS 系统模型链接中，“待处理材料”需要在处理活动中接受处理，而分类为 non-mft 的产品则不需要。例如，mft“municipal solid waste”（城市固体废物）通过“market for municipal solid waste”（城市固体废物市场）调用“treatment of municipal solid waste, incineration”（城市固体废物处理，焚烧）及其他处理活动。

请在[此处](system-models.md)进一步了解 APOS 系统模型及其链接规则。

### MO <a href="#zh-b0014" id="zh-b0014"></a>

多输出活动（multi-output activity）的缩写。

### 多输出活动 <a href="#zh-b0016" id="zh-b0016"></a>

具有多个输出的活动。

{% endtab %}

{% tab title="English 原文" %}

##

[Market Activity](#en-b0006)

[mft / non-mft](#en-b0011)

[MO](#en-b0014)

[Multi-Output Activity](#en-b0016)

### Market Activity <a href="#en-b0006" id="en-b0006"></a>

A market activity transfers a product or service (intermediate exchange) from one or more transforming activities that produce it, to the transforming activities that consume it. Whether a transforming activity supplies a given market activity is determined by their geographies. A market activity may cover either the global geography (GLO) or a specific region. The general rule is that a market is supplied by transforming activities that are located within the same geographical boundaries, and whose product is not consumed entirely by another transforming activity (through a direct activity link). The shares supplied by each transforming activity are determined by their production volumes. However, markets for which more detailed information is available may have their shares specified manually for each system model.

A market activity therefore provides the average consumption mix of a product for a given region, and the marginal consumption mix in the case of system models that use marginal suppliers.

In addition to the product or service that is transferred, a market activity may contain exchanges that model the average transportation of the product, direct emissions caused by the transportation, as well as an input from the market itself, which represents losses that occur during transportation and storage of the product.

More information about market activities is provided on this [page](market-activities.md).

### mft / non-mft <a href="#en-b0011" id="en-b0011"></a>

mft stands for “material for treatment”, non-mft satnds for “material not for treatment”. These are the two categories by which products are classified in the APOS system model. As the name implies, a “material for treatment” requires to be treated in a treatment activity in the linking of the APOS system model, while this is not the case for non-mft classified products. For example the mft “municipal solid waste” calls “treatment of municipal solid waste, incineration” and other treatment activities through the “market for municipal solid waste”.)

Read more about the APOS system model and its linking rules [here](system-models.md).

### MO <a href="#en-b0014" id="en-b0014"></a>

Abbreviation for multi-output activity

### Multi-Output Activity <a href="#en-b0016" id="en-b0016"></a>

An activity with more than one output.

{% endtab %}

{% endtabs %}
