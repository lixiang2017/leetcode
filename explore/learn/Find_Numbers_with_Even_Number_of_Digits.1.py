'''
You are here!
Your runtime beats 10.90 % of python submissions.
'''

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([(len(str(num)) & 1) == 0 for num in nums])
        