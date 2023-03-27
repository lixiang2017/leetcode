'''
利用并查集找环再DFS. 
合并成功True,已合并False.
在已合并的环里DFS，求步长。

Runtime: 1509 ms, faster than 40.50% of Python3 online submissions for Longest Cycle in a Graph.
Memory Usage: 142.9 MB, less than 50.47% of Python3 online submissions for Longest Cycle in a Graph.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x: int) -> int:
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            self.p[px] = py
            return True

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        def cycleLength(start, child, step):
            if start == child:
                return step 
            return cycleLength(start, edges[child], step + 1)

        uf = UF(n)
        ans = -1
        for a, b in enumerate(edges):
            if b != -1:
                if not uf.union(a, b):
                    ans = max(ans, cycleLength(a, b, 1))
        return ans 

