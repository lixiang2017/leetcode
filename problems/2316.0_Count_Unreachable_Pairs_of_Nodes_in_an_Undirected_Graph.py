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
