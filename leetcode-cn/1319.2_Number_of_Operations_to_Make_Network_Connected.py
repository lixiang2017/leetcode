'''
approach: Union Find
1. union by rank
2. path compression by iteration

执行结果：通过
显示详情
执行用时：184 ms, 在所有 Python 提交中击败了30.29%的用户
内存消耗：28.2 MB, 在所有 Python 提交中击败了24.11%的用户
'''



class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        size = len(connections)
        if size < n - 1: return -1
        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a, b)

        return uf.getCount - 1


class UnionFind(object):
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        # the number of nodes
        self.count = n
        # height
        self.rank = [0 for _ in range(n)]
        # the number of nodes in a component with index i
        self.size = [1 for _ in range(n)]
        # the number of connected component
        self.getCount = n

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False

        # by rank
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        self.getCount -= 1
        return True

    def find(self, x):
        if self.parent[x] == x:
            return x

        # path compression by iteration
        # find the root
        root = node = x
        while root != self.parent[root]:
            root = self.parent[root]

        while node != self.parent[node]:
            pa = self.parent[node]
            self.parent[node] = root
            node = pa

        return root
