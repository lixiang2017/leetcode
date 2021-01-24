'''
Time: O(M + N)
Space: O(M + N)

Details 
Runtime: 164 ms, faster than 5.04% of Python online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.5 MB, less than 79.17% of Python online submissions for Median of Two Sorted Arrays.
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m , n = len(nums1), len(nums2)
        nums = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
        if i < m:
            nums += nums1[i: ]
        if j < n:
            nums += nums2[j: ]
        
        if (m + n) & 1: # odd
            return nums[(m + n) / 2]
        else:
            return (nums[(m + n) / 2 - 1] + nums[(m + n) / 2]) / 2.0
            
        