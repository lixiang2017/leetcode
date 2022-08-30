'''
DFS + hash set

Runtime: 560 ms, faster than 33.11% of Python3 online submissions for Number of Islands.
Memory Usage: 23.5 MB, less than 13.50% of Python3 online submissions for Number of Islands.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        seen = set()
        m, n = len(grid), len(grid[0])

        def spread(i, j):
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and ni * n + nj not in seen and '1' == grid[ni][nj]:
                    seen.add(ni * n + nj)
                    spread(ni, nj)        
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if '1' == x and i * n + j not in seen:
                    ans += 1
                    seen.add(i * n + j)
                    spread(i, j)
        return ans 
