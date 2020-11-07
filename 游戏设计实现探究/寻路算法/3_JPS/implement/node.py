# -*- coding:utf-8 -*-
"""
iScore: g(y) = g(x) + dist(x,y)
"""



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

def calByManhadun(tPos, tTarPos):
    return abs(tPos[0] - tTarPos[0]) + abs(tPos[1] - tTarPos[1])

class CNode(object):
    def __init__(self, tPos):
        self.tPos = tPos
        self.oParent = None
        self.bCanGo = True
        self.iScore = float('inf')
        self.bJumpPoint = False
        self.bSelectJumpPoint = False
        self.bForceNeighbour = False
        self.bStart = False
        self.bEnd = False

    def __lt__(self, other):
        return self.iScore < other.iScore

    def __gt__(self, other):
        return self.iScore > other.iScore

    def __eq__(self, other):
        return self.iScore == self.iScore

    def GetMoveDirection(self):
        """获取移动方向"""
        lHori = lVert = lDiag = []
        if(self.oParent == None):
            lHori = [(-1, 0), (1, 0)]
            lVert = [(0, -1), (0, 1)]
            lDiag = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        else:
            tOffset = self.oParent.tPos - self.tPos
            lHori = [(tOffset[0], 0),]
            lVert = [(0,tOffset[1]),]
            lDiag = [tOffset,]




