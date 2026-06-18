class UF:
    def __init__(self, n: int):
        self.fa = list(range(n))
        self.count = n
    
    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x]= self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.fa[fx] = fy
            self.count -= 1

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n == k:
            return 0
        uf = UF(n)
        edges.sort(key=lambda e: e[2])
        for u, v, w in edges:
            uf.union(u, v)
            if uf.count == k:
                return w