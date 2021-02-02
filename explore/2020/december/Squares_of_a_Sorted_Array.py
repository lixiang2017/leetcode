'''
You are here!
Your runtime beats 99.74 % of python submissions.
'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([num * num for num in nums])
