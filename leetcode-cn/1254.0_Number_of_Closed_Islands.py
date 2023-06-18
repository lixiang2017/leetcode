'''
执行用时：72 ms, 在所有 Python3 提交中击败了42.35% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了7.99% 的用户
通过测试用例：47 / 47
'''
class UF:
    def __init__(self, m, n):
        total = m * n
        self.m = m
        self.n = n
        self.fa = list(range(total))
        self.is_closed = [True] * total
    
    def find(self, x):
        if x == self.fa[x]:
            return x 
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.fa[fx] = fy
            self.is_closed[fy] &= self.is_closed[fx]

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UF(m, n)
        for i in range(m):
            for j in [0, n - 1]:
                if grid[i][j] == 0:
                    uf.is_closed[i * n + j] = False 
        for i in [0, m - 1]:
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    uf.is_closed[i * n + j] = False 
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    continue 
                if grid[i - 1][j] == 0:
                    uf.union(i * n + j, (i - 1) * n + j)
                
                if grid[i][j - 1] == 0:
                    uf.union(i * n + j, (i * n + j - 1))

        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                idx = i * n + j
                if grid[i][j] == 0 and uf.find(idx) == idx and uf.is_closed[idx]:
                    ans += 1
        return ans 


