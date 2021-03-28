'''
执行用时：28 ms, 在所有 Python 提交中击败了14.86%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了33.13%的用户
'''


'''
In [22]: int('0b10111111111111111111111111111111', base=2)
Out[22]: 3221225471

In [23]: int('10111111111111111111111111111111', base=2)
Out[23]: 3221225471
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse = bin(n)[2:][:: -1]
        return int(reverse + (32 - len(reverse)) * '0', base=2)
