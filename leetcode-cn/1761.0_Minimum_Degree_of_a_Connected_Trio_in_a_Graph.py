'''
DFS

时间 3336ms, 击败 65.38%使用 Python3 的用户
内存 29.98MB, 击败 96.15%使用 Python3 的用户
'''
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        if 2 == n:
            return -1
        if len(edges) == n * (n - 1) // 2:
            return (n - 3) * 3

        ans = n * 3
        degree = Counter()
        graph = defaultdict(set)
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
            graph[a].add(b)
            graph[b].add(a)
        
        def dfs(start, cur, prev, step):
            nonlocal ans
            if degree[start] - 2 > ans or degree[cur] - 2 > ans or degree[prev] - 2 > ans:
                return 
            if step == 3:
                if start in graph[cur]:
                    ans = min(ans, degree[cur] + degree[start] + degree[prev] - 6)
                return 
            for nxt in graph[cur]:
                if nxt != prev and step <= 2:
                    dfs(start, nxt, cur, step + 1)

        for node in range(1, n + 1):
            if degree[node] - 2 > ans:
                continue
            dfs(node, node, -1, 1)
        
        return -1 if ans == n * 3 else ans 
