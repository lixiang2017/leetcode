'''
DFS

Runtime: 69 ms, faster than 53.59% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.7 MB, less than 27.99% of Python3 online submissions for Validate Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node.val 
                yield from dfs(node.right)
        
        for a, b in pairwise(dfs(root)):
            if a >= b:
                return False
        return True
                
