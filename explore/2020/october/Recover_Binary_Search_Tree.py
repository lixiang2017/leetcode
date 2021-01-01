'''
O(n) space

You are here!
Your runtime beats 92.21 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        nodes = []
        values = []
        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            nodes.append(root)
            values.append(root.val)
            inorder(root.right)
        
        inorder(root)
        values.sort()
        for node, value in zip(nodes, values):
            node.val = value
        
        
            
        