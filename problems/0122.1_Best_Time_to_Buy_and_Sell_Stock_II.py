'''
Success
Details
Runtime: 52 ms, faster than 41.45% of Python online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 14.2 MB, less than 17.58% of Python online submissions for Best Time to Buy and Sell Stock II.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        transactions = []
        
        size = len(prices)
        
        profit = 0
        current_low = sys.maxint
        for i in xrange(size - 1):
            if prices[i] < current_low:
                current_low = prices[i]
                print 'current_low: ', current_low
            
            if prices[i + 1] >= prices[i]:
                if i == size - 2:
                    transactions.append(prices[i + 1] - current_low)
                else:
                    continue
            elif prices[i + 1] < prices[i] and prices[i] > current_low:
                print 'prices[i], prices[i + 1]: ', prices[i], prices[i + 1]
                print 'append: ', prices[i] - current_low
                transactions.append(prices[i] - current_low)
                current_low = prices[i]
                print 'current_low2: ', current_low
            
        print 'transactions: ', transactions
        # transactions.sort(reverse = True)
        # k = min(k, len(transactions))
        k = len(transactions)
        for i in xrange(k):
            profit += transactions[i]
        return profit        
