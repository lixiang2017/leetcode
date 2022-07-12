'''
执行用时：24 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了50.72% 的用户
通过测试用例：44 / 44
'''
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row, column = [0] * n, [0] * m
        for r, c in indices:
            column[r] += 1
            row[c] += 1
        odd1 = sum(r % 2 for r in row)
        even1 = n - odd1 
        odd2 = sum(c % 2 for c in column)
        even2 = m - odd2 
        return odd1 * even2 + even1 * odd2 
