'''
BFS

Runtime: 1016 ms, faster than 9.36% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.6 MB, less than 48.51% of Python3 online submissions for Network Delay Time.
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = [float('inf')] * n 
        time[k - 1] = 0
        # (node - 1, time)
        q = deque([(k - 1, 0)])
        # graph
        g = defaultdict(dict)
        for u, v, w in times:
            g[u - 1][v - 1] = w
        while q:
            u, t = q.popleft()
            for v, w in g[u].items():
                if w + t < time[v]:
                    time[v] = w + t
                    q.append((v, time[v]))
                
        t = max(time)
        return t if t != float('inf') else -1
