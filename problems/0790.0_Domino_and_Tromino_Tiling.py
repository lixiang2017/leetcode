'''
DP

Runtime: 28 ms, faster than 94.87% of Python3 online submissions for Domino and Tromino Tiling.
Memory Usage: 14.3 MB, less than 70.51% of Python3 online submissions for Domino and Tromino Tiling.
'''
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * 1001
        dp[1], dp[2], dp[3] = 1, 2, 5
        if n <= 3:
            return dp[n]
        for i in range(n - 3):
            x = i + 4
            dp[x] = 2 * dp[x - 1] + dp[x - 3]
            dp[x] %= MOD
        return dp[n]
        
