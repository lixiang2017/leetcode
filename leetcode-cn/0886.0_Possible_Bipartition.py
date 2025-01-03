'''
UF

执行用时：356 ms, 在所有 Python3 提交中击败了10.47% 的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了88.92% 的用户
通过测试用例：70 / 70
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
执行用时：272 ms, 在所有 Python3 提交中击败了16.14% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了98.93% 的用户
通过测试用例：70 / 70
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
    
    