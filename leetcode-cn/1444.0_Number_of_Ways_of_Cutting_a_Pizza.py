'''
DFS + Memo

执行用时：484 ms, 在所有 Python3 提交中击败了17.82% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了52.48% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        r, c = len(pizza), len(pizza[0])
        MOD = 10 ** 9 + 7

        @cache
        def f(x, y, k):
            if not k:
                return any('A' == pizza[i][j] for i in range(x, r) for j in range(y, c)) % MOD
            w = 0
            for i in range(x + 1, r):
                if any('A' == pizza[ii][jj] for ii in range(x, i) for jj in range(y, c)):
                    w += f(i, y, k - 1)
            for j in range(y + 1, c):
                if any('A' == pizza[ii][jj] for ii in range(x, r) for jj in range(y, j)):
                    w += f(x, j, k - 1)
            return w % MOD 

        return f(0, 0, k - 1)
