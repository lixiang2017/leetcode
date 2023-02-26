'''
DP
T: O(MN)
S: O(MN)

Runtime: 143 ms, faster than 80.75% of Python3 online submissions for Edit Distance.
Memory Usage: 17.6 MB, less than 55.49% of Python3 online submissions for Edit Distance.
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # first row
        for j in range(n + 1):
            dp[0][j] = j
        # first column
        for i in range(m + 1):
            dp[i][0] = i
            
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
    
        return dp[-1][-1]
