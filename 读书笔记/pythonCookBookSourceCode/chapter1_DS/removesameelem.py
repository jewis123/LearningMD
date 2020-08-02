# -*-coding: utf-8 -*-
"""
需求： 删除序列相同元素并保持顺序
前景：如果不需要保持原有顺序，可以直接使用set
下面针对元素是否为hashable提供两种方案
"""

## hashable元素
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# unhashable元素
def dedupe(items, key=None):  # 通过key将序列元素转换成hashable类型
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))
