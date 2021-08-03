'''
Dijkstra(Greedy)

执行用时：68 ms, 在所有 Python3 提交中击败了93.74% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了79.04% 的用户
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph
        g = [[float('inf')] * n for _ in range(n)]
        # used 
        used = [False] * n
        # dist
        dist = [float('inf')] * n
        dist[k - 1] = 0  # source
        # set graph
        for u, v, w in times:
            g[u - 1][v - 1] = w
        
        for _ in range(n):
            # to find the nearest unused node x
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for v, w in enumerate(g[x]):
                dist[v] = min(dist[v], dist[x] + w)

        ans = max(dist)
        return ans if ans < float('inf') else -1        
