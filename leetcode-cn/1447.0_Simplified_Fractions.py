'''
更相减损术 辗转相除法，最大公约数
T: O(N^2 * logN)
S: O(1)

执行用时：124 ms, 在所有 Python3 提交中击败了41.18% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了9.80% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []

        def gcd(x, y):
            if x == 0:
                return y 
            return gcd(y % x, x)

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                # i / j
                if gcd(i, j) == 1:
                    ans.append(str(i) + '/' + str(j))

        return ans 

'''
执行用时：132 ms, 在所有 Python3 提交中击败了34.31% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了13.72% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []

        def gcd(x, y):
            if x == 0:
                return y 
            return gcd(y % x, x)

        for i in range(2, n + 1):
            for j in range(1, i):
                # j / i
                if gcd(i, j) == 1:
                    ans.append(str(j) + '/' + str(i))

        return ans 

'''
执行用时：64 ms, 在所有 Python3 提交中击败了96.08% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了40.20% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f'{numerator}/{denominator}' 
            for denominator in range(2, n + 1) for numerator in range(1, denominator)
            if gcd(numerator, denominator) == 1]

            