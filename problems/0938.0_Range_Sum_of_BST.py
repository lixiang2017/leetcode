'''
Approach: DFS

Success
Details 
Runtime: 312 ms, faster than 39.13% of Python online submissions for Range Sum of BST.
Memory Usage: 29.7 MB, less than 61.85% of Python online submissions for Range Sum of BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        
        range_sum = 0
        if L <= root.val <= R:
            range_sum += root.val
        if root.left:
            range_sum += self.rangeSumBST(root.left, L, R)
        if root.right:
            range_sum += self.rangeSumBST(root.right, L, R)
        
        return range_sum
