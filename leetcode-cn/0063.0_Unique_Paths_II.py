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
