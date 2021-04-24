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



'''
approach: Tarjan's Algorithm
Time: O(V + E)
Space: O(V)

You are here!
Your runtime beats 98.16 % of python3 submissions.
You are here!
Your memory usage beats 95.02 % of python3 submissions.
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # node is index, neighbors are in the list
        graph = [[] for i in range(n)]
        
        # build graph
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # min_discovery_time of nodes at respective indices from start node
        # 1. default to max which is the depth of continuous graph
        lows = [n] * n
        
        # critical edges 
        critical = []
        
        # args: node, node discovery_time in dfs, parent of this node
        def dfs(node, discovery_time, parent):
            
            # if the low is not yet discovered for this node
            if lows[node] == n:
                
                # 2. default it to the depth or discovery time of this node
                lows[node] = discovery_time
                
                # iterate over neighbors
                for neighbor in graph[node]:
                    
                    # all neighbors except parent
                    if neighbor != parent:
                        
                        expected_discovery_time_of_child = discovery_time + 1
                        actual_discovery_time_of_child = dfs(neighbor, expected_discovery_time_of_child, node)
                        
                        # nothing wrong - parent got what was expected => no back path
                        # this step is skipped if there is a back path
                        if actual_discovery_time_of_child >= expected_discovery_time_of_child:
                            critical.append((node, neighbor))
                        
                        # low will be equal to discovery time of this node or discovery time of child
                        # whichever one is minm
                        # if its discovery time of child - then there is a backpath
                        lows[node] = min(lows[node], actual_discovery_time_of_child)
                        

            # return low of this node discovered previously or during this call 
            return lows[node]
        
        dfs(n-1, 0, -1)
        
        return critical   


'''
approach: Tarjan's Algorithm
Time: O(V + E)
Space: O(V)

You are here!
Your runtime beats 82.51 % of python3 submissions.
You are here!
Your memory usage beats 78.94 % of python3 submissions.
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # build graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        res = []
        dfn = [-1] * n
        low = [-1] * n
        # tarjan's algorithm
        def tarjan(node, parent, depth):
            dfn[node] = depth
            low[node] = depth
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if dfn[neighbor] == -1:
                    tarjan(neighbor, node, depth + 1)
                    if dfn[node] < low[neighbor]:
                        res.append([node, neighbor])
                low[node] = min(low[node], low[neighbor])
                
        tarjan(0, -1, 0)
        return res
        