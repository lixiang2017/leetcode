'''
执行用时：120 ms, 在所有 Python3 提交中击败了63.64% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了59.09% 的用户
通过测试用例：43 / 43
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        a -> e
        e -> a/i
        i -> a/e/o/u
        o -> i/u
        u -> a
        '''
        MOD = 10 ** 9 + 7
        a1 = e1 = i1 = o1 = u1 = 1
        a2 = e2 = i2 = o2 = u2 = 0
        for i in range(n - 1):
            a2, e2, i2, o2, u2 = e1 + i1 + u1, a1 + i1, e1 + o1, i1, i1 + o1
            a1, e1, i1, o1, u1 = a2 % MOD, e2 % MOD, i2 % MOD, o2 % MOD, u2 % MOD 

        return (a1 + e1 + i1 + o1 + u1) % MOD
        