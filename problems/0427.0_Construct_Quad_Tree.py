'''
DFS

Runtime: 106 ms, faster than 94.21% of Python3 online submissions for Construct Quad Tree.
Memory Usage: 14.8 MB, less than 41.32% of Python3 online submissions for Construct Quad Tree.
'''
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def all_same(t, b, l, r) -> bool:
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if grid[i][j] != grid[t][l]:
                        return False
            return True
            
        def dfs(top, bottom, left, right) -> Node:
            if bottom - top + 1 == 1 or all_same(top, bottom, left, right):
                return Node(grid[top][left], True, None, None, None, None)
        
            row_mid = (top + bottom) // 2
            col_mid = (left + right) // 2
            top_left = dfs(top, row_mid, left, col_mid)
            top_right = dfs(top, row_mid, col_mid + 1, right)
            bottom_left = dfs(row_mid + 1, bottom, left, col_mid)
            bottom_right = dfs(row_mid + 1, bottom, col_mid + 1, right)
            return Node(1, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(0, n - 1, 0, n - 1)


