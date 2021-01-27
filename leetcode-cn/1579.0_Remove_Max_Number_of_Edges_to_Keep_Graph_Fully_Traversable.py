'''
approach: Union Find
Time: O(m * alpha(n)), m is the length of edges and n is the numbers of points
Space: O(n)


ref:
https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solution/bao-zheng-tu-ke-wan-quan-bian-li-by-leet-mtrw/
'''


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        num = 0
        ufa, ufb = UnionFind(n), UnionFind(n)
        # set vertex index starting from 0
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # common edges
        for edge in edges:
            t, u, v = edge
            if 3 == t:
                if not ufa.union(u, v):
                    num += 1
                else:
                    ufb.union(u, v)
        
        # 
        for edge in edges:
            t, u, v = edge
            if 1 == t:
                if not ufa.union(u, v):
                    num += 1
            elif 2 == t:
                if not ufb.union(u, v):
                    num += 1
        
        if ufa.getCount != 1 or ufb.getCount != 1:
            return -1
        return num

class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.getCount = n
        self.size = [1] * n
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return False

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.getCount -= 1
        return True
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y
