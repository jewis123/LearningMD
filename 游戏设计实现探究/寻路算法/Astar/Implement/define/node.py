# -*- coding:utf-8 -*-
"""
节点定义

欧氏距离（八向）：  dis = sqrt((x2 -x1)**2 + (y2- y1)**2)
曼哈顿距离（四向）：dis = (x2 -x1) + (y2- y1)
"""


class Node:
    def __init__(self, tCurPos, tStartPos, tEndPos):
        self.gx = self.cal_gx(tCurPos, tStartPos)
        self.hx = self.cal_hx(tCurPos, tEndPos)
        self.fx = self.cal_fx()
        self.parent = None

    def cal_gx(self, tCurPos, tStartPos):
        return sum(tCurPos) - sum(tStartPos)

    def cal_hx(self,  tCurPos, tEndPos):
        return sum(tCurPos) - sum(tEndPos)

    def cal_fx(self):
        return self.gx + self.hx

    def GetFx(self):
        return self.fx

    def GetParent(self):
        return self.parent

    def SetParent(self, oNode):
        self.parent = oNode
