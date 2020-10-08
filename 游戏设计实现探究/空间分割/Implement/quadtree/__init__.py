# -*-coding: utf-8 -*-
from point import CQuadTree
import rect as Rect

class Demo(object):
    def __init__(self,lObjs):
        self.oRect = Rect(0,0,1000,500) # 初始屏幕尺寸
        self.oTree = CQuadTree(0,self.oRect) # 创建四叉树根结点
        self.lAllObjs = lObjs           # 场景中所有物体
        self.AddObjs2QuadTree()

    def AddObjs2QuadTree(self):
        for obj in self.lAllObjs:
            self.oTree.Insert(obj)

    def DoCollision(self,oRect):
        lReturnObj = self.oTree.Retrive(oRect)
        for oCollision in lReturnObj:
             # 碰撞检测
             pass

    def Update(self):
        # self.oTree.Clear()
        # for obj in self.lAllObjs:
        #     self.oTree.Insert(obj)
        #
        # for obj in self.lAllObjs:
        #     # if obj.tag == "Creature"
        #     lReturnObj = self.oTree.Retrive(obj)
        #
        #     for oCollision in lReturnObj:
        #         # 检测是否碰撞
        #         pass

        self.oTree.Refresh()
