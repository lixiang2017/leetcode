'''
Success
Details 
Runtime: 64 ms, faster than 79.16% of Python online submissions for Power of Three.
Memory Usage: 11.8 MB, less than 42.86% of Python online submissions for Power of Three.
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n > 1:
            remainder = n % 3
            if remainder != 0:
                return False
            else:    
                n = n / 3 # quotient

        return True

if __name__ == "__main__":
    n = 27
    assert Solution().isPowerOfThree(n)

    n = 0
    assert not Solution().isPowerOfThree(n)

    n = 9
    assert Solution().isPowerOfThree(n)

    n = 45
    assert not Solution().isPowerOfThree(n)
    