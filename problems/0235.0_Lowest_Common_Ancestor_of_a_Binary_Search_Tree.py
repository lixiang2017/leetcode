'''
Runtime: 105 ms, faster than 69.73% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.7 MB, less than 97.27% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
        
        
'''
Runtime: 147 ms, faster than 24.84% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.7 MB, less than 97.27% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
        return root 
          