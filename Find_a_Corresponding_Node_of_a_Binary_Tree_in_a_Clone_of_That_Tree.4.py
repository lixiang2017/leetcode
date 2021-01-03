'''
Follow up: Solve the problem if repeated values on the tree are allowed.
target.val is useless, and we should compare target node (the pointer) with one node in original.

DFS
You are here!
Your runtime beats 78.18 % of python submissions.
You are here!
Your memory usage beats 52.12 % of python submissions.
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
        if not original:
            return
        elif original == target:
            return cloned
        
        return self.getTargetCopy(original.left, cloned.left, target) or \
            self.getTargetCopy(original.right, cloned.right, target)
                              