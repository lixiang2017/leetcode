'''
union find

Runtime: 2044 ms, faster than 24.59% of Python3 online submissions for Similar String Groups.
Memory Usage: 16.6 MB, less than 10.16% of Python3 online submissions for Similar String Groups.
'''
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        # union find
        p = list(range(n))
        set_count = n
        def find(x):
            if x == p[x]:
                return x
            p[x] = find(p[x])
            return p[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py
                nonlocal set_count
                set_count -= 1
        
        def isSimilar(i, j):
            return sum(1 for a, b in zip(strs[i], strs[j]) if a != b) <= 2
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isSimilar(i, j):
                    union(i, j)
        return set_count
