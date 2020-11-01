'''
Success
Details 
Runtime: 36 ms, faster than 100.00% of Python online submissions for Sort Array by Increasing Frequency.
Memory Usage: 13.3 MB, less than 100.00% of Python online submissions for Sort Array by Increasing Frequency.
'''

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return sorted(nums, key = lambda x: (count[x], -x))
        