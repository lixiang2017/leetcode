'''
approach: DP
Time: O(MN)
Space: O(MN)
执行用时：324 ms, 在所有 Python 提交中击败了33.69%的用户
内存消耗：20.8 MB, 在所有 Python 提交中击败了80.73%的用户
'''


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                curMax = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                if text1[i - 1] == text2[j - 1]:
                    curMax = max(curMax, dp[i-1][j-1] + 1)
                dp[i][j] = curMax

        return dp[M][N]
