'''
change pointers on the fly
T: O(N)
S: O(H), for the recursion stack

Runtime: 34 ms, faster than 80.80% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 14 MB, less than 13.79% of Python3 online submissions for Increasing Order Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        hair = cur = TreeNode()
        
        def inorder(node):
            nonlocal cur
            if not node:
                return 
            inorder(node.left)
            node.left = None
            # set right child of cur node
            cur.right = node
            # move to next one
            cur = node
            inorder(node.right)
        
        inorder(root)
        return hair.right
    
