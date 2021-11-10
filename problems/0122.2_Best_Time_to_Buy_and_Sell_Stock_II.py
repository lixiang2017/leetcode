'''
T: O(N)
S: O(1)

Runtime: 52 ms, faster than 98.24% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 15.1 MB, less than 66.73% of Python3 online submissions for Best Time to Buy and Sell Stock II.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        pre = prices[0]
        for post in prices:
            if post > pre:
                maxprofit += post - pre
            pre = post
        
        return maxprofit
