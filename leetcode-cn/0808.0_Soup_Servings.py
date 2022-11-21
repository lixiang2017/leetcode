'''
DP
执行用时：52 ms, 在所有 Python3 提交中击败了53.26% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了92.39% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0] = [0.5] + [1.0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] + \
                     dp[max(0, i - 2)][max(0, j - 2)] + dp[i - 1][max(0, j - 3)]) / 4
        return dp[n][n]

'''
执行用时：56 ms, 在所有 Python3 提交中击败了32.61% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了89.13% 的用户
通过测试用例：41 / 41
'''
class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0

        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (dfs(a - 4, b) + dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3)) / 4

        return dfs(n, n)
        