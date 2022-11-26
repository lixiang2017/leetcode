'''
dijkstra + heap

执行用时：168 ms, 在所有 Python3 提交中击败了81.94% 的用户
内存消耗：20.3 MB, 在所有 Python3 提交中击败了93.06% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append([v, w + 1])
            g[v].append([u, w + 1])
        
        dist = self.dijkstra(g, 0)
        ans = sum(d <= maxMoves for d in dist)
        for u, v, w in edges:
            a = max(maxMoves - dist[u], 0)
            b = max(maxMoves - dist[v], 0)
            ans += min(w, a + b)
        return ans 
    
    def dijkstra(self, g: List[List[List[int]]], start: int) -> List[int]:
        dist = [inf] * len(g)
        dist[start] = 0
        h = [(0, start)]
        while h:
            d, x = heappop(h)
            if d > dist[x]:
                continue
            for y, w in g[x]:
                new_d = dist[x] + w
                if new_d < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))
        return dist 
