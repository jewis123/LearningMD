# -*- coding:utf-8 -*-
"""
假定图上点到点直线距离都为1

 跳点搜索逻辑有两种：
1. 强迫邻居也算跳点: 即支持由上一个跳点直接斜向导航到强迫邻居。这个会产生穿插墙壁，或者被墙壁挤开的情况
2. 找到强迫邻居后，再在强迫邻居的直线方向找一个最靠近当前跳点的点作为下一步的跳点


 算法思路：
初始化OpenSet,将起点加入OpenSet
遍历OpenSet：
    1. 获取当前搜索点的所有邻居节点，剔除访问过的；将自己加入CloseSet
    2. 先沿着直线方向不断探索，将探索到的感兴趣的点(跳点、终点)加入OpenSet;
    3. 再沿着对角方向不断探索，将探索到的感兴趣的点加入OpenSet;
    4. 探索过程中找到终点，直接结算探索，进行回溯。
"""
from grid import *
from node import *
from defines import *
import heapq
import time

lStrightDirections = [1]  # ↑，→，↓，←
lDiagnalDirections = [(-1, 1), (1, 1), (-1 - 1), (1, -1)]  # ↖，↗，↙，↘

B_USE_BIT = 0  # 是否使用二进制表示地图
B_USE_PRUNE_JP = 0  # 是否剔除无用跳点
B_USE_PRE = 0  # 是否预处理

B_SHOW_SCORE = 0  # 是否显示节点得分

B_DIAGNAL_WITH_NO_BLOCK = 1  # 对角移动不存在障碍

def GetNodeType(lMap, tPos):
	return lMap[tPos[0]][tPos[1]]

def IsOutterBound(tPos):
	row, col = tPos
	if(row < 0
			or row >= I_MAP_WIDTH
			or col < 0
			or col >= I_MAP_HEIGHT):
		return True
	return False


class JPS(object):
	def __init__(self, lMap):
		self.oEndNode = self.oStartNode = None
		self.lOpenList = []
		self.lMap = lMap  # 地图副本，做展示用
		self.lNodes = [[None for i in range(I_MAP_WIDTH)] for j in range(I_MAP_HEIGHT)]  # 存点

		self.genMapNodes()

	def Run(self):
		import heapq
		while self.lOpenList:
			oCur = heapq.heappop(self.lOpenList)
			self.startJump(oCur)
		self.showPathInMap()

	def showPathInMap(self):
		"""展示路径"""
		oCur = self.oEndNode.oParent
		while oCur.oParent:
			row, col = oCur.tPos
			if oCur.bSelectJumpPoint:
				self.lMap[row][col] = S_SELECT_JUMP_POINT
			elif oCur.bJumpPoint:
				self.lMap[row][col] = S_JUMP_POINT
			elif oCur.bForceNeighbour:
				self.lMap[row][col] = S_FORCE_NEIGHBOUR
			else:
				self.lMap[row][col] = S_PATH
			if B_SHOW_SCORE:
				self.lMap[row][col] = "%d!" % oCur.iScore
			oCur = oCur.oParent

		import pprint
		pprint.pprint(self.lMap)

	def genMapNodes(self):
		"""初始化地图节点"""
		for row in range(I_MAP_HEIGHT):
			for col in range(I_MAP_WIDTH):
				oNode = CNode((row, col))
				self.lNodes[row][col] = oNode
				sType = GetNodeType(self.lMap, (row, col))
				if (sType == S_BLOCK):
					oNode.bCanGo = False
				elif (sType == S_START):
					heapq.heappush(self.lOpenList, oNode)
					oNode.bStart = True
					oNode.iScore = 0
					self.oStartNode = oNode
				elif (sType == S_END):
					oNode.iScore = 0
					oNode.bEnd = True
					self.oEndNode = oNode

		self.mapPreDeal()

	def mapPreDeal(self):
		"""地图预处理TODO"""
		pass

	def startJump(self, oCurNode):
		"""
		剔除规则：dist(p(x) -> x -> n) >= dist(p(x) -> 不经x -> n)
		即：现在算的相邻节点得分要比它已有的得分低，才能刷新并作为邻居
		"""
		lHori, lVert, lDiag = oCurNode.GetMoveDirection()
		# 横向跳
		for tDir in lHori:
			search(tDir, oCurNode.tPos)
		# 垂直跳
		# 对角跳

	def search(self, tDir, tCurPos):
		"""
		这个某个方向递归搜索
		"""
		tNextPos = (tDir[0] + tCurPos[0], tDir[1] + tCurPos[1])
		if(IsOutterBound(tNextPos)):
			return
		if(GetNodeType(self.lMap, tNextPos) in (S_END, S_BLOCK)):
			return


if __name__ == '__main__':
	tStart, tEnd = GetTestStartEnd()
	algr = JPS(TEST_MAP)
	iStartTime = time.time()
	algr.Run()
	iEndTime = time.time()
	print("耗时：", iEndTime - iStartTime)
