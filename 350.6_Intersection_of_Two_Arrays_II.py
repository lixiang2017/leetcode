'''
use collections.Counter and map # variations
Success
Details 
Runtime: 32 ms, faster than 84.34% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 11.9 MB, less than 25.64% of Python online submissions for Intersection of Two Arrays II.
'''

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        C = collections.Counter
        return list((C(nums1) & C(nums2)).elements())        


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print Solution().intersect(nums1, nums2)
    # assert Solution().intersect(nums1, nums2) == [4, 9]
