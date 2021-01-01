'''
You are here!
Your runtime beats 82.05 % of python submissions.

https://leetcode.com/problems/smallest-integer-divisible-by-k/solution/

https://blog.csdn.net/fuxuemingzhu/article/details/88778532

1、N1 % K == N2 % k   <==>/等价于     (10 * N1 + 1) % K == (10 * N + 1) % K
2、余数会循环，N的长度不会超过K位。
'''



class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K < 0 or K % 2 == 0 or K % 5 == 0: return -1
        
        remainder = 0
        seen_remainder = set()
        
        for lengthofN in range(1, K + 1):
            remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return lengthofN
            elif remainder in seen_remainder:
                return -1
            else: # not in seen_remainder
                seen_remainder.add(remainder)
            
        # return -1 # no use