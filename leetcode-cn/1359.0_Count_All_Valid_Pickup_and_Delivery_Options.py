'''
执行用时：32 ms, 在所有 Python3 提交中击败了68.33% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了78.33% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        choice = [i * (2 * i - 1) % MOD for i in range(1, n + 1)]
        return reduce(operator.mul, choice) % MOD
