'''
Success
Details
Runtime: 340 ms, faster than 10.24% of Python online submissions for Subtree of Another Tree.
Memory Usage: 14.6 MB, less than 53.07% of Python online submissions for Subtree of Another Tree.
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isIdentical(s, t):
            return True
        
        if s.left and self.isSubtree(s.left, t):
            return True
        
        if s.right and self.isSubtree(s.right, t):
            return True
        
        return False
        
    
    def isIdentical(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.isIdentical(node1.left, node2.left) and self.isIdentical(node1.right, node2.right)
        
