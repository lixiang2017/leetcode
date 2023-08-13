'''
approach: Two Pointers / Three Pointers
Time: O(M + N)
Space: O(1)

执行用时：16 ms, 在所有 Python 提交中击败了87.04% 的用户
内存消耗：13 MB, 在所有 Python 提交中击败了52.12% 的用户
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # move n steps backwards
        nums1[n: m + n] = nums1[:m]
        ptr, ptr1, ptr2 = 0, n, 0
        while ptr1 < m + n and ptr2 < n:
            if nums1[ptr1] < nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 += 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 += 1
            ptr += 1
        # left numbers in nums2
        if ptr2 < n:
            nums1[ptr:] = nums2[ptr2:]


'''
时间 40ms 击败 78.94%使用 Python3 的用户
内存 15.69mb 击败 57.09%使用 Python3 的用户
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1


