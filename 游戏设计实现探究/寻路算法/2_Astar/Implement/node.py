# -*- coding:utf-8 -*-
"""
节点定义

欧氏距离（八向）：  dis = sqrt((x2 -x1)**2 + (y2- y1)**2)
曼哈顿距离（四向）：dis = |(x2 -x1)| + |(y2- y1)|

启发函数 = DJK策略*比例1 + 目标有限策略*比例2
"""

GX_WEIGHT = 1
HX_WEIGHT = 1


## 基础方案
def GetNodeNeighbours(oNode, lNodeList):
    """四向搜索"""
    lDir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 四个方向邻居
    tCur = oNode.GetPos()
    for tDir in lDir:
        row, col = tCur[0] + tDir[0], tCur[1] + tDir[1]
        if 0 <= row < len(lNodeList) and 0 <= col < len(lNodeList[0]):
            yield lNodeList[row][col]


def GetNodeNeighbourAllowCorner(oNode, lNodeList):
    """
    允许对角， 八向搜索
    """
    lDir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # 八个方向邻居
    tCur = oNode.GetPos()
    for tDir in lDir:
        row, col = tCur[0] + tDir[0], tCur[1] + tDir[1]
        if 0 <= row < len(lNodeList) and 0 <= col < len(lNodeList[0]):
            yield lNodeList[row][col]


def GetNodeNeighboursWithNoObs(oNode, lNodeList):
    """
    允许对角, 同时避免斜穿障碍物顶角
    提前检查每个点的合法性
    当夹住对角的两个直线点都合法时，该对角才合法
    """
    lDirStright = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    lDirDiagnal = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    tCur = oNode.GetPos()
    for tDir in lDirStright:
        row, col = tCur[0] + tDir[0], tCur[1] + tDir[1]
        if 0 <= row < len(lNodeList) and 0 <= col < len(lNodeList[0]):
            yield lNodeList[row][col]

    for tDiagnal in lDirDiagnal:
        row = tDiagnal[0] + tCur[0]
        col = tDiagnal[1] + tCur[1]
        if 0 <= row < len(lNodeList) and 0 <= col < len(lNodeList[0]):
            if lNodeList[row][tCur[1]].IsCanGo() and lNodeList[tCur[0]][col].IsCanGo():
                yield lNodeList[row][col]


def CalNodeFx(oNode, tStartPos, tEndPos):
    gx = calGx(oNode, tStartPos)
    hx = calHx(oNode, tEndPos)
    fx = gx * GX_WEIGHT + hx * HX_WEIGHT  # GX_WEIGHT/HX_WEIGHT越大，遍历规模就越大，路线越趋向最短路线；反之，遍历规模越小，目标导向越强，路线可能不是最优路线（绕路）
    return fx


def calByManhadun(tPos, tTarPos):
    return abs(tPos[0] - tTarPos[0]) + abs(tPos[1] - tTarPos[1])


def calGx(oNode, tStartPos):
    tPos = oNode.GetPos()
    return calByManhadun(tPos, tStartPos)


def calHx(oNode, tEndPos):
    tPos = oNode.GetPos()
    return calByManhadun(tPos, tEndPos)


class Node:
    def __init__(self, tCurPos):
        self.gx = 0
        self.hx = 0
        self.fx = 0
        self.tPos = tCurPos
        self.parent = None
        self.bCanGo = True

    def GetGx(self):
        return self.gx

    def GetHx(self):
        return self.hx

    def GetFx(self):
        return self.fx

    def GetParent(self):
        return self.parent

    def GetPos(self):
        return self.tPos

    def IsCanGo(self):
        return self.bCanGo

    def SetParent(self, oNode):
        self.parent = oNode

    def SetFx(self, iFx):
        self.fx = iFx

    def SetIsCanGo(self, bFlag):
        self.bCanGo = bFlag
