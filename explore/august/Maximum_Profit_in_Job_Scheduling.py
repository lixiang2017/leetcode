'''
Sort + DP + Binary Search 
DP from left to right
T: O(NlogN)
S: O(N)

ref:
https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling/solution/cpython3-pai-xu-dper-fen-by-hanxin_hanxi-azq4/

You are here!
Your runtime beats 14.62 % of python3 submissions.
You are here!
Your memory usage beats 77.75 % of python3 submissions.
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        # sort by endTime
        jobs.sort(key = lambda job: job[1])
        end = [job[1] for job in jobs]
        dp = [0] * N
        dp[0] = jobs[0][2]
        
        for i in range(1, N):
            # index 位于 i 之前
            index = bisect.bisect_right(end, jobs[i][0]) - 1
            dp[i] = max(dp[i - 1], dp[index] + jobs[i][2])

        return dp[-1]


'''
DP from right to left

You are here!
Your runtime beats 69.59 % of python3 submissions.
You are here!
Your memory usage beats 80.31 % of python3 submissions.
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        # sort by startTime
        jobs.sort()
        start = [job[0] for job in jobs]
        dp = [0] * N
        # last profit
        dp[-1] = jobs[-1][2]
        for i in range(N - 2, -1, -1):
            # index 位于 i 之后
            index = bisect.bisect_left(start, jobs[i][1])
            tail = dp[index] if index < N else 0
            dp[i] = max(dp[i + 1], jobs[i][2] + tail)
        return dp[0]



'''
compress DP

You are here!
Your memory usage beats 64.43 % of python3 submissions.

In [4]: [3, 7] < [4] < [4, 1]
Out[4]: True
'''

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[1])
        # [ends, total_profit]
        dp = [[0, 0]]
        for s, e, p in jobs:
            # bisect_right - 1
            index = bisect.bisect(dp, [s + 1]) - 1
            if dp[index][1] + p > dp[-1][1]:
                dp.append([e, dp[index][1] + p])
        
        return dp[-1][1]




