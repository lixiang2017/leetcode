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


'''
DP, T: O(MN), S: O(MN)

执行用时：520 ms, 在所有 Python3 提交中击败了11.35% 的用户
内存消耗：24.3 MB, 在所有 Python3 提交中击败了8.85% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j - 1] + bool(text1[i - 1] == text2[j - 1])
                f[i][j] = max(f[i][j], f[i - 1][j], f[i][j - 1])
        return f[m][n]
    
    
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i, j in itertools.product(range(n), range(m)):
            if text2[i] == text1[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i, j + 1), dfs(i + 1, j))

        return dfs(0, 0)

'''
两个数组（滚动数组）
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(2)]
        for i, ch1 in enumerate(text1):
            for j, ch2 in enumerate(text2):
                if ch1 == ch2:
                    dp[(i + 1) % 2][j + 1] = 1 + dp[i % 2][j]
                else:
                    dp[(i + 1) % 2][j + 1] = max(dp[i % 2][j + 1], dp[(i + 1) % 2][j])
        return dp[m % 2][-1]
    
'''
一个数组
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for ch1 in text1:
            pre = 0
            for j, ch2 in enumerate(text2):
                tmp = dp[j + 1] # 暂存上一层的，也就是dp[i][j + 1]，备份给 pre 用
                if ch1 == ch2:
                    dp[j + 1] = 1 + pre
                else:
                    dp[j + 1] = max(dp[j + 1], dp[j])
                pre = tmp   # 上一层的，也就是dp[i][j + 1]
        return dp[-1]
