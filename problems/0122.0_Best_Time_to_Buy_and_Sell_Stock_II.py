class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum_profit = 0
        if not prices:
            return 0

        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                sum_profit += prices[i+1] - prices[i]

        return sum_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert Solution().maxProfit(prices) == 7
    prices = [1, 2, 3, 4, 5]
    assert Solution().maxProfit(prices) == 4
    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0
