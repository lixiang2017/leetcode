'''
You are here!
Your runtime beats 68.49 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        elements = self.inorder(root)
        dummy = TreeNode(-1)
        cur = dummy
        for element in elements:
            node = TreeNode(val = element)
            cur.right = node
            cur = cur.right
            
        return dummy.right

    def inorder(self, node):
        if not node:
            return []
        
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
        