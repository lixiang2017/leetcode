'''
Submission Result: Wrong Answer 
Input: [5,4,1,null,1,null,4,2,null,2,null]
Output: true
Expected: false
Stdout: inorder:  ['NULL', 4, 2, 1, 'NULL', 5, 'NULL', 1, 2, 4, 'NULL']
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
            if node.left:
                dfs(node.left)
            # else:                 # Wrong Answer
            elif node.right:        # still Wrong Answer
                inorder.append('NULL')
                
            if node:
                inorder.append(node.val)
            
            if node.right:
                dfs(node.right)
            # else:
            elif node.left:
                inorder.append('NULL')
                
        dfs(root)
        print 'inorder: ', inorder
        
        return inorder == inorder[::-1]
        
        
        