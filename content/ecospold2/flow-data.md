# 交换数据与结果

本组按官方 XML 结构组织。字段章节同时保留中文说明与英文原文。

| 字段章节 | 模式类型 | 字段条目数 |
| --- | --- | --- |
| [交换的通用字段](exchanges.md) | `TCustomExchange` | 25 |
| [中间交换专用字段](intermediate-exchanges.md) | `TIntermediateExchange` | 18 |
| [基本流交换专用字段](elementary-exchanges.md) | `TElementaryExchange` | 6 |
| [参数](parameters.md) | `TParameter` | 12 |
| [影响指标结果](impact-indicators.md) | `TImpactIndicatorResult` | 11 |

中间交换与基本流交换继承 `TCustomExchange`。查看其中一种交换时，请同时阅读通用字段和该交换的专用字段。

[全部字段索引](field-index.md) · [阅读约定与 XSD 约束](reading-guide.md)
