'''
执行用时：44 ms, 在所有 Python3 提交中击败了55.42% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.42% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        nums.sort(key=lambda x: x == 0)
        return nums 
        