'''
Runtime: 3852 ms, faster than 19.87% of Python3 online submissions for Critical Connections in a Network.
Memory Usage: 73.7 MB, less than 74.69% of Python3 online submissions for Critical Connections in a Network.
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        
        ans = []
        dfn, low = [-1] * n, [-1] * n
        # tarjan's algorithm
        def tarjan(node, parent, depth):
            dfn[node] = depth 
            low[node] = depth 
            for neigh in g[node]:
                if neigh == parent:
                    continue
                if dfn[neigh] == -1:
                    tarjan(neigh, node, depth + 1)
                    if dfn[node] < low[neigh]:
                        ans.append([node, neigh])
                low[node] = min(low[node], low[neigh])
        
        tarjan(0, -1, 0)
        return ans 
        