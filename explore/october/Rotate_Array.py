'''
You are here!
Your runtime beats 75.74 % of python submissions
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        # print 'k: ', k
        # nums = nums[-k: ] + nums[: -k]   # Wrong Answer
        # print 'nums: ', nums
        nums[ : ] = nums[-k: ] + nums[ : -k]
        
        