# -*- coding:utf-8 -*-
from graphdata import MAP2

"""
特点： 
    1. 适用于等权或无权图，只关心点到点之间能否找到通路
    2. 如果图上点与点之间的连接关系是动态变化的，需要维护MAP2中点与点之间的关系，这里可以分两种情况：
        - 动态给出关系，直接修改MAP2节点连通列表
        - 动态开启/关闭点与点直接的连接，这就需要保存原有图的连接关系，在副本上进行维护
"""

def SearchShortestRoad(iStart, iEnd):
    lShortestRoad = []
    lPre = [-1] * len(MAP2)
    bFound = bfsSearch(iStart, iEnd, lPre)
    if bFound:
        lShortestRoad.append(iEnd)
        while iStart != iEnd:
            lShortestRoad.insert(0, lPre[iEnd])
            iEnd = lPre[iEnd]
    return lShortestRoad


def bfsSearch(iStart, iEnd, lPre):
    lVisited = [False] * len(MAP2)
    queue = [iStart]
    while queue:
        for i in range(len(queue)):  # 层序遍历，保证不因节点连接顺序导致结果出错
            iCur = queue.pop(0)
            lVisited[iCur] = True
            for iVertex in MAP2[iCur]:
                if lVisited[iVertex] or iVertex in queue:
                    continue
                lPre[iVertex] = iCur
                if iVertex == iEnd:
                    return True
                queue.append(iVertex)
    return False


if __name__ == '__main__':
    import time
    import random

    startTime = time.time()
    for _ in range(10000):
        iStart = random.randint(0, 6)
        iEnd = random.randint(0, 6)
        SearchShortestRoad(0, 6)
    endTime = time.time()
    print(endTime - startTime)  # 0.041967153549194336, 0.04288482666015625, 0.04280686378479004

    # print(SearchShortestRoad(4,6))
