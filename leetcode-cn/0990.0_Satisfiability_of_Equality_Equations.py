'''
approach: Union Find
Time: O(N + ClogC), C <= 26
Space: O(C)


执行用时：52 ms, 在所有 Python3 提交中击败了83.37% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了78.62% 的用户
'''

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        # union
        for equation in equations:
            if equation[1] == '=' and equation[0] != equation[3]:
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                uf.union(x, y)
        # !=
        for equation in equations:
            if equation[1] == '!':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False

        return True            


class UnionFind:
    def __init__(self, n):
        self.groups = n
        self.parent = [i for i in range(n)]
    
    def union(self, x, y):
        xparent = self.find(x)
        yparent = self.find(y)
        if xparent == yparent:
            return False
        else:
            self.parent[xparent] = yparent
            self.groups -= 1
            return True
    
    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

'''
["a==b","b!=a"]
["b==a","a==b"]
["a==b","b==c","a==c"]
["a==b","b!=c","c==a"]
["c==c","b==d","x!=z"]
["f==a","a==b","f!=e","a==c","b==e","c==f"]
'''


