'''
DFS 

You are here!
Your runtime beats 69.61 % of python3 submissions.
You are here!
Your memory usage beats 17.66 % of python3 submissions.
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        @cache
        def dfs(currRow, currColumn, move):
            if move < 0:
                return 0
            if self.isOut(currRow, currColumn, m, n):
                return 1
            ways = 0
            for deltax, deltay in directions:
                nx, ny = currRow + deltax, currColumn + deltay
                ways += dfs(nx, ny, move - 1) % MOD

            return ways % MOD
        
        return dfs(startRow, startColumn, maxMove) 
    
    def isOut(self, x, y, m, n):
        return (x < 0 or y < 0 or x >= m or y >= n)

'''
# Do not forget MOD!
Input: 8
50
23
5
26
Output: 1590914794510
Expected: 914783380
'''