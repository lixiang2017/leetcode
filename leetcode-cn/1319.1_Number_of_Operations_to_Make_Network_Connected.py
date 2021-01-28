'''
approach: Union Find with Path Compression

执行结果：通过
显示详情
执行用时：152 ms, 在所有 Python 提交中击败了69.23%的用户
内存消耗：27 MB, 在所有 Python 提交中击败了53.85%的用户
'''

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1: return -1

        uf = UnionFind(n)
        for conn in connections:
            a, b = conn
            uf.union(a, b)

        return uf.getCount - 1


class UnionFind(object):
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        # the number of connected components
        self.getCount = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        
        # return self.find(self.parent[x])
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        else:
            self.parent[rootX] = rootY
            self.getCount -= 1

