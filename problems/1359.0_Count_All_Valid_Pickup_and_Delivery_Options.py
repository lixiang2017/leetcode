'''
Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
Memory Usage: 13.8 MB, less than 88.07% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
'''
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        choice = [i * (2 * i - 1) % MOD for i in range(1, n + 1)]
        return reduce(operator.mul, choice) % MOD
        