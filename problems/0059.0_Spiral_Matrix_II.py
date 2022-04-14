'''
simulation, one by one

T: O(N^2)
S: O(N^2)
Runtime: 31 ms, faster than 92.38% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.9 MB, less than 41.06% of Python3 online submissions for Spiral Matrix II.
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        # directions
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # direction index
        d = 0
        # number, start from 1 to n * n 
        x = 1 
        # position
        i, j = 0, 0
        while x <= n * n:
            # just fill
            ans[i][j] = x
            # next to fill
            ni, nj = i + ds[d][0], j + ds[d][1]
            if ni < 0 or ni >= n or nj < 0 or nj >= n or ans[ni][nj]:
                d = (d + 1) % 4
            i, j = i + ds[d][0], j + ds[d][1]
            x += 1    
        
        return ans         


'''
simulation, four directions
T: O(N^2)
S: O(N^2)

Runtime: 23 ms, faster than 99.20% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.9 MB, less than 41.01% of Python3 online submissions for Spiral Matrix II.
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        # directions
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # from 1 to n * n
        x = 1
        # fill numbers layer by layer
        for i in range((n + 1) // 2):
            # from left to right
            for j in range(i, n - i):
                ans[i][j] = x 
                x += 1
            # from top to bottom
            for r in range(i + 1, n - i):
                ans[r][n - i - 1] = x
                x += 1
            # from right to left
            for j in range(n - i - 2, i - 1, -1):
                ans[n - i - 1][j] = x
                x += 1
            # from bottom to top
            for r in range(n - i - 2, i, -1):
                ans[r][i] = x
                x += 1
        
        return ans         

