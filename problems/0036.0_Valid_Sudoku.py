'''
Runtime: 282 ms, faster than 9.22% of Python3 online submissions for Valid Sudoku.
Memory Usage: 14 MB, less than 36.06% of Python3 online submissions for Valid Sudoku.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRowValid(b):
            return all(max(Counter(b[i][j] for j in range(9) if b[i][j] != '.').values() or [0]) <= 1 for i in range(9))
        
        def isColumnValid(b):
            return all(max(Counter(b[i][j] for i in range(9) if b[i][j] != '.').values() or [0]) <= 1 for j in range(9))
        
        def isSubboxValid(b):
            return all(
                max(Counter(b[i+di][j+dj] for di in range(3) for dj in range(3) if b[i+di][j+dj] != '.').values() or [0]) <= 1 
                for i in [0, 3, 6] for j in [0, 3, 6]
            )
        
        return isRowValid(board) and isColumnValid(board) and isSubboxValid(board)
        