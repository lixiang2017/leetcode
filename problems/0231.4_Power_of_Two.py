'''
Runtime: 32 ms, faster than 69.55% of Python3 online submissions for Power of Two.
Memory Usage: 14.3 MB, less than 7.09% of Python3 online submissions for Power of Two.
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 0 == n & (n - 1)

'''
Runtime: 24 ms, faster than 96.97% of Python3 online submissions for Power of Two.
Memory Usage: 14.2 MB, less than 69.98% of Python3 online submissions for Power of Two.
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Counter(bin(n))['1'] == 1
        