'''
DFS

Runtime: 86 ms, faster than 10.44% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.4 MB, less than 25.69% of Python3 online submissions for Diameter of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            ans = max(ans, l + r)
            return 1 + max(l, r)
        
        dfs(root)
        return ans
