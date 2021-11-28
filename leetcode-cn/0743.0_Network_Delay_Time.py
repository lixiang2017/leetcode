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

'''
Dijkstra + visited

执行用时：64 ms, 在所有 Python3 提交中击败了87.77% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了93.85% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph
        g = defaultdict(dict)
        for u, v, w in times:
            g[u - 1][v - 1] = w
        used = [False] * n 
        dist = [float('inf')] * n 
        dist[k - 1] = 0

        for _ in range(n):
            # to find nearest unused node
            x = -1
            for i, use in enumerate(used):
                if not use and (x == -1 or dist[i] < dist[x]):
                    x = i
            used[x] = True
            for child, w in g[x].items():
                dist[child] = min(dist[child], dist[x] + w)
    
        m = max(dist)
        return [m, -1][m == float('inf')]

'''
Dijkstra + heapq

执行用时：68 ms, 在所有 Python3 提交中击败了77.51% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了24.97% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph
        g = defaultdict(dict)
        for u, v, w in times:
            g[u - 1][v - 1] = w
        dist = [float('inf')] * n 
        dist[k - 1] = 0
        # heap (cost, node)
        h = [(0, k - 1)]
        while h:
            cost, node = heappop(h)
            for child, time in g[node].items():
                if cost + time < dist[child]:
                    dist[child] = cost + time
                    heappush(h, (dist[child], child))
                
        m = max(dist)
        return [m, -1][m == float('inf')]

