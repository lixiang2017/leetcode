'''
You are here!
Your runtime beats 91.09 % of python submissions.
'''


class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        left = []
        right = []
        factors = []
        i = 1
        while (i ** 2 < n):
            if n % i == 0:
                left.append(i)
                right.append(n / i)
            i += 1
        
        if i ** 2 == n:
            factors = left + [i] + right[:: -1]
        else:
            factors = left + right[:: -1]
        
        if len(factors) >= k:
            return factors[k - 1]
        
        return -1
    