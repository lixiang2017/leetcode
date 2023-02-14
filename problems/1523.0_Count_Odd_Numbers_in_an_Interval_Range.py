'''
math

Runtime: 32 ms, faster than 65.45% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 14 MB, less than 7.11% of Python3 online submissions for Count Odd Numbers in an Interval Range.
'''
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + int(low & 1 and high & 1)
        
