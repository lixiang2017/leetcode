'''
10 / 58 test cases passed.
Status: Time Limit Exceeded
Submitted: 2 minutes ago
Last executed input:
[[8,8,10,9,1,7],[8,8,1,8,4,7],[8,6,10,3,7,7],[3,0,9,3,2,7],[6,8,9,4,2,5],[1,1,5,8,8,1],[5,6,5,2,9,9],[4,4,6,2,5,4],[4,4,5,3,1,6],[9,2,2,1,9,3]]

'''


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
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
