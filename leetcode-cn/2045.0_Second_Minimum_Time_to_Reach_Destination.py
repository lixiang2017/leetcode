'''
BFS
计算时间：走一步，再走一步

执行用时：552 ms, 在所有 Python3 提交中击败了64.37% 的用户
内存消耗：21.8 MB, 在所有 Python3 提交中击败了63.36% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # graph
        graph = [[] for _ in range(n + 1)]
        for e in edges:
            u, v = e 
            graph[u].append(v)
            graph[v].append(u)
        # dist[i][0] shortest path from 1 to i
        # dist[i][1] second shortest path from 1 to i
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        # (node, step)
        q = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            node, step = q.popleft()
            for nxt in graph[node]:
                d = step + 1
                if d < dist[nxt][0]:
                    dist[nxt][0] = d 
                    q.append((nxt, d))
                elif dist[nxt][0] < d < dist[nxt][1]:
                    dist[nxt][1] = d 
                    q.append((nxt, d))

        ans = 0
        for _ in range(dist[n][1]):
            if ans % (2 * change) >= change:
                # wait time
                ans += 2 * change - ans % (2 * change)
            ans += time 
        return ans 
