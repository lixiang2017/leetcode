'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了83.87% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了30.93% 的用户
通过测试用例：8 / 8
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def construct(l, r):
            if l > r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            poss = []
            for i in range(l, r + 1):
                left_trees = construct(l, i - 1)
                right_trees = construct(i + 1, r)
                for left in left_trees:
                    for right in right_trees:
                        node = TreeNode(i)
                        node.left = left 
                        node.right = right 
                        poss.append(node)
            return poss

        return construct(1, n)


