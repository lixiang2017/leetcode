'''
approach: Union Find

%53
%48
'''


'''
  3\0/1
  3/2\1
'''



class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        uf = UnionFind(n)

        for i, row in enumerate(grid):
            for j, square in enumerate(row):
                idx = (i * n + j) * 4    
                if square == ' ':
                    uf.union(idx, idx + 1)
                    uf.union(idx + 1, idx + 2)
                    uf.union(idx + 2, idx + 3)
                elif square == '/':
                    uf.union(idx, idx + 3)
                    uf.union(idx + 1, idx + 2)
                else:    # '\'
                    uf.union(idx, idx + 1)
                    uf.union(idx + 2, idx + 3)
                # union horizontal
                if j < n - 1:
                    nextIdx = (i * n + j + 1) * 4
                    uf.union(idx + 1, nextIdx + 3)
                # union vertical
                if i < n - 1:
                    nextIdx = ((i + 1) * n + j) * 4  
                    uf.union(idx + 2, nextIdx)

        return uf.getCount

class UnionFind(object):
    def __init__(self, n):
        # n, the length of grid
        self.parent = {i: i for i in range(n * n * 4)}
        self.getCount = n * n * 4

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        else:
            self.parent[rootX] = rootY
            self.getCount -= 1
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
