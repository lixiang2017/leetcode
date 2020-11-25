'''
Success
Details
Runtime: 36 ms, faster than 84.62% of Python online submissions for Smallest Integer Divisible by K.
Memory Usage: 18 MB, less than 5.13% of Python online submissions for Smallest Integer Divisible by K.
'''


class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        # Goal: Find multiple of K that is all ones (ex: 11...111)
        
        if K <= 0: # invalid input
            return -1
        if K % 2 == 0: # even number multiples never ends with 1
            return -1
        if K % 5 == 0: # 5 multiples never ends with 1
            return -1
        
        # get remainder of N / k
        # add 1 to N (so it ends in 1)
        # repeat
        seen_remainder = set()
        remainder = 0
        for lengthofN in range(1, K + 1):
            remainder = (10 * remainder + 1) % K
            if remainder == 0:
                return lengthofN
            elif remainder in seen_remainder:
                return -1
            else:
                seen_remainder.add(remainder)
                