'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了49.32% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了55.48% 的用户
通过测试用例：154 / 154
'''
'''
1 1
1 2

1 2 2
2 3 2

111
111
111
'''

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        border = set()
        m, n = len(grid), len(grid[0])
        c = grid[row][col]
        seen = set()

        def findBorder(i: int, j: int):
            if (i, j) in seen:
                return 
            seen.add((i, j))
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == c:
                        # connect
                        if ni in [0, m - 1] or nj in [0, n - 1]:
                            border.add((ni, nj))
                        findBorder(ni, nj)
                    else:
                        # not connect
                        border.add((i, j))

        findBorder(row, col)
        for bi, bj in border:
            grid[bi][bj] = color 
        return grid
