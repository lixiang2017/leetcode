'''
You are here!
Your runtime beats 93.44 % of python submissions.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target in nums:
            return True
        else:
            return False
