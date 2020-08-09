# -*- coding:utf-8 -*-
"""
A* 优化方案

- 移除CloseList改用节点属性保存可访问性，可将判断合法性由O(N)降到O(1)

- 获取最小Fx节点目前是用列表遍历， 可以构造最小堆。
                    插入            取最小
            优化前：   1            O(N)
            优化后：O(logN)          1

- 增加 Hx 在启发函数中的比重： 增加选点策略对目标的导向型
"""


import heapq

class Heap:
    """
    定制存放节点的小根堆, 可以参看heapq
    """

    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def IsEmpty(self):
        return not self.heap

    def push(self, val):
        self.heap.append(val)
        self.siftdown(self.heap, 0, len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise ValueError("head is empty! can not pop")
        lastElem = self.heap.pop()
        if self.heap:
            returnItem = self.heap[0]
            self.heap[0] = lastElem
            self.siftup(self.heap, 0)
            return returnItem
        return lastElem

    def peek(self):
        if not self.heap:
            raise ValueError("head is empty!")
        return self.heap[0]

    def siftdown(self, heap, startpos, pos):
        """由于新元素的出现，且处于不适宜的最底层，所以把比他大还在它上面的数都挪下来"""
        newItem = heap[pos]
        while pos > startpos:
            iParentIdx = (pos - 1) >> 1
            oParent = heap[iParentIdx]
            if newItem.GetFx() < oParent.GetFx():
                heap[pos] = oParent
                pos = iParentIdx
                continue
            break
        heap[pos] = newItem

    def siftup(self, heap, pos):
        """由于取走了原先最小的数，把最后一个数放在了不适宜的顶部，所以把比他小还处于下层的数挪上来"""
        iEndPos = len(heap)
        iStartPos = pos
        newItem = heap[pos]
        # 将更小的节点上移，直到遇到叶节点
        iChildPos = 2 * pos + 1  # 最左边的孩子
        while iChildPos < iEndPos:
            iRightPos = iChildPos + 1
            if iRightPos < iEndPos and not heap[iChildPos].GetFx() < heap[iRightPos].GetFx():
                iChildPos = iRightPos
            heap[pos] = heap[iChildPos]
            pos = iChildPos
            iChildPos = pos * 2 + 1
        heap[pos] = newItem
        self.siftdown(heap, iStartPos, pos)
