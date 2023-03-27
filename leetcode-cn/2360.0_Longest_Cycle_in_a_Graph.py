'''
利用并查集找环再DFS. 
合并成功True,已合并False.
在已合并的环里DFS，求步长。

执行用时：564 ms, 在所有 Python3 提交中击败了28.20% 的用户
内存消耗：143.8 MB, 在所有 Python3 提交中击败了21.79% 的用户
通过测试用例：76 / 76
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

