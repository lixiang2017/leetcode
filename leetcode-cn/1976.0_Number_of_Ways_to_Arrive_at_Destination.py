'''
Dijkstra + heap

执行用时：68 ms, 在所有 Python3 提交中击败了86.71% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了73.88% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = int(1e9 + 7)
        # graph
        g = defaultdict(dict)
        for u, v, t in roads:
            g[u][v] = t
            g[v][u] = t
        # distance from 0-th node to others
        dist = [float('inf')] * n
        dist[0] = 0
        # path count for every node
        pcnt = [0] * n
        pcnt[0] = 1
        #heap (cost, node)
        h = [(0, 0)]
        while h:
            cost, node = heappop(h)
            for child, time in g[node].items():
                if cost + time < dist[child]:
                    dist[child] = cost + time
                    pcnt[child] = pcnt[node]
                    heappush(h, (dist[child], child))
                elif cost + time == dist[child]:
                    pcnt[child] += pcnt[node]
                pcnt[child] %= MOD
        return pcnt[n - 1]

'''
Dijkstra + heap

执行用时：76 ms, 在所有 Python3 提交中击败了66.89% 的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了33.33% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # graph
        g = defaultdict(list)
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))
        # distance from 0-th node to others
        dist = [float('inf')] * n
        dist[0] = 0
        # path count for every node
        pcnt = [0] * n
        pcnt[0] = 1
        #heap (cost, node)
        h = [(0, 0)]
        while h:
            cost, node = heappop(h)
            for child, time in g[node]:
                if cost + time < dist[child]:
                    dist[child] = cost + time
                    pcnt[child] = pcnt[node]
                    heappush(h, (dist[child], child))
                elif cost + time == dist[child]:
                    pcnt[child] += pcnt[node]
                pcnt[child] %= MOD
        return pcnt[n - 1]



'''
Dijkstra + visited

执行用时：92 ms, 在所有 Python3 提交中击败了42.57% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了56.08% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # graph
        g = defaultdict(list)
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))
        # distance from 0-th node to others
        dist = [float('inf')] * n
        dist[0] = 0
        # path count for every node
        pcnt = [0] * n
        pcnt[0] = 1    
        visited = [False] * n 

        for _ in range(n):
            # to find nearest idx
            idx = -1
            for i, vis in enumerate(visited):
                if not vis and (idx == -1 or dist[i] < dist[idx]):
                    idx = i 
            visited[idx] = True
            for child, t in g[idx]:
                if dist[idx] + t < dist[child]:
                    dist[child] = dist[idx] + t
                    pcnt[child] = pcnt[idx]
                elif dist[idx] + t == dist[child]:
                    pcnt[child] += pcnt[idx]
                pcnt[child] %= MOD
        
        return pcnt[n - 1]

