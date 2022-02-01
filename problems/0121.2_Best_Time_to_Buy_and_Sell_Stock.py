'''
Runtime: 1297 ms, faster than 45.09% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25 MB, less than 80.69% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minx = prices[0]
        for p in prices:
            ans = max(ans, p - minx)
            minx = min(minx, p)
        return ans 
        