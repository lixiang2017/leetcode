'''
执行用时：40 ms, 在所有 Python3 提交中击败了52.05% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了87.70% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(x for x in nums if x != 0))
        