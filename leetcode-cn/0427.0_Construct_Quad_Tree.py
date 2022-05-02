'''
DFS

执行用时：200 ms, 在所有 Python3 提交中击败了87.59% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了33.58% 的用户
通过测试用例：22 / 22
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
            return len(set(grid[i][j] for i in range(t, b + 1) for j in range(l, r + 1))) == 1
            
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




'''
DFS

执行用时：192 ms, 在所有 Python3 提交中击败了96.35% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了35.77% 的用户
通过测试用例：22 / 22
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



