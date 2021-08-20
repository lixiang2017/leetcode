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


'''
You are here!
Your runtime beats 98.88 % of python3 submissions.
You are here!
Your memory usage beats 97.61 % of python3 submissions.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]
        for i in range(size):
            for j in range(size):
                curr = board[i][j]
                if curr == '.':
                    continue
                if curr in rows[i]:
                    return False
                else:
                    rows[i].add(curr)
                if curr in cols[j]:
                    return False
                else:
                    cols[j].add(curr)
                idx = (i // 3) * 3 + (j // 3)
                if curr in boxes[idx]:
                    return False
                else:
                    boxes[idx].add(curr)
        return True
    


'''
You are here!
Your runtime beats 98.88 % of python3 submissions.
You are here!
Your memory usage beats 72.08 % of python3 submissions.
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == '.':
                    continue
                if (curr, 'r', r) in seen:
                    return False
                if (curr, 'c', c) in seen:
                    return False
                if (curr, r // 3, c // 3) in seen:
                    return False
                seen[(curr, 'r', r) ] = True
                seen[(curr, 'c', c)] = True
                seen[(curr, r // 3, c // 3)] = True
                
        return True




      
