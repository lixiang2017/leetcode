'''
DFS

看着题干里说层序遍历还有输入输出的格式，还想着要找下子树下标关系。结果是想多了，题干只是为了描述而形式化定义的表达形式。
其实，代码里树的结构每个节点还是Node，类似二叉树递归去处理就行。

执行用时：64 ms, 在所有 Python3 提交中击败了92.86% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了32.86% 的用户
通过测试用例：61 / 61
'''
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if not quadTree1:
            return quadTree2
        if not quadTree2:
            return quadTree1
        if quadTree1.isLeaf and quadTree2.isLeaf:
            v = quadTree1.val | quadTree2.val
            return Node(v, True, None, None, None, None)
        if quadTree1.isLeaf and not quadTree2.isLeaf:
            if 0 == quadTree1.val:
                return quadTree2
            else:
                return quadTree1
        if not quadTree1.isLeaf and quadTree2.isLeaf:
            return self.intersect(quadTree2, quadTree1)

        if not quadTree1.isLeaf and not quadTree2.isLeaf:
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                if 1 == len(set([topLeft.val, topRight.val, bottomLeft.val, bottomRight.val])):
                    return Node(topLeft.val, True, None, None, None, None)
            node = Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
            return node 

