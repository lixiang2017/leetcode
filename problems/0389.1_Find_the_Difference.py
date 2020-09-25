'''
Success
Details
Runtime: 24 ms, faster than 71.56% of Python online submissions for Find the Difference.
Memory Usage: 13.4 MB, less than 5.32% of Python online submissions for Find the Difference.
'''

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for char in t:
            if char not in s or t.count(char) > s.count(char):
                return char