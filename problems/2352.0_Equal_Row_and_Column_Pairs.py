'''
Runtime: 515 ms, faster than 58.65% of Python3 online submissions for Equal Row and Column Pairs.
Memory Usage: 21.9 MB, less than 26.88% of Python3 online submissions for Equal Row and Column Pairs.
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = Counter()
        for row in grid:
            row_counter[tuple(row)] += 1
        ans = 0
        for col in zip(*grid):
            ans += row_counter[tuple(col)]
        return ans 
        