'''
Runtime: 52 ms, faster than 86.21% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 14 MB, less than 91.95% of Python3 online submissions for Richest Customer Wealth.
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)
        