'''
Runtime: 124 ms, faster than 96.64% of Python3 online submissions for Single Number.
Memory Usage: 16.7 MB, less than 26.15% of Python3 online submissions for Single Number.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)
        