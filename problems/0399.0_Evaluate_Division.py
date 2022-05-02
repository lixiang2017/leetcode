'''
Union Find

Runtime: 56 ms, faster than 20.53% of Python3 online submissions for Evaluate Division.
Memory Usage: 14 MB, less than 60.05% of Python3 online submissions for Evaluate Division.
'''
class UnionFind:
    def __init__(self):
        # variable -> parent
        self.p = dict()
        # variable -> float_value
        self.vs = dict()

    def find(self, x):
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y, fraction):
        # x / y = fraction
        if x not in self.vs and y not in self.vs:
            self.vs[x] = fraction
            self.vs[y] = 1.0
            self.p[x] = y
            self.p[y] = y
        elif x not in self.vs and y in self.vs:
            yv = self.vs[y]
            xv = yv * fraction
            self.vs[x] = xv
            self.p[x] = y
        elif x in self.vs and y not in self.vs:
            xv = self.vs[x]
            yv = xv / fraction
            self.vs[y] = yv
            self.p[y] = x 
        else:
            # all in 
            px, py = self.find(x), self.find(y)
            # xv * ? / yv = fraction  ->  ? = yv * fraction / xv
            # all values that their root is px, value need to * ? 
            xv = self.vs[x]
            yv = self.vs[y]
            factor = yv * fraction / xv
            for s in self.vs.keys():
                if self.find(s) == px:
                    self.vs[s] *= factor
            self.p[px] = py
            

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:  
        uf = UnionFind()
        for (a, b), fraction in zip(equations, values):
            uf.union(a, b, fraction)
        
        ans = []
        for c, d in queries:
            if c not in uf.vs or d not in uf.vs or uf.find(c) != uf.find(d):
                ans.append(-1.0)
            else:
                ans.append(uf.vs[c] / uf.vs[d])
                
        return ans 

