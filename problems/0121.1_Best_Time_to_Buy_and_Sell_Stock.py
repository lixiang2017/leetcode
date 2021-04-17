'''
approach: DP
Time: O(N + N) = O(N)
Space: O(N)

Runtime: 1272 ms, faster than 5.14% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 52.64% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        minPrices = [0] * N
        minPrice = prices[0]
        for i in range(N):
            minPrice = min(prices[i], minPrice)
            minPrices[i] = minPrice
        
        maxPrice = prices[-1]
        max_profit = 0
        for i in range(N - 1, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            profit = maxPrice - minPrices[i]
            max_profit = max(max_profit, profit)
        
        return max_profit
        