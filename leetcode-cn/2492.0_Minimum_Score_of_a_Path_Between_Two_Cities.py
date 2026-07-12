class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            x = self.p[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UF(n + 1)
        for a, b, d in roads:
            uf.union(a, b)
        ans = inf
        p1 = uf.find(1)
        for a, b, d in roads:
            pa = uf.find(a)
            if p1 == pa:
                ans = min(ans, d)

        return ans


"""UF, min"""


class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.min = [inf] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y, dist):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
        self.min[py] = min(self.min[px], self.min[py], dist)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UF(n)
        for a, b, dist in roads:
            uf.union(a - 1, b - 1, dist)
        p0 = uf.find(0)
        return uf.min[p0]


"""DFS"""


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b, dist in roads:
            g[a - 1].append((b - 1, dist))
            g[b - 1].append((a - 1, dist))

        ans = inf
        vis = [False] * n

        def dfs(x):
            nonlocal ans
            vis[x] = True
            for y, d in g[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)

        dfs(0)
        return ans
