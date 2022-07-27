'''
DFS

Runtime: 114 ms, faster than 46.58% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 26.3 MB, less than 30.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        '''
        if left:
            print('l: ', left.val, 'root: ', root.val)
        if right:
            print('r: ', right.val, 'root: ', root.val)
        '''
        if left and right:
            return root 
        return left or right 
    
    
'''
bottom-up

Your input
[3,5,1,6,2,0,8,null,null,7,4]
7
8
stdout
l:  7 root:  2
r:  7 root:  5
r:  8 root:  1
l:  7 root:  3
r:  8 root:  3

Output
3
Expected
3
'''
