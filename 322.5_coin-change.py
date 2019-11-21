#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#
'''
Accepted
182/182 cases passed (908 ms)
Your runtime beats 86.62 % of python submissions
Your memory usage beats 70 % of python submissions (11.9 MB)
'''
# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp = [0] + [float('inf') for _ in range(amount)+ 1]
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i]] + [dp[i - c] + 1 if i - c >= 0 else MAX for c in coins])

        return [dp[amount], -1][dp[amount] == MAX]

        
# @lc code=end

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    # 11 = 5 + 5 + 1
    assert Solution().coinChange(coins, amount) == 3

    coins = [2]
    amount = 3
    assert Solution().coinChange(coins, amount) == -1

    coins = [0] # must be a list. if 'coins = 0', TypeError: 'int' object is not iterable
    amount = 0
    assert Solution().coinChange(coins, amount) == 0





