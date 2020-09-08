'''
Success
Details
Runtime: 140 ms, faster than 98.62% of Python online submissions for Majority Element.
Memory Usage: 14.1 MB, less than 93.16% of Python online submissions for Majority Element.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]



if __name__ == '__main__':
	nums = [3,2,3]
	assert Solution().majorityElement(nums) == 3

	nums = [2,2,1,1,1,2,2]
	assert Solution().majorityElement(nums) == 2
