'''
执行用时：152 ms, 在所有 Python3 提交中击败了41.89% 的用户
内存消耗：28.6 MB, 在所有 Python3 提交中击败了29.73% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        presum = list(accumulate(nums, initial=0))
        ans = pre_min = pre_max = 0
        for s in presum:
            ans = max(ans, abs(s - pre_min), abs(s - pre_max))
            pre_min = min(s, pre_min)
            pre_max = max(s, pre_max)
        return ans 


'''
执行用时：80 ms, 在所有 Python3 提交中击败了87.84% 的用户
内存消耗：28.7 MB, 在所有 Python3 提交中击败了28.38% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        presum = list(accumulate(nums, initial=0))
        return max(presum) - min(presum)
        