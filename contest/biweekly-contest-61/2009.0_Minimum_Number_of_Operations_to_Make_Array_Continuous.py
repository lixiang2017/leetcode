'''
AC
'''
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        distinct = sorted(set(nums))
        L = len(distinct)
        max_in = 0
        for i, left in enumerate(distinct):
            right = left + N - 1
            idx = bisect_right(distinct, right)
            max_in = max(max_in, idx - i)
        return N - max_in
        
