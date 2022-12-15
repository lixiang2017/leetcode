'''
DP
T: O(MN)
S: O(MN)

Runtime: 384 ms, faster than 87.68% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 21.9 MB, less than 80.84% of Python3 online submissions for Longest Common Subsequence.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for i in range(n2):
            for j in range(n1):
                if text1[j] == text2[i]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[-1][-1]

'''
DP

Runtime: 419 ms, faster than 90.80% of Python3 online submissions for Longest Common Subsequence.
Memory Usage: 22 MB, less than 71.29% of Python3 online submissions for Longest Common Subsequence.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
