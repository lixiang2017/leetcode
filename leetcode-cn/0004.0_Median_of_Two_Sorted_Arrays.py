'''
执行用时：44 ms, 在所有 Python3 提交中击败了73.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了96.19% 的用户
通过测试用例：2094 / 2094
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        N = len(nums)
        if N % 2:
            return nums[N // 2]
        else:
            return (nums[N // 2] + nums[N//2 - 1]) / 2

'''
执行用时：40 ms, 在所有 Python3 提交中击败了85.87% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了14.72% 的用户
通过测试用例：2094 / 2094
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        i = j = 0
        nums = []
        while i < M and j < N:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < M:
            nums.extend(nums1[i:])
        if j < N:
            nums.extend(nums2[j:])
        L = M + N 
        if L % 2:
            return nums[L // 2]
        else:
            return (nums[L//2 - 1] + nums[L//2]) / 2
