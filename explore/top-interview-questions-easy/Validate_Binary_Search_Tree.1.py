'''
inorder tree traversal

You are here!
Your runtime beats 27.59 % of python submissions.
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
        tree = []
        def dfs(node):
            if node:
                dfs(node.left)
                tree.append(node.val)
                dfs(node.right)
            
        dfs(root)
        print 'tree: ', tree
        for i in xrange(len(tree) - 1):
            if tree[i + 1] > tree[i]:
                continue
            else:
                return False
            
        return True