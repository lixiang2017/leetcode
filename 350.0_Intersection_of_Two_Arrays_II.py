'''
Success
Details 
Runtime: 48 ms, faster than 31.31% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12 MB, less than 20.51% of Python online submissions for Intersection of Two Arrays II.
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = []
        for n in nums1:
            if n in nums2:
                common.append(n)
                # nums1.remove(n)   # n in nums1 should not be removed
                nums2.remove(n)

        return common


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert Solution().intersect(nums1, nums2) == [4, 9]
