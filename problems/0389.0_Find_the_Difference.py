'''
Success
Details
Runtime: 16 ms, faster than 97.61% of Python online submissions for Find the Difference.
Memory Usage: 13.7 MB, less than 5.32% of Python online submissions for Find the Difference.
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for element in s:
            res ^= ord(element)
        for element in t:
            res ^= ord(element)
        return chr(res)
