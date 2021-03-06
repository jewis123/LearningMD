# -*- coding:utf-8 -*-
"""
A* 优化方案

## 计算方面
fx,gx,hx 不要在初始化node时计算，放在遍历时计算，可避免不要节点的计算。

## 寻路方面
- 增加 Hx 在启发函数中的比重： 增加选点策略对目标的导向型，减少遍历数量

- 获取最小Fx节点目前是用列表遍历， 可以构造最小堆。
                    插入          删除              取最小（查+删）
            优化前： O(1)          O(N)             O(N)
            优化后：O(logN)        O(logN)          O(logN)

- 移除CloseList改用节点属性保存可访问性，可将判断合法性由O(N)降到O(1)，用空间换时间

- 分步寻径（TODO）： 在起点到终点增加多个断点， 使得一次寻路变成多次寻路，减少每次的搜索空间。属于分帧思路。

- 合并连续路块（TODO）

## 地图预处理方面
- 合并小格子为大格子： 通常合并障碍格子，以及与紧贴障碍格子的平行格子

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
        """先加入末尾在siftdown"""
        self.heap.append(val)
        self.siftdown(self.heap, 0, len(self.heap) - 1)

    def pop(self):
        """取头，再siftup"""
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
            if newItem.fx < oParent.fx:
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
            if iRightPos < iEndPos and not heap[iChildPos].fx < heap[iRightPos].fx:
                iChildPos = iRightPos
            heap[pos] = heap[iChildPos]
            pos = iChildPos
            iChildPos = pos * 2 + 1
        heap[pos] = newItem
        self.siftdown(heap, iStartPos, pos)
