'''
You are here!
Your runtime beats 96.99 % of python submissions.
'''



class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for element in (s + t):
            res ^= ord(element)
        return chr(res)