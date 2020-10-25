'''
Success
Details 
Runtime: 220 ms, faster than 80.47% of Python online submissions for Maximum Product of Three Numbers.
Memory Usage: 14.6 MB, less than 31.05% of Python online submissions for Maximum Product of Three Numbers.
'''


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
                      # + + +                       # - - +  / - - 0
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])     