'''
34 / 34 test cases passed.
    Status: Accepted
Runtime: 4000 ms
Memory Usage: 14.3 MB
    
Submitted: 0 minutes ago

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(s) == len(t) and all(s.count(c) == t.count(c) for c in s)