'''
DFS

执行用时：36 ms, 在所有 Python3 提交中击败了93.77% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了50.99% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])

        def infect(i, j):
            if i < 0 or i >= M or j < 0 or j >= N or board[i][j] != 'O':
                return
            board[i][j] = 'B'
            infect(i - 1, j)
            infect(i + 1, j)
            infect(i, j - 1)
            infect(i, j + 1)
        # change board "O" to "B"
        for i in range(M):
            infect(i, 0)
            infect(i, N - 1)
        for j in range(1, N - 1):
            infect(0, j)
            infect(M - 1, j)
        # recover "B" to "O", flip "O" to "X"
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

