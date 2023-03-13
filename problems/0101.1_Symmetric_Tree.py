'''
DFS

Runtime: 46 ms, faster than 10.64% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14 MB, less than 14.51% of Python3 online submissions for Symmetric Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isMirror(one: Optional[TreeNode], another: Optional[TreeNode]) -> bool:
            if not one and not another:
                return True
            elif not (one and another and one.val == another.val):
                return False
            return isMirror(one.left, another.right) and isMirror(one.right, another.left)
        
        return isMirror(root.left, root.right)
