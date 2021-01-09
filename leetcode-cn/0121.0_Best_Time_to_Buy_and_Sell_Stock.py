'''
approach: DP with state compression
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：28 ms, 在所有 Python 提交中击败了51.18% 的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了74.50% 的用户
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = sys.maxint
        profit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)

        return profit
