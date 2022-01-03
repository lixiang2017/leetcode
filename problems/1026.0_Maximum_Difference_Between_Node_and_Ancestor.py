'''
DFS

Runtime: 56 ms, faster than 18.45% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
Memory Usage: 20.7 MB, less than 44.74% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, maxv, minv):
            nonlocal ans
            if not node:
                return 
            maxv = max(maxv, node.val)
            minv = min(minv, node.val)
            ans = max(ans, abs(maxv - minv))
            dfs(node.left, maxv, minv)
            dfs(node.right, maxv, minv)
        
        dfs(root, root.val, root.val)
        return ans 
            
'''
DFS

Runtime: 40 ms, faster than 65.06% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
Memory Usage: 20.7 MB, less than 21.93% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node, maxv, minv):
            nonlocal ans
            if not node:
                return 
            maxv = max(maxv, node.val)
            minv = min(minv, node.val)
            ans = max(ans, maxv - minv)
            dfs(node.left, maxv, minv)
            dfs(node.right, maxv, minv)
        
        dfs(root, root.val, root.val)
        return ans 
            
