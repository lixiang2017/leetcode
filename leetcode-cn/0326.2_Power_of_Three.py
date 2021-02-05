'''
approach: Integer Limitations
Time:O(1)
Space: O(1)

Success
Details 
Runtime: 64 ms, faster than 81.29% of Python online submissions for Power of Three.
Memory Usage: 13.5 MB, less than 15.81% of Python online submissions for Power of Three.
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** 39 % n == 0
    