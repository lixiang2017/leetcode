'''
approach #2: Dynamic Programming(Bottom Up)

You are here!
Your memory usage beats 73.86 % of python submissions.
'''

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        dp = [[[0] * n for _ in range(n)] for __ in range(m)]
        # (row, col1, col2):
        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    # current cell
                    result = 0
                    result += grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]
                    # transition
                    if row != m - 1:
                        result += max(dp[row + 1][new_col1][new_col2] \
                                     for new_col1 in [col1, col1 + 1, col1 -1] \
                                     for new_col2 in [col2, col2 + 1, col2 - 1] \
                        if 0 <= new_col1 < n and 0 <= new_col2 < n)
                    dp[row][col1][col2] = result
            
        return dp[0][0][n - 1]
