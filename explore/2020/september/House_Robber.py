'''
You are here!
Your runtime beats 22.34 % of python submissions.
'''



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 == len(nums):
        	return 0
        elif 1 == len(nums):
        	return nums[0]
        elif 2 == len(nums):
        	return max(nums[0], nums[1])

        dp = [0] * 105
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
        	dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[len(nums) - 1]




if __name__ == '__main__':
	nums = [1,2,3,1]
	assert Solution().rob(nums) == 4
	# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	#             Total amount you can rob = 1 + 3 = 4.

	nums = [2,7,9,3,1]
	assert Solution().rob(nums) == 12
	# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
	#             Total amount you can rob = 2 + 9 + 1 = 12.

	nums = [5, 100, 5, 100, 5]
	assert Solution().rob(nums) == 200

	nums = [3, 50, 3, 3, 3, 3, 50]
	assert Solution().rob(nums) == 103

	nums = []
	assert Solution().rob(nums) == 0

	nums = [3]
	assert Solution().rob(nums) == 3

	nums = [3, 5]
	assert Solution().rob(nums) == 5

	nums = [3, 5, 1]
	assert Solution().rob(nums) == 5

	nums = [3, 5, 4]
	assert Solution().rob(nums) == 7
