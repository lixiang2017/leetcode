'''
Reverse DP

执行用时：32 ms, 在所有 Python3 提交中击败了97.89% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了84.04% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon) - 1
        col = len(dungeon[0]) - 1
        grid = [[0] * (col+1) for _ in range(row+1)]
        for i in range(row, -1, -1):
            if i == row:
                grid[i][col] = max(1 - dungeon[row][col], 1)
            else:
                grid[i][col] = max(1, grid[i+1][col] - dungeon[i][col])
            
        for j in range(col, -1, -1):
            if j < col:
                grid[row][j] = max(1, grid[row][j+1] - dungeon[row][j])
        
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                grid[r][c] = max(1, min(grid[r+1][c], grid[r][c+1]) - dungeon[r][c])
        
        return grid[0][0]
