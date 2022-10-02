'''
DFS + memoization

Runtime: 298 ms, faster than 87.75% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 18.3 MB, less than 43.46% of Python3 online submissions for Number of Dice Rolls With Target Sum.
'''
class Solution:
    MOD = 10 ** 9 + 7
    
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < 1 * n or target > k * n:
            return 0
        elif n == 1:
            return 1
        
        way = 0
        for f in range(1, k + 1):
            way += self.numRollsToTarget(n - 1, k, target - f)
            way %= self.MOD
        return way

'''
DP


Runtime: 546 ms, faster than 72.20% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 14.6 MB, less than 64.02% of Python3 online submissions for Number of Dice Rolls With Target Sum.
'''
class Solution:
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        if target < 1 * n or target > k * n:
            return 0
        dp = [[0] * n for _ in range(n * k + 1)]
        # sum
        for s in range(1, k + 1):
            dp[s][0] = 1
        # round
        for r in range(1, n):
            # sum
            for s in range(1 * (r + 1), k * (r + 1) + 1):
                for f in range(1, k + 1):
                    dp[s][r] += dp[s - f][r - 1]
                    dp[s][r] %= MOD

        return dp[target][n - 1]
    
