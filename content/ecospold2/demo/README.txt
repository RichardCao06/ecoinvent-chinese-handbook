EcoSpold2 教学构造数据与提取器

此目录的三个 .spold 文件完全由教程构造，不是 ecoinvent 数据库记录。活动、产品、基本流、区室、地域、系统模型、人员及影响方法 UUID 均为固定教学标识；邮箱为 demo@example.invalid。中英文标签明确标识教学用途。XSD 合法仅表示符合官方 EcoSpold02 格式，不意味着 master data 已在真实数据库登记、内容经官方认证或指标采用官方方法。

三个文件的用途

demo-product.spold：type=1，参考产品为 10 kg。电力输入 25 kWh，activityLinkId 指向 demo-electricity.spold 的活动；水资源输入为 0.04 m3；空气中的化石源 CO2 输出分别为 1.5 kg 与 -0.1 kg，两行共享基本流 master UUID 和区室，但交换实例 id 不同。-0.1 仍是 output，方向由 outputGroup=4 决定。生物源 CO2 输出为 0.2 kg，另用一个 master UUID，不能按名称或化学式与化石源流合并。参数 electricity_intensity 为 2.5 kWh/kg；参考产品的 dry mass 属性为 1 kg/kg，属性 amount=1 不是产品交换 amount=10。电力交换保存 mathematicalRelation 字符串 electricity_intensity * 10，不执行公式；其对数正态参数 meanValue=25、mu=3.2188758248682006（ln 25）、variance=0.01、varianceWithPedigreeUncertainty=0.04 用于展示原结构读取。

demo-electricity.spold：type=1，参考电力为 1 kWh，化石源 CO2 直接输出为 0.5 kg。

demo-lcia.spold：type=2，模拟预先提供的结果，参考产品仍为 10 kg，化石源 CO2 累计量为 13.9 kg，Teaching GWP (synthetic) 指标为 13.9 kg CO2-eq。13.9 的教学约定来自 1.5 - 0.1 + 25 * 0.5。此指标只使用本例的化石源 CO2 数值，不代表真实 GWP 方法；生物源 CO2 不参与该教学约定。提取器不计算这条供应网络或影响指标，它只读取已写入 XML 的结果。

从 ecoinvent-gitbook 仓库根目录运行（提取仅依赖 Python 标准库）

python content/ecospold2/demo/extract_ecospold.py content/ecospold2/demo --out /tmp/ecospold-teaching-export --language zh

python content/ecospold2/demo/extract_ecospold.py content/ecospold2/demo/demo-lcia.spold --out /tmp/ecospold-teaching-lcia --language en --kind lcia

INPUT 可为一个或多个文件/文件夹；文件夹递归发现 .xml 和 .spold。--language 只选择展示标签，全部原始语言仍保留。--kind 默认 unknown，upr/lci/lcia 只是调用者提供的数据阶段标签，不根据 type=1/2 自动推断。

导出文件与 API

metadata.json：每个 activityDataset 一条记录，包含 activity_id、activity_type、kind、context_id、default_language、所选 name、全部 names、geography、time_period、system_model（含有效 model context）、database_release、dataset_revision、normalization，以及三个非 flowData 部分的原始树 raw_sections。同一 XML 可以有多个 activityDataset。
exchanges.csv：保持每一交换行及原始 amount 字符串、符号、交换实例 exchange_id、master flow_id、方向/group/group_code、单位与上下文、供应活动链接、区室及原始属性/子元素。重复交换不自动合并。
parameters.csv 与 properties.csv：保留各自原始值与单位，不随参考交换缩放；产量 production_volume_amount 也只保留原始数值。
impacts.csv：保留 impactMethodId、impactCategoryId、impactIndicatorId 及各自 context、全部名称和 unitName。TImpactIndicatorResult 没有 unitId/unitContextId，这两列为空；真实指标的单位需要结合指标 master data 核对。这里的 amount 是指标结果而非排放量。
uncertainty.json：以原始 namespace tag、attributes、text 和 children 树保存不确定性及产量不确定性，不重新解释或重算参数。
supplier-links.json：仅在本次导出中按 activityLinkId + 链接上下文 + 产品 master UUID/产品上下文寻找候选，并要求系统模型 ID、有效模型上下文和数据库 majorRelease/minorRelease 已知且相等才确认匹配。省略 systemModelContextId 时合法回退到 file context；如果仍未知则不确认。状态包含 unlinked、not-in-export、ambiguous、matched、context-unavailable、metadata-unconfirmed 与 incompatible-metadata。所有身份相关候选保留 compatibility/reasons、模型、发布版本、修订、地域、时间与单位相符标志，供用户判断。不同 revision/地区/年份不作为拒绝条件；多个相容修订候选仍 ambiguous，不自动选最新。若存在未知元数据候选，也不把唯一已知候选直接确认。匹配不表示已验证工艺适用性或计算了供应网络。

CSV 中列表/字典列采用 JSON 字符串，文件为 UTF-8 BOM。缺失字段在 JSON 为 null，在 CSV 为空；缺失 amount 会明确报错，不当作 0。实际完整 CSV 列名、metadata 字段与数值期望见 extraction-example.json。

Python API：extract(paths, language='zh', kind='unknown') 返回上述七类列表组成的 dict；discover(inputs) 递归查找并去重；write_outputs(result, out) 写文件；main(argv=None) 返回成功 0 或失败 2。

归一化与边界

仅当存在唯一正数量的中间交换参考输出 outputGroup=0 时，exchanges/impacts 提供 normalized_amount=amount/referenceAmount，以 Decimal 精度 50 计算。group 按 XML 整数解析，合法空白、+0、00 不影响参考识别；保留原 group 文本。多个参考、没有参考、零参考、负参考均不给比例并保存 normalization_status。normalized_amount 是每一参考单位的算术比例，不是分配或完整 LCI/LCIA 结果；单位需要结合原单位及参考单位解读。属性、参数、产量不归一化。

提取器拒绝错误 namespace、childActivityDataset（需先展开继承）、方向不明以及非有限或缺失数量；不用数量正负猜方向，不执行数学关系字符串。它不是完整 XSD 验证器。读取后的基本流归并若另行实现，至少应包含 flow_id + flow_context_id + subcompartment_id + subcompartment_context_id + unit_id + unit_context_id，不能按名称合并；省略的上下文按 fileAttributes/contextId 回退。

验证与回归测试

以下测试命令在 GitHub 仓库根目录运行，使用仓库中的 tools/ 和官方原包；独立 demo ZIP 用于运行提取及查询示例，不包含这些仓库测试文件。测试依赖见 tools/requirements.txt，demo/extract_ecospold.py 与 query_demo.py 运行时只用标准库。

python -m unittest discover -s tools -p test_ecospold_tutorial.py -v

测试中的 lxml 只用于官方 XSD 验证；提取器本身不导入 lxml。使用原始 Schemas/datasets/EcoSpold02.xsd，离线 resolver 将包中位于 Schemas/ 的 XmlNamespace.xsd 映射到导入所需位置，不改官方文件。测试覆盖三个 XML 的 XSD 合法性、直接化石 CO2 1.4/10=0.14、电力 2.5、水 0.004、生物源/化石源身份分离、负输出方向、供应链接与歧义、多语言、缺可选项、多数据集、上下文、整数 group、错误 namespace、子数据集继承、无效参考、缺失/非法数字及公式不执行。本次实际运行 12 项测试全部通过（包含三个文件的官方 XSD 验证）；运行命令与文件清单也记录在 extraction-example.json。
