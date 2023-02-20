'''
BFS

Runtime: 37 ms, faster than 52.01% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.2 MB, less than 48.21% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        level = 1
        while q:
            nodes, vals = [], []
            for node in q:
                vals.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if level & 1:
                ans.append(vals)
            else:
                ans.append(reversed(vals))
            q = nodes
            level += 1
        return ans 
