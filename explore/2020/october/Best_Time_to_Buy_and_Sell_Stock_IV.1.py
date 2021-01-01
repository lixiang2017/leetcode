'''
Submission Detail
207 / 212 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 1 minute ago
Last executed input: 7
[48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
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
        def dfs(index, status, count):
            if index == size or count == k:
                return 0
            
            a, b, c = 0, 0, 0
            # status for buy or sell
            # stay still
            a = dfs(index + 1, status, count)
            if status:  # sell
                b = dfs(index + 1, 0, count + 1) + prices[index]
            else: # buy
                c = dfs(index + 1, 1, count) - prices[index]
            
            return max(a, b, c)
    
        return dfs(0, 0, 0)
               
        