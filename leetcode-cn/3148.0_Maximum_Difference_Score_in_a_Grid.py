class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ans = -inf
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                prev_min = inf
                if i > 0:
                    prev_min = min(prev_min, grid[i - 1][j])
                if j > 0:
                    prev_min = min(prev_min, grid[i][j - 1])
                ans = max(ans, grid[i][j] - prev_min)
                grid[i][j] = min(grid[i][j], prev_min)
        return ans 