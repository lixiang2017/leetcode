'''
执行用时：40 ms, 在所有 Python3 提交中击败了29.72% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了37.02% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n <= 1:
            return n
        
        f = [0, 1]
        for _ in range(n - 1):
            f.append(f[-1] + f[-2])
        return f[-1] % MOD
