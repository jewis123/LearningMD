# -*-coding: utf-8 -*-
"""
你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问。
itertools.groupby()
"""

rawdata = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# 先排序数据
rawdata.sort(key=itemgetter('date'))
# 然后根据迭代器分组
for date, items in groupby(rawdata, key=itemgetter('date')):
    print(date, type(items))
    for i in items:
        print(' ', i)
print ('---------------------------')
# 如果你仅仅只是想根据 date 字段将数据分组到一个大的数据结构中去，并且允许随机访问，
# 那么你最好使用 defaultdict() 来构建一个多值字典
from collections import defaultdict

rows_by_date = defaultdict(list)  # 构建multidict
for row in rawdata:
    rows_by_date[row['date']].append(row)

print(rows_by_date)
