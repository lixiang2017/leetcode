'''
Runtime: 286 ms, faster than 30.47% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 14.4 MB, less than 76.07% of Python3 online submissions for Is Graph Bipartite?.
'''
'''
思路：
使用邻接表储存图
对于每一个点，所有的相连接的neighbours (list)，最终需要合并在一个集合里，
所以使用并查集。所以对于每个点，union all its neighbors.

一定要边检查，边union。

突然发现，题干给的已经是图的邻接表的表示了。
'''

class UnionFind:
    def __init__(self, n):
        # parents
        self.p = list(range(n))
        # size
        self.size = [1] * n
        self.set_count = n 
    
    def find(self, x):
        if x == self.p[x]:
            return x 
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # make sure px <= py, so px -> py
        if self.size[px] > self.size[py]:
            px, py = py, px
        self.p[px] = py
        self.size[py] += self.size[px]
        self.set_count -= 1
        return True
        
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(n)
        for i, neighs in enumerate(graph):
            for j in range(len(neighs)):
                if uf.find(i) == uf.find(neighs[j]):
                    return False
                uf.union(neighs[0], neighs[j])
        return True
                
                
'''
[[1,2,3],[0,2],[0,1,3],[0,2]]
[[1,3],[0,2],[1,3],[0,2]]
[[4],[],[4],[4],[0,2,3]]


Input
[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
Output
true
Expected
false


Input
[[1],[0],[4],[4],[2,3]]
Output
false
Expected
true
''' 
                
                
        
        
        
        