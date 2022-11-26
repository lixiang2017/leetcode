'''
sort + binary search + DP + Greedy
T: O(NlogN)
S: O(N)

Runtime: 535 ms, faster than 98.68% of Python3 online submissions for Maximum Profit in Job Scheduling.
Memory Usage: 29.1 MB, less than 50.68% of Python3 online submissions for Maximum Profit in Job Scheduling.
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda job: job[1])
        startTime, endTime, profit = zip(*jobs)
        dp = [0] * (len(profit) + 1)
        for i in range(len(profit)):
            idx = bisect_right(endTime, startTime[i])
            dp[i + 1] = max(dp[i], dp[idx] + profit[i])
        return dp[-1]
        
