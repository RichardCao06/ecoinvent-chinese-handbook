# 提取与查询实践

理解 demo 后，可以先用很短的程序复现三个动作：按命名空间进入活动数据集，找到参考输出，再读取电力或环境交换的属性。这些例子直接处理 XML，不会求解产品系统，也不会执行公式字符串。

### 最小例子：读活动、参考产品和原始交换量

在下载了 demo 的目录运行下面代码，或把 `demo-product.spold` 改为自己的文件路径。这个短例子只演示读取一个普通活动数据集；后面的完整提取器会遍历文件中的全部普通数据集。

```python
from decimal import Decimal
import xml.etree.ElementTree as ET

ns = {"es": "http://www.EcoInvent.org/EcoSpold02"}
root = ET.parse("demo-product.spold").getroot()
dataset = root.find("es:activityDataset", ns)
if dataset is None:
    raise ValueError("需要普通 activityDataset；子数据集须先展开继承")

activity = dataset.find("es:activityDescription/es:activity", ns)
flow = dataset.find("es:flowData", ns)
if activity is None or flow is None:
    raise ValueError("缺少活动描述或 flowData")
print("活动 UUID：", activity.get("id"))

reference_rows = []
for exchange in flow.findall("es:intermediateExchange", ns):
    group_text = exchange.findtext("es:outputGroup", namespaces=ns)
    if group_text is not None and int(group_text) == 0:
        reference_rows.append(exchange)
if len(reference_rows) != 1:
    raise ValueError("请明确处理参考输出缺失或多个参考输出的情况")
reference = reference_rows[0]
reference_amount = Decimal(reference.attrib["amount"])
if not reference_amount.is_finite() or reference_amount <= 0:
    raise ValueError("这个简单比例示例需要有限且正的参考输出量")

for tag in ("intermediateExchange", "elementaryExchange"):
    for exchange in flow.findall("es:" + tag, ns):
        raw = exchange.attrib["amount"]
        quantity = Decimal(raw)
        if not quantity.is_finite():
            raise ValueError("交换量必须是有限数字")
        names = [n.text for n in exchange.findall("es:name", ns)]
        units = [n.text for n in exchange.findall("es:unitName", ns)]
        print(tag, exchange.get("id"), names, raw, units,
              "相对于一个参考单位：", quantity / reference_amount)
```

属性用 `exchange.attrib["amount"]` 读取，是为了让缺少必需数量时明确报错；对于本来可选的 `activityLinkId`，则可用 `.get("activityLinkId")` 保留缺失状态。缺失不是零，`"0"` 也不是缺失。程序用 `is None` 判断节点是否存在，不用节点的真假值，以免把无子元素的合法节点判断成不存在。

这个例子把所有语言的名称和单位都显示出来。正式筛选时，应选用明确的语言回退策略并保留原文，而不是每次只读第一个 `name`。真正识别对象时，还应优先采用 UUID、上下文、区室和单位，名称用于阅读和辅助检索。

### 完整提取器：保留关系，而不是把所有 amount 摊成一列

[下载提取脚本 extract_ecospold.py](demo/extract_ecospold.py)。它只使用 Python 标准库。将脚本与下载的 demo 放在同一目录后，可以先分别运行以下命令：

```sh
python3 extract_ecospold.py demo-product.spold --out output-upr --kind upr --language zh
python3 extract_ecospold.py demo-lcia.spold --out output-lcia --kind lcia --language zh
```

要在本次导出范围内解析供应引用，可把两个 UPR demo 放入同一个目录，再对该目录运行脚本。文件夹读取会递归收集 `.spold` 和 `.xml` 文件；建议把不同数据库版本、系统模型和导出阶段分开放置，以便解释候选链接。`--kind` 是使用者提供的来源信息；它不会把 UPR 变成 LCI，也不会凭 `type` 自动猜测下载类型。未明确时使用默认的 `unknown`，把不确定性保留在结果中。

脚本写出的 `metadata.json` 保留活动、地区、时间、模型、上下文和版本信息；`exchanges.csv` 逐行保留交换实例、产品或基本流 UUID、原量、单位、方向分组及相对于参考输出的比例。它另外导出 `parameters.csv`、`properties.csv` 和 `impacts.csv`，避免把参数值、属性值和 LCIA 指标值混成同一类数量。`uncertainty.json` 保留分布和属性结构；`supplier-links.json` 表示供应引用在当前导出范围内是否找到候选。

归一化列只是一条交换量与唯一正参考输出量的比例。原始字符串仍保留，负号仍保留；属性、参数和年度产量不会自动跟着交换量缩放。如果没有参考输出、参考输出为零或负值，或存在多个参考输出，脚本不给出一个假装明确的规范化结果。也不展开继承或计算分配。

这些 CSV 可以用于后续筛选或导入自己的数据表，但请同时带上元数据。比如比较两个文件的电力输入时，先确认两者的参考产品和单位、系统模型、地区、年份，以及数据集是普通单元过程还是累积结果。只拼接“名称、amount”两列，会丢掉这些决定数值含义的条件。

### 把问题变成明确的查询：电力、直接排放和现成影响指标

下面把“拿到自己想要的数据”落实成三个可以运行的查询。先将 `extract_ecospold.py`、`demo-product.spold`、`demo-electricity.spold` 和 `demo-lcia.spold` 放在同一目录，再[下载查询脚本 query_demo.py](demo/query_demo.py)，或将下面完整代码保存为该目录中的 `query_demo.py`。在该目录运行 `python3 query_demo.py` 即可，全部依赖都来自 Python 标准库，无需安装 pip 包。代码通过 `Path(__file__).resolve().parent` 找到同目录文件，因此保存为脚本后，也可以从其他工作目录运行它。

三个文件及代码中的所有 UUID 都是教学构造，不是 ecoinvent 的真实数据或真实对象标识。用于自己的文件时，第一步应读出其元数据和候选记录，确认活动、产品或基本流、区室、单位、系统模型和导出阶段，再从实际 XML 与对应主数据中确认 UUID 及上下文；不能把下面的教学 UUID 直接套在真实数据上。代码中的预期行数和预期数值也是针对教学文件的核对条件，改用自己的文件时，应按研究目标重新定义这些条件。

第一项查询从 `exchanges` 取电力中间交换的 `input` 行，同时匹配产品 UUID、有效上下文及单位 UUID、有效上下文。主 UPR 的参考输出为 10 kg 教学产品，所以电力原量 25 kWh 对应的 `normalized_amount` 是 2.5 kWh/kg 教学产品。代码虽然一起读取了供给电力的教学 UPR，却先以活动 UUID、上下文和唯一 `dataset_key` 限定主产品过程；供给过程自身的排放不会进入本过程的直接排放查询。`kind='upr'` 是我们根据文件来源声明的阶段，不会触发网络计算。

第二项查询取主 UPR 的化石源 CO₂ 基本流 `output`。筛选键包含流 UUID 与有效上下文、子区室 UUID 与有效上下文、单位 UUID 与有效上下文这六项身份信息，另明确要求基本流输出分组。区室的“空气”和子区室的“未指定”由这里选定的子区室主数据身份确定，名称只用于解释。有效上下文指显式引用上下文，或引用属性省略时回退到文件自身上下文；提取器已完成这一步。两个不同交换实例的原量 1.5 和 -0.1 都保持 `output`，方向由分组定义，不能因负号改成输入，也不能取绝对值。按同一完整键汇总，两行净量为 1.4 kg，归一化净量为 0.14 kg/kg 教学产品。生物源 CO₂ 有另一个流 UUID，其 0.2 kg 单独显示并排除在化石源净量之外。这里有意要求恰好两条教学记录；在真实文件中多条同键记录可能是合法的，应保留交换实例，明确汇总口径后再求和，不能无条件只拿第一条或删除重复名称。

第三项查询从 `impacts` 读取现成的模拟 LCIA 指标，逐层匹配方法、类别、指标各自的 UUID 与有效上下文，并核对 `unitName` 为 `kg CO2-eq`。这种指标字段以单位名称记录单位，不应凭空补上交换量所用的单位 UUID。教学文件中的原指标量是 13.9 kg CO2-eq，参考输出同样为 10 kg，归一化量是 1.39 kg CO2-eq/kg 教学产品。它来自文件中已存的 `impactIndicator/@amount`，不是把前面的直接 CO₂ 净量当成任意气候指标，也不是本程序算出了完整 LCIA。

三个查询都先检查结果数量：预期唯一的活动、电力或指标若缺失或多匹配，会明确报错；预期的两条化石记录也核对数量及实例 UUID。没有唯一正参考输出，或 `normalized_amount` 缺失时，代码拒绝给出归一化量。原量和归一化量使用 `Decimal`，求和保留符号，整个代码不执行公式文本。下面的数值检查用于复现教学结果；归一化只是相对于参考输出的算术比例，不能代替分配、继承展开、上游网络求解或影响评价计算。

```python
#!/usr/bin/env python3
"""查询教学构造数据；只读已存数值，不执行公式或计算产品系统。"""
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path

from extract_ecospold import extract


# 以下 UUID 全部来自随文教学 demo，不能用于筛选真实 ecoinvent 数据。
DEMO = Path(__file__).resolve().parent
CONTEXT = "f71ac544-3bc8-5c15-8ea4-072d907663f1"
PRODUCT_ACTIVITY = "19d3e06c-2a4a-545d-b368-6470e75e1a27"
LCIA_ACTIVITY = "fc37834f-30b0-5563-b8f5-16fb8683b395"
ELECTRICITY = "cf4dd220-d849-5595-92fe-1dac1fcecae7"
FOSSIL_CO2 = "f420b314-c085-57e7-ba47-5cdfa839e9a3"
BIOGENIC_CO2 = "d951f598-3f40-57c4-ba76-71df73f1096b"
AIR_UNSPECIFIED = "6bbb1a41-12de-5599-843e-cc02d4084a9a"
KG = "a4800e12-54b1-5444-a6d0-b48a59529439"
KWH = "a5533771-6995-50cd-b03c-7a2af998708e"
METHOD = "496741dc-72ec-5f95-bedb-078512fde969"
CATEGORY = "07a7bfca-c863-5fd0-a2bf-24aa3af0d959"
INDICATOR = "9ce9802d-268d-5ac0-af08-ffca6dc91aa2"


def require_count(rows, expected, label):
    if len(rows) != expected:
        raise ValueError(f"{label}：预期 {expected} 行，实际 {len(rows)} 行；请核对缺失或多匹配")
    return rows


def quantity(raw, label):
    if raw is None or str(raw).strip() == "":
        raise ValueError(f"{label}：数值缺失，不能替换为零")
    try:
        value = Decimal(raw)
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"{label}：不是有效十进制数 {raw!r}") from exc
    if not value.is_finite():
        raise ValueError(f"{label}：数值必须有限")
    return value


def normalized(row):
    if row.get("normalization_status") != "unique-positive-reference":
        raise ValueError("没有唯一正参考输出，不能使用 normalized_amount")
    return quantity(row.get("normalized_amount"), "normalized_amount")


def expect(actual, expected, label):
    if actual != Decimal(expected):
        raise ValueError(f"{label}：教学结果应为 {expected}，实际为 {actual}")


def dataset_meta(result, activity_id, label):
    matches = [m for m in result["metadata"]
               if m["activity_id"] == activity_id and m["context_id"] == CONTEXT]
    meta = require_count(matches, 1, label)[0]
    norm = meta["normalization"]
    if norm["status"] != "unique-positive-reference":
        raise ValueError(f"{label}：参考输出缺失、多条、零值或负值")
    expect(quantity(norm["reference_amount"], "参考数量"), "10", label + "参考数量")
    refs = [r for r in result["exchanges"]
            if r["dataset_key"] == meta["dataset_key"]
            and r["exchange_id"] == norm["reference_exchange_id"]]
    ref = require_count(refs, 1, "参考交换实例")[0]
    if (ref["unit_id"], ref["unit_context_id"], ref["unit_name"]) != (KG, CONTEXT, "kg"):
        raise ValueError("教学参考输出的单位应为指定上下文的 kg")
    return meta


def elementary_key(row):
    # 三个对象各用 UUID + 有效上下文；有效上下文已由提取器处理省略回退。
    return (row["flow_id"], row["flow_context_id"],
            row["subcompartment_id"], row["subcompartment_context_id"],
            row["unit_id"], row["unit_context_id"])


def main():
    upr = extract([DEMO / "demo-product.spold", DEMO / "demo-electricity.spold"],
                  language="zh", kind="upr")
    meta = dataset_meta(upr, PRODUCT_ACTIVITY, "教学产品 UPR")
    # 限定主 UPR，供应过程的直接排放不混入本过程直接排放。
    rows = [r for r in upr["exchanges"] if r["dataset_key"] == meta["dataset_key"]]
    print("教学产品基准：10 kg（唯一正参考输出）")

    electricity = [r for r in rows if r["exchange_kind"] == "intermediateExchange"
                   and r["direction"] == "input"
                   and (r["flow_id"], r["flow_context_id"], r["unit_id"], r["unit_context_id"])
                   == (ELECTRICITY, CONTEXT, KWH, CONTEXT)]
    power = require_count(electricity, 1, "指定电力输入")[0]
    expect(quantity(power["amount"], "电力原量"), "25", "电力原量")
    expect(normalized(power), "2.5", "电力归一化量")
    print(f"电力 input：{power['amount']} kWh；normalized_amount={normalized(power)} kWh/kg 教学产品")

    fossil_key = (FOSSIL_CO2, CONTEXT, AIR_UNSPECIFIED, CONTEXT, KG, CONTEXT)
    fossil = [r for r in rows if r["exchange_kind"] == "elementaryExchange"
              and r["direction"] == "output" and r["group_code"] == 4
              and elementary_key(r) == fossil_key]
    require_count(fossil, 2, "教学化石 CO₂ 输出记录")
    if len({r["exchange_id"] for r in fossil}) != 2:
        raise ValueError("化石 CO₂ 的交换实例 UUID 重复")
    amounts = [quantity(r["amount"], "化石 CO₂ 原量") for r in fossil]
    if sorted(amounts) != sorted([Decimal("1.5"), Decimal("-0.1")]):
        raise ValueError("教学化石 CO₂ 应保留 1.5 和 -0.1 两行，不改负号或方向")
    with localcontext() as ctx:
        ctx.prec = 50
        net = sum(amounts, Decimal("0"))
        net_normalized = sum((normalized(r) for r in fossil), Decimal("0"))
    expect(net, "1.4", "化石 CO₂ 净量")
    expect(net_normalized, "0.14", "化石 CO₂ 归一化净量")
    for r in fossil:
        print(f"化石 CO₂ {r['direction']} 行：amount={r['amount']} kg；normalized_amount={normalized(r)} kg/kg 教学产品")
    print(f"直接化石 CO₂ 净量：{net} kg；normalized 净量={net_normalized} kg/kg 教学产品")

    bio_key = (BIOGENIC_CO2, CONTEXT, AIR_UNSPECIFIED, CONTEXT, KG, CONTEXT)
    bio = require_count([r for r in rows if r["exchange_kind"] == "elementaryExchange"
                         and r["direction"] == "output" and elementary_key(r) == bio_key],
                        1, "教学生物源 CO₂ 输出")[0]
    expect(quantity(bio["amount"], "生物源 CO₂"), "0.2", "生物源 CO₂")
    print(f"生物源 CO₂ 排除：{bio['amount']} kg；未计入化石 CO₂ 净量")

    lcia = extract([DEMO / "demo-lcia.spold"], language="zh", kind="lcia")
    lcia_meta = dataset_meta(lcia, LCIA_ACTIVITY, "教学模拟 LCIA")
    impact_key = (METHOD, CONTEXT, CATEGORY, CONTEXT, INDICATOR, CONTEXT, "kg CO2-eq")
    impacts = [r for r in lcia["impacts"] if r["dataset_key"] == lcia_meta["dataset_key"]
               and (r["impactMethodId"], r["impactMethodContextId"],
                    r["impactCategoryId"], r["impactCategoryContextId"],
                    r["impactIndicatorId"], r["impactIndicatorContextId"], r["unit_name"])
               == impact_key]
    impact = require_count(impacts, 1, "指定方法/类别/指标及单位")[0]
    expect(quantity(impact["amount"], "模拟 LCIA 原量"), "13.9", "模拟 LCIA 原量")
    expect(normalized(impact), "1.39", "模拟 LCIA 归一化量")
    print(f"模拟 LCIA 指标：{impact['amount']} {impact['unit_name']}；normalized_amount={normalized(impact)} kg CO2-eq/kg 教学产品")


if __name__ == "__main__":
    main()
```

运行后，电力查询显示 `25` 和 `2.5`；两条化石 CO₂ 输出分别显示原量 `1.5`、`-0.1` 以及归一化量 `0.15`、`-0.01`，净量为 `1.4` 和 `0.14`；生物源 `0.2` 明确排除；模拟 LCIA 显示 `13.9` 和 `1.39`。保留这些原行、筛选键及参考输出，才可以解释这个数从哪个过程、哪类流和哪个基准而来。


### 按你的问题筛选数据

如果想取电力消耗，应筛选中间交换中的输入，并以明确的产品 UUID 或经过确认的产品集合识别电力，然后核对 kWh、MJ 等单位。单靠名称含有 electricity 的字符串筛选可以用于初步查找，但最终统计应核对产品身份；供给市场、电压等级和不同产品不应被无条件视作相同对象。相对于参考产品的比率取 `normalized_amount`，原始清单量取 `amount`，并把参考输出的单位带在结果旁。

如果想取某种污染物的直接排放，应筛选基本流输出，匹配其基本流主数据 UUID 及有效上下文、区室、子区室及其有效上下文，以及单位 UUID 及有效上下文，并保留正负记录。同名物质在水、土壤或不同空气子区室的环境意义可能不同。聚合时先说明是在统计毛记录、净量还是某组区室；示例中化石源与生物源 CO2 也要分别处理。

如果想取材料属性，例如某交换的干质量，应在 `properties.csv` 找到其所属交换实例，再匹配属性 UUID 与单位，阅读属性定义后决定怎样与交换量组合。属性量可能按单位产品给出，也可能有其他语义。不能因为“dry mass”这个名称就无条件执行“交换量乘属性值”，更不能把属性量当作一笔额外的投入或排放。

如果想取现成的碳足迹或其他影响指标，应在 `impacts.csv` 按方法、类别和指标 UUID 筛选，保留单位及参考输出。如果文件没有该指标，空结果表示文件没有提供它；需要获得相应 LCIA 导出或按适用方法另行计算。不能把 CO2 物质量之和替换成任意气候变化指标，也不能把多个不同单位或层级的指标相加。

如果想沿上游找供应过程，应先看供应引用是否明确、目标产品与上下文是否一致，以及目标是否在当前导出中。匹配到一个文件，只表示找到了这条引用的候选，不代表全系统已经闭合。在真实数据库中，多个参考产品、模型、地区、时间和版本可能让同一活动 UUID 对应多个候选；缺失引用也可能要依靠数据库的链接规则。完整产品系统还可能有循环和多功能过程，需要适当的清单计算工具处理，不能用这个读取脚本的候选连接代替网络求解。

### 把公式和不确定性当作另一个层次的信息

demo 中的电力参数为每 kg 产品 2.5 kWh，交换量则为 25 kWh。它们之间的关系写在数学关系字段里。提取脚本会读出参数、交换量和公式文本；它不会用 Python 的 `eval()` 执行公式。ecoSpold 的公式语言有自身规则，且变量名、继承和取值范围需要按规范解析。对于已提供 `amount` 的导出，读取器应先保留该量及是否为计算量的标记，而不是用一个随意实现的公式求值器覆盖它。

demo 中的对数正态分布分别记录 meanValue、mu、基础方差和含谱系不确定性的方差。读取平均交换量不等于做了一次蒙特卡洛抽样；把方差当作标准差也会改变分布。[不确定性章节](uncertainty.md)解释这些字段，并把原始参数保留在独立 JSON 中。需要传播不确定性时，应选用正确的分布参数化和适用工具，先处理规范里的原文疑点。

[先看 demo 的具体 XML 节点](demo-walkthrough.md) · [保留数据解释与追溯信息](provenance.md)
