'''
You are here!
Your runtime beats 90.07 % of python submissions.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = [0] * len(nums)
        maximum = nums[0]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = (dp[i - 1] + nums[i]) if dp[i - 1] > 0 else nums[i]
            #if dp[i - 1] > 0:
            #    dp[i] = dp[i - 1] + nums[i]
            #else:
            #    dp[i] = nums[i]
            
            maximum = max(maximum, dp[i])
            
        return maximum
        
if __name__ == '__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	assert Solution().maxSubArray(nums) == 6
	# Explanation: [4,-1,2,1] has the largest sum = 6.

	nums = [1]
	assert Solution().maxSubArray(nums) == 1

	nums = [0]
	assert Solution().maxSubArray(nums) == 0

	nums = [-1]
	assert Solution().maxSubArray(nums) == -1

	nums = [-2147483647]
	assert Solution().maxSubArray(nums) == -2147483647
