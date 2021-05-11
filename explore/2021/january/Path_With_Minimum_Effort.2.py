'''
approach: Union Find + Sort

ref:
https://leetcode-cn.com/problems/path-with-minimum-effort/solution/python-zui-duan-lu-jing-bing-cha-ji-er-f-avva/

执行结果：通过
显示详情
执行用时：656 ms, 在所有 Python 提交中击败了86.11%的用户
内存消耗：17.3 MB, 在所有 Python 提交中击败了24.64%的用户
'''


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        uf = UnionFind(m * n)

        edges = []  # (source, destination, diff)
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if i > 0:
                    edges.append([idx - n, idx, abs(heights[i - 1][j] - heights[i][j])])
                if j > 0:
                    edges.append([idx - 1, idx, abs(heights[i][j - 1] - heights[i][j])])

        edges.sort(key = lambda edge: edge[2])
        for edge in edges:
            uf.union(edge[0], edge[1])
            if uf.isConnnected(0, m * n - 1):
                return edge[2]

        return 0


class UnionFind(object):
    """docstring for UnionFind"""
    def __init__(self, n):
        super(UnionFind, self).__init__()
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.componentCount = n

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False

        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

        self.componentCount -= 1
        return True

    def isConnnected(self, x, y):
        return self.find(x) == self.find(y)
