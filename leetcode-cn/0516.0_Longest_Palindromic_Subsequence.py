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


'''
区间DP
https://www.bilibili.com/video/BV1Gs4y1E7EU/

执行用时：812 ms, 在所有 Python3 提交中击败了98.37% 的用户
内存消耗：246.4 MB, 在所有 Python3 提交中击败了5.00% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))
        
        return dfs(0, len(s) - 1)


'''
区间DP
https://www.bilibili.com/video/BV1Gs4y1E7EU/

执行用时：984 ms, 在所有 Python3 提交中击败了92.28% 的用户
内存消耗：31.2 MB, 在所有 Python3 提交中击败了74.44% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]


