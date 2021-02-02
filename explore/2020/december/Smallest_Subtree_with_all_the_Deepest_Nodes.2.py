'''
You are here!
Your runtime beats 29.57 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        self.max_depth = 0
        
        def postorder(root, depth = 0):
            if not root:
                return depth
            
            l = postorder(root.left, depth + 1)
            r = postorder(root.right, depth + 1)
            self.max_depth = max(self.max_depth, l, r)
            if l == r == self.max_depth:
                self.ans = root
            return max(l, r)
        
        postorder(root)
        return self.ans
    