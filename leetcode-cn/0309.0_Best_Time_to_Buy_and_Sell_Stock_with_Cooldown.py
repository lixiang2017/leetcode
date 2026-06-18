class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            return max(dfs(i - 1, True) + prices[i], dfs(i - 1, False))

        return dfs(n - 1, False)