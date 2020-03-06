'''
use two dicts to create two counters
Success
Details 
Runtime: 32 ms, faster than 84.34% of Python online submissions for Intersection of Two Arrays II.
Memory Usage: 12.2 MB, less than 5.13% of Python online submissions for Intersection of Two Arrays II.
'''


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        count1, count2 = {}, {}

        for e in nums1:
            count1[e] = count1.get(e, 0) + 1

        for e in nums2:
            count2[e] = count2.get(e, 0) + 1

        for e in nums1:
            res.extend(min(count1.pop(e, 0), count2.pop(e, 0)) * [e])

        return res


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print Solution().intersect(nums1, nums2)
    # assert Solution().intersect(nums1, nums2) == [4, 9]
