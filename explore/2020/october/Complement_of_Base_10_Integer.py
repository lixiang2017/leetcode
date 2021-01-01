'''
You are here!
Your runtime beats 100.00 % of python submissions.
'''

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if 0 == N:
            return 1
        
        origin_N = N
        bits_counter = 0
        while N:
            N >>= 1
            bits_counter += 1
            
        print 'bits_counter: ', bits_counter
        return 2 ** bits_counter - origin_N - 1