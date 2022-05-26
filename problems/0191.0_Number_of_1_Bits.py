class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return format(n, 'b').count('1')


'''
Runtime: 32 ms, faster than 87.55% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.9 MB, less than 7.92% of Python3 online submissions for Number of 1 Bits.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        