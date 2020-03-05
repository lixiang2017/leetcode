'''
Success
Details 
Runtime: 24 ms, faster than 27.54% of Python online submissions for Power of Four.
Memory Usage: 11.8 MB, less than 44.44% of Python online submissions for Power of Four.
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        if num & (num - 1) != 0:   # even number
            return False  
        
        return num % 3 == 1

if __name__ == "__main__":
    num = 16
    assert Solution().isPowerOfFour(num)

    num = 5
    assert not Solution().isPowerOfFour(num)

    num = 0
    assert not Solution().isPowerOfFour(num)
