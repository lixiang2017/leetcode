'''

You are here!
Your runtime beats 98.88 % of python3 submissions.
You are here!
Your memory usage beats 44.63 % of python3 submissions.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidRow():
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])
            return True
        
        def isValidColumn():
            for j in range(9):
                seen = set()
                for i in range(9):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])
            return True  
        
        def isValidBox():
            # top left, start i, start j
            for si in [0, 3, 6]:
                for sj in [0, 3, 6]:
                    seen = set()
                    # delta i, delta j
                    for di in range(3):
                        for dj in range(3):
                            # new i, new j
                            ni, nj = si + di, sj + dj
                            if board[ni][nj] != '.':
                                if board[ni][nj] in seen:
                                    return False
                                else:
                                    seen.add(board[ni][nj])                            
            return True
    
        return isValidRow() and isValidColumn() and isValidBox()
        
