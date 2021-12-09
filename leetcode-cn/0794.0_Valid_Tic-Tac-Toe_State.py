'''
由于棋盘比较小，xc == oc or xc == oc + 1 过滤之后就不用 win count再限制了。

执行用时：28 ms, 在所有 Python3 提交中击败了87.10% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了30.11% 的用户
通过测试用例：109 / 109
'''
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # x count, o count
        xc = sum ([1 for row in board for ch in row if ch == 'X'])
        oc = sum ([1 for row in board for ch in row if ch == 'O'])
        if not (xc == oc or xc == oc + 1):
            return False
        
        def get_win_count(ch):
            c = 0
            # row
            c += sum([1 if len(set(list(row))) == 1 and row[0] == ch else 0 for row in board])
            # col
            c += sum([1 if len(set(board[i][j] for i in range(3))) == 1 and board[0][j] == ch           
                        else 0 for j in range(3) ])
            # diag
            c += sum([1 if len(set(board[i][i] for i in range(3))) == 1 and board[0][0] == ch else 0])
            c += sum([1 if len(set(board[i][2 - i] for i in range(3))) == 1 and board[0][2] == ch else 0])
            return c
        # x win count, o win count
        xwc, owc = get_win_count('X'), get_win_count('O')
        if xwc and owc:
            return False
        if xwc and xc == oc:
            return False
        if owc and xc == oc + 1:
            return False

        return True

'''
["XXX",
 "OOX",
 "OOX"]
'''
