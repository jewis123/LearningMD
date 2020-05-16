# -*- coding:utf-8 -*-
from graphdata import MAP2

"""
利用BFS搜索点对点最短路径
特点： 
    1. 适用于等权或无权图，只关心点到点之间能否找到通路
    2. 如果图上点与点之间的连接关系是动态变化的，需要维护MAP2中点与点之间的关系，这里可以分两种情况：
        - 动态给出关系，直接修改MAP2节点连通列表
        - 动态开启/关闭点与点直接的连接，这就需要保存原有图的连接关系，在副本上进行修改
"""


def searchShortestRoad(iStart, iEnd, Map):
    lShortestRoad = []
    lPre = [-1] * len(Map)
    bFound = bfsSearch(iStart, iEnd, lPre, Map)
    if bFound:
        lShortestRoad.append(iEnd)
        while iStart != iEnd:
            lShortestRoad.insert(0, lPre[iEnd])
            iEnd = lPre[iEnd]
    return lShortestRoad


def bfsSearch(iStart, iEnd, lPre, Map):
    lVisited = [False] * len(Map)
    queue = [iStart]
    while queue:
        for i in range(len(queue)):  # 层序遍历，保证不因节点连接顺序导致结果出错
            iCur = queue.pop(0)
            lVisited[iCur] = True
            for iVertex in Map[iCur]:
                if lVisited[iVertex] or iVertex in queue:
                    continue
                lPre[iVertex] = iCur
                if iVertex == iEnd:
                    return True
                queue.append(iVertex)
    return False


def refreshMap(lUnReached, MapCopy):
    MapCopy.clear()
    for links in MAP2:
        MapCopy.append(list(links))

    for iVetex, links in enumerate(MapCopy):
        if iVetex in lUnReached:
            MapCopy[iVetex] = []
        else:
            for iLinkVertex in links:
                if iLinkVertex in lUnReached:
                    links.remove(iLinkVertex)


if __name__ == '__main__':


    print(searchShortestRoad(4, 6, MAP2))

    # 动态改变图连通情况
    MapCopy = []
    lUnReached = [1,2,3]  # 1，2，3索引的点不可达
    refreshMap(lUnReached, MapCopy)
    # print(MapCopy)
    print(searchShortestRoad(0, 4, MapCopy))

    import time
    import random
    startTime = time.time()
    for _ in range(10000):
        iStart = random.randint(0, 6)
        iEnd = random.randint(0, 6)
        searchShortestRoad(0, 6)
    endTime = time.time()
    print(endTime - startTime)  # 0.041967153549194336, 0.04288482666015625, 0.04280686378479004
