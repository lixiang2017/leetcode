'''
sort 

执行用时：44 ms, 在所有 Python3 提交中击败了65.45% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了90.91% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        i, n = 0, len(nums)
        got_sum = 0
        while i < n and got_sum <= total - got_sum:
            got_sum += nums[i]
            i += 1
        return nums[: i]
