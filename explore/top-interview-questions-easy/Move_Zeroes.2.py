'''
You are here!
Your runtime beats 31.58 % of python submissions.

You are here!
Your runtime beats 77.88 % of python submissions.

You are here!
Your runtime beats 58.65 % of python submissions.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in xrange(len(nums)):
            if nums[j]:
                nums[i] = nums[j]
                i += 1
        
        for j in xrange(i, len(nums)):
            nums[j] = 0
