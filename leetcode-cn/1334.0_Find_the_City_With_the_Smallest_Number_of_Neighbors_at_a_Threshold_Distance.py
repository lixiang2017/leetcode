'''
Dijkstra

执行用时：464 ms, 在所有 Python3 提交中击败了74.67% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了74.02% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # graph
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        # 
        for i in range(n):
            # source, start: i
            used = [False] * n
            for _ in range(n):
                # to find nearest unused node
                idx = -1
                for j, use in enumerate(used):
                    if not use and (idx == -1 or dist[i][j] < dist[i][idx]):
                        idx = j
                used[idx] = True
                # for child, cost in g[idx].items():
                for child, cost in enumerate(dist[idx]):
                    # i -dist[i][idx]-> idx -(cost)-> child
                    if dist[i][idx] + cost < dist[i][child]:
                        dist[i][child] = dist[i][idx] + cost
                        dist[child][i] = min(dist[child][i], dist[i][child])

        c = float('inf')
        ans = 0
        for i, ds in enumerate(dist):
            cnt = sum(d <= distanceThreshold for d in ds)
            if cnt <= c:
                c = cnt
                ans = i
        return ans
