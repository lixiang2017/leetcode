'''
You are here!
Your runtime beats 99.86 % of python submissions.
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        n = len(nums)
        dp1 = [0] * n
        dp2 = [0] * n
        # house 1 to n-1 ---->  i from 0 to n-2
        dp1[0] = nums[0]
        dp1[1] = max(dp1[0], nums[1])
        # dp1[2] = max(dp1[1], dp1[0] + nums[2])
        # dp1[3] = max(dp1[2], dp1[1] + nums[3])
        for i in xrange(2, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        
        # house 2 to n  ---->   i from 1 to n-1
        dp2[1] = nums[1]
        dp2[2] = max(dp2[1], nums[2])
        # dp2[3] = max(dp2[2], dp2[1] + nums[3])
        for i in xrange(3, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        
        return max(dp1[n - 2], dp2[n - 1])
        