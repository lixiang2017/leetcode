'''
216 / 216 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 15.1 MB
提交时间：13 小时前
'''
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, x in enumerate(nums) if x == target]
