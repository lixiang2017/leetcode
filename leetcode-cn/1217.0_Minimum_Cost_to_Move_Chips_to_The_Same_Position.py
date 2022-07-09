'''
执行用时：40 ms, 在所有 Python3 提交中击败了41.77% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.99% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n = len(position)
        odd = sum(p & 1 for p in position)
        return min(odd, n - odd)
