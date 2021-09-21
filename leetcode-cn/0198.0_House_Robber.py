'''
DP, T:O(N),S: O(1)

执行用时：20 ms, 在所有 Python3 提交中击败了99.49% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了99.46% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for x in nums:
            dp0, dp1 = max(dp0, dp1), max(dp0 + x, dp1)
        return max(dp0, dp1)



'''
执行用时：24 ms, 在所有 Python3 提交中击败了97.13% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了18.51% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for x in nums:
            dp0, dp1 = dp1, max(dp0 + x, dp1)
        return max(dp0, dp1)
        