"""UF"""


class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.edge_count = [0] * n
        self.node_count = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
            self.edge_count[py] += self.edge_count[px]
            self.node_count[py] += self.node_count[px]
        self.edge_count[py] += 1


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            uf.union(a, b)
        roots = {uf.find(i) for i in range(n)}
        ans = 0
        for r in roots:
            ec, nc = uf.edge_count[r], uf.node_count[r]
            if nc * (nc - 1) // 2 == ec:
                ans += 1
        return ans


"""DFS"""


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        vis = [False] * n

        def dfs(i):
            nonlocal v, e
            vis[i] = True
            v += 1

            for y in g[i]:
                e += 1
                if not vis[y]:
                    dfs(y)

        ans = 0
        for i, b in enumerate(vis):
            if not b:
                v = e = 0
                dfs(i)
                ans += v * (v - 1) == e
        return ans


"""BFS"""


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        vis = [False] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                v = e = 0
                # bfs(i)
                q = deque([i])
                vis[i] = True
                while q:
                    x = q.popleft()
                    v += 1
                    e += len(g[x])
                    for y in g[x]:
                        if not vis[y]:
                            vis[y] = True
                            q.append(y)

                ans += v * (v - 1) == e
        return ans
