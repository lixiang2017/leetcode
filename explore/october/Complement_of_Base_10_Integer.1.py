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
        binary = bin(N)
        binary = binary[2:]  # to strip the leading '0b' in binary
        binary = list(binary)
        for i in xrange(len(binary)):
            if '1' == binary[i]:
                binary[i] = '0'
            else:
                binary[i] = '1'

        return int(''.join(binary), 2)