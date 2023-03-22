'''
Union Find

Runtime: 1555 ms, faster than 97.65% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
Memory Usage: 58.7 MB, less than 96.31% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
'''
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        fa = list(range(n))
        score = [10005] * n
        
        def find(x):
            if x == fa[x]:
                return x
            fa[x] = find(fa[x])
            return fa[x]
        
        def union(x, y, dist):
            fx, fy = find(x), find(y)
            if fx == fy:
                score[fx] = min(score[fx], dist)
                return
            fa[fx] = fy
            score[fy] = min(score[fy], score[fx], dist)
        
        for a, b, dist in roads:
            union(a -  1, b - 1, dist)
        
        f1 = find(0)
        return score[f1]
