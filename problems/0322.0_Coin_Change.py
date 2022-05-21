'''
DP
T: O(MN)
S: O(N)

Runtime: 1897 ms, faster than 53.00% of Python3 online submissions for Coin Change.
Memory Usage: 14.1 MB, less than 82.65% of Python3 online submissions for Coin Change.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 2 * amount + 10
        dp = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
         
        return dp[amount] if dp[amount] != MAX else -1
    

'''

Input: [1]
0
Output: -1
Expected: 0
'''
