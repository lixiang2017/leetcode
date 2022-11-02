'''
simulation

Runtime: 497 ms, faster than 38.77% of Python3 online submissions for Where Will the Ball Fall.
Memory Usage: 14.2 MB, less than 84.52% of Python3 online submissions for Where Will the Ball Fall.
'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n
        for b in range(n):
            col = b
            stuck = False
            for r in range(m):
                if grid[r][col] == 1: # \
                    # stuck
                    if col == n - 1 or grid[r][col + 1] == -1:
                        stuck = True
                        break
                    else:
                        col += 1
                else: # /
                    # stuck
                    if col == 0 or grid[r][col - 1] == 1:
                        stuck = True
                        break
                    else:
                        col -= 1
            if not stuck:
                ans[b] = col
        
        return ans 
        
