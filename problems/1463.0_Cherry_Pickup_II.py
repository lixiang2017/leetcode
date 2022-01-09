'''
DP

Runtime: 2132 ms, faster than 26.78% of Python3 online submissions for Cherry Pickup II.
Memory Usage: 18.1 MB, less than 82.38% of Python3 online submissions for Cherry Pickup II.
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [ [[-1] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]
        
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    best = -1
                    for dj1 in [j - 1, j, j + 1]:
                        for dj2 in [k - 1, k, k + 1]:
                            if 0 <= dj1 < n and 0 <= dj2 < n:
                                best = max(best, dp[i - 1][dj1][dj2])
                    if best == -1:
                        dp[i][j][k] = -1
                    else:
                        dp[i][j][k] = best + grid[i][j] + (j != k) * grid[i][k]
        
        ans = 0
        for j in range(n):
            for k in range(n):
                ans = max(ans, dp[m -1][j][k])
        
        return ans
