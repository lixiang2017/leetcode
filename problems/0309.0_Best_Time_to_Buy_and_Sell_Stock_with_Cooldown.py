'''
Runtime: 54 ms, faster than 35.12% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
Memory Usage: 14.6 MB, less than 63.31% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        s0, s1, s2 = [0] * n, [0] * n, [0] * n
        # s1[0] = float('-inf')  # wrong
        s1[0] = -prices[0]
        for i in range(1, n):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s0[i - 1] - prices[i], s1[i - 1])
            s2[i] = s1[i - 1] + prices[i]
        return max(s0[-1], s2[-1])
        