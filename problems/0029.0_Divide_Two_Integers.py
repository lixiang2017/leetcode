'''
bitwise

Runtime: 56 ms, faster than 27.91% of Python3 online submissions for Divide Two Integers.
Memory Usage: 13.8 MB, less than 76.13% of Python3 online submissions for Divide Two Integers.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        MIN, MAX = -(1 << 31), (1 << 31) - 1
        ans = 0
        dividend, divisor = abs(dividend), abs(divisor)
        min_d = divisor
        fold = 1
        while dividend >= divisor:
            divisor <<= 1
            fold <<= 1
        divisor >>= 1
        fold >>= 1
        while dividend >= min_d:
            if dividend >= divisor:
                dividend -= divisor
                ans += fold
            divisor >>= 1
            fold >>= 1
        
        if negative:
            ans = -ans
        if ans > MAX:
            return MAX
        if ans < MIN:
            return MIN
        return ans 
