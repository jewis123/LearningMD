# -*-coding: utf-8 -*-
"""
利用heapq实现优先级队列
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))# 优先级为负数的目的是使得元素按照优先级从高到低排序。index 变量的作用是保证同等优先级元素的正确排序。
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
     def __init__(self, name):
         self.name = name
     def __repr__(self):
         return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())