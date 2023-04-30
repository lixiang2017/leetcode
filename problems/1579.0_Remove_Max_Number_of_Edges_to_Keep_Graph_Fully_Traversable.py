'''
Runtime: 2255 ms, faster than 37.74% of Python3 online submissions for Remove Max Number of Edges to Keep Graph Fully Traversable.
Memory Usage: 56.4 MB, less than 18.87% of Python3 online submissions for Remove Max Number of Edges to Keep Graph Fully Traversable.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.set_count = n
        
    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
            self.set_count -= 1
            return True
        else:
            return False
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        t1, t2 = [], []
        uf1 = UF(n)
        common_remove = remove1 = remove2 = 0
        
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1:
                t1.append([u, v])
            elif t == 2:
                t2.append([u, v])
            else:
                if not uf1.union(u, v):
                    common_remove += 1
                    
        uf2 = copy.deepcopy(uf1)
        # t1
        for u, v in t1:
            if not uf1.union(u, v):
                remove1 += 1
        # t2
        for u, v in t2:
            if not uf2.union(u, v):
                remove2 += 1
                
        if uf1.set_count != 1 or uf2.set_count != 1:
            return -1
        else:
            return common_remove + remove1 + remove2

