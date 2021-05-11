'''
approach: Bit Manipulation(left shift)
Time: O(log(dividend / divisor))
Space: O(1)

You are here!
Your runtime beats 98.70 % of python submissions.
You are here!
Your memory usage beats 69.11 % of python submissions.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        isNegative = False
        if dividend < 0:
            isNegative = 1 - isNegative
            dividend = -dividend
        if divisor < 0:
            isNegative = 1 - isNegative
            divisor = -divisor
        
        shift = 0
        while dividend >= (divisor << shift):
            shift += 1
        shift -= 1
        
        while dividend >= divisor and shift >= 0:
            while dividend >= (divisor << shift):
                dividend -= (divisor << shift)
                quotient += (1 << shift)
            shift -= 1
        
        quotient = -quotient if isNegative else quotient
        return 2147483647 if quotient < -2147483648 or quotient > 2147483647 else quotient

'''
Input:
-2147483648
-1
Output:
2147483648
Expected:
2147483647

returns 2^31 − 1 when the division result overflows
[−2^31,  2^31 − 1]
[-2147483648, 2147483647]
'''

