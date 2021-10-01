'''
Simulation

You are here!
Your runtime beats 23.60 % of python3 submissions.
You are here!
Your memory usage beats 34.50 % of python3 submissions.
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = len(moves)
        posa, posb = set(), set()
        # row, column
        ra, rb = [set() for _ in range(3)], [set() for _ in range(3)]
        ca, cb = [set() for _ in range(3)], [set() for _ in range(3)]
        
        for i in range(N):
            r, c = moves[i]
            # for A
            if not (i & 1):
                posa.add(tuple(moves[i]))
                ra[r].add(c)
                ca[c].add(r)
                # check
                if i >= 4:
                    if max(map(len, chain(ra, ca))) == 3 or \
                       ((0, 0) in posa and (1, 1) in posa and (2, 2) in posa) or \
                       ((0, 2) in posa and (1, 1) in posa and (2, 0) in posa):
                        return 'A'
            else:  # for B
                posb.add(tuple(moves[i]))
                rb[r].add(c)
                cb[c].add(r)   
                # check
                if i >= 5:
                    if max(map(len, chain(rb, cb))) == 3 or \
                       ((0, 0) in posb and (1, 1) in posb and (2, 2) in posb) or \
                       ((0, 2) in posb and (1, 1) in posb and (2, 0) in posb):
                        return 'B'

        return 'Draw' if 9 == N else 'Pending'


'''
因为 You can assume that moves is valid (It follows the rules of Tic-Tac-Toe)
最后检查棋盘结果即可。中间不必检查。

You are here!
Your runtime beats 52.17 % of python3 submissions.
You are here!
Your memory usage beats 34.50 % of python3 submissions.
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = len(moves)
        posa, posb = set(), set()
        # row, column
        ra, rb = [set() for _ in range(3)], [set() for _ in range(3)]
        ca, cb = [set() for _ in range(3)], [set() for _ in range(3)]
        
        for i in range(N):
            r, c = moves[i]
            # for A
            if not (i & 1):
                posa.add(tuple(moves[i]))
                ra[r].add(c)
                ca[c].add(r)
            else:  # for B
                posb.add(tuple(moves[i]))
                rb[r].add(c)
                cb[c].add(r)          
        # check
        if max(map(len, chain(ra, ca))) == 3 or \
           ((0, 0) in posa and (1, 1) in posa and (2, 2) in posa) or \
           ((0, 2) in posa and (1, 1) in posa and (2, 0) in posa):
            return 'A'                
        elif max(map(len, chain(rb, cb))) == 3 or \
           ((0, 0) in posb and (1, 1) in posb and (2, 2) in posb) or \
           ((0, 2) in posb and (1, 1) in posb and (2, 0) in posb):
            return 'B'

        return 'Draw' if 9 == N else 'Pending'



'''
bitwise

You are here!
Your runtime beats 33.76 % of python3 submissions.
You are here!
Your memory usage beats 88.25 % of python3 submissions.
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a = sum(1 << (3 * x + y) for x, y in moves[::2])
        b = sum(1 << (3 * x + y) for x, y in moves[1::2])
        
        check = [0b111000000, 0b000111000, 0b000000111,
                0b100100100, 0b010010010, 0b001001001,
                0b100010001, 0b001010100]
        for c in check:
            if a & c == c: return 'A'
            if b & c == c: return 'B'
        
        return ['Pending', 'Draw'][9 == len(moves)]

'''
ref:
https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game/solution/jian-dan-si-xing-jie-99-shu-du-mo-fang-j-oo52/

You are here!
Your runtime beats 13.44 % of python3 submissions.
You are here!
Your memory usage beats 96.40 % of python3 submissions.
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 横竖斜的和均为15
        SUDOKU = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        if 15 in [sum(k) for k in combinations([SUDOKU[i][j] for i, j in moves[::2]], 3)]: return 'A'
        if 15 in [sum(k) for k in combinations([SUDOKU[i][j] for i, j in moves[1::2]], 3)]: return 'B'
        return ['Pending', 'Draw'][9 == len(moves)]
                
