'''
把周围的都先算出来，最后算自己
DFS + memoization
matrix[ni][nj] < matrix[i][j]

执行用时：364 ms, 在所有 Python3 提交中击败了12.68% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了65.82% 的用户
通过测试用例：138 / 138
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        path = [[1] * n for _ in range(m)]
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if path[i][j] != 1:
                return path[i][j]
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                    path[i][j] = max(path[i][j], dfs(ni, nj) + 1)
            return path[i][j]
            
        for i in range(m):
            for j in range(n):
                path[i][j] = dfs(i, j)
        return max(chain(*path))


'''
matrix[ni][nj] > matrix[i][j]

执行用时：320 ms, 在所有 Python3 提交中击败了23.43% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了62.79% 的用户
通过测试用例：138 / 138
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        path = [[1] * n for _ in range(m)]
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if path[i][j] != 1:
                return path[i][j]
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    path[i][j] = max(path[i][j], dfs(ni, nj) + 1)
            
            return path[i][j]
            
        for i in range(m):
            for j in range(n):
                path[i][j] = dfs(i, j)
        return max(chain(*path))


