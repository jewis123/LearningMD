# -*- coding:utf-8 -*-
"""
假定图上点到点直线距离都为1

跳点搜索逻辑有两种：
1. 强迫邻居也算跳点: 即支持由上一个跳点直接斜向导航到强迫邻居。这个会产生穿插墙壁，或者被墙壁挤开的情况
2. 找到强迫邻居后，再在强迫邻居的直线方向找一个最靠近当前跳点的点作为下一步的跳点

"""
from grid import *
from node import *
from defines import *

lStrightDirections = [(0, 1), (0, 1), (0, -1), (-1, 0)]
lDiagnalDirections = [(-1, 1), (1, 1), (-1 - 1), (1, -1)]


def isOuterGrid(lMap, tPos):
    return tPos[0] < 0 or tPos[0] >= len(lMap) or tPos[1] < 0 or tPos[1] >= len(lMap[0])


def isBlock(lMap, tPos):
    return lMap[tPos[0]][tPos[1]] == S_BLOCK


class Jps(object):
    def __init__(self, tStart, tEnd, lMap):
        self.tStartPos = tStart
        self.tEndPos = tEnd
        self.lMap = lMap

    def jumpPointSearch(self):
        import heapq
        lRoadMap = []
        openlist = []
        closelist = []
        heapq.heappush(openlist, CNode(self.tStartPos))
        while openlist:
            oCur = heapq.heappop(openlist)
            for tPrunedNeighbour in self.getPrunedNeighbours(oCur):
                pass


    def getPrunedNeighbours(self, oCurNode):
        """
        获取剔除后的邻居点
        """
        lPrunedNeighbours = []
        lAllDir = lStrightDirections + lDiagnalDirections
        tCurPos = oCurNode.tPos
        for tDir in lAllDir:
            tNeighbour = tCurPos + tDir
            if self.isNeedPrune(tNeighbour, tCurPos, oCurNode.iParentScore):
                continue
            lPrunedNeighbours.append(tNeighbour)
        return lPrunedNeighbours

    def isNeedPrune(self, tNeighbourPos, tCurPos, iCurParentScore):
        """
        满足条件即剔除掉：dist(p(x) -> x -> n) >= dist(p(x) -> 不经x -> n)
        :return:
        """
        if isBlock(self.lMap, tNeighbourPos):
            return True
        # todo

    def findNextJumpPoint(self, tXPos, tDirection):
        tStepNode = tXPos + tDirection  # 沿着方向走一步
        if isBlock(self.lMap, tStepNode) or isOuterGrid(self.lMap, tStepNode):
            return
        if self.tEndPos == tStepNode:
            return tStepNode
        if self.isContainForceNeighbour(tStepNode):
            return tStepNode
        if tDirection in lDiagnalDirections:
            # 分解为两个直线分量
            tHoriDir = (tDirection[0], 0)
            if self.findNextJumpPoint(tStepNode, tHoriDir):
                return tStepNode
            tVerDir = (0, tDirection[1])
            if self.findNextJumpPoint(tStepNode, tVerDir):
                return tStepNode
        return self.findNextJumpPoint(tStepNode, tDirection)  # 沿着方向一直探索

    def isContainForceNeighbour(self, tStepNode):
        pass


if __name__ == '__main__':
    pass
