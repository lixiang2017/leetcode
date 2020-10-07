'''
DFS

You are here!
Your runtime beats 99.41 % of python submissions.
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
        if not root:
            return True
        
        def isMirror(tree1, tree2):
            if not tree1 or not tree2:
                return tree1 == tree2
            
            if tree1.val != tree2.val:
                return False
            
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left) # caution the order of nodes!
        
        return isMirror(root.left, root.right)
        
        
        