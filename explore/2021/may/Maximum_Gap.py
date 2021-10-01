'''
Time: O(NlogN)
'''

import numpy
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        return 0 if len(nums) < 2 else int(max(numpy.diff(nums)))
        