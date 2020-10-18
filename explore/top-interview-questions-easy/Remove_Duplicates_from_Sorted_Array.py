'''
You are here!
Your runtime beats 96.18 % of python submissions.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # if len(nums) == 1:
        #     return 1
        
        size = len(nums)
        i, j = 0, 0
        while i < size and j < size:
            before = nums[j]
            while j < size and nums[j] == before:
                j += 1
            i += 1
            if i < size and j < size:
                nums[i] = nums[j]
        return i
        