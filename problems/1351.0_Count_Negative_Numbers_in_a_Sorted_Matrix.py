'''
T: O(M + N)
S: O(1)

Runtime: 134 ms, faster than 40.35% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 17.6 MB, less than 14.16% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = 0, n - 1
        ans = 0
        while i < m and j >= 0:
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            ans += n - j - 1
            i += 1
        ans += (m - i) * n
        return ans 


'''
bisect_right

Runtime: 129 ms, faster than 61.82% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 17.6 MB, less than 14.16% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 0
        for i, row in enumerate(grid):
            idx = bisect_right(row, 0, key=lambda x: -x)
            ans += n - idx
        return ans 


'''
bisect_left

Runtime: 138 ms, faster than 24.11% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 17.3 MB, less than 66.13% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 0
        for i, row in enumerate(grid):
            idx = bisect_left(row, 1, key=lambda x: -x)
            ans += n - idx
        return ans 


'''
zip(*grid)

Runtime: 127 ms, faster than 69.41% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 17.6 MB, less than 14.16% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        ans = 0
        for column in zip(*grid):
            idx = bisect_left(column, 1, key=lambda x: -x)
            ans += m - idx
        return ans 

'''
Runtime: 125 ms, faster than 75.89% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 17.5 MB, less than 44.05% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        ans = 0
        for column in zip(*grid):
            idx = bisect_right(column, 0, key=lambda x: -x)
            ans += m - idx
        return ans 

        