'''
分区

执行用时：28 ms, 在所有 Python3 提交中击败了97.46% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.37% 的用户
通过测试用例：87 / 87
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = p2 = 0
        for i, x in enumerate(nums):
            if x == 0:
                nums[p2] = 2; p2 += 1
                nums[p1] = 1; p1 += 1
                nums[p0] = 0; p0 += 1
            elif x == 1:
                nums[p2] = 2; p2 += 1
                nums[p1] = 1; p1 += 1
            else:
                nums[p2] = 2; p2 += 1
            