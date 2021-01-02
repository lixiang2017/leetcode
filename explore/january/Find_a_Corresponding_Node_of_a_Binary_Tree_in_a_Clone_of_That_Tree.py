'''
DFS

You are here!
Your runtime beats 74.55 % of python submissions.
You are here!
Your memory usage beats 67.88 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        target_value = target.val
        def dfs(node, value):
            if node:
                if node.val == value:
                    return node
                return dfs(node.left, value) or dfs(node.right, value)
        
        return dfs(cloned, target_value)
        
        