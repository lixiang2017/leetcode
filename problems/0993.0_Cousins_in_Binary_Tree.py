'''
BFS

Runtime: 36 ms, faster than 52.28% of Python3 online submissions for Cousins in Binary Tree.
Memory Usage: 14.2 MB, less than 90.31% of Python3 online submissions for Cousins in Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        xy_parent, xy_depth = dict(), dict()
        q = deque([(root, 0)])
        while q:
            node, d = q.popleft()
            for child in (node.left, node.right):
                if child:
                    if child.val in (x, y):
                        xy_parent[child.val] = node.val
                        xy_depth[child.val] = d + 1
                    q.append((child, d + 1))   
            if len(xy_parent) >= 2:
                break
            
        return xy_parent[x] != xy_parent[y] and xy_depth[x] == xy_depth[y]
