'''
DP, T:O(N^2)，S:O(N^2)

执行用时：1096 ms, 在所有 Python3 提交中击败了80.91% 的用户
内存消耗：31 MB, 在所有 Python3 提交中击败了69.28% 的用户

86 / 86 个通过测试用例
状态：通过
执行用时: 1096 ms
内存消耗: 31 MB
提交时间：6 小时前
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][N - 1]


'''
转化为最长公共子序列LCS，DP, T:O(N^2)，S:O(N^2)

执行用时：2040 ms, 在所有 Python3 提交中击败了15.60%的用户
内存消耗：39.7 MB, 在所有 Python3 提交中击败了5.00%的用户
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        r = ''.join(list(reversed(s)))
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                if s[i] == r[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[N][N]
