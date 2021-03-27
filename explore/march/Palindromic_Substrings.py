'''
approach: Brute Force
Time: O(N^3)
Space: O(1)

You are here!
Your runtime beats 16.02 % of python submissions.
You are here!
Your memory usage beats 48.31 % of python submissions.
'''


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        cnt = 0
        for i in range(N):
            for j in range(i + 1, N + 1):
                if s[i: j] == s[i: j][:: -1]:
                    cnt += 1
        
        return cnt
