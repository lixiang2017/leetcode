'''
You are here!
Your runtime beats 45.76 % of python submissions.
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        low = prices[0]
        max_profit = 0
        for price in prices:
            if price < low:
                low = price
            if price - low > max_profit:
                max_profit = price - low
        
        return max_profit
        


