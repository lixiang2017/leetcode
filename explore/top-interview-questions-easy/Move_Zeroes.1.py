'''
You are here!
Your runtime beats 77.88 % of python submissions.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        size = len(nums)
        j = 0
        for i in xrange(size):
            if nums[i] == 0:
                # j = i  # [1, 0]
                j = max(i, j)
                while j < size and nums[j] == 0:
                    j += 1
                if j == size:
                    break
                nums[i] = nums[j]
                nums[j] = 0
