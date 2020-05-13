# -*-coding: utf-8 -*-
"""
需求：将字典的键映射到多个值
方法一：键映射的值为一个序列结构
方法二：使用collections.defaultdict
"""

from collections import defaultdict

d = defaultdict(list)  #根据传参确定对应值的数据结构
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d["a"])
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d["a"])



# # 自己创建一个多值映射字典，初始化麻烦
# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)
#
# #如果使用 defaultdict 的话代码就更加简洁了：
#
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)