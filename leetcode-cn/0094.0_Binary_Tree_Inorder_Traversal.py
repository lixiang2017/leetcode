'''
approach: One Line / DFS

执行用时：44 ms, 在所有 Python3 提交中击败了32.70%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了98.79%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return list(chain(self.inorderTraversal(root.left), [root.val], self.inorderTraversal(root.right))) if root else []
