'''
You are here!
Your runtime beats 78.69 % of python submissions.
'''



class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # binary = bin(N)
        # binary = binary[2:]  # to strip the leading '0b' in binary
        # binary = list(binary)
        binary = list(bin(N)[2:])   # combine three lines of code above into one line
        for i in xrange(len(binary)):
            if '1' == binary[i]:
                binary[i] = '0'
            else:
                binary[i] = '1'

        return int(''.join(binary), 2)