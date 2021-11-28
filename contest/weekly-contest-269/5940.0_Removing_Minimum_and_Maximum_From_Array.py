'''
60 / 60 个通过测试用例
状态：通过
执行用时: 104 ms
内存消耗: 25.1 MB
提交时间：13 小时前
'''
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        maxidx = minidx = 0
        maxv = minv = nums[0]
        for i, x in enumerate(nums):
            if x > maxv:
                maxv = x
                maxidx = i
            if x < minv:
                minv = x
                minidx = i
        return min(
            max(minidx, maxidx) + 1,
            n - min(minidx, maxidx),
            min(minidx, maxidx) + 1 + n - max(minidx, maxidx)
        )

