'''
You are here!
Your runtime beats 86.30 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        elif low <= root.val <= high:
            left_sum = self.rangeSumBST(root.left, low, high)
            right_sum = self.rangeSumBST(root.right, low, high)
            return left_sum + root.val + right_sum
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else: # root.val > high
            return self.rangeSumBST(root.left, low, high)

    