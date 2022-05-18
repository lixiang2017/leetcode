'''
BFS

Runtime: 442 ms, faster than 10.70% of Python3 online submissions for Deepest Leaves Sum.
Memory Usage: 17.7 MB, less than 66.46% of Python3 online submissions for Deepest Leaves Sum.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        last_sum = 0 
        q = [root]
        while q:
            last_sum = 0
            next_q = []
            for node in q:
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
                last_sum += node.val
            q = next_q
        return last_sum
