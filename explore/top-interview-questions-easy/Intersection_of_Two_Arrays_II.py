'''
You are here!
Your runtime beats 69.30 % of python submissions.
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        
        common = []
        size1, size2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < size1 and j < size2:
            if nums1[i] == nums2[j]:
                common.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return common

