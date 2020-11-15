'''
You are here!
Your runtime beats 13.03 % of python submissions.
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
        
        range_sum = 0
        if low <= root.val <= high:
            range_sum += root.val
        range_sum += self.rangeSumBST(root.left, low, high)
        range_sum += self.rangeSumBST(root.right, low, high)
        return range_sum
    