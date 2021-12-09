'''
Runtime: 66 ms, faster than 36.28% of Python3 online submissions for Binary Tree Tilt.
Memory Usage: 16.5 MB, less than 24.41% of Python3 online submissions for Binary Tree Tilt.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        
        def getSum(node: Optional[TreeNode]) -> int:
            nonlocal tilt
            if not node:
                return 0
            ls = getSum(node.left)
            rs = getSum(node.right)
            tilt += abs(ls - rs)
            return ls + node.val + rs
        
        getSum(root)
        return tilt
        