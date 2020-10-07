'''
Submission Result: Wrong Answer 
Input: [1,2,2,2,null,2]
Output: true
Expected: false
Stdout: inorder:  [2, 2, 1, 2, 2]
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
        
        inorder = []
        def dfs(node):
            if node:
                dfs(node.left)
                inorder.append(node.val)
                dfs(node.right)
        dfs(root)
        print 'inorder: ', inorder
        
        return inorder == inorder[::-1]
        