'''
approach: DP
dp[i] means the max profit at i-th day

Time: O(N)
Space: O(N)
执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了73.54% 的用户
内存消耗：14 MB, 在所有 Python 提交中击败了33.98% 的用户
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        size = len(prices)
        dp = [0] * size
        minPrice = prices[0]
        for i in range(1, size):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
        return dp[-1]
