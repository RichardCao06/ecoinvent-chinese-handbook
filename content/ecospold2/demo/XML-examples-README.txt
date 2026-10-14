ecoSpold2 逐章 XML 教学片段

本说明对应独立的 ecospold2-xml-examples.zip，包中包含 xml-examples/、两份字段读取脚本和三份完整教学 .spold。如当前目录没有 xml-examples/，请从 GitBook 各字段章节下载“XML 片段与读取代码 ZIP”。

xml-examples/*.xml 覆盖22种官方类型及243条字段，均为构造的教学数据，不是ecoinvent数据库记录。示例分开显示输入/输出、继承删除标记和8种互斥的不确定性分布。每份片段可用ElementTree独立解析，但它不是完整.spold文件，也没有提供有效的真实主数据引用或完整父链。

read_xml_fields.py 的 field_values(node, relative_path) 读取章节中的路径，例如 @amount、unitName、lognormal/@variance。属性返回原始字符串列表；元素返回包含attributes/text/xml的记录列表。缺失返回[]，不应用默认值、不转换单位、不执行公式、不作归一化或LCA计算。

在此目录运行GitBook每章的提取代码；保持xml-examples子目录。完整.spold应先按本章父级路径选择节点，再传给field_values。名称为es的前缀只是程序中定义的命名空间别名，必须绑定http://www.EcoInvent.org/EcoSpold02。

各片段按官方XSD对应类型进行了结构校验。这里是类型级校验，不覆盖完整文件的父级关系、身份约束、外部主数据或继承语义。查询整份数据集与数量归一化可另从 GitBook“提取与查询实践”下载 ecospold2-tutorial-demo.zip；该完整 demo 包才包含 extract_ecospold.py、query_demo.py 和相应 README.txt。本 XML 片段包不包含这三份文件，主要用于逐字段阅读和定位；不要把类型片段目录作为完整数据集目录交给导出器扫描。
