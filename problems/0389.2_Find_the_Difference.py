'''
Success
Details
Runtime: 20 ms, faster than 86.79% of Python online submissions for Find the Difference.
Memory Usage: 13.6 MB, less than 5.32% of Python online submissions for Find the Difference.
'''



class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for char in (s + t):
            res ^= ord(char)
        return chr(res)