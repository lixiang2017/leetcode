'''
two pointers
Success
Details 
Runtime: 36 ms, faster than 63.17% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 11.8 MB, less than 71.79% of Python online submissions for Intersection of Two Arrays II.
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1, pt2 = 0, 0

        while True:
            try:
                if nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                elif nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert Solution().intersect(nums1, nums2) == [4, 9]
