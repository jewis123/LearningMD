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
step20：转入step7，循环遍历列表Nlist中的所有邻居节点
step21：转入step4，直到Openlist为空或者Nmin等于终点E


注意点：
fx,gx,hx 不要在初始化node时计算，可减少计算量
"""

from define.node import *
from defines import *


class CAstar:
    """
    """

    def __init__(self, map):
        self.lOpen = []  # 存点
        self.lClose = []  # 存坐标
        self.lBlock = []  # 存坐标
        self.lNodes = [[None for i in range(I_MAP_WIDTH)] for j in range(I_MAP_HEIGHT)] # 存点
        self.tStartPos = self.tEndPos = ()
        self.map = map

    def GenMapNode(self):
        self.tStartPos, self.tEndPos = GetStartEndPos()
        for row in range(I_MAP_HEIGHT):
            for col in range(I_MAP_WIDTH):
                oNode = Node((row, col))
                self.lNodes[row][col] = oNode
                if self.map[row][col] == S_BLOCK:
                    self.lBlock.append((row, col))
                elif self.map[row][col] == S_START:
                    iFx = CalNodeFx(oNode, self.tStartPos, self.tEndPos)
                    oNode.SetFx(iFx)
                    self.lOpen.append(oNode)

    @staticmethod


    def FindPath(self):
        while self.lOpen:
            oMinFNode = self.getMinFNode()
            for oNeighbour in self.getNodeNeighbours(oMinFNode):
                tCur =  oNeighbour.GetPos()
                iOldFx = oNeighbour.GetFx()
                if tCur in self.lBlock or tCur in self.lClose:  # 剪枝
                    continue
                if oNeighbour in self.lOpen:
                    iNewFx = CalNodeFx(oNeighbour, oMinFNode.GetPos(), self.tEndPos) + oMinFNode.GetFx()
                    if iNewFx < iOldFx:
                        oNeighbour.SetParent(oMinFNode)
                        oNeighbour.SetFx(iNewFx)
                else:
                    iFx = CalNodeFx(oNeighbour, oMinFNode.GetPos(),self.tEndPos)
                    oNeighbour.SetParent(oMinFNode)
                    oNeighbour.SetFx(iFx)
                    self.lOpen.append(oNeighbour)




    def getMinFNode(self):
        iMinIdx, iMin = 0, 0xff
        for idx, oNode in enumerate(self.lOpen):
            if oNode.GetFx() < iMin:
                iMinIdx = idx
                iMin = oNode.GetFx()
        return self.lOpen.pop(iMinIdx)

    def getNodeNeighbours(self, oNode):
        """采用曼哈顿距离执行四向搜索"""
        lDir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 四个方向邻居
        tCur = oNode.GetPos()
        for tDir in lDir:
            row, col = tCur[0] + tDir[0], tCur[1] + tDir[1]
            yield self.lNodes[row][col]



if __name__ == "__main__":
    oLogic = CAstar()
    oLogic.GenMapNode(MAP1)
