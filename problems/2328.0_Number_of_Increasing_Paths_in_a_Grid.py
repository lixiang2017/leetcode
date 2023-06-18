'''
Runtime: 2485 ms, faster than 43.21% of Python3 online submissions for Number of Increasing Paths in a Grid.
Memory Usage: 75.6 MB, less than 54.86% of Python3 online submissions for Number of Increasing Paths in a Grid.
'''
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        ans = 0
        cnt = [[1] * n for _ in range(m)]
        pairs = [(-grid[i][j], i, j) for i in range(m) for j in range(n)]
        pairs.sort()
        for x, i, j in pairs:
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > -x:
                    cnt[i][j] += cnt[ni][nj]
            ans += cnt[i][j]
            ans %= MOD 
        return ans 
