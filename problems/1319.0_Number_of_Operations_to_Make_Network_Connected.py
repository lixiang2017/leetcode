'''
UF

Runtime: 468 ms, faster than 96.80% of Python3 online submissions for Number of Operations to Make Network Connected.
Memory Usage: 33.9 MB, less than 93.14% of Python3 online submissions for Number of Operations to Make Network Connected.
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n - 1:
            return -1
        # union find
        fa = list(range(n))
        set_count = n
        def find(x: int) -> int:
            if fa[x] == x:
                return x
            fa[x] = find(fa[x])
            return fa[x]
        
        def union(x: int, y: int):
            fx, fy = find(x), find(y)
            if fx != fy:
                nonlocal set_count
                set_count -= 1
                fa[fx] = fy
        
        for a, b in connections:
            union(a, b)
        return set_count - 1
        
