class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        max_cost = -1
        for u, v, cost in edges:
            if online[u] and online[v]:
                g[u].append((v, cost))
                if u == 0:
                    max_cost = max(max_cost, cost)

        def check(lower: int):
            @cache
            def dfs(x: int) -> int:
                if x == n - 1:
                    return 0
                res = inf
                for y, cost in g[x]:
                    if cost >= lower:
                        res = min(res, dfs(y) + cost)
                return res

            return dfs(0) <= k

        left, right = -1, max_cost + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
