'''
Author: lixiang
Beats: 2.31%
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        if j >= 0:
            nums1[0 : j+1] = nums2[0: j+1]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1[:m+n] == [1, 2, 2, 3, 5, 6]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1[:m+n] == [1]

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1[:m + n] == [1, 2]

    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1[:m + n] == [1, 2, 3, 4, 5, 6]