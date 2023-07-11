'''
DP
T: O(N)
S: O(1)

执行用时：980 ms, 在所有 Python3 提交中击败了87.57% 的用户
内存消耗：30.3 MB, 在所有 Python3 提交中击败了51.41% 的用户
通过测试用例：65 / 65
'''
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            x = nums[i]
            dp0, dp1 = max(dp0, dp1 - x), max(dp1, dp0 + x)
        return max(dp0,  dp1)
