'''
Time: O(N)
Space :O(1)

You are here!
Your runtime beats 8.17 % of python submissions.
You are here!
Your memory usage beats 92.33 % of python submissions.
'''

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        return sum(self.isVowel(ch)for ch in s[: N / 2]) == sum(self.isVowel(ch)for ch in s[N / 2:])
    
    def isVowel(self, ch):
        return ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
