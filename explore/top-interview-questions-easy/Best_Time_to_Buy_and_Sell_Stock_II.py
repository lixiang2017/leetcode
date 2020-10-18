'''
not use index i

You are here!
Your runtime beats 15.53 % of python submissions.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        sum_profit = 0
        last_price = prices[0]
        for price in prices:
            if price < last_price:
                last_price = price
            else:
                sum_profit += price - last_price
                last_price = price
                
        return sum_profit
