'''
执行用时：3600 ms, 在所有 Python3 提交中击败了20.65% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了61.52% 的用户
通过测试用例：71 / 71
'''
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 1):
            minx = maxx = nums[i]
            for j in range(i + 1, n):
                minx = min(minx, nums[j])
                maxx = max(maxx, nums[j])
                ans += maxx - minx
        return ans 

