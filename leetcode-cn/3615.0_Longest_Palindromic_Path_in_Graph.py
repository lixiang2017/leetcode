class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        odd = sum(c % 2 for c in Counter(label).values())
        theoretical_max = n - max(odd - 1, 0)
        if len(edges) == n * (n - 1) // 2:
            return theoretical_max

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
   
        @cache
        def dfs(x: int, y: int, vis: int) -> int:
            res = 0
            for v in g[x]:
                if vis >> v & 1:
                    continue
                for w in g[y]:
                    if vis >> w & 1 == 0 and v != w and label[w] == label[v]:
                        tv, tw = v, w
                        if tv > tw:
                            tv, tw = tw, tv
                        res = max(res, dfs(tv, tw, vis | 1 << v | 1 << w) + 2)
            return res
        
        ans = 0
        for x, to in enumerate(g):
            ans = max(ans, dfs(x, x, 1 << x) + 1)
            if ans == theoretical_max:
                return ans
            for y in to:
                if x < y and label[x] == label[y]:
                    ans = max(ans, dfs(x, y, 1 << x | 1 << y) + 2)
                    if ans == theoretical_max:
                        return ans
        return ans