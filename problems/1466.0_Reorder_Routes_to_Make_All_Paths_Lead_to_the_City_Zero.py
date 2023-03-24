'''
BFS

Runtime: 1260 ms, faster than 64.29% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
Memory Usage: 43.7 MB, less than 77.43% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()
        g = defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
            edges.add((a, b))
        ans = 0
        q = deque([0])
        seen = {0}
        while q:
            node = q.popleft()
            for child in g[node]:
                if child not in seen:
                    seen.add(child)
                    q.append(child)
                    if (node, child) in edges:
                        ans += 1
        return ans 


'''
DFS

Runtime: 1250 ms, faster than 67.43% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
Memory Usage: 70.7 MB, less than 50.57% of Python3 online submissions for Reorder Routes to Make All Paths Lead to the City Zero.
'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()
        g = defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
            edges.add((a, b))
        ans = 0
    
        def dfs(node, parent):
            for child in g[node]:
                if child != parent:
                    if (node, child) in edges:
                        nonlocal ans
                        ans += 1
                    dfs(child, node)
        dfs(0, -1)    
        return ans 

