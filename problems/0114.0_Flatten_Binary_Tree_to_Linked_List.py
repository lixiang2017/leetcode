'''
Runtime: 63 ms, faster than 40.05% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 15.3 MB, less than 10.29% of Python3 online submissions for Flatten Binary Tree to Linked List.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = []
        def dfs(node):
            if not node:
                return
            pre.append(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        for a, b in pairwise(pre):
            a.left = None
            a.right = b 
            