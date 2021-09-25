'''
Binary Search

执行用时：32 ms, 在所有 Python3 提交中击败了76.03% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了7.36% 的用户
通过测试用例：88 / 88
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        if l == -1 or l == len(nums) or nums[l] != target:
            return [-1, -1]
        r = bisect_right(nums, target)
        return [l, r - 1]
