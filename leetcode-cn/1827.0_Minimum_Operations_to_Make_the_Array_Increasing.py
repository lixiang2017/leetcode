'''
执行用时：56 ms, 在所有 Python3 提交中击败了48.76% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了91.32% 的用户
通过测试用例：94 / 94
'''
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nxt = nums[0] + 1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] < nxt:
                ans += nxt - nums[i]
                nxt += 1
            else:
                nxt = nums[i] + 1
        return ans 