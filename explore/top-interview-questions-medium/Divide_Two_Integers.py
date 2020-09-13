'''
Time Limit Exceeded
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0:
            dividend = - dividend
            sign = - sign
        if divisor < 0:
            divisor = - divisor
            sign = - sign
        
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        
        if sign < 0:
            quotient = - quotient
        
        return quotient
            



if __name__ == '__main__':
	dividend = 10
	divisor = 3
	print Solution().divide(dividend, divisor)
	assert Solution().divide(dividend, divisor) == 3

	dividend = 1
	divisor = 1
	print Solution().divide(dividend, divisor)
	assert Solution().divide(dividend, divisor) == 1

	dividend = -2147483648
	divisor = -1
	print Solution().divide(dividend, divisor)
	assert Solution().divide(dividend, divisor) == 2147483648