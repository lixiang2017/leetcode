'''
执行用时：68 ms, 在所有 Python 提交中击败了93.48%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了89.13%的用户
'''


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        a %= MOD
        a10 = [a ** i % MOD for i in range(10)]
        ans = 1
        for p in b:
            ans **= 10
            ans %= MOD
            ans *= a10[p]
            ans %= MOD

        return ans

'''
执行用时：60 ms, 在所有 Python3 提交中击败了87.05% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了83.09% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int(''.join(map(str, b))), 1337)

'''
quick mul

执行用时：76 ms, 在所有 Python3 提交中击败了69.42% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了74.10% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        MOD = 1337
        for e in reversed(b):
            ans = ans * self.pow(a, e, MOD) % MOD
            a = self.pow(a, 10, MOD)
        return ans

    def pow(self, a: int, n: int, mod: int) -> int:
        p = 1
        while n:
            if n % 2 == 1:
                p = p * a % mod
            a = a * a % mod
            n >>= 1
        return p 

'''
执行用时：112 ms, 在所有 Python3 提交中击败了43.17% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了64.75% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        MOD = 1337
        for e in reversed(b):
            ans = ans * self.pow(a, e, MOD) % MOD
            a = self.pow(a, 10, MOD)
        return ans

    def pow(self, a: int, n: int, mod: int) -> int:
        p = 1
        while n:
            if n % 2 == 1:
                p *= a % mod
            a *= a % mod
            n >>= 1
        return p 


'''
执行用时：84 ms, 在所有 Python3 提交中击败了64.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.32% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for e in b:
            ans = self.pow(ans, 10, MOD) * self.pow(a, e, MOD) % MOD 
        return ans 
    
    def pow(self, base: int, n: int, mod: int) -> int:
        if n < 0:
            base = 1.0 / base
        p = 1
        while n:
            if n & 1:
                p *= base % mod 
            base *= base 
            n >>= 1
        return p 


'''
执行用时：72 ms, 在所有 Python3 提交中击败了73.02% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了98.92% 的用户
通过测试用例：55 / 55
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for e in b:
            ans = pow(ans, 10, MOD) * pow(a, e, MOD) % MOD 
        return ans 
    
    
