## dict和defaultdict区别联系

- 联系：dict是父类
- 区别：

| 区别                    | dict           | defaultdict                       |
| ----------------------- | -------------- | --------------------------------- |
| 通过 [ ] 获取不存在的键 | 报KeyError异常 | 通过default_factory创建键并初始化 |
| 创建键并设置默认值      | setdefault     | 通过default_factory创建键并初始化 |
| 初始化速度              | 快             | 慢一半                            |
| 连续增加新键值对速度    | 慢             | 快                                |
|                         |                |                                   |

补充：

- defaultdict可以更快更便捷的对字典元素进行组合处理：分组 / 计数 / 累计 / 去重
- 不指定default_factory，则 defaultdict 退化成 dict 
- defaultdict 通过`[]`自动创建并初始化键值对，若使用get 效果和dict一致
- defaultdict 通过`[]`自动创建并初始化键值对时，值得类型可以是任意指定值的类型，如若不指定就是default_factory类型
- default_factory类型随时可改
- default_factory还能指定为回调，即当访问到一个不存在的键时，执行此回调

### 什么时候用defaultdict

- 如果您的代码在很大程度上是基于字典的，并且一直在处理丢失的键。
- 如果您的字典项需要使用恒定的默认值初始化。 
- 如果您的代码依赖字典来汇总，累加，计数或分组值，并且性能是一个问题。