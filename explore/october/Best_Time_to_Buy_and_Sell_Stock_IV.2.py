'''
212 / 212 test cases passed.
	Status: Accepted
Runtime: 356 ms
Memory Usage: 52 MB
	
Submitted: 0 minutes ago
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
        
        # to memorise history
        memo = {}
        def dfs(index, status, count):
            if (index, status, count) in memo:
                return memo[(index, status, count)]
            
            if index == size or count == k:
                memo[(index, status, count)] = 0
                return 0
            
            a, b, c = 0, 0, 0
            # status for buy or sell
            # stay still
            a = dfs(index + 1, status, count)
            if status:  # sell
                b = dfs(index + 1, 0, count + 1) + prices[index]
            else: # buy
                c = dfs(index + 1, 1, count) - prices[index]
            
            memo[(index, status, count)] = max(a, b, c)
            return memo[(index, status, count)]
    
        return dfs(0, 0, 0)
               
        