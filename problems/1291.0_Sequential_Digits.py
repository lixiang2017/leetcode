'''
Runtime: 32 ms, faster than 62.30% of Python3 online submissions for Sequential Digits.
Memory Usage: 14.3 MB, less than 22.22% of Python3 online submissions for Sequential Digits.
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        enum = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789
        ]
        idx1 = bisect_left(enum, low)
        idx2 = bisect_right(enum, high)
        return enum[idx1: idx2]
        