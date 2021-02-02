'''
Submission Result: Wrong Answer 
Input: [5,4,6,null,null,3,7]
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
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            print 'True'
            return True
        if node.left and node.left.val >= node.val:
            print 'left node: ', node.left.val, 'false'
            return False
        if node.right and node.right.val <= node.val:
            print 'right node: ', node.right.val, 'false'
            return False
        return self.dfs(node.left) and self.dfs(node.right)
    