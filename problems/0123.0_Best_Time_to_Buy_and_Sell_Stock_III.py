'''
DP
T: O(N)
S: O(1)

Runtime: 1475 ms, faster than 37.81% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 28.5 MB, less than 30.49% of Python3 online submissions for Best Time to Buy and Sell Stock III.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2


'''
DP
T: O(N)
S: O(1)

Runtime: 1137 ms, faster than 72.71% of Python3 online submissions for Best Time to Buy and Sell Stock III.
Memory Usage: 28.3 MB, less than 46.55% of Python3 online submissions for Best Time to Buy and Sell Stock III.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p - buy1)
            buy2 = min(buy2, p - sell1)
            sell2 = max(sell2, p - buy2)
        return sell2
        
