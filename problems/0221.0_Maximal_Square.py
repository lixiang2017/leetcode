'''
DP

Runtime: 323 ms, faster than 18.87% of Python3 online submissions for Maximal Square.
Memory Usage: 15.5 MB, less than 91.57% of Python3 online submissions for Maximal Square.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxsqlen = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])
        return maxsqlen * maxsqlen
            