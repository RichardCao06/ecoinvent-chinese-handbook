# 属性

英文原题：Properties  
来源：[ecoinvent 官方原文](https://support.ecoinvent.org/properties)  
原文快照：2026-10-13  
审核状态：AI 交叉审校通过

原站修改日期：2025-09-26

{% tabs %}

{% tab title="中文" %}

## ecoinvent 数据库的最新版本包含约 3,500 种不同产品，包括原材料、商品和服务。 <a href="#zh-b0002" id="zh-b0002"></a>

2023 年 10 月 24 日

同一种产品可以采用多种技术、在多个位置生产，有时会因此具有不同的产品属性，例如物理和化学属性。比如，不同树种的木材密度可能不同，不同地区原油的热值可能不同，城市废物的不同组成部分也可能具有不同的碳含量。因此，ecoinvent 数据库中每个具有质量的产品都附有属性信息。

### ecoinvent 数据库中的产品属性 <a href="#zh-b0005" id="zh-b0005"></a>

数据库中除废物外的每个产品都添加了价格属性。价格以欧元表示，代表全球长期（通常为五年）平均价格。不过，价格中未反映快速波动的市场价格和外部性。

对于多输出过程，各种输出的价格用于确定归因型系统模型中的经济分配因子。当必须维持产品的物理属性时，可能采用例外做法，热电联产过程便是一例。这些产品的分配会考虑所产生热和电的㶲。经济分配因子的属性称为真实价值（true value）。

有关分配的更多信息，请参阅[系统模型部分](system-models.md)。

此外，每个具有质量的产品均提供<strong>六项必填产品属性</strong>：

- <strong>干质量</strong>  
  数据库为每个具有质量的产品规定干质量。对于水以外的物质，干质量不等于灰分含量，而是湿质量减去水质量，因此包括以化学键结合的 H 和 O。所以，当水进入或释放于涉及化学结合 H 和 O 的化学反应时，水的投入或输出可能具有干质量，尽管这有些不符合直觉。
- <strong>湿质量</strong>  
  样品或物体的湿物质质量，湿质量 = 干质量 + 湿质量中的水质量；市场中的运输量按此数值计算。
- <strong>含水率</strong>  
  湿质量中的水质量与干质量之比。  
  含水率 = 湿质量中的水质量/干质量
- <strong>湿质量中的水质量</strong>  
  湿质量中减去干质量后的水量。  
  湿质量中的水质量 = 湿质量 – 干质量。
- <strong>生物源和化石碳含量</strong>  
  数据库为每个具有质量的产品规定化石碳和非化石碳含量；二者始终按单位干质量给出（即为无量纲属性）。

许多<strong>可选产品属性</strong>会在有用时提供。常见示例包括：

- <strong>金属矿石的金属含量</strong>  
  金属含量（例如铁矿石的铁含量）按单位干质量给出（即为无量纲属性）。
- <strong>寿命和全寿命产能</strong>  
  寿命是某项基础设施从建造到开始退役之间的时期。全寿命产能是基础设施在其整个寿命内充分利用时能够生产的产品数量或提供的服务单位数量。例如，这可以是汽车行驶的公里数，或发电厂满负荷运行所生产的千瓦时数。  
    
  <strong>示例：</strong> 活动“lignite power plant construction, 500 MW”的参考产品为 1 单位“lignite power plant”。寿命定义为 34 年，产能定义为满负荷发电 300,000 小时。因此，全寿命产能为 1.5E11 kWh（对应 300,000 小时\*500 MW）。这一属性对计算消费活动的基础设施投入非常有用：发电活动每生产 1 kWh 电力，需要该项投入 1 kWh/(0.68\*lifetime\_capacity) = 9.8E-12 单位。
- <strong>热值或能量含量</strong>  
  能量含量信息由两项属性提供，即低位热值（heating value, net）和高位热值（heating value, gross）。低位热值（LHV）为燃料、化学品、木材等所有相关产品规定，以每单位参考产品的 MJ 数表示，并针对所规定含水率下的材料给出。高位热值为燃料等特定产品提供，以 MJ/kg 产品表示。热值可以因燃料的地理来源或技术来源而异，也可以在整个数据库中统一。例如，石油的低位热值在整个数据库中统一定义为 43.2 MJ/kg。

<strong>属性为何有用</strong>

产品属性可服务于多种用途，既可用于数据库内部，也可用于定制工具和分析。

其中最突出的是，碳含量属性以及区分生物源碳与化石碳的能力，对于分析碳平衡和碳足迹至关重要。

同样，ecoinvent 中的质量和水属性有助于开展详尽的水平衡和水足迹分析。

所有材料、商品和服务均提供价格属性，这也使简单的成本分析乃至生命周期成本分析成为可能（不计外部性和人力资源消耗）。

当某种产品在不同位置或采用不同技术生产而具有不同属性时，属性的明确规定使各种来源的供应可以汇入同一个共同市场。在市场中，可以确定消费组合的加权平均产品属性，并将这些属性一致地提供给消费过程。

{% endtab %}

{% tab title="English 原文" %}

## The latest version of the ecoinvent database contains around 3,500 different products, including raw materials, goods, and services. <a href="#en-b0002" id="en-b0002"></a>

Oct 24th, 2023

The same product can be produced from multiple technologies and in multiple locations, sometimes resulting in different product properties, e.g., physical and chemical properties. For example, wood from different species may have different densities, crude oil from different regions may have different heating values and different fractions of municipal waste may have different carbon contents. Thus, every product with mass in the ecoinvent database comes with property information.

### Product Properties in the ecoinvent Database <a href="#en-b0005" id="en-b0005"></a>

Price is added as a property to every product of the database, except waste. The price represents a global and long-term (typically five years) average, in euros. However, rapidly fluctuating market prices and externalities are not reflected in the price.

In the case of multi-output processes, the prices of the various outputs are used to determine the economic allocation factor in the attributional system models. Exceptions may apply where physical product properties must be maintained: heat and power co-generation processes are an example. These products are allocated taking into account the exergy of the generated heat and electricity. The property of the economic allocation factor is called true value.

Read more about allocation in the [system models section](system-models.md).

Additionally, <strong>six mandatory product properties </strong>are available for each product with mass:

- <strong>Dry Mass </strong>  
  Dry mass is specified in the database for every product with mass. For substances other than water, dry mass is not the same as ash content but is calculated as the wet mass minus the water mass and thus includes chemically bound H and O. Inputs or outputs of water may therefore, somewhat counterintuitively, have a dry mass when the water is incorporated into or released from chemical reactions involving chemically bound H and O.
- <strong>Wet Mass </strong>  
  The wet matter of a sample or of an object, wet mass = dry mass + water in wet mass, that is, the value used to calculate transport in the markets.
- <strong>Water Content </strong>  
  The ratio between water in wet mass and dry mass.   
  Water content = water in wet mass/dry mass
- <strong>Water in Wet Mass </strong>  
  The amount of water in the wet mass after subtracting the dry mass.   
  Water in wet mass = wet mass – dry mass.
- <strong>Biogenic and Fossil Carbon Content </strong>  
  The fossil and the non-fossil carbon contents are specified for every product with mass in the database; they are always given per dry mass (i.e., they are dimensionless properties).

Numerous <strong>optional product properties </strong>are specified where they are useful. Common examples include:

- <strong>The Metal Content of Metal Ores </strong>  
  Metal content, e.g., iron content of iron ore, is given per dry mass (i.e., it is a dimensionless property).
- <strong>The Lifetime and Lifetime Capacity </strong>  
  The lifetime is the period between the time of construction and the time of initiating decommissioning of an infrastructure item. Lifetime capacity is the quantity of products or service units an infrastructure is capable of producing or performing over its entire lifetime at full utilization. For example, this could be the kilometres driven by a car or the kilowatt hours produced by a power plant at full load.   
    
  <strong>Example:</strong> The activity “lignite power plant construction, 500 MW” has a reference product of 1 unit of “lignite power plant”. The lifetime is defined as 34 years, and the capacity is defined as 300,000 hours of electricity production at full load. Hence, the lifetime capacity is 1.5E11 kWh (corresponding to 300,000 hours\*500 MW). This property is very useful for calculating the inputs of infrastructure to consumption activities: the electricity production activity will require 1 kWh/(0.68\*lifetime\_capacity) = 9.8E-12 units of this input to produce 1 kWh of electricity.
- <strong>Heating Value or Energy Content </strong>  
  Information on the energy content is provided by two properties, i.e. lower heating value (heating value, net) and higher heating value (heating value, gross). Lower heating values (LHVs) are specified for all relevant products, such as fuels, chemicals, and wood. LHVs are expressed as MJ per unit of reference product. The LHVs are quoted for materials at the specified water content. Higher heating values are provided for specific products such as fuels in MJ per kg of product. Heating values can either vary depending on the geographical or technological origin of the fuel or be standardized throughout the entire database. For example, the lower heating value of petroleum is defined as 43.2 MJ/kg throughout the entire database.

<strong>Why are Properties Useful </strong>

Product properties can serve many purposes, both within the database and for tailored tools and analysis.

Most prominently, properties for carbon content and the ability to distinguish between biogenic and fossil carbon are essential to analyze carbon balances and carbon footprints.

Similarly, the mass and water properties in ecoinvent allow for thorough water balances and water footprinting.

The price property, which is available for all materials, goods and services, also allows for simple cost analysis, even life cycle cost analysis (without externalities and human resource consumption).

When a product is produced with different properties in different locations or from different technologies, the specification of the properties allows the supply from all origins to meet in one common market. In the market, the weighted average product properties of the consumption mix can be determined and consistently supplied to the consumption processes.

{% endtab %}

{% endtabs %}
