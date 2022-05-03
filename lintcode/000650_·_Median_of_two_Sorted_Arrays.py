'''
binary search
二分range, 二分数组中的最大值最小值区间，其实就是二分答案
T: O(log(range) * (logM + logN)), range is 2 * 10^6
S: O(1)

101 ms 时间消耗 ·
6.11 MB 空间消耗 ·
您的提交打败了 74.60 % 的提交
'''

from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param b: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        # write your code here
        m, n = len(nums1), len(nums2)
        c = m + n 
        k = c // 2
        if c % 2:
            return self.findkth(nums1, nums2, k + 1)
        else:
            small = self.findkth(nums1, nums2, k)
            big = self.findkth(nums1, nums2, k + 1)
            return (small + big) / 2

    def findkth(self, nums1, nums2, k):
        if 0 == len(nums1):
            return nums2[k - 1]
        if 0 == len(nums2):
            return nums1[k - 1]
        start = min(nums1[0], nums2[0])
        end = max(nums1[-1], nums2[-1])
        while start <= end:
            mid = (start + end) // 2
            k1 = self.countSmallerEqual(nums1, mid)
            k2 = self.countSmallerEqual(nums2, mid)
            if k1 + k2 < k:
                start = mid + 1
            else:
                # so many same numbers in nums1 or nums2, so need to use >= k for answer
                # answer = mid, so return end + 1
                end = mid - 1             
        return end + 1

    def countSmallerEqual(self, nums, x):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
        # index for [l-1], count l
        return l 

