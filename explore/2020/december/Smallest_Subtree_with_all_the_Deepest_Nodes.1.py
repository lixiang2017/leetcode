'''
You are here!
Your runtime beats 95.70 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root)[1]
        
    
    def helper(self, node):
        '''
            return a pair: [depth, node]
        '''
        if not node:
            return [0, None]
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        # left_depth, right_depth = left[0], right[0]
        diff_depth = left[0] - right[0]
        max_depth = max(left[0], right[0]) + 1
        if 0 == diff_depth:
            # return [left[0] + 1, node]
            return [max_depth, node]
        elif diff_depth > 0:
            # return [left[0] + 1, left[1]]   
            return [max_depth, left[1]]
        else:
            # return [right[0] + 1, right[1]]
            return [max_depth, right[1]]
            