'''
mask

执行用时：48 ms, 在所有 Python3 提交中击败了32.35% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了44.12% 的用户
通过测试用例：288 / 288
'''
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        mask = [0] * 101
        for x in nums1:
            mask[x] |= 1
        for x in nums2:
            mask[x] |= 2
        for x in nums3:
            mask[x] |= 4
        return [i for i in range(101) if mask[i] in [3, 5, 6, 7]]
