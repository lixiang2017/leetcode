'''
approach: Tarjan's Algorithm
Time: O(V + E)
Space: O(V)

You are here!
Your memory usage beats 46.40 % of python3 submissions.
'''


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        def dfs(prev, curr, depth):
            if depths[curr] > -1:
                return depths[curr]
            
            depths[curr] = depth
            min_back_depth = n
            for v in graph[curr]:
                if v == prev:
                    continue
                back = dfs(curr, v, depth + 1)
                if back <= depth:
                    connections.remove((min(curr, v), max(curr, v)))
                min_back_depth = min(min_back_depth, back)
            return min_back_depth
            
        
        # build graph
        graph = [[] for _ in range(n)]
        for s, t in connections:
            graph[s].append(t)
            graph[t].append(s)
        
        depths = [-1] * n
        connections = set(tuple(sorted(c)) for c in connections)
        dfs(0, 0, 0)
        return [list(c) for c in connections]
        