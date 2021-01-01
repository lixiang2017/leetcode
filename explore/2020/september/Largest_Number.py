'''
You are here!
Your runtime beats 88.30 % of python submissions.
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        compare = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums.sort(cmp = compare, reverse = True)
        return str(int(''.join(nums)))

if __name__ == '__main__':
	nums = [10,2]
	assert Solution().largestNumber(nums) == "210"

	nums = [3,30,34,5,9]
	assert Solution().largestNumber(nums) == "9534330"
