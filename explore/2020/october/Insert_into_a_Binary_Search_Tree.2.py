'''
use helper function

You are here!
Your runtime beats 75.93 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def helper(root, val):
            if not root:
                return TreeNode(val)
            
            if val < root.val:
                root.left = helper(root.left, val)
            else:
                root.right = helper(root.right, val)
            
            return root
        
        return helper(root, val)