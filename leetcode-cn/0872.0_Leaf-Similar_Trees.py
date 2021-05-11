'''
approach: DFS
Time: O(N), where N is the number of nodes in the given binary tree.
Space： O(N + N) = O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了11.69% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.67% 的用户
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1, leaves2 = [], []

        def getLeaves(node):
            if not node:
                return
            
            yield from getLeaves(node.left)
            if not (node.left or node.right):
                yield node.val
            yield from getLeaves(node.right)

        leaves1 = list(getLeaves(root1))
        leaves2 = list(getLeaves(root2))
        return leaves1 == leaves2
