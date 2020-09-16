'''
XOR : ^

You are here!
Your runtime beats 89.53 % of python submissions.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res = res ^ num
        return res
