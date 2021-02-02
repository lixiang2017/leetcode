'''
58 / 58 test cases passed.
Status: Accepted
Runtime: 808 ms
Memory Usage: 31.3 MB
Submitted: 1 minute ago

use functools.lru_cache in python3

approach #1: Dynamic Programming (Top Down)

two similar approaches: Dynamic Programming(Top Down) and Dynamic Programming(Bottom Up).
The first one is also known as dfs with memoization or memoization dp, and the second one is 
also known as tabulation dp. They have the same main idea but different coding approaches.
'''



class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        @lru_cache(None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return -float('inf')
            # current cell
            result = 0
            result += grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            # transition
            if row != m - 1:
                result += max(dp(row + 1, new_col1, new_col2) \
                             for new_col1 in [col1, col1 + 1, col1 -1] \
                             for new_col2 in [col2, col2 + 1, col2 - 1])
            
            return result
        
        return dp(0, 0, n - 1)
