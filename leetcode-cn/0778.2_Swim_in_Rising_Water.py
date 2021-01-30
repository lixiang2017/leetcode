'''
approach: Sort + Union Find
Time: O(N ^ 2 + N^2*log(N^２) + ...) = O(N ^ 2 * logN)
Space: O(N ^ 2)

same as https://leetcode-cn.com/problems/path-with-minimum-effort/

# find0
执行结果：
通过
显示详情
执行用时：140 ms, 在所有 Python 提交中击败了53.85%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了80.77%的用户

# find
执行结果：
通过
显示详情
执行用时：124 ms, 在所有 Python 提交中击败了57.69%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了50.00%的用户
'''


class Solution(object):

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size = len(grid)
        uf = UnionFind(size * size)
        edges = []  #(source_idx, destination_idx, max_elevation)
        for i in range(size):
            for j in range(size):
                idx = i * size + j
                if i > 0:
                    edges.append((idx - size, idx, max(grid[i - 1][j], grid[i][j])))
                if j > 0:
                    edges.append((idx - 1, idx, max(grid[i][j - 1], grid[i][j])))
        
        edges.sort(key=lambda edge: edge[2])
        for src_idx, dest_idx, elevation in edges:
            uf.union(src_idx, dest_idx)
            if uf.isConnected(0, size * size - 1):
                return elevation

        return -1


class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.rank = [0 for _ in range(n)]
        self.componentCount = n

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY: return False

        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        self.componentCount -= 1
        return True

    def find0(self, x):
        self.parent[x] = x if x == self.parent[x] else self.find(self.parent[x])
        return self.parent[x]

    def find(self, x):
        if x == self.parent[x]: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
