# -*- coding:utf-8 -*-

"""
利用Dijkstra算法实现寻找图的单源最短路径


"""
from graphdata import *

def Dijkstra(iVertexCnt, iSource, MAP):
    """
已知：
    顶点数：iVertexCnt
    图: MAP(V,E)
    源点：iSource
求：从点 iSource 到 其他点的最短距离
路径：最短路径保存在矩阵Routine中
    :return: Routine
    """
    # 初始化
    visited = [False] * iVertexCnt
    lPreNodes = [i for i in range(iVertexCnt)]   # 最短路径中v的前驱结点
    lShortest = [I_NO_WAY] * iVertexCnt     # 源点各顶点的最短距离
    lShortest[iSource] = 0                 # 下标表示具体顶点编号，值表示源点到顶点的最短距离

    for i in range(iVertexCnt): #确定lShortest
        # 寻找距离i点最近的节点iNearestVex，和最短距离lShortest[iNearestVex]
        iNearestVex = -1
        iMin = I_NO_WAY
        for j in range(iVertexCnt):
            if not visited[j] and lShortest[j] < iMin: # 遍历过的直接比较
                iNearestVex = j
                iMin = lShortest[j]

        # 找不到小于INF的最短距离表示源点与剩余节点不连通
        if iNearestVex == -1:
            return lPreNodes

        visited[iNearestVex] = True

        # 松弛操作，更新经过iNearest节点的其他节点最短路径
        for k in range(iVertexCnt):
            if not visited[k] and MAP[iNearestVex][k] != I_NO_WAY and \
                lShortest[iNearestVex] + MAP[iNearestVex][k] < lShortest[k]:

                lShortest[k] = lShortest[iNearestVex] + MAP[iNearestVex][k]
                lPreNodes[k] = iNearestVex

    return lPreNodes


def DfsSearch(iSource, iTarget, lPreNodes, lShorestRoutine):
    if iSource == iTarget:
        lShorestRoutine.append(iSource)
        return
    DfsSearch(iSource, lPreNodes[iTarget], lPreNodes, lShorestRoutine)
    lShorestRoutine.append(iTarget)

if __name__ == '__main__':

    lShorestRoutine = []
    lPreNodes = Dijkstra(6,0, MAP1)
    print(lPreNodes)
    
    #  v = 2: 0->5->2  cost = 2 + 5 = 7
    #  v = 3: 0->4->3  cost = 1 + 4 = 5
    DfsSearch(0, 2,lPreNodes, lShorestRoutine)
    print(lShorestRoutine)