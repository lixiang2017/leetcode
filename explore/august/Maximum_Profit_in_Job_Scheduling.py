'''
Sort + DP + Binary Search 
T: O(NlogN)
S: O(N)

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
            index = bisect.bisect_right(end, jobs[i][0]) - 1
            dp[i] = max(dp[i - 1], dp[index] + jobs[i][2])

        return dp[-1]