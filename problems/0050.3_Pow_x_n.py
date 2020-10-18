'''
Success
Details
Runtime: 12 ms, faster than 97.02% of Python online submissions for Pow(x, n).
Memory Usage: 13.7 MB, less than 8.16% of Python online submissions for Pow(x, n).
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return pow(x, n)
        
        # recursive
        if not n:
            return 1  
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
        