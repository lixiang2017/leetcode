'''
Time Limit ExceededDetails
Last executed input
0.00001
2147483647
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        isNegative = False
        if 0 == n:
            return 1.00000
        elif n < 0:
            n = -n
            isNegative = True

        res = 1.0
        while n:
            res *= x
            n -= 1
        
        return 1.0 / res if isNegative else res
        