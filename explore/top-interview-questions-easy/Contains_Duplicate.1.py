'''
You are here!
Your runtime beats 16.30 % of python submissions.

You are here!
Your runtime beats 54.55 % of python submissions.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False

