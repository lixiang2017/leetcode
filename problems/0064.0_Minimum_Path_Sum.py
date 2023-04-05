'''
DP

Runtime: 99 ms, faster than 69.52% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.7 MB, less than 80.67% of Python3 online submissions for Minimum Path Sum.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
