'''
42 / 42 个通过测试用例
状态：通过
执行用时: 256 ms
内存消耗: 33.2 MB
提交时间：11 小时前
'''

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(chain(*grid))
        L = len(nums)
        mid = nums[L // 2]
        ans = 0
        for num in nums:
            ops, remainder = divmod(abs(num - mid), x)
            if remainder:
                return -1
            ans += ops
        return ans

