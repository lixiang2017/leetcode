'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了53.11% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了43.84% 的用户
通过测试用例：117 / 117
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 
        elif not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or \
            self.hasPathSum(root.right, targetSum - root.val)

