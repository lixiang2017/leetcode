class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        low = prices[0]
        for price in prices:
            if low > price:
                low = price
            if price - low > max_profit:
                max_profit = price - low

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    assert Solution().maxProfit(prices) == 5
    prices = [7, 6, 4, 3, 1]
    assert Solution().maxProfit(prices) == 0
