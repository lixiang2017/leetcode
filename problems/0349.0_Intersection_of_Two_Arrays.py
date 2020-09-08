'''
Success
Details 
Runtime: 56 ms, faster than 17.64% of Python online submissions for Intersection of Two Arrays.
Memory Usage: 11.9 MB, less than 69.44% of Python online submissions for Intersection of Two Arrays.

O(n ^ 2 + ...)
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = []
        for n in nums1:
            if n in nums2:
                common.append(n)
        
        return list(set(common))

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print Solution().intersection(nums1, nums2)  # [2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print Solution().intersection(nums1, nums2)  # [9,4]
