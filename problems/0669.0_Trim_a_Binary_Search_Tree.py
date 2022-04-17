'''
recursion

Runtime: 52 ms, faster than 88.11% of Python3 online submissions for Trim a Binary Search Tree.
Memory Usage: 18.1 MB, less than 48.91% of Python3 online submissions for Trim a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        else:
            return self.trimBST(root.left, low, high)
        
        
