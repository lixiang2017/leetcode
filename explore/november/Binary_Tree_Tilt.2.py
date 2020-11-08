'''
You are here!
Your runtime beats 87.38 % of python submissions.
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
        self.tilts = []
        self.findSum(root)
        return sum(self.tilts)
    
    def findSum(self, node):
        if not node:
            return 0
        
        left_sum = self.findSum(node.left)
        right_sum = self.findSum(node.right)
        self.tilts.append(abs(left_sum - right_sum))
        return node.val + left_sum + right_sum
    