'''
DP

执行用时：220 ms, 在所有 Python3 提交中击败了62.98% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了83.36% 的用户
通过测试用例：1306 / 1306
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for i in range(n2):
            for j in range(n1):
                if word2[i] == word1[j]:
                    # dp[i+1][j+1] = max(dp[i+1][j], 1 + dp[i][j], dp[i][j+1])
                    # 只可能从左上角转移到当前位置
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    # dp[i+1][j+1] = max(dp[i+1][j], dp[i][j], dp[i][j+1])
                    #　只可能从上面或左侧转移到当前位置
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        # return n1 + n2 - 2 * max(dp[-1])
        #　最长公共子序列的长度值肯定会在在最后一个数字
        return n1 + n2 - 2 * dp[-1][-1]
