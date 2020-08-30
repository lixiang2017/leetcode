'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3435/
You are here!
Your runtime beats 29.47 % of python submissions
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_sum = 0
        if root:
            if root.left and root.left.left is None and root.left.right is None:
                left_sum += root.left.val
            elif root.left:
                left_sum += self.sumOfLeftLeaves(root.left)
            if root.right:
                left_sum += self.sumOfLeftLeaves(root.right)
                
        return left_sum
