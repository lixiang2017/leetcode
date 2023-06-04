'''
Runtime: 201 ms, faster than 42.68% of Python3 online submissions for Number of Provinces.
Memory Usage: 16.6 MB, less than 57.01% of Python3 online submissions for Number of Provinces.
'''
class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n))
        self.set_count = n
    
    def find(self, x):
        if self.fa[x] == x:
            return x 
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.fa[px] = py
            self.set_count -= 1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.set_count
        
        