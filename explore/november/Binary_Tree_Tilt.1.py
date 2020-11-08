'''
You are here!
Your runtime beats 100.00 % of python submissions.
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
        def findSum(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            
            left_sum = findSum(root.left)
            right_sum = findSum(root.right)
            self.tilt += abs(left_sum - right_sum)
            
            return root.val + left_sum + right_sum
        
        self.tilt = 0
        findSum(root)
        
        return self.tilt
