# -*- coding:utf-8 -*-
"""

"""


class CNode(object):
    def __init__(self, tPos, iParentScore=0, tPrentPos=(0, 0), iScore=0):
        self.tPos = tPos
        self.iScore = iScore
        self.iParentScore = iParentScore
        self.tParentPos = tPrentPos

    def getDirction(self):


    def SetScore(self, iToHereCost):
        self.iScore = self.iParentScore + iToHereCost

    def __lt__(self, other):
        return self.iScore < other.iScore

    def __gt__(self, other):
        return self.iScore > other.iScore

    def __eq__(self, other):
        return self.iScore == self.iScore
