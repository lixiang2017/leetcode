'''
Runtime: 67 ms, faster than 20.36% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.4 MB, less than 26.00% of Python3 online submissions for Binary Tree Level Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = []
        q = [root] if root else []
        while q:
            vals = []
            next_q = []
            for node in q:
                vals.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            level.append(vals)
            q = next_q
        return level
        