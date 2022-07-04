'''
DP
T: O(N * forget)
S: O(N * forget)

执行用时：1588 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：37.6 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：80 / 80
'''
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * forget for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = sum(dp[i - 1][delay - 1: forget - 1]) % MOD 
            for j in range(1, forget):
                dp[i][j] = dp[i - 1][j - 1] % MOD 
        return sum(dp[-1]) % MOD 
