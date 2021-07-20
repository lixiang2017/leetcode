'''
Sort
执行用时：276 ms, 在所有 Python3 提交中击败了92.21% 的用户
内存消耗：25.8 MB, 在所有 Python3 提交中击败了12.98% 的用户
'''
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mini = nums[0] + nums[-1]
        for i in range(1, len(nums) // 2):
            mini = max(mini, nums[i] + nums[len(nums) - i - 1])
        return mini
