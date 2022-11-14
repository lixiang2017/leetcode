'''
Runtime: 355 ms, faster than 64.84% of Python3 online submissions for Most Stones Removed with Same Row or Column.
Memory Usage: 14.6 MB, less than 72.25% of Python3 online submissions for Most Stones Removed with Same Row or Column.
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
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py 
            self.set_count -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # same y; x list -> index for stones
        x_indice = defaultdict(list)
        # same x; y list -> index for stones
        y_indice = defaultdict(list)

        n = len(stones)
        for i, (x, y) in enumerate(stones):
            x_indice[y].append(i)
            y_indice[x].append(i)
        
        uf = UF(n)
        for _, indice in chain(x_indice.items(), y_indice.items()):
            i = indice[0]
            for j in indice:
                uf.union(i, j)
        return n - uf.set_count
        