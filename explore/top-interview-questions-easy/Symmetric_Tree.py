'''
Submission Result: Wrong Answer 
Input: [1,2,2,null,3,null,3]
Output: true
Expected: false
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        if not root:
            return True
        elif root.left is None and root.right is None:
            return True
        elif (root.left is None and root.right) or (root.left and root.right is None):
            print root.left, root.right, 'false'
            return False
        
        return root.left.val == root.right.val and self.isSymmetric(root.left) and self.isSymmetric(root.right)
        '''
        def helper(node):
            if not node:
                return True
            if node.left is None and root.right is None:
                return True
            if root.left is None and root.right is not None:
                return False
            if root.left is not None and root.right is None:
                return False
            if root.left.val != root.right.val:
                return False
            return helper(node.left) and helper(node.right)
        
        return helper(root)
        