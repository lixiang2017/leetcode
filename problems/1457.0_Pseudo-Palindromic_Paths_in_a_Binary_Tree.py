'''
DFS

Runtime: 3014 ms, faster than 5.30% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
Memory Usage: 85 MB, less than 79.75% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq = [0] * 10
        ans = 0
        
        def dfs(node, freq):
            nonlocal ans 
            if not node:
                return 
            freq[node.val] += 1
            if 1 >= sum(f % 2 for f in freq) and node.left is None and node.right is None:
                ans += 1
            dfs(node.left, freq)
            dfs(node.right, freq)
            freq[node.val] -= 1   ##!!!!!
        
        dfs(root, freq)
        return ans 
