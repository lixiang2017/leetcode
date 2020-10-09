'''
You are here!
Your runtime beats 100.00 % of python submissions.

34 / 34 test cases passed.
    Status: Accepted
Runtime: 12 ms
Memory Usage: 14.2 MB
Submitted: 0 minutes ago
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return all(s.count(c) == t.count(c) for c in string.ascii_lowercase)