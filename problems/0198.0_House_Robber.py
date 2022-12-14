'''
DP
T: O(N)
S: O(1)

Runtime: 32 ms, faster than 70.60% of Python3 online submissions for House Robber.
Memory Usage: 14.3 MB, less than 52.92% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        r = not_r = 0
        for x in nums:
            r, not_r = not_r + x, max(r, not_r)
        return max(r, not_r)
            

'''
DP
T: O(N)
S: O(N)

Runtime: 37 ms, faster than 85.04% of Python3 online submissions for House Robber.
Memory Usage: 13.8 MB, less than 97.62% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0, dp1 = [0] * n, [0] * n
        dp1[0] = nums[0]
        for i in range(1, n):
            dp0[i] = max(dp0[i - 1], dp1[i - 1])
            dp1[i] = dp0[i - 1] + nums[i]
        return max(dp0[-1], dp1[-1])
        
