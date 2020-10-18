'''
You are here!
Your runtime beats 23.08 % of python submissions.
'''

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        size = len(prices)
        # max profit without time limits
        if k > size // 2:
            return sum(i - j for i, j in zip(prices[1 : ], prices[ : -1]) if i > j)
        
        dp = [[[0, 0] for _ in xrange(k + 1)] for _ in xrange(size)]
        # init
        for i in xrange(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        # iterate
        for i in xrange(1, size):
            for j in xrange(1, k + 1):
                # buy
                dp[i][j - 1][1] = max(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0] - prices[i])                
                # sell
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])

        
        return dp[-1][k][0]
           
        