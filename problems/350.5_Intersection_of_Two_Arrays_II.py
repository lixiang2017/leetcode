'''
use collections.Counter and map
Success
Details 
Runtime: 36 ms, faster than 63.55% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12.1 MB, less than 5.13% of Python online submissions for Intersection of Two Arrays II.
'''

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1, c2 = map(collections.Counter, (nums1, nums2))
        return list((c1 & c2).elements())        


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print Solution().intersect(nums1, nums2)
    # assert Solution().intersect(nums1, nums2) == [4, 9]
