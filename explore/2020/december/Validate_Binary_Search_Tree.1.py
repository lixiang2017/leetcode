'''
Submission Result: Wrong Answer 
Input: [1,1]
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
    def __init__(self):
        self.in_order = []
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.dfs(root)
        return self.in_order == sorted(self.in_order)
    
    def dfs(self, node):
        if not node:
            return 
        if node.left:
            self.dfs(node.left)
        self.in_order.append(node.val)
        if node.right:
            self.dfs(node.right)
            