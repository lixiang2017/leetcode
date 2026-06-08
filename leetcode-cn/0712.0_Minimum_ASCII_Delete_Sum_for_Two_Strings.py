class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[0][j] = ord(s1[j - 1]) + dp[0][j - 1]
        for i in range(1, n + 1):
            dp[i][0] = ord(s2[i - 1]) + dp[i - 1][0]
        for i, j in itertools.product(range(1, n + 1), range(1, m + 1)):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1] + ord(s1[j - 1]), dp[i - 1][j] + ord(s2[i - 1]))
        return dp[n][m]