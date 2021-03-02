'''
You are here!
Your runtime beats 31.14 % of python submissions.
'''


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if not (len(str(num)) & 1):
                count += 1
        return count
        
        