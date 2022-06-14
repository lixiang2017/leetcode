'''
DP
T: O(MN)
S: O(MN)

Runtime: 528 ms, faster than 19.68% of Python3 online submissions for Delete Operation for Two Strings.
Memory Usage: 17.9 MB, less than 22.72% of Python3 online submissions for Delete Operation for Two Strings.
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # first row
        for j in range(n + 1):
            dp[0][j] = j
        # first column
        for i in range(m + 1):
            dp[i][0] = i 
            
        for i in range(m):
            for j in range(n):
                if word2[i] == word1[j]:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
                else:
                    dp[i + 1][j + 1] = min(dp[i][j] + 2, dp[i + 1][j] + 1, dp[i][j + 1] + 1)
        
        return dp[-1][-1]

'''
Input
"a"
"b"
Output
1
Expected
2
'''
