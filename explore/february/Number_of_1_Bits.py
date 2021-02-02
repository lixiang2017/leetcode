'''

You are here!
Your runtime beats 62.72 % of python submissions.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        print n
        # return str(n).count('1')  # wrong
        return bin(n).count('1')

'''
Your input
00000000000000000000000000001011
11111111111111111111111111111101
Your stdout
11
4294967293

Your answer
3
31
Expected answer
3
31
'''
