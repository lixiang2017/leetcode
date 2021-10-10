'''
Runtime: 56 ms, faster than 82.71% of Python3 online submissions for Bitwise AND of Numbers Range.
Memory Usage: 14.3 MB, less than 23.30% of Python3 online submissions for Bitwise AND of Numbers Range.
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1
        return right
        