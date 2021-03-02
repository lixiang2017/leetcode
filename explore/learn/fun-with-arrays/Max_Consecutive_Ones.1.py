'''
You are here!
Your runtime beats 92.97 % of python submissions.
'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        strs = ''.join([str(num) for num in nums]).split('0')
        return max([len(one) for one in strs])
            