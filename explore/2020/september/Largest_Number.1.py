'''
You are here!
Your runtime beats 74.81 % of python submissions.
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums = sorted(nums, cmp = lambda a, b: cmp(b + a, a + b))
        if nums[0] == '0':
            return '0'

        return ''.join(nums)

if __name__ == '__main__':
	nums = [10,2]
	assert Solution().largestNumber(nums) == "210"

	nums = [3,30,34,5,9]
	assert Solution().largestNumber(nums) == "9534330"
