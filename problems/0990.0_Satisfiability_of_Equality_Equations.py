'''
Union Find

Runtime: 105 ms, faster than 11.95% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14 MB, less than 94.08% of Python3 online submissions for Satisfiability of Equality Equations.
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
            self.p[px] = py
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        for e in equations:
            if e[1] == '=':
                x, y = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
                uf.union(x, y)
        for e in equations:
            if e[1] == '!':
                x, y = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
                px, py = uf.find(x), uf.find(y)
                if px == py:
                    return False
        return True


'''
Runtime: 75 ms, faster than 57.77% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14 MB, less than 94.08% of Python3 online submissions for Satisfiability of Equality Equations.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        for e in equations:
            if e[1] == '=':
                x, y = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
                uf.union(x, y)
        for e in equations:
            if e[1] == '!':
                x, y = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
                px, py = uf.find(x), uf.find(y)
                if px == py:
                    return False
        return True

'''
size 

Runtime: 114 ms, faster than 6.50% of Python3 online submissions for Satisfiability of Equality Equations.
Memory Usage: 14.1 MB, less than 35.38% of Python3 online submissions for Satisfiability of Equality Equations.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] >= self.size[py]:
                self.p[py] = px
                self.size[px] += self.size[py]
            else:
                self.p[px] = py
                self.size[py] += self.size[px]
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        not_equal_pair = []
        for e in equations:
            x, y = ord(e[0]) - ord('a'), ord(e[3]) - ord('a')
            if e[1] == '=':
                uf.union(x, y)
            else:
                not_equal_pair.append([x, y])
        for x, y in not_equal_pair:
            px, py = uf.find(x), uf.find(y)
            if px == py:
                return False
        return True
