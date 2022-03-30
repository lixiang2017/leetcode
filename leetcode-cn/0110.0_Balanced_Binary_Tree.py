'''
DFS

执行用时：120 ms, 在所有 Python3 提交中击败了5.75% 的用户
内存消耗：22.6 MB, 在所有 Python3 提交中击败了5.09% 的用户
通过测试用例：228 / 228
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        @lru_cache(None)
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        if not root:
            return True
        elif abs(height(root.left) - height(root.right)) > 1:
            return False 
        return self.isBalanced(root.left) and self.isBalanced(root.right)
