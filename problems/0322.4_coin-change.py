#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#
'''
Accepted
182/182 cases passed (712 ms)
Your runtime beats 92.55 % of python submissions
Your memory usage beats 45 % of python submissions (12.1 MB)
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
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

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





