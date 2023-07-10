'''
Runtime: 639 ms, faster than 18.41% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 57.1 MB, less than 63.22% of Python3 online submissions for Minimum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = inf 
        
        def dfs(node, depth):
            if not node.left and not node.right:
                nonlocal ans 
                ans = min(ans, depth)
                return
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return ans 
        