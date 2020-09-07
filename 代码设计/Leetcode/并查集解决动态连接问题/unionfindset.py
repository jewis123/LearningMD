# -*- coding:utf-8 -*-
"""
解决具有传递性的问题
"""


class TreeNode:
    def __init__(self, iNum):
        self.iVal = iNum
        self.iGroupNum = iNum  # 组别
        self.lChildren = []  # 直接相连的节点
        self.oParent = None  # 父节点
        self.iWeight = 1  # 拥有连通节点数


class UnionFindSet:
    def __init__(self):
        self.dNodes = {}

    def initUnitDict(self, ltPairs):
        """初始化, 每个点元素各自为根节点"""
        lelems = []
        for tPair in ltPairs:
            for elem in tPair:
                if elem not in lelems:
                    lelems.append(elem)
        for elem in lelems:
            self.dNodes[elem] = TreeNode(elem)

    def unionNodePair(self, oNode1, oNode2):
        """
        将小树节点加到大树节点下
        :param oNode1: 大树节点
        :param oNode2: 小树节点
        :return:
        """
        oNode2.oParent = oNode1
        oNode1.lChildren.append(oNode2)
        oNode1.iWeight += oNode2.iWeight
        oNode2.iGroupNum = oNode1.iGroupNum

    def Union(self, ltPair):
        self.initUnitDict(ltPair)
        for tPair in ltPair:
            oNode1, oNode2 = self.getElemNode(tPair)
            root1, root2 = self.findRoot(oNode1), self.findRoot(oNode2)
            if root1 is root2:
                continue
            if root1.iWeight >= root2.iWeight:
                self.unionNodePair(root1, root2)
            else:
                self.unionNodePair(root2, root1)

    def getElemNode(self, tElementPair):
        """
        获取点对对应的节点
        :param tElementPair:
        :return: node1,node2
        """
        return self.dNodes[tElementPair[0]], self.dNodes[tElementPair[1]]

    def findRoot(self, oNode):
        """
        寻找节点的根节点，
        并沿途执行路径压缩: 将经过节点变成其父节点的兄弟节点
        :param oNode:
        :return: root
        """
        root = oNode
        while root.oParent:
            oCur = root
            root = root.oParent
            if root.oParent:
                grandpa = root.oParent
                grandpa.lChildren.append(oCur)
        return root

    def getElemGroup(self, iElem):
        if iElem not in self.dNodes:
            return
        return self.dNodes[iElem].iGroupNum

    def getGroupCnt(self):
        lGroup = []
        for oNode in self.dNodes.values():
            iGroup = oNode.iGroupNum
            if iGroup not in lGroup:
                lGroup.append(iGroup)
        return len(lGroup)

    def PrintElementLinks(self, iElem):
        lRst = []
        for oNode in self.dNodes[iElem].lChildren:
            lRst.append(oNode.iVal)
        print(lRst)


if __name__ == "__main__":
    lRawPairs = (
        (0, 5),
        (5, 6),
        (6, 1),
        (6, 7),
        (1, 2),
        (2, 7),

        (8, 3),
        (8, 9),
        (3, 4),
        (4, 9),
    )

    ufs = UnionFindSet()
    ufs.Union(lRawPairs)
    ufs.PrintElementLinks(0)
    print(ufs.getGroupCnt())
