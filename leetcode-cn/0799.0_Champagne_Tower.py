'''
simulation for iteration, T: O(N^2), S: O(N)

执行用时：200 ms, 在所有 Python3 提交中击败了11.86% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了57.06% 的用户
通过测试用例：312 / 312
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(query_row):
            next_row = []
            for left, right in pairwise([0] + row + [0]):
                next_row.append((max(left - 1, 0) + max(right - 1, 0)) / 2)
            row = next_row
        return min(1.0, row[query_glass])
