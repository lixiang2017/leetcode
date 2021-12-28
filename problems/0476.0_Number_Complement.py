'''
Runtime: 28 ms, faster than 81.72% of Python3 online submissions for Number Complement.
Memory Usage: 14.3 MB, less than 7.36% of Python3 online submissions for Number Complement.
'''
class Solution:
    def findComplement(self, num: int) -> int:
        bit_len = 0
        num1 = num
        while num:
            bit_len += 1
            num >>= 1
        return (1 << bit_len) - num1 - 1
        