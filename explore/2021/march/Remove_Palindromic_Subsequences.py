'''
approach: Brainteaser

You are here!
Your runtime beats 71.84 % of python submissions.
You are here!
Your memory usage beats 33.01 % of python submissions.
'''

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if '' == s:
            return 0
        elif s == s[:: -1]:
            return 1
        else:
            return 2
        

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if '' == s else 1 if s == s[:: -1] else 2
        