'''
执行用时：56 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：151 / 151
'''
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(operator.and_, map(set, nums)))
