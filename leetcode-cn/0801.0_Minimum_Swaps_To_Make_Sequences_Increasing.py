'''
DP
T: O(N)
S: O(1)

执行用时：276 ms, 在所有 Python3 提交中击败了69.42% 的用户
内存消耗：29.6 MB, 在所有 Python3 提交中击败了59.51% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a, b = 0, 1
        for i in range(1, n):
            at, bt = a, b 
            a = b = n 
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                a = min(a, at)
                b = min(b, bt + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                a = min(a, bt)
                b = min(b, at + 1)
        return min(a, b)

