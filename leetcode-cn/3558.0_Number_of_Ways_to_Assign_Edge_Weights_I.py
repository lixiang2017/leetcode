class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        M = 1_000_000_007
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(x: int, fa: int) -> int:
            d = 0
            for y in g[x]:
                if y != fa:
                    d = max(d, dfs(y, x) + 1)
            return d

        depth = dfs(1, 0)
        return pow(2, depth - 1, M)