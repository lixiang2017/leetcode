'''
Runtime: 1015 ms, faster than 68.80% of Python3 online submissions for Possible Bipartition.
Memory Usage: 20 MB, less than 80.54% of Python3 online submissions for Possible Bipartition.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.set_count = n
    
    def find(self, x):
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[py] = px 
            self.set_count -= 1

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # dis group, graph
        dis = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            dis[a].append(b)
            dis[b].append(a)
        
        uf = UF(n)
        for i, d in enumerate(dis):
            if len(d) > 1:
                dn = len(d)
                for j in range(1, dn):
                    uf.union(d[0] - 1, d[j] - 1)

        # 5
        # [[1,2],[3,4],[4,5],[3,5]]
        for a, b in dislikes:
            if uf.find(a - 1) == uf.find(b - 1):
                return False
        return n <= 1 or uf.set_count > 1

'''
Runtime: 953 ms, faster than 70.39% of Python3 online submissions for Possible Bipartition.
Memory Usage: 19.3 MB, less than 99.37% of Python3 online submissions for Possible Bipartition.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n)) 
        
    def find(self, x):
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[py] = px

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        uf = UF(n * 2 + 2)
        for a, b in dislikes:
            if uf.find(a) == uf.find(b):
                return False
            uf.union(a + n, b)
            uf.union(a, b + n)
        return True
    
    