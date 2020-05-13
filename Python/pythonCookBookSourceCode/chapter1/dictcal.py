# -*-coding: utf-8 -*-

"""
需求：在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）
解决方案：
1. zip将键值对翻转，通过新键做操作，但是结果可能并不直接满足条件
2. 直接操作字典，只能获取一半信息（要么操作键，要么操作值）
"""

prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))
# (45.23, 'AAA')
max(zip(prices.values(), prices.keys()))
# (45.23, 'ZZZ')
