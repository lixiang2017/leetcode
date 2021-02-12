'''
approach: Sort
Time: O(NlogN + MlogM)
Space: O(1)

You are here!
Your runtime beats 52.05 % of python submissions.
You are here!
Your memory usage beats 23.88 % of python submissions.
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s)) == sorted(list(t))
    