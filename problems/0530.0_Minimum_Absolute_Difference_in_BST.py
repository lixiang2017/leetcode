'''
Runtime: 99 ms, faster than 5.10% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 18.5 MB, less than 69.94% of Python3 online submissions for Minimum Absolute Difference in BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        return min(b - a for a, b in pairwise(inorder(root)))

