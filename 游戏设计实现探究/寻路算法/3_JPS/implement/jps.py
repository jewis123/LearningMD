# -*- coding:utf-8 -*-
"""
假定图上点到点直线距离都为1

跳点搜索逻辑有两种：
1. 强迫邻居也算跳点: 即支持由上一个跳点直接斜向导航到强迫邻居。这个会产生穿插墙壁，或者被墙壁挤开的情况
2. 找到强迫邻居后，再在强迫邻居的直线方向找一个最靠近当前跳点的点作为下一步的跳点


### 算法思路：
初始化OpenSet和CloseSet,将起点加入OpenSet，将障碍加入CloseSet;
遍历OpenSet：
    1. 获取当前搜索点的所有邻居节点，剔除访问过的；将自己加入CloseSet
    2. 先沿着直线方向不断探索，将探索到的感兴趣的点(跳点、终点)加入OpenSet;
    3. 再沿着对角方向不断探索，将探索到的感兴趣的点加入OpenSet;
    4. 探索过程中找到终点，直接结算探索，进行回溯。
"""
from grid import *
from node import *
from defines import *

lStrightDirections = [1]  # ↑，→，↓，←
lDiagnalDirections = [(-1, 1), (1, 1), (-1 - 1), (1, -1)] #↖，↗，↙，↘


isUseBit = 0
isUsePrune = 0
isUsePre = 0

isShowCost = 0


def IsBlock(lMap, tPos):
    return lMap[tPos[0]][tPos[1]] == S_BLOCK



class JPS(object):
    def __init__(self, tStart, tEnd, lMap):
        self.tStartPos = tStart
        self.tEndPos = tEnd
        self.lMap = lMap

    def Run(self):
        import heapq
        lRoadMap = []   # 记录当前点的父节点
        openlist = []   # 待遍历节点
        closelist = []  # 遍历过的节点
        heapq.heappush(openlist, CNode(self.tStartPos))
        while openlist:
            oCur = heapq.heappop(openlist)






if __name__ == '__main__':
    tStart, tEnd = GetTestStartEnd()
    algr = JPS(tStart, tEnd, TEST_MAP)
    algr.Run()
