'''
执行用时：56 ms, 在所有 Python3 提交中击败了94.57% 的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了71.64% 的用户
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        pre = 0
        for num in nums:
            pre = max(pre + num, num)
            maximum = max(maximum, pre)
        return maximum


'''
执行用时：60 ms, 在所有 Python3 提交中击败了90.07% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了48.62% 的用户
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)