'''
DFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 78.73 % of python3 submissions.
You are here!
Your memory usage beats 8.58 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subsum = set()
        MOD = 10 ** 9 + 7
        
        def dfs(node: TreeNode):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subsum.add(s)
            return s
        
        total = dfs(root)
        maxp = 0
        for sub in subsum:
            maxp = max(maxp, (total - sub) * sub)
        return maxp % MOD
