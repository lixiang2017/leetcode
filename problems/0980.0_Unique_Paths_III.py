'''
backtracking

Runtime: 56 ms, faster than 83.91% of Python3 online submissions for Unique Paths III.
Memory Usage: 14.3 MB, less than 46.77% of Python3 online submissions for Unique Paths III.
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        def dfs(grid, i, j, zero):
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                if zero == -1:
                    return 1
                else:
                    return 0
            zero -= 1
            grid[i][j] = -1
            a = dfs(grid, i - 1, j, zero)
            b = dfs(grid, i + 1, j, zero)
            c = dfs(grid, i, j - 1, zero)
            d = dfs(grid, i, j + 1, zero)
            zero += 1
            grid[i][j] = 0
            return a + b + c + d
        
        sx = sy = zero = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    zero += 1
                elif grid[i][j] == 1:
                    sx, sy = i, j
        
        return dfs(grid, sx, sy, zero)
