# -*-coding: utf-8 -*-
import rect as Rect


class CQuadTree(object):
    MAX_OBJECTS = 10  # 划分前拥有节点最大数
    MAX_LEVELS = 5  # 子节点最大深度

    def __init__(self, level, bounds):
        self.iLevel = level  # 该节点的深度，根节点的默认深度为0
        self.lObj = []       # 存储物体对象列表,可能多个对象存在一个子节点中
        self.oRect = bounds  # 该节点对应的象限在屏幕上的范围，bounds是一个矩形
        self.lNodes = []     # 四个子节点列表

    def Clear(self):
        self.lObj = []
        for i in range(len(self.lNodes)):
            if self.lNodes[i]:
                self.lNodes[i].Clear()
                self.lNodes[i] = None

    def Split(self):
        '''某个象限节点内储存的物体数量超过MAX_OBJECTS时，对这个节点进行划分'''
        subWidth = self.oRect.width // 2
        subHeight = self.oRect.height // 2
        x = self.oRect.x
        y = self.oRect.y

        self.lNodes[0] = CQuadTree(self.iLevel + 1, Rect(x + subWidth, y, subWidth, subHeight))
        self.lNodes[1] = CQuadTree(self.iLevel + 1, Rect(x, y, subWidth, subHeight))
        self.lNodes[2] = CQuadTree(self.iLevel + 1, Rect(x, y + subHeight, subWidth, subHeight))
        self.lNodes[3] = CQuadTree(self.iLevel + 1, Rect(x + subWidth, y + subHeight, subWidth, subHeight))

    def GetIndex(self, oRect):
        '''将节点划分象限'''
        bTop = oRect.y + oRect.height <= self.oRect.centroid.y
        bBottom = oRect.y >= self.oRect.centroid.y
        bLeft = oRect.x + oRect.width <= self.oRect.centroid.x
        bRight = oRect.x >= self.oRect.centroid.x

        if bTop:
            if bRight:
                return 0
            else:
                return 1
        elif bBottom:
            if bLeft:
                return 2
            else:
                return 3

        # 跨过多个象限
        return -1

    def Insert(self, oRect):
        '''
        将物体插入四叉树，
        如果节点超过当前节点最大容量，
        该节点分裂并将所有保存的对象分到相应相应子节点下
        （占多个象限的物体依然保存在该节点上）
        '''
        # 如果有子节点，根据物体所在象限保存到相应子节点中
        if self.lNodes:
            index = self.GetIndex(oRect)

            if not index == -1:
                self.lNodes[index].Insert(oRect)
                return

        # 保存物体
        self.lObj.append(oRect)

        # 如果超出当前节点容量
        if len(self.lObj) > CQuadTree.MAX_OBJECTS and self.iLevel < CQuadTree.MAX_LEVELS:
            self.Split()
            i = 0
            for k,v in enumerate(self.lObj):
                index = self.GetIndex(v)
                if not index == -1:
                    self.lNodes[index].Insert(self.lObj.pop(k))

    def Retrive(self, oRect):
        '''
        给出一个对象，返回所有可能与这个对象发生碰撞的列表
        '''
        lresult = []

        if self.lNodes:
            index = self.GetIndex(oRect)
            if not index == -1:
                lresult.extend(self.lNodes[index].Retrive(oRect))
            else:
                arr = oRect.Carve(self.oRect)
                for item in arr:
                    index = self.GetIndex(item)
                    lresult.extend(self.lNodes[index].Retrive(oRect))

        lresult.extend(self.lObj)
        return lresult

    def IsInner(self,oRectObj,oRectBounds):
        return oRectObj.x >= oRectBounds.x \
               and oRectObj.x+ oRectObj.width <= oRectBounds.x + oRectBounds.width \
               and oRectObj.y >= oRectBounds.y \
               and oRectObj.y + oRectObj.height <= oRectBounds.y + oRectBounds.height

    def Refresh(self,oRoot):
        oRoot = oRoot or self
        for k,oRect in enumerate(self.lObj):
            index = self.GetIndex(oRect)

            # 如果矩形不属于该象限，则将该矩形重新插入
            if not self.IsInner(oRect,self.oRect):
                if not self == oRoot:
                    oRoot.Insert(self.lObj.pop(k))
            # 如果矩形属于该象限且该象限具有子象限，就将该矩形插入子象限中
            elif self.lNodes:
                self.lNodes[index].Insert(self.lObj.pop(k))

        # 递归刷新子象限
        for node in self.lNodes:
            node.Refresh(oRoot)