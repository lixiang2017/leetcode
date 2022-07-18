'''
Union Find

Runtime: 268 ms, faster than 24.18% of Python3 online submissions for Max Area of Island.
Memory Usage: 14.1 MB, less than 92.54% of Python3 online submissions for Max Area of Island.
'''
class UF:
    def __init__(self, n):
        # parent
        self.p = list(range(n))
        self.size = [1] * n
        self.set_count = n
    
    def find(self, x):
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False 
        if self.size[px] > self.size[py]:
            px, py = py, px   # make sure self.size[px] <= self.size[py]
        self.p[px] = py
        self.size[py] += self.size[px]
        self.set_count -= 1
        return True

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        uf = UF(m * n)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if 0 == x:
                    continue
                max_area = max(1, max_area)
                idx = i * n + j 
                # right and down
                for ni, nj in [(i + 1, j), (i, j + 1)]:
                    if ni < m and nj < n and 1 == grid[ni][nj]:
                        uf.union(idx, ni * n + nj)
                        max_area = max(max_area, uf.size[uf.find(idx)])
        return max_area
    
