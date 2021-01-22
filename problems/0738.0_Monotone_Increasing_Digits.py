'''
208 / 302 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
963856657
'''

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        while N:
            if self.isMonotone(N):
                return N
            else:
                N -= 1
    
    def isMonotone(self, num):
        """
        :type num: int
        :rtype: bool
        """

        pre_digit = num % 10
        num = num / 10
        while num:
            digit = num % 10
            if digit > pre_digit:
                return False
            num /= 10
            pre_digit = digit
        
        return True
            