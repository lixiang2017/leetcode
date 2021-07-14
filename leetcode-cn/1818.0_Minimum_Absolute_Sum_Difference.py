'''
执行结果：
解答错误
显示详情

添加备注
输入：
[1,28,21]
[9,21,20]
输出：
16
预期结果：
9
'''
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max_diff_idx = sum_diff = 0
        for i, diff in enumerate(diffs):
            sum_diff += diff
            if diff > max_diff:
                max_diff = diff
                max_diff_idx = i
        
        min_diff = min(abs(n1 - nums2[max_diff_idx]) for n1 in nums1)
        return (sum_diff - max_diff + min_diff) % MOD




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
