'''
approach: DP
Time: O(M * N)
Space: O(M * N)

执行用时：24 ms, 在所有 Python 提交中击败85.00%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了30.00%的用户
'''

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        M, N = len(s), len(t)
        dp = [[0] * N + [1] for _ in range(M + 1)]
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]
