'''
Runtime: 50 ms, faster than 34.24% of Python3 online submissions for Add Digits.
Memory Usage: 13.8 MB, less than 91.66% of Python3 online submissions for Add Digits.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            t = 0
            while num:
                t += (num % 10)
                num //= 10
            num = t
        return num
        