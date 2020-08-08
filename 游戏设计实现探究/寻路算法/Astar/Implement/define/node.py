# -*- coding:utf-8 -*-
"""
节点定义

欧氏距离（八向）：  dis = sqrt((x2 -x1)**2 + (y2- y1)**2)
曼哈顿距离（四向）：dis = (x2 -x1) + (y2- y1)
"""

def UpdateNode(oNode, oNewParent):
    pass

def CalNodeFx(oNode, tStartPos, tEndPos):
    gx = calGx(oNode, tStartPos)
    hx = calHx(oNode, tEndPos)
    fx = gx + hx
    return fx

def calGx(oNode, tStartPos):
    pass

def calHx(oNode, tEndPos):
    pass

class Node:
    def __init__(self, tCurPos):
        self.gx = 0
        self.hx = 0
        self.fx =0
        self.tPos = tCurPos
        self.parent = None

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

    def SetParent(self, oNode):
        self.parent = oNode

    def SetFx(self,iFx):
        self.iFx = iFx
