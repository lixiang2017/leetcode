'''
AC

'''
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        board[rMove][cMove] = color
        oposite = chr(ord('B') + ord('W') - ord(color))
        
        def checkVertical():
            # up
            i = rMove - 1
            if i >= 0:
                while i > 0 and board[i][cMove] == oposite:
                    i -= 1
                if board[i][cMove] == color and rMove - i >= 2:
                    return True
            # down
            i = rMove + 1
            if i <= 7:
                while i < 7 and board[i][cMove] == oposite:
                    i += 1
                if board[i][cMove] == color and i - rMove >= 2:
                    return True            
            return False
        
        def checkHorizontal():
            # left
            j = cMove - 1
            if j >= 0:
                while j > 0 and board[rMove][j] == oposite:
                    j -= 1
                if board[rMove][j] == color and cMove - j >= 2:
                    return True
            # right
            j = cMove + 1
            if j <= 7:
                while j < 7 and board[rMove][j] == oposite:
                    j += 1
                if board[rMove][j] == color and j - cMove >= 2:
                    return True
            return False

        
        def checkDiagonal():
            # top left
            i, j = rMove - 1,  cMove - 1
            if i >= 0 and j >= 0:
                while i > 0 and j > 0 and board[i][j] == oposite:
                    i -= 1
                    j -= 1
                if board[i][j] == color and cMove - j >= 2:
                    return True
            # bottom right
            i, j = rMove + 1,  cMove + 1
            if i <= 7 and j <= 7:
                while i < 7 and j < 7 and board[i][j] == oposite:
                    i += 1
                    j += 1
                if board[i][j] == color and j - cMove >= 2:
                    return True
            # top right
            i, j = rMove - 1,  cMove + 1
            if i >= 0 and j <= 7:
                while i > 0 and j < 7 and board[i][j] == oposite:
                    i -= 1
                    j += 1
                if board[i][j] == color and j - cMove >= 2:
                    return True            
            # bottom left
            i, j = rMove + 1,  cMove - 1
            if i <= 7 and j > 0:
                while i < 7 and j > 0 and board[i][j] == oposite:
                    i += 1
                    j -= 1
                if board[i][j] == color and cMove - j >= 2:
                    return True            
            
            return False
        
        
        return checkVertical() or checkHorizontal() or checkDiagonal()

