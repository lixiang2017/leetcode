'''
approach: Math
Time: O(1)
Space: O(1)

You are here!
Your runtime beats 83.49 % of python submissions.
You are here!
Your memory usage beats 48.62 % of python submissions.
'''

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n * n - 1) / 4 if n & 1 else n * n / 4
