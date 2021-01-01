'''
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
        # record the required maximum difference
        self.result = 0
        
        def helper(node, cur_max, cur_min):
            if not node:
                return
            
            # update `result`
            self.result = max(self.result,
                             abs(cur_max - node.val),
                             abs(cur_min - node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)
        
        helper(root, root.val, root.val)
        return self.result