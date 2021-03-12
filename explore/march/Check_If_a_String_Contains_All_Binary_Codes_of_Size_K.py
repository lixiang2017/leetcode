'''
approach: Hash Set
Time: O(N)
Space: O(2 ^ k)

You are here!
Your memory usage beats 70.83 % of python submissions.
'''


class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        N = len(s)
        if N < 2 ** k:
            return False
        
        seen = set()
        for i in range(0, N - k + 1):
            seen.add(s[i: i + k])
        
        if len(seen) == 2 ** k:
            return True
        else:
            return False
        