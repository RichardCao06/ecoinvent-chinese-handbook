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
