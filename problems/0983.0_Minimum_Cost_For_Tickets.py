'''
DP

Runtime: 53 ms, faster than 39.96% of Python3 online submissions for Minimum Cost For Tickets.
Memory Usage: 14 MB, less than 58.35% of Python3 online submissions for Minimum Cost For Tickets.
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = [days[0]] + days
        n = len(days)
        dp = [i * costs[0] for i in range(n)]
        for i in range(1, n):
            dp[i] = min(dp[i], dp[i - 1] + costs[0])
            j = i
            while j < n and days[i] + 6 >= days[j]:
                dp[j] = min(dp[j], dp[i - 1] + costs[1])
                j += 1
            k = i
            while k < n and days[i] + 29 >= days[k]:
                dp[k] = min(dp[k], dp[i - 1] + costs[2])
                k += 1

        return dp[-1]
