'''
approach: Binary Search
Time: O(NlogN)
Space: O(N)

执行用时：320 ms, 在所有 Python3 提交中击败了88.20% 的用户
内存消耗：26.8 MB, 在所有 Python3 提交中击败了69.94% 的用户
'''

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1_sort = sorted(nums1) # IndexError: list index out of range
        nums1_sort = sorted(nums1 + [10 ** 7])
        ans = sum(abs(n1 - n2) for n1, n2 in zip(nums1, nums2))
        MOD = 10 ** 9 + 7
        diff = 10 ** 7
        for n1, n2 in zip(nums1, nums2):
            idx = bisect.bisect_left(nums1_sort, n2)
            diff = min(diff, abs(nums1_sort[idx] - n2) - abs(n1 - n2), \
                abs(nums1_sort[idx - 1] - n2) - abs(n1 - n2))
        ans += diff
        return ans % MOD
