'''
AC

118 / 118 个通过测试用例
状态：通过
执行用时: 44 ms
内存消耗: 14.9 MB
提交时间：3 小时前
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if 1== k:
            return 0
        
        nums.sort()
        N = len(nums)
        minn = float('inf')
        for i in range(N - k + 1):
            minn = min(minn, nums[i + k - 1] - nums[i])
        return minn

