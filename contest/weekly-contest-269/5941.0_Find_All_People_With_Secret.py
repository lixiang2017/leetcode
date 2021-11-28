'''
42 / 42 个通过测试用例
状态：通过
执行用时: 964 ms
内存消耗: 112 MB
提交时间：12 小时前
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        while x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            x = self.p[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py
        
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        m = meetings
        m.sort(key=lambda mm: mm[2])
        ml = len(m)
        uf = UF(n)
        uf.union(0, firstPerson)
        i = 0
        while i < ml:
            j = i
            ai, bi, ti = m[i]
            aj, bj, tj = m[j]
            while j < ml and m[j][2] == ti:
                a, b, _ = m[j]
                uf.union(a, b)
                j += 1    
            k = i
            while k < j:
                a, b, _ = m[k]
                if uf.find(a) != uf.find(0):
                    uf.p[a] = a
                if uf.find(b) != uf.find(0):
                    uf.p[b] = b
                k += 1
            i = j
            
        p0 = uf.find(0)
        return [i for i in range(n) if uf.find(i) == p0]

