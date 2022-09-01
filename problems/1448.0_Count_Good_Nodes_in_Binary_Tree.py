'''
DFS
T: O(N)
S: O(logN)

Runtime: 271 ms, faster than 91.03% of Python3 online submissions for Count Good Nodes in Binary Tree.
Memory Usage: 32.6 MB, less than 46.30% of Python3 online submissions for Count Good Nodes in Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(node, pre_max):
            nonlocal ans 
            if not node:
                return 
            if node.val >= pre_max:
                ans += 1
                pre_max = node.val
            dfs(node.left, pre_max)
            dfs(node.right, pre_max)
            
        dfs(root, -inf)
        return ans 
