'''
approach: Loop / Iteration


You are here!
Your runtime beats 77.32 % of python submissions.
You are here!
Your memory usage beats 68.65 % of python submissions.
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1 and n % 3 == 0:
            n /= 3
        return 1 == n
        