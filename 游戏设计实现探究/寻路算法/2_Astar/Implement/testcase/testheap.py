import unittest
from optimization import Heap


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        class CNode:
            def __init__(self, val):
                self.fx = val
            def GetFx(self):
                return self.fx
        self.lNodes = [CNode(11), CNode(3), CNode(2),
                       CNode(5), CNode(84), CNode(1), CNode(6)]
        self.heap = Heap()
        for node in self.lNodes:
            self.heap.push(node)

    def test_pop(self):
        self.assertEqual(self.heap.pop(), self.lNodes[1])


if __name__ == '__main__':
    unittest.main()
