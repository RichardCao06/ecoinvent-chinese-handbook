"""Shared chapter destinations for the narrative ecoSpold2 handbook."""
GROUPS = [
 ('activity-description','活动描述',[
  ('TActivity','activity','活动'),('TClassification','classification','活动分类'),
  ('TGeography','geography','地理区域'),('TTechnology','technology','技术'),
  ('TTimePeriod','time-period','时间范围'),('TMacroEconomicScenario','macro-economic-scenario','宏观经济情景')]),
 ('flow-data','交换数据与结果',[
  ('TCustomExchange','exchanges','交换的通用字段'),('TIntermediateExchange','intermediate-exchanges','中间交换专用字段'),
  ('TElementaryExchange','elementary-exchanges','基本流交换专用字段'),('TParameter','parameters','参数'),
  ('TImpactIndicatorResult','impact-indicators','影响指标结果')]),
 ('complex-types','复合类型',[
  ('TCompartment','compartments','区室与子区室'),('TUncertainty','uncertainty','不确定性与分布参数'),
  ('TProperty','properties','交换属性'),('TTransferCoefficient','transfer-coefficients','转移系数'),
  ('TTextAndImage','text-and-image','文本、图像与文本变量')]),
 ('modelling-validation','建模与审查',[
  ('TRepresentativeness','representativeness','代表性'),('TReview','review','审查')]),
 ('administrative-information','管理信息',[
  ('TDataEntryBy','data-entry','数据录入者'),('TDataGeneratorAndPublication','publication','数据生成者与发布'),
  ('TFileAttributes','file-attributes','文件属性'),('TRequiredContextReference','required-contexts','所需上下文引用')])]
CHAPTERS = {sid:(slug,title) for _,_,items in GROUPS for sid,slug,title in items}
