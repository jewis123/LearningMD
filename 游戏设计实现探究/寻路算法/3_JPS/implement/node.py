# -*- coding:utf-8 -*-
"""
iScore: g(y) = g(x) + dist(x,y)
"""


class CNode(object):
    def __init__(self, tPos):
        self.tPos = tPos
        self.parent = None
        self.bCanGo = True
        self.iScore = float('inf')
        self.iParentScore = float('inf')

    def __lt__(self, other):
        return self.iScore < other.iScore

    def __gt__(self, other):
        return self.iScore > other.iScore

    def __eq__(self, other):
        return self.iScore == self.iScore

    def getDirctionTuple(self, tFromPos):
        return self.tPos - tFromPos

    def SetScore(self, iToHereCost):
        self.iScore = self.iParentScore + iToHereCost

    def SetParent(self, oNode):
        self.parent = oNode

    def SetFx(self, iFx):
        self.fx = iFx

    def SetIsCanGo(self, bFlag):
        self.bCanGo = bFlag


