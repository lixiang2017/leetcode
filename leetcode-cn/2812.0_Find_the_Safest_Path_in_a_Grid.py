"""
多源BFS计算dist
"""


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py

    def is_connected(self, x, y):
        px, py = self.find(x), self.find(y)
        return px == py


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if 1 == grid[0][0] or 1 == grid[-1][-1]:
            return 0
        n = len(grid)
        one = []
        zero = []
        dist = [[-1] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    one.append((i, j))
                    dist[i][j] = 0
                else:
                    zero.append((i, j))

        q = one
        while q:
            next_q = []
            for i, j in q:
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n and dist[x][y] < 0:
                        dist[x][y] = dist[i][j] + 1
                        next_q.append((x, y))
            q = next_q

        edges = []
        for i, j in zero:
            idx = i * n + j
            if i > 0 and 0 == grid[i - 1][j]:
                edges.append([idx, idx - n, min(dist[i][j], dist[i - 1][j])])
            if j > 0 and 0 == grid[i][j - 1]:
                edges.append([idx, idx - 1, min(dist[i][j], dist[i][j - 1])])

        edges.sort(key=lambda t: -t[2])

        uf = UF(n * n)
        for idx1, idx2, s in edges:
            uf.union(idx1, idx2)
            if uf.is_connected(0, n * n - 1):
                return s
        return 0
