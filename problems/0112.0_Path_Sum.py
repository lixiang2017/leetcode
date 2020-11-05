'''
Success
Details
Runtime: 60 ms, faster than 6.92% of Python online submissions for Path Sum.
Memory Usage: 17 MB, less than 54.26% of Python online submissions for Path Sum.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum

        def dfs(node, current_sum):     
            if not node:
                return False
            print 'node.val: ', node.val, 'current_sum:', current_sum, 'sum: ',sum
            current_sum += node.val  #  !!!
            if not node.left and not node.right and current_sum == sum:
                return True
            
            l = r = False
            l = dfs(node.left, current_sum)
            r = dfs(node.right, current_sum)
            return l or r
            
        return dfs(root, 0) 
        