'''
T: O(2N + N^2) = O(N^2)
S: O(2N) = O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了29.01% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了90.84% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        haveSpace = False
        N = len(board)
        # row, column
        xr, xc = [0] * N, [0] * N
        o_row, o_column = [0] * N, [0] * N

        # check diagonal
        def check_diag(ch):
            cnt1 = cnt2 = 0
            for i in range(N):
                if ch == board[i][i]:
                    cnt1 += 1
                if ch == board[i][N - 1 - i]:
                    cnt2 += 1
            return N == max(cnt1, cnt2)

        if check_diag('X'):
            return 'X'
        elif check_diag('O'):
            return 'O'

        for i in range(N):
            for j in range(N):
                if ' ' == board[i][j]:
                    haveSpace = True
                elif 'O' == board[i][j]:
                    o_row[i] += 1
                    o_column[j] += 1
                elif 'X' == board[i][j]:
                    xr[i] += 1
                    xc[j] += 1
                # check
                if o_row[i] == N or o_column[j] == N:
                    return 'O'
                elif xr[i] == N or xc[j] == N:
                    return 'X'

        return ['Draw', 'Pending'][haveSpace]
