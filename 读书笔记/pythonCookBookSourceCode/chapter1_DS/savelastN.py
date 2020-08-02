# -*-coding: utf-8 -*-
from collections import deque

"""
利用deque的特性保存最新的N条记录
"""

def search(lList, iMod, history = 2):
    historyDeque = deque(maxlen=history)
    print ('lList',lList)
    for elem in lList:
        if elem % iMod == 0:
            yield elem, historyDeque
        historyDeque.append(elem)



elems = [1,2,3,4,5,6,7,8,9]
for elem, dq in search(elems,5,2):
    print('elem,dq',elem,dq)
    for el in dq:
        print('inner cycle--',el)
    print('outer cycle--',elem)
    print('-'*20)