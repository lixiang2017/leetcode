'''
wrapper the robbery action into a rob function for repetition

You are here!
Your runtime beats 65.79 % of python submissions.
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def rob(array):
            first, sec = 0, 0
            for current in array:
                first, sec = sec, max(first + current, sec)
            return sec
        
        return max(rob(nums[1: ]), rob(nums[: -1]))