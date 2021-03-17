'''
approach: DP
Time: O(N)
Space: O(1)

You are here!
Your memory usage beats 72.84 % of python submissions.
'''

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        N = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, N):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        
        return sell
        