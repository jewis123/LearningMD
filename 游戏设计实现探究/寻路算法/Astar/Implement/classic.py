# -*- coding:utf-8 -*-
"""
经典A*算法

核心思想：
BFS
启发函数 FX = GX+HX
每次选择距离起点与终点的距离和最小的点执行下一轮更新

要点
计算当前点到起点的距离: GX
    - if parent.gx < cur.gx: cur.gx = parent.gx + 1   #更新
计算当前点到终点的距离: HX
    - 曼哈顿距离：四向
    - 欧式距离： 八向


伪代码：
step1：设置起点S，终点E，地图大小mapsize，障碍物集合Blocklist
step2：将起点S添加到开放列表Openlist中
step3：计算S的目标函数f(x)
step4：查找Openlist中f(x)最小的节点，记为Nmin
step5：将Nmin从Openlist中删除，并添加Nmin到封闭列表Closelist中
step6：查找Nmin的所有邻居节点，得到集合Nlist
step7：对于Nlist中的每个元素N，进行如下循环:
step8： if N 属于 Closelist 或者 N 属于 Blocklist:
step9：      跳过该节点
step10： if N不属于Openlist：
step11：     添加N到Openlist
step12：     设置节点N的父节点为Nmin
step13：     计算节点N的目标函数f(x)
step14： else if N属于Openlist：
step15：     节点N以前计算过f(x)，记原有的f(x)为f(x)_old
step16：     计算节点N以Nmin为父节点的新的目标函数f(x)_new
step17：     if f(x)_new < f(x)_old:
step18：         设置节点N的父节点为Nmin
step19：         并且更新节点N的目标函数f(x) = f(x)_new
step20：         转入step7，循环遍历列表Nlist中的所有邻居节点
step21：转入step4，直到Openlist为空或者Nmin等于终点E
"""

from define.node import Node
from defines import *


class Astar:
    def __init__(self):
        self.lOpen = []
        self.lClose = []
        self.lBlock = []
        self.lNodes = None

    def GenMapNode(self, map):
        self.lNodes = [[None for i in range(I_MAP_WIDTH)] for j in range(I_MAP_HEIGHT)]
        tStartPos, tEndPos = self.getStartEndPos(map)
        for row in range(I_MAP_HEIGHT):
            for col in range(I_MAP_WIDTH):
                oNode = Node((row, col), tStartPos, tEndPos)
                self.lNodes = oNode
                if map[row][col] == S_BLOCK:
                    self.lBlock.append(oNode)
                elif map[row][col] == S_START:
                    self.lOpen.append(oNode)

    @staticmethod
    def getStartEndPos(map):
        tStart = tEnd = (0, 0)
        bStartFind = bEndFind = False
        for row in range(I_MAP_HEIGHT):
            for col in range(I_MAP_WIDTH):
                if map[row][col] == S_START:
                    tStart = (row, col)
                    bStartFind = True
                elif map[row][col] == S_END:
                    tEnd = (row, col)
                    bEndFind = True
                if bEndFind and bStartFind:
                    break
        return tStart, tEnd

    def FindPath(self):
        


if __name__ == "__main__":
    pass
