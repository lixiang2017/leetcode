'''
Success
Details 
Runtime: 16 ms, faster than 83.07% of Python online submissions for Power of Four.
Memory Usage: 11.9 MB, less than 11.11% of Python online submissions for Power of Four.
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        while num > 1:
            remainder = num % 4
            if remainder != 0:
                return False
            else:    
                num = num / 4
        
        return True

if __name__ == "__main__":
    num = 16
    assert Solution().isPowerOfFour(num)

    num = 5
    assert not Solution().isPowerOfFour(num)

    num = 0
    assert not Solution().isPowerOfFour(num)
