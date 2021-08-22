'''
simulation, iteration
T: O(N)
S: O(N)

执行用时：32 ms, 在所有 Python3 提交中击败了74.57% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了22.86% 的用户
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        if n < 2:
            return nums[n]
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i//2] + nums[(i//2) + 1])
        return max(nums)
