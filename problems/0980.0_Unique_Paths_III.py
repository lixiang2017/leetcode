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


'''
DFS + mask

Runtime: 86 ms, faster than 70.84% of Python3 online submissions for Unique Paths III.
Memory Usage: 13.9 MB, less than 93.68% of Python3 online submissions for Unique Paths III.
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        si = sj = ei = ej = 0
        once_mask = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x != -1:
                    once_mask |= (1 << (i * n + j))
                if x == 1:
                    si, sj = i, j
                elif x == 2:
                    ei, ej = i, j 
        
        ans = 0
        def dfs(i, j, mask):
            if i == ei and j == ej and mask == once_mask:
                nonlocal ans 
                ans += 1
                return 
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != -1 and mask & (1 << (ni * n + nj)) == 0:
                    mask2 = mask | (1 << (ni * n + nj))
                    dfs(ni, nj, mask2)
        
        dfs(si, sj, 1 << (si * n + sj))
        return ans

'''
backtrack

Runtime: 60 ms, faster than 88.41% of Python3 online submissions for Unique Paths III.
Memory Usage: 13.9 MB, less than 93.56% of Python3 online submissions for Unique Paths III.
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        si = sj = zero = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    zero += 1
                elif x == 1:
                    si, sj = i, j

        ans = 0
        def backtrack(i, j, zero):
            if grid[i][j] == 2:
                nonlocal ans
                ans += int(zero == -1)
                return 
            zero -= 1
            grid[i][j] = -1
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != -1:
                    backtrack(ni, nj, zero)
            grid[i][j] = 0
            zero += 1
        
        backtrack(si, sj, zero)
        return ans
