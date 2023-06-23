'''
执行用时：256 ms, 在所有 Python3 提交中击败了22.49% 的用户
内存消耗：37.9 MB, 在所有 Python3 提交中击败了5.20% 的用户
通过测试用例：27 / 27
'''
class UF:
    def __init__(self, n):
        self.fa = list(range(n))
        self.size = [1] * n 
    
    def find(self, x):
        if x == self.fa[x]:
            return x 
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.fa[fx] = fy 
            self.size[fy] += self.size[fx]

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m, n = len(land), len(land[0])
        uf = UF(m * n)
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    continue
                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
                    if 0 <= ni < m and 0 <= nj < n and land[ni][nj] == 0:
                        uf.union(i * n + j, ni * n + nj)
        
        ans = []
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if land[i][j] == 0 and uf.find(idx) == idx:
                    ans.append(uf.size[idx])
        ans.sort()
        return ans 
        