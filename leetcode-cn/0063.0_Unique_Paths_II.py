'''
DP, T: O(MN), S: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了92.73% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了86.69% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m, n = len(grid), len(grid[0]) if grid else 0
        if 0 == m or 0 == n or 1 == grid[0][0] or 1 == grid[-1][-1]:
            return 0
        # first row
        i, j = 0, 1
        while j < n and grid[0][j] == 0:
            grid[0][j] = 1
            j += 1
        while j < n:
            grid[0][j] = 0
            j += 1        
        # first column
        while i < m and grid[i][0] == 0:
            grid[i][0] = 1
            i += 1
        while i < m:
            grid[i][0] = 0
            i += 1        
        for i in range(1, m):
            for j in range(1, n):
                if 0 == grid[i][j]:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                else:
                    grid[i][j] = 0

        return grid[-1][-1] 

'''
DFS + cache

执行用时：40 ms, 在所有 Python3 提交中击败了55.27% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.06% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m, n = len(g), len(g[0]) if g else 0

        @cache
        def path(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or 1 == g[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return path(i - 1, j) + path(i, j - 1)
        
        return path(m - 1, n - 1)


'''
DFS + lru_cache

执行用时：40 ms, 在所有 Python3 提交中击败了55.27% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.06% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m, n = len(g), len(g[0]) if g else 0

        @lru_cache
        def path(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or 1 == g[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return path(i - 1, j) + path(i, j - 1)
        
        return path(m - 1, n - 1)


'''
DFS + memoization

执行用时：40 ms, 在所有 Python3 提交中击败了55.27% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了21.33% 的用户
通过测试用例：41 / 41ss
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m, n = len(g), len(g[0]) if g else 0
        p = [[-1] * n for _ in range(m)]

        def path(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if p[i][j] != -1:
                return p[i][j]
            if 1 == g[i][j]:
                p[i][j] = 0
                return 0
            if i == 0 and j == 0:
                p[i][j] = 1
                return 1
            p[i][j] = path(i - 1, j) + path(i, j - 1)
            return p[i][j]
        
        return path(m - 1, n - 1)





