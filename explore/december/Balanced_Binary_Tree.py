'''
approach: DFS/Recursion

You are here!
Your runtime beats 35.63 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_dept = self.dept(root.left)
        right_dept = self.dept(root.right)
        return abs(left_dept - right_dept) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def dept(self, node):
        if not node:
            return 0
        return max(self.dept(node.left), self.dept(node.right)) + 1




