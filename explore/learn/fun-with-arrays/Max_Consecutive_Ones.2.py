'''
You are here!
Your runtime beats 88.99 % of python submissions.
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(max(''.join(map(str, nums)).split('0')))
            