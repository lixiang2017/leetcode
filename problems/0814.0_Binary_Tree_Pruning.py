'''
DFS
T: O(N)
S: O(N)

Runtime: 48 ms, faster than 57.37% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 14 MB, less than 23.50% of Python3 online submissions for Binary Tree Pruning.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def sumTree(node):
            if not node:
                return 0
            left_sum = sumTree(node.left)
            right_sum = sumTree(node.right)
            s = left_sum + right_sum + node.val 
            if 0 == left_sum:
                node.left = None 
            if 0 == right_sum:
                node.right = None
            return s 
    
        s = sumTree(root)
        return root if s != 0 else None 

