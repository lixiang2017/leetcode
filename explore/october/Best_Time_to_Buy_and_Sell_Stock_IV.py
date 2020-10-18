'''
Submission Result: Wrong Answer 
Input: 2
[1,2,4,2,5,7,2,4,9,0]
Output: 12
Expected: 13
Stdout: current_low:  1
prices[i], prices[i + 1]:  4 2
append:  3
current_low2:  4
current_low:  2
prices[i], prices[i + 1]:  7 2
append:  5
current_low2:  7
current_low:  2
prices[i], prices[i + 1]:  9 0
append:  7
current_low2:  9
transactions:  [3, 5, 7]
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
        transactions.sort(reverse = True)
        k = min(k, len(transactions))
        for i in xrange(k):
            profit += transactions[i]
        return profit
               
        