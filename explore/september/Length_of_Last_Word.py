'''
You are here!
Your runtime beats 84.49 % of python submissions.
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1]) if len(words) > 0 else 0