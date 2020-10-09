'''
You are here!
Your runtime beats 98.83 % of python submissions.
'''



class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(s.count(c) == t.count(c) for c in string.ascii_lowercase)   
        # just 26 letters versus solution in Valid_Anagram.1.py