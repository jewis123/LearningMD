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
step20：转入step4，直到Openlist为空或者Nmin等于终点E


注意点：
fx,gx,hx 不要在初始化node时计算，可减少计算量
"""

from node import *
from defines import *
from optimization import *

B_SHOW_MAP_FX = 0         # 显示节点启发函数得分
B_USE_HEAP = 1            # 使用小根堆存储

B_SHOW_STEP = False
I_STEP = 1

B_DIAGNAL_WITH_NO_BLOCK = 1  # 对角移动不存在障碍
B_DIAGNAL = 1


class CAstar:
    def __init__(self, map):
        self.lOpen = []  # 存点
        self.nodeHeap = Heap()

        self.lNodes = [[None for i in range(I_MAP_WIDTH)] for j in range(I_MAP_HEIGHT)]  # 存点
        self.tStartPos = self.tEndPos = ()
        self.oStartNode = self.oEndNode = None
        self.map = map

        self.genMapNode()

    def appendOpenList(self, oNode):
        if B_USE_HEAP:
            self.nodeHeap.push(oNode)
        else:
            self.lOpen.append(oNode)

    def isOpenListEmpty(self):
        if B_USE_HEAP:
            return not self.nodeHeap.IsEmpty()
        else:
            return self.lOpen != []

    def showPathInMap(self):
        """显示最短路径"""
        global I_STEP
        oCur = self.oEndNode.oParent
        while oCur.oParent:
            row, col = oCur.tPos
            self.map[row][col] = I_STEP if B_SHOW_STEP else S_PATH
            I_STEP += 1
            if B_SHOW_MAP_FX :
                self.map[row][col] = "%d!" % oCur.fx
            oCur = oCur.oParent
        import pprint
        pprint.pprint(self.map)

    def getMinFNode(self):
        """找出OpenList中Fx最小的点, 并移出OpenList"""
        if B_USE_HEAP:
            return self.nodeHeap.pop()
        else:
            iMinIdx, iMin = 0, 0xff
            for idx, oNode in enumerate(self.lOpen):
                if oNode.fx < iMin:
                    iMinIdx = idx
                    iMin = oNode.fx
            return self.lOpen.pop(iMinIdx)

    def getNodeNeighbours(self, oNode):
        """获取当前节点的邻居节点"""
        if not (B_DIAGNAL_WITH_NO_BLOCK or B_DIAGNAL):
            yield from GetNodeNeighbours(oNode, self.lNodes)
        if B_DIAGNAL:
            if B_DIAGNAL_WITH_NO_BLOCK:
                yield from GetNodeNeighboursWithNoObs(oNode, self.lNodes)
            else:
                yield from GetNodeNeighbourAllowCorner(oNode, self.lNodes)

    def genMapNode(self):
        """初始化地图节点"""
        self.tStartPos, self.tEndPos = GetStartEndPos()
        for row in range(I_MAP_HEIGHT):
            for col in range(I_MAP_WIDTH):
                oNode = Node((row, col))
                self.lNodes[row][col] = oNode

                if self.map[row][col] == S_BLOCK:
                    oNode.bCanGo = False

                elif self.map[row][col] == S_START:  # 首先起点加入OpenList
                    iFx = CalNodeFx(oNode, self.tStartPos, self.tEndPos)
                    oNode.fx = iFx
                    self.appendOpenList(oNode)
                    self.oStartNode = oNode

                    if B_SHOW_MAP_FX:
                        self.map[row][col] = str(iFx)

                elif self.map[row][col] == S_END:
                    self.oEndNode = oNode
                    iFx = CalNodeFx(oNode, self.tStartPos, self.tEndPos)
                    oNode.fx = iFx

                    if B_SHOW_MAP_FX:
                        self.map[row][col] = str(iFx)

        self.mapPreDeal()

    def mapPreDeal(self):
        """地图预处理"""
        pass

    def mergeLinkedBlocks(self):
        """合并连接的障碍"""
        pass

    def mergeLinkedRoad(self):
        """合并连接的空路"""
        pass

    def FindPath(self):
        while self.isOpenListEmpty():
            oMinFNode = self.getMinFNode()
            tMinNodePos = oMinFNode.tPos
            if tMinNodePos == self.tEndPos:
                break

            for oNeighbour in self.getNodeNeighbours(oMinFNode):
                iOldFx = oNeighbour.fx
                x, y = oNeighbour.tPos
                if not oNeighbour.bCanGo:  # 剪枝
                    continue
                if oNeighbour in self.lOpen:
                    iNewFx = CalNodeFx(oNeighbour, tMinNodePos, self.tEndPos) + oMinFNode.GetFx()
                    if iNewFx < iOldFx:
                        oNeighbour.oParent = oMinFNode
                        oNeighbour.fx = iNewFx

                        if B_SHOW_MAP_FX:
                            self.map[x][y] = str(iNewFx)
                else:
                    iFx = CalNodeFx(oNeighbour, tMinNodePos, self.tEndPos) + oMinFNode.fx
                    oNeighbour.oParent = oMinFNode
                    oNeighbour.fx = iFx
                    self.appendOpenList(oNeighbour)

                    if B_SHOW_MAP_FX:
                        self.map[x][y] = str(iFx)

            oMinFNode.bCanGo = False

        self.showPathInMap()


if __name__ == "__main__":
    import time

    oLogic = CAstar(MAP1)
    iStartTime = time.time()
    oLogic.FindPath()
    iEndTime = time.time()
    print("耗时：", iEndTime - iStartTime)
