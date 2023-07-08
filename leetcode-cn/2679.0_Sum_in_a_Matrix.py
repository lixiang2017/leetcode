'''
执行用时：88 ms, 在所有 Python3 提交中击败了97.37% 的用户
内存消耗：33.6 MB, 在所有 Python3 提交中击败了5.85% 的用户
通过测试用例：1057 / 1057
'''
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort(reverse=True)
        return sum(max(col) for col in zip(*nums))


'''
no need to reverse

执行用时：96 ms, 在所有 Python3 提交中击败了89.25% 的用户
内存消耗：33.6 MB, 在所有 Python3 提交中击败了8.36% 的用户
通过测试用例：1057 / 1057
'''
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        return sum(max(col) for col in zip(*nums))


'''
执行用时：120 ms, 在所有 Python3 提交中击败了64.40% 的用户
内存消耗：33.8 MB, 在所有 Python3 提交中击败了5.02% 的用户
通过测试用例：1057 / 1057
'''
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        return sum(map(max, zip(*map(sorted, nums))))
