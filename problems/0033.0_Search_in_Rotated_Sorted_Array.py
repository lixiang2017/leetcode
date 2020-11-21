'''
Success
Details
Runtime: 28 ms, faster than 61.59% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.9 MB, less than 12.79% of Python online submissions for Search in Rotated Sorted Array.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        for i in range(size):
            if nums[i] == target:
                return i
        
        return -1