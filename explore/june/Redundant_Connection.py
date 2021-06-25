'''
approach: Union Find
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 71.41 % of python3 submissions.
You are here!
Your memory usage beats 39.82 % of python3 submissions.
'''


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        uf = UnionFind(N + 1)
        for a, b in edges:
            if not uf.union(a, b):
                return [a, b]
        
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.father = list(range(n))
    
    def find(self, x):
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, x, y):
        fax = self.find(x)
        fay = self.find(y)
        if fax == fay:
            return False
        else:
            self.father[fax] = fay
            return True

'''
approach: Union Find
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 88.15 % of python3 submissions.
You are here!
Your memory usage beats 66.32 % of python3 submissions.

ref:
https://leetcode.com/problems/redundant-connection/discuss/108002/Unicode-Find-(5-short-lines
'''


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = ''.join(map(chr, range(1001)))
        for u, v in edges:
            if tree[u] == tree[v]:
                return [u, v]
            tree = tree.replace(tree[u], tree[v])

