'''
You are here!
Your runtime beats 90.96 % of python submissions.
'''


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        
        while s:
            i = min(map(s.rindex, set(s)))
            c = min(s[: i+1])
            res += c
            s = s[s.index(c) :].replace(c, '')
        
        return res