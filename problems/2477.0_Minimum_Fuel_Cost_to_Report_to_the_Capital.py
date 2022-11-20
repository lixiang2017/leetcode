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
