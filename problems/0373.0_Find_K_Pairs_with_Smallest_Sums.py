'''
k * k

执行用时：720 ms, 在所有 Python3 提交中击败了25.66% 的用户
内存消耗：118.1 MB, 在所有 Python3 提交中击败了16.39% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # ks = nsmallest(k, [(x + y, x, y) for x in nums1 for y in nums2])
        ks = nsmallest(k, [(nums1[i] + nums2[j], nums1[i], nums2[j]) \
            for i in range(min(k, len(nums1))) for j in range(min(k, len(nums2)))])
        return [[x, y]for _sum, x, y in ks]
