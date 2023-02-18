'''
DFS

Runtime: 38 ms, faster than 40.79% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14 MB, less than 32.63% of Python3 online submissions for Minimum Distance Between BST Nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = inf
        prev = -inf   
        
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nonlocal ans, prev
            ans = min(ans, node.val - prev)
            prev = node.val 
            dfs(node.right)
            
        dfs(root)
        return ans
    
'''
DFS

Runtime: 35 ms, faster than 56.88% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 13.7 MB, less than 98.72% of Python3 online submissions for Minimum Distance Between BST Nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = inf  
        
        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node.val 
                yield from  dfs(node.right)
            
        for a, b in pairwise(dfs(root)):
            ans = min(ans, b - a)
        return ans
    