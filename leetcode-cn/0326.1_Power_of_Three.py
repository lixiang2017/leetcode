'''
Approach #1: Loop Iteration
Time: O(logN)
Space: O(1)

Success
Details 
Runtime: 64 ms, faster than 81.29% of Python online submissions for Power of Three.
Memory Usage: 13.3 MB, less than 91.96% of Python online submissions for Power of Three.
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        
        while 0 == n % 3:
            n /= 3
        
        return 1 == n
    