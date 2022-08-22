'''
Runtime: 46 ms, faster than 63.84% of Python3 online submissions for Power of Four.
Memory Usage: 13.9 MB, less than 10.18% of Python3 online submissions for Power of Four.
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and len(bin(n)) & 1
