'''
You are here!
Your runtime beats 86.79 % of python submissions.
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # sum_s, sum_t = 0, 0
        sum_s = sum([ord(element) for element in s])
        sum_t = sum([ord(element) for element in t])
        return chr(sum_t - sum_s)



