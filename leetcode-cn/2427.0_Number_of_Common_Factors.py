'''
执行用时：36 ms, 在所有 Python3 提交中击败了72.14% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了98.93% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        return sum(g % i == 0 for i in range(1, g + 1))

'''
执行用时：52 ms, 在所有 Python3 提交中击败了8.57% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了78.93% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def _gcd(x, y):
            if x == 0:
                return y
            return _gcd(y % x, x)

        def calc_cnt(g):
            res = 1
            c = Counter()
            i = 2 
            while i * i <= g:
                while g % i == 0:
                    c[i] += 1
                    g //= i
                i += 1
            if g > 1:
                c[g] += 1
            for f, cnt in c.items():
                res *= (cnt + 1)
            return res 

        g = _gcd(a, b)
        return calc_cnt(g)

