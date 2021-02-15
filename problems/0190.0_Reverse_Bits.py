'''
approach: Bit Manipulation
Time: O(32) = O(1)
Space: O(1)

ref:
https://leetcode.com/problems/reverse-bits/solution/

Runtime: 20 ms, faster than 61.04% of Python online submissions for Reverse Bits.
Memory Usage: 13.7 MB, less than 12.66% of Python online submissions for Reverse Bits.
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse, power = 0, 31
        while n:
            reverse += (n & 1) << power
            n >>= 1
            power -= 1
        
        return reverse
    