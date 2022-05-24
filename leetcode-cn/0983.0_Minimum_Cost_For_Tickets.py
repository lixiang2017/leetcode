'''
DP
T: O(365 * 37)
S: O(365)

执行用时：60 ms, 在所有 Python3 提交中击败了13.33% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了70.27% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * n 
        dp[0] = min(costs)
        # try cost[1]
        j = 1
        while j < n and days[j] <= days[0] + 7 - 1:
            dp[j] = min(dp[j], costs[1])
            j += 1
        # try cost[2]
        j = 1
        while j < n and days[j] <= days[0] + 30 - 1:
            dp[j] = min(dp[j], costs[2])
            j += 1

        for i in range(n):
            d = days[i]
            # days[i] -> dp[i]
            # try cost[0]
            j = i + 1
            if j < n:
                dp[j] = min(dp[j], dp[i] + costs[0])
            # try cost[1]
            j = i + 1
            while j < n and days[j] <= days[i + 1] + 7 - 1:
                dp[j] = min(dp[j], dp[i] + costs[1])
                j += 1
            # try cost[2]
            j = i + 1
            while j < n and days[j] <= days[i + 1] + 30 - 1:
                dp[j] = min(dp[j], dp[i] + costs[2])
                j += 1

        return dp[-1]
