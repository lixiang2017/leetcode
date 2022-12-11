'''
DFS + DFS
T: O(N + N)
S: O(logN) for recursive stack

Runtime: 393 ms, faster than 83.94% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
Memory Usage: 74.8 MB, less than 82.99% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = ans = 0
        MOD = 10 ** 9 +7
        
        def dfs(node):
            if not node:
                return 
            nonlocal total
            total += node.val 
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        def subsum(node):
            if not node:
                return 0
            lsum = subsum(node.left)
            rsum = subsum(node.right)
            nonlocal ans
            ans = max(ans, (total - lsum) * lsum, (total - rsum) * rsum)
            return node.val + lsum + rsum 

        subsum(root)
        return ans % MOD
        
