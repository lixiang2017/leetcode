'''
You are here!
Your runtime beats 17.29 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt_root = 0
        if not root:
            return 0
        
        if root.left:
            tilt_root += self.findTilt(root.left)
            sum_left = self.sumNode(root.left)
        else:
            sum_left = 0
        if root.right:
            tilt_root += self.findTilt(root.right)
            sum_right = self.sumNode(root.right)
        else:
            sum_right = 0
            
        tilt_root += abs(sum_left - sum_right)
        return tilt_root

    def sumNode(self, node):
        if not node:
            return 0
        
        sum_of_node = node.val
        if node.left:
            sum_of_node += self.sumNode(node.left)
        if node.right:
            sum_of_node += self.sumNode(node.right)
        return sum_of_node
    