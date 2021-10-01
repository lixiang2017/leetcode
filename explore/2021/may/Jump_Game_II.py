'''
approach: DP
Time: O(N^2)
Space: O(N)

You are here!
Your runtime beats 88.50 % of python3 submissions.
You are here!
Your memory usage beats 79.51 % of python3 submissions.
'''


import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        # dp = [sys.maxsize] * N
        dp = [N + 5] * N
        dp[0] = 0
        for i in range(N):
            for step in range(1, nums[i] + 1):
                if i + step < N:
                    dp[i + step] = min(dp[i + step], dp[i] + 1)
                else:
                    break
        
        return dp[-1]
    
    