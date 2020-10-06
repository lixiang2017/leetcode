'''
Submission Result: Wrong Answer 

Input: [10,5,15,null,null,6,20]
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if root.left and root.left.val >= root.val:
            left = False
            return False
        else:
            left = True
        
        if root.right and root.right.val <= root.val:
            right = False
            return False
        else:
            right = True
            
        
        return left and right and self.isValidBST(root.left) and self.isValidBST(root.right)