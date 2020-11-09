'''
Approach #2: Maximum Minus Minimum

You are here!
Your runtime beats 69.10 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def helper(node, cur_max, cur_min):
            # if encounter leaves, calculate from root to the leaf
            if not node:
                return cur_max - cur_min
            # else, update cur_max and cur_min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)
    
        return helper(root, root.val, root.val)
