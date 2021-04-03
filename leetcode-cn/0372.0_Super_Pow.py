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
