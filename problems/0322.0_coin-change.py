#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#
'''
Accepted
182/182 cases passed (980 ms)
Your runtime beats 84.05 % of python submissions
Your memory usage beats 77.5 % of python submissions (11.9 MB)
'''
# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = [amount + 1] * (amount + 1)
        result[0] = 0

        for i in xrange(1, amount+1):
            for c in coins:
                if i >= c:
                    result[i] = min(result[i], result[i - c] + 1)

        if result[amount] == amount + 1:
            return -1
        else:
            return result[amount]

        
# @lc code=end

if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    # 11 = 5 + 5 + 1
    assert Solution().coinChange(coins, amount) == 3

    coins = [2]
    amount = 3
    assert Solution().coinChange(coins, amount) == -1

    coins = 0
    amount = 0
    assert Solution().coinChange(coins, amount) == 0





