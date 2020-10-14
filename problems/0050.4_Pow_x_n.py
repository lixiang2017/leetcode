'''
Success
Details
Runtime: 20 ms, faster than 61.29% of Python online submissions for Pow(x, n).
Memory Usage: 13.6 MB, less than 8.16% of Python online submissions for Pow(x, n).
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return pow(x, n)
        
        '''
        # recursive
        if not n:
            return 1  
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)
        '''
        
        # iterative
        if n < 0:
            n = -n
            x = 1 / x
        
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        
        return pow
    
            
        