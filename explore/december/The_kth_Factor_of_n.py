'''
You are here!
Your runtime beats 71.29 % of python submissions.
'''


class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) >= k:
                    return factors[-1]
        return -1
    