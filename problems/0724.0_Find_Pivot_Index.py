'''
Success
Details 
Runtime: 116 ms, faster than 93.10% of Python online submissions for Find Pivot Index.
Memory Usage: 14.5 MB, less than 27.83% of Python online submissions for Find Pivot Index.
'''

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_sum = sum(nums)
        left_sum = 0
        i = 0
        for num in nums:
            right_sum = all_sum - left_sum - num
            if right_sum == left_sum:
                return i
            
            left_sum += num
            i += 1
        
        return -1