'''
DFS

Runtime: 4461 ms, faster than 45.45% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
Memory Usage: 150.4 MB, less than 9.09% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
'''
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        ans = 0
        g = [[] for _ in range(len(roads) + 1)]
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(x, fa):
            size = 1
            for y in g[x]:
                if y != fa:
                    size += dfs(y, x)
            if x:
                nonlocal ans
                ans += (size + seats - 1) // seats
            return size 
        
        dfs(0, -1)
        return ans

'''
DFS

Runtime: 2081 ms, faster than 53.27% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
Memory Usage: 160.1 MB, less than 70.09% of Python3 online submissions for Minimum Fuel Cost to Report to the Capital.
'''
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        # topo, people count at each node
        cnt = [0] * n
        # graph
        g = defaultdict(list)
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)
        
        # people cnt for each node
        def people_cnt(node, parent):
            if 1 == len(g[node]) and node != 0:
                cnt[node] = 1
                return 1
            c = 1
            for child in g[node]:
                if child != parent:
                    c += people_cnt(child, node)
            cnt[node] = c
            return c 
        
        people_cnt(0, -1)
        
        ans = 0
        for node in range(1, n):
            ans += (cnt[node] + seats - 1) // seats
        return ans

