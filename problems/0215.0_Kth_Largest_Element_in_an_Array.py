'''
Success
Details 
Runtime: 36 ms, faster than 99.71% of Python online submissions for Kth Largest Element in an Array.
Memory Usage: 14.2 MB, less than 84.21% of Python online submissions for Kth Largest Element in an Array.


'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]
