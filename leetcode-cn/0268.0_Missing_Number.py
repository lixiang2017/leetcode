'''
执行用时：44 ms, 在所有 Python3 提交中击败了51.35% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了57.93% 的用户
通过测试用例：122 / 122
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2  - sum(nums)
        