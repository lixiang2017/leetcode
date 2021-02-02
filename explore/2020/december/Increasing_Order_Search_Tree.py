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
        # print 'elements: ', elements
        elements = elements[:: -1]
        pre = None
        for element in elements:
            pre = TreeNode(val = element, right = pre)
        return pre

    def inorder(self, node):
        if not node:
            return None
        
        left = self.inorder(node.left)
        right = self.inorder(node.right)
        # return left + [node.val] + right
        ans = left if left else []
        ans += [node.val]
        if right:
            ans += right
        return ans
    
    