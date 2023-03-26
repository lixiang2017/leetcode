'''
union find

Runtime: 2070 ms, faster than 88.26% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
Memory Usage: 74.8 MB, less than 76.87% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
'''
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        fa = list(range(n))
        set_cnt = [1] * n
        
        def find(x: int) -> int:
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]
    
        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if fx == fy:
                return 
            fa[fx] = fy
            set_cnt[fy] += set_cnt[fx]
        
        for a, b in edges:
            union(a, b)
            
        roots = [i for i in range(n) if i == fa[i]]
        ans = 0
        total = n
        for r in roots:
            total -= set_cnt[r]
            ans += set_cnt[r] * total
        return ans 


'''
DFS

Runtime: 2183 ms, faster than 65.28% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
Memory Usage: 114.3 MB, less than 7.29% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
'''
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            
        all_nodes = set(range(n))
        seen = set()

        def dfs(x, parent):
            for child in g[x]:
                if child not in seen and child != parent:
                    seen.add(child)
                    all_nodes.remove(child)
                    dfs(child, x)
        
        total = n
        ans = 0
        while all_nodes:
            x = all_nodes.pop()
            seen = {x}
            dfs(x, -1)
            total -= len(seen)
            ans += len(seen) * total
        return ans 
        

'''
BFS

Runtime: 2184 ms, faster than 64.24% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
Memory Usage: 75.5 MB, less than 62.50% of Python3 online submissions for Count Unreachable Pairs of Nodes in an Undirected Graph.
'''
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            
        all_nodes = set(range(n))
        seen = set()

        def bfs(x):
            q = deque([x])
            while q:
                node = q.popleft()
                for child in g[node]:
                    if child not in seen:
                        q.append(child)
                        seen.add(child)
                        all_nodes.remove(child)
        
        total = n
        ans = 0
        while all_nodes:
            x = all_nodes.pop()
            seen = {x}
            bfs(x)
            total -= len(seen)
            ans += len(seen) * total
        return ans 
        

